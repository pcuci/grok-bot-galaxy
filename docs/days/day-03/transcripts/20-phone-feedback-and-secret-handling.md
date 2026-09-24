# D3-C20: Phone feedback and secret handling

## Source and review state

- Interval: [05:09:48.792, 05:16:48.888).
- Source: X `1YGNrbXEeazGw`; [inputs/hashes](README.md), [sources](../sources.md).
- Nonverbatim **ASR-based review draft**. Phone audio cannot be independently identified from ASR.

## Input intervals and identity

Source/checkpoint hashes are in [the index](README.md). These are exact
normalized PCM intervals, not audio-verified word or speaker boundaries.

| Part and hashes | Part-local interval | Source interval |
| --- | --- | --- |
| [part-11](README.md#part-11) | 00:09:48.792-00:16:48.888 | 05:09:48.792-05:16:48.888 |

## Edited conversation

### 05:09:48.792-05:11:06.392 | Feedback-to-repair automation

**Speakers:** probable Lauren D3-H02 and hosts. **To:** audience. **Type/purpose:** workflow report.

Lauren describes UI polish and bug fixes, then revisits the feedback button Matt added. A host says a 20-character minimum was added after spam. Submitted feedback reportedly enters Slack, where bots try to reproduce a problem, confirm it, fix it and automatically merge. This is a later, more permissive workflow report than the early triage-only instruction in D3-C08. The transcript does not establish that every submission received independent verification.

### 05:11:06.392-05:12:06.872 | Phone feedback demonstration

**Speakers:** host caller D3-HU, probable Matt D3-H01 as builder/narrator, and a claimed voice-agent response D3-B-VOICE-FEEDBACK. **To:** phone agent/team/audience. **Type/purpose:** live-demo narration, human feedback and claimed generated acknowledgement.

The hosts call a number for an xAI voice agent. The caller praises the tool and asks for the feedback to reach the team. An apparent agent response says it was sent; the hosts then describe seeing it in their Slack channel almost immediately. The reader/narrator and generated response are separate sources. This is a transcript-reported demo, not an independently tested phone-to-Slack delivery. No phone number is reproduced.

### 05:12:06.872-05:13:31.192 | Builder explanation and apparent token exposure

**Speaker:** probable Matt, with other host interjections. **To:** audience/production. **Type/purpose:** implementation explanation and security response report.

Matt describes using a GUI voice-workflow builder rather than writing the voice agent's code, with a webhook passing feedback into Slack. He claims the same moderation guardrails apply as to the other feedback path; that claim is untested here.

He notices a token may have been shown, asks production to leave his screen, and later says only part of the value was visible and that he has deleted it for safety. The derivative contains no token value or private endpoint. This report is not proof that exposure was harmless or that revocation succeeded. Security consequences remain an audio-review and operational-evidence question.

### 05:13:31.192-05:16:48.888 | Appropriate uses and an unfinished repair

**Speakers:** hosts; probable Matt on voice tools. **To:** each other/audience. **Type/purpose:** capability discussion, reservations, hypothetical examples and PR feedback.

The hosts describe combining app and phone feedback into bot workflows. One says voice agents are useful but would not want one calling people on his behalf, and that encountering an agent while seeking urgent help can be frustrating. They suggest information collection and tool-assisted tasks, with escalation to a human where appropriate.

Account deletion, address updates and a restaurant call that escalates to staff are hypothetical examples, not implemented studio features. They distinguish these xAI/Grok voice tools from Grokbot-specific functionality.

Returning to the game, a host reports a draft PR for missing lineup abilities, but wants more card detail before accepting the look. It remains in review at this point, despite the earlier request and ongoing feedback automation.

## Editorial changes and unresolved evidence

Phone/contact details and any sensitive values are excluded; the security event itself is retained. Capability claims, moderation, token handling, delivery and attribution remain pending audio review. No successful secret rotation or universal automated repair is asserted.
