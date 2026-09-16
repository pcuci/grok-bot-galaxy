# Audio storage and quality

## Storage contract

- `.data/day-01/`: ignored original M4A, 18 PCM WAVs, raw ASR/checkpoints,
  historical runner, and VAD model. These remain the preferred local ASR inputs.
- `.data/audio-quality/`: ignored codec experiments, metrics, and partial outputs.
- `audio/day-01/part-*.opus`: intended compact derivatives for ordinary Git,
  together with a completed `manifest.json`. Preparation is not complete yet.
- `scripts/prepare_audio.py`: bounded, standard-library CLI using installed
  FFmpeg/FFprobe. It neither downloads media nor runs transcription.

Moving files into `.data/` does not delete them, reduce local storage, or remove
old Git objects. The previously observed approximately 669 MB Git object store
has not been pruned. No Git staging, commit, or push occurred in this task.
Ordinary-Git eligibility is not redistribution permission.

## Original sizes and preservation

| Artifact | Bytes | Decimal MB |
| -------- | ----- | ---------- |
| Extracted M4A | 265,500,294 | 265.50 |
| All 18 WAVs | 1,008,403,560 | 1,008.40 |
| One full half-hour WAV | 57,600,078 | 57.60 |
| Final WAV | 29,202,234 | 29.20 |
| Original audio total | 1,273,903,854 | 1,273.90 |

All 78 original files retained their SHA-256 hashes across the `data/` to
`.data/` move and subsequent sample experiment. The aggregate identity of the
sorted relative-file-name to SHA-256 mapping is:

```text
95404ee7899ea8782c25d844cff85d4683973b838a6273ba2dfc94adc97f94a1
```

The original runner and checkpoint model identity are unchanged. Do not edit
that runner in place or inject recompressed audio into its old checkpoints.
See [Day 1 sources](../days/day-01/sources.md) for source and PCM identities.

## Codec choice

Use **mono Opus, 32 kbps VBR target**, encoded from the existing mono 16 kHz PCM
parts. Preserve full timeline and silence: no trimming, normalization, denoising,
or VAD concatenation. Settings are `application=audio`, 20 ms frames, compression
level 10. Actual VBR size varies; target bitrate alone is not a size guarantee.
The first full part produced during the interrupted run was 7,249,459 bytes.
A completed full-event size has not been measured.

32 kbps is a provisional size/ASR-consistency trade-off, not a proven universal
minimum for accurate transcription. 24 kbps changed more words in the sampled
recognitions. 48 kbps improved the low-RMS subset but not the pooled result;
it may merit reconsideration for difficult speech after listening review.

## Local experiment on 2026-09-16

Eight existing checkpoint windows from parts 1, 3, 6, 8, 10, 13, 15, and 17 were
selected deterministically, alternating the 10th and 50th RMS percentiles among
nonempty 12-25-second speech regions. Total: 178.908 seconds, 2,862,528 PCM
samples, and 555 normalized reference words.

Fresh PCM and each codec roundtrip were recognized with the same installed
Whisper tiny.en int8 model through sherpa-onnx 1.13.8, CPU, two threads, greedy
search, identical windows, and no prompt carry-over. Fresh PCM matched the
normalized existing checkpoint text in all eight windows. No utterance text was
sent to the hosted editor model or saved in the experimental metric artifacts.

| Target kbps | Sample encoded bytes | Word edits vs fresh PCM | Pooled disagreement | Exact windows |
| ----------- | -------------------- | ----------------------- | ------------------- | ------------- |
| 24 | 496,585 | 19 | 3.42% | 4/8 |
| 32 | 648,404 | 10 | 1.80% | 5/8 |
| 48 | 952,078 | 12 | 2.16% | 6/8 |

Low-RMS pooled disagreement was 3.03%, 3.03%, and 1.68% respectively. These are
normalized word edit distances against **machine recognition of PCM**, not WER
against a human transcript. No candidate produced identical recognition across
all windows. The small, non-monotonic differences do not establish that either
32 or 48 kbps is more accurate.

All 24 codec roundtrips retained sample counts. The 32 recognitions completed in
103.4 seconds with no retries, using an existing offline environment; no package
or model download was performed. Local scripts, metrics, hashes, selection,
and validation reports are retained in `.data/audio-quality/`.

Limitations: no listening review or ground truth; checkpoint selection excludes
speech missed by the original pipeline; low RMS is not proof of quiet dictation;
sparse windows may miss overlap, whispers, music, and non-English speech.
Standalone clip encoding also differs from continuous full-part encoding.
Original PCM remains the safest available input for local ASR.

## Preparation and validation

The implemented CLI uses Python 3.10+ and installed FFmpeg/FFprobe with libopus.
Inspect its supported arguments first:

```sh
python3 -B scripts/prepare_audio.py --help
```

From repository root, the preparation command is:

```sh
python3 -B scripts/prepare_audio.py \
  --source .data/day-01/day-1-grok-bot-galaxy.m4a \
  --parts .data/day-01/parts \
  --output audio/day-01 \
  --bitrate-kbps 32
```

The first run, following the test suite, exceeded a **300-second outer command
limit**. Nine partial-output files were present; there was no completion manifest
and they must not be treated as a completed set. They were moved unchanged to
`.data/audio-quality/interrupted-prepare-32/`, leaving the intended output
directory empty. No FFmpeg process remained running at inspection. A longer
bounded rerun awaits human approval; no automatic retry was started.

On success, the CLI strips non-encoder metadata, fully decodes every output,
checks exact PCM sample counts and a 20 MiB per-file ceiling, and records source,
WAV, and encoded hashes; source-relative ranges; tool versions; and settings.
The manifest is published last. Conflicting files/settings are refused rather
than overwritten. A matching completed rerun verifies and skips encoding.

Append `--check` to the preparation command for read-only verification after
completion. It is expected to fail before a completed manifest exists. Byte
reproducibility is limited to the same toolchain/settings. The CLI does not prove
source-to-WAV alignment or ASR quality; those are separate evidence checks.

Validation performed:

```sh
python3 -B -W error -m unittest discover -s scripts -p test_prepare_audio.py -v
```

**35 tests passed**, including real FFmpeg integration, sample-count checks,
metadata restrictions, source/output hash checks, idempotence, conflict refusal,
and failure cleanup. Full-event output validation remains pending.

## Publication gate

`.gitattributes` explicitly disables LFS filtering for the selected compact Opus
paths. `.gitignore` excludes `.data/`, the retired `data/` path, large audio
formats, raw experiment audio, and temporary preparation directories. Video
remains excluded. Before a separately authorized save, verify the completed
manifest, actual Git attributes/ignore rules, source rights, intended destination,
and privacy. Only compact reviewed derivatives belong in ordinary Git.
