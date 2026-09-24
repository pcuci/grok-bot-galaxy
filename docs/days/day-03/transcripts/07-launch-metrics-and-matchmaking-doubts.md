# D3-C07: Launch metrics and matchmaking doubts

## Source and review state

- Interval: [01:49:07.576, 02:08:46.424).
- Source: X `1YGNrbXEeazGw`; [inputs/hashes](README.md), [sources](../sources.md).
- **ASR-based review draft**. Counts are human reports of dashboards/bot outputs, not independently measured usage.

## Input intervals and identity

Source/checkpoint hashes are in [the index](README.md). These are exact
normalized PCM intervals, not audio-verified word or speaker boundaries.

| Part and hashes | Part-local interval | Source interval |
| --- | --- | --- |
| [part-04](README.md#part-04) | 00:19:07.576-00:30:00.000 | 01:49:07.576-02:00:00.000 |
| [part-05](README.md#part-05) | 00:00:00.000-00:08:46.424 | 02:00:00.000-02:08:46.424 |

## Edited conversation

### 01:49:07.576-01:53:11.832 | First reported audience activity

**Speakers:** probable hosts D3-H01/D3-H02/D3-H03. **To:** audience/each other. **Type:** narrated activity, requests and speculation.

Matt describes choosing an emoji profile image and improving favicons/social metadata. Another interrupts with a report of 96 leaderboard entries. Roshan asks a data bot for a recurring 15-minute launch pulse: signups, practice sessions and guest-to-account conversion. A dashboard request is not itself a running, accurate monitor.

They narrate their own ranks falling, another player overtaking them and about 225 X followers. Player handles are omitted; rank movement is retained without linking handles to real people. They are surprised the app has not crashed and discuss possible prizes, still not approved.

### 01:53:11.832-01:57:08.312 | Automated changes and network contracts

**Speaker:** probable Lauren D3-H02, based on first-person work and cohost address. **To:** audience. **Type:** retrospective implementation claims and engineering explanation.

Lauren says she used P-stack/potato mode for automatic PR merging and had not read the code before this inspection. She credits underlying infrastructure while acknowledging the early implementation was loose. Someone reports almost 500 users. The backend is described as Go in Vercel functions with PlanetScale; this is narration, not repository inspection.

She explains the risk of one person's backend change removing a field another person's UI expects. They use REST, and she describes parsing responses with Zod for validation. Given more time she might design the contract differently. Neither runtime validation nor reported tests establishes complete end-to-end type safety.

### 01:57:08.312-02:02:05.016 | What should the dashboard measure?

**Speakers:** probable Roshan and Lauren. **To:** each other/audience. **Type:** bot-output narration and product discussion. **Claimed author:** D3-B-DATA-R.

Roshan reports over 600 practice sessions, around 400 X sign-ins and a figure of 38 practice-to-sign-in conversions, while warning that the snapshot is already behind current activity. They discuss funnel stages, repeated play, retention and where users drop out. These counts have different denominators and are not added together or treated as verified analytics.

Asked what to prioritize, he says a zero-to-one, pre-revenue product needs to know whether users play, finish and return. Revenue matters eventually, but they explicitly have no monetization in the app at this point. Signed-in perks are possibilities. They also want metrics to diagnose replayability and game balance, acknowledging limited game-building experience.

### 02:02:05.016-02:06:51.224 | Contradictory balance signals

**Speakers:** probable hosts. **To:** each other and bots. **Type:** reported metrics, hypotheses and requests.

A host reads 41.8% as a loss ratio while calling results loss-heavy; later they say there are more losses than wins. This numerical/semantic tension is preserved, not corrected to a win rate. Another suspects AI matching because their own games repeatedly use AI. They explain a snapshot pool where an opponent lineup is removed after use, but the explanation is not verified against code.

They discuss aiming closer to an even win/loss experience and requesting analysis from the game-design bot. The integration list includes hosting, database, GitHub, Slack, Notion, authentication and design tools. Their claim that connected context helps interpretation does not prove the resulting interpretation correct; they say even one bot can be useful rather than requiring a large team.

### 02:06:51.224-02:08:46.424 | Investigate before opening a PR

**Speakers:** probable Roshan and cohosts. **To:** D3-B-CRIT-R, D3-B-ENG-R and audience. **Type:** data handoff, conflicting observations and dictated request.

Roshan reports asking the data bot to share launch information with Crit, his game-design bot. Hosts remain confused: leaderboard scores move, but their own matches use AI and one person's score does not change after a win. Speculation about whether AI games award rating is disputed.

Roshan asks his founding-engineer bot to investigate Elo and matchmaking using potato mode and a cloud agent. He explicitly requests findings first and no PR yet. Coffee-delivery chatter is condensed. No diagnosis or repair is inferred from the request.

## Editorial changes and unresolved evidence

Dashboard denominators, freshness, win/loss terminology and matchmaking behavior remain unresolved. No player identities, subscriber identity guesses or third-party metrics are verified. Substantive disagreements are retained; applause, rank-name repetition and incidental chatter are condensed.
