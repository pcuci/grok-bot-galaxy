#!/usr/bin/env python3
"""Prepare verified, lossy Opus derivatives without changing source bytes.

Python 3.10+ and installed ffmpeg/ffprobe (with libopus) are required. This CLI
owns subprocess output: raw media, metadata and child diagnostics are never
printed. Exit codes: 0 verified/prepared, 1 refused/failed, 2 CLI usage, 130
interrupted. Offsets describe the supplied WAV sequence, not an independently
verified segmentation of the original. No ASR quality equivalence is claimed.
Extremely short clips may be refused if ffmpeg's resampler drops samples;
validation never pads or trims a decode to force a matching count.
"""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import threading
import wave

RATE = 16000
FULL_SAMPLES = 1800 * RATE
MAX_BYTES = 20 * 1024 * 1024
TIMEOUT = 120
BLOCK = 64 * 1024
RECOVERY = (
    "Inspect existing artifacts; restore the matching inputs/settings or choose "
    "a new empty output directory. A partial run without manifest.json is not "
    "complete; preserve it for review. Nothing is automatically overwritten."
)


class AudioError(Exception):
    """A safe, path-free operator diagnostic."""


def fingerprint(path):
    if path.is_symlink() or not path.is_file():
        raise AudioError("Expected a regular, non-symlink file.")
    digest = hashlib.sha256()
    size = 0
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(BLOCK), b""):
            digest.update(block)
            size += len(block)
    return {"bytes": size, "sha256": digest.hexdigest()}


def output_path(path):
    # Reject symlinks before resolving anything, including dangling links and
    # ancestors. Reject '..' rather than normalizing away a symlink traversal.
    if ".." in path.parts:
        raise AudioError("Output path must not contain '..'.")
    path = path.absolute()
    for component in (*reversed(path.parents), path):
        if component.is_symlink():
            raise AudioError("Output directory or ancestor is a symlink.")
        if component.exists() and not component.is_dir():
            raise AudioError("Output directory collides with a file.")
    return path


def output_entries(path):
    output_path(path)
    if not path.exists():
        return set()
    entries = list(path.iterdir())
    if any(item.is_symlink() for item in entries):
        raise AudioError("Output contains a symlink; refusing destination escape.")
    return {item.name for item in entries}


