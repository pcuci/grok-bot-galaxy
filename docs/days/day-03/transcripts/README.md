# Day 3 transcript index and timeline

Status: **ASR-based review draft**, nonverbatim grouped conversation. All 16
parts were read in full. No audio listening, verified quotation or independently
verified external outcome is claimed. [Day overview](../README.md),
[entities](../entities.md), [sources](../sources.md),
[gaps](../gap-ledger.md), [review queue](../review-queue.md).

## Time and identity

Source: X `1YGNrbXEeazGw`. Source SHA-256:
`f121e311238c48e0b6cc44ddc52726cbbd0b4bfa0fa6705c849b1c57ef56a558`.
Checkpoint identity:
`0d847ac4af716e652da03e4cc0a654cbe2a187f6b4697960f6a0d1c20571f5f0`.

Half-open intervals cover 459237717 samples at 16 kHz, ending exactly at
07:58:22.3573125. Times are normalized recording coordinates after four DTS
and two discontinuity corrections, not broadcast wall clock or word alignment.
Part-local time plus `(part_number - 1) * 1800` gives recording time.

Each chapter has contributing part-local/source ranges; hashes below identify
all three raw exports and the PCM part. The [machine ledger](../coverage-ledger.json)
records every region, timed group, crossing and gap. Routing is not a semantic
completeness claim. All consequential claims and boundaries await audio review.

## Chronological chapter map

