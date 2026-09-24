# D2-C20: Backend separation and a shared studio task board

## Source and review state

- Source: X `1PKqrNyvmYwGb`; [sources](../sources.md).
- Interval: [06:39:49.016, 07:00:08.184).
- Inputs: `part-14.json` local [00:09:49.016, 00:30:00.000), then
  `part-15.json` local [00:00:00.000, 00:00:08.184), under
  `.data/day-02/transcripts/`; both TXT parts read in full.
- **ASR-based review draft**, nonverbatim; no audio or screen verification.
- Speakers: probable hosts Roshan, Lauren and Matt, from explicit address and
  contextual roles; individual mixed turns unresolved. They address one another,
  viewers and their own bot instances. See [entities](../entities.md).

## Orientation

The hosts reconnect the client/server work and create coordination bots. Board
updates and PR notifications do not establish a playable, deployed game.

## Edited conversation

### 06:39:49.016-06:41:30.072 | Promotion and studio reset

**Speakers:** probable hosts to viewers. **Type:** announcement and work recap.

A host repeats a limited first-1,000-user offer involving installing Dr. Eggbot
and creating a bot, describing a month of usage as $200 in value. These are
historical promotional claims, not verified terms or current availability.

The hosts return to their game-studio build and explain that some of them worked
off-screen during the workshop. No progress is inferred solely from elapsed time.

### 06:41:30.072-06:43:38.264 | Separate client and authoritative server

**Speakers:** probable Roshan and Lauren. **Type:** implementation report and plan.

Roshan reports converting the prototype to a Next.js/React app with server-side
placeholders, separating client and server apps so they can evolve independently.
Lauren argues competitive results should be decided on the server, since a player
can modify client code. Authentication is still part of the work.

They consider alternative clients, including 3D, pixel art and a joking terminal
version, but not multiple launch clients as a requirement. The current leaderboard
contains placeholder names and is not fully wired up. A hoped-for launch in a
few hours is a target, not a completed deployment. Roshan asks his coordinator to
bring the team's Notion tasks together.

### 06:43:38.264-06:47:20.728 | Research, PR notifications and launch priorities

**Speakers:** probable Lauren and Roshan, Matt joins ad discussion.
**Type:** work reports, scoping and requests.

Lauren says a new game-research bot studied mechanics and wrote a standalone
Notion document. It is not yet connected into a shared process. Roshan describes
his founding engineer, Bake, watching GitHub PR changes while he and Lauren work
on client and backend respectively. Notifications help coordination but are not
independent proof of each merge.

They identify backend shipping/deployment and the web client as core work. A 3D
experiment should be nonblocking and discardable if unhelpful. For advertising,
they distinguish making promotional assets from selling in-game placements:
what space is sold, whether slots or a marketplace make sense, and pricing are
still questions. These items are being captured into a plan, not settled revenue.

### 06:47:20.728-06:51:14.584 | One dictated prompt, separate Slack bots

**Speakers:** probable hosts; one dictates to their Dr. Eggbot instances.
**Type:** human-to-bot request and reported setup.

They ask to share the Notion document and propose bots that monitor Slack
mentions. As an experiment, all turn on voice input for the same spoken request:
create a bot to process mentions, including task-completion notices related to
the game board. They report successful input on more than one account.

The shared prompt does not create one shared bot identity. Two hosts are amused
that their separate instances chose the same name, rendered Hing here and Ping
later. At least one still needs Slack installation/connection. They move away
from the screen to avoid exposing secrets; no credentials are retained here.

The generated plan contains task pages and a minute-by-minute schedule, which
the hosts do not validate as achievable. They discuss checklists versus database
views and a personal pattern of triggering work when a board item moves to in
progress. That pattern is not permission for this curator to enable automation.

### 06:51:14.584-06:54:16.408 | Ad research and motion-asset variants

**Speaker:** probable Matt; hosts respond. **Type:** requests and demo narration.

Matt sends research on how games sell ads and asks for a client/server approach.
Pixel-art explorations are also underway. He revisits Remotion outputs in square,
portrait and landscape shapes, correcting an aspect-ratio description as he goes.

He explicitly says the previews need crop/fidelity work and do not explain the
game well yet. Final mechanics and assets could replace current components.
Rendering a local video is possible, not proof of campaign publication. The
hosts discuss phone frames and Figma assets as a possible next experiment; a
workspace would first need setup.

### 06:54:16.408-06:57:11.608 | Personal automation examples and event triggers

**Speaker:** probable Matt, other hosts add ideas. **Type:** secondhand examples
and proposals, not new demonstrations of the cited users' results.

Matt returns to Karen's printed morning digest and imagines a dated journal
sheet or receipt-printer feed. He mentions a user named Lenny with an uncertain
surname reportedly paying a parking citation through a payment integration,
another marketplace-selling example and printed arithmetic worksheets. These
reports are not independent payment, sale or educational-outcome evidence.
Incidental family and account details are omitted.

They distinguish daily schedules from event-triggered routines, such as Slack
messages or monitoring alerts. Automatic incident investigation is an imagined
extension, not a verified response system demonstrated here.

### 06:57:11.608-07:00:08.184 | Board propagation and still-unfinished wiring

**Speakers:** probable Roshan and Lauren; other host joins prototype discussion.
**Type:** narrated message send, coordination requests and status qualification.

Roshan says he changed the Notion board to a Kanban view and previews a Slack
message before sending it to the other hosts. He hopes their bots receive the
canonical board link. Lauren wants a dedicated PM bot to update Notion, separate
from a mention-handling Slack bot. They see tasks and PR notifications changing.

Asked whether the application is ready, Lauren says it is not finished and
mentions rebasing, backend and authentication work. The hosts decide an optional
3D prototype can proceed without waiting for full server integration. They wonder
whether 3D should be limited to battles and how existing bot shapes would transfer.
The final cross-part fragment is unclear and not repaired into a design choice.

## Editorial changes and unresolved evidence

- Kept separate Ping instances despite identical names; no assumed shared account.
- Preserved placeholder leaderboard, unfinished backend and nonblocking client
  experiments. Board movement is not a validated deployment result.
- Promotional terms and third-party personal-use reports require separate review.
- No secrets, guessed contact details or screen-only content reconstructed.
