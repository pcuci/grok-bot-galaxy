# Day 2 entity and alias ledger

Status: **ASR-based review draft**. IDs are local editorial handles, not verified
identities. Evidence is only the full-day X ASR linked in the
[chapter index](transcripts/README.md). No voice recognition, external profiles,
YouTube captions or guessed cross-source alignment were used.

## Attribution rules

- Probable means an introduction, explicit address or described ownership supports
  the candidate. It does not mean audio-verified spelling or diarized turns.
- A bot named for a person is not that person. A template, an installed instance,
  a game-card representation and a spawned coding agent are distinct entities.
- Unnamed/mixed hosts and audience questioners remain unresolved; chapter labels
  identify the plausible group, not an invented exact speaker sequence.
- Humans narrate/read all reported bot messages. The named bot is the claimed
  author/worker, never automatically the audible speaker.

## Human candidates

| ID | Candidate and role | Evidence and limits |
| --- | --- | --- |
| D2-H01 | Matt, host | Host introductions from 00:10:03.992; explicitly addressed at 05:46:23.096 and 08:17:59.640. Distinct from Matthew Berman. Surname/employer not established. |
| D2-H02 | Roshan, host | Introductions from 00:10:03.992; self-introduction during Karen segment, explicit address at 07:07:24.216. ASR variants Russian/Roshen are contextual candidates only. |
| D2-H03 | Lauren, host; Potato alias candidate | Introductions from 00:10:03.992; hosts address her during bot and backend work, including 08:14:09.080. Alias refers to contextual self/presenter usage, not every potato term. |
| D2-H04 | Amrita, sales-engineering presenter | Self-introduction around 00:30:02.488; continuous workshop through 01:23:56.184. Surname/employer unresolved. |
| D2-H05 | Marcel, coffee co-owner in customer clip | Self-introduction 02:13:22.264-02:14:06.072. Business spelling Icon/Eich-On unresolved; not host company. |
| D2-H06 | Karen X Cheng, creator guest | Interview 02:39:03.512-03:03:48.124; closing self-identification/spelling supports Cheng over garbled opening surname. Still probable, not external identity verification. |
| D2-H07 | Krista/Crystal Letts, sales presenter | Introductions 04:00:00.000 onward and handoff at 04:05:34.584. Given name remains unresolved; exact turns sometimes mixed with Mark. |
| D2-H08 | Mark Wright, sales presenter | Introductions 04:00:00.000 onward; recap and contrasting preferences 04:15:47.800-04:23:32.024. Probable, not diarized. |
| D2-H09 | Matthew/Matt Berman, guest | Self-identification 04:43:49.368; interview through 05:09:55.128. Never merge with D2-H01. |
| D2-H10 | Unnamed customer-video speaker | 05:09:55.128-05:13:11.832; introduced as Nokia product/engineering executive, but ASR organization/title wording differs. Identity unresolved. |
| D2-H11 | Student guest; Shardul/Shredule Marathe candidate | 05:13:11.832 onward; Stanford rising-junior/CS self-description; garbled spoken handle/spelling 05:56:06.392-05:56:45.788. No guessed handle. Intern language is banter, not proof of employment. |
| D2-H12 | Simon, SDR presenter | Self-introduction 05:59:52.376 across part boundary. Human distinct from Simon Bot and Simon Soldiers. Employer wording unresolved. |
| D2-H13 | David, support presenter | Self-introduction 07:30:52.216; user-operations engineering role claimed. Surname/employer unresolved. |
| D2-HU | Unresolved audience, moderator, production and mixed speakers | Used throughout workshop questions and transitions; not one person. A relayed viewer question does not identify the audible reader as the viewer. |

### Mentioned people are not established participants

Brian and Alex are mentioned collaborators in Matthew's editing account
(04:43:49.368-04:46:43.704); Lee Robinson is mentioned in Matt's onboarding story
(04:54:18.584-04:58:56.952); Kenny and Justin receive design credits
(05:46:36.088-05:47:24.240). Lenny with an uncertain surname appears in a
secondhand payment example (06:55:04.856-06:55:25.336). A Paul is mentioned as
inspiration for a comment-cleanup specialist (03:38:01.944-03:41:19.544).
No full identities, participation or attribution of speech are inferred.

## Host bot instances and templates

