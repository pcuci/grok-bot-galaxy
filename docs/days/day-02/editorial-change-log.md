# Day 2 editorial change log

Status: **ASR-based review draft**. This records derivative editing, not changes
to source evidence. No audio-verified corrections or quotations were made.

## Inputs and authorized transformation

The operator authorized this editor-hosted model to process full-day X ASR.
All 17 TXT parts were read in full, in chronological order, with JSON interval
checks and JSON/TXT/SRT consistency validation. No YouTube captions or external
sources were used to repair words or infer alignment.

The result is **26 nonverbatim edited conversations**, organized into 174 timed
topic sections. Chapter boundaries are semantic where recoverable, may span
30-minute files, and include explicit interruption/transition coverage. Metadata
and the [coverage ledger](coverage-ledger.json) bind them to unchanged inputs.
This is not a verbatim transcript, a translation of every ASR token or an
independently verified event synthesis.

## Editing rules applied

- Removed filler, repeated acknowledgements and recognition noise only from the
  derivative; retained meaningful disagreement, corrections, failures and reversals.
- Grouped inseparable turns instead of inventing diarization or exact speaker
  changes. Speaker-to-addressee and interaction types are explicit in labels or
  local prose; default addressee conventions are in the transcript index.
- Kept human readers distinct from the bots credited with generated content.
- Used readable contextual product spellings such as Grok Bot, Notion and Cursor
  where repeated local evidence supported the reading. This is navigation-level
  normalization, not verified spelling of every spoken token.
- Did not confidently repair names, employer affiliations, prices, quantities,
  model versions or questionable meaning from general knowledge.
- Kept claims, requests, proposed actions, narrated previews and externally
  verified outcomes separate. No external outcomes were independently verified.
- No direct quotations: all event wording is paraphrased. Backticks identify
  artifact/tool labels, not audio-verified speech.
- Minimized incidental family, health, private-contact, account and access detail.
  Redactions preserve workflow/decision context without copying sensitive values.
- Did not reconcile apparent duplicate speech by wording alone. Every raw region
  remains represented by an input ID; no raw record was deleted or edited.

## Material editorial choices

| Source interval | Choice in derivative | Basis / unresolved question |
| --- | --- | --- |
| 00:10:03.992 onward | Host names remain probable; unstable employer names not resolved. | Introductions/address in ASR, no audio/profile verification. |
| 00:45:07.696-01:23:56.184 | Flylo and its bot team kept as workshop environment; personal and demo-account instances separated. | Explicit account switch and demo-company framing. |
| 01:07:27.064-01:12:22.808 | Salesforce slide result distinguished from Grab request and unclear figure. | Reported result versus new request; uncertain number not silently fixed. |
| 01:23:56.184 | Boundary remains a mixed region rather than fabricated clean handoff. | ASR region contains end of answer and host transition. |
| 02:13:22.264-02:15:30.264 | Coffee-business story retained as testimonial; incidental family detail minimized. | No measured business outcome or verified business spelling. |
| 02:39:03.512-03:03:48.124 | Karen X Cheng retained as probable candidate over garbled opening; plotter marked unfinished. | Closing self-identification/spelling and explicit project limitation. |
| 03:33:56.824-03:42:01.496 | Cupcake Eng ownership/continuity qualified; label versus instructions distinction retained. | Mutual host address and description review, not independent runtime evidence. |
| 04:00:00.000-04:32:50.128 | Krista/Crystal name unresolved; differing routine preferences retained; Echo not continuous streaming. | Presenter Q&A clarifies stopping Granola before slide update. |
| 04:43:49.368-05:09:55.128 | Host Matt separated from Matthew Berman; prospective utility estimate not realized savings. | Guest introduction and account of switching that morning. |
| 05:09:55.128-05:13:11.832 | Initial large-codebase analysis not described as completed migration. | Customer clip qualifies host promotional shorthand. |
| 05:13:11.832-05:31:26.648 | Student/intern framing qualified; contact research not sent outreach; actual experience required. | Interview context, privacy warning and explicit anti-fabrication advice. |
| 05:15:12.280, 05:18:28.600, 05:22:07.864, 05:25:59.512, 05:28:52.600 | Refined initial rounded internal C16 routing cuts to actual JSON region starts. | Targeted check of already-read part 11; no new diarization or audio certainty. |
| 05:34:47.384-05:56:06.392 | Ads represented as requested/preliminary motion assets, with debug failure and cleanup. | Hosts explicitly identify defects; no campaign launch evidence. |
| 06:14:03.640-06:39:49.016 | Prospect scores and drafts not treated as delivered outreach; unanswered cost quantity retained. | Demo narration and qualified Q&A. |
| 06:47:46.040-07:15:43.888 | Same-prompt Slack bots kept separate; Notion permissions and DM-listening fix retained. | Identical names do not imply shared instance; hosts describe access/subscription gaps. |
| 07:19:38.744-07:19:58.544 | Test-deletion discussion explicitly preserved as consequential but unverified action. | No audio/repository evidence establishes execution; later verification claims do not erase it. |
| 07:40:33.720-07:55:20.056 | Flylo support policy/tickets marked synthetic; Tune did not invent the approved FAQ rule. | Presenter defines pretend airline and supplies policy before update. |
| 07:55:20.056-07:58:53.624 | Rehearsal result, permission change, retry and eventual reported reply kept distinct. | Narration shows waiting and fallback to an earlier example. |
| 08:14:09.080-08:19:13.656 | Closing bugs and untested/unrebased ads retained alongside positive recap. | Explicit host caveats; no inferred final match, deployment or revenue. |

The [gap ledger](gap-ledger.md) records exact omission/review windows, and the
[review queue](review-queue.md) owns unresolved checks. No direct quote has been
approved for reuse. Screens, background conversation and quiet dictation cannot
be reconstructed from missing ASR.

## Validation notes and scope protection

- Two initial custom-validator failures were comparison mistakes, not source
  defects: rounding combined JSON offsets and exact subtraction of a floating
  remainder duration. The corrected checks use the original float-addition
  convention for combined JSON and sample count/rate for PCM duration.
- All 90 inventoried raw files matched their baseline byte counts and hashes on
  recheck. All 54 export hashes matched the recorded ASR validation.
- Both protected global documents have different hashes from the initial baseline.
  They were **not edited by this curation pass**; separate concurrent caption/global
  work was explicitly expected. Current/baseline hashes are recorded, not reverted.
- No writes outside `docs/days/day-02/`, no scripts installed or persisted, and no
  network, cloud transcription, Git operations, deletion or synthesis execution.
- Markdownlint is not on PATH. No package download or broad pre-commit hook was
  run. The validation report names the bounded custom Markdown checks instead.

See [validation.json](validation.json) for check results, not a claim of completed
human/audio acceptance.
