# Day 3 entity and alias ledger

Status: **ASR-based review draft**. These are Day 3 evidence-local IDs, not a
verified participant roster. No identities are imported from Day 2. All times
refer to X `1YGNrbXEeazGw` on the normalized recording timeline; see
[sources](sources.md) and the [chapter index](transcripts/README.md).

## Attribution rules

A self-introduction or explicit address is stronger textual evidence than
continuity, but remains subject to ASR/audio review. No diarization, face/voice
recognition or numerical identity confidence was available. Later turns are
probable by topic and role continuity, not confirmed by voice. `D3-HU` is a
category for unresolved or mixed humans, not one persistent person.

A human reading a response remains the speaker; the bot is only the claimed
output author. Apparent generated voice in C20/C28/C29 is separately labeled.
A role, template, installed instance, game card and company are not interchangeable.

## Human candidates

| ID | Candidate and basis | Source interval | Uncertainty |
| --- | --- | --- | --- |
| D3-H01 | Host Matt, self-introduction in the opening group | [C01](transcripts/01-opening-and-overnight-rework.md), 00:09:56.440-00:12:21.720 | Not the marketing-ops guest Matt; employer wording is unstable |
| D3-H02 | Host Lauren, also Potato; opening introduction | [C01](transcripts/01-opening-and-overnight-rework.md), 00:10:12.600-00:12:21.720 | Later coding/card/Steve turns probable by continuity |
| D3-H03 | Host Roshan; opening and growth-segment introductions | [C01](transcripts/01-opening-and-overnight-rework.md), 00:10:17.688-00:12:21.720; [C11](transcripts/11-vincent-growth-ideas.md), 02:44:13.144-02:48:48.120 | ASR name variants are not additional people |
| D3-H04 | RevOps stage presenter, addressed as probable Max | [C02](transcripts/02-revops-task-routing.md), 00:34:20.024 onward; [C04](transcripts/04-revops-questions-and-transition.md), 01:05:30.744 within 01:04:12.696-01:07:45.752 | Introduction missing; possible same person as H07, not merged |
| D3-H05 | Vincent; growth guest; surname probably Zhu from spelled ZHU | [C11](transcripts/11-vincent-growth-ideas.md), 02:44:13.144-02:48:48.120; [C12](transcripts/12-vincent-bot-onboarding-and-promotions.md), 03:16:07.864-03:16:15.056 | Human distinct from both Vincent-named bot instances |
| D3-H06 | Executive in recorded enterprise video; ASR renders Cal Day and Tokyo | [C10](transcripts/10-enterprise-video-and-break.md), 02:35:12.056-02:38:24.888 | Name/company unresolved; do not substitute Day 2's identity |
| D3-H07 | Marketing-ops guest introduced as Matthew, later Matt | [C13](transcripts/13-marketing-ops-guest-and-cerebro.md), 03:24:42.744 within 03:23:06.520-03:26:02.584 | Says he presented earlier; same task demo suggests H04, but Max/Matthew conflict remains |
| D3-H08 | Blake, post-sales presenter; self-introduction | [C15](transcripts/15-post-sales-team-and-meeting-demo.md), 03:57:15.640 within 03:57:14.104-04:01:06.008 | Customer roles in her demo are not additional real participants |
| D3-H09 | Dan Hill, introduced by host and self-identifying with Stripe Link | [C22](transcripts/22-recap-stripe-link-and-sponsored-cards.md), 05:31:18.776-05:31:49.008 | Affiliation is self-reported, not externally checked |
| D3-H10 | Josh Kim, marketing presenter; self-introduction | [C25](transcripts/25-marketing-workshop-research-and-positioning.md), 06:00:44.248-06:00:56.272 | An audience address rendered John is not sufficient to rename him |
| D3-H11 | Eric, closing-build guest; self-introduction | [C28](transcripts/28-eric-joins-voice-prs-and-sharing.md), 06:43:11.384-06:43:32.380 | No surname inferred; employment/history statements are self-report |
| D3-HU | Unresolved attendees, callers, production interjections, montage voices and inseparable host turns | Throughout; exact groups in the [index](transcripts/README.md) and coverage ledger | Do not merge unrelated questions or assign gender/identity from voice |

## Host bot instances and claimed authors

Owner abbreviations below mean candidate host ownership, not independently
inspected account identity. Entity descriptions inherit the cited chapter's
ASR-only status.