def read_parts(directory):
    candidates = [p for p in directory.iterdir() if p.suffix.lower() == ".wav"]
    if not candidates or any(not re.fullmatch(r"part-[0-9]+\.wav", p.name)
                             for p in candidates):
        raise AudioError("Parts must be named part-01.wav onward, without gaps.")
    paths = sorted(candidates, key=lambda p: int(p.stem[5:]))
    records = []
    offset = 0
    for number, path in enumerate(paths, 1):
        if path.name != f"part-{number:02}.wav":
            raise AudioError("Parts must be contiguous and canonically numbered from 01.")
        identity = fingerprint(path)
        try:
            with wave.open(str(path), "rb") as audio:
                if (audio.getnchannels(), audio.getframerate(), audio.getsampwidth(),
                        audio.getcomptype()) != (1, RATE, 2, "NONE"):
                    raise AudioError("WAV inputs must be mono 16 kHz signed 16-bit PCM.")
                samples = audio.getnframes()
                if not 0 < samples <= FULL_SAMPLES:
                    raise AudioError("Every WAV must contain 1 through 28,800,000 samples.")
                if number < len(paths) and samples != FULL_SAMPLES:
                    raise AudioError("Only the final WAV may be shorter than 1800 seconds.")
                size = 0
                for block in iter(lambda: audio.readframes(BLOCK // 2), b""):
                    size += len(block)
                if size != samples * 2:
                    raise AudioError("WAV PCM payload is truncated or not sample-aligned.")
        except (wave.Error, EOFError) as error:
            raise AudioError("Invalid or unsupported PCM WAV input.") from error
        if fingerprint(path) != identity:
            raise AudioError("A WAV changed during inspection.")
        records.append({
            "wav": {"file": path.name, **identity},
            "pcm_samples": samples,
            "start_sample": offset,
            "end_sample": offset + samples,
            "start_seconds": offset / RATE,
            "end_seconds": (offset + samples) / RATE,
        })
        offset += samples
    return paths, records


def run_tool(command):
    try:
        result = subprocess.run(command, stdin=subprocess.DEVNULL,
                                stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                                timeout=TIMEOUT, check=True)
    except subprocess.TimeoutExpired as error:
        raise AudioError("Media tool exceeded its 120-second deadline.") from error
    except (OSError, subprocess.CalledProcessError) as error:
        raise AudioError("Media tool unavailable or failed; check ffmpeg/ffprobe and libopus.") from error
    return result.stdout


def tool_versions():
    versions = {}
    for tool in ("ffmpeg", "ffprobe"):
        report = run_tool([tool, "-version"])
        lines = report.decode("utf-8").splitlines()
        if not lines or not lines[0].startswith(f"{tool} version "):
            raise AudioError("Unrecognized media-tool version report.")
        versions[tool] = {
            "version": lines[0],
            # Build configuration can contain local paths; retain only its hash.
            "version_report_sha256": hashlib.sha256(report).hexdigest(),
        }
    return versions


def decoded_samples(path, expected):
    command = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-nostdin",
               "-xerror", "-protocol_whitelist", "file,pipe", "-i", str(path),
               "-map", "0:a:0", "-ar", str(RATE), "-c:a", "pcm_s16le",
               "-f", "s16le", "pipe:1"]
    expired = threading.Event()
    with subprocess.Popen(command, stdin=subprocess.DEVNULL,
                          stdout=subprocess.PIPE, stderr=subprocess.DEVNULL) as process:
        def expire():
            expired.set()
            try:
                process.kill()
            except ProcessLookupError:
                pass

        timer = threading.Timer(TIMEOUT, expire)
        timer.daemon = True
        timer.start()
        size = 0
        try:
            # Discard PCM as it arrives: memory is bounded and no raw decode is
            # stored. The watchdog also bounds a stalled pipe read or child exit.
            for block in iter(lambda: process.stdout.read(BLOCK), b""):
                size += len(block)
                if size > expected * 2:
                    raise AudioError("Decoded audio exceeds the input sample count.")
            status = process.wait(timeout=TIMEOUT)
            if expired.is_set():
                raise AudioError("Audio decode exceeded its 120-second deadline.")
            if status or size != expected * 2:
                raise AudioError("Full decode failed or did not preserve the exact PCM sample count.")
        finally:
            timer.cancel()
            if process.poll() is None:
                process.kill()
            process.wait(timeout=TIMEOUT)
    return size // 2


def inspect_encoded(path, samples):
    if path.is_symlink() or not path.is_file() or not 0 < path.stat().st_size < MAX_BYTES:
        raise AudioError("Encoded file must be regular, nonempty and below 20 MiB.")
    identity = fingerprint(path)
    try:
        info = json.loads(run_tool([
            "ffprobe", "-v", "error", "-protocol_whitelist", "file,pipe",
            "-show_entries",
            "stream=codec_name,codec_type,channels:stream_tags:format_tags:chapter=id",
            "-of", "json", str(path),
        ]))
        streams = info.get("streams", [])
        if (len(streams) != 1 or streams[0].get("codec_name") != "opus"
                or streams[0].get("codec_type") != "audio"
                or streams[0].get("channels") != 1 or info.get("chapters")):
            raise AudioError("Encoded file must contain only one mono Opus stream, without chapters.")
        for section in [*streams, info.get("format", {})]:
            if any(key.lower() != "encoder" for key in section.get("tags", {})):
                raise AudioError("Encoded file contains non-encoder metadata.")
    except (ValueError, TypeError, AttributeError) as error:
        raise AudioError("Invalid ffprobe result.") from error
    count = decoded_samples(path, samples)
    if fingerprint(path) != identity:
        raise AudioError("Encoded file changed during validation.")
    return {"file": path.name, **identity, "decoded_pcm_samples": count}


def encode(source, destination, bitrate):
    run_tool([
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-nostdin", "-n",
        "-xerror", "-protocol_whitelist", "file,pipe", "-i", str(source),
        "-map", "0:a:0", "-map_metadata", "-1", "-map_chapters", "-1",
        "-c:a", "libopus", "-ar", str(RATE), "-ac", "1",
        "-b:a", f"{bitrate}k", "-application", "audio", "-frame_duration", "20",
        "-compression_level", "10", "-vbr", "on", "-threads", "1",
        "-fflags", "+bitexact", "-flags:a", "+bitexact",
        "-fs", str(MAX_BYTES), "-f", "opus", str(destination),
    ])


def confirm_inputs(source, paths, manifest):
    if fingerprint(source) != {k: manifest["original"][k] for k in ("bytes", "sha256")}:
        raise AudioError("Original changed during preparation or validation.")
    for path, record in zip(paths, manifest["parts"]):
        if fingerprint(path) != {k: record["wav"][k] for k in ("bytes", "sha256")}:
            raise AudioError("WAV changed during preparation or validation.")
    current = {p.name for p in paths[0].parent.iterdir() if p.suffix.lower() == ".wav"}
    if current != {p.name for p in paths}:
        raise AudioError("WAV inventory changed during preparation or validation.")


def prepare(source, parts, output, bitrate=32, check=False):
    if bitrate not in (24, 32, 48):
        raise AudioError("Bitrate must be 24, 32 or 48 kbps.")
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", source.name):
        raise AudioError("Original must have a simple, share-safe basename.")
    original = {"file": source.name, **fingerprint(source)}
    source = source.resolve(strict=True)
    parts = parts.resolve(strict=True)
    output = output_path(output)
    if (output == parts or output in parts.parents or parts in output.parents
            or output == source or output in source.parents):
        raise AudioError("Output must not overlap original or parts locations.")
    paths, records = read_parts(parts)
    names = {f"part-{number:02}.opus" for number in range(1, len(paths) + 1)}
    entries = output_entries(output)
    complete = "manifest.json" in entries
    if entries and (not complete or entries != names | {"manifest.json"}):
        raise AudioError("Conflicting or partial output directory; refusing to encode.")
    if check and not complete:
        raise AudioError("No completed manifest.json to check.")
    manifest = {
        "schema_version": 1,
        "original": original,
        "tools": tool_versions(),
        "settings": {
            "codec": "libopus", "container": "opus", "bitrate_kbps": bitrate,
            "application": "audio", "frame_duration_ms": 20,
            "compression_level": 10, "vbr": "on", "channels": 1,
            "pcm_sample_rate_hz": RATE, "pcm_format": "s16le", "threads": 1,
            "bitexact": True, "map_metadata": -1, "map_chapters": -1,
            "max_encoded_bytes_exclusive": MAX_BYTES,
        },
        "limitations": [
            "Lossy listening derivative; prefer original PCM for ASR. Recognition parity is unverified.",
            "Offsets are cumulative supplied-WAV samples; original-to-WAV segmentation is not verified here.",
            "Byte reproducibility is limited to the same toolchain and settings.",
        ],
        "total_pcm_samples": sum(record["pcm_samples"] for record in records),
        "parts": records,
    }
    if complete:
        manifest_path = output / "manifest.json"
        if not manifest_path.is_file() or manifest_path.stat().st_size > MAX_BYTES:
            raise AudioError("Invalid manifest file.")
        try:
            saved = json.loads(manifest_path.read_text(encoding="utf-8"))
        except (ValueError, UnicodeError) as error:
            raise AudioError("Invalid manifest JSON.") from error
        for number, record in enumerate(records, 1):
            record["encoded"] = inspect_encoded(output / f"part-{number:02}.opus",
                                                record["pcm_samples"])
        if saved != manifest:
            raise AudioError("Manifest, input/output fingerprints, settings or tool versions differ.")
        confirm_inputs(source, paths, manifest)
        if output_entries(output) != entries:
            raise AudioError("Output inventory changed during validation.")
        return "verified", manifest

    output.mkdir(parents=True, exist_ok=True)
    output_path(output)
    with tempfile.TemporaryDirectory(prefix=".prepare-audio-", dir=output) as directory:
        temporary = Path(directory)
        for number, (path, record) in enumerate(zip(paths, records), 1):
            target = temporary / f"part-{number:02}.opus"
            encode(path, target, bitrate)
            record["encoded"] = inspect_encoded(target, record["pcm_samples"])
        confirm_inputs(source, paths, manifest)
        if output_entries(output) != {temporary.name}:
            raise AudioError("Output changed before promotion; refusing to overwrite.")
        manifest_path = temporary / "manifest.json"
        with manifest_path.open("x", encoding="utf-8") as handle:
            json.dump(manifest, handle, indent=2, sort_keys=True, ensure_ascii=True)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        # Hard-link promotion is atomic AND refuses existing destinations, unlike
        # replace/rename. Manifest is last; interruption cannot imply completion.
        for name in sorted(names):
            output_path(output)
            os.link(temporary / name, output / name, follow_symlinks=False)
        output_path(output)
        os.link(manifest_path, output / "manifest.json", follow_symlinks=False)
    return "prepared", manifest


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True, help="Original audio (hashed only).")
    parser.add_argument("--parts", type=Path, required=True, help="Contiguous mono 16 kHz PCM WAV directory.")
    parser.add_argument("--output", type=Path, required=True, help="Dedicated non-symlink output directory.")
    parser.add_argument("--bitrate-kbps", type=int, choices=(24, 32, 48), default=32,
                        help="Opus VBR target (default: 32).")
    parser.add_argument("--check", action="store_true",
                        help="Read-only verification of manifest, hashes and full decodes; writes nothing.")
    args = parser.parse_args(argv)
    try:
        action, manifest = prepare(args.source, args.parts, args.output, args.bitrate_kbps, args.check)
    except KeyboardInterrupt:
        print("ERROR: Interrupted; no incomplete run should be treated as complete.", file=sys.stderr)
        print(f"ACTION REQUIRED: {RECOVERY}", file=sys.stderr)
        return 130
    except (AudioError, OSError, subprocess.SubprocessError, UnicodeError) as error:
        message = str(error) if isinstance(error, AudioError) else "Local file or media-tool operation failed."
        print(f"ERROR: {message}", file=sys.stderr)
        print(f"ACTION REQUIRED: {RECOVERY}", file=sys.stderr)
        return 1
    print(f"SUCCESS: {action} {len(manifest['parts'])} parts; all hashes and decoded sample counts checked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
