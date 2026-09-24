# Day 3 sources and processing record

Status: **ASR-based review draft**. The full-day X ASR was text-reviewed; no audio
was listened to during curation. Structural validation is not a speech-accuracy,
identity, demo-success or external-outcome check.

## Authority and source

The operator authorized private study extraction and explicitly authorized
processing raw transcripts in this editor-hosted model. This curation pass writes
only to `docs/days/day-03/**`; concurrent parent updates to global status/navigation
are separate and expected. Raw evidence is read-only. This pass uses
only full-day X ASR: no YouTube inputs, caption alignment, network requests,
cloud transcription, Git writes or cross-day synthesis.

| Field | Value |
| --- | --- |
| Evidence source | X broadcast `1YGNrbXEeazGw` |
| Public source identifier | `https://x.com/i/broadcasts/1YGNrbXEeazGw` (recorded, not fetched this pass) |
| Manifest title | Building a company in 3 days - launching today! |
| Uploader metadata | Grok Bot |
| Retained audio | `.data/day-03/day-3-grok-bot-galaxy.m4a` |
| Source SHA-256 | `f121e311238c48e0b6cc44ddc52726cbbd0b4bfa0fa6705c849b1c57ef56a558` |
| Concatenated PCM SHA-256 | `e99f1541358af21cbef3ce270540a2e07d1c660531b5c1921da309f7423245d7` |
| PCM samples | 459237717 at 16000 Hz, mono, signed 16-bit |
| PCM duration | 28702.3573125 seconds / 07:58:22.3573125 |
| Parts | 16: fifteen 1800-second parts, then 1702.3573125 seconds |
| Checkpoint identity | `0d847ac4af716e652da03e4cc0a654cbe2a187f6b4697960f6a0d1c20571f5f0` |
| Recognition regions | 3806 total; 3800 nonempty; six empty |
| ASR exports | 51: sixteen JSON/TXT/SRT triplets plus one full-day triplet |

The title is metadata, not proof of a company, launch, profitability or any
particular content. The actual trajectory is preserved in the
[chronological chapters](transcripts/README.md), including the closing failure
reports rather than just the launch announcement.

## Manifest chain and raw preservation

Read-only inputs under `.data/day-03/`:

- `source-manifest.json`: acquisition metadata, rights statement, stream-copy
  transformation, warning examples and retained-audio hash.
- `parts-manifest.json`: exact sample intervals, individual WAV hashes, PCM
  configuration, full-decode comparison and normalized timeline description.
- `ingest-validation.json`: prior ingest checks and their limitations.
- `asr-validation.json`: run settings, model/runner/VAD identities, batch status,
  export hashes and structural checks.
- `transcripts/part-01` through `part-16`, each in JSON, TXT and SRT; combined
  `full-transcript.json`, `.txt` and `.srt`.

The [baseline inventory](input-inventory.json) records all 96 regular files
reachable under the Day 3 raw directory, totaling 1,165,816,222 bytes, including
runtime cache files. Baseline export hashes matched all 51 ASR-manifest hashes.
The final [validation report](validation.json) records a fresh file-set, size,
symlink-flag and hash comparison. No raw file is corrected, deleted or rewritten.

The upstream manifest says the original MPEG-TS video transport was deleted
before this curation after its ingest checks. It is not retained evidence in
this pass. Its recorded SHA-256 is
`4f07a7c8b142b59df88cf5c139bf29ddf38301b5f5122c14e90e24d6f0df1e07`.
No transport comparison can be independently repeated here without that input.

## Timing caveats that survive successful validation

The source was AAC stream-copied into M4A, not re-encoded, with **four
non-monotonic DTS corrections and two discontinuity offsets** reported by
FFmpeg. The manifest's AAC payload comparison passed; an initial whole-ADTS-byte
comparison failed because of buffer-fullness header differences, then matched
after header normalization. Those are prior ingest results, not new listening
verification.

The PCM timeline uses the recorded resampling filter:

```text
aresample=16000:async=1:first_pts=0,asetnsamples=n=16000:p=0,asetpts=N/SR/TB
```

It preserves the resulting normalized recording timeline. It is **not original
broadcast wall-clock timing** and not an independently validated alignment to
any other source. The source container duration is 28702.309667 seconds, which
is 0.0476455 seconds shorter than PCM. Use sample counts for exact duration.

For part number `n`, source-relative seconds equal part-local seconds plus
`(n - 1) * 1800`. Chapter intervals are half-open. Millisecond timestamps are
ASR speech-region boundaries, not word timing or exact speaker-turn boundaries.
The exact final PCM endpoint retains more precision. Regions crossing a chapter
or section boundary are recorded as crossings, not silently truncated or removed.

## ASR and review method

The upstream run used Whisper tiny.en INT8 on CPU and Silero VAD, English only,
with at most four workers, one recognizer thread and one VAD thread, 0.4-second
minimum silence, 0.2-second minimum speech, 20-second maximum VAD speech,
25-second inference slices and checkpoints every 25 regions. No diarization or
word alignment is available.

All sixteen TXT parts were read completely in chronological order across this
curation session and its saved checkpoint. JSON supplies exact segment intervals
and file identity; TXT/SRT and the combined JSON are structurally cross-checked.
The full-day export is not treated as an additional independent source.

The derivative is an edited nonverbatim conversation, not a word-perfect
transcript or a handful of chapter summaries. It retains meaningful exchanges,
questions, failed demos, uncertain names/numbers and changes in authority. Filler,
repeated screen directions, incidental handles, private contact details, lyric-like
break material and unintelligible fragments are handled explicitly in the
[gap ledger](gap-ledger.md) and [editorial log](editorial-change-log.md).

## Inherited ASR-validation limits

- Structural success does not measure VAD recall, recognition accuracy or the
  amount of speech missed entirely.
- Empty output, labels and intervals between regions are not verified silence.
- Checkpoint identity omits CLI thread settings and a direct source hash; the
  manifest binds those separately. Shared identity does not equate different days.
- JSON can become complete before non-atomic TXT/SRT export; exports were checked
  independently, not assumed valid from the completion flag.
- No interruption/resume-corruption test was performed in this run.
- Upstream model/VAD source and license were not independently established;
  no redistribution is authorized by these records.

## Rights and acceptance gates

Private study permission does not establish redistribution rights. Review
intended audience, retention and destination access before sharing derivatives.
This pass copies no raw transcript, recording, credential, phone number or
private contact link into the edited chapters.

The skill's audio checks for representative boundaries and consequential claims
remain **unmet**. Human identities, numbers, demo behavior, privacy assurances,
permissions, payments and outage recovery require review. The
[review queue](review-queue.md) covers every chapter plus specific priority
contradictions. No event-synthesis artifacts are created by this curation.
