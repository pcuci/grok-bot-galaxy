# Agent workspace

## Ownership and task boundary

[AGENTS.md](../../AGENTS.md) is the repository policy. Optional governance imports
are procedural guidance, not higher authority or permission. Project build,
transcription, tests, and event documentation must not depend on the governance
checkout. No submodule, package dependency, hook, service, credential, MCP server,
model provider, repeat task, or background agent is installed here.

The completed 2026-09-16 onboarding-only subtask permitted edits/validation in
`.agents/**`, generated `.cursor/` and `.claude/` projections, root `AGENTS.md`,
and this document. It excluded other docs, data, pipeline scripts, Git metadata,
and governance source edits. No staging, commits, push, or branch creation.
Completion ended that grant; these instructions are not future execution authority.

The subsequent explicit request to onboard the `baseline` capability set permits
updating the target import manifest, scoped importer/tests, runtime projections,
local prompt override, and related orientation docs. It does not authorize
changes to governance source, event evidence, root policy, Git state, credentials,
services, or automation. This onboarding grant ends with validated completion.

The initial Git state was unborn `main`, with no tracked files. Existing `data/`
and `docs/` directories were not evidence of an empty filesystem. No event media
or raw transcript content was read, downloaded, transcribed, or uploaded during
onboarding. Public standards pages were fetched for compatibility research only.

## Baseline capability set

- `.agents/agents.md` points to the authoritative root policy.
- `.agents/imports.json` declares `imports: [{"bundle": "baseline"}]`, resolved
  from the optional governance Codex source, not governance's local overrides.
- The inspected baseline contains 37 shared skills, including `save`, Git
  workflows, Decision Record workflows, review, progress, and documentation
  tools. None grants operations by being installed.
- Two agent definitions are projected: `dr-maintainer` and
  `sovereign-execution-architect`. These are available definitions, not running
  background agents or newly authorized tool/server access.
- All six baseline includes are accounted for: owned `agents.md` and
  `system-prompt.md` overrides, plus links for `mcp.json`, `models.json`,
  `dotagents-settings.json`, and `layouts/ui.json`. MCP servers are empty,
  models contain policy profiles only, settings are disabled, and UI panels empty.
- Four repository-owned skills implement event-specific guidance:
  [broadcast-ingest](../../.agents/skills/broadcast-ingest/skill.md),
  [local-transcribe](../../.agents/skills/local-transcribe/skill.md),
  [transcript-curate](../../.agents/skills/transcript-curate/skill.md), and
  [event-synthesize](../../.agents/skills/event-synthesize/skill.md).
- Local `skill.md` files are canonical. Relative `SKILL.md -> skill.md` links
  support uppercase discovery. Each runtime skill directory is a relative link
  to `.agents/skills/<name>`; no runtime instructions are authored separately.
- Imported markers link to Codex, not governance's repo-local overrides.
  Local regular `skill.md` files win. Never edit an imported file through a link.

This replaces the initial three-skill selection with the requested full baseline
capabilities while retaining the four event skills (41 skills total). The local
system prompt preserves repository-first authority instead of importing the
shared prompt's conflicting federal-first order. Root `AGENTS.md` is unchanged.

No GSD or unrelated vendor bundle is selected. Even `components: ["skills"]`
does not constrain all stock materializer behavior, so the scoped local importer
remains the maintained path. Imported `regovern` or `save` instructions referring
to absent helpers do not install them or override this maintenance procedure;
follow root policy and ask before extending the import set.

## Verified standards and differences

Sources fetched on 2026-09-16:

