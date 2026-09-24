# D2-C25: Support costs, traces and enterprise guardrails

## Source and review state

- Source: X `1PKqrNyvmYwGb`; [sources](../sources.md).
- Interval: [08:00:02.072, 08:10:43.032).
- Input: `part-17.json` local [00:00:02.072, 00:10:43.032), under
  `.data/day-02/transcripts/`; TXT read in full.
- **ASR-based review draft**, nonverbatim; no audio reviewed.
- Speakers: probable David, unresolved audience questioners and an unresolved
  moderator relaying questions from X. Addressees: one another and viewers.

## Orientation

The Q&A qualifies costs and describes ways to inspect and govern support changes.
Those suggestions are not proof of enterprise-wide enforcement in the demo.

## Edited conversation

### 08:00:02.072-08:02:27.320 | Cost depends on the loop

**Speakers:** questioner asks; probable David responds. **Type:** pricing question
and personal estimates, not an official tariff or audited benchmark.

David says usage draws on subscriptions, with exact plan relationships unclear
in ASR. Classifiers, traces and evaluations change the cost. He estimates roughly
$1-$2 for medium-to-complex tickets in his setup and describes experiments batching
low-complexity cases with scripts that reduced those to about $0.20 per ticket.

He compares this with other support products and human handling, but supplies no
controlled comparison. Ticket complexity, what counts as a resolution and the
small amount of optimization work are material qualifications. Do not treat the
figures as a general price guarantee or realized savings for the hosts' studio.

### 08:02:27.320-08:04:22.744 | Inspect traces before claiming self-improvement

**Speakers:** questioner and probable David. **Type:** debugging Q&A.

Asked how to investigate failures between multiple bots, David describes eval
and trace tables in Postgres, connected through Supabase and initially arranged
with Build. Traces record run timing and which sources were inspected or selected;
tests can be rerun after changes. He says even dry-run ticket notes should leave
traces, not just customer-facing answers.

The questioner asks whether this is bot configuration or a separate overseer.
David explains the connector/setup approach and suggests Tune can inspect those
records for improvements. He says this infrastructure was not shown in the demo;
no database contents or coverage guarantees are independently verified here.

### 08:04:22.744-08:05:10.776 | Phone support is not demonstrated

**Speakers:** questioner and probable David. **Type:** capability question and
limited-experience answer.

Asked about a bot with a phone for customer support, David says he has not done
much of it. He recalls a video by Matt involving a phone number and a reservation,
and invites further experimentation. This is a reference to another example,
not evidence that a support-phone system was deployed or tested in this session.

### 08:05:10.776-08:08:00.312 | Nontechnical access and reviewed knowledge changes

**Speakers:** questioner challenges; probable David responds.
**Type:** risk question and proposed controls.

The questioner worries that easy bot creation could let nontechnical users damage
production databases or issue inappropriate refunds. David says setup should
involve someone aware of the architecture and constrained templates, such as
requiring approval before knowledge-base updates. He mentions future multiplayer
work as a direction, not a current guarantee.

He proposes storing knowledge in a GitHub-style workflow so changes can use
branches, PRs, code owners, automated review and human approval. Evaluations can
run against the proposed branch before merging. This is a suggested governance
pattern, not proof that prompt-only constraints prevent all unauthorized writes
or that these controls were active in the demonstrated environment.

### 08:08:00.312-08:09:47.224 | Specific IDs and the common support cases

**Speakers:** moderator relays viewer questions; probable David answers.
**Type:** optimization and onboarding advice.

Asked about batching, David says it can help and notes his demo request to reply
to a first name forced extra searches through tickets. Providing exact ticket
IDs can avoid listing/searching all open tickets. The explanation is a mechanism,
not a measured benchmark for every batch size.

Asked what the hosts' new company should set up first, he recommends identifying
the common issues that generate most volume, documenting them with good SOPs,
and testing/evaluating those answers. His 80/20 framing is a heuristic, not
measured support data for this not-yet-launched game.

### 08:09:47.224-08:10:43.032 | Handoff with an unreviewed transition

**Speakers:** probable David closes; background/studio fragments unresolved.
**Type:** transition and coverage gap.

David returns the stream to the studio. The remaining ASR consists of silence
labels and brief unclear production chatter about showing a screen. These are
not repaired into a substantive exchange or certified as silence. See the
[gap ledger](../gap-ledger.md) for exact recognition and uncovered intervals.

## Editorial changes and unresolved evidence

- Cost figures remain personal estimates with complexity and batching qualifiers.
- Future/team controls and suggested PR governance are not deployed controls.
- Traces were described, not inspected; phone example is secondhand.
- All numerical, safety and identity claims remain pending audio review.
