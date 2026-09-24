# Day 2 and Day 3 extraction and curation status

Updated 2026-09-24 after Day 3 ingest, ASR, curation and sampled text review.
Both days are ready for **ASR-based draft review**, not audio-verified acceptance.
Event synthesis and the study plan have not been produced.

## Current handoff

| Stage | Day 2 | Day 3 |
| --- | --- | --- |
| Audio acquisition and strict decode | Passed | Passed |
| Exact PCM chunks and full-decode hash comparison | Passed | Passed |
| Raw ASR and independent export validation | Passed | Passed |
| Nonverbatim curation draft | 26 chapters, 174 timed groups | 33 chapters, 157 timed groups |
| Audio verification, consequential claims and identities | Pending | Pending |
| Event synthesis and study plan | Not run | Not run |

- [Day 2 overview](../days/day-02/README.md),
  [chapters](../days/day-02/transcripts/README.md),
  [source record](../days/day-02/sources.md),
  [review queue](../days/day-02/review-queue.md).
- [Day 3 overview](../days/day-03/README.md),
  [chapters](../days/day-03/transcripts/README.md),
  [source record](../days/day-03/sources.md),
  [review queue](../days/day-03/review-queue.md).

## Sources and measured coverage

The official event page linked these full-day X recordings. Titles are metadata,
not evidence of a successful company, launch or commercial outcome.

| Measurement | Day 2 | Day 3 |
| --- | --- | --- |
| Public source | <https://x.com/i/broadcasts/1PKqrNyvmYwGb> | <https://x.com/i/broadcasts/1YGNrbXEeazGw> |
| Title | Grok Bot builds a Game Studio LIVE | Building a company in 3 days - launching today! |
| HLS fragments | 14,885 | 14,144 |
| Download time | 754.41 seconds | 464.86 seconds |
| Retained M4A bytes | 255,494,347 | 242,819,870 |
| Mono 16 kHz PCM samples | 483,176,448 | 459,237,717 |
| PCM duration | 08:23:18.528 | 07:58:22.3573125 |
| Exact 30-minute parts | 16 plus 23:18.528 remainder | 15 plus 28:22.3573125 remainder |
| ASR regions | 4,119 | 3,806 |
| JSON/TXT/SRT exports, including combined | 54 | 51 |

Raw artifacts remain ignored under `.data/day-02/` and `.data/day-03/`:

- `day-2-grok-bot-galaxy.m4a` or `day-3-grok-bot-galaxy.m4a`.
- `parts/part-*.wav`, unchanged after ingest validation.
- `transcripts/part-*.{json,txt,srt}` and `full-transcript.{json,txt,srt}`.
- `source-manifest.json`, `parts-manifest.json`, `asr-validation.json` and logs;
  Day 3 also has `ingest-validation.json`.
- Byte-identical copies of the historical Day 1 runner and VAD model.

The per-day source records and manifests retain source, model, runner, part and
export hashes. Curation inventories and validation reports record that Day 2's
90 raw files and Day 3's 96 raw files remained unchanged during their respective
curation passes. Raw file counts include manifests and runtime artifacts, not
just transcripts.

## Working acquisition method and timing limitations

The operator requested the same strategy as Day 1: yt-dlp native HLS fragment
download, audio extraction, then deletion of temporary video after validation.
Both new days used cached yt-dlp 2026.08.19, `replay-300`, eight concurrent
fragments, bounded retries and abort-on-unavailable-fragment behavior. Both
completed within the 900-second per-day download limit. MPEG-TS transport lived
only in ignored `.data/`; it was removed after audio validation and promotion.

FFmpeg 8.0.1 stream-copied AAC into M4A without re-encoding audio. These files
are extracted derivatives, not byte-identical original broadcast containers.
Day 2 required two non-monotonic DTS corrections. Day 3 required four DTS
corrections and two discontinuity offsets. Day 3's source and extracted AAC
matched across all 1,345,423 frame payloads; an initial whole-ADTS comparison
failed because buffer-fullness header bits changed. Normalizing only those bits
made the full ADTS streams match. The diagnostic history remains in its manifest.

