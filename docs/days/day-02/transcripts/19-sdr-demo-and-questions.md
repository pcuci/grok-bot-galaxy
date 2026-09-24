# D2-C19: Prospect routines, research scaling and SDR questions

## Source and review state

- Source: X `1PKqrNyvmYwGb`; [sources](../sources.md).
- Interval: [06:14:03.640, 06:39:49.016).
- Inputs: `part-13.json` local [00:14:03.640, 00:30:00.000), then
  `part-14.json` local [00:00:00.000, 00:09:49.016), under
  `.data/day-02/transcripts/`; both TXT parts read in full.
- **ASR-based review draft**, nonverbatim; no audio/visual review. Demo observations
  below are the presenter's narration, not independent inspection of his screen.
- Speaker: probable Simon, to audience; questioners unresolved. Bot identities
  carry over from C18. Flylo is explicitly a demo account, not the game studio.

## Orientation

Simon narrates his prospecting system, then qualifies its cost and complexity.
The demo does not establish delivery of every draft or resulting customer sales.

## Edited conversation

### 06:14:03.640-06:15:26.200 | Reading the bot team's activity

**Speaker:** probable Simon. **Type:** demo narration.

Simon says color coding helps him distinguish research from outbound copy and
parallel work. An army huddle lets Web Search assign research to soldiers and
collect responses. He identifies Flylo as the demo account. Small presentation
adjustments are condensed; no prospect contact records are copied.

### 06:15:26.200-06:19:11.224 | Priorities and scheduled work

**Speaker:** probable Simon. **Type:** routine descriptions and examples.

His routine targets 50 new prospects daily, with five prioritized for immediate
action and 45 for later. Signals might include an unanswered sales inquiry or
relevant content interest. He describes calendar blocks around existing meetings,
not a fixed universal schedule. An inbox manager ranks Slack and email actions.

Daily account scans look for new signups, usage and content activity. He values
speed to lead and reports more receptive responses, without a measured effect.
A Salesforce account-stage trigger can stop outreach when a deal advances. This
unsequencing guard matters: automation should not keep cold-outbounding a contact
as though an active deal did not exist.

### 06:19:11.224-06:21:46.968 | Draft review and breaking out of templates

**Speaker:** probable Simon. **Type:** narrated output and writing critique.
**Claimed authors:** coordinator and writing bots; human remains reader/reviewer.

The demo sequencer uses CSVs for queues, prospects and daily actions. Simon calls
the UI unattractive and says it is mainly system memory, not something the user
should inspect constantly. He reports Gmail drafts that he can review one by
one, with an optional bot-generated confidence/quality score.

He stresses reviewing closely while teaching the bot one's voice. Even after
filtering examples, initial messages looked like the same template with swapped
names. He asked for examples and critiqued each until messages became more
specific. A bot's self-rating is not independent evidence of accuracy or response
likelihood; the segment does not verify that all drafts were sent.

### 06:21:46.968-06:25:50.936 | Separate parallel jobs, reconnect account evidence

**Speaker:** probable Simon. **Type:** architecture explanation and examples.

He groups outbound work by platform, with Shakespeare handling email, rather than
creating multiple bots for the same task without a reason. Separate bots make
sense when work genuinely runs in parallel or needs distinct context.

His PLG bot uses Salesforce context. A previously lost opportunity might become
relevant after a missing capability ships; the customer-context bot can explain
why it was lost and help reprioritize outreach. This is an example, not a named
customer win. Enrichment checks address validity; an Amplemarket-like tool is
named in ASR. Company research uses a tool rendered Sumble to infer technology
stacks, job postings and organizational roles. Spellings and exact integration
behavior need audio/product verification.

He connects public company information with meeting references to identify who
might care and whether they are an economic buyer. No contact details, scraped
profiles or private customer records are included in this derivative.

### 06:25:50.936-06:31:14.104 | Parallel research and an evolving ICP skill

**Speaker:** probable Simon. **Type:** scaling explanation and narrated demo.

Web Search delegates batches to low-context workers so research across hundreds
of accounts is not serial. He gives a 200-account example divided into groups of
40; it is an illustrative scale, not a measured run completed here. The search
provider name is unclear in ASR. Usage signals help rank prospects alongside
external research, and the configuration can be shared with teammates.

He demonstrates invoking a prospecting skill for Flylo, while most normal work
runs as routines. A separate ICP skill captures current findings about who values
the product. He explicitly says that profile is still evolving. Keeping it in a
reusable skill lets dependent workflows reference an updated version rather than
repeating stale assumptions.

He narrates CSV fields and colored bot messages as research begins, then ends
the demo. This establishes a reported invocation and activity, not audited
completion of every enrichment or outreach step.

### 06:31:14.104-06:33:57.080 | End-to-end ambition without bot proliferation

**Speaker:** probable Simon. **Type:** advice and acknowledged limitation.

He argues that initial setup and feedback can pay off when a whole workflow is
coherent. But he also warns that messaging many bots increases context switching.
Having created too many himself, he asks whether an existing email bot could
also manage the inbox, or whether a routine is enough. The criterion is useful
parallel work and reduced burden, not maximizing bot count.

### 06:33:57.080-06:35:55.160 | No fixed token-cost answer

**Speakers:** unresolved audience questioner; probable Simon responds.
**Type:** cost question and qualified answer.

Asked for daily/weekly token consumption or dollar cost for 50 prospects, Simon
does not provide a number. He says volume, meeting context, internal data and the
amount of fresh enrichment affect usage. He recommends inspecting one's own
instance and discussing optimizations. A weekly batch of 250 might fit some
workflows better than 50 daily; his daily setup prioritizes freshness and may
consume more. Neither schedule is established as cheaper by a measurement here.

### 06:35:55.160-06:37:43.224 | Why a soldier huddle?

**Speakers:** unresolved questioner; probable Simon. **Type:** architecture Q&A.

The questioner asks why use a group chat if the coordinator already connects
bots, and what soldiers do. Simon says soldiers do general web research, while
the group lets him inspect outputs returning to Web Search. He also finds it
easier to resize the worker group when Web Search handles delegation and each
worker needs little context. The claim is inspectability and scalability, not
proof that a group chat automatically validates research.

### 06:37:43.224-06:39:49.016 | Getting started and the stage transition

**Speakers:** unresolved questioner; probable Simon; another audience speaker.
**Type:** onboarding question, advice, naming aside and transition.

A questioner says it may be hard for a new user to decide what should run in
parallel and asks if the coordinator can help create an appropriate team. Simon
recommends explaining the overall workflow and working with the bot to divide
it into practical responsibilities, rather than requiring a perfect architecture
up front. No fully automatic onboarding result is demonstrated in the answer.

An audience member briefly jokes about a personal soldier naming convention;
it does not establish a new participant identity or organizational affiliation.
The remaining placeholders and transition are unverified coverage, not certified
silence, before the stream returns to the hosts.

## Editorial changes and unresolved evidence

- Kept demo Flylo distinct from real account histories and the host game studio.
- Retained unanswered numeric cost question, draft review, unsequencing guard,
  templated-output problem and warning against redundant bots.
- Incidental contact data and unnecessary personal naming aside minimized.
- No output self-score, color indicator or narration treated as independent proof.
