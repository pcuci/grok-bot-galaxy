# Grok Bot Galaxy

An evolving, evidence-linked account of how humans and Grok bots work together:
what they attempted, what they demonstrated, what they decided, and what other
teams can learn. Requests, bot success reports, and verified outcomes are not
interchangeable.

Day 1–3 curation status updated: 2026-09-24. The prerequisite
and Day 1 preparation instructions below retain their 2026-09-16 validation
baseline; see each day's source record for its own checks.

## Current state

| | Day 1 | Day 2 | Day 3 |
| --- | --- | --- | --- |
| PCM duration / parts | 08:45:12.567 / 18 | 08:23:18.528 / 17 | 07:58:22.357 / 16 |
| Local ASR regions (structurally validated) | 2,977 | 4,119 | 3,806 |
| Curated chapters (ASR-based draft) | [32](docs/days/day-01/transcripts/README.md) | [26](docs/days/day-02/transcripts/README.md) | [33](docs/days/day-03/transcripts/README.md) |
| Audio review / synthesis | Pending | Pending | Pending |

Structural ASR completion does not establish accuracy or full speech coverage.
Day 2/3 acquisition used yt-dlp HLS fragments; see the
[extraction checkpoint](docs/reference/day-02-03-extraction-status.md).

- Ten official YouTube sessions have local captions and full-text Markdown
  derivatives under ignored `.data/youtube/`; content review remains separate
  from structural validation. See the [session source record](docs/reference/youtube-sessions.md).
- Full-day Day 2/3 audio, exact PCM chunks and raw transcripts passed structural
  validation. See the [checkpoint](docs/reference/day-02-03-extraction-status.md)
  for durations, local paths and limitations. Curation used full-day ASR, not
  aligned YouTube captions; neither source establishes verified day outcomes.
- Four repo-local skills capture ingest, transcription, curation, and synthesis.
  Governance's optional `baseline` adds 37 shared skills and two agent definitions;
  it is not a project dependency or permission to execute their workflows.

## Start here

- [Documentation index](docs/README.md)
- [Complete planned knowledge-base layout](docs/reference/knowledge-base-layout.md)
- [Day 1 source and validation record](docs/days/day-01/sources.md)
- [Day 2 curation draft](docs/days/day-02/README.md)
- [Day 3 curation draft](docs/days/day-03/README.md)
- [Editorial method](docs/reference/editorial-method.md)
- [Agent workspace and governance maintenance](docs/reference/agent-workspace.md)
- [Roadmap](ROADMAP.md)

## Understand the sessions and learn from them

Two repo-owned skills provide the core workflow:

| Skill | Question it answers | Output |
| --- | --- | --- |
| [`transcript-curate`](.agents/skills/transcript-curate/SKILL.md) | What happened, who was speaking, and what was requested, claimed, or shown? | Source-linked chapters, attribution notes, and coverage/review gaps |
| [`event-synthesize`](.agents/skills/event-synthesize/SKILL.md) | What decisions, outcomes, lessons, and open questions does the reviewed evidence support? | Concise session reviews, then day-level and cross-session synthesis |

Optional `file-review` checks factual support; `denoise` makes reviewed writing
more concise. Ingest and transcription skills are only needed for new source
material, not to reread the captions already available.

Start with one session: review its chronological topics, check consequential
claims against source playback, then write a nonverbatim review using the
[session review template](docs/templates/session-review.md). Keep caption-only
findings provisional. Full text stays in ignored `.data/`; authored reviews go
under `docs/days/day-XX/sessions/`, with day and cross-session lessons built from
those reviews. Do not create empty reports or infer events from missing sources.

- [Detailed analysis workflow, skill map, and folder hierarchy](docs/reference/session-analysis.md)
- [Session videos, local input locations, and timing caveats](docs/reference/youtube-sessions.md)
- [Editorial and evidence rules](docs/reference/editorial-method.md)

