# D1-C19: Venue finder, maps, auth and flyers

## Source and review state

- Interval: [05:07:38.168, 05:17:29.784).
- Source: X `1AxRnZbVpjaxl`; [inputs/hashes](README.md), [sources](../sources.md), [entities](../entities.md).
- **ASR-based review draft**, nonverbatim grouped conversation; not audio-verified. No quotations.
- Context: Hosts' live build (Ship by Thursday demo company); guest remarks within it are advice, not decisions.

## Input intervals and identity

Source/checkpoint hashes are in [the index](README.md). These are exact
silence-preserving PCM intervals, not audio-verified word or speaker boundaries.

| Part and hashes | Part-local interval | Source interval |
| --- | --- | --- |
| [part-11](README.md#part-11) | 00:07:38.168-00:17:29.784 | 05:07:38.168-05:17:29.784 |

## Edited conversation

### 05:07:38.168-05:09:57.880 | Lauren's request for a restaurant-finding tool

**Speaker:** Lauren D1-H02 dictating. **To:** Steve D1-B-STEVE-L, with Tater D1-B-TATER-L to spawn a cloud agent. **Type:** human-to-bot instruction.

Lauren gives Steve context: build the platform by dogfooding, doing the pop-up work themselves and only building tools once they are good. She wants to start with location, using potato mode, and asks Tater to spawn a cloud agent for prototypes of a tool that finds restaurants, makes phone calls easy and looks up people behind a restaurant, perhaps on professional networks, to reach a manager. She imagines a map with search by cuisine and location and fast calling, tool first rather than polished. She notes the prompt is two minutes long and, as usual, asks Steve to restate it before executing.

### 05:09:57.880-05:12:20.984 | Calling tools, a shortlist, maps and a places directory

**Speakers:** Lauren asking; probable Matt D1-H01 answering; Roshan D1-H03. **Type:** discussion and report.

Asked how he did phone calls, Matt names a voice-calling MCP and says he pulled a shortlist of about 15 restaurants into Grok Bot as a manual alternative, with bots also looking for locations and email setup. Lauren says they will need a map API key; they consider OpenStreetMap as a free alternative. A host proposes a directory of good pop-up places that hosts could rate after events. These are ideas and reported research, not calls made.

### 05:12:20.984-05:15:15.224 | Authentication choices and a manual contact list

**Speakers:** Lauren; Matt; Roshan. **Type:** technical decision discussion.

Lauren wants a simple admin dashboard accessible only by Matt. Matt describes his bot approach: find 20 businesses with emails and phone numbers for manual outreach; he thinks finding a caterer a month out is feasible but a location harder. They compare authentication services; one host says he will start with one service and adjust. They then find a Vercel deployment-protection option and settle on using it for the prototype's minimal authentication, to avoid overbuilding.

### 05:15:15.224-05:17:29.784 | Street-corner flyers, keys and a verification PR

**Speakers:** probable Roshan proposing flyers; Matt; Lauren. **Type:** proposals and status.

A host, probably Roshan, spins up a bot D1-B-GEO-U to find about 50 common San Francisco street corners and asks his design bot D1-B-DESIGN-R for flyers, for guerrilla marketing. Matt continues polishing the landing page and notes some steps, such as creating API keys, remain manual. Lauren reports a verification-skill PR is up and she is reading it. Someone asks a bot for regular status updates. A host says his new bot already knew about October 15 and that Notion should be the source of truth. Room noise signals the next session.

## Editorial changes and unresolved evidence

The flyer bot and design bot owners are probable. No calls, flyers or auth deployment are verified.
