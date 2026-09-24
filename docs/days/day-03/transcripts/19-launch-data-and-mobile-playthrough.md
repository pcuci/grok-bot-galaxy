# D3-C19: Launch data and mobile playthrough

## Source and review state

- Interval: [04:53:20.376, 05:09:48.792).
- Source: X `1YGNrbXEeazGw`; [inputs/hashes](README.md), [sources](../sources.md).
- Nonverbatim **ASR-based review draft**. All screens and actions are transcript-reported, not visually or externally verified.

## Input intervals and identity

Source/checkpoint hashes are in [the index](README.md). These are exact
normalized PCM intervals, not audio-verified word or speaker boundaries.

| Part and hashes | Part-local interval | Source interval |
| --- | --- | --- |
| [part-10](README.md#part-10) | 00:23:20.376-00:30:00.000 | 04:53:20.376-05:00:00.000 |
| [part-11](README.md#part-11) | 00:00:00.000-00:09:48.792 | 05:00:00.000-05:09:48.792 |

## Edited conversation

### 04:53:20.376-04:58:15.320 | Reported usage and uncertain funnel definitions

**Speakers:** host group D3-H01/D3-H02/D3-H03, individual turns probable or unresolved from continuing context. **To:** each other/audience. **Type/purpose:** data-bot output paraphrase and interpretation; claimed author D3-B-DATA-R.

The hosts read a bot summary of over 1,000 users, 3,500 practice sessions and a 47% win rate, tentatively interpreting the last figure as better tuning. Asked where players drop out, they say there is not yet a compelling reason to sign in beyond the leaderboard. They also question whether the chart's sign-in event really measures conversion. An open practice session is not necessarily a lost customer.

They discuss a launch spike, an ambiguous 1908 figure and roughly 400-500 games per hour during a still-incomplete hour. They joke that cumulative charts and a small vertical axis flatter growth. Those caveats prevent treating the chart as a validated funnel or sustained growth result.

The conversation turns to whether the reusable game-studio workflow is itself the more valuable product: game design, prototypes, art and preview-deployment playtests might help build another game or a toolkit. These are future possibilities, not delivered products. They describe the current release as a first playtest and want continued iteration.

### 04:58:15.320-05:01:38.456 | Card visuals, responsive layout and leaderboard

**Speakers:** host group; Lauren D3-H02 probable for card work, others unresolved where inseparable. **To:** each other/audience. **Type/purpose:** UI change reports and mobile inspection narration.

A host reports adding an activity ticker and signed-in profile image. Card rarity is explained, and earlier glow effects are said to have been lost and scheduled to return. They switch to browser device emulation to inspect mobile layout. The result looks better to them, but button grouping and placement still need work; their improved-mobile claim is conditional on more feedback.

They mention over 1,000 X signups and the first diamond-ranked player. Player handles are omitted. Possible prizes are deferred; no award is established. The feedback form remains part of the narrated interface.

### 05:01:38.456-05:04:43.256 | Explain the game; discover missing ability text

**Speaker:** probable Roshan D3-H03 with host interjections. **To:** audience, then engineering bot D3-B-ENG-R. **Type/purpose:** playthrough narration and dictated repair request.

He explains the auto-battler: draft an ordered three-bot lineup, use attack/health and abilities, resolve combat, and win two rounds of three. Gold buys cards between rounds; he suggests revisiting whether ten gold is balanced. A freeze control preserves a shop card for a later turn.

While swapping the lineup, he cannot see the cards' abilities. The hosts first wonder whether this is mobile-specific, then consider a broader interface bug. He dictates a request to open a PR restoring ability visibility in the shop. The instruction is not proof of a fix.

### 05:04:43.256-05:07:15.544 | A win and new feature requests

**Speaker:** probable Roshan and host group. **To:** audience/engineering bot. **Type/purpose:** match narration, design suggestions and requests; claimed workers unnamed cloud agents.

The player reports winning the round and match. The hosts like the animations and suggest stronger effects, sound and background music, including prior prototypes reportedly stored in Notion. No audio pass is completed here.

Recalling Vincent's earlier growth ideas, Roshan requests a win-sharing button and an OG image, perhaps featuring the winning team or a generic card. He then asks for the sponsor form to move behind a button like feedback and for the form to be checked. They describe separate ability-fix and sharing agents working, not completed features.

### 05:07:15.544-05:09:48.792 | Reproduce the ticker obstruction before coding

**Speakers:** host group. **To:** each other and engineering bot. **Type/purpose:** bug discussion, delegation advice and repair instruction.

The ticker covers shop buttons. They discuss attaching a screenshot versus asking the agent to inspect the game in its own browser and responsive mode. One host recommends noticing when the human is doing work the bot could take on, perhaps with a recurring Dr. Egg D3-B-EGG-L suggestion.

The actual dictated instruction specifies inspecting and reproducing the obstruction before writing code, then fixing it with a cloud agent. They explain why browser use and screenshots can check behavior rather than only code. This is a requested verification method and capability claim, not evidence that every future change is verified.

## Editorial changes and unresolved evidence

Card-by-card arithmetic, filler and player handles are compressed or omitted; game rules, uncertainties, requests and defects are retained. Numbers, conversion definitions, bot ownership and all narrated UI results require audio review; external usage and deployment would need separate evidence.