Analysis is a separate step from downloading or converting captions. Confirm
permission for the actual model-hosting environment before sending it raw text;
no skill implicitly authorizes that processing, publication, or Git operations.

## Local evidence and publication

Ignored `.data/day-01/` contains the extracted M4A, `parts/part-01.wav` through
`part-18.wav`, raw `transcripts/`, the historical `transcribe.py`, and the Silero
VAD model. Preserve the runner and checkpoints: script bytes participate in
checkpoint identity. Do not rerun transcription just to reorganize documents.

Original audio, PCM, raw transcripts, models, and local experiments stay ignored
under `.data/`. Compact mono Opus derivatives are intended for
`audio/day-01/part-*.opus`, using ordinary Git rather than LFS. Never force-add
originals or video. The 32 kbps setting was selected after a small local ASR
comparison, not a claim of unchanged accuracy; prefer original PCM for ASR.

**Derivative preparation is incomplete:** the full-event encode hit its
five-minute command limit. Partial files are preserved under ignored
`.data/audio-quality/interrupted-prepare-32/`; no completed audio manifest exists.
See [audio storage and quality](docs/reference/audio-storage.md) for measurements,
limitations, the tested preparation command, and remaining validation.

The interrupted audio preparation did not stage, commit or push media. A request
to version audio does not establish a license to redistribute a third-party broadcast. Record rights
and destination access before publication; check originals and derivatives for
incidental private content.

Raw transcript curation by an editor-hosted model may send content off-machine.
That processing requires explicit authorization; no third-party transcription
service is configured here.

## Prerequisite software

Media processing runs locally on a CPU. It does not require a GPU/CUDA, a paid
transcription service, the Speed of Sound GUI, Git LFS, or a governance checkout.
Initial tool/model installation and source acquisition require network access;
recognition can then run offline.

| Software | Purpose | Locally checked version |
| -------- | ------- | ----------------------- |
| Git | Repository access; eventual authorized audio versioning | Use your system Git |
| Python | Preparation scripts require 3.10+; use 3.12 for the tested ASR environment | 3.12.13 for ASR |
| uv | Isolated yt-dlp execution and transcription script dependencies | 0.12.13 |
| yt-dlp | Inspect and download an authorized broadcast | 2026.08.19 |
| FFmpeg and FFprobe | Extract, inspect, resample, split, encode, and validate audio | 8.0.1-3ubuntu2+esm4 |
| sherpa-onnx | CPU inference with Whisper tiny.en int8 and Silero VAD | 1.13.8 |
| NumPy | Audio arrays for the local ASR runner | 2.5.3 in the codec experiment |

FFmpeg needs AAC decoding, PCM WAV output, the `aresample`, `asetnsamples`, and
`asetpts` filters, the segment muxer, and **libopus** encoding. The checked
versions describe this machine, not a lockfile or a guarantee that every newer
combination works. The historical runner pins sherpa-onnx but not NumPy.

For Ubuntu/Debian, a starting point is:

```sh
sudo apt-get update
sudo apt-get install git python3 ffmpeg
```

