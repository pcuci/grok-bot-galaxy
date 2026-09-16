#!/usr/bin/env python3
"""Opt-in explicit-skill or baseline governance projection; standard library only."""

import argparse
import json
import os
from pathlib import Path
import re
import sys
import uuid

NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
BASELINE_INCLUDES = {
    "agents.md", "system-prompt.md", "mcp.json", "models.json",
    "dotagents-settings.json", "layouts/ui.json",
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate_manifest(manifest):
    """Validate the intentionally narrow v2 subset, not the entire Codex schema."""
    require(isinstance(manifest, dict), "Manifest must be an object")
    require(set(manifest) == {
        "version", "sourcePackage", "imports", "skills", "localOverrides",
        "components", "include", "exclude", "x-governance",
    }, "Unexpected or missing manifest fields; review before expanding imports")
    require(type(manifest["version"]) is int and manifest["version"] == 2,
            "Expected manifest version 2")
    source = manifest["sourcePackage"]
    require(isinstance(source, str) and source and not Path(source).is_absolute(),
            "sourcePackage must be relative to .agents")
    baseline = manifest["imports"] == [{"bundle": "baseline"}]
    require((baseline and manifest["components"] == ["skills", "agents"]
             or manifest["imports"] == [] and manifest["components"] == ["skills"])
            and manifest["include"] == [] and manifest["exclude"] == [],
            "Only explicit skills or baseline with components [skills, agents] are supported")
    metadata = manifest["x-governance"]
    require(isinstance(metadata, dict) and set(metadata) == {
        "optional", "observedRevision"}, "Invalid x-governance metadata")
    require(metadata["optional"] is True and isinstance(metadata["observedRevision"], str)
            and re.fullmatch(r"[0-9a-f]{40}", metadata["observedRevision"]),
            "Governance must be optional with an observed revision")
    overrides = manifest["localOverrides"]
    require(isinstance(overrides, dict) and set(overrides) == {"skills", "disabledSkills"}
            and overrides["disabledSkills"] == [], "Unsupported localOverrides shape")
    for entries, source in [(manifest["skills"], "codex"), (overrides["skills"], "repo")]:
        require(isinstance(entries, list), "Skill selections must be arrays")
        names = set()
        for entry in entries:
            require(isinstance(entry, dict) and set(entry) == {"name", "source"},
                    "Each skill requires name and source only")
            name = entry["name"]
            require(isinstance(name, str) and len(name) <= 64 and NAME.fullmatch(name),
                    "Invalid skill name")
            require(entry["source"] == source and name not in names,
                    "Invalid source or duplicate skill selection")
            names.add(name)


def validate_local_skill(marker, name):
    require(marker.is_file() and not marker.is_symlink(),
            f"Local skill must be an owned regular file: {marker}")
    text = marker.read_text()
    match = re.fullmatch(r"---\n(.*?)\n---\n\n(.+)\n", text, re.S)
    require(match is not None, f"Invalid skill frontmatter/body: {marker}")
    lines = match[1].splitlines()
    require(len(lines) == 2 and lines[0] == f"name: {name}"
            and lines[1].startswith("description: "),
            f"Expected single-line name, description (shared spec subset): {marker}")
    require(1 <= len(lines[1][13:]) <= 1024 and lines[1][13:].strip(),
            f"Invalid description: {marker}")


def safe_parents(root, destination):
    require(destination.is_relative_to(root), "Destination escapes repository")
    for parent in destination.parents:
        if parent == root:
            break
        require(not parent.is_symlink(), f"Refusing symlinked parent: {parent}")
        require(not parent.exists() or parent.is_dir(), f"Non-directory parent: {parent}")


def checked_source(path, package, *, tree=False):
    """Check resolved resources, including nested symlinks, before projecting them."""
    boundary = package.resolve(strict=True)
    seen = set()

    def visit(item):
        resolved = item.resolve(strict=True)
        require(resolved.is_relative_to(boundary), f"Source link escapes Codex package: {item}")
        require(resolved.is_file() or resolved.is_dir(), f"Unsupported source resource: {item}")
        if tree and resolved.is_dir() and resolved not in seen:
            seen.add(resolved)
            for child in sorted(resolved.iterdir()):
                visit(child)

    visit(path)
    return path


def read_source_json(path, package):
    checked_source(path, package)
    require(path.is_file(), f"Expected source JSON file: {path}")
    value = json.loads(path.read_text())
    require(isinstance(value, dict), f"Expected source JSON object: {path}")
    return value


def bundle_names(entries, kind):
    require(isinstance(entries, list), f"Bundle {kind} must be an array")
    names = set()
    for entry in entries:
        if isinstance(entry, dict):
            require(set(entry) == {"name", "source"} and entry["source"] == "codex",
                    f"Only Codex bundle {kind} sources are supported")
            entry = entry["name"]
        require(isinstance(entry, str) and len(entry) <= 64 and NAME.fullmatch(entry),
                f"Unsafe bundle {kind} name")
        require(entry not in names, f"Duplicate bundle {kind} name: {entry}")
        names.add(entry)
    return names


def baseline_assets(package):
    bundle = read_source_json(package / "bundles/baseline.json", package)
    require(set(bundle) <= {"id", "description", "metadata", "publicSafe", "components",
                            "includes", "extends", "packages"}
            and bundle.get("id") == "baseline", "Unsupported baseline catalog shape")
    for key in ("extends", "packages"):
        require(bundle.get(key, []) == [], f"Unsupported active bundle asset class: {key}")
    components = bundle.get("components")
    require(isinstance(components, dict)
            and set(components) <= {"skills", "agents", "knowledge", "tasks"},
            "Unsupported bundle component classes")
    for key in ("knowledge", "tasks"):
        require(components.get(key, []) == [], f"Unsupported active bundle asset class: {key}")
    skills = bundle_names(components.get("skills", []), "skills")
    agents = bundle_names(components.get("agents", []), "agents")
    includes = bundle.get("includes", [])
    require(isinstance(includes, list) and all(isinstance(p, str) and p in BASELINE_INCLUDES
                                             for p in includes),
            "Unsafe or unsupported baseline include path")
    require(len(includes) == len(set(includes)), "Duplicate baseline includes")
    return skills, agents, includes


def validate_include(path, package, name):
    checked_source(path, package)
    require(path.is_file(), f"Expected include file: {path}")
    if not name.endswith(".json"):
        return
    value = read_source_json(path, package)
    if name == "mcp.json":
        require(set(value) <= {"mcpServers", "metadata"} and value.get("mcpServers") == {},
                "Baseline MCP configuration must have empty mcpServers")
    elif name == "dotagents-settings.json":
        require(set(value) <= {"enabled", "notes", "profile"} and value.get("enabled") is False,
                "Baseline workspace settings must remain disabled")
    elif name == "models.json":
        profiles = value.get("profiles")
        require(set(value) <= {"defaultProfile", "metadata", "profiles"}
                and isinstance(profiles, dict) and isinstance(value.get("defaultProfile"), str)
                and value["defaultProfile"] in profiles
                and all(isinstance(profile, dict) and set(profile) == {"description", "policy"}
                        and all(isinstance(text, str) for text in profile.values())
                        for profile in profiles.values()),
                "Baseline models must remain policy-only profiles")
    elif name == "layouts/ui.json":
        require(set(value) == {"layout", "panels"} and value["layout"] == "default"
                and value["panels"] == [], "Unsupported active baseline layout")


def validate_agent(source, package, name):
    checked_source(source, package, tree=True)
    require(source.is_dir() and {p.name for p in source.iterdir()} == {"agent.md", "config.json"}
            and (source / "agent.md").is_file(), f"Unsupported agent definition: {name}")
    config = read_source_json(source / "config.json", package)
    connection = config.get("connection")
    require(set(config) <= {"$comment", "connection", "modelConfig", "toolConfig", "metadata"}
            and isinstance(connection, dict)
            and set(connection) <= {"delegationKey", "type", "trigger"}
            and connection.get("type") == "internal"
            and connection.get("delegationKey") == name
            and ("trigger" not in connection or connection["trigger"] == {
                "kind": "manual", "events": ["human.delegated"]}),
            f"Agent must be internal and non-auto-run: {name}")


def plan_links(root, manifest, package, local_only=False):
    validate_manifest(manifest)
    canonical = root / ".agents/skills"
    locals_ = {item["name"] for item in manifest["localOverrides"]["skills"]}
    selected = locals_ | {item["name"] for item in manifest["skills"]}
    links = {}
    warnings = []
    agents, includes = set(), []
    if manifest["imports"]:
        if local_only or not package.is_dir():
            warnings.append("Optional bundle unavailable/skipped: baseline (skills, agents, includes)")
        else:
            skills, agents, includes = baseline_assets(package)
            selected |= skills
    for name in sorted(selected):
        folder = canonical / name
        marker = folder / "skill.md"
        safe_parents(root, marker)
        if name in locals_ or (marker.is_file() and not marker.is_symlink()):
            validate_local_skill(marker, name)
            links[folder / "SKILL.md"] = marker
        else:
            if local_only or not package.is_dir():
                warnings.append(f"Optional import unavailable/skipped: {name}")
                continue
            checked_source(package / "skills", package)
            matches = sorted(p for p in package.glob(f"skills/**/{name}/skill.md")
                             if p.is_file())
            require(len(matches) == 1, f"Expected one Codex source for {name}, got {len(matches)}")
            source = checked_source(matches[0].parent, package, tree=True)
            for item in sorted(source.iterdir()):
                if item.name in {"SKILL.md", ".materialized-skill", "PROVENANCE.md"}:
                    continue
                links[folder / item.name] = item
            links[folder / "SKILL.md"] = marker
        for runtime in [".cursor", ".claude"]:
            links[root / runtime / "skills" / name] = folder
    for name in sorted(agents):
        source = package / "agents" / name
        validate_agent(source, package, name)
        folder = root / ".agents/agents" / name
        links[folder] = source
        for runtime in [".cursor", ".claude"]:
            links[root / runtime / "agents" / name] = folder
    for name in includes:
        source = package / name
        validate_include(source, package, name)
        destination = root / ".agents" / name
        safe_parents(root, destination)
        if destination.is_file() and not destination.is_symlink():
            warnings.append(f"Preserving repository-owned include: {name}")
        else:
            links[destination] = source
    return links, warnings


def apply_links(root, links, *, dry_run=False, check=False, relink=False):
    pending = []
    # Preflight the entire plan before writing anything; preserve all owned files.
    for destination, source in links.items():
        safe_parents(root, destination)
        target = os.path.relpath(source, destination.parent)
        if destination.is_symlink():
            if os.readlink(destination) == target:
                continue
            require(relink and not check, f"Link drift (review, then --relink): {destination}")
        else:
            require(not destination.exists(), f"Refusing to overwrite owned path: {destination}")
        pending.append((destination, target))
    require(not check or not pending, f"Missing projections: {len(pending)}; run --dry-run first")
    for destination, target in pending:
        print(f"{'Would link' if dry_run else 'Link'} {destination.relative_to(root)} -> {target}")
        if dry_run:
            continue
        destination.parent.mkdir(parents=True, exist_ok=True)
        temporary = destination.with_name(f".{destination.name}.{uuid.uuid4().hex}.tmp")
        try:
            temporary.symlink_to(target)
            os.replace(temporary, destination)
        finally:
            temporary.unlink(missing_ok=True)
    return len(pending)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--governance", type=Path, help="Override the optional governance checkout path")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true", help="Validate and preview without writing")
    mode.add_argument("--check", action="store_true", help="Read-only manifest, skill, and projection checks")
    parser.add_argument("--local-only", action="store_true", help="Skip optional imported skills and bundle assets")
    parser.add_argument("--relink", action="store_true", help="Explicitly replace drifted symlinks, never owned files")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    manifest_path = root / ".agents/imports.json"
    safe_parents(root, manifest_path)
    require(not manifest_path.is_symlink(), "Manifest must be repository-owned")
    manifest = json.loads(manifest_path.read_text())
    validate_manifest(manifest)
    package = ((args.governance.resolve() / ".agents/codex") if args.governance
               else (manifest_path.parent / manifest["sourcePackage"]).resolve())
    links, warnings = plan_links(root, manifest, package, args.local_only)
    for warning in warnings:
        print(f"WARNING: {warning}", file=sys.stderr)
    changed = apply_links(root, links, dry_run=args.dry_run, check=args.check, relink=args.relink)
    print(f"PASS: manifest subset and local skill schemas; {len(links)} links checked; "
          f"{changed} {'planned' if args.dry_run else 'changed'}; {len(warnings)} warnings")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)
