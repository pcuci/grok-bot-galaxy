# D2-C12: Polish, server authority and the next work split

## Source and review state

- Source: X `1PKqrNyvmYwGb`; [sources](../sources.md).
- Interval: [03:42:01.496, 04:00:00.000).
- Input: `.data/day-02/transcripts/part-08.json`, local
  [00:12:01.496, 00:30:00.000); TXT read in full.
- **ASR-based review draft**, nonverbatim; no listening or screen review.
- Probable Roshan drives initial polish (explicit screen request); Matt presents
  the lander; Lauren contributes engineering/design advice. Unnamed turns remain
  an unresolved host group; no diarization is inferred.

## Orientation

The hosts examine how to turn a local prototype into a shared game, debating
client-side debug controls, landing-page friction and exploitable rerolls.

## Edited conversation

### 03:42:01.496-03:45:03.480 | Client debug controls are not a security boundary

**Speakers:** probable Roshan and Lauren. **To:** each other/coding agents.
**Type:** narrated inspection, objection and repair requests.

Roshan runs the prototype locally and asks an agent to pin the header. He proposes
hiding the debug menu behind a flag. Another host objects that a runtime flag
still ships the code and a player could alter values in the console. They say
competitive battle/matchmaking logic needs server authority, though that work is
not completed now. This preserves the move from cosmetic hiding toward a real
trust-boundary concern.

He also works on minting a bot and removes unnecessary copy. A number floats
separately when its card rotates; he asks that it attach and rotate with the card.
These are observed-by-presenter defects and requests, not verified repairs here.

### 03:45:03.480-03:46:51.032 | Parallel polish and incomplete design assets

**Speaker:** probable Roshan; other hosts respond. **To:** audience/agents.
**Type:** workflow explanation and status.

Ability labels remain confusing beside raw stats. Roshan explains Cursor's
multitask mode: separate subagents can address several tagged design changes at
once. Another host notes that serial prompting had blocked her earlier work.
They ask to remove an unnecessary container and notice the logo still needs
attention. Generated assets are reportedly in progress, not ready.

### 03:46:51.032-03:50:09.656 | Does the game need a landing page?

**Speaker:** probable Matt, with unresolved host critique. **To:** cohosts/agent.
**Type:** narrated lander, disagreement and compromise.

Matt shows a shimmer-card lander and describes using a low-effort fast model for
rapid design edits; the exact model version is uncertain in ASR. He wants less
crowded type, real marketplace bots instead of fictional examples, and copy that
explains why to play rather than leaking prototype/implementation language.

A host asks whether a lander is needed at all if players can enter the game
directly. They consider a guide or interactive tutorial. Another likes having a
home page. They converge provisionally on keeping the appealing hero/card stack
and a large play button leading into X login, rather than a long marketing page
or an unexplained login wall. This is design direction, not a conversion test.

### 03:50:09.656-03:51:47.032 | Template promotion and checkpoint reports

**Speakers:** probable Lauren and unresolved hosts. **To:** audience/cohosts.
**Type:** template demonstration and progress report.

A host shows a Dr. Eggbot QR code and describes installing it to improve bot
prompts and run health checks. No link or QR is reconstructed from the ASR.
Another says alignment fixes are being checkpointed to main so everyone can
pull current changes. The team still lacks a satisfactory logo and begins
planning the remaining work. Git activity is their report, not this curator's
operation or independent inspection.

### 03:51:47.032-03:54:36.984 | Shared playability before more features

**Speakers:** unresolved host group, with Matt explicitly asked about his work.
**To:** each other. **Type:** proposed work split and playtest narration.

They want a coherent prototype in main so each person can build independent
features and reconcile changes. Authentication is offered as a task so the three
hosts can sign in and actually play one another. Matt is asked to work on assets,
ability icons and perhaps a small tutorial. Another host takes interest in the
round-to-round flow, which still requires repeated clicks.

During a local playthrough, they report the rating falling with losses and then
a win; a sample rating of 1258 is not a verified persistent account record. The
main concern remains feel and animation. They describe the current mechanics as
roughly rock-paper-scissors with numbers and defer additional systems.

### 03:54:36.984-03:57:18.264 | Business work and agent self-checks

**Speakers:** unresolved host group. **To:** each other/agents.
**Type:** ideas, task offers and narrated testing.

They remember the business around the game: discovery and possible stadium
advertising. A moderated ad marketplace or bids are ideas, with the stream as a
possible source of early interest. There is no advertiser, bid or payment yet.
A host offers to think about stadiums; another discusses game-server authority
and authentication to prevent cheating.

While cleaning navigation, Roshan describes an agent using the browser to walk
through its own output. He demonstrates queuing a tier-badge request for parallel
work instead of interrupting the current task. The captain flow still needs
fixes. These are narrated checks, not independently inspected test evidence.

### 03:57:18.264-04:00:00.000 | Reroll exploit, hidden bots and workshop handoff

**Speakers:** unresolved host group. **To:** each other/agents/audience.
**Type:** design objection, alternative and next-work announcement.

A host notices that unlimited visible rerolls would let players keep trying
until they have three legendary bots. One suggests removing rerolls. Another
suggests showing only the chosen captain and keeping the two random teammates
hidden. They then consider retaining a reroll control under that hidden-information
approach. The rule is unresolved; it must not be summarized as a final no-reroll
policy.

They announce continued off-stream work on design, lander, core flow,
authentication and playtesting, hoping to return after the sales workshop with
more progress. The remaining interval includes a brief transition/music fragment;
no off-stream completion is inferred.

## Editorial changes and unresolved evidence

- Retained feature-flag objection, lander disagreement and reversal on rerolls.
- Requests and plans remain distinct from implementation; no public launch,
  payment or secure server is certified.
- Screen actions and repeated filler condensed; exact model, logo and bot-name
  spellings remain review items.
