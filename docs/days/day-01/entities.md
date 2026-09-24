# Day 1 entity and alias ledger

Status: **ASR-based review draft**. These are Day 1 evidence-local IDs, not a
verified participant roster. No identities are imported from Day 2 or Day 3.
All times refer to X `1AxRnZbVpjaxl` on the silence-preserving PCM timeline; see
[sources](sources.md) and the [chapter index](transcripts/README.md).

## Attribution rules

A self-introduction or explicit address is stronger textual evidence than
continuity, but remains subject to audio review. No diarization, face/voice
recognition or numerical identity confidence was available. Later turns are
probable by topic, screen narration and role continuity, not confirmed by voice.
`D1-HU` is a category for unresolved or mixed humans, not one person.

A human reading a response remains the speaker; the bot is only the claimed
output author. Bot names are not unique: separate owners' copies stay separate.
Demo-company titles (CEO, CPO, CTO, chief potato officer) are stream roles, not
employment titles.

## Human candidates

| ID | Candidate and basis | Source interval | Uncertainty |
| --- | --- | --- | --- |
| D1-H01 | Matt Palmer, host; self-introduction as developer experience | [C01](transcripts/01-opening-and-host-introductions.md), 00:06:08.632 within 00:04:15.608-00:07:04.544 | Surname from ASR self-introduction only; later turns probable; called CEO of the demo company |
| D1-H02 | Lauren, host, alias Potato; self-introduction | [C01](transcripts/01-opening-and-host-introductions.md), 00:10:11.352-00:12:04.640 | Surname not stated in Day 1 ASR; demo titles CTO/chief potato officer |
| D1-H03 | Roshan, host, product; self-introduction | [C01](transcripts/01-opening-and-host-introductions.md), 00:08:29.544 within 00:07:04.544-00:10:11.352 | Surname not stated; probable PM-workshop co-presenter in [C22](transcripts/22-pm-workshop-colleague-model-and-bot-team.md) |
| D1-H04 | Roman, Grok Bot 101 presenter | [C03](transcripts/03-grok-bot-101-product-principles.md), whole chapter; thanked by name at 00:38:21.208 | Surname and role unstated |
| D1-H05 | Amrita, 101 demo presenter and self-described field engineer | [C04](transcripts/04-grok-bot-101-demo-bots-approvals-and-teaching.md)-[C06](transcripts/06-grok-bot-101-questions-and-summary.md), 00:38:21.208-01:29:44.848 | ASR also renders Rita/Ann Reardon; full name not verified |
| D1-H06 | Peter Yang, guest; former PM, creator | [C07](transcripts/07-peter-yang-joins-and-audience-idea-research.md)-[C09](transcripts/09-prototype-bot-dogfooding-and-peter-advice.md), 01:32:20.696-02:24:35.320 | Surname from recap in [C14](transcripts/14-post-break-review-factory.md); self-reports unverified |
| D1-H07 | Codie Sanchez, guest; ASR renders Cody | [C12](transcripts/12-codie-sanchez-controversy-and-distribution.md)-[C13](transcripts/13-codie-sanchez-research-bot-lead-magnets-and-break.md), 02:55:28.344-03:19:30.960 | Full name at host closing near 03:18:37; business metrics are self-reports |
| D1-H08 | Lingxi, engineering-workshop presenter; self-introduction | [C15](transcripts/15-engineering-workshop-principles-and-use-cases.md)-[C16](transcripts/16-engineering-workshop-bot-fleet-demo.md), 03:54:08.056-04:39:25.360 | Founders presenter later says Lingji; surname unstated |
| D1-H09 | Kevin, PM-workshop presenter; self-introduction | [C22](transcripts/22-pm-workshop-colleague-model-and-bot-team.md)-[C23](transcripts/23-pm-workshop-flylow-demo-and-questions.md), 05:54:10.488-06:33:17.424 | ASR surname DiParco unreliable; turns alternate with co-presenter |
| D1-H10 | Eric, guest; introduced as co-founder/CEO of a creator finance company | [C24](transcripts/24-eric-narrows-audience-to-tech-brand-merch.md)-[C26](transcripts/26-build-a-grok-bot-merch-and-platform-advice.md), 06:41:15.096-07:23:10.640 | Surname not in ASR; inherited map says Eric Wei, unconfirmed; company spelling unresolved |
| D1-H11 | Shub, founders-workshop presenter; self-introduction | [C27](transcripts/27-founders-workshop-framing-and-close-bot.md)-[C29](transcripts/29-founders-questions-and-challenge.md), 07:23:29.240-08:18:43.640 | Surname unstated |
| D1-H12 | Jenny, **human** guest; VC, creator, agency founder | [C30](transcripts/30-jenny-joins-bot-roster-and-venue-criteria.md)-[C31](transcripts/31-event-budget-permit-bot-and-overnight-agents.md), 08:20:13.112-08:41:48.664 | Surname unresolved; **not** D1-B-JENNY-X |
| D1-HU | Unresolved attendees, questioners, production crew, chat voices and inseparable host turns | Throughout; exact groups in the [index](transcripts/README.md) | Do not merge questioners or infer identity from voice |