1. [Live .agents Protocol](https://dotagentsprotocol.com/), labeled
   **DRAFT 2026-02-24**, sections 3-6: workspace overrides are optional, adoption
   is incremental, and the displayed layout uses `memories/` and
   `speakmcp-settings.json`. The full layout and runnable examples are not a
   mandatory checklist for every repository.
2. [Website PR #7](https://github.com/aj47/dotagentsprotocol-website/pull/7),
   merged 2026-03-18 as `502a9d5f886d0aad8d3da83c03354bdfa4b389e7`:
   the inspected diff introduces `knowledge/`, `commands/`,
   `dotagents-settings.json`, and `enabledRuntimeTools`. These merged changes
   differ from the fetched live page; do not conflate source and deployed spec.
3. [Mono runtime source](https://github.com/aj47/dotagents-mono/tree/fd76e502e551d5266ce50a5ed4b1536ed7323e26/packages/core/src/agents-files),
   revision `fd76e502e551d5266ce50a5ed4b1536ed7323e26`: inspected
   `frontmatter.ts` and `skills.ts`. Frontmatter is parsed as simple single-line
   key/value pairs. Skill IDs fall back to the directory or name; `id` and
   `enabled` are not necessary for the four local skills. The serializer sorts
   keys alphabetically. The loader skips symlink entries, so external imported
   projections must not be assumed discoverable by this runtime.
4. [Agent Skills specification](https://agentskills.io/specification), live
   unversioned page: requires uppercase `SKILL.md`, YAML frontmatter with
   directory-matching lowercase-hyphen `name` and nonempty `description`.
   The local files use only these two fields, each on one line, to satisfy both
   parsers without tool grants or vendor-specific metadata.
5. Local governance source revision
   `42c3b85d3a2fe08c6482a778e727afc38c4aafe6`, inspected at
   `/home/paul/code/home.cloud/governance`:
   `scripts/onboard-governed-project.mjs`, `scripts/validate-dotagents.mjs`,
   `.agents/repo-contracts/templates/imports.template.json`, and
   `.agents/codex/bundles/baseline.json`. These are implementation evidence, not
   requirements that downstream projects adopt governance's entire workspace.

| Area | Finding and repository decision |
| ---- | ------------------------------- |
| Workspace | PASS: incremental guidelines and skills, not every runtime example. |
| Skill discovery | PASS: four owned lowercase markers with uppercase links; actual editor UI discovery remains untested. |
| Memories/knowledge | OMITTED: event knowledge stays in `docs/`; no duplicate archive or synthetic notes. |
| Settings and services | Baseline definitions only: disabled workspace settings, empty MCP servers/UI panels, policy-only model profiles, two non-auto-run agent definitions, and no tasks. This does not disable globally configured services. |
| Imports | EXTENSION: v2 manifest is a governance contract, not a live protocol file schema. |
| Imported frontmatter | LIMITATION: Codex uses extra top-level fields and multiline YAML descriptions. Do not claim strict Agent Skills or simple mono-parser compatibility for imported sources. |
| Backups | Runtime backup directories are not scaffolded as empty ceremony. Owned files are reviewed edits; generated links are reproducible and atomically replaced. |
| Local validator | NOT APPLICABLE wholesale: governance's validator is hardwired to its own checkout and requires Codex, settings, backups, registry and fixtures. It is not a downstream `--repo` validator. |

`agentify` guidance contains stale/self-contradictory rename examples and a broad
required-files checklist. Use the actual sources above, not those examples, to
decide applicability. Never run its save handoff under this onboarding grant.

## Manifest and safe materialization

The manifest uses a v2 `baseline` bundle import and `localOverrides.skills` for
the four owned event skills, with `components: ["skills", "agents"]` and no
extra explicit skills. `sourcePackage` is interpreted relative to `.agents/`
by the local adapter. `x-governance.optional` and `observedRevision`
are explicitly repository extensions: the revision records the inspected source,
not an immutable pin. Symlinks follow subsequent checkout changes, so review and
revalidate on refresh. Optional means the project and owned skills work without
that checkout; it does not make existing broken import links valid.

Stock tooling was inspected and dry-run during both initial and baseline
onboarding, but deliberately not applied:

```sh
# Run from the governance checkout; both commands are read-only previews.
node scripts/onboard-governed-project.mjs --repo /home/paul/code/pcuci/grok-bot-galaxy --bundle baseline --dry-run
node scripts/onboard-governed-project.mjs --repo /home/paul/code/pcuci/grok-bot-galaxy --dry-run
```

Both initially resolved successfully. With the old manifest, the second
recognized the three Codex and four repo-local skill selections, but additionally
planned vendor skill bridges and vendor agents. The baseline dry run resolves
the requested shared skills but retains those unrelated vendor side effects. `resolveSelectedAgentSources` generates vendor adapters
unconditionally, and component bridging is broader than selected skills.
`sourcePackage` is not used for source resolution; the invoked script's checkout
is used instead. `--profile` examples in the onboarding skill are stale; use
neither that flag nor an assumed source-path option. Reinspect before any future
stock-tool application, which is not the maintained refresh path here.

The standard-library-only adapter at `.agents/scripts/onboard.py` validates the
narrow manifest subset, owned skill metadata, and baseline catalog, preflights
all destinations, and projects only selected skills, agents, and includes. It
supports the old explicit-skill form as well as the baseline; it is not a generic
replacement for the governance materializer.

It rejects unsupported bundle asset classes, unsafe paths, source links escaping
Codex, active MCP/settings/provider configuration, and auto-run agent connections.
Agent tool/server lists remain source metadata, not permission to use those tools
or servers. No fetch, Git, source writes, task activation, or build integration
occurs. Existing owned includes are preserved; other owned-path conflicts and
symlinked destination parents fail before projection writes. Link writes use
temporary symlinks and atomic rename; no backups of event data are made. Run it
without concurrent workspace edits. It does not prune old/unselected assets;
review removals explicitly rather than broad-cleaning the workspace.

From this repository root:

```sh
python3 -B .agents/scripts/onboard.py --dry-run
python3 -B .agents/scripts/onboard.py
python3 -B .agents/scripts/onboard.py --check
python3 -B .agents/scripts/test_onboard.py
```

For a relocated governance checkout, inspect its source first, then supply its
actual absolute path via `--governance`. Preview with `--dry-run --relink`, then
apply with `--relink` only after reviewing the changed link destinations; this
never permits replacing regular files. The override does not rewrite the
manifest. Update `sourcePackage` separately if the new relative layout should be
shared. Re-run `--check` with the same override. Do not invent a checkout URL,
auto-clone governance, or add it as a project dependency.

Without governance, use `--local-only` (also accepted with `--dry-run` or
`--check`). It maintains/checks the four owned skills and skips the baseline
bundle's assets with a warning; existing external links are left alone. A missing optional checkout
also warns and skips imports by default. A present but incomplete or ambiguous
Codex source fails instead of silently selecting a different skill. Import
removal/cleanup requires a separately reviewed edit. Essential policy and local
instructions remain regular, readable files without Python or governance.

## Baseline onboarding validation

- Requested bundle: 37 Codex skills, four retained local skills, two agent
  definitions, and six includes (two owned overrides, four shared links).
- Applied 148 new relative links; all 172 planned links passed `--check`.
- A second application changed zero links. The two preservation warnings for
  owned `agents.md` and `system-prompt.md` are expected.
- `--check --local-only` passed for 12 owned-skill projections, with one expected
  warning that baseline assets were skipped.
- `python3 -B .agents/scripts/test_onboard.py`: 28 tests passed, including baseline
  resolution/overrides, no vendor expansion, missing optional source, unsafe
  paths, active configuration rejection, preflight conflicts, and catalog drift.
- All source links are live checkout references, not immutable pins. Revalidation
  detects unsupported catalog/config changes but cannot prevent source content
  from changing between checks. No pruning or upstream runtime certification is
  claimed. Actual editor/agent runtime invocation is not part of onboarding.

## Historical initial-onboarding validation

The following records describe the earlier three-skill state, not the current
baseline configuration.

- Stock full-baseline and narrowed-manifest dry runs: passed resolution; broad
  side effects observed and not applied.
- Local adapter dry run: 24 planned relative links, seven skills, no skipped
  imports; schema validation passed. Application created those 24 links.
  `python3 -B .agents/scripts/onboard.py --check` passed; a second application
  changed zero links. `--check --local-only` passed for 12 local links with
  three explicit optional-import warnings.
- `python3 -B .agents/scripts/test_onboard.py`: 11 tests passed, covering dry-run
  purity, idempotence, optional-source absence, local-only mode, schema rejection,
  owned-file conflicts, symlink-parent escape, local precedence, explicit
  relinking, invalid skill metadata, ambiguous imports, and escaping resources.
- Independent PyYAML parsing: all four owned skill files passed the required
  `name`/`description` subset. No `skills-ref` executable or Markdown linter was
  installed; do not describe these checks as an upstream validator certification.
- Independent structural checks passed for seven owned Markdown files (local
  links, trailing whitespace, final newlines), Python AST parsing, all 24
  resolving relative symlinks, symlink-only runtime projections, and absence of
  MCP/model/task/agent configuration. This was not a Markdown lint run.
- Final read-only Git checks: source governance remained clean at the recorded
  revision; target remained on unborn `main` with an empty index. All new files
  listed by Git were within the authorized paths.

This is governance onboarding, not validation of an implemented media pipeline.
No pipeline CLI flags, ASR accuracy, checkpoints, source permissions, or day
outcomes were verified. Day-one expected paths are
`data/day-01/{day-1-grok-bot-galaxy.m4a,parts/*.wav,transcripts/*,transcribe.py,silero_vad.onnx}`;
inspect real scripts and `--help` before processing. Days two and three remain
pending source acquisition/review.

LFS attributes and video ignore configuration are outside the authorized edit
scope. `git check-attr filter -- data/day-01/day-1-grok-bot-galaxy.m4a` reported
`unspecified`. `git check-ignore --verbose --no-index` for that same audio path
returned exit 1 (no matching ignore rule), not a successful exclusion. No LFS or
ignore configuration was added. The policy is not enforcement: verify actual
attributes/video ignore rules and publication rights before any later staging.
Models, checkpoints, raw transcripts, and evidence originals are not
automatically publishable.

### Subsequent repository foundation work

The preceding validation record is the onboarding-only snapshot. Subsequent
work under the broader migration/documentation request added `.gitignore` and
scoped audio `.gitattributes`, root orientation, a document layout, editorial
method, and day placeholders. Git LFS remains absent; attributes are not an
installation or publication authorization. See the current
[Day 1 source record](../days/day-01/sources.md) for media/checkpoint validation
and the [roadmap](../../ROADMAP.md) for outstanding gates. No portable pipeline
under `scripts/` has been added. The governance checks and 11 tests were rerun
successfully after migration; no materialization changes were needed.

### Later audio-storage change

The historical `data/` and LFS statements above describe prior states. The human
subsequently requested ignored `.data/` originals and compact audio suitable for
ordinary Git. All 78 original files were moved with matching hashes; local skills
and root policy now reflect that layout. `scripts/prepare_audio.py` and its tests
implement compact derivative preparation, not a replacement ASR pipeline.
The full encode timed out before completion; partial outputs remain ignored.
See [audio storage](audio-storage.md) for current commands, quality evidence,
validation results, and the pending completion gate.
