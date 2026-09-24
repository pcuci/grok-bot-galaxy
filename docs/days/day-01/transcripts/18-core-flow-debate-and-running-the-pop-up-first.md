# D1-C18: Core-flow debate and running the pop-up first

## Source and review state

- Interval: [04:55:12.056, 05:07:38.168).
- Source: X `1AxRnZbVpjaxl`; [inputs/hashes](README.md), [sources](../sources.md), [entities](../entities.md).
- **ASR-based review draft**, nonverbatim grouped conversation; not audio-verified. No quotations.
- Context: Hosts' live build (Ship by Thursday demo company); guest remarks within it are advice, not decisions.

## Input intervals and identity

Source/checkpoint hashes are in [the index](README.md). These are exact
silence-preserving PCM intervals, not audio-verified word or speaker boundaries.

| Part and hashes | Part-local interval | Source interval |
| --- | --- | --- |
| [part-10](README.md#part-10) | 00:25:12.056-00:30:00.000 | 04:55:12.056-05:00:00.000 |
| [part-11](README.md#part-11) | 00:00:00.000-00:07:38.168 | 05:00:00.000-05:07:38.168 |

## Edited conversation

### 04:55:12.056-04:59:20.632 | Sketching the platform's data model

**Speakers:** Lauren D1-H02, Roshan D1-H03, Matt D1-H01; turns are interleaved. **Type:** design brainstorming and fragmentary dictation.

Lauren asks what users do on the platform. They list sign-in, creating an event as the defining object with name and date/time, sign-up links, and management tools; a host proposes owners, hosts and attendees with platform-wide account types. Lauren wants a whiteboard, suggests a drawing tool, and dictates a fragmentary request to prototype the first flows, including event creation, a sign-up form and venue maps. ASR is very fragmented here; missing words are not reconstructed. Roshan wonders whether location data could help users research pop-up places. Matt asks whether to think big or build a tracer-bullet MVP; Lauren wants a scrappy prototype but first the hero use case.

### 04:59:20.632-05:01:04.216 | Hero use case and scope worry

**Speakers:** probable Roshan describing; Lauren; Matt. **Type:** discussion.

The hero use case is a person or group who wants a restaurant pop-up for their community and manages the whole operation on the platform: location, staffing, menu, a run of show, invitations and attendee management, ticketed or not. Lauren worries each part could be its own product and asks for a crisper core flow. Matt reduces an event to name and start/end time, then asks whether bookings need time slots.

### 05:01:04.216-05:03:06.968 | Run the pop-up first; build tools as needed

**Speakers:** Lauren proposing; Matt and Roshan agreeing. **Type:** proposal and apparent agreement.

Lauren suggests focusing on actually running their pop-up and building tools as they do it, incorporating them into the platform over time. Matt agrees they should start reaching out. He says finding food makers comes before menus and that bookings are blocked by the website: it collects emails but advertises no details. He wants the landing page done, restaurant canvassing and perhaps an X account inviting restaurant owners and Bay Area chefs, and says Dr. Eggbot will spin up an outreach bot D1-B-OUTREACH-M. This is a request.

### 05:03:06.968-05:05:47.864 | Manual work first, calls and company email

**Speakers:** Roshan asking; Lauren; Matt. **Type:** advice and planning.

Asked what is the best use of her time, Lauren says the core question is what to build, grounded in running their own pop-up, just as she does work manually before turning it into an agent skill. She notes, echoing Codie, that they are not domain experts. She suggests cold-calling, referencing a video Matt shared about connecting Grok Bot to a voice agent, but with humans taking over the calls. Matt says he can research phone numbers and will wire up email by configuring DNS for their domain; they weigh forwarding, a workspace suite or an agent-mail service, and agree emails should sound like a real person.

### 05:05:47.864-05:07:38.168 | A tentative October 15 date and research dispatch

**Speakers:** Matt dictating; Lauren; Roshan. **To:** Matt's Dr. Eggbot copy D1-B-EGG-M; cohosts. **Type:** instruction and tentative date choice.

Matt asks Dr. Eggbot for a research bot to find restaurateurs or businesses that could host the pop-up, thinking through food service, location and a date. Proposing a date about a month out so calls can cite it, he suggests October 15; a cohost agrees it is a good start. He asks it to note this in Notion as the business plan, list San Francisco and Bay Area caterers and restaurateurs, then research locations, dispatching bots in parallel. He then reports his bot has trouble accessing repositories; Lauren suggests restarting or the GitHub CLI, and Matt suspects a wrong connector. **October 15 is a working date, not a booked event.**

## Editorial changes and unresolved evidence

Speaker attribution in the data-model brainstorm is grouped because ASR does not separate turns. The fragmentary dictation is not converted into a clean prompt.
