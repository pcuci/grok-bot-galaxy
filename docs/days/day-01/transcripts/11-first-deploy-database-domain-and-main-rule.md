# D1-C11: First deploy, database, domain and the main-branch rule

## Source and review state

- Interval: [02:36:10.360, 02:55:28.344).
- Source: X `1AxRnZbVpjaxl`; [inputs/hashes](README.md), [sources](../sources.md), [entities](../entities.md).
- **ASR-based review draft**, nonverbatim grouped conversation; not audio-verified. No quotations.
- Context: Hosts' live build (Ship by Thursday demo company); guest remarks within it are advice, not decisions.

## Input intervals and identity

Source/checkpoint hashes are in [the index](README.md). These are exact
silence-preserving PCM intervals, not audio-verified word or speaker boundaries.

| Part and hashes | Part-local interval | Source interval |
| --- | --- | --- |
| [part-06](README.md#part-06) | 00:06:10.360-00:25:28.344 | 02:36:10.360-02:55:28.344 |

## Edited conversation

### 02:36:10.360-02:39:00.696 | Connecting Vercel, Matt's ops bots and a hidden screen

**Speakers:** Lauren D1-H02; Matt D1-H01; Roshan D1-H03. **Type:** setup narration.

Lauren inspects the repository: a single index HTML file with inline styles, which she calls scrappy but more than they had. She starts connecting Vercel to the repository, authorizing GitHub and signing up for an account. Meanwhile Matt says he is creating an ops bot D1-B-OPS-M for company setup work and a creative director D1-B-CREATIVE-M for naming and high-level details. Roshan resends a pending invitation. Lauren asks production to hide her screen briefly; the stream is cut and a cohost streams instead. The reason is not stated; no hidden content is inferred.

### 02:39:00.696-02:43:50.040 | First deploy, where sign-ups go, and PlanetScale

**Speakers:** Lauren, Roshan, Matt. **To:** each other; Steve D1-B-STEVE-L. **Type:** reported outcome, discussion and instruction.

Lauren connects Notion. A host reports deployments running on main after pushes, naming a pop-up project URL in garbled ASR; they note it is only an HTML page that does not store anything yet. After discussing Google Sheets, Notion or a flat file, Lauren asks Steve to connect the landing page to a Notion database for sign-ups. Roshan then proposes integrating PlanetScale immediately to avoid ripping out a temporary store later; Lauren agrees and asks for PlanetScale Postgres, trimming nice-to-have features. They say PlanetScale accounts are provided by that company's team.

Roshan recaps for new viewers: Matt is building a company playbook and go-to-market motion; there is an early HTML landing-page prototype; the direction is a pop-up platform plus possibly their own pop-up; Lauren is wiring integration and the database.

### 02:43:50.040-02:49:44.152 | Domain brainstorming, cancelled guest and cloud agents

**Speakers:** Matt, Roshan, Lauren. **To:** chat; Steve; Tater D1-B-TATER-L via Steve. **Type:** requests and explanation.

Matt says his creative director is suggesting names and asks chat for domains; a host wonders whether shipbythursday.com is available. Production reports that the next guest cannot come. Lauren tells Steve to unblock itself while credentials are pending, think about table design and dependencies, and tell Tater to use cloud agents, perhaps a project agent. She explains that Grok Bot orchestrates, while Cursor's harness is better for coding; cloud agents run in their own VMs and can test, click around and take CPU traces. She says Tater created a project, a special cloud agent for long projects, and hedges that they may not keep it. Awaiting PlanetScale credentials, she asks for local development in a cloud machine with a video or screenshot back.

### 02:49:44.152-02:52:40.336 | A purchased domain and the direct-to-main rule

**Speakers:** probable Roshan reporting the domain; Matt; Lauren. **To:** cohosts; Steve. **Type:** reported outcome and explicit workflow instruction.

A host reports that they now own a domain written in ASR as ship-by-thurs.day and that it is on Vercel. Matt wants it for a company lander, with the product on a separate domain; a working product title is still needed. Matt says he is using his Dr. Eggbot copy D1-B-EGG-M to install a Cursor team kit, skills and PStack and connect cloud agents.

Lauren reports that Steve opened a pull request, calls that a mistake, and gives a new rule: no pull requests; ship to main until someone else is added. She notes the PR is about two thousand lines and she will not read it. She then says she wants a reviewer bot in addition to Tater; production cuts to a hold screen for technical difficulties before she continues. This direct-to-main rule is later superseded by a PR-review design in [C14](14-post-break-review-factory.md) and [C17](17-review-channel-verification-and-waitlist.md).

### 02:52:40.336-02:55:28.344 | Hold screen and resumption fragments

**Speakers:** unresolved. **Type:** low-information interval.

No regions are recognized for more than two minutes, followed by short fragments. The span is not called silence and is not filled in.

## Editorial changes and unresolved evidence

The purchased domain and main deployments are speaker reports; registrar, DNS and deployment records were not inspected. The exact instruction wording around someone else joining needs audio review.