| ID | Label / role / owner | Evidence and qualifications |
| --- | --- | --- |
| D3-B-PLAY-R | Play, Roshan's playtester | [C01](transcripts/01-opening-and-overnight-rework.md), 00:15:50.648-00:16:34.136; checks game behavior after green CI are reported |
| D3-B-STEVE-L | Steve, Lauren's chief | [C08](transcripts/08-feedback-intake-and-first-bug-triage.md), 02:10:39.096-02:13:12.952, explicit around 02:11:14.008; [C31](transcripts/31-final-build-check-in-and-unfinished-ads.md), 07:34:08.408-07:34:32.432 recap request |
| D3-B-STEVE-OTHER | Another host's chief, also Steve | [C01](transcripts/01-opening-and-overnight-rework.md), 00:26:25.944-00:28:38.328; owner unresolved, Steven only suggested |
| D3-B-CUPCAKE-ENG | Displayed Cupcake engineering label | [C01](transcripts/01-opening-and-overnight-rework.md), 00:26:25.944-00:28:38.328; do not merge with every later Cupcake-named bot |
| D3-B-DATA-R | Roshan's data scientist, name not established | [C07](transcripts/07-launch-metrics-and-matchmaking-doubts.md), 01:57:08.312-02:06:51.224; [C28](transcripts/28-eric-joins-voice-prs-and-sharing.md), 06:44:56.920-06:48:02.872; human reads metrics |
| D3-B-CRIT-R | Roshan's game-design bot | [C07](transcripts/07-launch-metrics-and-matchmaking-doubts.md), 02:06:51.224-02:08:46.424; design critique is claimed output, not a verified mechanic |
| D3-B-ENG-R | Roshan's initially unnamed founding engineer | [C07](transcripts/07-launch-metrics-and-matchmaking-doubts.md), 02:08:10.328-02:08:44.240 investigation-only request; probable relation to Bake, preserved as earlier unresolved identity |
| D3-B-BAKE-R | Bake, explicitly Roshan's founding engineer later; possible Cupcake Bug Fixes display label | [C28](transcripts/28-eric-joins-voice-prs-and-sharing.md), 06:48:36.312-06:49:26.224; [C29](transcripts/29-engineering-rigor-and-new-game-bugs.md), 07:06:23.128-07:07:38.416; probable alias of ENG-R, not proven unique instance |
| D3-B-EGG-L | Dr. Egg, Lauren's bot-creation/coaching bot | [C09](transcripts/09-expanding-the-repair-loop.md), 02:25:55.128-02:30:08.248; [C33](transcripts/33-closing-metrics-outage-and-failed-sponsorship-test.md), 07:53:50.168-07:54:39.548; garbled Dr. Aang variant is not a new identity |
| D3-B-CRUMBLE-L | Crumble, Lauren's new feedback triage bot | [C09](transcripts/09-expanding-the-repair-loop.md), 02:26:46.104-02:30:08.248; name and role from creation narration |
| D3-B-CHROME-L | Chrome/Crumb, probable playtester | [C09](transcripts/09-expanding-the-repair-loop.md), 02:26:17.592-02:27:23.384; spelling unresolved, not silently merged with Crumble |
| D3-B-TATER-L | Tater-like engineering label | [C09](transcripts/09-expanding-the-repair-loop.md), around 02:27:51.896 in 02:27:23.384-02:30:08.248; fragmentary name |
| D3-B-HASHBROWN-L | Hashbrown, verifier in Lauren's triage flow | [C09](transcripts/09-expanding-the-repair-loop.md), 02:29:26.872-02:30:08.248; verification role requested/reported, not audited |
| D3-B-VINCENT-R | Roshan-created growth idea logger named after guest Vincent | [C11](transcripts/11-vincent-growth-ideas.md), 02:47:40.216-02:48:48.120; probable logger for sponsored-card idea in [C22](transcripts/22-recap-stripe-link-and-sponsored-cards.md), 05:40:17.432-05:40:50.544 |
| D3-B-VINCENT-CHIEF | Vincent the human guest's own main bot; no secure bot name | [C12](transcripts/12-vincent-bot-onboarding-and-promotions.md), 03:10:31.672-03:11:15.448; distinct ownership from VINCENT-R |
| D3-B-CEREBRO-R | Roshan's installed audience-research instance | [C13](transcripts/13-marketing-ops-guest-and-cerebro.md), 03:36:12.408-03:36:52.568; results in [C14](transcripts/14-advertiser-personas-and-unconnected-prospecting.md), 03:36:52.568-03:55:28.056 |
| D3-B-VOICE-FEEDBACK | xAI phone-feedback agent built by probable Matt | [C20](transcripts/20-phone-feedback-and-secret-handling.md), 05:11:06.392-05:13:31.192; caller, generated acknowledgement and human Slack narrator separate |
| D3-B-GRIND-L | Grind / cheater bot, probably Lauren's player | [C28](transcripts/28-eric-joins-voice-prs-and-sharing.md), 06:53:59.192-06:54:09.424; [C31](transcripts/31-final-build-check-in-and-unfinished-ads.md), 07:34:41.624-07:35:14.288 reports score decline |
| D3-B-GRIND-M | Matt's separate grind bot | [C30](transcripts/30-broken-ad-auction-and-feedback-projects.md), 07:14:08.248-07:14:20.208; explicitly behind Lauren's setup |
| D3-B-FEEDBACK-M | Matt's Cupcake feedback fixer | [C30](transcripts/30-broken-ad-auction-and-feedback-projects.md), 07:11:13.944-07:12:18.104; [C31](transcripts/31-final-build-check-in-and-unfinished-ads.md), 07:30:58.296-07:32:14.288; distinct from Lauren's triage system |
| D3-B-LOOP-M | Matt's engineering loop bot | [C30](transcripts/30-broken-ad-auction-and-feedback-projects.md), 07:13:50.040-07:15:29.040; personal workflow, not necessarily the feedback fixer |

