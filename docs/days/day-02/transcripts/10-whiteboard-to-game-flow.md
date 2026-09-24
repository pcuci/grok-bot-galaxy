# D2-C10: Whiteboard to a simpler game flow

## Source and review state

- Source: X `1PKqrNyvmYwGb`; [sources](../sources.md).
- Interval: [03:10:47.384, 03:30:40.216).
- Inputs: `part-07.json` local [00:10:47.384, 00:30:00.000), then
  `part-08.json` local [00:00:00.000, 00:00:40.216), under
  `.data/day-02/transcripts/`; both TXT parts read in full.
- **ASR-based review draft**, nonverbatim; no audio or screen review.
- Probable Lauren drives the whiteboard/prototype; Matt and Roshan are present
  by mutual address but individual interjections remain unresolved.

## Orientation

The hosts replace dense debug screens with a visual game flow, while continuing
to debate how much numerical detail to show and what must happen before launch.

## Edited conversation

### 03:10:47.384-03:13:54.392 | Draw the desired flow by hand

**Speakers:** probable Lauren and unresolved hosts. **To:** each other/audience.
**Type:** narrated whiteboard and design explanation.

After reacting to Karen's printer, Lauren says she used the break to draw rough
screens in tldraw. She could have asked a bot but wanted to understand the flow
herself. The game name is a working title. A player chooses a captain, receives
two other bots and can inspect a collection associated with the account.
Tracking the original minter is suggested, but they note that the first uploader
need not be the template's creator.

She opens the whiteboard inside Cursor's browser so an agent can screenshot it.
The earlier trading-card design has attractive elements but is not the game she
wants: she wants larger, simpler and more playful screens. The screenshot is
claimed agent input, not something this curator inspected.

### 03:13:54.392-03:17:21.880 | Hide arithmetic during the battle?

**Speakers:** probable Lauren and unresolved hosts. **To:** each other/agent.
**Type:** design proposals and unresolved choices.

The proposed sequence is choose captain, drag to order, confirm, find a match,
then show one bot matchup at a time. A loading screen may be unnecessary if
matchmaking is fast. Named example opponents and abilities in the sketch are
mock data, not confirmed participants or matches.

Lauren wants to avoid a screen full of percentages. They discuss relative power
arrows or bands, possibly revealing an opponent's strength only when an ability
fires to create suspense. Stat-band examples and a 150 total are tentative and
incomplete, not a stable balancing rule. They want win/loss animations and admit
the battle presentation needs more design work.

### 03:17:21.880-03:21:07.544 | Test a mockup and correct the layout

**Speakers:** probable Lauren and unresolved hosts. **To:** agent/cohosts.
**Type:** narrated prototype, critique and repair requests.

They try a refreshed version and explicitly question whether the login is real;
it is described as a mock. A diamond-style tier is preferred to a raw rating,
but a post-match summary could expose numbers to explain a loss and be shared.
The current screen does not match Lauren's sketch.

She requests three main cards, with the first a captain selector, and drags or
tries to reorder a sample team. A card described as Lingxi's engineering bot is
an in-game label, not proof its owner or bot is operating live. She asks for
drag-and-drop and removal of an extra order button. Someone says changes have
been pushed so cohosts can start working; this is a report, not a Git inspection.

### 03:21:07.544-03:24:31.416 | Pacing, replay and rating feedback

**Speakers:** probable Lauren and unresolved hosts. **To:** each other/agent.
**Type:** playtest and requested changes.

A mock match advances too quickly. They want animation, less stat text, and
rounds that advance automatically instead of requiring repeated clicks. They
also discuss automatically seeking another match after a short pause.

Rating feedback proves less simple than hiding every number. A tier plus an
unexplained delta may confuse people. They propose medals such as bronze/silver/
diamond, with the underlying rating accessible on hover. Thresholds mentioned
are examples. No implemented public ranking system is verified here.

### 03:24:31.416-03:28:49.272 | Parallel animation research and a simple leaderboard

**Speakers:** unresolved hosts, with Lauren advising. **To:** coding agents and
one another. **Type:** work coordination and engineering options.

Some requested changes are not yet implemented after refresh. They discuss
committing/pushing quickly and joke about having no time for PRs. This describes
their live workflow, not authority for this curator to write Git state.

A host asks an agent to research animation frameworks rather than invent every
effect. Lauren suggests a few small programmatic JavaScript prototypes and notes
that the product's own bot avatars involved careful design. They prefer starting
with 2D to get something playable sooner; 3D can be a later visual layer.

They want viewers to play as soon as possible and notice that a leaderboard is
missing. For a first version, rank by the rating and leave richer medals/tiers
for later. This is proposed scope, not completed launch evidence.

### 03:28:49.272-03:30:40.216 | Collaboration and debug-only advantage

**Speakers:** probable Lauren and unresolved hosts. **To:** each other/audience.
**Type:** status check, workflow revision and narrated debug adjustment.

Asked whether the newest changes are pushed, the operator says work is still
ongoing. With three contributors, they consider switching to PRs, qualifying the
earlier speed-first comment. Screenshots and a rating tooltip reportedly appear
as the agent continues.

They choose Dr. Eggbot again, joke about its weak stats, and use the debug controls
to alter an ability/stat rather than claim a legitimate competitive advantage.
They explicitly note that debug controls must not be exposed when deployed.
The conversation crosses the raw-part boundary without a new scene.

## Editorial changes and unresolved evidence

- Mock login/opponents, debug edits, unimplemented requests and the PR-workflow
  revision are retained. Bot-card names are not human attribution.
- Numerical bands/tiers remain examples. No tested matchmaking or public launch
  is inferred from prototype narration.
- Unclear names, brief waiting/navigation and repeated reactions are condensed
  or flagged, not silently repaired into exact mechanics.
