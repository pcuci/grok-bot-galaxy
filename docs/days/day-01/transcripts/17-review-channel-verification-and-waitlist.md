# D1-C17: Review channel, verification skill and waitlist

## Source and review state

- Interval: [04:40:12.632, 04:55:12.056).
- Source: X `1AxRnZbVpjaxl`; [inputs/hashes](README.md), [sources](../sources.md), [entities](../entities.md).
- **ASR-based review draft**, nonverbatim grouped conversation; not audio-verified. No quotations.
- Context: Hosts' live build (Ship by Thursday demo company); guest remarks within it are advice, not decisions.

## Input intervals and identity

Source/checkpoint hashes are in [the index](README.md). These are exact
silence-preserving PCM intervals, not audio-verified word or speaker boundaries.

| Part and hashes | Part-local interval | Source interval |
| --- | --- | --- |
| [part-10](README.md#part-10) | 00:10:12.632-00:25:12.056 | 04:40:12.632-04:55:12.056 |

## Edited conversation

### 04:40:12.632-04:41:45.176 | Lauren's goal: basic review and triage automation

**Speakers:** probable Matt D1-H01 prompting; Lauren D1-H02. **Type:** status narration.

A host asks Lauren what she has shipped. She says internal Slack has automations for reviewing PRs and triaging bug reports, and she wants a basic version so bots can post PRs to a channel, get them reviewed, then merge and perhaps auto-deploy. Her screen is not yet visible.

### 04:41:45.176-04:45:02.904 | Matt's recap, repositories and research bots

**Speaker:** Matt. **To:** audience. **Type:** recap and setup narration.

Matt restates the plan: an in-person San Francisco pop-up, collecting attendees and people who can make it happen, since they are not restaurateurs, then a platform built from that software, with making money by day three as a stretch goal. His screen shows GitHub connection and Cursor cloud-agent permissions for the Ship by Thursday organization. He repeats the demo-company titles. He lists repositories, a prioritizer bot D1-B-PRIORITIZER-M and his operator-research bot D1-B-OPRESEARCH-M, whose list includes well-known San Francisco restaurant groups. He credits Lauren's Dr. Eggbot for creating bots. A research list is not outreach.

### 04:45:02.904-04:48:28.920 | A PR-review channel, bug channel and verification skill

**Speaker:** Lauren. **To:** audience; Steve D1-B-STEVE-L. **Type:** demonstrated configuration and request.

Lauren shows a Slack PR-review channel where she and bots post PR links. A Cursor automation, currently just a prompt, reviews each posted PR using PStack for correctness, risk and missing tests; she is unsure she likes all of it. She is creating a bug-report channel with a similar automation and may pipe X feedback into it later, while noting the app barely exists. She says verification lets agents run the app, take traces and snapshots and debug without her as a bottleneck. She asked Steve to use PStack's create-verification-skill; Steve delegated to Tater D1-B-TATER-L. Slack appears frozen on screen.

### 04:48:28.920-04:52:26.072 | Lander polish, what a verification skill contains, and email provider

**Speakers:** Matt; Lauren. **Type:** narration and explanation.

Matt says he is polishing the lander design with a minimalism-oriented design skill, converting Lauren's prototype into something more professional, while Lauren works on back-end services and a waitlist. Lauren, awaiting a cloud agent, explains that a good verification skill includes a standard CLI/script so agents interact with the app reproducibly instead of writing token-heavy ad hoc scripts, and a feature map describing features, navigation and shortcuts. Matt considers Loops or Resend for waitlist email, chooses Resend for simplicity.

### 04:52:26.072-04:55:12.056 | Database connected, and a redesign request

**Speakers:** Lauren; Matt; overlapping cohosts. **To:** each other; Matt's founding-engineer bot D1-B-FOUNDENG-M. **Type:** reported outcome and dictated instruction.

They note a Resend plugin exists. After waiting for the domain, a host says the form is now connected to the database, so page visitors would create entries in PlanetScale; they look for entries. Lauren says the form should be redesigned because they may not be collecting useful information, and asks viewers not to submit yet. Matt dictates to his founding-engineer bot: make the UI much more minimalist, collect email sign-ups from guests into the database, and add a top-right button for restaurateurs or proprietors to request to help. He says he will personally work on outreach research. A few unintelligible fragments follow.

## Editorial changes and unresolved evidence

The database connection is a reported state; no rows were inspected. See D1-R08 for whether visitors submitted before the redesign warning.
