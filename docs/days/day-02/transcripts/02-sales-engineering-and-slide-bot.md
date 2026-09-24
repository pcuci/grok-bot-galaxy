# D2-C02: Sales engineering and the slide bot

## Source and review state

- Source: X `1PKqrNyvmYwGb`; [hashes and provenance](../sources.md).
- Interval: [00:30:00.000, 00:45:07.696).
- Input: `part-02.json`, local [00:00:00.000, 00:15:07.696), with TXT read in full.
  Raw inputs live under `.data/day-02/transcripts/` and remain unchanged.
- Artifact: nonverbatim edited conversation; **ASR-based review draft**.
- No listening, screen inspection, direct quotations or external-source checking.
- Speaker: probable Amrita, from self-introduction at 00:30:02.488. Employer
  wording alternates between Cursor and SpaceX in ASR and remains unresolved.
- Addressee throughout: workshop audience, except explicitly described bot prompts.

## Orientation

The presenter introduces sales-engineering workflows, then requests a templated
customer-case-study slide. These examples are not the hosts' game-studio build.

## Edited conversation

### 00:30:00.000-00:31:48.728 | Session and demonstration boundary

**Speaker:** probable Amrita. **Type:** introduction and session plan.

The presenter introduces herself as a field engineer and outlines sales
engineering, sales, SDR and support workshops, with returns to Matt, Lauren and
Roshan's company-building stream. Today she will show three bots she says she
uses regularly. Two will operate in a sandbox demo project; another supports
customer case-study slides in her own workflow. She promises product context,
demos, questions and in-person build time. QR-code coasters offer starting
templates; those codes are not inspected here.

### 00:31:48.728-00:34:52.984 | Colleague metaphor and computer access

**Speaker:** probable Amrita. **Type:** product explanation and experience claims.

She contrasts one-off chatbot requests with a team of persistent bots that can
work while a user is away or using a phone. The intended value is finished work,
not continual supervision. She describes a messaging interface, long-lived
memory and feedback that can influence later work.

Bots have their own computers. She cites earlier form creation and a reported
MongoDB-analysis example, rather than demonstrating those tasks in this interval.
She says users can inspect or take control of the computer and enterprise admins
can restrict websites and downloads. These are presenter claims, not an audit of
access enforcement. The colleague metaphor does not establish unsupervised safety.

### 00:34:52.984-00:38:06.168 | Routines, sharing and completion claims

**Speaker:** probable Amrita. **Type:** usage examples and product advocacy.

She describes a morning routine that finds relevant newsletters and podcasts in
email and sends a digest to Slack. A similar routine can summarize overnight
work messages, particularly for distributed teams. Shared sales and engineering
bots are presented as a way to keep resources and behavior consistent.

She says a new bot asks what it is for, and proposes asking a bot which teammates
it needs, rather than designing every assistant manually. She emphasizes coming
back to completed work instead of repeated approval questions. Later security
questions qualify this broad framing; it is not permission for arbitrary action
or proof that every task finishes successfully.

### 00:38:06.168-00:41:25.144 | Three specialist roles

**Speaker:** probable Amrita. **Type:** explanation. **Claimed output authors:**
Sherlock, Serena Williams, Echo and Mimi where named; none is an audible human.

For technical customer questions, she uses a bot called Sherlock with repository
access. Questions may concern security, memory or implementation details absent
from public docs. She says she has instructed it not to disclose IP and to use
customer-appropriate language. This is an instruction, not proof of leak prevention.

She calls her competitor-research bot Serena Williams, explaining that the name
references studying competitors. It can try products in its computer, compare
behavior and suggest improvements. This bot is distinct from the human athlete.

She describes Echo as assembling relevant slides from a master deck using call
notes, and says other presenters may show it later. Her own demonstration will
use Mimi for customer proof points, Sherlock for technical expertise and Serena
for competitor research. The distinction between preparatory claims and this
live exercise is retained.

### 00:41:25.144-00:43:37.464 | Teach a consistent case-study format

**Speaker:** probable Amrita. **To:** audience. **Type:** narration of prior work
and paraphrase of claimed Mimi output. **Claimed author:** Mimi; source material
reportedly comes from customer blog posts.

She opens Mimi's description and computer, saying it has access to a slide deck.
The desired format is consistent: logo, problem, solution, impact and a sourced
quotation. She describes existing Starlink and Jellyfish examples. Company and
product associations in this ASR are inconsistent; no customer relationship is
independently verified here.

For Jellyfish she says a short request plus a blog link was enough because Mimi
already knew the job. She describes Mimi finding the brand logo, arranging the
content and taking screenshots. The audience is being shown prior claimed work,
not watching that earlier creation occur. No quoted blog text is reproduced.

### 00:43:37.464-00:45:07.696 | Request a Salesforce slide

**Speaker:** probable Amrita. **To:** Mimi, then audience. **Type:** human-to-bot
request followed by narration. **Claimed source:** a Salesforce blog post.

She selects a post she describes as reporting an 85% reduction in a legacy
code-coverage task. The metric, baseline and product association require checking;
it is not adopted as a verified result. She asks Mimi to create another slide
for Salesforce and supplies the post.

She expects Mimi to insert the slide into the deck, work with its own cursor,
and return screenshots/status. She checks access, then switches accounts to
Sherlock and Serena while Mimi works. At this point the slide has been requested,
not verified as finished. Later retries and the reported result are retained in
D2-C04.

## Editorial changes and unresolved evidence

- The many computer/screen navigation fragments are condensed without implying
  that this editor inspected the screen.
- Product and employer inconsistency, the 85% figure, claimed security controls
  and customer proof points are in the review queue.
- Placeholder noise and unrecognized fragments remain explicit coverage
  limitations. Repetition explaining the same routine is consolidated here.
- No live-company outcome or direct quotation is extracted from this workshop.
