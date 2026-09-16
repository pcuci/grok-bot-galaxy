---
name: transcript-curate
description: Curate raw event transcripts into evidence-linked semantic chapters with probable speaker attribution, separate human and bot identities, and clear distinctions between requests, bot output, advice, and observed actions. Use after local ASR without overwriting raw evidence.
---

# Transcript curate

Read `../../../AGENTS.md`. Confirm raw transcript processing is authorized for
this agent's actual hosting environment; local ASR does not make subsequent
remote-model curation local. Keep event artifacts under `docs/` and raw machine
outputs under ignored `.data/`.

## Establish the evidence boundary

1. Inventory source audio, source IDs/hashes, transcript run/checkpoint IDs,
   coverage gaps, timing precision, and existing day documents. Preserve raw
   transcripts and originals byte-for-byte. Work in a separate derivative.
2. Discover existing documentation conventions and script interfaces. Do not
   invent CLI flags or assume every half-hour part has a completed transcript.
3. State whether the result is a nonverbatim summary, edited transcript, or
   audio-verified quotation. ASR text alone is not a verified quote.

## Chapters and attribution

- Build semantic chapters around topic changes, demonstrations, questions, and
  decisions, not around arbitrary half-hour boundaries. A chapter may cross
  parts; cite every contributing source interval. Keep a chronological index
  even when thematic chapters revisit earlier discussions.
- Maintain an entity/alias ledger with separate IDs for human Steve, bot Steve,
  human Jenny, and bot Jenny when those labels occur. These are disambiguation
  categories, not assertions that all four participated. Keep uncertain entities
  unresolved; do not merge them by spelling, voice similarity, or context alone.
- Record attribution as confirmed, probable, or unknown, with the actual basis:
  self-introduction, explicit address, visible labels if legitimately available,
  or contextual inference. Voice similarity is not identity proof. Do not invent
  speaker diarization or numerical confidence unsupported by the pipeline.
- Separate the audible speaker from the quoted/generated author. A human
  reading a bot response remains the human speaker, with the bot as claimed
  output origin. Record ambiguity if it is unclear who produced the content.
- Classify utterances and summaries as human request/question, human observation,
  bot/generated output, quoted third-party statement, proposed advice, or
  observed action/result. Advice and predictions are not decisions or executed
  actions; a bot's success claim is not independent verification.

## Editorial procedure

1. For each chapter record title, source ID, source-relative start/end, input
   transcript/version, summary, attribution with basis, and uncertainty/gaps.
2. Correct names, numbers, and material claims only against evidence. Retain
   inaudible/uncertain markers; record consequential corrections and timestamps
   in an editorial change log. Do not silently improve what someone said.
3. Reconcile chunk-overlap duplicates using time alignment and listening. Keep
   intentional repetition and repeated demonstrations; identical wording alone
   is not enough to delete evidence.
4. Use minimal audio-verified quotations only when necessary and authorized.
   Otherwise paraphrase without quotation marks and label it nonverbatim.
5. Exclude or redact incidental personal/sensitive content from shareable
   derivatives without destroying lawfully retained originals. Link to restricted
   evidence by safe ID instead of copying secrets or private data.

## Acceptance and handoff

Check that every substantive summary has a source interval, chapter ranges are
valid, attribution is qualified, bot/human identities remain distinct, and no
unprocessed gap has been filled with invented content. Verify representative
boundaries and all consequential claims against audio. Pass chapters, entity
ledger, coverage, editorial changes, and open questions to `event-synthesize`.
Report unresolved speakers and contradictions rather than guessing.