Install `uv` using its [official installation guide](https://docs.astral.sh/uv/getting-started/installation/).
Then install the tested Python minor version and check the tools:

```sh
uv python install 3.12
uv --version
uv tool run --from yt-dlp yt-dlp --version
ffmpeg -version
ffprobe -version
ffmpeg -hide_banner -h encoder=libopus
python3 -B scripts/prepare_audio.py --help
```

These are setup suggestions, **not a clean-machine-tested installer**. Distribution
packages can be older than the checked versions; confirm capabilities before
processing. `uv tool run` may download packages on first use. Once cached, use
`--offline` to prevent uv network resolution.

Allow several GB of free disk space: Day 1's M4A and WAVs alone occupy **1.27 GB**
(decimal), before models, dependency caches, raw transcripts, compact derivatives,
and temporary outputs. A video-backed acquisition can require additional space.
Ignoring `.data/` keeps files out of Git; it does not free local disk space.

## Reproducing the media workflow

Run these examples from repository root. Do not run them over preserved evidence.
Confirm source permissions and platform terms before downloading, and record the
source URL, retrieval time, tool versions, and SHA-256 hashes without credentials
or signed URLs. Publication requires a separate rights check.

### 1. Inspect and download audio

Inspect the available formats first:

```sh
uv tool run --from yt-dlp yt-dlp --no-playlist --list-formats \
  'https://x.com/i/broadcasts/1AxRnZbVpjaxl'
```

The following is a **new reproduction example**, not the recovered historical
download command. It requires an audio-only format and a fresh directory:

```sh
mkdir -p .data
mkdir .data/reproduce-day-01 && \
uv tool run --from yt-dlp yt-dlp \
  --no-playlist --no-overwrites -f bestaudio \
  --extract-audio --audio-format m4a \
  -o '.data/reproduce-day-01/source.%(ext)s' \
  'https://x.com/i/broadcasts/1AxRnZbVpjaxl'
```

`--extract-audio` uses FFmpeg; requesting M4A may require conversion if the source
codec is not suitable. It does not promise byte identity with the broadcast.
If no audio-only format is available, this command fails rather than silently
falling back to video. Review the format list and acquisition permissions before
selecting a video-backed stream; keep any temporary video ignored under `.data/`.
Do not bypass authentication or access restrictions.

The inherited Day 1 acquisition used HLS and removed temporary video after audio
extraction. Its exact format selector and codec-copy/transcode choices were not
recovered. The preserved artifact is `.data/day-01/day-1-grok-bot-galaxy.m4a`;
see the [source record](docs/days/day-01/sources.md) for its hash and limitations.

### 2. Extract PCM and split into exact half-hour parts

After a successful download, inspect the new audio:

```sh
ffprobe -v error -show_format -show_streams -of json \
  .data/reproduce-day-01/source.m4a
sha256sum .data/reproduce-day-01/source.m4a
```

Decode, downmix to mono, resample to 16 kHz signed 16-bit PCM, and segment in one
pass. The fresh-directory guard prevents overwriting an existing parts set:

```sh
mkdir .data/reproduce-day-01/parts && \
ffmpeg -nostdin -v error -xerror -n \
  -i .data/reproduce-day-01/source.m4a \
  -map 0:a:0 -ac 1 -ar 16000 \
  -af 'aresample=16000:async=1:first_pts=0,asetnsamples=n=16000:p=0,asetpts=N/SR/TB' \
  -c:a pcm_s16le -f segment -segment_time 1800 \
  -segment_start_number 1 -reset_timestamps 1 \
  .data/reproduce-day-01/parts/part-%02d.wav
```

**Keep the filter intact.** It preserves timestamp gaps as silence and aligns
segment boundaries; a naive decode of the preserved Day 1 source shortened its
PCM timeline by 12.215375 seconds. The validated original produced 17 parts of
28,800,000 samples each plus a final 14,601,078-sample part. A newly downloaded
source may differ: verify sample counts, hashes, and source-to-parts alignment
rather than assuming it matches. Never use silence removal to concatenate speech.

### 3. Transcribe locally: currently operator-specific

**A clean clone cannot yet run the historical ASR workflow.** The runner, raw
checkpoints, audio, and models are not distributed with the repo. The preserved
`.data/day-01/transcribe.py` also hardcodes the local model directory:

- `~/snap/speedofsound/common/models/sherpa-onnx-whisper-tiny.en/`
  - `tiny.en-encoder.int8.onnx`
  - `tiny.en-decoder.int8.onnx`
  - `tiny.en-tokens.txt`
- `.data/day-01/silero_vad.onnx`

The GUI supplied the cached Whisper assets; inference here uses sherpa-onnx,
not the GUI. Consult the [official sherpa-onnx project](https://github.com/k2-fsa/sherpa-onnx)
for compatible Whisper model assets and their terms. The recorded VAD asset is
[Silero VAD](https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/silero_vad.onnx);
its recorded SHA-256 is in the [source record](docs/days/day-01/sources.md).
Verify asset hashes before reusing checkpoints; an arbitrary similarly named
model is not interchangeable.

If the preserved runner and matching assets are already available, its PEP 723
header lets uv resolve NumPy and `sherpa-onnx==1.13.8`. Inspect the CLI first:

```sh
uv run --offline --no-project --python 3.12 \
  .data/day-01/transcribe.py --help
```

Offline execution requires cached Python and dependencies. On a newly provisioned
machine, omitting `--offline` permits uv to resolve/download dependencies; it does
not acquire model files. Once inputs are verified and a transcription run is
intended, a bounded single-part invocation is:

```sh
uv run --offline --no-project --python 3.12 \
  .data/day-01/transcribe.py --parts 1 --workers 1 --threads 2
```

This targets the preserved `day-01/parts/`, **not** the fresh reproduction folder.
It writes checkpoints and TXT/SRT exports under `day-01/transcripts/`; even a
completed-part rerun rewrites exports and combined outputs. Do not execute it
merely to check installation, or edit the historical runner in place: its bytes
are part of checkpoint identity. A portable, versioned runner with configurable
paths remains follow-up work.

The original full run used eight workers and one thread per worker. Choose
parallelism for available CPU/RAM rather than copying that setting blindly.
Silero VAD finds speech regions, then Whisper processes windows up to 25 seconds;
30-minute parts are storage units, not model context windows. Outputs have
approximate speech-region timestamps, **not speaker identification**. Readable
chapters and human/bot attribution require a separate evidence review.

### 4. Prepare compact audio for Git

For the existing validated Day 1 source and PCM parts:

```sh
python3 -B scripts/prepare_audio.py \
  --source .data/day-01/day-1-grok-bot-galaxy.m4a \
  --parts .data/day-01/parts \
  --output audio/day-01 \
  --bitrate-kbps 32
```

Append `--check` for read-only verification **after** successful completion and
manifest creation. The CLI validates decoded sample counts and hashes, refuses
conflicting outputs, and writes the manifest last. It neither downloads nor
transcribes media. The first full-event run timed out; a longer bounded rerun
is still pending approval. Do not treat partial files as a completed set.

32 kbps mono Opus is a provisional storage compromise, not a proven minimum for
accurate recognition. Keep original PCM for preferred ASR input. See
[audio storage and quality](docs/reference/audio-storage.md) for the comparison,
full validation contract, and publication gates.

The preparation script's automated checks are:

```sh
python3 -B -W error -m unittest discover -s scripts -p test_prepare_audio.py -v
```

These include small FFmpeg integration cases, not full-event transcription or a
listening review. No media is staged or published by this workflow.

## Agent workflow

Read [AGENTS.md](AGENTS.md). The four owned skills are:

- `broadcast-ingest`: provenance and timeline-preserving half-hour parts.
- `local-transcribe`: bounded local ASR and validated resumable checkpoints.
- `transcript-curate`: readable, evidence-linked chapters with qualified attribution.
- `event-synthesize`: decisions, progress, lessons, and unresolved questions.

The full `baseline` capability set is declared in `.agents/imports.json` and
projected through the scoped local importer. Local policy and prompt overrides
remain authoritative; shared MCP configuration is empty and workspace activation
is disabled. Unrelated vendor bundles are not imported.

The governance workspace has its own independently runnable checks:

```sh
python3 -B .agents/scripts/onboard.py --check
python3 -B .agents/scripts/test_onboard.py
```

These validate agent workspace setup, not transcript quality.
`scripts/prepare_audio.py` prepares and validates compact derivatives; it does
not download media or transcribe it. The historical transcription runner remains
local under `.data/day-01/`. Inspect real implementations and `--help` before
running commands.
