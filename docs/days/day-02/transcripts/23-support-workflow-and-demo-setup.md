# D2-C23: Customer-support workflows and the Flylo demo environment

## Source and review state

- Source: X `1PKqrNyvmYwGb`; [sources](../sources.md).
- Interval: [07:30:46.392, 07:43:06.776).
- Input: `part-16.json` local [00:00:46.392, 00:13:06.776), under
  `.data/day-02/transcripts/`; TXT read in full.
- **ASR-based review draft**, nonverbatim; no audio/screen verification.
- Speaker: probable David, self-introduced at 07:30:52.216 as an engineer in user
  operations; surname and exact employer wording unresolved. Addressee: audience.
- Flylo is explicitly a pretend airline; its support policy is not the hosts'
  company policy. Build, Reply, Alert and Tune are demonstration bot identities.

## Orientation

David presents a staged approach to support automation, then introduces a
simplified environment for the examples in C24.

## Edited conversation

### 07:30:46.392-07:35:21.016 | Delegation, routines and integration claims

**Speaker:** probable David to audience. **Type:** introduction and product
explanation, not a benchmark of every claimed capability.

David plans a demo-heavy workshop with questions afterward. He describes a
messenger-like interface for delegating work that continues after the initial
message, with either one general bot or a team of specialists. A separate
computer lets bots work without occupying the user's local machine.

Scheduled and event-triggered routines can start work while the user is offline.
He names ticketing, Slack and knowledge-base connections and suggests cloud
agents can build missing pieces. These are capability claims and suggested
approaches, not proof that all connectors exist or can safely be built for every
service without additional permissions.

### 07:35:21.016-07:36:40.024 | Read, draft, then consider replying

**Speaker:** probable David. **Type:** safety-oriented workflow advice.

David acknowledges that letting an agent reply to customers can be uncomfortable.
He recommends starting with reading tickets and identifying the issue, then
creating draft notes that a human can inspect before sending, and only later
allowing replies when confidence is justified.

He recommends evaluations and traces to inspect behavior before publication.
These are proposed controls, not a guarantee that a model's confidence score is
correct or that every action is protected by an enforced permission boundary.

### 07:36:40.024-07:39:31.640 | Alerts, internal questions and improvement

**Speaker:** probable David. **Type:** use-case explanation and hypothetical examples.

A support queue may contain urgent cases that are hard to spot. He proposes
routines that identify a churn threat from a long-standing customer and alert a
Slack channel. The example's customer age and hourly schedule are illustrative,
not evidence of a particular customer or measured detection performance.

He also wants teammates to query the knowledge base, including internal policy
that should not be sent to customers. A sales teammate preparing for a call and
a manager asking about refund-policy changes are examples. Finally, he suggests
reviewing traces and prior tickets for missed alerts or poor handling and
proposing improvements. This does not authorize autonomous policy changes.

### 07:39:31.640-07:40:33.720 | Four demo roles, not a required starting architecture

**Speaker:** probable David. **Type:** demo setup and advice.

Build handles setup/infrastructure; Reply answers tickets and internal questions;
Alert posts escalations; Tune helps improve the system. David explicitly says
users need not predesign this team. He recommends starting with one workflow and
splitting responsibilities when scope or parallelism requires it. That qualification
matters alongside the more elaborate teams shown earlier in the day.

### 07:40:33.720-07:43:06.776 | Public docs, private policy and synthetic tickets

**Speaker:** probable David. **Type:** narrated demo environment.

He shows a Notion knowledge base with public product/authentication/billing
material and separate internal procedures. Flylo is a pretend airline, simplified
to a monthly Wi-Fi subscription described as $20. A demonstration refund policy
approves requests within 14 days and denies later ones. These are synthetic
workshop rules, not verified legal terms, host-product pricing or a real airline's
policy.

Reply's loop is described as reading the ticket and knowledge, deciding whether
to reply or hand off, then leaving a note. Example tickets are prefilled in a
system rendered Plain in context, with Stripe and Slack ready for later steps.
The presenter says some connectors were prepared in advance. This is not a
from-zero integration demonstration and no customer IDs or access details are
copied into this derivative.

## Editorial changes and unresolved evidence

- Kept simulated airline pricing, refund terms and ticket identities separate
  from real host-company operations.
- Distinct human narrator and four claimed bot authors/workers throughout.
- Capability and safety assertions require audio and independent product checks.
- No real customer evidence, connector configuration or credentials reproduced.
