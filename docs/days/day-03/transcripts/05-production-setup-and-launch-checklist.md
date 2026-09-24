# D3-C05: Production setup and launch checklist

## Source and review state

- Interval: [01:21:04.184, 01:36:06.488).
- Source: X `1YGNrbXEeazGw`; [inputs/hashes](README.md), [sources](../sources.md).
- Nonverbatim **ASR-based review draft**. No audio, code, dashboards or production environment independently inspected.

## Input intervals and identity

Source/checkpoint hashes are in [the index](README.md). These are exact
normalized PCM intervals, not audio-verified word or speaker boundaries.

| Part and hashes | Part-local interval | Source interval |
| --- | --- | --- |
| [part-03](README.md#part-03) | 00:21:04.184-00:30:00.000 | 01:21:04.184-01:30:00.000 |
| [part-04](README.md#part-04) | 00:00:00.000-00:06:06.488 | 01:30:00.000-01:36:06.488 |

## Edited conversation

### 01:21:04.184-01:24:14.360 | Return to a still-pending launch

**Speakers:** probable Roshan D3-H03, with Matt D3-H01 and Lauren D3-H02 interjecting by context. **To:** audience/production. **Type:** build narration, expectations and privacy request.

The hosts return to the game-studio build. They ask production not to display screens while configuring client and web secrets. No secret is repeated in this derivative. Roshan describes a UI polish pass; another host immediately lowers expectations, saying there is still much to improve.

They want the app live so viewers can supply feedback, with marketing and monetization discussion later. A first playtest and iterative updates are the near-term aim, not a polished final release.

### 01:24:14.360-01:27:42.968 | Integration and deployment work

**Speaker:** probable Roshan. **To:** audience/cohosts. **Type:** reported workflow and infrastructure state. **Claimed workers:** unnamed repair/review bots and playtester.

He describes bots turning noticed bugs into cloud-agent PRs, with playtesting, other reviews and CI before approval. Matt is working on Clerk production authentication and X login. They mention domains, DNS, cross-origin configuration and callbacks as sources of friction. Vercel preview links supported earlier testing, but moving to production requires further configuration and hardening.

PlanetScale is named as the game database provider. Load tests are reported from overnight and further hardening is in progress. They have a domain but are withholding it until the product is live. The described checks do not establish security or capacity.

### 01:27:42.968-01:31:41.528 | Feedback-to-fix loop and debugging

**Speakers:** probable hosts. **To:** audience/one another. **Type:** workflow explanation, analogy and unresolved implementation.

They describe a Slack bug channel and compare it with internal triage systems that reproduce issues, inspect logs and identify the right person or repair. They want a similar loop for this app, returning PRs rather than only investigations. Concurrent UI and authentication rewrites make new failures plausible.

Another host compares debugging with checking a lamp's bulb, power and connections: identify steps between input and result, then isolate the failing link. Agents can help, but do not remove the need to understand the system. Production callbacks still need attention.

### 01:31:41.528-01:34:24.376 | Login reports and scattered context

**Speakers:** host group; dashboard speaker unresolved. **To:** cohosts/audience/production. **Type:** narrated testing and planning.

One host reports signing in and seeing one active user in Clerk; another says they are playing too. The number later becomes three, with possible dashboard lag. These are reports, not a reconciled user metric.

They open Notion to create a launch checklist. Existing bot-generated pages and task boards look messy. They describe canonical schema and game-mechanics documents as shared context, while code remains important engineering context. Finding the checklist itself is awkward; documentation existing does not mean it is well organized.

### 01:34:24.376-01:36:06.488 | Polish first or open the playtest?

**Speakers:** probable hosts, precise turn ownership unresolved. **To:** each other/chat. **Type:** deliberation and proposed validation step.

Authentication is tentatively checked off. They debate whether to wait for the UI rewrite or launch now with explicit expectations: this is a first playtest, poorly polished and likely to break. One has not clicked through recently. They agree to run through the game while hiding the URL, then share it if the result feels acceptable. The next chapter preserves that test rather than treating the checklist discussion as a completed launch.

## Editorial changes and unresolved evidence

Repeated screen directions and filler are condensed. Secrets are discussed only as a category; no values or private endpoints are copied. Provider-name normalization is contextual and pending audio review. Production claims, counts and workflow enforcement remain unverified.
