# D1-C04: Grok Bot 101: demo bots, approvals and teaching

## Source and review state

- Interval: [00:38:21.208, 01:06:17.432).
- Source: X `1AxRnZbVpjaxl`; [inputs/hashes](README.md), [sources](../sources.md), [entities](../entities.md).
- **ASR-based review draft**, nonverbatim grouped conversation; not audio-verified. No quotations.
- Context: Grok Bot 101 or engineering **workshop** demonstration, separate from the hosts' live build.

## Input intervals and identity

Source/checkpoint hashes are in [the index](README.md). These are exact
silence-preserving PCM intervals, not audio-verified word or speaker boundaries.

| Part and hashes | Part-local interval | Source interval |
| --- | --- | --- |
| [part-02](README.md#part-02) | 00:08:21.208-00:30:00.000 | 00:38:21.208-01:00:00.000 |
| [part-03](README.md#part-03) | 00:00:00.000-00:06:17.432 | 01:00:00.000-01:06:17.432 |

## Edited conversation

### 00:38:21.208-00:40:29.464 | Agenda and three demo bots

**Speaker:** Amrita D1-H05, named by the host in forms such as Rita and thanked Roman by name. **To:** in-room audience/stream. **Type:** workshop introduction.

Amrita points to the week's enterprise sessions for go-to-market, engineering, marketing and admins, and a public galaxy page for registration. She introduces three bots for the demo: Data Dan D1-B-DATADAN-A, Slide Sonia D1-B-SONIA-A and Email Ethan D1-B-ETHAN-A. The plan is to collect audience data through a form, turn it into slides and charts, and email a stakeholder. Slide Sonia and Email Ethan already exist; Data Dan is to be created live.

### 00:40:29.464-00:43:57.560 | Creating Data Dan and a coffee survey by voice

**Speaker:** Amrita. **To:** audience; then Data Dan. **Type:** narrated creation and dictated instruction.

She creates Data Dan and says Grok Bot suggests purposes from a bot name. Using voice mode, she dictates a request for a Google Form asking how many cups of coffee people drink per day and their favorite San Francisco coffee shops, with four named options. She says two-way voice is deployed internally and expected publicly soon; that release timing is a claim. She opens the bot's computer view, describing an isolated Linux VM, and shows installed plugins/MCPs. When the bot requests approval for a task she allows it, previewing configurable approval rules.

### 00:43:57.560-00:51:49.752 | Teaching Slide Sonia and routines

**Speaker:** Amrita. **To:** audience; Slide Sonia. **Type:** demonstrated teaching and instructions.

She uses teach a task while controlling Slide Sonia's computer herself, adding and previewing a fly-in animation, then stops the recording; she reports that the recording becomes a reusable skill. She says the bots have isolated computers so they can work in parallel, and that she and a bot can edit different slides of the same deck. Slide Sonia's description includes font/color rules and a screenshot-on-completion rule. She adds a routine asking Sonia to summarize deck changes and who made them each morning at 9 a.m., and describes a cross-bot weekly summary routine as a possible pattern.

### 00:51:49.752-01:00:00.248 | Email rules and bot-to-bot requests

**Speaker:** Amrita. **To:** Data Dan, Email Ethan, audience. **Type:** dictated requests, reported bot messages and advice.

She checks Data Dan, which is still building the form and asking for many approvals. She asks Email Ethan to draft an email to a named contact about coffee data, then adds a rule that the bot must ask before replying to emails. She then asks Data Dan to message Slide Sonia (also called Slide Guru) for details of a 101 deck for an email to a coworker. She reads messages showing Email Ethan asking Data Dan for data, Data Dan saying the spreadsheet is not ready, and Email Ethan choosing an existing coffee-cup **sample data set** instead. Slide Sonia is reported scanning the deck to provide an outline. These are displayed bot messages narrated by Amrita, not independently inspected.

### 01:00:00.248-01:06:17.432 | Duplicating, sharing templates and an email draft

**Speaker:** Amrita. **Type:** advice and demonstration.

An auto-review block prevents a reply until she clicks allow once. She recommends duplicating bots for differently tailored email audiences, sharing bots as templates, and publishing to a team; she points to public marketplace bots including Lauren's. She shows an email draft modal that can be edited, readdressed, deleted or rephrased. Data Dan reports the form ready; she asks it to turn the form into a scannable QR code. She describes sidebar sections, including an engineering section, and creates a group chat with the three bots. She tells the bot no security check is needed for the QR step and recommends treating refusals or questions as signs a bot needs teaching, stored in memory.

## Editorial changes and unresolved evidence

The contact name in the email request is omitted as incidental. Bot names Slide Sonia/Sonya/Slide Guru are grouped as one displayed bot with aliases, pending screen evidence. Use of sample data is kept distinct from any live survey results.
