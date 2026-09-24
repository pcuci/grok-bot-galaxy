# D1-C16: Engineering workshop: bot-fleet demo

## Source and review state

- Interval: [04:16:15.928, 04:40:12.632).
- Source: X `1AxRnZbVpjaxl`; [inputs/hashes](README.md), [sources](../sources.md), [entities](../entities.md).
- **ASR-based review draft**, nonverbatim grouped conversation; not audio-verified. No quotations.
- Context: Grok Bot 101 or engineering **workshop** demonstration, separate from the hosts' live build.

## Input intervals and identity

Source/checkpoint hashes are in [the index](README.md). These are exact
silence-preserving PCM intervals, not audio-verified word or speaker boundaries.

| Part and hashes | Part-local interval | Source interval |
| --- | --- | --- |
| [part-09](README.md#part-09) | 00:16:15.928-00:30:00.000 | 04:16:15.928-04:30:00.000 |
| [part-10](README.md#part-10) | 00:00:00.000-00:10:12.632 | 04:30:00.000-04:40:12.632 |

## Edited conversation

### 04:16:15.928-04:18:11.384 | Lingxi's bot fleet and why it is split

**Speaker:** Lingxi D1-H08. **Type:** workshop explanation. **Context:** workshop demo bots, not the hosts' bots.

He introduces his chief of staff, rendered Ling Shishi D1-B-LINGSHISHI-X, and engineers: Craig for UI D1-B-CRAIG-X (later ASR also renders Cry, Crank or Kreg), Steve for developer experience D1-B-STEVE-X, and Hogan for infrastructure D1-B-HOGAN-X. The same model could do any task; he separates them for context limits and role-specific pipelines, and mostly talks to the chief of staff, which routes work. **Lingxi's Steve is not Lauren's Steve.**

### 04:18:11.384-04:21:28.920 | Onboarding a marketplace nightly-audit bot

**Speaker:** Lingxi. **To:** his engineer bot; new bot. **Type:** live demonstration and dictated instruction.

He calls this a first-time live setup. He says he downloaded an engineer-bot template and now adds a nightly audit engineer from the marketplace, which begins onboarding. Instead of re-explaining workflows, he asks his existing engineer bot to onboard the new member, renamed Steve, on enforced engineering workflows. ASR here leaves ambiguous whether the new nightly bot D1-B-NIGHTLY-X takes the Steve name previously used for his developer-experience bot; the two IDs are not merged. He reads that Craig messaged Steve with Notion-board requirements, definitions of clean and workflow stages, and that they confirmed with each other. He triggers the audit now for demo purposes, saying it usually runs at 4 a.m., which differs from 3 a.m. in [C15](15-engineering-workshop-principles-and-use-cases.md).

### 04:21:28.920-04:25:38.744 | A Flylow bug and onboarding Jenny for the playbook

**Speaker:** Lingxi. **To:** Craig; chief of staff; new bot Jenny D1-B-JENNY-X. **Type:** dictated requests and advice.

He asks Craig to click through an urgent reported issue on the Flylow Air demo website D1-O-FLYLOW: users cannot check previously booked flights. He shows the bot navigating the site on its computer. He warns that urgent can make agents skip steps or guess, and that he does not want to repeat urgency instructions. He asks his chief of staff to onboard a new member named Jenny as head of operations, to own an engineering playbook in Notion and update other engineers. **This Jenny is a workshop bot, not the later human guest Jenny D1-H12.**

### 04:25:38.744-04:30:01.304 | Audit progress, confirmed bug and a P0 definition

**Speaker:** Lingxi. **To:** Craig. **Type:** narrated bot output and instruction.

He reports that Steve is researching improvements without further chat, has started cloud agents, and is condensing results into a PR. Craig reports the issue is real: the trips page is a stub while navigation links to it. Lingxi defines a P0 escalation workflow: a routine checks cloud agents every five minutes and interrupts or nudges them if they are off track, such as long sleep commands during tests, deviating from the goal, or being too conservative.

### 04:30:01.304-04:35:33.304 | Playbook propagation, proof requirements and a ready PR

**Speaker:** Lingxi. **To:** Craig; Jenny. **Type:** instructions and narrated bot-to-bot exchange.

He asks Craig to fix the issue urgently under P0. Craig is reported to know the P0 definition, so it need not be copied to every bot. He asks Craig to have Jenny add it to the playbook and announce it; he reads that Jenny announced to engineer bots and confirmed the update. He then adds a requirement that PRs include proof, such as screenshots for UI changes and evidence for performance changes. He reports Steve has a cleanup PR ready, another task still running, and a marketplace engineer bot using a Notion fleet database of tasks and stages to limit context.

### 04:35:33.304-04:39:25.360 | Review bots and closing lessons

**Speaker:** Lingxi. **Type:** demonstration and advice.

He mentions security-comment and bug-detection bots on a PR, opens a PR from a previously started cloud agent with screenshots, and says he merges with confidence after reviewing results and proof. Takeaways: treat bots like talented interns via messages; reduce repetition by extracting instructions into playbooks or supervising bots; and give agents a complete feedback loop, such as computer-use testing, to know success versus failure. He thanks viewers and sends them back to the hosts.

### 04:39:25.360-04:40:12.632 | Return transition

**Type:** low-information interval with a beep label and a fragment.

## Editorial changes and unresolved evidence

Bot-name spellings and the Steve rename require screen/audio review. Reported PRs, merges and fixes are workshop claims; no Flylow fix is independently verified.