Named people who are only mentioned (teammates, marketplace publishers, quoted
founders and creators) are not participants and receive no ID.

## Host live-build bots

Owner suffix L, M or R means candidate owner Lauren, Matt or Roshan; U means
unresolved. Entity descriptions inherit the cited chapter's ASR-only status.

| ID | Label / role / owner | Evidence and qualifications |
| --- | --- | --- |
| D1-T-EGG | Dr. Eggbot marketplace template, created by Lauren to build bots | [C08](transcripts/08-restaurant-ideas-to-pop-up-platform.md), 01:55:41.464-02:00:00.216; template is not an instance |
| D1-B-EGG-L | Lauren's installed Dr. Eggbot | Same C08 interval; asked to make Tater in [C10](transcripts/10-tater-roles-and-repository-setup.md) |
| D1-B-EGG-M | Matt's installed Dr. Eggbot copy | [C08](transcripts/08-restaurant-ideas-to-pop-up-platform.md), 02:03:02.296-02:07:03.544; later bot creation in C09, C11, C13, C18 |
| D1-B-STEVE-L | Steve, Lauren's default bot turned chief of staff | [C08](transcripts/08-restaurant-ideas-to-pop-up-platform.md), 02:03:02.296-02:07:03.544; opened a large PR in [C11](transcripts/11-first-deploy-database-domain-and-main-rule.md); **not Lingxi's Steve** |
| D1-B-XBOT-L | Lauren's X plugin bot | C08, 02:00:00.216-02:03:02.296 |
| D1-B-GROKPOT-L | Prototype bot named from chat; spelling Grokpot/Grot/Grottapot | [C09](transcripts/09-prototype-bot-dogfooding-and-peter-advice.md), 02:09:57.592-02:12:23.000; reported name-update bug |
| D1-B-TATER-L | Tater, Lauren's engineer bot using cloud agents | [C10](transcripts/10-tater-roles-and-repository-setup.md), 02:24:35.320-02:27:43.000; [C11](transcripts/11-first-deploy-database-domain-and-main-rule.md), [C17](transcripts/17-review-channel-verification-and-waitlist.md), [C19](transcripts/19-venue-finder-maps-auth-and-flyers.md) |
| D1-B-HASHBROWN-L | Hash Brown, reviewer of Tater's PRs, reportedly created during the break | [C14](transcripts/14-post-break-review-factory.md), 03:50:17.912-03:52:31.384; creation not observed |
| D1-B-DROP-L | Drop, Lauren's merch bot using Grok Imagine | [C25](transcripts/25-merch-novelty-templates-and-tickets.md), 07:04:47.544-07:06:15.704 |
| D1-B-MARKY-R | Marky Mark market-research bot on Roshan's screen | [C07](transcripts/07-peter-yang-joins-and-audience-idea-research.md), 01:32:20.696-01:45:50.520; output read in [C08](transcripts/08-restaurant-ideas-to-pop-up-platform.md) |
| D1-B-DESIGN-R | Roshan's existing designer bot | C08, 02:00:00.216-02:03:02.296; flyers requested in [C19](transcripts/19-venue-finder-maps-auth-and-flyers.md) |
| D1-B-MARKET-M | Matt's separate market-research bot | C08, 01:53:09.312-01:55:41.464 |
| D1-B-PROSPECT-M | Matt's prospecting bot, requested via Dr. Eggbot | C08, 02:03:02.296-02:07:03.544; request only |
| D1-B-PRIORITIZER-M | Matt's prioritization bot | [C09](transcripts/09-prototype-bot-dogfooding-and-peter-advice.md), 02:09:57.592-02:12:23.000; listed in C17 |
| D1-B-OPS-M | Matt's ops bot | [C11](transcripts/11-first-deploy-database-domain-and-main-rule.md), 02:36:10.360-02:39:00.696 |
| D1-B-CREATIVE-M | Matt's creative director for naming | Same C11 interval; domain names in C11 G03 |
| D1-B-OPRESEARCH-M | Operator-research bot from the Codie exercise | [C13](transcripts/13-codie-sanchez-research-bot-lead-magnets-and-break.md), 03:10:20.728-03:14:02.776; listed by Matt in C17; template promised in C26; owner probable |
| D1-B-FOUNDENG-M | Matt's founding-engineer bot for the lander | [C17](transcripts/17-review-channel-verification-and-waitlist.md), 04:52:26.072-04:55:12.056 |
| D1-B-OUTREACH-M | Outreach bot requested via Dr. Eggbot | [C18](transcripts/18-core-flow-debate-and-running-the-pop-up-first.md), 05:01:04.216-05:03:06.968; mentioned in C26 |
| D1-B-HOSTFINDER-M | Host/venue finder writing to Notion | [C21](transcripts/21-venue-criteria-permits-and-art-pivot.md), 05:32:16.536-05:36:51.640 |
| D1-B-KBM-M | Knowledge-base manager; passive, then polling | [C20](transcripts/20-knowledge-manager-stack-flyer-copy-and-merch.md), 05:17:29.784-05:19:04.984; [C21](transcripts/21-venue-criteria-permits-and-art-pivot.md), 05:34:37.432-05:36:51.640; owner probable Matt |
| D1-B-DROP-M | A second merch bot also named Drop | [C26](transcripts/26-build-a-grok-bot-merch-and-platform-advice.md), 07:12:13.400-07:16:17.688; owner probable Matt; **not D1-B-DROP-L** |
| D1-B-GEO-U | Street-corner/flyer research bot | [C19](transcripts/19-venue-finder-maps-auth-and-flyers.md), 05:15:15.224-05:17:29.784; owner probable Roshan |
| D1-B-MENU-U | Menu-concept bot | [C21](transcripts/21-venue-criteria-permits-and-art-pivot.md), 05:36:51.640-05:39:34.200 |
| D1-B-BUDGET-U | Event-planner/budget bot fired off during Jenny's advice | [C31](transcripts/31-event-budget-permit-bot-and-overnight-agents.md), 08:31:39.736-08:39:03.096; no output shown |