## RevOps and post-sales examples

These are presenter-owned example systems, not the hosts' live company.

| ID | Claimed role | Evidence |
| --- | --- | --- |
| D3-B-OP1 | RevOps chief coordinating task intake | [C02](transcripts/02-revops-task-routing.md), 00:37:42.264-00:44:02.936; H04 narrates |
| D3-B-FISHER | Inbox/calendar/chat intake | [C02](transcripts/02-revops-task-routing.md), 00:37:42.264-00:42:28.152 |
| D3-B-JUNO | Requirements and corner-case thought partner | [C02](transcripts/02-revops-task-routing.md), 00:37:42.264-00:39:22.072; [C03](transcripts/03-lead-review-app-and-guardrails.md), 00:46:10.616-00:49:31.000 |
| D3-B-OND | Engineering/systems bot; ASR owned/own | [C02](transcripts/02-revops-task-routing.md), 00:37:42.264-00:39:22.072; music-device spelling unresolved |
| D3-B-TERRITORY | Territory-planning specialist | [C02](transcripts/02-revops-task-routing.md), 00:42:28.152-00:44:02.936; draft resolution, not finalized dispute |
| D3-B-GUS | Blake's chief, coordinating specialists | [C15](transcripts/15-post-sales-team-and-meeting-demo.md), 04:04:09.240-04:07:25.944; subsequent output read by Blake |
| D3-B-FRANKIE | Follow-up specialist | Same C15 interval; distinct from Franny |
| D3-B-WALLY | Writing/style specialist | Same C15 interval; draft-versus-sent learning in [C17](transcripts/17-post-sales-setup-cost-and-human-work.md), 04:25:11.448-04:25:33.904 |
| D3-B-TRUDY | Sourced product knowledge | Same C15 interval; source accuracy not inspected |
| D3-B-SCOUT | Internal-update radar; sometimes direct notifications | Same C15 interval; exception to one-contact pattern |
| D3-B-FRANNY | Forms specialist | [C15](transcripts/15-post-sales-team-and-meeting-demo.md), 04:07:25.944-04:08:51.480; [C16](transcripts/16-post-sales-drafts-forms-and-staff-meeting.md), 04:13:31.992-04:21:39.960 |
| D3-B-HARBOR | Harbor account-context bot | [C16](transcripts/16-post-sales-drafts-forms-and-staff-meeting.md), 04:10:04.216-04:21:39.960; workshop account, not verified customer |
| D3-B-NORTHWIND | Northwind account-context bot | [C16](transcripts/16-post-sales-drafts-forms-and-staff-meeting.md), 04:13:31.992-04:20:30.392 |
| D3-B-BRIGHTLINE | Brightline account-context bot | [C16](transcripts/16-post-sales-drafts-forms-and-staff-meeting.md), 04:17:51.000-04:20:30.392 |

## Marketing workshop team

All six are Josh's claimed specialist instances in the X Air example, introduced
in [C25](transcripts/25-marketing-workshop-research-and-positioning.md),
06:07:22.936-06:08:46.104. Josh is the human reader/narrator of their outputs.

| ID | Role and observed-in-ASR task | Further evidence |
| --- | --- | --- |
| D3-B-MKT-RESEARCH | Competitive/site research | C25, 06:08:46.104-06:11:36.440 |
| D3-B-MKT-PRODUCT | Positioning, document revisions and ad-copy variants | C25, 06:11:36.440-06:15:53.272 |
| D3-B-MKT-WEB | Landing-page PR and reported deployment | [C26](transcripts/26-marketing-campaign-build-and-automation.md), 06:15:53.272-06:28:14.296 |
| D3-B-MKT-PERFORMANCE | Current ad-campaign shell, not demonstrated paid delivery | C26, 06:15:53.272-06:22:05.496 |
| D3-B-MKT-ANALYST | Analysis of an earlier campaign, not current-draft results | C26, 06:22:05.496-06:24:15.032 |
| D3-B-MKT-PM | Requested coordinator for three new campaigns | C26, 06:24:15.032-06:27:30.296; queued, not all completed |

