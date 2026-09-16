# Editorial method

## Evidence and processing boundary

Raw ASR stays in ignored `.data/`; cleaned text belongs in `docs/days/`. The local
model performs transcription, not speaker diarization. Before any hosted-model
curation, confirm permission for that actual processing environment. Do not
upload raw audio or transcripts to a third-party service implicitly.

Preserve original bytes, raw JSON/TXT/SRT, and historical runner identity. A
polished version must never replace the machine evidence. Record input file IDs,
hashes or checkpoint identities, exact intervals, and editorial review status.

## Three distinct artifacts

- **Edited conversation:** readable English retaining substantive exchanges,
  uncertainty, corrections, repetition when meaningful, and changes of direction.
  Nonverbatim unless specifically audio-verified. Not a word-perfect record.
- **Summary:** compressed analysis of a source interval, labeled as a summary.
- **Quotation:** exact wording checked against audio, with a timestamp and
  permission to reproduce it. ASR alone cannot establish a verified quotation.

Remove filler only when meaning is preserved. Do not repair an unclear claim
into the claim that seems more sensible. Mark it unresolved and put consequential
uncertainty into the review queue. Log material name, number, and meaning changes.

## Attribution and addressees

For each meaningful turn or group of inseparable turns, capture:

- Source interval and approximate timing precision.
- Audible speaker ID, or unresolved speaker/group.
- Attribution: confirmed, probable, or unresolved; state the evidence basis.
- Addressee: named human, bot instance, audience, or unresolved.
- Interaction type and purpose.
- Claimed content author when a human reads another human's or a bot's output.

Keep these interaction types separate:

1. Human-to-human discussion, question, or advice.
2. Human-to-bot dictated instruction.
3. Human narration of activity.
4. Human reading or paraphrasing bot output.
5. Reported bot-to-bot exchange, not necessarily independently observed.
6. Hypothetical/example prompt.
7. Mixed or background speech without separable attribution.

Use explicit self-introduction, address, and contextual evidence. Voice similarity
or a name appearing in ASR is insufficient. Never fabricate turn boundaries,
precise speaker timestamps, or numeric confidence scores.

A bot name is not a unique identity: different owners may install separate
instances. Keep Lauren's Steve separate from Lingxi's Steve, human guest Jenny
separate from Jenny bot, and similarly named research/prototyping bots separate
until evidence supports a merge. These are inherited review requirements, not
newly confirmed identity findings. Quiet dictation may be absent from ASR.

## Time and coverage

Global time equals part-local time plus `(part_number - 1) * 1800` seconds.
Use the silence-preserving PCM timeline. Do not subtract breaks, concatenate VAD
speech without offsets, or equate wall-clock schedule slots with recording time.
ASR segments are approximate recognition regions, not word alignment.

For each chapter, account for all substantive speech in its interval or mark
omissions, redactions, overlapping speech, and unintelligibility explicitly.
Maintain a gap ledger across chapters. Never infer silence from an empty ASR
result or successful checkpoint completion.

## Claims and outcomes

Use distinct states: proposed, requested, in progress, completion reported,
result demonstrated, blocked, and unresolved. A successful external deployment,
email delivery, or customer outcome needs evidence beyond a dictated request or
bot status message. Keep workshop demos separate from the hosts' live build.

Preserve disagreements and reversals. Demo-company titles must not be mistaken
for real employment titles. Guest advice is not automatically a team decision.
Day 2 and Day 3 remain pending until their own sources are acquired and reviewed.

## Review and sharing

Audio-check representative boundaries and every consequential correction or
claim. Track the interval, reviewer action, finding, and remaining uncertainty;
do not claim listening verification when only ASR was read.

Review shareable derivatives for incidental personal information and secrets.
Exclude or redact sensitive content without destroying lawfully held originals.
Record rights, intended audience, and destination access before publication.
Local possession and public replay availability do not establish redistribution
permission. Git ignore rules are safeguards, not a complete privacy review.
