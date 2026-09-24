# Day 2 coverage and omission ledger

Status: **ASR-based review draft**. No audio was reviewed. Coverage below accounts
for source time and editorial treatment, not verified speech completeness.

## Exact machine accounting

[coverage-ledger.json](coverage-ledger.json) is the exact interval ledger:

| Measure | Result | Meaning |
| --- | --- | --- |
| PCM timeline | 08:23:18.528 | Preserved source-relative duration |
| Chapters / topic sections | 26 / 174 | Contiguous editorial routing, including gaps |
| JSON recognition regions | 4119 | Every region has a primary chapter and section intersections |
| Nonempty / empty regions | 4113 / 6 | Empty regions remain accounted for even though TXT/SRT omit them |
| Label-only candidates | 296 | Mechanical bracket/parenthesis heuristic, not audio classification |
| Other text-present regions | 3817 | May still include errors, filler, repetition or hallucinations |
| Recognition-region duration | 07:00:58.048 | 25258.048 seconds, including label/empty regions |
| No-region duration | 01:22:20.480 | 4940.480 seconds across 4102 intervals |

Region duration plus no-region duration equals the full PCM duration exactly.
Neither duration is a count of actual speech or silence. The 4102 intervals
include ordinary small VAD gaps, production waits and long breaks; they are not
4102 proven ASR failures. Every interval has millisecond coordinates and a stable
`D2-GNNNN` ID in the machine ledger.

Raw JSON regions have `D2-PNN-RNNNN` IDs and SHA-256 of their original text.
They are routed by source interval, not duplicated when crossing a topic cut.
No raw text is copied into the ledger. Time coverage proves where to review,
not that a paragraph retains every semantic nuance.

## Large or explicit non-conversation intervals

These review windows are editorial groups, not additional disjoint time buckets.
They overlap the exact region/gap accounting above and must not be summed again.

| Source interval | Treatment | Review need |
| --- | --- | --- |
| 00:00:00.000-00:10:03.992 | Opening contains placeholders and no recoverable substantive exchange; C01 retains an explicit gap section. | Determine whether there was music, silence or missed speech. |
| 01:40:25.240-01:48:11.160 | C05 preserves waiting/technical-difficulty remarks; 01:41:32.016 onward is unrecoverable interruption coverage. | Check production interruption and any background speech. |
| 02:30:00.000-02:39:03.512 | C09 accounts for continuation of announced break. | No verified silence; inspect any missing speech. |
| 03:03:48.124-03:10:47.384 | C09 retains post-interview gap with clipped fragment. | Check exact return boundary and background content. |
| 04:32:50.128-04:43:49.368 | C14 omits music/lyric-like repetition rather than reproducing lyrics or inventing dialogue. | Audio needed to distinguish music from missed background conversation. |
| 05:59:30.512-05:59:52.376 | Stage handoff without a recovered exchange; C17 includes transition. | Verify introduction boundary. |
| 06:39:29.040-06:39:49.016 | Stage-to-studio placeholders after naming aside; C19. | Check mixed speech and return cut. |
| 07:30:30.032-07:30:46.392 | Host-to-support-workshop handoff; C22. | No silence asserted. |
| 08:09:47.224-08:10:43.032 | C25 retains closing plus unrecovered production chatter and placeholders. | Verify speaker change and any substantive lost words. |
| 08:20:01.232-08:23:18.528 | C26 sparse outro; music/wind labels and a short unrecovered fragment at 08:22:42.488-08:22:43.824. | Check end content; no imagined post-stream play or deployment. |

## Condensation, unavailable meaning and privacy exclusions

These entries describe what was not reproduced verbatim and why. All chapter
text is nonverbatim. Times identify review windows; they are not claims that
every second in the window was omitted.

