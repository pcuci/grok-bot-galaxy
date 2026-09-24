# Day 1 editorial change log

Status: **ASR-based review draft**. This log describes derivative
transformations; raw originals remain unchanged. Source identity and input
hashes are in [sources](sources.md), [inventory](input-inventory.json) and the
[chapter index](transcripts/README.md).

## Processing and scope

The operator explicitly approved editor-hosted model curation of Day 1 raw ASR
on 2026-09-24 for private study, on the same basis as Days 2 and 3. All 18 TXT
parts were read in full; JSON supplied exact region intervals. No transcription
rerun, network request, caption input, event synthesis or Git operation was used.
Writes were limited to `docs/days/day-01/**` plus the Day 1 status lines in the
root README, docs index, layout reference and roadmap.

## Chapter map changes

The inherited 13-chapter plan was used as a starting point. Its boundaries were
checked against region timing and content, then split where topics changed.

| Inherited chapter | Draft chapters | Main change and reason |
| --- | --- | --- |
| 01 opening and team setup | C01-C02 | Split introductions from goals/tools/setup; end moved to the 101 start so the handoff gap is inside C02 |
| 02 Grok Bot 101 | C03-C06 | Split principles, demo, failed QR access and Q&A; the following gap sits in C06 |
| 03 Peter Yang research and prototyping | C07-C09 | Split idea research, pop-up convergence and prototype/dogfooding plus Peter's advice |
| 04 prototype to working application | C10-C11 | Split roles/repo setup from deploy/database/domain/main rule; hold-screen gap in C11 |
| 05 Codie Sanchez | C12-C13 | Split advice from the bot exercise; the long break is C13's final group |
| 06 post-break engineering update | C14 | Start moved to the first post-break region (03:48:44.024) |
| 07 engineering workshop | C15-C16 | Split principles from the fleet demo; transition inside C16 |
| 08 live build scope and concept changes | C17-C21 | Five chapters for review/verification, core-flow debate, venue tool, knowledge manager and the art pivot |
| 09 product management workshop | C22-C23 | Split framing from demo and Q&A; the eight-minute gap is inside C23 |
| 10 Eric, customers and merchandise | C24-C26 | Split audience narrowing, merch novelty and build-a-Grok-Bot/platform advice |
| 11 founders workshop | C27-C29 | End moved from 08:18:17 to 08:18:43.640 because Shub's closing continues past the old boundary |
| 12 Jenny event planning | C30-C31 | Start moved to 08:18:43.640 so the remote-audio transition is the first group |
| 13 day-one retrospective | C32 | Start 08:41:48.664, the first retrospective region; ends at the exact PCM endpoint |

## Transformations

- Paraphrased ASR into 151 timed groups with speakers, addressees, interaction
  types and claimed output authors; all groups are half-open and contiguous.
- Removed filler and repetition loops without turning requests, plans or bot
  status messages into verified actions.
- Grouped inseparable host turns instead of inventing diarization.
- Normalized obvious product names (Grok Bot, Cursor, PlanetScale, Vercel,
  Notion, Resend) where context is clear; consequential spelling and identity
  ambiguities remain explicit.
- Did not deduplicate repeated demonstrations or repeated contest reminders
  across separate times. Parts are contiguous without intentional overlap.
- Omitted incidental handles, email-address requests and personal details.
- Standardized editorial punctuation to ASCII. Raw text is untouched.

## Consequential editorial choices requiring review

| Source interval | Chapters | Choice, basis and unresolved question |
| --- | --- | --- |
| 00:00:00.000-00:00:25.152 | C01 | Mid-sentence start retained as a limitation; no reconstructed opening |
| 00:17:27.896-00:21:36.312 and 02:49:44.152-02:52:40.336 | C02, C11 | Direct-to-main intentions retained, then contrasted with PR-review work in C14/C17 |
| 01:00:00.248-01:10:59.160 | C04-C05 | Live survey access failure kept separate from sample/test data used for email and chart |
| 01:32:20.696-01:37:17.976 | C07 | Market-research bot owner probable Roshan from screen context |
| 02:12:23.000-02:17:44.440 | C09 | Run-our-own-pop-up recorded as conversational agreement, not formal decision |
| 02:27:43.000-02:30:36.280 | C10 | Demo-company titles labeled as stream roles, not employment |
| 02:39:00.696-02:52:40.336 | C11 | Main deployments, database choice and domain purchase recorded as reported states |
| 03:10:20.728-03:14:02.776 | C13 | Operator-research bot narrator/owner attributed as probable Matt |
| 03:19:30.960-03:48:44.024 | C13 | Break duration mismatch retained |
| 03:50:17.912-03:52:31.384 | C14 | Hash Brown's creation during the break kept as a report |
| 04:18:11.384-04:21:28.920 | C16 | Lingxi's Steve rename left ambiguous; 4 a.m. vs 3 a.m. audit timing retained |
| 04:21:28.920-04:35:33.304 | C16 | Workshop bot Jenny separated from human guest Jenny |
| 04:52:26.072-04:55:12.056 | C17 | Database connection is reported; no entries inspected |
| 05:05:47.864-05:07:38.168 | C18 | October 15 labeled working date, not booked event |
| 05:17:29.784-05:36:51.640 | C20-C21 | Knowledge manager passive configuration then five-minute polling, both preserved |
| 05:39:34.200-05:49:47.864 | C21 | Art exhibition kept as considered pivot, later displaced by merch discussion |
| 06:15:12.952-06:17:32.248 | C23 | Funnel correction: audible human speaker unresolved; Ashley as claimed author |
| 06:47:00.728-06:49:56.792 | C24 | Tech-brand merch start labeled tentative; Matt's simplicity objection preserved |
| 06:55:36.888-07:02:07.832 | C25 | Contradictory tungsten-cube prices preserved |
| 07:12:13.400-07:16:17.688 | C26 | Two independently named Drop bots kept separate |
| 08:31:39.736-08:41:48.664 | C31 | Budget bot fired without shown output; permit bot and social-account access remain advice |
| 08:43:39.352-08:44:55.984 | C32 | Closing doubt about the pop-up problem kept; no final concept inferred |

All chapter IDs resolve through the [index](transcripts/README.md); ownership and
alias decisions are in [entities](entities.md). No correction in this pass is
labeled audio-verified. The [review queue](review-queue.md) holds unmet gates.
