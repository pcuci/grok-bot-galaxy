# YouTube session sources

## Status and scope

Discovery checked 2026-09-23. The [official Galaxy page](https://x.ai/galaxy)
links ten individual session videos, separately from its three full-day X
recordings. YouTube watch-page metadata identifies their channel as Grok
(`@Grok`), publication date as 2026-09-21, and visibility as unlisted.

These are the ten sessions currently linked by the official page, not a claim
that every event session has a YouTube upload. Acquisition and local structural
validation completed 2026-09-24 UTC: **all ten original-English automatic VTT
caption tracks are downloaded**, totaling 3,049,808 bytes and 17,628 cues. No
creator-provided English tracks were exposed. No audio/video was downloaded
for this caption work. One [provisional SDR session review](../days/day-02/sessions/sdr-Iia8EF7niiA.md)
has since been authored from caption text; the other nine session reviews and
all session audio verification remain pending.

Raw captions are temporary inputs for later interpretation, not a permanent
archive. The operator authorized downloading for private study, asserted
copyright clearance, and requested that raw copies not be kept long-term.
Cleanup remains pending the interpretation handoff; no existing day evidence
was deleted or modified.

An extracted search-service version of the event page omitted the session cards;
a direct page fetch exposed them. Discovery used the live page and YouTube
watch-page metadata, not the incomplete extraction alone. A subsequent Python
request to the event page returned HTTP 403; no bypass was attempted.

## Officially linked recordings

Titles and presenters below follow the event page. Presenter listings are not
speaker diarization. Durations are YouTube metadata, not decoded-media checks or
proof that the whole scheduled session is included.

| Day | Session | Listed presenters | Duration | YouTube source |
| --- | --- | --- | --- | --- |
| 1 | Grok Bot for Engineers | Lingxi Li | 45:10 | [zCqmTSF2ctg](https://www.youtube.com/watch?v=zCqmTSF2ctg) |
| 1 | Grok Bot for Product Managers | Kevin Niparko and Roshan Sadanani | 35:12 | [gNysgEu-lew](https://www.youtube.com/watch?v=gNysgEu-lew) |
| 1 | Grok Bot for Founders | Shub Gaur | 37:14 | [hPE3A4Smkxc](https://www.youtube.com/watch?v=hPE3A4Smkxc) |
| 2 | Grok Bot for Sales Engineers | Amrita Venkatraman | 45:58 | [tpDfoh5qPF8](https://www.youtube.com/watch?v=tpDfoh5qPF8) |
| 2 | Grok Bot for Sales | Krista Letz and Mark Wright | 21:07 | [SVZe46xaVTg](https://www.youtube.com/watch?v=SVZe46xaVTg) |
| 2 | Grok Bot for SDRs | Simon Lackowski | 34:04 | [Iia8EF7niiA](https://www.youtube.com/watch?v=Iia8EF7niiA) |
| 2 | Grok Bot for Customer Support | David Gan | 31:24 | [BSB--jUnx9U](https://www.youtube.com/watch?v=BSB--jUnx9U) |
| 3 | Grok Bot for Marketing Operations | Matthew Silberman and Teresa Hsu | 21:45 | [EA-sxwWK0Vs](https://www.youtube.com/watch?v=EA-sxwWK0Vs) |
| 3 | Grok Bot for Post Sales | Blake Schuller | 30:03 | [EGt8FfTmTMY](https://www.youtube.com/watch?v=EGt8FfTmTMY) |
| 3 | Grok Bot for Marketing | Josh Kim | 30:11 | [db38-FgdaGQ](https://www.youtube.com/watch?v=db38-FgdaGQ) |

### Other leads and exclusions

- [Grok Bot 101, Day 1 Part 02](https://www.youtube.com/watch?v=jxaN9uxKFMA):
  Raner, 1:00:00. Its description claims Galaxy provenance, but it is not linked
  by the official event page. Completeness, edits, and redistribution permission
  are unverified. Keep outside the approved-source set until reviewed.
- [Grok Bot for Sales Engineering](https://www.youtube.com/watch?v=Z-20jz--GYU):
  Matthew A, 53:56. Description says Day 2; event provenance is insufficient.
  Prefer the officially linked Sales Engineers session.
- [Meet Grok Bot](https://www.youtube.com/watch?v=rkigdXf-52I) and
  [Grok Bot for GTM](https://www.youtube.com/watch?v=JZQsf5AXEig) are Cursor
  workshops from August 20 and August 26, respectively, not Galaxy sessions.
- Full-day mirrors, multi-session compilations, and third-party recaps are not
  substitutes for the requested individual recordings.

## Raw evidence placement

Use a separate source namespace, `.data/youtube/<video-id>/`, rather than placing
YouTube captions among the original `.data/day-01/transcripts/` ASR checkpoints.
The existing `/.data/` ignore rule covers this namespace. Ignoring files is not
access control; retained originals also need restrictive local permissions.

Each acquired source directory contains:

- `raw/`: original caption response bytes, with language and track origin in the
  filename. Preserve manual and automatic tracks separately when both exist.
- `manifest.json`: canonical watch URL, video ID, title, channel, event day,
  retrieval time, tool version, duration, rights/processing basis, track language
  and origin, source-relative coverage, byte counts, and SHA-256 hashes.

- `derived/automatic.en-orig.md`: full-text, timestamped Markdown for every cue,
  generated locally from the original VTT. All ten session derivatives exist.

Open `.data/youtube/README.md` for the local session index. Markdown files remain
ignored and private (0600; containing directories 0700), like the temporary
captions. They are not reviewed summaries and must not be mistaken for accurate,
complete speech transcripts or independently verified quotations.

Conversion preserves cue order, start/end timestamps, internal text line breaks,
empty cues, and rolling-caption repetition. It removes VTT display tags and
inline word timestamps, decodes text entities, normalizes CRLF and outer blank
display/separator rows, and leaves wording unchanged. The parser uses timestamp
boundaries because these exports contain blank display rows inside cue blocks;
the initial blank-block parser stopped without writing outputs.

`.data/youtube/markdown-validation.json` records converter/input/output SHA-256
hashes and per-session cue counts. Conversion fixtures and Markdown text/timing
round-trips passed for all 17,628 cues. A separate read-only regeneration check
matched all ten outputs. Run locally from repository root:

```sh
python3 -B .data/youtube/captions_to_markdown.py --check
```

The converter and its fixtures are local working artifacts, not clean-clone
project dependencies. No network access, model interpretation, deduplication,
speaker attribution, or raw-caption modification is part of this conversion.

Do not persist cookies, signed caption/media URLs, full extractor info dumps,
private contact details, or credentials. Do not download audio/video merely to
obtain captions. Translated tracks must not silently replace original-language
tracks. Missing captions are a recorded gap, not permission to start cloud ASR.
All ten sources are now under `.data/youtube/<video-id>/raw/automatic.en-orig.vtt`.
Source directories are mode 0700 and caption files are mode 0600. The aggregate
local validation record is `.data/youtube/validation.json`; it contains hashes,
counts, timing bounds, and anomalies, not caption text.

### Acquisition and validation results

All times below are seconds relative to the individual YouTube video. Cue
counts include rolling-caption overlaps and must not be treated as utterance or
word counts. First/last cue bounds do not prove uninterrupted speech coverage.

| Source ID | Cues | First cue | Last cue end | End beyond reported duration |
| --- | --- | --- | --- | --- |
| zCqmTSF2ctg | 2,053 | 0.400 | 2711.680 | 1.680 |
| gNysgEu-lew | 2,013 | 0.080 | 2111.839 | 0 |
| hPE3A4Smkxc | 2,115 | 0.240 | 2235.599 | 1.599 |
| tpDfoh5qPF8 | 2,621 | 0.480 | 2747.160 | 0 |
| SVZe46xaVTg | 1,171 | 0.000 | 1268.200 | 1.200 |
| Iia8EF7niiA | 1,967 | 0.160 | 2041.559 | 0 |
| BSB--jUnx9U | 1,477 | 0.640 | 1886.200 | 2.200 |
| EA-sxwWK0Vs | 1,005 | 0.240 | 1303.519 | 0 |
| EGt8FfTmTMY | 1,659 | 0.320 | 1804.920 | 1.920 |
| db38-FgdaGQ | 1,547 | 0.080 | 1805.720 | 0 |

Checks passed for ten nonempty UTF-8 WebVTT files, parseable timestamps,
nonnegative ordered cue starts, positive cue durations, file permissions, and
hash consistency where acquisition hashes already existed. Overlapping cues
remain unchanged. The aggregate validation adds the Customer Support hash.

Timing review remains open: five final cue ends exceed the reported integer
video duration. Customer Support also has cues starting at 1884.030 and 1884.040
against reported duration 1884. These are source timing discrepancies, not
silently trimmed data or proof of missing/corrupt speech. Initial strict checks
stopped on Engineers and Customer Support; their original failure manifests
remain as `manifest.initial-validation.json`. Engineers was rechecked with end
overruns explicitly recorded; Customer Support remains flagged for timing review.

Acquisition used cached yt-dlp 2026.08.19 through offline uv, `--ignore-config`,
`--no-playlist`, `--skip-download`, `--no-overwrites`, `--sub-format vtt`, and
original-English selection `--sub-langs en-orig --write-auto-subs`. No cookies,
credentials, translated tracks, or full metadata dumps were retained. Requests
were sequential, with 15-second socket and 60-second subprocess limits, zero
network retries, and bounded batches. The extractor warned that no supported
JavaScript runtime was found; caption extraction nevertheless succeeded. No
runtime or dependency was installed to suppress that warning.

## Complementing the existing day evidence

All three days have structurally validated local ASR and ASR-based curation
drafts: 32 Day 1, 26 Day 2 and 33 Day 3 chapters. See the
[Day 1 index](../days/day-01/transcripts/README.md) and
[Day 2/3 extraction checkpoint](day-02-03-extraction-status.md). Audio review
remains pending. Preserve all original evidence unchanged.

Candidate full-day chapters for each session, by topic only (not verified time
alignments unless a row says the alignment is checked):

| Session | Candidate day chapters |
| --- | --- |
| Engineers (Day 1) | Chapters C15–C16 in the [Day 1 index](../days/day-01/transcripts/README.md); ASR draft, alignment unverified |
| Product Managers (Day 1) | Chapters C22–C23 in the [Day 1 index](../days/day-01/transcripts/README.md); ASR draft, alignment unverified |
| Founders (Day 1) | Chapters C27–C29 in the [Day 1 index](../days/day-01/transcripts/README.md); ASR draft, alignment unverified |
| Sales Engineers (Day 2) | [D2-C02](../days/day-02/transcripts/02-sales-engineering-and-slide-bot.md)–[C04](../days/day-02/transcripts/04-workshop-results-and-guardrails.md) |
| Sales (Day 2) | [D2-C13](../days/day-02/transcripts/13-sales-workflows-and-questions.md) |
| SDRs (Day 2) | [D2-C18](../days/day-02/transcripts/18-sdr-workflow-design.md)–[C19](../days/day-02/transcripts/19-sdr-demo-and-questions.md); **alignment checked** by content anchors (Day 2 ≈ video + 05:59:51.5; Q&A 06:33:57–06:39:49 not in video), not yet playback-confirmed; see [provisional review](../days/day-02/sessions/sdr-Iia8EF7niiA.md) and [Day 2 sources](../days/day-02/sources.md#verified-session-alignments) |
| Customer Support (Day 2) | [D2-C23](../days/day-02/transcripts/23-support-workflow-and-demo-setup.md)–[C25](../days/day-02/transcripts/25-support-costs-traces-and-governance.md) |
| Marketing Operations (Day 3) | [D3-C13](../days/day-03/transcripts/13-marketing-ops-guest-and-cerebro.md)–[C14](../days/day-03/transcripts/14-advertiser-personas-and-unconnected-prospecting.md) |
| Post Sales (Day 3) | [D3-C15](../days/day-03/transcripts/15-post-sales-team-and-meeting-demo.md)–[C18](../days/day-03/transcripts/18-post-sales-verification-and-migration-questions.md) |
| Marketing (Day 3) | [D3-C25](../days/day-03/transcripts/25-marketing-workshop-research-and-positioning.md)–[C27](../days/day-03/transcripts/27-marketing-questions-and-permission-limits.md) |

Day 3's RevOps workshop (D3-C02–C04) has no officially linked session video.

1. Treat the table as comparison candidates; confirm each alignment against
   both sources before recording it.
2. Keep YouTube timestamps video-relative. Edited recordings can remove Q&A,
   breaks, or intermediate speech; never assume a constant offset maps the whole
   video onto a full-day source. Record aligned intervals and unmatched gaps.
3. Surface reviewed, nonverbatim supplements under the relevant
   `docs/days/day-XX/` directory, with video ID, caption version/hash, interval,
   attribution basis, uncertainty, and links to any matching day evidence.
4. Classify each comparison as corroborating, additional coverage, conflicting,
   or unresolved. Two transcripts of the same recording are not independent
   confirmation of a claimed external outcome. Do not silently correct local ASR
   from another unverified recognition result.
5. Day 2/3 session captions can provide partial workshop coverage after review;
   they cannot establish full-day coverage or the hosts' live-build outcomes.
6. Follow the [editorial method](editorial-method.md): distinguish requests,
   advice, generated output, narrated success, and independently observed results.
   Audio verification remains required for quotations and consequential claims.

## Authority and next step

Acquisition proceeded on the operator's explicit authorization and statement of
copyright clearance for private study. This records the operator's assertion,
not an independent legal determination or a finding that public availability
confers download rights under [YouTube's terms](https://www.youtube.com/t/terms).
No access-control bypass was attempted.

Interpretation is deferred as requested. Caption text was processed only by local
validation and Markdown conversion code; it was not printed into this
editor-hosted model's context.
Exception, 2026-09-24: the operator explicitly approved editor-hosted processing
of the SDR (`Iia8EF7niiA`) captions for private study; see its
[provisional caption-only review](../days/day-02/sessions/sdr-Iia8EF7niiA.md).
Before later hosted-model curation, confirm authorization for that actual
processing environment under [repository policy](../../AGENTS.md). Review timing
anomalies, rolling-caption repetition, and source alignment before comparing
claims with Day 1 ASR. Publish only reviewed, nonverbatim, privacy-checked
summaries with source intervals and limitations.

Remove only these task-created temporary caption copies and full-text Markdown
derivatives after the interpretation handoff, as requested by the operator;
preserve source links, hashes, and review
notes. Do not apply this cleanup instruction to existing full-day evidence.
No staging, commit, push, media redistribution, credentials, scheduled jobs,
package installation, or governance-source changes were performed.
