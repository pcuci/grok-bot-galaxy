# Knowledge-base layout

This is the complete planned Markdown layout, not a claim that all documents
exist. Foundation pages are present; event analysis, registries, workflows, and
cleaned conversations will be authored after processing permission and evidence
review. Do not create empty analyses that imply work is complete.

## Repository boundaries

- `README.md`: purpose, status, navigation, and local evidence access.
- `ROADMAP.md`: sequenced work with verifiable exit criteria.
- `AGENTS.md`: repository-owned authority and evidence policy.
- `.agents/`: reusable instructions and optional governance imports, not event data.
- `.data/day-01/`: ignored extracted M4A, half-hour WAVs, raw ASR, runner, VAD.
- `.data/audio-quality/`: ignored local codec experiments and interrupted outputs.
- `audio/day-01/`: intended compact Opus parts and manifest; preparation pending.
- `scripts/`: tested compact-audio preparation and validation, not an ASR replacement.
- `docs/`: all event-facing Markdown, including cleaned conversations.

There is no second `clean/` tree. `docs/days/day-01/transcripts/` will hold the
cleaned, annotated conversation organized by meaning rather than processing
chunks. Raw `.data/day-01/transcripts/` remains unchanged and ignored by Git.

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
  - `transcripts/`: the thirteen proposed chapters listed below.
- `days/day-02/README.md`: pending only; expand after acquisition and review.
- `days/day-03/README.md`: pending only; expand after acquisition and review.
- `templates/`
  - `day-overview.md`
  - `transcript-chapter.md`
  - `reusable-workflow.md`

When new days have authorized evidence, instantiate the same day-level artifact
set as Day 1, choosing chapter filenames and boundaries from those recordings.
Do not predict future chapter titles, participants, decisions, or results.

## Tentative Day 1 chapters

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
