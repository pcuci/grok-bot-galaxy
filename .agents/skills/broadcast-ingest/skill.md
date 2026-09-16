---
name: broadcast-ingest
description: Ingest authorized event broadcast audio while preserving original bytes, source metadata, hashes, exact half-hour PCM chunks, and silence-relative timestamps. Use before local transcription or when auditing media provenance.
---

# Broadcast ingest

Read `../../../AGENTS.md`. This skill specifies a workflow, not an implemented
pipeline CLI or permission to download. Event-facing documentation goes under
`docs/`; media and machine metadata stay in the authorized data directory.

## Inputs and preflight

1. Establish the authorized source URL/event day, retention and redistribution
   rights, output directory, disk budget, and download time limit. Resolve
   privacy/copyright uncertainty before acquisition. Never bypass access controls.
2. Discover the actual implementation under `scripts/`, inspect its code and
   `--help`, and use only supported flags. Do not invent downloader commands.
3. Inspect existing artifacts before writing. Day one uses
   `.data/day-01/day-1-grok-bot-galaxy.m4a`, `parts/*.wav`, and `transcripts/*`.
   Do not overwrite an existing original, even if another download looks newer.

## Acquisition and provenance

- Prefer audio-only acquisition; do not download video merely for convenience.
  Video is never a Git artifact. If only an authorized video source exists,
  arrange separately approved temporary storage and retention before extraction.
- Preserve the acquired audio bytes unchanged. If conversion was necessary,
  label the M4A as a derivative and record the source format and transformation;
  do not call transcoded audio a byte-identical original.
- Record a stable source ID, public URL without secret query values, title,
  publisher/channel, event day, retrieval time with timezone, permissions status,
  file size, SHA-256, duration, codec, sample rate, channels, and inspected tool
  versions/settings. Distinguish event time from retrieval time. Unknown values
  stay unknown; never infer missing broadcast dates or speakers.
- Download into a temporary file, validate it, then atomically promote it on the
  same filesystem. On rerun, accept an existing artifact only after checking its
  identity/hash; preserve conflicting versions for review rather than replacing.

## Exact half-hour parts

1. Decode/resample consistently to mono 16 kHz PCM WAV for the planned ASR stack,
   preserving the full timeline including leading, internal, and trailing
   silence. Record any codec start offset, priming, padding, or resampling
   duration discrepancy; do not silently shift the origin.
2. Cut at decoded sample boundaries: part `k` (zero-based) covers
   `[k * 1800, min((k + 1) * 1800, duration))` seconds. Every full part has
   `28,800,000` samples at 16 kHz. Only the final part may be shorter. Do not add
   a zero-length terminal part or silence-pad the remainder to fake coverage.
3. Half-hour parts are storage/processing units, not semantic chapters or
   individual Whisper inference windows. Do not use silence removal, speed
   changes, VAD concatenation, or approximate compressed-stream cuts here.
4. Produce a machine-readable parts manifest with ordered part IDs, source hash,
   per-part hash, sample count/rate, start/end sample offsets and source-relative
   seconds. File naming must be deterministic and agree with actual scripts.
5. Validate contiguous, non-overlapping coverage of the decoded source; verify
   the sum of sample counts and the final endpoint. Compare boundary audio and
   silence positions with the original. Container duration estimates alone do
   not prove sample-exact segmentation.

## Handoff and acceptance

Pass the immutable original, provenance, and validated parts manifest to
`local-transcribe`. Report bytes/hashes, measured duration, full-part count,
remainder, and any timeline offset. A partial or failed download is not ready
for ASR. No media is staged or published here. Originals, WAVs, models, raw ASR,
and local quality experiments stay under ignored `.data/`.

Compact `audio/day-*/part-*.opus` derivatives may use ordinary Git after an
explicit save grant and rights review. Inspect `scripts/prepare_audio.py --help`
before preparing them. Require source/output hashes, encoding settings, and a
completed manifest; fully decode every part and verify exact source sample counts.
Do not replace PCM or claim ASR accuracy from a successful decode or a small
codec comparison. Keep partial runs ignored until validated. See
`docs/reference/audio-storage.md` from repository root for current evidence.
