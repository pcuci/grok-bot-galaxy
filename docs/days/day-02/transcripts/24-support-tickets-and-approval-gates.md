# D2-C24: Support tickets, refund examples and knowledge approval

## Source and review state

- Source: X `1PKqrNyvmYwGb`; [sources](../sources.md).
- Interval: [07:43:06.776, 08:00:02.072).
- Inputs: `part-16.json` local [00:13:06.776, 00:30:00.000), then
  `part-17.json` local [00:00:00.000, 00:00:02.072), under
  `.data/day-02/transcripts/`; both TXT parts read in full.
- **ASR-based review draft**, nonverbatim; no audio or screen review.
- Speaker: probable David to audience and his demo bots. All ticket replies and
  status messages are human narration of claimed bot output, not bot speech.
- Ticket names are demonstration labels, not identified real customers.

## Orientation

David works through simple answers, a handoff, refund examples and a human-approved
knowledge update. The internal Slack reply takes retries and waiting.

## Edited conversation

### 07:43:06.776-07:45:15.928 | A password-reset answer grounded in public docs

**Speaker:** probable David; **to:** Reply and audience. **Type:** request and
narrated result. **Claimed author:** Reply.

David asks Reply to answer a basic password-reset ticket, labeled Alex. While
waiting he explains the prepared connectors and the simple process the bot must
follow. He then says the ticket has a reply and an internal note recording the
issue, confidence and source. He compares the answer with the public reset steps
and reports a match. This is narrated demo evidence, not an independent
verification of email delivery or of the underlying documentation.

### 07:45:15.928-07:47:27.960 | Missing SSO knowledge leads to escalation

**Speaker:** probable David; **to:** Reply/audience. **Type:** request, reported
handoff and bot-to-bot delegation. **Claimed workers:** Reply then Alert.

The next ticket concerns an SSO/Okta-like issue not covered in the prepared
knowledge base. David has instructed Reply not to answer without sufficient
support. It reportedly finds neither public nor internal documentation, records
low confidence and hands off instead of improvising a fix.

Reply also contacts Alert because an enterprise user may be locked out. David
reports an alert in Slack. The handoff is the intended result, not a failed
attempt to generate a plausible answer. He marks the example done to continue;
that is not proof the underlying customer issue was resolved.

### 07:47:27.960-07:51:14.552 | Two refund cases, with different results

**Speaker:** probable David; **to:** Reply and audience. **Type:** synthetic setup,
request and narrated external-system result. **Claimed author/actor:** Reply.

David sets up two demonstration subscribers under the 14-day policy. Carter is
newly subscribed and should receive cancellation/refund; Damon is outside the
window and should not. The spoken date is part of the demo narration and is not
used to establish the broadcast's date. He says approvals can be required or
more autonomy allowed, then asks the bot to handle both.

The step takes time; he supplies customer IDs to help lookup. No identifiers are
retained here. Later he reports that the replies are present, refreshes Stripe
and says Carter changed from active to canceled with payment refunded. For Damon,
the reply denies the refund without exposing the full internal SOP and offers
a future cancellation; David says the account remains unchanged on refresh.

These are narrated results in a demonstration environment. They do not establish
real-money settlement, a real customer's eligibility, or that a suggested future
cancellation was executed.

### 07:51:14.552-07:55:20.056 | Do not invent policy for a missing FAQ

**Speaker:** probable David; **to:** Reply, Tune and audience. **Type:** request,
reported knowledge gap, human policy instruction and retry.

A ticket labeled Elena/Selena asks whether a Wi-Fi pass may be shared. Reply finds
that the knowledge base does not answer this and recommends involving Tune rather
than inventing a rule. David explicitly supplies the demonstration policy: pass
sharing is not allowed, and the FAQ should say so.

He emphasizes that knowledge-base changes need a human's final say because a wrong
rule could affect many later answers. Tune reportedly adds a visibly distinguished
entry about simultaneous use. David skips an unspecified extra step; no omitted
demonstration is reconstructed.

The original ticket still has a handoff note and no answer. David asks Reply to
retry after the update. He then reports a new answer with a source link to the
added section. The important sequence is missing evidence, human-supplied policy,
knowledge update, retry and reported reply, not autonomous discovery of a true rule.

### 07:55:20.056-07:58:53.624 | Internal Slack answer needs permission and retries

**Speaker:** probable David; **to:** the internal-support bot/audience.
**Type:** internal-user roleplay, permission change, waiting and reported result.

David poses as a billing teammate asking for the internal refund SOP. Unlike the
customer-facing answer, this should use internal knowledge. He encounters a
permission request to post in Slack and chooses an always-allow option for the
demonstration. The reply does not arrive immediately; he retries and checks that
the process is running.

While waiting, he points to an earlier rehearsal result as an example of what
should happen. That earlier result must not be mistaken for the current request's
completion. Later he says the new request replied and added an emoji. Exact
latency, payload and access enforcement are not independently checked here.

### 07:58:53.624-08:00:02.072 | Start simple and scope write access

**Speaker:** probable David to audience. **Type:** advice and transition to Q&A.

David recommends read-only operation first, then drafts or manual approvals before
allowing writes. Different bots can have different permissions; one may post to
Slack automatically while another must ask. He notes the demo was more protective
than he wanted at the end, but prefers caution around writes.

He says there is no single settled playbook and recommends fitting bots to the
user's workflow, starting simple and experimenting with missing pieces. The
short end-of-part transition contains no additional recovered substantive speech.

## Editorial changes and unresolved evidence

- Kept demo ticket names as example labels only; removed access/customer IDs.
- Separated handoff from resolution, refund narration from real-money proof, and
  future cancellation offer from execution.
- Preserved waits, permission intervention, retry and use of a rehearsal example.
- Human instruction, not Tune, supplied the new FAQ policy. No direct quotations.
