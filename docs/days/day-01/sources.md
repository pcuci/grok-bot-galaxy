# Day 1 sources and validation

Status: media and checkpoints structurally validated on 2026-09-16; an
**ASR-based curation draft** was added on 2026-09-24 (see
[curation pass](#curation-pass-on-2026-09-24)). No audio was listened to.

## Source and rights

- Public source: [X broadcast 1AxRnZbVpjaxl](https://x.com/i/broadcasts/1AxRnZbVpjaxl).
- Inherited title/publisher: Day 1: Grok Bot Galaxy Livestream, @bot.
- Context references for future review: [official event page](https://x.ai/galaxy),
  [event listing](https://luma.com/3ifrgttw), and
  [PM session listing](https://luma.com/spacexai-qki6).
- These public pages were not re-fetched during the 2026-09-16 media validation.
- Acquisition was requested by the operator in the earlier conversation.
  Exact retrieval timestamp/timezone and independent rights evidence remain
  unrecorded. Public availability is not redistribution permission.
- **Hosted-model processing:** the operator (Paul) explicitly approved
  editor-hosted model curation of Day 1 raw ASR on 2026-09-24, for private
  study, on the same basis as Days 2 and 3. This covers reading raw transcripts
  in this editor model; it is not publication or redistribution permission.
- Audio publication and redistribution rights remain open gates. No external
  transcription service is configured, and no transcription was rerun.

The inherited acquisition report describes an HLS download using yt-dlp
2026.08.19, all 15,599 fragments acquired, audio extracted, and temporary video
removed. This report was not independently reproduced here. The M4A is the
preserved extracted-audio artifact, not a claim of byte identity with the
original broadcast stream. Original extraction codec-copy/transcode details are
not established by the present probe.

## Current local artifacts

Paths are relative to repository root. Originals now live under ignored `.data/`;
the relocation preserved all 78 files byte-for-byte. See
[audio storage](../../reference/audio-storage.md) for codec tests and the
incomplete compact-derivative preparation.

| Artifact | Measured result |
| -------- | --------------- |
| `.data/day-01/day-1-grok-bot-galaxy.m4a` | 265,500,294 bytes |
| Source stream | AAC, stereo, 48,000 Hz |
| Container duration | 31,512.519667 seconds |
| Reported start offset | 0.012 seconds |
| `.data/day-01/parts/part-01.wav` through `part-17.wav` | 28,800,000 samples / 1,800 seconds each |
| `.data/day-01/parts/part-18.wav` | 14,601,078 samples / 912.567375 seconds |
| All WAVs | Mono, 16,000 Hz, signed 16-bit uncompressed PCM |
| Total PCM | 504,201,078 samples / 31,512.567375 seconds |
| Raw checkpoints | 18 complete parts, 2,977 recognition regions |

M4A SHA-256 measured after migration:

```text
22d46211b73e916a5f3a845201fcfa72eaef878078103838a09e3ef987f0ba80
```

Concatenated WAV PCM SHA-256 (payloads only, not WAV headers):

```text
0902621aa6c75a4c16b4ff9841bf0eb2b8adaaa8fcf9c70b6e585f360c89e5e2
```

All checkpoint model/VAD/script identities matched this recomputed identity:

```text
0d847ac4af716e652da03e4cc0a654cbe2a187f6b4697960f6a0d1c20571f5f0
```

No pre-migration source hash record was available in the inspected layout. The
current hash is a baseline, not proof of historical byte preservation. Metadata
inspection confirmed the old `.dotfiles/tmp/grok-bot-1AxRnZbVpjaxl` directory is
absent. Artifact paths now resolve under this repository.

## Timeline handling

Source packet timestamps contain gaps according to the inherited processing
record. The historical split filled gaps with silence instead of shifting all
subsequent speech earlier. The recorded split command, run from the data day
directory at the time, was:

```sh
ffmpeg -nostdin -v error -xerror -y \
  -i day-1-grok-bot-galaxy.m4a \
  -map 0:a:0 -ac 1 -ar 16000 \
  -af 'aresample=16000:async=1:first_pts=0,asetnsamples=n=16000:p=0,asetpts=N/SR/TB' \
  -c:a pcm_s16le -f segment -segment_time 1800 \
  -segment_start_number 1 -reset_timestamps 1 parts/part-%02d.wav
```

This is historical documentation, **not an instruction to overwrite existing
parts**. Do not rerun it in place. The current read-only validation reproduced
its filter and compared decoded PCM to existing WAV payloads.

The PCM endpoint differs from the container duration by 0.047708 seconds.
The inherited playlist estimate was approximately 31,518.7 seconds; it was not
revalidated. Do not equate the PCM timeline with exact broadcast schedule time.

## Local transcription

The preserved `.data/day-01/transcribe.py` uses isolated PEP 723 dependencies,
including sherpa-onnx 1.13.8 and NumPy, Whisper tiny.en int8 encoder/decoder, and
Silero VAD. The model directory belongs to the local Speed of Sound installation;
the historical runner is operator-specific, not yet a portable pipeline.

Recognition windows are bounded to 25 seconds; processing parts are 30 minutes.
The inherited run used eight workers and one thread per worker. These runtime
settings are not encoded in checkpoint identity. VAD gives approximate speech
regions, not diarization or word alignment.

Silero model SHA-256 from the inherited acquisition record:

```text
9e2449e1087496d8d4caba907f23e0bd3f78d91fa552479bb9c23ac09cbb1fd6
```

Preserve the original runner, models, and raw checkpoints. Changing script bytes
changes identity and can invalidate resume checks. No transcription rerun or
model installation was performed during this validation.

## Validation on 2026-09-16

Read-only local Python checks, using standard-library hashing, WAV parsing, and
JSON assertions, passed:

- Exactly 18 sequential parts; actual payload lengths agree with WAV headers.
- Every WAV hash agrees with its existing checkpoint signature.
- Every checkpoint is complete and has matching part, duration, offset, region
  count, and recomputed model/VAD/script identity.
- All 2,977 regions are finite, sample-aligned, ordered, non-overlapping, within
  their part, and no longer than 25 seconds.
- Combined JSON equals the script-defined offset-adjusted concatenation.
- TXT/SRT exports exist; their contents were not reviewed.
- No temporary checkpoints were found; validation inputs' metadata stayed stable.

The following historical probe was executed from repository root before the
move to `.data/`. Substitute `.data/` for `data/` when inspecting current files:

```sh
/usr/bin/ffprobe -v error \
  -show_entries format=format_name,start_time,duration,size,bit_rate:stream=index,codec_type,codec_name,sample_rate,channels,channel_layout,time_base,start_pts,start_time,duration_ts,duration,nb_frames \
  -of json data/day-01/day-1-grok-bot-galaxy.m4a
```

A read-only source decode used the following command. Its binary stdout was
captured directly by a Python in-memory hash, never printed or written to disk:

```sh
/usr/bin/ffmpeg -hide_banner -loglevel warning -nostdin -xerror \
  -threads 1 -i data/day-01/day-1-grok-bot-galaxy.m4a \
  -map 0:a:0 -vn -sn -dn \
  -af 'aresample=16000:async=1:first_pts=0,asetnsamples=n=16000:p=0,asetpts=N/SR/TB' \
  -ac 1 -ar 16000 -c:a pcm_s16le -f s16le pipe:1
```

FFmpeg 8.0.1-3ubuntu2+esm4 exited 0 in 38.579 seconds, with no warning/error
output. The resulting sample count and SHA-256 matched all existing WAV payloads
exactly. Commands were bounded to 120 seconds, with a 110-second decode timer.

An earlier comparison omitted the historical silence-preserving filter and
failed: it decoded only 31,500.352 seconds, 12.215375 seconds less than the WAVs.
That comparison was not a reproduction of the split procedure. The corrected
filter comparison above resolved the discrepancy; no media was rewritten.

## Remaining limitations

- No audio listening, ASR quality grading, or independent speech-coverage review.
- One empty-text recognition result in part 14; it does not prove silence.
- Checkpoint signatures do not include the M4A hash, schema version, or runtime
  settings. A durable source/parts provenance manifest remains future work.
- The 2026-09-16 structural checks inspected raw JSON only in local memory. The
  2026-09-24 curation pass, under the approval above, read all TXT parts in this
  hosted editor model; see below.
- Compact Opus derivatives now use ordinary Git attributes, not LFS. Preparation
  timed out before completion; partial outputs are ignored and no audio is staged.
- No video is tracked. Ignore patterns cannot prevent deliberate force-adds or
  identify video saved with a misleading extension.

## Curation pass on 2026-09-24

Authority: operator approval of editor-hosted curation for private study, as
recorded above. Writes were limited to `docs/days/day-01/**` and the Day 1
status lines in the root README, docs index, layout reference and roadmap.
Raw `.data/day-01/` was read-only; no network, transcription rerun, caption
input, Git staging or event synthesis was used.

- All 18 TXT parts were read in full in chronological order. JSON supplied exact
  region intervals and was cross-checked against TXT/SRT structurally.
- Output: 32 chronological chapters, 151 timed groups, covering
  00:00:00.000-08:45:12.567375 with half-open intervals. See the
  [transcript index](transcripts/README.md), [entities](entities.md),
  [gap ledger](gap-ledger.md), [editorial log](editorial-change-log.md) and
  [review queue](review-queue.md).
- Machine records: [input inventory](input-inventory.json) (all 78 files under
  `.data/day-01/`, hashed before writing), [coverage ledger](coverage-ledger.json)
  (all 2,977 regions routed, one empty region, inter-region gaps) and
  [validation](validation.json) (fresh integrity, structure, link and privacy
  pattern checks after writing).
- The derivative is an edited nonverbatim conversation. No quotation is
  audio-verified; the skill's audio checks for boundaries and consequential
  claims remain **unmet**.
