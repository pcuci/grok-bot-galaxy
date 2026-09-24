# D2-C04: Workshop results, limits and guardrails

## Source and review state

- Source: X `1PKqrNyvmYwGb`; [sources](../sources.md).
- Interval: [01:07:27.064, 01:23:56.184).
- Input: `.data/day-02/transcripts/part-03.json`, local
  [00:07:27.064, 00:23:56.184); TXT read in full.
- **ASR-based review draft**; nonverbatim edited conversation, no audio reviewed.
- Speaker: probable Amrita; audience/remote question readers unresolved.
  Bot names denote claimed generated authors, never a verified audible voice.

## Orientation

The workshop returns to the slide task, examines newly created bot roles, and
answers questions that qualify its earlier broad automation claims.

## Edited conversation

### 01:07:27.064-01:09:03.864 | Salesforce result and a login concern

**Speaker:** probable Amrita. **To:** audience. **Type:** narrated status,
paraphrased bot output and presenter assessment. **Claimed author:** Mimi.

She recalls an earlier outage and reads Mimi's status that the Salesforce pair
is being built and screenshots will follow. She initially thinks the bot has
trouble logging in and offers to take control. She then says the two slides look
right, although the logo is small, and describes a problem/solution/impact layout
from the supplied post.

She estimates the work took ten to fifteen minutes and suggests using the slide
with similar prospects. This is a narrated result and quality judgment, not
independent visual verification, a timed benchmark or confirmation of the
underlying customer metric. She then finds a Grab blog post for another example.

### 01:09:03.864-01:12:22.808 | Repeat the template, not the manual work

**Speaker:** probable Amrita. **To:** Mimi, then audience. **Type:** request,
workflow explanation and experience claims.

She asks Mimi to create a Grab case study. She explains that multiple posts
could be sent together, then irrelevant slides hidden for a specific customer.
Uber versus Grab is an example of relevance, not an actual call occurring now.
The desired layout remains logo, problem, solution, impact and a sourced quote;
no quotation is reproduced in this derivative.

She prefers explicit slide templates to generic, wordy AI design. She says Mimi
can find key points, arrange the slide and retrieve the logo. When Mimi reports
checking Salesforce before proceeding, she explicitly approves that result and
asks it to start Grab. She hopes to see Grab after Q&A; that hope is not a result.

She describes sometimes preparing for 15-20 customers in a week and having the
bot discover independently published customer posts. A recurring discovery-and-
slide task is suggested. These are usage reports, not measured productivity data.

### 01:12:22.808-01:15:43.928 | Examine the new team critically

**Speaker:** probable Amrita. **To:** audience. **Type:** narration and paraphrase
of generated bot descriptions. **Claimed creator:** Sherlock.

She says three bots were created in response to the earlier request. Battle
Card Blair would combine Serena's hands-on comparisons with Sherlock's Flylo
code knowledge to produce sales-engineering battle cards. She imagines combining
that with Mimi's slide work; that cross-account arrangement is a possible use,
not established execution.

Demo Drake is described as a demo-script and talk-track specialist grounding
claims in Sherlock's knowledge, using Serena or Blair for competitor contrast.
AI Radar monitors public engineering posts and the newly taught AI-blog skill,
handing testing to Serena and treating Sherlock as the internal technical source.

She questions whether AI Radar duplicates Serena and whether she wants to keep
it. That hesitation matters: creation is not proof that the team structure is
optimal. She says bots can sometimes push back instead of agreeing with every
request, then closes the presentation and invites questions.

### 01:15:43.928-01:17:35.512 | Anti-bot detection and site restrictions

**Speakers:** unresolved audience questioner; probable Amrita answering.
**To:** each other/audience. **Type:** question and qualified advice.

A questioner asks whether automated desktop use can get an account blocked,
using Facebook as an example. Amrita refers to a CAPTCHA encountered earlier
and says some websites detect bots strongly enough that she cannot get through.
She does not provide a general workaround or promise access.

For enterprise use she recommends administrators block sites that are not
appropriate for work. This is advice about restrictions, not a test showing
that bans or harmful activity are impossible.

### 01:17:35.512-01:19:24.600 | Will computer use replace MCP?

**Speakers:** unresolved questioner and probable Amrita. **Type:** question,
comparison and prediction.

The question asks whether developers should keep building MCP integrations if
bots can use computers. Amrita expects computer use to become important but does
not think MCP disappears. She describes MCP as an agent-facing API and says it
can currently be faster for actions such as creating a Google Doc.

She speculates that improved models may make computer use faster. For now she
finds MCP easier to monitor and constrain through allow/deny choices, and expects
computer-use guardrails to improve. Prediction is not current capability.

### 01:19:24.600-01:21:19.352 | Production access requires controls

**Speakers:** unresolved remote-question reader; probable Amrita answering.
**Type:** security question, limitation and narrated settings advice.

After inviting attendees to share use cases, a remote question asks how a bot
with internal-system access can be prevented from changing production. The ASR
contains a repeated/ambiguous version of the question; it is not treated as an
assertion that a production change occurred.

Amrita says enterprise guardrails are the current answer and are still being
hardened. She mentions rules/skills for avoiding unauthorized deployment, then
opens an auto-review setting. She advises configuring production deployment and
internal-system use to ask first rather than allow automatically. This records a
presenter's suggested control, not proof that a natural-language rule is an
enforced boundary or that the demonstrated account was safely configured.

### 01:21:19.352-01:22:15.480 | No Linux support, no integration?

**Speakers:** unresolved question reader and probable Amrita. **Type:** question
and acknowledged limitation.

The question asks about a tool with no MCP server that cannot run on Linux.
Amrita says there is no way in the current setup: the bots' VMs are Linux, so a
non-Linux tool without an integration cannot simply run there. She would need
the particular tool to investigate further. This qualifies the earlier claim
that a missing MCP need not block use; it is not a universal browser solution.

### 01:22:15.480-01:23:56.184 | Token usage and an approximate cost example

**Speakers:** unresolved questioner; probable Amrita. **Type:** billing question,
experience estimate and advice.

Asked about token usage, she says conversation and computer work consume tokens.
She attributes improving cost/performance to model development. The ASR renders
a model name as Rock 4-6; its exact name/version is unresolved and is not repaired
from external knowledge.

She estimates a whole slide deck cost roughly $20-30 compared with four or five
hours of manual work. These are personal approximations with unclear scope, not
published pricing or a benchmark. She says shorter bot replies may reduce usage.
The follow-up asking whether compute/spend itself can be adjusted continues into
the next chapter's transition and receives a narrower answer there.

## Editorial changes and unresolved evidence

- Salesforce slides are a presenter-reported result; Grab completion is not
  established in this interval. Screenshots were not available to this reviewer.
- Generated helpers remain bot instances, not humans or guaranteed specialists.
- Security controls, token cost and model identity require consequential review.
- Microphone checks and filler are condensed; questions and limiting answers are
  retained. The workshop-to-host cut is not treated as a clean speaker boundary.