Cursor cloud agents, a Cursor project agent and a Cursor PR-review automation
are separate agent systems, not Grok Bot instances. Unnamed ticket-design,
naming, prototype and permit bots remain role descriptions without IDs.

## Workshop and guest bots

These are presenter-owned demo systems, never the hosts' live build.

| ID | Owner/context and role | Evidence |
| --- | --- | --- |
| D1-B-DATADAN-A | Amrita; Data Dan, created live for a coffee form | [C04](transcripts/04-grok-bot-101-demo-bots-approvals-and-teaching.md), 00:40:29.464 onward; form access failed in C05 |
| D1-B-SONIA-A | Amrita; Slide Sonia, alias Sonya/Slide Guru | C04, 00:43:57.560-00:51:49.752 |
| D1-B-ETHAN-A | Amrita; Email Ethan, used sample data | C04, 00:51:49.752-01:06:17.432 |
| D1-B-MANAGER-A | Amrita; manager bot created live | [C05](transcripts/05-grok-bot-101-qr-failure-group-chat-and-manager.md), 01:10:59.160-01:14:15.992 |
| D1-B-LINGSHISHI-X | Lingxi; chief of staff, ASR Ling Shishi | [C16](transcripts/16-engineering-workshop-bot-fleet-demo.md), 04:16:15.928-04:18:11.384 |
| D1-B-CRAIG-X | Lingxi; Craig, UI engineering, aliases Cry/Crank/Kreg | C16, 04:16:15.928-04:35:33.304 |
| D1-B-STEVE-X | Lingxi; Steve for developer experience | C16, 04:16:15.928-04:18:11.384; **not Lauren's Steve** |
| D1-B-NIGHTLY-X | Lingxi; nightly audit engineer, renamed Steve | C16, 04:18:11.384-04:35:33.304; relation to STEVE-X unresolved |
| D1-B-HOGAN-X | Lingxi; Hogan, infrastructure | C16, 04:16:15.928-04:18:11.384 |
| D1-B-JENNY-X | Lingxi; Jenny, head-of-operations **bot** owning a playbook | C16, 04:21:28.920-04:35:33.304; **not human Jenny D1-H12** |
| D1-B-CORA-P | PM workshop; Cora, chief of staff | [C22](transcripts/22-pm-workshop-colleague-model-and-bot-team.md), 06:03:47.256-06:08:56.344 |
| D1-B-EMILY-P | PM workshop; Emily, engineering manager | C22 same; delegation in [C23](transcripts/23-pm-workshop-flylow-demo-and-questions.md) |
| D1-B-ASHLEY-P | PM workshop; Ashley, data science; claimed author of the funnel correction | C23, 06:11:05.656-06:17:32.248 |
| D1-B-PMP-P | PM workshop; PMP, also Pete, PRDs | C23, 06:15:12.952-06:23:20.984 |
| D1-B-PIXEL-P | PM workshop; Pixel, designer | C23, 06:17:32.248-06:23:20.984 |
| D1-B-RAY-P | PM workshop; Ray, recruiter | C22, 06:03:47.256-06:08:56.344 |
| D1-B-PMENG-P | PM workshop engineer bots: Einstein, Ego, Nova, Larry, Eileen | C23, 06:08:56.344-06:11:05.656 and 06:23:20.984-06:27:27.928; names ASR-uncertain; grouped, not individually verified |
| D1-B-CLOSE-S | Shub; Close Bot | [C27](transcripts/27-founders-workshop-framing-and-close-bot.md), 07:32:51.192-07:41:46.936 |
| D1-B-PROD-S | Shub; Prod Bot | [C28](transcripts/28-founders-workshop-prod-stalk-proto-and-tips.md), 07:41:46.936-07:44:27.416 |
| D1-B-STALK-S | Shub; competitor-tracking bot, ASR Stock/Stalk Bot | C28, 07:44:27.416-07:48:39.160; spelling unresolved |
| D1-B-PROTO-S | Shub; Proto Bot with its own Grok Bot account | C28, 07:48:39.160-07:54:13.048 |
| D1-B-YAP-S | Shub; writing-as-him bot | Same C28 interval |
| D1-B-MISC-S | Shub; miscellaneous-requests bot | Same C28 interval |
| D1-B-MASTERCHIEF-J | Jenny's chief-of-staff bot, Master Chief | [C30](transcripts/30-jenny-joins-bot-roster-and-venue-criteria.md), 08:20:13.112-08:22:51.128; self-report |
| D1-B-BOXY-J | Jenny's inbox monitor | C30, 08:22:51.128-08:24:57.848 |
| D1-B-SCRIBE-J | Jenny's meeting-notes/delegation bot | Same C30 interval |
| D1-B-SCOUT-J | Jenny's venue-search bot, described as her own | C30, 08:27:34.424-08:30:01.752 |