| ID | Source interval | Edited conversation | Parts |
| --- | --- | --- | --- |
| D3-C01 | 00:00:00.000-00:34:20.024 | [Opening and overnight rework](01-opening-and-overnight-rework.md) | 1, 2 |
| D3-C02 | 00:34:20.024-00:44:02.936 | [RevOps task routing](02-revops-task-routing.md) | 2 |
| D3-C03 | 00:44:02.936-00:56:23.832 | [Lead-review app and guardrails](03-lead-review-app-and-guardrails.md) | 2 |
| D3-C04 | 00:56:23.832-01:21:04.184 | [RevOps questions and transition](04-revops-questions-and-transition.md) | 2, 3 |
| D3-C05 | 01:21:04.184-01:36:06.488 | [Production setup and launch checklist](05-production-setup-and-launch-checklist.md) | 3, 4 |
| D3-C06 | 01:36:06.488-01:49:07.576 | [Practice match and playtest release](06-practice-match-and-playtest-release.md) | 4 |
| D3-C07 | 01:49:07.576-02:08:46.424 | [Launch metrics and matchmaking doubts](07-launch-metrics-and-matchmaking-doubts.md) | 4, 5 |
| D3-C08 | 02:08:46.424-02:25:55.128 | [Feedback intake and first bug triage](08-feedback-intake-and-first-bug-triage.md) | 5 |
| D3-C09 | 02:25:55.128-02:35:12.056 | [Expanding the repair loop](09-expanding-the-repair-loop.md) | 5, 6 |
| D3-C10 | 02:35:12.056-02:44:13.144 | [Enterprise video and break](10-enterprise-video-and-break.md) | 6 |
| D3-C11 | 02:44:13.144-03:07:44.248 | [Vincent's growth ideas](11-vincent-growth-ideas.md) | 6, 7 |
| D3-C12 | 03:07:44.248-03:23:06.520 | [Vincent's bot onboarding and promotions](12-vincent-bot-onboarding-and-promotions.md) | 7 |
| D3-C13 | 03:23:06.520-03:36:52.568 | [Marketing-ops guest and Cerebro](13-marketing-ops-guest-and-cerebro.md) | 7, 8 |
| D3-C14 | 03:36:52.568-03:57:14.104 | [Advertiser personas and unconnected prospecting](14-advertiser-personas-and-unconnected-prospecting.md) | 8 |
| D3-C15 | 03:57:14.104-04:10:04.216 | [Post-sales team and meeting demo](15-post-sales-team-and-meeting-demo.md) | 8, 9 |
| D3-C16 | 04:10:04.216-04:21:39.960 | [Post-sales drafts, forms and staff meeting](16-post-sales-drafts-forms-and-staff-meeting.md) | 9 |
| D3-C17 | 04:21:39.960-04:33:50.040 | [Post-sales setup, cost and human work](17-post-sales-setup-cost-and-human-work.md) | 9, 10 |
| D3-C18 | 04:33:50.040-04:53:20.376 | [Post-sales verification and migration questions](18-post-sales-verification-and-migration-questions.md) | 10 |
| D3-C19 | 04:53:20.376-05:09:48.792 | [Launch data and mobile playthrough](19-launch-data-and-mobile-playthrough.md) | 10, 11 |
| D3-C20 | 05:09:48.792-05:16:48.888 | [Phone feedback and secret handling](20-phone-feedback-and-secret-handling.md) | 11 |
| D3-C21 | 05:16:48.888-05:29:23.960 | [Analytics, templates and UI delivery](21-analytics-templates-and-ui-delivery.md) | 11 |
| D3-C22 | 05:29:23.960-05:42:00.728 | [Recap, Stripe Link and sponsored cards](22-recap-stripe-link-and-sponsored-cards.md) | 11, 12 |
| D3-C23 | 05:42:00.728-05:50:54.168 | [Voice, subscriptions and a first-dollar goal](23-voice-subscriptions-and-first-dollar-goal.md) | 12 |
| D3-C24 | 05:50:54.168-06:00:41.176 | [Link demo limits and personal use cases](24-link-demo-limits-and-personal-use-cases.md) | 12, 13 |
| D3-C25 | 06:00:41.176-06:15:53.272 | [Marketing workshop research and positioning](25-marketing-workshop-research-and-positioning.md) | 13 |
| D3-C26 | 06:15:53.272-06:28:14.296 | [Marketing campaign build and automation](26-marketing-campaign-build-and-automation.md) | 13 |
| D3-C27 | 06:28:14.296-06:43:09.784 | [Marketing questions and permission limits](27-marketing-questions-and-permission-limits.md) | 13, 14 |
| D3-C28 | 06:43:09.784-06:54:34.424 | [Eric joins, voice PRs and sharing](28-eric-joins-voice-prs-and-sharing.md) | 14 |
| D3-C29 | 06:54:34.424-07:08:33.048 | [Engineering rigor and new game bugs](29-engineering-rigor-and-new-game-bugs.md) | 14, 15 |
| D3-C30 | 07:08:33.048-07:28:29.016 | [Broken ad auction and feedback projects](30-broken-ad-auction-and-feedback-projects.md) | 15 |
| D3-C31 | 07:28:29.016-07:41:04.120 | [Final build check-in and unfinished ads](31-final-build-check-in-and-unfinished-ads.md) | 15, 16 |
| D3-C32 | 07:41:04.120-07:50:12.472 | [Host reflections on distribution and restraint](32-host-reflections-on-distribution-and-restraint.md) | 16 |
| D3-C33 | 07:50:12.472-07:58:22.3573125 | [Closing metrics, outage and failed sponsorship test](33-closing-metrics-outage-and-failed-sponsorship-test.md) | 16 |

## Part hashes

Paths below are relative to `.data/day-03/`. Raw bytes remain restricted/local;
this index does not redistribute them. Full inventory: [input hashes](../input-inventory.json).

### Part-01

Source interval: 00:00:00.000-00:30:00.000.

| Input | SHA-256 |
| --- | --- |
| `parts/part-01.wav` | `31c975835236eb2fc8ff09eaa1ed471b27b29efbcb6efb30a988f1f993108822` |
| `transcripts/part-01.json` | `0d597b207844345d11cc5e10fbce8d29b26f3f5a4586c5cfee514d34798d2530` |
| `transcripts/part-01.txt` | `c2188647e3c58e3f1a54fff898cd886b921d777567b0021c4bb44e5e55e640ef` |
| `transcripts/part-01.srt` | `0d6669655d5972ac13368b6ff87233210889b20b0776579b6030c40d9636b43c` |

### Part-02

Source interval: 00:30:00.000-01:00:00.000.

| Input | SHA-256 |
| --- | --- |
| `parts/part-02.wav` | `604000ab51c0b5365ae69b94e0e93d9982a8f87e7492efb635d2c02b8d414e82` |
| `transcripts/part-02.json` | `7b699e883bebcfc1aad1d549dbfe355f9864f9c0f59311d782fadb869a98c7c0` |
| `transcripts/part-02.txt` | `e94bb07239452a87dffea59caf8943cc432f9f8a5068e623ae117d411a93d32e` |
| `transcripts/part-02.srt` | `8d3df877414659291fc0ffad4792ae14ed395f22e834b57bb56e396d48ea566e` |

### Part-03

Source interval: 01:00:00.000-01:30:00.000.

| Input | SHA-256 |
| --- | --- |
| `parts/part-03.wav` | `1192c660b8869cd164d4da89f2adf86f1beda588a8a82e662e0373c3463de52a` |
| `transcripts/part-03.json` | `0c985ee6d0bb615d066da8e0892ec715e416f7833f49871cd04e44b7cddbc11a` |
| `transcripts/part-03.txt` | `d167d900004971abbb9aa55f0c899cbb4c2f0459ed3e141ea397bf802646e71c` |
| `transcripts/part-03.srt` | `d66a6684468ce11e65a985373cf0f9a2d51d51bcdb90b2d641d105d28d932fe0` |

### Part-04

Source interval: 01:30:00.000-02:00:00.000.

| Input | SHA-256 |
| --- | --- |
| `parts/part-04.wav` | `28ab305de735912cdd88a09db6477dfbbaef4bc8532d471c5d1f518f2877b068` |
| `transcripts/part-04.json` | `67aa8ee8e4f062f5a773448ecc15ec30fd66393aa30979351dfe5997be3662f2` |
| `transcripts/part-04.txt` | `a886d47f5fffd948972dfabd69537ac14a34fe045d64a6de0139ddf5c6000694` |
| `transcripts/part-04.srt` | `42f60b83d4305362b969530ef2dc649bb1f6cd07768e5c1aaea00c3899fdbf0f` |

### Part-05

Source interval: 02:00:00.000-02:30:00.000.

| Input | SHA-256 |
| --- | --- |
| `parts/part-05.wav` | `93ee292491669cc2c71672e0ecbf57ea47c3bf42bf5feecc0dee0f79923c497f` |
| `transcripts/part-05.json` | `659175b752ca07793db87bccd3ed2e2eef4b91f86197a8d479d7005c10858ca6` |
| `transcripts/part-05.txt` | `d934d5c37a788910d0f5d9d91ee989880b8d1d752509c9ff1b59b83b3cc31325` |
| `transcripts/part-05.srt` | `61697b11b6b12ea26fcf454117b83f37c5b2c8f0f6c7e84a218c29d2c4dcd41d` |

### Part-06

Source interval: 02:30:00.000-03:00:00.000.

| Input | SHA-256 |
| --- | --- |
| `parts/part-06.wav` | `00dda9cbe0f31433dd29c0589205abc68faa8bf89cce0e61e649c9a985c5298b` |
| `transcripts/part-06.json` | `47ce55913e42316d6c871cd028b1e5c3e99c4b81bc97274746a8bdd609e46f70` |
| `transcripts/part-06.txt` | `9d1be16f81cf96b044e2bf78afe4d1d50b026680e07a74a4080a5c46f2baf385` |
| `transcripts/part-06.srt` | `8f94df273a35c1c8830608873927b9a2dab56f9a565af33bc0cc9b455eb9efc0` |

### Part-07

Source interval: 03:00:00.000-03:30:00.000.

| Input | SHA-256 |
| --- | --- |
| `parts/part-07.wav` | `161bbaf3e3d643570e164cbf44b4724bfd77c05473c6bd315788297cbeef5264` |
| `transcripts/part-07.json` | `35dac016251f84acf64c419a493ce3427cde3b7745026fa6f50255074adb98bc` |
| `transcripts/part-07.txt` | `916dfbe869ff02db7c7d59ded19e1b9cf6e611eb65b20eea9ac853632b6d1604` |
| `transcripts/part-07.srt` | `ea8d7123651af698db577f2d7eee0910d438775ec0b3e50cfa85d1e7b77787bd` |

### Part-08

Source interval: 03:30:00.000-04:00:00.000.

| Input | SHA-256 |
| --- | --- |
| `parts/part-08.wav` | `86414db2e8ead91521cb298d7e62f2740cda65c90bbaf198118429af1f3dc2db` |
| `transcripts/part-08.json` | `04d51a58706e9e6e0a71a5c731625ced386ce142896c0957ea2e62ed715376a3` |
| `transcripts/part-08.txt` | `5a6dab8ca5deb1a22201e634020fa32247874646c2e347aed4ab630490514f3b` |
| `transcripts/part-08.srt` | `e05a268ca18f80debc42b287d91bf1380a419fbbd6279519fec57f341ce67630` |

### Part-09

Source interval: 04:00:00.000-04:30:00.000.

| Input | SHA-256 |
| --- | --- |
| `parts/part-09.wav` | `e2d4b45a65151e1553d3344697e2063ec0154d11f9864e01b7589c28eb440eb1` |
| `transcripts/part-09.json` | `cea2884e7e29fad3cb0b0f9963f3e1aacaddc84f3577691404bdf5b94009776d` |
| `transcripts/part-09.txt` | `6fd4f1efbd095c570fe049e405ea858cce61f4d699e12b728ab0529f7d83f451` |
| `transcripts/part-09.srt` | `1a264001a80780276d8bf049d893c03d3081d5b4cb25287b23b66b57a27dc6eb` |

### Part-10

Source interval: 04:30:00.000-05:00:00.000.

| Input | SHA-256 |
| --- | --- |
| `parts/part-10.wav` | `069074bd88b085f8548c796432bbf7d4d757e9a0ec0a9662e625021ca95edb00` |
| `transcripts/part-10.json` | `d08d9b6882d4a5a32e1afe2b45e534b15bcf26b1b91ec79fc89f6c12fa723a99` |
| `transcripts/part-10.txt` | `280ba37a94fc788115a49167652e9f774d43e37865fa79e73d259b559fbd7b15` |
| `transcripts/part-10.srt` | `5cd1a24e18729ed432d95895495b32311fb6e3b6db5ba9cde97e4d339f38f931` |

### Part-11

Source interval: 05:00:00.000-05:30:00.000.

| Input | SHA-256 |
| --- | --- |
| `parts/part-11.wav` | `2be831270c2e06df8ec550f8bba0ccab444ab7a2f84ef20b0edab52901658d7e` |
| `transcripts/part-11.json` | `d37ad3283edbed92bddce1cfa5c9fc6af0452624145b3cb7a4da4be2c65ae073` |
| `transcripts/part-11.txt` | `84d7472a245af82c010b199b0c43be83ad44925d5f0d8dca73d5fa5f928b8332` |
| `transcripts/part-11.srt` | `585e871f94e6508c915365003e26135a6e0e95e9ffdbdb6e13b9fbba4ae093dc` |

### Part-12

Source interval: 05:30:00.000-06:00:00.000.

| Input | SHA-256 |
| --- | --- |
| `parts/part-12.wav` | `b4dc51e7eceea4717cb39279a8ecafdeec73fc0b51d4d628685210b798a90b90` |
| `transcripts/part-12.json` | `f0fa78eeebff12ee8afd50423a9deae499d0cd57b3a30b10c2caf70f499e8be3` |
| `transcripts/part-12.txt` | `a5431327f0d5f419d365d8ce9b04d64709d503f510536e1da2c047c8aecee0f2` |
| `transcripts/part-12.srt` | `35b5e83a7231f22bf426297218e8d6920c195a789618b55b28e6aa1cff9687d7` |

### Part-13

Source interval: 06:00:00.000-06:30:00.000.

| Input | SHA-256 |
| --- | --- |
| `parts/part-13.wav` | `9dfc22e17db83fff5bb10ff038a60c6a87944c6e728c8a5613ca2ef85ef0923a` |
| `transcripts/part-13.json` | `22d84d87fdb7e723db40efaad6b41e45dc4b0790e9802790ec368b1ea939ed6a` |
| `transcripts/part-13.txt` | `4a7afddaa80d843a6fe5e15d50a28b0409689ed1d325dc4a2fe91fa0db4e50b9` |
| `transcripts/part-13.srt` | `075a29d160c8bdd3feb6bc31365040f5def6441974b34de3da61f22391716b85` |

### Part-14

Source interval: 06:30:00.000-07:00:00.000.

| Input | SHA-256 |
| --- | --- |
| `parts/part-14.wav` | `dd7956a9c8c6edbedff1d814331b252a01f6c2aea685c77bccb5ac786bf9852e` |
| `transcripts/part-14.json` | `adfb4c0d52e286c97e4a735cb777f26912bc9fa9ed5374e676c2df9ceb71117f` |
| `transcripts/part-14.txt` | `9d6661c1801d58e22b5e73e1334d031fefac09eb491080cfd30c8660efff2421` |
| `transcripts/part-14.srt` | `744299d93b0f000c6392138e2f6fc984d5f9b01e11047b2d9cf05004100d1809` |

### Part-15

Source interval: 07:00:00.000-07:30:00.000.

| Input | SHA-256 |
| --- | --- |
| `parts/part-15.wav` | `ec8e3c3378a86297ea9ea0f363f22047b70681ceeca323d643e54bdc8aa54814` |
| `transcripts/part-15.json` | `4293b2a73328735f82235b4054a8f2eab8c2ea6e331f6363416320751177835c` |
| `transcripts/part-15.txt` | `0272f97affa3fbbb8d2488f507cdc4a9ce89d4da3a127f2f5dd8680aa8190ff9` |
| `transcripts/part-15.srt` | `d0ec79852a78032bf7f0a5f1eb6b63b3507ab01f145425c71ac7e0fc6330d409` |

### Part-16

Source interval: 07:30:00.000-07:58:22.3573125.

| Input | SHA-256 |
| --- | --- |
| `parts/part-16.wav` | `d3ea1eaaff9276f1e9a1bd98afd3cf3ba5d6d9b373d3e439b393f232595f4759` |
| `transcripts/part-16.json` | `24bf91c0a2caea73a2c95721ac8fad6dace883b60b1195cffe285e23eebe3240` |
| `transcripts/part-16.txt` | `262db2baab9c55d79891c584f91eeacce949872dbaf0689112b28a6cae8539db` |
| `transcripts/part-16.srt` | `79c1e8e051a3366c2e437b8265b40cb4709212d29fbb961811fa9a98090d6945` |

## Coverage and handoff

The chapters retain the live game build separately from RevOps, enterprise,
post-sales and X Air examples. Gaps remain on the timeline, and closing failures
remain alongside celebratory reports. No decisions, progress or lessons
synthesis is created here. See [validation](../validation.json) for exact local
checks and [editorial changes](../editorial-change-log.md) for omissions and
consequential interpretation choices.
