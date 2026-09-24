# Day 2 sources and processing boundary

Status: **ASR-based review draft**. This pass curates the full-day X ASR only.
No YouTube captions, external identity research, guessed alignment or new
transcription were used. All quotations and audio-review gates remain pending.

## Authority and rights

The operator explicitly authorized processing these raw transcripts in this
editor-hosted model after discussion of that processing boundary. Local ASR does
not imply this subsequent curation is local-model processing.

The source manifest records operator-authorized **private study extraction**;
**redistribution rights are not established**. These derivatives are private-study
review drafts, not publication clearance. Public availability and a polished
paraphrase do not confer rights to publish names, claims or event material.
No network requests, cloud transcription, Git writes or deletions were performed
in this curation pass. Writes are restricted to `docs/days/day-02/`.

## Recording identity

| Field | Manifest evidence |
| --- | --- |
| Source | X broadcast `1PKqrNyvmYwGb` |
| Public reference, not fetched in this pass | `https://x.com/i/broadcasts/1PKqrNyvmYwGb` |
| Publisher/title | Grok Bot / Grok Bot builds a Game Studio LIVE |
| Local audio | `.data/day-02/day-2-grok-bot-galaxy.m4a` |
| Bytes | 255494347 |
| Audio format | AAC, stereo, 48000 Hz, extracted by stream copy |
| M4A reported duration | 30198.506 seconds |
| Curation timeline | 30198.528 seconds / 08:23:18.528, decoded PCM timeline |
| Source manifest | `.data/day-02/source-manifest.json` |
| Parts manifest | `.data/day-02/parts-manifest.json` |
| ASR validation record | `.data/day-02/asr-validation.json` |

The title is a source label, **not proof** of a built studio, launch or business
outcome. Source-relative time is not a wall-clock schedule or externally aligned
session time. The small container/PCM duration difference is retained, not hidden
by shifting or trimming timestamps.

### Hash anchors

Source M4A SHA-256:

```text
9f23b6c0fd2f89e0b5b56cdb7c79a0e1b9ed2d3dc4e4faaa064814c4be2c722a
```

ASR checkpoint/model identity:

```text
0d847ac4af716e652da03e4cc0a654cbe2a187f6b4697960f6a0d1c20571f5f0
```

Concatenated PCM payload SHA-256:

```text
5b459a94162a57a8c7951dfa3682cfec533e0c595a1acba57775755edf3f16b1
```

Every inventoried input has a byte count and SHA-256 in
[input-inventory.json](input-inventory.json), including all three manifests,
54 transcript exports, WAVs and historical working artifacts. Inventory does not
mean all files were semantic inputs: partial/probe audio and logs were hashed for
preservation, not used as alternative transcripts.

## Acquisition and PCM provenance

The manifest records an earlier HLS/MPEG-TS acquisition and FFmpeg 8.0.1 AAC
stream-copy extraction into M4A without audio re-encoding. It records two
non-monotonic DTS corrections and a successful full strict decode. The M4A is
an **extracted derivative, not the original transport bytes**. The transport's
recorded hash is provenance metadata; the manifest says temporary video was
previously removed. This pass did not delete or reacquire anything.

PCM is mono, 16000 Hz, signed 16-bit, totaling **483176448 samples**. The earlier
parts validation records concatenated WAV payloads matching the timeline-preserving
source decode by sample count and hash. This pass rechecks WAV properties and
concatenated payload identity but does not rerun the original M4A decoder or
claim listening review.

There are 16 full 1800-second parts plus a 1398.528-second remainder. Silence was
not removed from this timeline. Part-local recognition times are converted with
`(part_number - 1) * 1800` seconds; chapter boundaries can span parts.

## ASR inputs and reading coverage

- `.data/day-02/transcripts/part-01` through `part-17`, each JSON/TXT/SRT.
- `.data/day-02/transcripts/full-transcript.json`, `.txt` and `.srt`.
- Whisper tiny.en English INT8 on CPU, with Silero VAD. No diarization or
  word-level alignment. Recognition-region boundaries are approximate.
- All **17 TXT parts were read in full**, including placeholder and repetitive
  sections. This was not a keyword-only skim. The combined export is validated
  against the parts, not separately treated as an additional source of speech.
- Recorded ASR validation: passed at `2026-09-24T03:36:23.957769+00:00`, 17 complete
  parts, **4119 regions**, **4113 nonempty**, **6 empty**, combined exports
  validated, no temporary-checkpoint residue reported.
- Nonempty includes music/silence placeholders and hallucination-like fragments.
  Successful checkpoint completion is not proof of complete speech recognition.

The [coverage ledger](coverage-ledger.json) maps every raw JSON region by part
and one-based segment number into chapter/section intervals, with a text hash
rather than raw content. It also records every interval without a recognition
region. **Routing coverage is not semantic completeness or verified silence.**
See the [gap ledger](gap-ledger.md) for omissions and the
[review queue](review-queue.md) for unresolved evidence.

## Verification scope

[validation.json](validation.json) records the exact structural, export and
integrity checks actually run for this pass. It distinguishes matching input
hashes from successful audio/content review. The protected-doc baseline covers
`docs/README.md` and `docs/reference/youtube-sessions.md`; neither is an output
of this task. Expected concurrent Day 3/global work is outside this pass.

No authenticated services, emails, payments, bot instructions, deployment steps
or Git actions described in the recording were executed. The next synthesis
stage is reserved for the parent agent after review of this curation handoff;
this pass creates no decisions, progress or lessons documents.

## Verified session alignments

Added 2026-09-24 by a separate session-review pass, which read YouTube captions
under the operator's explicit approval of editor-hosted processing for private
study. The full-day curation statements above describe the earlier ASR-only
pass and remain accurate for it.

| Session | Mapping | Basis | Unmatched material |
| --- | --- | --- | --- |
| [SDRs, `Iia8EF7niiA`](sessions/sdr-Iia8EF7niiA.md) | Day 2 ≈ video + 05:59:51.5 (±0.5 s); video [00:00:00.160, 00:34:01.559) ↔ Day 2 ≈ [05:59:51.7, 06:33:53.1) | 12 content anchors from video 00:00:00.160 to 00:33:52.2; well-matched offsets 21591.46–21591.62 s, no drift or internal edit detected at anchor resolution | Day-side only: host handoff before 05:59:52 and the Q&A 06:33:57.080–06:39:49.016 (D2-C19 latter half). Video-side: none identified |

Alignment compares two automatic recognitions of the same speech; it is a
timing mapping, not independent confirmation of content. Playback has not
confirmed it (see D2-R32).
