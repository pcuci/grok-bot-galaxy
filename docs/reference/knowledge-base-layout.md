# Knowledge-base layout

This is the complete planned Markdown layout, not a claim that all documents
exist. Foundation pages, all three days' ASR-based curation drafts and one
provisional SDR session review are present. Audio-verified acceptance, day-level
synthesis and cross-day registries/workflows remain pending. Do not create empty
analyses that imply work is complete.

## Repository boundaries

- `README.md`: purpose, status, navigation, and local evidence access.
- `ROADMAP.md`: sequenced work with verifiable exit criteria.
- `AGENTS.md`: repository-owned authority and evidence policy.
- `.agents/`: reusable instructions and optional governance imports, not event data.
- `.data/day-01/`: ignored extracted M4A, half-hour WAVs, raw ASR, runner, VAD.
- `.data/youtube/`: temporary ignored session captions and full-text Markdown;
  preserve their separation from concise reviews in `docs/`.
- `.data/audio-quality/`: ignored local codec experiments and interrupted outputs.
- `audio/day-01/`: intended compact Opus parts and manifest; preparation pending.
- `scripts/`: tested compact-audio preparation and validation, not an ASR replacement.
- `docs/`: all event-facing Markdown, including cleaned conversations.

There is no second `clean/` tree. Each `docs/days/day-XX/transcripts/` holds
nonverbatim, annotated conversation drafts organized by meaning rather than
processing chunks. Raw `.data/day-XX/transcripts/` remains unchanged and ignored
by Git.

## Complete documentation inventory

Paths below are relative to `docs/`.

- `README.md`: navigation and evidence conventions.
- `event-overview.md`: event purpose, format, constraints, and demo-company roles.
- `timeline.md`: chronology with breaks, milestones, and explicit coverage gaps.
- `decision-index.md`: cross-day decision lineage and reversals, not just advice.
- `lessons.md`: portable practices grounded in observed results and limitations.
- `open-questions.md`: unresolved product, attribution, evidence, and outcome issues.
- `reference/`
  - `people.md`: human IDs, backgrounds, contributions, aliases, and evidence.
  - `bots.md`: bot instance IDs, owners, purposes, addressees, and uncertainty.
  - `terminology.md`: recurring terms and ASR correction candidates.
  - `public-sources.md`: official schedule and public context, rights and retrieval notes.
  - `editorial-method.md`: transformations, attribution, review, and coverage rules.
  - `youtube-sessions.md`: session source inventory and caption validation status.
  - `session-analysis.md`: skill map, review cycle, and session-to-day synthesis.
  - `audio-storage.md`: local originals, compact codec choice, tests, and preparation.
  - `agent-workspace.md`: standards choices and optional governance maintenance.
  - `knowledge-base-layout.md`: this plan and tentative semantic chapter map.
- `workflows/`
  - `README.md`: how to use evidence-backed workflow notes.
  - `human-bot-communication-and-delegation.md`
  - `bot-creation-onboarding-and-specialization.md`
  - `shared-context-memory-and-playbooks.md`
  - `research-to-business-validation.md`
  - `engineering-delivery-and-verification.md`
  - `analytics-to-product-delivery.md`
  - `customer-feedback-and-founder-operations.md`
  - `event-planning-and-human-approvals.md`
- `days/day-01/`
  - `README.md`: scope, inputs, review state, and navigation.
  - `sources.md`: provenance, processing, hashes, validation, and rights status.
  - `progress-and-outcomes.md`: requested/reported/demonstrated/blocked work.
  - `decisions.md`: consequential choices with rationale, alternatives, and changes.
  - `lessons-and-failures.md`: what worked or failed and the strength of evidence.
  - `review-queue.md`: attribution, coverage, rights, and claim-review backlog.
  - `transcripts/`: 32 ASR-based draft chapters that supersede the thirteen
    proposed below; see the [Day 1 index](../days/day-01/transcripts/README.md).
- `days/day-02/`, `days/day-03/`: same artifact set as Day 1 (curation drafts
  present; synthesis files pending), plus `entities.md`, `gap-ledger.md`,
  `editorial-change-log.md`, `coverage-ledger.json`, `input-inventory.json`
  and `validation.json`. Day 1 now has the same curation-draft files
  (2026-09-24); its synthesis files remain pending.