## Templates, cards and organizational contexts

| ID or category | Meaning and boundary | Evidence |
| --- | --- | --- |
| D3-O-GAME | Live host project: Cupcake working name, then Thursday Arena; game studio with first auto-battler | [C01](transcripts/01-opening-and-overnight-rework.md), 00:19:30.936-00:22:49.272; [C06](transcripts/06-practice-match-and-playtest-release.md), 01:44:08.664-01:49:07.576; [C33](transcripts/33-closing-metrics-outage-and-failed-sponsorship-test.md), 07:50:12.472-end |
| D3-O-REVOPS | Stage/internal task and lead-review examples | [C02](transcripts/02-revops-task-routing.md)-[C04](transcripts/04-revops-questions-and-transition.md), 00:34:20.024-01:10:52.760; prepared fake-data lead app is not a live host-company result |
| D3-O-ENTERPRISE-VIDEO | Separate executive testimonial | [C10](transcripts/10-enterprise-video-and-break.md), 02:35:12.056-02:38:24.888; company identity unresolved |
| D3-O-FLYLO-CS | Explicit Flylo demo company for Blake's accounts | [C15](transcripts/15-post-sales-team-and-meeting-demo.md), 04:08:51.480-04:10:04.216; account/contact roles are not real customers established here |
| D3-O-XAIR | Explicit X Air airline-style demo | [C25](transcripts/25-marketing-workshop-research-and-positioning.md), 06:07:56.280-06:08:26.928; unrelated to game-studio product |
| D3-T-CEREBRO | Shared audience-research template, supplied by guest Matt | [C13](transcripts/13-marketing-ops-guest-and-cerebro.md), 03:34:50.040-03:36:52.568; separate from installed CEREBRO-R |
| Other templates | Inbot/Cooper references, game-designer share, Eric's project organizer and PlanetScale administrator | [C13](transcripts/13-marketing-ops-guest-and-cerebro.md), 03:30:00.248-03:36:52.568; [C21](transcripts/21-analytics-templates-and-ui-delivery.md), 05:21:30.104-05:27:01.688; [C22](transcripts/22-recap-stripe-link-and-sponsored-cards.md), 05:40:51.032-05:42:00.728; [C29](transcripts/29-engineering-rigor-and-new-game-bugs.md), 06:59:04.568-07:01:50.520; no unproven instance merges |
| Game-card labels | Dr. Egg, Lingxi, Office Ops Desk, Dial, Writing, Nightly Audit Engineer and other marketplace-derived cards | [C06](transcripts/06-practice-match-and-playtest-release.md), 01:36:06.488-01:46:18.392; [C29](transcripts/29-engineering-rigor-and-new-game-bugs.md), 07:01:50.520-07:05:37.784; not proof those humans/bots participated operationally |
| Workshop contacts | Maya, Priya, Alex and account-role labels | [C16](transcripts/16-post-sales-drafts-forms-and-staff-meeting.md), 04:11:23.544-04:13:31.992; names in illustrative output, no contact details retained |
| External agent | Attendee's Ariel, spelling inconsistent including AIREAL/AREAL | [C27](transcripts/27-marketing-questions-and-permission-limits.md), 06:36:20.440-06:38:17.360; OpenClaw example, not a confirmed Grokbot instance |
| Unnamed temporary bots | Cloud repair agents, sound/3D bots, Dan's shopping/finance/projects, new rules-learning bot | Roles remain unnamed in relevant chapters; do not manufacture unique IDs from repeated generic roles |

## Mandatory non-merges and remaining checks

- H04/H07: probable relationship, unresolved Max/Matthew conflict. Host Matt H01
  is explicitly distinct; see C21, 05:24:26.904-05:24:49.840.
- Bake/ENG-R/Cupcake engineering/feedback fixer: owner and role continuity alone
  does not prove identical instances; earlier IDs stay stable.
- Vincent human, Roshan's Vincent logger and Vincent's own chief remain separate.
- Frankie and Franny remain separate; game-card Dr. Egg is not automatically the
  operational Dr. Egg instance.
- No human Steve, human Jenny or bot Jenny participation is established by this
  pass. Their appearance in general editorial guidance is not event evidence.
- All employers, names, consequential attributions and bot ownership await the
  [audio review queue](review-queue.md). No identification from Day 2, captions,
  external profiles or inferred voice matching was used.
