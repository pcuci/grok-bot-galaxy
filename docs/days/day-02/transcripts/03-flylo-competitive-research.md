# D2-C03: Flylo competitor research and bot collaboration

## Source and review state

- Source: X `1PKqrNyvmYwGb`; [sources](../sources.md).
- Interval: [00:45:07.696, 01:07:27.064).
- Inputs under `.data/day-02/transcripts/`: `part-02.json`, local
  [00:15:07.696, 00:30:00.000), and `part-03.json`, local
  [00:00:00.000, 00:07:27.064). Both TXT parts read in full.
- **ASR-based review draft**, nonverbatim edited conversation; no audio review.
- Speaker throughout: probable Amrita, continuous workshop context. The named
  bots below are claimed text authors/addressees, not audible speakers.

## Orientation

Flylo is explicitly introduced as a flight-booking demo company. Its supposed
code behavior, competitors and engineering proposals must not be attributed to
the hosts' game studio or adopted as independently verified technical facts.

## Edited conversation

### 00:45:07.696-00:48:00.088 | Establish the demo company and expert

**Speaker:** probable Amrita. **To:** audience. **Type:** setup explanation and
reading/paraphrase of bot output. **Claimed author:** Sherlock in this demo account.

She switches accounts to two workshop bots and introduces Flylo, a simple
flight-booking app with front-end, back-end, web and crew-facing components.
Sherlock's description gives it access to booking repositories and asks it to
investigate customer issues and explain them clearly. ASR alternates Flylo,
Flylow, Vilo and other spellings; Flylo is a navigation label, not a verified brand.

She recalls asking about two people booking the same last seat. Sherlock
reportedly inspected the code using cloud agents and identified Postgres-level
protection. It distinguished last remaining cabin capacity from an individually
assigned seat. She paraphrases a customer explanation involving a ten-minute
checkout hold and a conflict if another customer starts first. Neither that code
nor its concurrency behavior is inspected in this pass.

She suggests turning the explanation into a draft email or explicitly approving
sending it. This is a possible next action, not evidence that an email was sent.

### 00:48:00.088-00:50:58.072 | Give Serena a comparative task

**Speaker:** probable Amrita. **To:** audience, then Serena. **Type:** explanation,
human request and narration of reported bot-to-bot contact.

Serena's job is to use competing booking products and compare them with Flylo.
The presenter lists Expedia, Skyscanner and Google Flights as possible examples.
She also wants technical blogs and release notes considered, and describes a
possible weekly competitor-news routine. An AI travel agent is offered as a
feature to investigate, not an existing Flylo capability.

She asks which products are worth testing. She says Serena immediately contacts
Sherlock for a baseline: current booking flow, fare selection, seat selection and
known gaps. The presenter reads this exchange from the interface; there is no
independent observation of the bots' tool calls here.

### 00:50:58.072-00:54:42.968 | Narrow competitors, then add AI research

**Speaker:** probable Amrita. **To:** Serena/audience. **Type:** instructions,
narration and capability claims. **Claimed authors:** Serena and Sherlock.

She selects Southwest and Spirit for comparison. Sherlock reportedly begins
checking what the code supports. While Serena works, she adds a question about
AI travel-agent capabilities in competitor products.

The presenter describes Serena selecting dates and working through Southwest's
booking flow. She says this can be repeated across other competitors or targeted
to specific features. She emphasizes that the added AI question should augment,
not discard, the original booking-flow task. She reports an initial AI-feature
response while booking testing continues. Successful browsing and multitasking
are presenter reports, not separately verified results.

### 00:54:42.968-00:57:24.024 | Code agents and a group-chat retry

**Speaker:** probable Amrita. **To:** audience. **Type:** narration and workflow
advice. **Claimed authors:** Sherlock/Serena, plus Cursor cloud agents.

She says separate cloud agents are checking the front-end and back-end so
Sherlock can ground competitive answers in implementation. She proposes letting
them work and checking Mimi, then resends the slide request. The resend matters:
the earlier task is not treated as seamless completion.

Returning to research, she explains that a group chat can expose bot discussion
without hopping between conversations. Her first attempt appears to add the
wrong people; she retries, navigates through several screens and eventually says
both intended bots are in the chat. Exact UI behavior is not recoverable from
ASR alone, so no reliable sequence of clicks is invented.

### 00:57:24.024-01:00:05.752 | Ask for a low-effort differentiator

**Speaker:** probable Amrita. **To:** Sherlock and Serena, then audience.
**Type:** request and hypothetical follow-through.

She asks the two bots to identify a meaningful competitor differentiator that
would be low effort to build. She expects their combined code and product
knowledge to inform a response. She then describes possible follow-through:
create a product document or PR and put the research into a shared tool.

An AI travel agent is an illustrative possibility in this explanation, not the
bots' established recommendation. She lists Google Docs, Confluence and other
tools, and says browser access can sometimes substitute for a missing MCP or
API. Power BI and MongoDB are examples. The later Linux and anti-bot limitations
are essential qualifications; this is not a universal integration guarantee.
The sentence about accessing tools continues across the raw-part boundary.

### 01:00:05.752-01:03:15.288 | Teach a competitor-blog skill

**Speaker:** probable Amrita. **To:** Sherlock/audience. **Type:** narrated
computer demonstration and human-to-bot instruction.

She describes private skills, including an earlier slide-animation skill. To
teach a new research procedure, she takes over Sherlock's computer and records
herself searching for an Expedia technical blog, examining posts and looking
specifically for AI-related engineering content. A GraphQL item and a possible
agentic-platform article are mentioned; titles and findings are not verified.

After stopping the recording, she says Sherlock can use the learned procedure
for other competitors. She dictates that the important part was looking for
AI-related posts to keep the product's AI work informed. She explains that the
skill could have been taught through Serena instead and claims skills are
available across her bots. This records the claimed behavior, not an access-scope
or learning-quality test.

### 01:03:15.288-01:04:48.600 | Read the proposed improvements

**Speaker:** probable Amrita. **To:** audience. **Type:** paraphrase of reported
bot-to-bot discussion. **Claimed authors:** Sherlock and Serena.

Sherlock reportedly identifies managing existing bookings as table stakes and a
flexible-date calendar as a potentially easy improvement: some front-end wiring
exists but is not called. Serena reportedly distinguishes those from round-trip
and baggage work, which may look important but is not low effort. The presenter
reads a question about which of booking management and calendar improvements
felt more useful in the competing tools.

She points out direct bot tagging as a way to request specific expertise. The
comparison remains a recommendation under discussion, not a committed feature,
verified code finding or shipped change.

### 01:04:48.600-01:07:27.064 | Let the team propose its own helpers

**Speaker:** probable Amrita. **To:** Sherlock, with Serena referenced; then
audience. **Type:** human request and advisory examples.

She asks which additional bots would help with competitive differentiation and
sales engineering, and tells Sherlock to create them. A chief-of-staff bot
creating inbox or calendar helpers is a separate example, not something executed
in this demo.

She suggests giving a bot a particular customer/POC goal and asking it to design
a small support team. In her framing, the point is to reduce planning burden,
not create more management work. Which helpers actually appear is examined in
the next chapter; creation is only requested at this boundary.

## Editorial changes and unresolved evidence

- Flylo spelling variants are grouped only within this explicitly continuous
  sandbox demonstration; they are not merged with the live game studio.
- Technical concurrency claims, the ten-minute hold, feature effort and browser
  results require code/audio review. No external sites were accessed here.
- UI retries and the Mimi resend are preserved; navigation filler is condensed.
- Bot messages remain attributed to their claimed authors with Amrita as reader.
