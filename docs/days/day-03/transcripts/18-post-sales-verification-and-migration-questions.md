# D3-C18: Post-sales verification and migration questions

## Source and review state

- Interval: [04:33:50.040, 04:53:20.376).
- Source: X `1YGNrbXEeazGw`; [inputs/hashes](README.md), [sources](../sources.md).
- Nonverbatim **ASR-based review draft**, not verified technical guidance.

## Input intervals and identity

Source/checkpoint hashes are in [the index](README.md). These are exact
normalized PCM intervals, not audio-verified word or speaker boundaries.

| Part and hashes | Part-local interval | Source interval |
| --- | --- | --- |
| [part-10](README.md#part-10) | 00:03:50.040-00:23:20.376 | 04:33:50.040-04:53:20.376 |

## Edited conversation

### 04:33:50.040-04:36:12.216 | Layers, retention and an unanswered failure question

**Speakers:** unresolved attendees D3-HU and probable Blake D3-H08. **To:** one another. **Type/purpose:** architecture and customer-success questions; personal reports.

An attendee asks about managers between Gus D3-B-GUS and the specialists. Blake says she has not needed that layer: Gus has reportedly handled about 15-20 bots, and she has not tested larger teams. She would consider another layer if limits appeared, rather than assuming a human organizational chart is necessary.

Another attendee asks whether retention or sales improved and whether anything went badly wrong. Blake describes catching small product updates, drafting timely messages and identifying account issues earlier. She feels this improves trust and tailored service, but supplies no retention measurement. The separate request for a serious failure example is not substantively answered before the next question; absence of an answer is not evidence of no failures.

### 04:36:12.216-04:37:09.880 | Cross-bot verification is not established

**Speakers:** attendee and probable Blake. **To:** one another. **Type/purpose:** verification question and explicitly uncertain explanation.

The attendee asks whether one bot verifies another's work. Blake frames this as Harbor D3-B-HARBOR checking Frankie D3-B-FRANKIE, then says she would be surprised if Harbor actually did that. She thinks verification happens within individual bots, with Gus bringing a wider view of the combined information. Her account does not establish independent cross-bot checking or the correctness of the workshop's outputs.

### 04:37:09.880-04:40:15.512 | Migration and management overhead

**Speakers:** attendee and probable Blake. **To:** one another/audience. **Type/purpose:** migration questions, experience report and tentative advice.

Asked about moving existing skills and MCP setups from other tools, Blake says she is not familiar enough with them to give a technical migration path. She would ask for the existing context to be exported and used to build a new system, possibly with a staff meeting to critique it. That suggestion is not a tested import procedure.

She acknowledges spending a lot of time onboarding and correcting bots initially. She says the resulting system is now quieter, with notifications reserved for specified events and useful routines. A travel anecdote about someone carrying a computer for another agent illustrates her preference for hosted VMs; it does not establish a requirement of competing products. Incidental personal detail is omitted.

### 04:40:15.512-04:43:46.904 | Bot sprawl and routing external agents

**Speakers:** attendees and probable Blake. **To:** one another. **Type/purpose:** dependency-risk and interoperability questions; untested suggestions.

An attendee worries that deleting underused bots leaves references in other bots. Blake recommends preventing sprawl early and suggests a possible technical-debt bot to inspect dependencies and consolidate unused work. She does not demonstrate reference cleanup or establish that deletion is safe.

Another proposes running several external coding agents inside the VM and using Grokbot to route among them, preserving invested skills. Blake explicitly says she has not seen this done and cannot say whether it succeeds. She suggests discussing consolidation with the bot, without claiming the proposed multi-agent router works.

### 04:43:46.904-04:46:51.096 | Context audits, long dictation and a cut-off answer

**Speakers:** attendees and probable Blake. **To:** one another. **Type/purpose:** audit/correctness questions and personal advice.

Asked how to audit forgotten instructions, Blake describes individual bot identities and change logs, then suggests asking the bot to analyze what it has done, changed or forgotten. No audit artifact is inspected here. Asked whether long dictation causes hallucination, she says she has not noticed much herself and sometimes requests distillation before deeper analysis. This is not a correctness benchmark.

Her most important personal example is a bot attending an internal meeting so she can spend time elsewhere. That recollection must remain distinct from the current workshop's sign-in failure and illustrative fallback in D3-C16. The next thought trails off around 04:46:37.592-04:46:41.648; the record does not supply a completed answer.

### 04:46:51.096-04:53:20.376 | Unresolved transition

**Speaker:** unresolved. **Type/purpose:** coverage marker.

The ASR contains labels for silence, pauses and blank audio separated by gaps. No substantive conversation is reconstructed. These labels do not certify that the recording was silent; the return starts mid-discussion. Audio review is needed to establish whether speech was lost.

## Editorial changes and unresolved evidence

All Q&A topics are retained, including nonanswers and admissions of uncertainty. Labels, filler and the incomplete final phrase are not expanded into invented content. Verification, migration, retention, memory and hallucination claims remain pending audio and, where needed, technical evidence.