| ID | Name/owner candidate | Role, evidence and separation rule |
| --- | --- | --- |
| D2-T-EGG | Dr. Eggbot template | Meta-bot for creating/configuring bots; repeatedly discussed, including 01:29:32.312-01:32:55.512. Not one installed instance or a human. |
| D2-B-EGG-L | Lauren's Dr. Eggbot instance | Her team configuration, including 07:14:24.696-07:15:34.800 and 08:16:28.664-08:17:35.152. Separate from other hosts' installs. |
| D2-B-EGG-M | Matt's Dr. Eggbot instance candidate | Cupcake Eng rewrite 03:33:56.824-03:42:01.496 and ads onboarding 05:36:37.208-05:38:18.704. Ownership contextual, continuity not proven. |
| D2-B-EGG-R | Roshan's Dr. Eggbot instance candidate | Prototype/game/sound requests 07:00:08.184-07:03:02.128 and 07:27:13.368-07:29:13.808. Do not merge with Lauren/Matt. |
| D2-B-STEVE-L | Steve, Lauren's coordinator | Explicit ownership around 01:31; role restated 03:38:01.944-03:41:19.544. A bot, not a human Steve. |
| D2-B-STEVE-M | Steve, Matt's coordinator candidate | My Steve during Remotion onboarding, 05:37:42.648-05:38:18.704. Separate from Lauren's Steve; earlier unnamed Matt coordinator only a continuity candidate. |
| D2-B-COORD-R | Unnamed Roshan coordinator | Task-board/PR coordination 06:43:11.288-06:45:39.984; no safe basis to name it Steve. |
| D2-B-ENG-M | Cupcake Eng, Matt's helper candidate | Engineering-context request and description review 03:33:56.824-03:42:01.496. Link to earlier founding-engineer label unresolved. |
| D2-B-BAKE-R | Bake, Roshan's founding engineer candidate | Named 06:44:27.160-06:45:17.168; PR watching and game-design exchange later. Not automatically Cupcake Eng. |
| D2-B-TATER-L | Tater, Lauren's engineer | Role explanation 03:38:01.944-03:41:19.544; project-agent delegation 07:21:42.040-07:22:09.456. |
| D2-B-MASH-L | Mash, Lauren's team candidate | Mentioned 03:38:01.944-03:41:19.544 and 07:23:32.664-07:24:10.652; role unresolved. Mashed as a verb is not a bot attribution. |
| D2-B-HASH-L | Hash Brown, Lauren's team candidate | Mentioned 03:38:01.944-03:41:19.544; role/instance continuity unresolved. |
| D2-B-PING-R | Ping/Hing, Roshan's Slack watcher candidate | Same-prompt creation 06:47:46.040-06:50:57.208; mention/DM correction 07:13:43.416-07:15:43.888. Ownership probable. |
| D2-B-PING-L | Separate Lauren Slack watcher candidate | Simultaneous creation and same-name exchange 06:47:46.040-06:50:57.208; not merged with D2-B-PING-R. |
| D2-B-PING-M | Separate Matt Slack watcher candidate | Same creation experiment; final connection/name not cleanly attributable. Later checking listeners at 07:17:22.936. Distinct candidate, not proven successful install. |
| D2-B-PM-L | Unnamed Lauren PM bot | Request to maintain Notion separately from Slack mentions, 06:58:05.016-06:58:31.248. Creation/result only as narrated later. |
| D2-B-GLOW-R | Glow, visual prototyper | Named 07:02:20.344-07:02:52.400; lightweight 3D/2.5D experiments, not a shipped client. |
| D2-B-CRIT-R | Crit, game-design reviewer | Named 07:02:52.984; consults founding engineer 07:12:34.008 and 07:16:33.112 onward. Separate from Lauren's research bot. |
| D2-B-WHISK-L | Whisk, game designer | Named 08:15:56.440. Possible relation to earlier unnamed Lauren research bot, not confirmed. |
| D2-B-CHROME-L | Chrome, playtester | Named 08:15:59.352; functional clicking/bugs, game-quality feedback not yet taught. Not every browser Chrome mention. |
| D2-B-TONES-R | Tones, audio engineer | Requested 07:27:52.088 and named 07:29:01.496; candidates reviewed 08:11:21.592-08:13:50.896. |
| D2-B-ADS-M | Unnamed Remotion/ad specialists | Requests 05:34:47.384-05:39:18.744 and 06:51:14.584 onward. Creative assets versus marketplace engineering may be different workers; do not merge into one proven instance. |
| D2-B-PROJECT-L | Unnamed project coordinator/subagent group | 07:20:37.592-07:24:28.368; Tater works with it. Coding subagents are not automatically persistent Grok Bot instances. |
| D2-U-GAMECARD | Imported game-card entities | Templates represented in the game, discussed 00:12:40.888 onward. A Dr. Eggbot card does not itself identify the live coordinating bot. |

## Workshop and guest bot candidates