## Organizations and contexts

| ID or category | Meaning and boundary | Evidence |
| --- | --- | --- |
| D1-O-SHIP | Ship by Thursday: hosts' GitHub organization, working company name and a reported domain | [C02](transcripts/02-business-goals-tools-and-blank-slate.md), 00:21:36.312-00:25:10.808; [C11](transcripts/11-first-deploy-database-domain-and-main-rule.md), 02:49:44.152-02:52:40.336 |
| Pop-up concept | Evolving live-build idea: restaurant pop-up and platform, own pop-up, tentative October 15, art exhibition, tech-brand merch, build-a-Grok-Bot | C08-C09, C18, C21, C24-C26; ends in doubt in [C32](transcripts/32-day-one-retrospective.md) |
| D1-O-FLYLOW | Flylow Airlines demo company used by engineering, PM and founders workshops | C16, C23, C28; not a real customer or the hosts' company |
| D1-O-NORTHWIND | Founders-workshop demo customer, a note-taking/meeting product | C27, 07:32:51.192-07:38:38.008 |
| Livestream challenge | Template-sharing contest with Starbase trip, repeated through the day | C01, C06, C21, C23, C29, C32; terms spoken, not verified |

## Mandatory non-merges and remaining checks

- Lauren's Steve D1-B-STEVE-L, Lingxi's Steve D1-B-STEVE-X and Lingxi's renamed
  nightly bot D1-B-NIGHTLY-X stay separate.
- Human guest Jenny D1-H12 and Lingxi's bot Jenny D1-B-JENNY-X stay separate.
  No bot owned by guest Jenny is named Jenny in ASR.
- Dr. Eggbot: template D1-T-EGG, Lauren's copy and Matt's copy stay separate.
- Two Drop merch bots stay separate. Hash Brown and Tater are Lauren's by her
  narration only.
- Inherited uncertain names: Grokpot (retained), research bot (Marky Mark),
  Slide Sonia/Sonya (retained as aliases), Ling Shishi, Pete/PMP (one bot by
  presenter wording), Ego (one of five grouped PM engineer bots), Stockbot/Stalkbot
  (one competitor bot) and Scribe (Jenny's notes bot). None is audio-verified.
- All names, employers and ownership await the [audio review queue](review-queue.md).
