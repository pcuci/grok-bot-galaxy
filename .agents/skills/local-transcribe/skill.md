---
name: local-transcribe
description: Transcribe bounded broadcast chunks locally with sherpa_onnx Whisper tiny.en int8 and Silero VAD, preserving source timestamps and resumable validated checkpoints without implicit cloud uploads. Use after audio provenance and parts are validated.
---

# Local transcribe

Read `../../../AGENTS.md` and the ingest manifest. This is the requested local
pipeline contract, not a claim that the separate implementation already meets
it. Never upload audio, transcripts, prompts, or checkpoints implicitly.

## Preflight

1. Inspect the actual `scripts/` implementation and its supported `--help`.
   Day-one working paths include `.data/day-01/transcribe.py`,
   `.data/day-01/silero_vad.onnx`, `parts/*.wav`, and `transcripts/*`. Do not
   assume the working script and eventual reusable CLI have identical flags.
2. Verify installed `sherpa_onnx` and compatible local Whisper `tiny.en` int8
   encoder/decoder/token assets plus Silero VAD. Record versions, asset hashes,
   license/source, language, decoding and VAD settings. No implicit model
   downloads, package installs, network fallback, or cloud transcription.
   Missing/incompatible assets block execution until separately authorized.
3. Tiny.en is English-only; mark non-English stretches unsupported or uncertain
   rather than inventing translation. ASR cannot identify speakers by itself.
4. Set explicit CPU threads, maximum inference duration, memory budget, per-part
   timeout, retry cap, and checkpoint frequency from the implemented interface
   and available resources. Stop rather than run an unbounded whole-broadcast job.

## VAD and inference

- Prefer preserved PCM under `.data/` over lossy Git audio for ASR. If only Opus
  derivatives are available, validate their manifest and decoded sample counts,
  use a separate ignored work directory, and mark changed audio/checkpoint identity.
  Never mix recognition from recompressed inputs into original checkpoints.
- Keep half-hour WAV parts intact. Use Silero VAD to select speech intervals
  without rewriting the source timeline. Validate waveform rate/channel/length
  against the ingest manifest before each part.
- Bound inference windows to the actual model/runtime limit (Whisper's usual
  context is about 30 seconds, not 30 minutes). Split long uninterrupted speech
  explicitly; record overlap/padding and how duplicated boundary words are
  reconciled. Never allow VAD to produce arbitrarily long inference inputs.
- Map every result back to source time: part start plus VAD/window start plus
  model-local offset, accounting for overlap/padding only once. Preserve gaps
  for silence. Do not timestamp concatenated speech as contiguous source audio.
- If the API yields text without reliable word/segment timing, retain the
  inference-window interval and label the precision; do not fabricate word
  timestamps. Record silence, empty results, errors, and unprocessed intervals
  separately. Empty output is not automatically verified silence.
- Flag hallucination-prone silence, music, overlapping speech, and repeated text
  for listening review. Keep raw recognizer output even when deriving cleaned
  text. Never silently fill missing speech from context.

## Resumable checkpoints

Use the actual pipeline's schema, or document a schema before implementation.
Each checkpoint must bind: schema version, source and part hashes, exact part
range, model/VAD/token hashes, script/version fingerprint, all inference/VAD
settings, window ID/range, status, output hash/path, and timing precision.

Write output to temporary files, validate them, then atomically rename on the
same filesystem. Promote the completion checkpoint last. Preserve previous
valid checkpoints; interrupted writes and partial output must never count as
complete. Do not promise atomic behavior unless the implementation provides it.

On resume, parse every candidate checkpoint, match all input/configuration
fingerprints, verify output existence/hash/schema, and check ordered in-range
timestamps and expected window coverage. Only matching completed windows may
be skipped. Quarantine corrupt/stale checkpoints without destroying raw
outputs; rerun only the affected work within the authorized retry budget.
Reject a changed source/model/settings fingerprint rather than merging runs.

## Validation and handoff

- Test a bounded sample with speech, silence, a half-hour boundary, and overlap.
  Check source-aligned timestamps by listening. Test interruption/resume and a
  corrupt or mismatched checkpoint before trusting unattended resumption.
- Validate monotonic source ranges, gap classifications, duplicate boundaries,
  and processed versus total coverage. Validated silence counts as processed;
  errors and missing windows remain incomplete.
- Hand raw transcripts, provenance, checkpoints, and a coverage/error report to
  `transcript-curate`. Report actual commands and results, not intended behavior.
  Do not claim a full transcript from a partial run or ASR quality from schema
  checks alone. Leave originals and previous raw outputs intact.