| ID | Name/owner | Role and evidence |
| --- | --- | --- |
| D2-B-MIMI-A | Mimi, Amrita | Slide/case-study helper, 00:38:06.168-00:45:07.696; Salesforce result 01:07:27.064. |
| D2-B-SHERLOCK-A | Sherlock, Amrita personal-team candidate | Expert-role explanation 00:38:06.168-00:41:25.144; do not merge with switched demo account. |
| D2-B-SHERLOCK-DEMO | Sherlock, Amrita's Flylo demo instance | Explicit account switch and repository expertise 00:45:07.696-00:48:00.088. Human reads claimed code findings. |
| D2-B-SERENA-DEMO | Serena Williams, Flylo demo competitor bot | 00:48:00.088-01:07:27.064. Named bot, not the athlete participating. Earlier role description does not prove identical account instance. |
| D2-B-BLAIR-DEMO | Battle Card Blair | Proposed/new helper in team expansion 01:04:48.600-01:15:43.928; generated role, completion not independently verified. |
| D2-B-DRAKE-DEMO | Demo Drake | Same expansion; demo/research helper candidate, exact scope needs audio. |
| D2-B-RADAR-DEMO | AI Radar | Same expansion; AI-research monitoring candidate. |
| D2-B-REX | Rex, Marcel | Coffee-business metrics/research account, 02:14:06.072-02:15:11.960. Not measured business results. |
| D2-T-PAPER | Karen's newspaper template | 02:42:41.944-02:50:19.000; distinguish reusable template from numerous test instances. |
| D2-B-KAREN | Karen's task-named bot group | Chief of staff, package/show/stock trackers and newspaper test instances, 02:39:03.512-03:01:49.912. Group inventory, not one bot. |
| D2-B-OLIVE | Olive, Krista/Crystal | Coordinator, named after her dog, 04:05:34.584-04:08:55.768. Dog is not bot or speaker. |
| D2-B-PG | PG, Krista/Crystal | Prospecting/outbound, 04:08:55.768-04:12:21.048. |
| D2-B-ECHO | Echo, Krista/Crystal | Call-informed decks; 04:05:34.584, clarification 04:30:40.760-04:31:57.816. Not continuous streaming. |
| D2-B-SALES-U | Unnamed customer/engineering bots | Sales workshop 04:12:21.048-04:15:47.800 and 04:25:53.048-04:28:55.192; owner-specific groups, not merged across presenters. |
| D2-B-BERMAN | Matthew's personal/business bot group | Family coordination, listings, sponsorship and utilities, 04:46:43.704-05:08:20.600. Exact instance split/names unresolved; not host Steve. |
| D2-B-STUDENT | Student's job-search bot group | Recruiter/alumni finders, job finder, letter writer and critic, 05:18:28.000-05:28:52.000. Role group, not a single instance; exact names unresolved. |
| D2-B-SIMON | Simon Bot, Simon's coordinator | 06:11:45.816-06:12:24.048; not D2-H12. |
| D2-B-SHAKESPEARE | Shakespeare, Simon | Email writer, 06:12:24.632 onward; the historical author is not a participant. |
| D2-B-WEBSEARCH | Web Search, Simon | Research coordinator, 06:12:34.232 onward. |
| D2-B-SOLDIERS | Simon Soldiers, plural worker group | 06:12:34.232-06:13:00.944 and Q&A 06:35:55.160-06:37:43.224. Group membership/count variable. |
| D2-B-SDR-RESEARCH | Simon's PLG/company/customer/enrichment helpers | 06:22:44.792-06:27:40.560. Distinct functional roles; exact instance aliases/merges unresolved. |
| D2-B-BUILD | Build, David demo | Setup/infrastructure, introduced 07:39:31.640-07:40:03.632; later trace setup account. |
| D2-B-REPLY | Reply, David demo | Customer and internal answers, same introduction; human David reads its claimed outputs. |
| D2-B-ALERT | Alert, David demo | Escalation/Slack, same introduction; SSO handoff 07:46:28.216-07:47:16.304. |
| D2-B-TUNE | Tune, David demo | Improvement/knowledge changes, same introduction; human supplies FAQ policy 07:52:41.272-07:53:19.632. |

## Demo organizations and reserved ambiguities

- `D2-O-STUDIO`: the hosts' live game-studio project, working game name Cupcake.
  Not Flylo and not automatically the hosts' employer.
- `D2-O-FLYLO-SE`, `D2-O-FLYLO-SDR`, `D2-O-FLYLO-SUPPORT`: related workshop
  examples using Flylo/Flylow/Vilo spellings. Keep environments and data separate;
  shared branding is not proof they share a deployed database or policy.
- `D2-U-TICKETS`: Alex, Ben-like, Carter, Damon and Elena/Selena support labels
  in C24 are seeded demo tickets, not established real customers or attendees.
- Human Steve, human Jenny and bot Jenny are **not established by this pass**.
  No Day 1 entity was imported merely to populate those categories. Any future
  occurrence requires separate evidence and an instance/owner check.

## Open identity work

Audio review is required for every candidate name and owner mapping. Unnamed
specialists remain role-based groups where finer identity would be invented.
This ledger does not attempt to identify family members, customers, contacts or
background speakers. Rights/privacy clearance is still required before sharing.
