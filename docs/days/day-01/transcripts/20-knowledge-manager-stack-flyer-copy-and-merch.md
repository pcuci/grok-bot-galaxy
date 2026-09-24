# D1-C20: Knowledge manager, stack, flyer copy and merch

## Source and review state

- Interval: [05:17:29.784, 05:30:03.512).
- Source: X `1AxRnZbVpjaxl`; [inputs/hashes](README.md), [sources](../sources.md), [entities](../entities.md).
- **ASR-based review draft**, nonverbatim grouped conversation; not audio-verified. No quotations.
- Context: Hosts' live build (Ship by Thursday demo company); guest remarks within it are advice, not decisions.

## Input intervals and identity

Source/checkpoint hashes are in [the index](README.md). These are exact
silence-preserving PCM intervals, not audio-verified word or speaker boundaries.

| Part and hashes | Part-local interval | Source interval |
| --- | --- | --- |
| [part-11](README.md#part-11) | 00:17:29.784-00:30:00.000 | 05:17:29.784-05:30:00.000 |
| [part-12](README.md#part-12) | 00:00:00.000-00:00:03.512 | 05:30:00.000-05:30:03.512 |

## Edited conversation

### 05:17:29.784-05:19:04.984 | A passive knowledge-base manager

**Speaker:** probable Matt D1-H01 dictating; cohosts. **To:** Dr. Eggbot copy; new bot D1-B-KBM-M. **Type:** bot creation instruction.

A host asks Dr. Eggbot for a knowledge-base manager to groom Notion. Its job is to watch other bot conversations but **not act unless specifically called**, wait for messages, update Notion selectively rather than dumping everything, and check with him first. He says it will keep Notion current. Lauren says no design system exists; they suggest a component library such as a base UI kit and not worrying yet.

### 05:19:04.984-05:23:09.560 | Viewer recap, code-quality rules and how strict a stack

**Speakers:** Matt recapping; Roshan D1-H03; Lauren D1-H02. **Type:** recap and engineering discussion.

For new viewers, a host says bot teams are working on a design system, landing page and architecture, with one host on guerrilla marketing through a marketing bot and another on website design and business calls; Lauren is on engineering. Lauren is torn about adding lint rules to a prototype; a cohost argues refactoring later is easier than predicting needs and they may pivot. Lauren says a code base is a form of memory: architecture and stack constraints make agents smarter by default. She floats the strictest possible stack, perhaps Rust, then weighs TypeScript, which exists already and agents like, Go, and Rust compile times; no final stack decision is recorded.

### 05:23:09.560-05:26:29.944 | Flyer copy, novelty and exclusivity

**Speakers:** probable Roshan reading his bot's question; Matt; Lauren. **Type:** bot-output reading, advice and ideas.

A host says his marketing bot asks for a flyer headline and reads options such as one night, October 15, San Francisco pop-up and dinner finds you. Matt argues nobody cares yet and nobody cares that it is made with AI; the pitch should make people feel they are trying something new, proposing a headline asking when you last tried something new. A host reports an initial street-corner map in Slack. Lauren suggests a Grok Bot theme with a secret merch drop, stressing time-limited exclusivity. They propose each host bring something unique: merch for Lauren, social games or an on-site experience for another host. These are ideas, not approved copy.

### 05:26:29.944-05:30:03.512 | Flyer draft, video proof and email domain

**Speakers:** Roshan; Lauren; Matt. **Type:** status reports and instruction.

A host says an early flyer campaign is ready and a marketing Slack channel exists. Lauren says bots can produce videos and attach them to PR descriptions, but this PR lacks one; she asks to update the verification skill to use proof videos, including for back-end changes. Matt reports Resend domain verification is hooked up for checking DNS and shows early minimalist designs, proposing the repository as the design source of truth. He is still fixing GitHub CLI authentication.

## Editorial changes and unresolved evidence

The knowledge-base manager's passive configuration is preserved for comparison with the later polling request in [C21](21-venue-criteria-permits-and-art-pivot.md). Owner of this bot is probable Matt.
