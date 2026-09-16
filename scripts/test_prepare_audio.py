"""Synthetic-only tests; no event media, network, ASR or third-party Python modules."""

from contextlib import ExitStack, redirect_stderr, redirect_stdout
import hashlib
import io
import json
from pathlib import Path
import shutil
import struct
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import wave

import prepare_audio as audio


def write_wav(path, samples=513, rate=16000, channels=1, width=2):
    with wave.open(str(path), "wb") as handle:
        handle.setparams((channels, width, rate, 0, "NONE", "not compressed"))
        if width == 2:
            # Nonzero boundary samples and internal silence, without utterances.
            data = [((index * 73) % 16000 - 8000) if index % 7 else 0
                    for index in range(samples * channels)]
            if data:
                data[0], data[-1] = 12000, -12000
            handle.writeframes(struct.pack(f"<{len(data)}h", *data))
        else:
            handle.writeframes(bytes(samples * channels * width))


def snapshot(directory):
    if not directory.exists():
        return None
    return {p.name: (p.read_bytes(), p.stat().st_mtime_ns)
            for p in directory.iterdir() if p.is_file()}


class Fixture(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="prepare-audio-test-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.parts = self.root / "parts"
        self.parts.mkdir()
        self.wav = self.parts / "part-01.wav"
        write_wav(self.wav)
        self.source = self.root / "original.wav"
        shutil.copyfile(self.wav, self.source)
        self.output = self.root / "compact"

    def prepare(self, **kwargs):
        return audio.prepare(self.source, self.parts, self.output, **kwargs)

    def fake_tools(self):
        stack = ExitStack()
        self.addCleanup(stack.close)
        stack.enter_context(patch.object(audio, "tool_versions", return_value={
            "ffmpeg": "ffmpeg synthetic test", "ffprobe": "ffprobe synthetic test",
        }))

        def encode(source, destination, bitrate):
            destination.write_bytes(f"synthetic-opus-{bitrate}".encode())

        def inspect(path, samples):
            return {"file": path.name, **audio.fingerprint(path), "decoded_pcm_samples": samples}

        encoder = stack.enter_context(patch.object(audio, "encode", side_effect=encode))
        stack.enter_context(patch.object(audio, "inspect_encoded", side_effect=inspect))
        return encoder


class InputTests(Fixture):
    def test_sample_bound_and_offsets(self):
        self.assertEqual(audio.FULL_SAMPLES, 28_800_000)
        write_wav(self.wav, 640)
        write_wav(self.parts / "part-02.wav", 513)
        with patch.object(audio, "FULL_SAMPLES", 640):
            paths, records = audio.read_parts(self.parts)
        self.assertEqual(len(paths), 2)
        self.assertEqual(records[0]["start_sample"], 0)
        self.assertEqual(records[0]["end_sample"], 640)
        self.assertEqual(records[1]["start_sample"], 640)
        self.assertEqual(records[1]["end_sample"], 1153)
        self.assertEqual(records[1]["end_seconds"], 1153 / 16000)
        self.assertEqual(records[0]["wav"]["sha256"], hashlib.sha256(self.wav.read_bytes()).hexdigest())

    def test_all_eighteen_offsets_without_large_fixtures(self):
        for number in range(1, 19):
            write_wav(self.parts / f"part-{number:02}.wav", 640 if number < 18 else 319)
        with patch.object(audio, "FULL_SAMPLES", 640):
            _, records = audio.read_parts(self.parts)
        self.assertEqual(records[-1]["start_sample"], 17 * 640)
        self.assertEqual(records[-1]["end_sample"], 17 * 640 + 319)

    def test_invalid_formats(self):
        for options in ({"rate": 48000}, {"channels": 2}, {"width": 1}, {"samples": 0}):
            with self.subTest(options=options):
                write_wav(self.wav, **options)
                with self.assertRaises(audio.AudioError):
                    audio.read_parts(self.parts)

    def test_oversized_final_part(self):
        with patch.object(audio, "FULL_SAMPLES", 512), self.assertRaises(audio.AudioError):
            audio.read_parts(self.parts)

    def test_short_nonfinal_part(self):
        write_wav(self.parts / "part-02.wav")
        with self.assertRaisesRegex(audio.AudioError, "Only the final"):
            audio.read_parts(self.parts)

    def test_missing_and_noncanonical_parts(self):
        for name in ("part-02.wav", "part-00.wav", "part-1.wav", "other.wav", "part-01.WAV"):
            with self.subTest(name=name):
                changed = self.parts / name
                self.wav.rename(changed)
                try:
                    with self.assertRaises(audio.AudioError):
                        audio.read_parts(self.parts)
                finally:
                    changed.rename(self.wav)

    def test_truncated_payload(self):
        self.wav.write_bytes(self.wav.read_bytes()[:-2])
        with self.assertRaisesRegex(audio.AudioError, "truncated"):
            audio.read_parts(self.parts)

    def test_invalid_wav(self):
        self.wav.write_bytes(b"not a wave")
        with self.assertRaisesRegex(audio.AudioError, "Invalid"):
            audio.read_parts(self.parts)

    def test_input_symlink(self):
        self.wav.unlink()
        self.wav.symlink_to(self.source)
        with self.assertRaisesRegex(audio.AudioError, "non-symlink"):
            audio.read_parts(self.parts)


class PreparationTests(Fixture):
    def test_complete_rerun_and_check_are_read_only(self):
        encoder = self.fake_tools()
        inputs = self.source.read_bytes(), self.wav.read_bytes()
        action, manifest = self.prepare()
        self.assertEqual(action, "prepared")
        self.assertEqual(manifest["original"]["file"], "original.wav")
        self.assertEqual(manifest["original"]["sha256"], hashlib.sha256(inputs[0]).hexdigest())
        self.assertEqual(manifest["parts"][0]["encoded"]["decoded_pcm_samples"], 513)
        self.assertNotIn(str(self.root), (self.output / "manifest.json").read_text())
        before = snapshot(self.output)
        with patch.object(Path, "mkdir", side_effect=AssertionError("write in check")), \
                patch.object(audio.os, "link", side_effect=AssertionError("write in check")), \
                patch.object(audio.tempfile, "TemporaryDirectory", side_effect=AssertionError("write in check")):
            self.assertEqual(self.prepare()[0], "verified")
            self.assertEqual(self.prepare(check=True)[0], "verified")
        self.assertEqual(encoder.call_count, 1)
        self.assertEqual(snapshot(self.output), before)
        self.assertEqual((self.source.read_bytes(), self.wav.read_bytes()), inputs)

    def test_no_manifest_check_creates_nothing(self):
        with self.assertRaisesRegex(audio.AudioError, "No completed manifest"):
            self.prepare(check=True)
        self.assertFalse(self.output.exists())

    def test_every_conflict_is_preflighted(self):
        encoder = self.fake_tools()
        for name in ("part-01.opus", "part-18.opus", "notes.txt", ".prepare-audio-abandoned"):
            with self.subTest(name=name):
                self.output.mkdir(exist_ok=True)
                artifact = self.output / name
                artifact.write_bytes(b"preserve")
                with self.assertRaisesRegex(audio.AudioError, "Conflicting or partial"):
                    self.prepare()
                self.assertEqual(artifact.read_bytes(), b"preserve")
                artifact.unlink()
        encoder.assert_not_called()

    def test_corrupt_manifest_and_incomplete_inventory(self):
        encoder = self.fake_tools()
        self.prepare()
        manifest = self.output / "manifest.json"
        manifest.write_text("{broken")
        with self.assertRaisesRegex(audio.AudioError, "Invalid manifest JSON"):
            self.prepare()
        (self.output / "part-01.opus").unlink()
        with self.assertRaisesRegex(audio.AudioError, "Conflicting or partial"):
            self.prepare()
        self.assertEqual(encoder.call_count, 1)

    def test_changed_inputs_outputs_settings_and_tools_refused(self):
        encoder = self.fake_tools()
        self.prepare()
        for path in (self.source, self.wav, self.output / "part-01.opus", self.output / "manifest.json"):
            original = path.read_bytes()
            if path.suffix == ".json":
                changed = json.loads(original)
                changed["parts"][0]["end_sample"] += 1
                path.write_text(json.dumps(changed))
            elif path.suffix == ".wav":
                data = bytearray(original)
                data[-1] ^= 1
                path.write_bytes(data)
            else:
                path.write_bytes(original + b"changed")
            before = snapshot(self.output)
            with self.subTest(path=path.name), self.assertRaises(audio.AudioError):
                self.prepare(check=True)
            self.assertEqual(snapshot(self.output), before)
            path.write_bytes(original)
        with self.assertRaisesRegex(audio.AudioError, "differ"):
            self.prepare(bitrate=24)
        with patch.object(audio, "tool_versions", return_value={"ffmpeg": "changed"}), \
                self.assertRaisesRegex(audio.AudioError, "differ"):
            self.prepare()
        self.assertEqual(encoder.call_count, 1)

    def test_late_encode_failure_cleans_all_temporary_files(self):
        encoder = self.fake_tools()
        write_wav(self.wav, 640)
        write_wav(self.parts / "part-02.wav", 513)

        def fail_second(source, destination, bitrate):
            destination.write_bytes(b"partial")
            if source.name == "part-02.wav":
                raise audio.AudioError("synthetic failure")

        encoder.side_effect = fail_second
        with patch.object(audio, "FULL_SAMPLES", 640), self.assertRaises(audio.AudioError):
            self.prepare()
        self.assertEqual(list(self.output.iterdir()), [])

    def test_decode_failure_cleans_temporary_files(self):
        self.fake_tools()
        with patch.object(audio, "inspect_encoded", side_effect=audio.AudioError("decode failed")), \
                self.assertRaises(audio.AudioError):
            self.prepare()
        self.assertEqual(list(self.output.iterdir()), [])

    def test_input_drift_prevents_promotion(self):
        encoder = self.fake_tools()

        def drift(source, destination, bitrate):
            destination.write_bytes(b"synthetic opus")
            self.source.write_bytes(b"changed original")

        encoder.side_effect = drift
        with self.assertRaisesRegex(audio.AudioError, "Original changed"):
            self.prepare()
        self.assertEqual(list(self.output.iterdir()), [])

    def test_concurrent_output_conflict_not_overwritten(self):
        encoder = self.fake_tools()

        def drift(source, destination, bitrate):
            destination.write_bytes(b"synthetic opus")
            (self.output / "part-01.opus").write_bytes(b"another writer")

        encoder.side_effect = drift
        with self.assertRaisesRegex(audio.AudioError, "Output changed"):
            self.prepare()
        self.assertEqual(snapshot(self.output).keys(), {"part-01.opus"})
        self.assertEqual((self.output / "part-01.opus").read_bytes(), b"another writer")

    def test_promotion_refuses_racing_file_and_leaves_no_manifest(self):
        self.fake_tools()
        real_link = audio.os.link

        def collide(source, destination, **kwargs):
            destination.write_bytes(b"racing writer")
            return real_link(source, destination, **kwargs)

        with patch.object(audio.os, "link", side_effect=collide), self.assertRaises(FileExistsError):
            self.prepare()
        self.assertEqual((self.output / "part-01.opus").read_bytes(), b"racing writer")
        self.assertFalse((self.output / "manifest.json").exists())
        with self.assertRaisesRegex(audio.AudioError, "partial"):
            self.prepare()

    def test_directory_overlap(self):
        for output in (self.source, self.parts, self.parts / "nested", self.root):
            with self.subTest(output=output.name), self.assertRaises(audio.AudioError):
                audio.prepare(self.source, self.parts, output)

    def test_symlink_destinations_and_ancestors(self):
        elsewhere = self.root / "elsewhere"
        elsewhere.mkdir()
        self.output.symlink_to(elsewhere, target_is_directory=True)
        for output in (self.output, self.output / "child"):
            with self.subTest(output=output.name), self.assertRaisesRegex(audio.AudioError, "symlink"):
                audio.prepare(self.source, self.parts, output)
        self.assertEqual(list(elsewhere.iterdir()), [])
        self.output.unlink()
        self.output.mkdir()
        (self.output / "part-01.opus").symlink_to(elsewhere / "missing")
        with self.assertRaisesRegex(audio.AudioError, "symlink"):
            self.prepare()

    def test_parent_traversal_rejected(self):
        with self.assertRaisesRegex(audio.AudioError, "must not contain"):
            audio.output_path(self.root / "unused" / ".." / "compact")


class ToolTests(Fixture):
    def test_encoding_settings(self):
        with patch.object(audio, "run_tool") as run:
            audio.encode(self.wav, self.output / "part-01.opus", 48)
        command = run.call_args.args[0]
        for option, expected in (("-b:a", "48k"), ("-application", "audio"),
                                 ("-frame_duration", "20"), ("-compression_level", "10"),
                                 ("-vbr", "on"), ("-map_metadata", "-1"),
                                 ("-map_chapters", "-1"), ("-ar", "16000")):
            self.assertEqual(command[command.index(option) + 1], expected)
        self.assertNotIn("-af", command)
        self.assertNotIn("-ss", command)
        self.assertNotIn("-t", command)
        self.assertIn("-n", command)

    def test_subprocess_deadline_and_redaction(self):
        with patch.object(audio.subprocess, "run", side_effect=subprocess.TimeoutExpired("private", 120)) as run:
            with self.assertRaisesRegex(audio.AudioError, "deadline"):
                audio.run_tool(["ffmpeg", "private"])
        self.assertEqual(run.call_args.kwargs["timeout"], 120)
        self.assertEqual(run.call_args.kwargs["stderr"], subprocess.DEVNULL)

    def test_streaming_decoder_timeout(self):
        real_popen = subprocess.Popen

        def stalled(command, **kwargs):
            return real_popen([sys.executable, "-c", "import time; time.sleep(10)"], **kwargs)

        with patch.object(audio.subprocess, "Popen", side_effect=stalled), \
                patch.object(audio, "TIMEOUT", 0.1), \
                self.assertRaisesRegex(audio.AudioError, "deadline"):
            audio.decoded_samples(self.wav, 513)

    def test_streaming_decoder_rejects_short_and_long_counts(self):
        real_popen = subprocess.Popen
        for size in (1024, 1028):
            def wrong_size(command, **kwargs):
                return real_popen([sys.executable, "-c", f"import sys; sys.stdout.buffer.write(bytes({size}))"], **kwargs)
            with self.subTest(size=size), patch.object(audio.subprocess, "Popen", side_effect=wrong_size), \
                    self.assertRaises(audio.AudioError):
                audio.decoded_samples(self.wav, 513)

    def test_codec_channels_metadata_chapters_and_size(self):
        path = self.root / "part-01.opus"
        path.write_bytes(b"synthetic")
        valid = {"streams": [{"codec_name": "opus", "codec_type": "audio", "channels": 1,
                               "tags": {"encoder": "test"}}]}
        invalid = [
            {"streams": [{"codec_name": "vorbis", "codec_type": "audio", "channels": 1}]},
            {"streams": [{"codec_name": "opus", "codec_type": "audio", "channels": 2}]},
            {**valid, "format": {"tags": {"title": "private metadata"}}},
            {**valid, "chapters": [{"id": 1}]},
            {"streams": valid["streams"] * 2},
        ]
        for info in invalid:
            with self.subTest(info=info), patch.object(audio, "run_tool", return_value=json.dumps(info)), \
                    self.assertRaises(audio.AudioError):
                audio.inspect_encoded(path, 513)
        with patch.object(audio, "run_tool", return_value=json.dumps(valid)), \
                patch.object(audio, "decoded_samples", return_value=513):
            self.assertEqual(audio.inspect_encoded(path, 513)["decoded_pcm_samples"], 513)
        with patch.object(audio, "MAX_BYTES", len(path.read_bytes())), \
                self.assertRaisesRegex(audio.AudioError, "below 20 MiB"):
            audio.inspect_encoded(path, 513)

    def test_cli_error_is_path_free_and_has_recovery(self):
        stdout, stderr = io.StringIO(), io.StringIO()
        with redirect_stdout(stdout), redirect_stderr(stderr):
            status = audio.main(["--source", str(self.root / "private-missing.wav"),
                                 "--parts", str(self.parts), "--output", str(self.output), "--check"])
        self.assertEqual(status, 1)
        self.assertEqual(stdout.getvalue(), "")
        self.assertIn("ERROR:", stderr.getvalue())
        self.assertIn("ACTION REQUIRED:", stderr.getvalue())
        self.assertNotIn("private-missing", stderr.getvalue())
        self.assertNotIn(str(self.root), stderr.getvalue())
        self.assertNotIn("\x1b", stderr.getvalue())

    def test_cli_interrupt(self):
        stdout, stderr = io.StringIO(), io.StringIO()
        with patch.object(audio, "prepare", side_effect=KeyboardInterrupt), \
                redirect_stdout(stdout), redirect_stderr(stderr):
            status = audio.main(["--source", str(self.source), "--parts", str(self.parts),
                                 "--output", str(self.output)])
        self.assertEqual(status, 130)
        self.assertEqual(stdout.getvalue(), "")
        self.assertIn("Interrupted", stderr.getvalue())


@unittest.skipUnless(shutil.which("ffmpeg") and shutil.which("ffprobe"), "ffmpeg/ffprobe not installed")
class FFmpegIntegrationTests(Fixture):
    def test_padding_at_tiny_and_frame_boundary_lengths(self):
        for samples in (319, 320, 321, 513, 16001):
            with self.subTest(samples=samples):
                write_wav(self.wav, samples)
                output = self.root / f"compact-{samples}"
                _, manifest = audio.prepare(self.source, self.parts, output)
                self.assertEqual(manifest["parts"][0]["encoded"]["decoded_pcm_samples"], samples)
                self.assertEqual(audio.prepare(self.source, self.parts, output, check=True)[0], "verified")

    def test_sub_resampler_length_requires_exact_decode_or_refusal(self):
        write_wav(self.wav, 1)
        encoded = self.root / "tiny.opus"
        audio.encode(self.wav, encoded, 32)
        # Independent tiny decode oracle: some ffmpeg resamplers emit zero
        # samples here. Refusal, not manufactured padding, is the safe result.
        decoded = subprocess.run([
            "ffmpeg", "-v", "error", "-nostdin", "-i", str(encoded),
            "-ar", "16000", "-c:a", "pcm_s16le", "-f", "s16le", "pipe:1",
        ], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, check=True, timeout=120)
        if len(decoded.stdout) == 2:
            _, manifest = self.prepare()
            self.assertEqual(manifest["parts"][0]["encoded"]["decoded_pcm_samples"], 1)
        else:
            with self.assertRaisesRegex(audio.AudioError, "sample count"):
                self.prepare()
            self.assertEqual(list(self.output.iterdir()), [])

    def test_source_metadata_is_not_retained(self):
        tagged = self.root / "tagged.wav"
        subprocess.run([
            "ffmpeg", "-v", "error", "-nostdin", "-n", "-i", str(self.wav),
            "-metadata", "title=SYNTHETIC_PRIVATE_TITLE", "-metadata", "artist=SYNTHETIC_ARTIST",
            "-c:a", "pcm_s16le", str(tagged),
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, timeout=120)
        shutil.copyfile(tagged, self.wav)
        self.prepare()
        self.assertEqual(self.prepare(check=True)[0], "verified")
        for path in self.output.iterdir():
            self.assertNotIn(b"SYNTHETIC_PRIVATE_TITLE", path.read_bytes())
            self.assertNotIn(b"SYNTHETIC_ARTIST", path.read_bytes())

    def test_first_last_parts_hashes_reproducibility_and_check(self):
        write_wav(self.wav, 640)
        write_wav(self.parts / "part-02.wav", 513)
        inputs = self.source.read_bytes(), self.wav.read_bytes()
        with patch.object(audio, "FULL_SAMPLES", 640):
            _, manifest = self.prepare()
            before = snapshot(self.output)
            self.assertEqual(self.prepare(check=True)[0], "verified")
            self.assertEqual(self.prepare()[0], "verified")
            self.assertEqual(snapshot(self.output), before)
            second = self.root / "second"
            audio.prepare(self.source, self.parts, second)
        self.assertEqual((self.source.read_bytes(), self.wav.read_bytes()), inputs)
        for path in self.output.iterdir():
            self.assertEqual(path.read_bytes(), (second / path.name).read_bytes())
        for record, count in zip(manifest["parts"], (640, 513)):
            encoded = record["encoded"]
            data = (self.output / encoded["file"]).read_bytes()
            self.assertEqual(encoded["sha256"], hashlib.sha256(data).hexdigest())
            self.assertEqual(encoded["bytes"], len(data))
            self.assertEqual(encoded["decoded_pcm_samples"], count)
        self.assertEqual(manifest["total_pcm_samples"], 1153)

    def test_changed_encoded_bytes_are_rejected(self):
        self.prepare()
        path = self.output / "part-01.opus"
        path.write_bytes(path.read_bytes() + b"modified")
        before = snapshot(self.output)
        with self.assertRaises(audio.AudioError):
            self.prepare(check=True)
        self.assertEqual(snapshot(self.output), before)

    def test_all_bitrates(self):
        for bitrate in (24, 32, 48):
            with self.subTest(bitrate=bitrate):
                _, manifest = audio.prepare(self.source, self.parts, self.root / str(bitrate), bitrate)
                self.assertEqual(manifest["settings"]["bitrate_kbps"], bitrate)


if __name__ == "__main__":
    unittest.main()
