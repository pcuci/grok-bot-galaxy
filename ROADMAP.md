# Grok Bot Galaxy roadmap

Turn preserved event evidence into a readable account of human-bot teamwork,
with decisions and portable lessons traceable to recording-relative intervals.
Keep historical evidence immutable and future-day claims pending review.

## Phase 1: Evidence foundation (current)

### Epic: Preserve and validate Day 1

Need: The migrated media and checkpoints must remain recoverable without
confusing structural ASR completion with editorial or publication readiness.

- [x] Move Day 1 artifacts out of the dotfiles scratch directory.
- [x] Validate 18 WAVs, checkpoint identities, segment bounds, and combined JSON.
- [x] Match a silence-preserving source decode to concatenated WAV PCM.
- [x] Move originals and raw evidence into ignored `.data/`, preserving all bytes.
- [x] Permit only compact Opus derivatives in ordinary Git; ignore large media.
- [x] Compare 24/32/48 kbps on eight local ASR samples; select 32 kbps provisionally.
- [x] Add a tested derivative preparation/validation CLI.
- [ ] Finish full-event encoding after the five-minute timeout and validate all parts.
- [ ] Record source retention/redistribution rights and intended Git access.
- [ ] Complete the generated source/part/output hash manifest before audio staging.
- [ ] Review quiet/overlapping speech and ASR stability on the actual full-part encodes.

> **Win criteria:** A reviewed provenance manifest identifies source and part
> hashes, rights, and timeline handling; compact parts fully decode with matching
> sample counts; only approved derivatives are eligible for ordinary Git, while
> originals, models, and raw ASR remain ignored.

### Epic: Optional, portable agent guidance

Need: Reusable methods should travel with this repo without making the operator's
personal governance checkout necessary for understanding or processing evidence.

- [x] Add root policy and four event-specific skills.
- [x] Import governance's optional baseline with shared skills and agent definitions.
- [x] Extend the tested, scoped materializer for baseline assets and local overrides.
- [x] Document the tested compact-audio CLI without claiming a portable ASR pipeline.

> **Win criteria:** Agent workspace checks and local-only checks pass; all four
> owned skills remain readable without governance; any published pipeline
> instructions match tested CLI help rather than assumed flags.

## Phase 2: Reviewed Day 1 knowledge base

### Epic: Attributed, readable conversation

Need: Machine ASR has no speaker diarization and cannot reliably distinguish
quiet bot dictation, human conversation, and narrated bot output.

- [x] Confirm hosted-model transcript processing permission (approved 2026-09-24).
- [x] Review the tentative chapter boundaries and account for every gap (ASR text; 32 chapters).
- [x] Establish people/bot instance ledgers with evidence and uncertainty.
- [x] Produce complete edited conversations separately from raw ASR (ASR-based draft).
- [ ] Audio-check consequential corrections, identities, and chapter boundaries.
- [x] Track omissions, redactions, attribution uncertainty, and coverage explicitly.

> **Win criteria:** Every chapter has source intervals and qualified attribution;
> all substantive speech is represented or explicitly marked omitted/unresolved;
> consequential claims have audio-review evidence and raw files remain unchanged.

### Epic: Decisions, outcomes, and transferable workflows

Need: A demonstration or instruction must not become an unsupported claim that
the live-build team shipped or independently verified a result.

- [ ] Derive the timeline, progress, decisions, failures, and lessons from chapters.
- [ ] Separate live-build outcomes from workshop demonstrations and guest advice.
- [ ] Link reusable workflows to evidence, caveats, and human approval boundaries.
- [ ] Validate Markdown links and review unresolved claims before sharing.

> **Win criteria:** Every substantive synthesis claim links to reviewed evidence;
> requested, reported, demonstrated, and blocked states remain distinct; open
> questions and disagreements remain visible.

## Phase 3: Days 2 and 3 (curation drafts done)

### Epic: Extend only with reviewed evidence

Need: The knowledge base must grow with reviewed evidence rather than filling
future days with predictions or assuming that time passing proves completion.

- [x] Acquire Day 2 and Day 3 under private-study authorization.
- [x] Validate, chunk, and locally transcribe both days.
- [x] Produce ASR-based curation drafts (Day 2: 26 chapters; Day 3: 33).
- [ ] Audio-review consequential claims, identities, and boundaries per day.
- [ ] Run event synthesis per day before adding outcomes.
- [ ] Build cross-day decision histories without overwriting earlier uncertainty.

> **Win criteria:** Each day has its own provenance, validated parts, reviewed
> chapters, and evidence-linked outcomes, or remains explicitly pending.

## Future vision

- A practical reference for designing accountable human-bot teams.
- Comparable examples of delegation, memory, verification, and recovery.
- Lessons that distinguish generalizable practices from event-specific anecdotes.
