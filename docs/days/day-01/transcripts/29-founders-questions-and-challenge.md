# D1-C29: Founders workshop: questions and challenge

## Source and review state

- Interval: [08:00:43.576, 08:18:43.640).
- Source: X `1AxRnZbVpjaxl`; [inputs/hashes](README.md), [sources](../sources.md), [entities](../entities.md).
- **ASR-based review draft**, nonverbatim grouped conversation; not audio-verified. No quotations.
- Context: Founders **workshop** on demo companies, separate from the hosts' live build.

## Input intervals and identity

Source/checkpoint hashes are in [the index](README.md). These are exact
silence-preserving PCM intervals, not audio-verified word or speaker boundaries.

| Part and hashes | Part-local interval | Source interval |
| --- | --- | --- |
| [part-17](README.md#part-17) | 00:00:43.576-00:18:43.640 | 08:00:43.576-08:18:43.640 |

## Edited conversation

### 08:00:43.576-08:04:36.984 | Setting bots up, multiple computers and determinism

**Speakers:** in-room questioners D1-HU; Shub D1-H11. **Type:** workshop Q&A.

Asked for a framework for the one-to-two-hour setup, Shub says inventory everything you do, group it into domains such as finance, customers or marketing, and let bots expand scope; some prefer a chief-of-staff bot, which he personally does not, depending on how much control one wants. Asked about bots across multiple computers, he says confusion from about a week earlier has been improved, a claim. Asked how to enforce deterministic enterprise policy, he says models are inherently nondeterministic; have a cloud agent write code encoding the decision tree and instruct the bot to call it every time, or ask other bots for permission.

### 08:04:36.984-08:09:53.048 | Importing setups, authentication friction and slow UIs

**Speakers:** questioners, partly inaudible; Shub. **Type:** Q&A.

Asked how to import setups from other tools, he says a bot to help is in progress; meanwhile make connections interoperable, for example through a password manager integration and imported browser cookies. He acknowledges unsolved authentication pieces and platforms that do not want bots. Asked about frustrating key setup, he advises asking the bot to figure it out without prescribing tools, citing why he chose a meeting-notes tool. Asked whether UI flows can match API speed, he suggests headless browsing and says models are improving computer use, but matching an API is harder.

### 08:09:53.048-08:13:37.400 | Many bots, token cost, forgetting and the marketplace

**Speakers:** questioners; Shub. **Type:** Q&A.

He says group chats make eager bots talk over each other and get expensive, so use them sparingly; cloud-agent models can be specified; and you can tell a bot to forget overused context. Asked how to evaluate marketplace bots, he says the official marketplace is currently hand-audited, with consent-based optimization and bot reviewers, and suggests asking a bot what it does before running it. These are presenter claims.

### 08:13:37.400-08:18:11.128 | Cross-account bots, local execution, memory and cloud agents

**Speakers:** questioners; Shub. **Type:** Q&A.

Bots talking across people or accounts is not available today, he says. For using local and bot computers together, he points to a local-execution setting, while favoring bot computers because local automation interrupts the user and consumes resources. Bots do not share memory but share a file system: one VM with per-bot instances. He describes first-class Cursor cloud-agent integration where Grok Bot passes relevant context and can QA results, recommending cloud agents for complex shipping tasks where model control matters.

### 08:18:11.128-08:18:43.640 | Wrap and challenge reminder

**Speaker:** Shub. **Type:** housekeeping.

He closes the Q&A and repeats the Starbase challenge; cheering follows. Surrounding production-audio fragments continue into the next chapter.

## Editorial changes and unresolved evidence

Many questions are inaudible; only restated questions are summarized. Silence labels in this interval are not treated as verified silence.