| Source interval / chapter | Omitted or condensed material | Substantive context retained |
| --- | --- | --- |
| Throughout, all 17 parts | Filler, acknowledgements, repeated setup language, screen-navigation instructions, routine waiting and phonetic noise. | Requests, objections, corrections, changed direction and reported limits. |
| 01:23:56.184, C04/C05 boundary | One recognition region mixes final workshop answer and host return. | Marked as mixed; no fabricated clean speaker cut. |
| 02:13:22.264-02:15:30.264, C07 | Incidental child/family details. | Marcel/Rex business-use account remains a testimonial, not measured results. |
| 02:39:03.512-03:03:48.124, C09 | Health self-description, incidental personal/access details, uncertain public URL and garbled vacation fragment. | Screen-overload motivation, printing surprise, unfinished plotter and login friction. |
| 03:30:40.216-03:33:56.824, C11 | Long repetitive ASR phrase not recoverable as a meaningful exchange. | Code-driven avatars versus generated ability icons. Audio needed for lost meaning. |
| 03:38:01.944-03:41:19.544, C11 | Unclear specialist/model names. | Durable instructions, stale preview and comment-cleanup rationale; no invented tool names. |
| 04:15:47.800-04:23:32.024, C13 | Garbled restaurant/topic fragment and partially missing initial audience question. | Requests for finished research, contrasting routine preferences and usage caveats. |
| 04:46:43.704-05:05:13.016, C14 | Family/school specifics, private account/customer details, transaction contacts and incidental health/billing detail. | Coordination, sales reports, prospective utility estimate and security caveats. |
| 05:09:55.128-05:13:11.832, C15 | Unrecovered staffing figure/title wording. | Claimed initial code analysis distinguished from complete migration. |
| 05:18:28.600-05:22:07.864, C16 | Contact records and private directory/access detail; no guessed recruiter handle. | Privacy caution and outreach proposed, not sent. |
| 05:56:06.392-05:58:26.716, C17 | Uncertain guest handle and extended profile-photo banter. | Candidate name, portfolio encouragement, no hire claim. |
| 06:14:03.640-06:31:14.104, C19 | Prospect contact/CSV data and uncertain tool spellings. | Ranking, human review, unsequencing and evolving ICP. |
| 06:39:13.848-06:39:29.040, C19 | Personal naming joke generalized; no religious identity inferred. | Brief audience aside remains in chronology. |
| 06:50:57.208-06:51:14.584, C20 | Connection/secrets setup moved off-screen by presenters. | Setup incomplete at that point; no secrets reconstructed. |
| 06:54:16.408-06:56:22.072, C20 | Incidental account/family details and uncertain names in secondhand examples. | Printing, payment and marketplace reports remain secondhand. |
| 07:10:29.880-07:13:43.416, C21 | Screen-only game recommendations and poorly recognized skill names. | Critique of AI-like prose, engineer handoff and canonical-doc request. |
| 07:24:33.656-07:29:19.864, C22 | Visual/audio assets are not reconstructable from ASR. | Host feedback, uncertain fit and sound-design request. |
| 07:47:27.960-07:58:53.624, C24 | Customer IDs, access details, waiting and an unspecified skipped demo step. | Refund difference, human-supplied FAQ policy, permission gate and Slack retry. |
| 08:10:43.032-08:14:09.080, C26 | Music itself and garbled/contradictory preference fragments. | Subjective reactions, candidates not final selection; no generated lyrics. |
| 08:14:09.080-08:15:37.368, C26 | Incidental X account handles. | Login reports, import bug and leaderboard issue. |
| Repeated promotional sections in C12/C13/C17/C20/C22/C26 | Repetitive sales wording and guessed QR/entry links. | Offer/contest announcements retained as unverified historical claims. |

No known substantive recoverable session was intentionally dropped. However,
ASR errors and grouped editorial paraphrase prevent a claim of exhaustive speech
preservation. Screen-only data and quiet/overlapping dictation cannot be restored
from these inputs. Consequential omissions and claims remain in the
[review queue](review-queue.md), with [editorial changes](editorial-change-log.md).

## Review method still required

A reviewer with authorized audio access should inspect all empty/label candidates,
large gaps, mixed boundaries and consequential claims, then record exact findings.
Review the original timeline without removing breaks. Repetition alone is not a
basis to delete aligned evidence; this pass removed no raw records and made no
cross-part duplicate deletion. No coverage gap was filled with a guessed quote.
