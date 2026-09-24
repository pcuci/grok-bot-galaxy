# D1-C21: Venue criteria, permits and an art pivot

## Source and review state

- Interval: [05:30:03.512, 05:54:10.488).
- Source: X `1AxRnZbVpjaxl`; [inputs/hashes](README.md), [sources](../sources.md), [entities](../entities.md).
- **ASR-based review draft**, nonverbatim grouped conversation; not audio-verified. No quotations.
- Context: Hosts' live build (Ship by Thursday demo company); guest remarks within it are advice, not decisions.

## Input intervals and identity

Source/checkpoint hashes are in [the index](README.md). These are exact
silence-preserving PCM intervals, not audio-verified word or speaker boundaries.

| Part and hashes | Part-local interval | Source interval |
| --- | --- | --- |
| [part-12](README.md#part-12) | 00:00:03.512-00:24:10.488 | 05:30:03.512-05:54:10.488 |

## Edited conversation

### 05:30:03.512-05:32:16.536 | A very prototype prototype and a manual-calls plan

**Speakers:** Lauren D1-H02; Matt D1-H01; Roshan D1-H03. **Type:** status and planning.

Lauren says the prototype is vanilla HTML and JavaScript, fine for now, and they should keep iterating. Asked where they will be by the next talk, Matt says he may try manual calls off camera to learn how hard booking is; Lauren says her prototype is being built and can be iterated on. A host plans a bare-bones marketing plan and guerrilla campaign and may hire people to put up flyers; another says he knows people who could help. Experiential ideas and merch go in a Notion marketing section.

### 05:32:16.536-05:34:37.432 | Venue criteria from lived knowledge, and permit timing

**Speakers:** Lauren asking; Matt answering. **Type:** Q&A and reported research.

Asked what matters when finding venues, Matt says an event is about making people feel a certain way; start with guests, perhaps 100, a space that fits them and lets them control the environment. He names two local event spaces he knows and says he would pattern-match from them, perhaps bootstrapping a bot skill. Budget has not been discussed and needs research. He reports that his host-finder bot D1-B-HOSTFINDER-M is putting research in Notion and flagging permits: street closures and alcohol could require several weeks to a month, so a month out is tight and six weeks might be safer; he reads a public venue's multi-week review times. Neighborhood details are omitted.

### 05:34:37.432-05:36:51.640 | Knowledge manager switches to polling; host-finder guidance

**Speakers:** Lauren proposing; Matt dictating. **To:** knowledge-base manager D1-B-KBM-M; host finder. **Type:** proposal and instruction.

Lauren realizes the context they share aloud should reach engineering and suggests recording it into company Notion. Matt tells his knowledge-base manager to **ping active bots every five minutes**, extract the most important details and put them in Notion, while worrying about Notion spam; a host compares it to a git log. **This reverses the passive configuration in [C20](20-knowledge-manager-stack-flyer-copy-and-merch.md).** Matt tells the host finder to start from known high-quality places, avoid government-run facilities because of lead time, and prefer venues with a caterer or alcohol license so a vendor can handle licensing.

### 05:36:51.640-05:39:34.200 | What each host would bring, and a menu bot

**Speakers:** Roshan; Matt; Lauren. **Type:** ideas and bot creation.

Asked what he would bring, Matt says good food and a limited menu; he wants creative freedom for the chef but maybe designed cocktails or menu elements. A host says he recorded the discussion for a bot. They spin up a menu bot D1-B-MENU-U. A host who jokes that he is now the geo-scraper guy, probably Roshan, asks bots to search sites such as review platforms for top-rated dishes for inspiration.

### 05:39:34.200-05:42:48.056 | From dining toward an art exhibition; Roshan leaves

**Speakers:** Matt raising the question; Roshan and Lauren. **Type:** proposal and tentative pivot.

Matt asks whether they are set on a restaurant; a generic pop-up is possible. Food involves chefs, licensing and complexity. A host proposes an art exhibition: crowdsource art, have bots review submissions, sell more tickets and use any large space. Matt says he likes the art exhibition, then asks whether it means paying many artists; others suggest an exhibition space plus community submissions, perhaps art about Grok Bot avatars, and an interactive digital gallery before visiting in person. They think insurance and a venue may suffice, or friends in events can advise. Roshan says he must leave because he is presenting the next talk, Grok Bot for PMs.

### 05:42:48.056-05:49:47.864 | Communicating the change, PR backlog and venue data

**Speakers:** Matt; Lauren. **To:** Steve D1-B-STEVE-L; host finder. **Type:** instructions, narrated bot output and status.

After Roshan leaves, Matt says flexible warehouse-like spaces fit an exhibition. Lauren, probably, tells her bot Steve about the change of plan and says she will work on the venue finder, while Matt works on the lander UI. Lauren reviews PRs, including a verification-skill PR and several numbered prototype PRs, and is surprised there are already 13 or more because prototype requests opened many. A knowledge-base bot posts to Slack and a marketing channel includes a top-50 flyer-corner list. Matt reads or writes a message that they are **considering** an art pop-up rather than a dining experience and asks to optimize for a large warehouse space. Lauren proposes using a maps API for search, adding filters such as venue size, and entering call details so the tool improves. She says her engineer and verifier bots are busy but PRs lack videos and screenshots, so Steve should drive them to completion. Matt says Resend will send a waitlist confirmation email from a company address once set up.

### 05:49:47.864-05:54:10.488 | Challenge reminder, stuck PRs and pre-session fragments

**Speakers:** Matt; Lauren; production cues. **Type:** housekeeping and status.

With a few minutes left, Matt restates the template challenge and says the product-manager session is next with Roshan among the presenters. Lauren groups agent PRs by status and finds some stuck. Remaining ASR consists of short unintelligible fragments before the session starts; it is not reconstructed.

## Editorial changes and unresolved evidence

The art pivot is described with considering in the recognized message and is revisited in [C24](24-eric-narrows-audience-to-tech-brand-merch.md); it is not treated as final. PR numbers are ASR-uncertain.
