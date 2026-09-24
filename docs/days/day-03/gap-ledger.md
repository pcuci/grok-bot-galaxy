# Day 3 gaps, omissions and coverage limits

Status: **ASR-based review draft**. All sixteen parts were read in full. A
complete chapter partition or segment routing does not prove that every spoken
word was recognized or retained. See [machine coverage](coverage-ledger.json),
[chapter index](transcripts/README.md) and [sources](sources.md).

## Explicit low-information intervals

Intervals are half-open normalized recording time. Four DTS corrections and two
discontinuity offsets precede this timeline; labels do not establish silence.

| Interval | Chapter | Disposition and limit |
| --- | --- | --- |
| 00:00:00.000-00:09:56.440 | [C01](transcripts/01-opening-and-overnight-rework.md) | Labels/gaps only; opening speech may be absent from ASR; nothing invented |
| 00:28:38.328-00:34:20.024 | C01 | Labels/gaps; RevOps resumes mid-thought, introduction missing |
| 01:10:52.760-01:21:04.184 | [C04](transcripts/04-revops-questions-and-transition.md) | Music-like material/recognition gaps; lyrics and unclear fragments omitted |
| 02:38:24.888-02:44:13.144 | [C10](transcripts/10-enterprise-video-and-break.md) | Music-like transition; not converted to dialogue |
| 03:16:30.872-03:23:06.520 | [C12](transcripts/12-vincent-bot-onboarding-and-promotions.md) | Music-like transition; lyric-like fragments omitted |
| 04:46:51.096-04:53:20.376 | [C18](transcripts/18-post-sales-verification-and-migration-questions.md) | Labels/gaps, with previous answer cut off and hosts returning mid-discussion |
| 07:18:14.736-07:28:29.016 | [C30](transcripts/30-broken-ad-auction-and-feedback-projects.md) | Announced break; labels, mumbling and lyric-like fragments omitted, no claim all audio was music |
| 07:58:03.440-07:58:22.3573125 | [C33](transcripts/33-closing-metrics-outage-and-failed-sponsorship-test.md) | No recognized region after goodbye; exact 18.9173125-second tail retained |

Every empty ASR region, every interval not covered by a recognized region and
every chapter/section crossing is separately enumerated in `coverage-ledger.json`.
No gap is removed from source offsets. Label-like regions outside these broad
intervals are conservatively marked as candidates, not declared nonspeech.

## Editorial omissions and retained substance

| Material | Treatment | Source scope |
| --- | --- | --- |
| Filler, false starts, screen-switch instructions and repeated promotional countdowns | Condensed while retaining substantive instructions, expiry corrections and promotional promises as unverified reports | Across all timed chapter sections; especially C01, C12, C31 |
| Card-by-card arithmetic, rank banter, player handles | Condensed/handles omitted; rules, UI defects, changed behavior and numeric contradictions retained | C01/C06/C19/C21/C28/C29/C31/C33 |
| Private account contacts, phone numbers, destination links, account identifiers and possible credentials | Not reproduced; safe roles and event descriptions used instead | C02-C04, C15-C18, C20, C24, C28, C31, C33 |
| Repeated capability promotion | Condensed within each exchange; actual requests, nudges, limitations and failed results retained | RevOps, post-sales and marketing workshops |
| Garbled names, counts, brief side comments and overlapping turns | Unresolved or grouped, never silently corrected into a confident fact | Exact groups in chapters and entity/review ledgers |
| Jokes, lyric-like material and personal anecdote detail | Purpose/context retained where useful; wording and incidental personal detail omitted | C10/C12/C18/C20/C24/C27/C29-C33 |
| Earlier-day recap montage | Retained as replay fragments, not new Day 3 actions or cross-day proof | C22, 05:29:23.960-05:30:53.468 |
| Blake's final answer | Truncated thought retained as incomplete; no ending supplied | C18, 04:46:34.104-04:46:51.096 |

There are no deliberately unread parts. The intent is to retain every
substantive recognized exchange, not every token. Grouped paraphrases are less
detailed than raw ASR and require human review for semantic omissions. The
mechanical routing does **not** certify that intent was perfectly achieved.

## Review-required gaps in proof

- No audio listening: absent/quiet speech, overlapping speakers, non-English
  content and uncertain names/numbers cannot be recovered in this pass.
- No inspected screens: all screenshots, browser actions, PRs and charts are
  reported in transcript text, not observed directly by this curator.
- No independently checked external actions: payments, customer results,
  outreach, production fixes, permission changes and data accuracy remain claims.
- Original video transport was already removed upstream; retained audio and
  manifests cannot independently re-establish every source-transport property.
- No caption inputs were read and no X-to-YouTube alignment was attempted.
- No synthesis of decisions, lessons or progress is included. Speaker reflections
  are retained as conversation, not promoted into editorial conclusions.