Chunking retained the Day 1 silence-preserving resampling filter. Each full part
contains 28,800,000 samples. Concatenated WAV payload counts and hashes match a
fresh full-source decode with the same filter. PCM exceeds container duration
by 0.022 seconds for Day 2 and 0.0476455 seconds for Day 3. Use the normalized
PCM timeline, not wall-clock schedule slots or assumed YouTube offsets.

## ASR and curation validation

Local ASR used cached Python 3.12, sherpa-onnx 1.13.8, Whisper tiny.en INT8 and
Silero VAD. Batches had at most four workers, one recognizer thread each, a
15-minute limit and an 8 GiB per-process virtual-memory ceiling. Day 2's five
batches totaled 32m55.208s; Day 3's four batches totaled 29m45.007s. No ASR
processing timeout or retry occurred.

Checks covered source/part/model identities, completed checkpoints, ordered
nonoverlapping sample-aligned regions no longer than 25 seconds, exact TXT/SRT
rendering and offset-adjusted combined JSON. Those checks establish structural
consistency, not speech recall, recognition accuracy or speaker identification.

All 17 Day 2 and 16 Day 3 TXT parts were read for nonverbatim curation. Chapters
retain source intervals, attribution qualifications, requests versus reported
results, separate human/bot identities, and explicit omissions. YouTube captions
were not read or aligned in these passes and remain a separate workstream.

Day 3 received an independent ASR-text comparison of chapters 01, 06, 16 and 33,
plus checks of all 3,806 region mappings. Two localized issues were corrected:
an unsupported authentication qualifier and a launch-handoff sentence assigned
to the preceding time group. Final Day 3 validation passed 18 checks, including
340 local links and 48 anchors. Markdownlint was unavailable; documented fallback
structural checks ran without installing packages.

Neither curation pass listened to audio. Gap ledgers include empty recognition
regions and intervals without ASR; these are not certified silence. Boundaries,
identities, numbers, payment claims, production status and other consequential
statements remain subject to the per-day review queues.

## Prior interruptions preserved

Day 2's initial direct FFmpeg HLS attempt failed on non-monotonic DTS. A corrected
remux attempt then exceeded 900 seconds, leaving an unusable M4A without its
`moov` atom. This was not the eventual successful yt-dlp acquisition.

| Preserved failed/sample artifact under `.data/day-02/` | Bytes |
| --- | --- |
| `day-2-grok-bot-galaxy.partial.m4a` | 80,703 |
| `remux-probe.m4a` | 80,703 |
| `corrected-probe.m4a` | 577,309 |
| `day-2-grok-bot-galaxy.remux.partial.m4a` | 157,024,300 |

The timed-out file's SHA-256 is
`bfa25a4ad60cc6ca8b923b84eecd6d711506bc4f8708f2fb535127b301d52d74`.
It remains distinct from the validated audio. A later Day 3 preflight help
command opened an interactive pager and timed out before changing data; the
operator explicitly renewed the task and processing resumed noninteractively.

## Authority and remaining work

The operator authorized private-study extraction, then editor-hosted transcript
curation, and renewed Day 3 chunking/transcription/curation. This grants neither
redistribution rights nor independent verification of narrated outcomes.

- Originals remain local and ignored; Day 1 evidence is unchanged.
- No media, raw transcripts or models were committed or published.
- No cloud transcription, credentials, new model downloads, background jobs or
  governance-source changes were performed. No staging, commits or pushes.
- Processing retained the 10 GB new-artifact budget and at least 10 GB free disk,
  five-minute chunk/decode caps, and 15-minute ASR batch caps.
- Review the draft chapters and audio-priority queues next. Event synthesis must
  preserve unverified status where review evidence is still missing; the study
  plan remains subsequent work, not a completed artifact.
