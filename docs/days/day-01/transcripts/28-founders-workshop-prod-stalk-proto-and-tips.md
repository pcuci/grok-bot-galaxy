# D1-C28: Founders workshop: Prod, competitor, Proto bots and tips

## Source and review state

- Interval: [07:41:46.936, 08:00:43.576).
- Source: X `1AxRnZbVpjaxl`; [inputs/hashes](README.md), [sources](../sources.md), [entities](../entities.md).
- **ASR-based review draft**, nonverbatim grouped conversation; not audio-verified. No quotations.
- Context: Founders **workshop** on demo companies, separate from the hosts' live build.

## Input intervals and identity

Source/checkpoint hashes are in [the index](README.md). These are exact
silence-preserving PCM intervals, not audio-verified word or speaker boundaries.

| Part and hashes | Part-local interval | Source interval |
| --- | --- | --- |
| [part-16](README.md#part-16) | 00:11:46.936-00:30:00.000 | 07:41:46.936-08:00:00.000 |
| [part-17](README.md#part-17) | 00:00:00.000-00:00:43.576 | 08:00:00.000-08:00:43.576 |

## Edited conversation

### 07:41:46.936-07:44:27.416 | Prod Bot: what shipped and what was unshipped

**Speaker:** Shub D1-H11. **To:** Prod Bot D1-B-PROD-S; audience. **Type:** demonstration.

He asks Prod Bot for a daily rundown of Flylow D1-O-FLYLOW, the same demo surface as the PM session. It reviews PRs and issues and walks through the product using its own login, mapping changes to experience. The output lists shipped items, unshipped items and decisions worth being intentional about, with screenshots and a video of the bot navigating the site. He recommends asking bots for videos to verify work and connecting bots to metrics to surface results proactively.

### 07:44:27.416-07:48:39.160 | The competitor-tracking bot

**Speaker:** Shub. **To:** D1-B-STALK-S. **Type:** demonstration and advice with a caution.

The bot finds competitors, signs up autonomously and reports what they ship, changelogs, posts, hiring and team priorities, compounding over time. He asks for a competitor pulse on two hypothetical competitors of the demo note-taking app, naming two real note-taking products. Routines run every few days and stay silent unless relevant. He shows a teardown with a video of onboarding using a throwaway email, notes one competitor is not hiring, and describes emailing churned customers to learn why they left, while jokingly acknowledging a corporate-espionage concern and urging responsible use. He promises to share this bot.

### 07:48:39.160-07:54:13.048 | Proto Bot, a voice-clone writer and a miscellaneous bot

**Speaker:** Shub. **Type:** demonstration and advice.

Proto Bot runs its own separate Grok Bot account on its computer, so it can prototype and QA with product context. He asks it to pull recent demo feedback; it reports a customer wants the template-share button to pop more and starts working. He describes piping all feedback channels into one bot that opens PRs, while founders still decide which feedback to ship. His writing bot D1-B-YAP-S learns from his email, Slack and messages to write like him; other bots consult it; sensitive emails can stay drafts and it learns from edits. A miscellaneous bot D1-B-MISC-S absorbs random questions, such as whether an album has dropped, without polluting other bots, and can pass lessons on. Proto Bot's cloud-agent work had not finished.

### 07:54:13.048-08:00:43.576 | Lessons and cost tips

**Speaker:** Shub. **Type:** advice.

Lessons: let bots run with as much access as you are comfortable with; invest in bots rather than discarding them; give good skills and intentional tasks; spend an hour or two deciding what to delegate. Cost tips: browser use is powerful but expensive, so have bots discover underlying APIs from network requests and call them directly; audit routines, avoid very frequent schedules such as every 15 minutes, and prefer webhooks or inbound signals. Other tips: make a voice bot, import browser cookies for sign-ins, group bots by expertise, write good skills, and keep a bot that optimizes other bots. He shows a QR code for the competitor bot and hands back to the hosts, while staying for in-room Q&A.

## Editorial changes and unresolved evidence

Claims about autonomy, access and costs are presenter advice. Access-maximizing advice is recorded, not endorsed; it bears on approval boundaries.