- `templates/`
  - `day-overview.md`
  - `transcript-chapter.md`
  - `session-review.md`
  - `reusable-workflow.md`

For individual session reviews, add
`days/day-XX/sessions/<topic>-<video-id>.md` under the relevant day when review
starts, and link it from that day's `README.md` with its review state. These
concise, nonverbatim reviews complement full-day chapters; they do not duplicate
full transcripts or imply complete day coverage. See the
[session analysis guide](session-analysis.md) and
[session review template](../templates/session-review.md). Create substantive
reviews, not a directory of placeholder reports.

When new days have authorized evidence, instantiate the same day-level artifact
set as Day 1, choosing chapter filenames and boundaries from those recordings.
Do not predict future chapter titles, participants, decisions, or results.

## Tentative Day 1 chapters

**Superseded 2026-09-24** by the 32-chapter ASR-based draft in the
[Day 1 transcript index](../days/day-01/transcripts/README.md); the mapping and
boundary changes are in the
[Day 1 editorial log](../days/day-01/editorial-change-log.md#chapter-map-changes),
and every gap below is dispositioned in the
[Day 1 gap ledger](../days/day-01/gap-ledger.md). The table is retained as the
inherited plan.

These boundaries and names are inherited planning notes, **not newly verified
attribution or audio-reviewed segmentation**. All times are recording-relative,
not wall-clock schedule times. Use half-open intervals at shared boundaries.
The ending is the validated PCM endpoint, 08:45:12.567375.

| File under `days/day-01/transcripts/` | Proposed interval |
| ----------------------------------- | ----------------- |
| `01-opening-and-team-setup.md` | 00:00:00-00:29:43 |
| `02-grok-bot-101.md` | 00:30:26-01:29:45 |
| `03-peter-yang-research-and-prototyping.md` | 01:31:05-02:24:35 |
| `04-prototype-to-working-application.md` | 02:24:35-02:52:40 |
| `05-codie-sanchez-business-and-distribution.md` | 02:55:28-03:19:31 |
| `06-post-break-engineering-update.md` | 03:48:46-03:53:55 |
| `07-engineering-workshop.md` | 03:54:08-04:39:25 |
| `08-live-build-scope-and-concept-changes.md` | 04:40:13-05:54:10 |
| `09-product-management-workshop.md` | 05:54:10-06:33:17 |
| `10-eric-wei-customers-and-merchandise.md` | 06:41:15-07:23:11 |
| `11-founders-workshop.md` | 07:23:30-08:18:17 |
| `12-jenny-event-planning-and-operations.md` | 08:20:13-08:41:48 |
| `13-day-one-retrospective.md` | 08:41:49-08:45:12.567375 |

Every interval outside those chapters must also be accounted for. Current gaps:

- 00:29:43-00:30:26
- 01:29:45-01:31:05
- 02:52:40-02:55:28
- 03:19:31-03:48:46 (candidate long break)
- 03:53:55-03:54:08
- 04:39:25-04:40:13
- 06:33:17-06:41:15 (candidate long break)
- 07:23:11-07:23:30
- 08:18:17-08:20:13
- 08:41:48-08:41:49

Review gaps before labeling them silence or breaks. Preserve substantive speech
in a neighboring chapter or a separate transition section; never discard it
solely because the tentative map excludes it. The recording reportedly starts
mid-sentence; retain that limitation until listening review establishes it.

## Extraction order

1. Confirm processing permissions; preserve and inventory source evidence.
2. Review identities and aliases alongside source intervals, not from names alone.
3. Create timestamped, readable conversation with explicit addressees and ambiguity.
4. Audio-review consequential corrections, boundaries, and claims.
5. Derive day-level decisions, outcomes, failures, and lessons from chapters.
6. Derive cross-day indexes and workflows only from reviewed day evidence.

A workflow document must distinguish a suggested practice from one demonstrated
successfully. A chapter must contain recoverable conversation, not a summary
masquerading as a transcript.
