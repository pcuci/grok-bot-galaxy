"""Run with python3 -B .agents/scripts/test_onboard.py; fixtures stay in .agents."""

import copy
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location("onboard", Path(__file__).with_name("onboard.py"))
onboard = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(onboard)
AGENTS = Path(__file__).resolve().parents[1]


class OnboardingTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix=".onboard-test-", dir=AGENTS)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.package = self.root / "source"
        self.manifest = {
            "version": 2, "sourcePackage": "../source", "imports": [],
            "skills": [{"name": "fs-read", "source": "codex"}],
            "localOverrides": {
                "skills": [{"name": "local-test", "source": "repo"}], "disabledSkills": [],
            },
            "components": ["skills"], "include": [], "exclude": [],
            "x-governance": {"optional": True, "observedRevision": "0" * 40},
        }
        self.local = self.root / ".agents/skills/local-test/skill.md"
        self.local.parent.mkdir(parents=True)
        self.local.write_text("---\nname: local-test\ndescription: Test local skill.\n---\n\n# Test\n")
        self.source = self.package / "skills/core/fs-read/skill.md"
        self.source.parent.mkdir(parents=True)
        self.source.write_text("---\nname: fs-read\ndescription: Test import.\n---\n\n# Read\n")

    def plan(self, **kwargs):
        return onboard.plan_links(self.root, self.manifest, self.package, **kwargs)

    def write_json(self, path, value):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value))

    def baseline(self):
        self.manifest.update(imports=[{"bundle": "baseline"}], skills=[],
                             components=["skills", "agents"])
        self.bundle_path = self.package / "bundles/baseline.json"
        self.bundle = {
            "id": "baseline", "description": "Fixture", "publicSafe": True, "metadata": {},
            "components": {"skills": ["fs-read"], "agents": ["manual-agent", "internal-agent"],
                           "tasks": [], "knowledge": []},
            "includes": sorted(onboard.BASELINE_INCLUDES),
        }
        self.write_json(self.bundle_path, self.bundle)
        for name in self.bundle["components"]["agents"]:
            folder = self.package / "agents" / name
            config = {"connection": {"type": "internal", "delegationKey": name}}
            if name == "manual-agent":
                config["connection"]["trigger"] = {"kind": "manual", "events": ["human.delegated"]}
            self.write_json(folder / "config.json", config)
            (folder / "agent.md").write_text("# Fixture agent\n")
        for name in ("agents.md", "system-prompt.md"):
            (self.package / name).write_text("# Imported guidance\n")
        self.write_json(self.package / "mcp.json", {"mcpServers": {}, "metadata": {}})
        self.write_json(self.package / "dotagents-settings.json", {"enabled": False})
        self.write_json(self.package / "models.json", {
            "defaultProfile": "balanced",
            "profiles": {"balanced": {"description": "Test", "policy": "Current runtime model"}},
        })
        self.write_json(self.package / "layouts/ui.json", {"layout": "default", "panels": []})

    def snapshot(self):
        return {str(p.relative_to(self.root)): (p.readlink().as_posix() if p.is_symlink()
                else p.read_bytes() if p.is_file() else None) for p in self.root.rglob("*")}

    def test_schema(self):
        onboard.validate_manifest(self.manifest)
        for key, value in [("imports", [{"bundle": "baseline"}]),
                           ("components", ["skills", "agents"]), ("version", 1),
                           ("sourcePackage", "/absolute/source"),
                           ("imports", [{"bundle": "../escape"}])]:
            invalid = copy.deepcopy(self.manifest)
            invalid[key] = value
            with self.assertRaises(ValueError):
                onboard.validate_manifest(invalid)
        self.manifest["skills"][0]["name"] = "../../escape"
        with self.assertRaises(ValueError):
            onboard.validate_manifest(self.manifest)

    def test_dry_run_and_idempotence(self):
        links, warnings = self.plan()
        self.assertEqual(warnings, [])
        before = self.snapshot()
        onboard.apply_links(self.root, links, dry_run=True)
        self.assertEqual(before, self.snapshot())
        self.assertGreater(onboard.apply_links(self.root, links), 0)
        after = self.snapshot()
        self.assertEqual(onboard.apply_links(self.root, links, check=True), 0)
        self.assertEqual(onboard.apply_links(self.root, links), 0)
        self.assertEqual(after, self.snapshot())
        for destination in links:
            self.assertTrue(destination.exists())
            self.assertFalse(destination.readlink().is_absolute())

    def test_missing_optional_source(self):
        links, warnings = onboard.plan_links(self.root, self.manifest, self.root / "missing")
        self.assertEqual(len(warnings), 1)
        self.assertEqual(len(links), 3)
        onboard.apply_links(self.root, links)
        self.assertEqual(self.local.read_bytes(), (self.local.parent / "SKILL.md").read_bytes())

    def test_local_only(self):
        links, warnings = self.plan(local_only=True)
        self.assertEqual(len(links), 3)
        self.assertEqual(len(warnings), 1)

    def test_owned_path_conflict_preflights_before_writes(self):
        conflict = self.root / ".claude/skills/local-test"
        conflict.parent.mkdir(parents=True)
        conflict.write_text("human work")
        before = self.snapshot()
        links, _ = self.plan()
        with self.assertRaises(ValueError):
            onboard.apply_links(self.root, links, relink=True)
        self.assertEqual(before, self.snapshot())

    def test_symlink_parent_escape(self):
        outside = self.root / "outside"
        outside.mkdir()
        (self.root / ".cursor").symlink_to(outside)
        links, _ = self.plan()
        before = self.snapshot()
        with self.assertRaises(ValueError):
            onboard.apply_links(self.root, links)
        self.assertEqual(before, self.snapshot())

    def test_local_override_wins(self):
        local = self.root / ".agents/skills/fs-read/skill.md"
        local.parent.mkdir()
        local.write_text("---\nname: fs-read\ndescription: Local override.\n---\n\n# Local\n")
        links, _ = self.plan()
        self.assertNotIn(local, links)
        self.assertEqual(links[local.parent / "SKILL.md"], local)

    def test_relocation_requires_explicit_relink(self):
        links, _ = self.plan()
        onboard.apply_links(self.root, links)
        marker = self.root / ".agents/skills/fs-read/skill.md"
        marker.unlink()
        marker.symlink_to("old-source/skill.md")
        with self.assertRaises(ValueError):
            onboard.apply_links(self.root, links)
        onboard.apply_links(self.root, links, relink=True)
        onboard.apply_links(self.root, links, check=True)
        self.assertEqual(marker.read_bytes(), self.source.read_bytes())

    def test_invalid_local_metadata(self):
        self.local.write_text("---\nname: wrong\ndescription: Bad.\n---\n\n# Test\n")
        with self.assertRaises(ValueError):
            self.plan()

    def test_ambiguous_import_rejected(self):
        duplicate = self.package / "skills/other/fs-read/skill.md"
        duplicate.parent.mkdir(parents=True)
        duplicate.write_text(self.source.read_text())
        with self.assertRaises(ValueError):
            self.plan()

    def test_source_resource_escape_rejected(self):
        (self.source.parent / "outside").symlink_to(self.local)
        with self.assertRaises(ValueError):
            self.plan()

    def test_baseline_selection_and_owned_includes(self):
        self.baseline()
        self.bundle["components"]["skills"] = [{"name": "fs-read", "source": "codex"}]
        self.write_json(self.bundle_path, self.bundle)
        owned = [self.root / ".agents" / name for name in ("agents.md", "system-prompt.md")]
        for path in owned:
            path.write_text("# Repository policy wins\n")
        # Decoys must never be selected by name or expanded as vendor bridges.
        for path in (self.package / "skills/core/unselected/skill.md",
                     self.root / "vendor/skills/fs-read/skill.md",
                     self.root / "source-overrides/skills/fs-read/skill.md",
                     self.package / "agents/unselected/agent.md"):
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("Not selected\n")
        links, warnings = self.plan()
        self.assertEqual(len(links), 17)
        self.assertEqual(len(warnings), 2)
        for path in owned:
            self.assertNotIn(path, links)
        self.assertEqual(links[self.root / ".agents/skills/fs-read/skill.md"], self.source)
        self.assertEqual(links[self.root / ".agents/agents/manual-agent"],
                         self.package / "agents/manual-agent")
        for runtime in (".cursor", ".claude"):
            self.assertEqual(links[self.root / runtime / "agents/manual-agent"],
                             self.root / ".agents/agents/manual-agent")
        self.assertFalse(any("vendor" in str(p) or "unselected" in str(p)
                             or "source-overrides" in str(p) for p in (*links, *links.values())))
        before = self.snapshot()
        onboard.apply_links(self.root, links, dry_run=True)
        self.assertEqual(before, self.snapshot())
        onboard.apply_links(self.root, links)
        after = self.snapshot()
        self.assertEqual(onboard.apply_links(self.root, self.plan()[0], check=True), 0)
        self.assertEqual(onboard.apply_links(self.root, self.plan()[0]), 0)
        self.assertEqual(after, self.snapshot())
        for path in owned:
            self.assertFalse(path.is_symlink())
            self.assertEqual(path.read_text(), "# Repository policy wins\n")
        for path in links:
            self.assertTrue(path.exists())
            self.assertFalse(path.readlink().is_absolute())

    def test_baseline_local_skill_override(self):
        self.baseline()
        self.test_local_override_wins()

    def test_baseline_can_add_explicit_codex_skills(self):
        self.baseline()
        self.bundle["components"]["skills"] = []
        self.write_json(self.bundle_path, self.bundle)
        self.manifest["skills"] = [{"name": "fs-read", "source": "codex"}]
        self.assertEqual(self.plan()[0][self.root / ".agents/skills/fs-read/skill.md"], self.source)

    def test_baseline_without_source_keeps_four_local_skills(self):
        self.baseline()
        names = ["broadcast-ingest", "local-transcribe", "transcript-curate", "event-synthesize"]
        self.manifest["localOverrides"]["skills"] = [{"name": n, "source": "repo"} for n in names]
        for name in names:
            marker = self.root / ".agents/skills" / name / "skill.md"
            marker.parent.mkdir()
            marker.write_text(f"---\nname: {name}\ndescription: Fixture.\n---\n\n# Local\n")
        for package, local_only in ((self.root / "missing", False),
                                    (self.root / "missing", True), (self.package, True)):
            with self.subTest(package=package, local_only=local_only):
                links, warnings = onboard.plan_links(self.root, self.manifest, package, local_only)
                self.assertEqual(len(links), 12)
                self.assertEqual(len(warnings), 1)
                self.assertIn("baseline", warnings[0])
                onboard.apply_links(self.root, links)
                self.assertEqual(onboard.apply_links(self.root, links, check=True), 0)

    def test_baseline_does_not_read_catalog_in_local_only_mode(self):
        self.baseline()
        self.bundle_path.write_text("invalid JSON")
        self.assertEqual(len(self.plan(local_only=True)[0]), 3)
        with self.assertRaises(ValueError):
            self.plan()

    def test_baseline_unsafe_names_and_includes(self):
        self.baseline()
        for kind in ("skills", "agents", "includes"):
            for name in ("../escape", "/absolute", "nested/name", "..", "x\\y"):
                with self.subTest(kind=kind, name=name):
                    bundle = copy.deepcopy(self.bundle)
                    if kind == "includes":
                        bundle[kind] = [name]
                    else:
                        bundle["components"][kind] = [name]
                    self.write_json(self.bundle_path, bundle)
                    before = self.snapshot()
                    with self.assertRaises(ValueError):
                        self.plan()
                    self.assertEqual(before, self.snapshot())

    def test_baseline_rejects_unsupported_asset_classes(self):
        self.baseline()
        mutations = [
            ("extends", ["other"]), ("packages", ["vendor"]),
            ("includes", ["tasks/job.json"]), ("hooks", {"start": "run"}),
            ("components", {"skills": [], "tasks": ["auto"]}),
            ("components", {"skills": [], "knowledge": ["memory"]}),
            ("components", {"skills": [], "commands": ["run"]}),
            ("components", {"skills": [{"name": "fs-read", "source": "vendor"}]}),
            ("components", {"skills": [{"name": "fs-read", "source": "repo"}]}),
        ]
        for key, value in mutations:
            with self.subTest(key=key, value=value):
                bundle = copy.deepcopy(self.bundle)
                bundle[key] = value
                self.write_json(self.bundle_path, bundle)
                with self.assertRaises(ValueError):
                    self.plan()

    def test_baseline_rejects_malformed_or_duplicate_selections(self):
        self.baseline()
        for kind in ("skills", "agents", "includes"):
            for value in (None, {}, "fs-read", [None], ["fs-read", "fs-read"]):
                with self.subTest(kind=kind, value=value):
                    bundle = copy.deepcopy(self.bundle)
                    if kind == "includes":
                        bundle[kind] = value
                    else:
                        bundle["components"][kind] = value
                    self.write_json(self.bundle_path, bundle)
                    with self.assertRaises(ValueError):
                        self.plan()

    def test_baseline_config_activation_rejected(self):
        self.baseline()
        for name, value in (
            ("mcp.json", {"mcpServers": {"runner": {"command": "run"}}}),
            ("mcp.json", {}),
            ("mcp.json", {"mcpServers": {}, "servers": {"runner": {}}}),
            ("dotagents-settings.json", {"enabled": True}),
            ("dotagents-settings.json", {"enabled": 0}),
            ("dotagents-settings.json", {"enabled": False, "onStart": "run"}),
            ("models.json", {"providers": {"remote": {}}}),
            ("layouts/ui.json", {"layout": "default", "panels": ["active"]}),
        ):
            with self.subTest(name=name, value=value):
                path = self.package / name
                original = path.read_text()
                self.write_json(path, value)
                before = self.snapshot()
                with self.assertRaises(ValueError):
                    self.plan()
                self.assertEqual(before, self.snapshot())
                path.write_text(original)

    def test_baseline_agents_reject_auto_run_or_external_connections(self):
        self.baseline()
        path = self.package / "agents/manual-agent/config.json"
        config = json.loads(path.read_text())
        changes = [
            {**config, "schedule": "* * * * *"},
            {"connection": {"type": "external", "delegationKey": "manual-agent"}},
            {"connection": {"type": "internal", "delegationKey": "manual-agent", "autoRun": True}},
            {"connection": {"type": "internal", "delegationKey": "manual-agent", "trigger": None}},
            {"connection": {"type": "internal", "delegationKey": "manual-agent",
                            "trigger": {"kind": "automatic", "events": ["on-start"]}}},
            {"connection": {"type": "internal", "delegationKey": "manual-agent",
                            "trigger": {"kind": "manual", "events": ["on-start"]}}},
        ]
        for value in changes:
            with self.subTest(config=value):
                self.write_json(path, value)
                with self.assertRaises(ValueError):
                    self.plan()

    def test_baseline_source_symlink_escapes(self):
        self.baseline()
        for path in (self.bundle_path, self.package / "agents/manual-agent/config.json",
                     self.package / "mcp.json", self.package / "layouts/ui.json"):
            with self.subTest(path=path):
                content = path.read_bytes()
                path.unlink()
                path.symlink_to(self.local)
                with self.assertRaises(ValueError):
                    self.plan()
                path.unlink()
                path.write_bytes(content)

    def test_nested_source_resource_escape_rejected(self):
        resources = self.source.parent / "references"
        resources.mkdir()
        (resources / "escape.md").symlink_to(self.local)
        with self.assertRaises(ValueError):
            self.plan()

    def test_baseline_agent_and_include_conflicts_preflight(self):
        self.baseline()
        for relative in (".agents/agents/manual-agent", ".cursor/agents/manual-agent",
                         ".claude/agents/manual-agent", ".agents/mcp.json"):
            with self.subTest(relative=relative):
                path = self.root / relative
                path.mkdir(parents=True)
                (path / "owned").write_text("Human work\n")
                before = self.snapshot()
                links, _ = self.plan()
                with self.assertRaises(ValueError):
                    onboard.apply_links(self.root, links, relink=True)
                self.assertEqual(before, self.snapshot())
                (path / "owned").unlink()
                path.rmdir()

    def test_baseline_rejects_symlinked_include_parent(self):
        self.baseline()
        outside = self.root / "outside"
        outside.mkdir()
        (self.root / ".agents/layouts").symlink_to(outside)
        with self.assertRaises(ValueError):
            self.plan()

    def test_baseline_link_drift_needs_relink(self):
        self.baseline()
        links, _ = self.plan()
        onboard.apply_links(self.root, links)
        for relative in (".agents/agents/manual-agent", ".cursor/agents/manual-agent",
                         ".agents/mcp.json"):
            with self.subTest(relative=relative):
                path = self.root / relative
                path.unlink()
                path.symlink_to("old-source")
                for kwargs in ({}, {"check": True}, {"check": True, "relink": True}):
                    with self.assertRaises(ValueError):
                        onboard.apply_links(self.root, links, **kwargs)
                onboard.apply_links(self.root, links, relink=True)
                self.assertEqual(onboard.apply_links(self.root, links, check=True), 0)

    def test_baseline_cli_governance_override_and_local_only(self):
        self.baseline()
        script = self.root / ".agents/scripts/onboard.py"
        script.parent.mkdir()
        shutil.copyfile(Path(__file__).with_name("onboard.py"), script)
        self.manifest["sourcePackage"] = "../missing"
        self.write_json(self.root / ".agents/imports.json", self.manifest)
        governance = self.root / "governance"
        package = governance / ".agents/codex"
        package.parent.mkdir(parents=True)
        self.package.rename(package)

        def run(*args):
            return subprocess.run([sys.executable, "-B", str(script), *args], cwd=self.root,
                                  capture_output=True, text=True, timeout=10)

        before = self.snapshot()
        preview = run("--governance", str(governance), "--dry-run")
        self.assertEqual(preview.returncode, 0, preview.stderr)
        self.assertEqual(before, self.snapshot())
        missing = run("--governance", str(governance), "--check")
        self.assertNotEqual(missing.returncode, 0)
        self.assertIn("Missing projections", missing.stderr)
        applied = run("--governance", str(governance))
        self.assertEqual(applied.returncode, 0, applied.stderr)
        for args in (("--governance", str(governance), "--check"), ("--check", "--local-only"),
                     ("--check",)):
            with self.subTest(args=args):
                result = run(*args)
                self.assertEqual(result.returncode, 0, result.stderr)
                if "--governance" not in args:
                    self.assertIn("Optional bundle unavailable/skipped", result.stderr)
        self.write_json(package / "dotagents-settings.json", {"enabled": True})
        invalid = run("--governance", str(governance), "--check")
        self.assertNotEqual(invalid.returncode, 0)
        self.assertIn("settings must remain disabled", invalid.stderr)

    def test_baseline_changed_catalog_is_revalidated(self):
        self.baseline()
        links, _ = self.plan()
        onboard.apply_links(self.root, links)
        self.bundle["components"]["skills"].append("new-skill")
        self.write_json(self.bundle_path, self.bundle)
        with self.assertRaises(ValueError):
            self.plan()
        new_source = self.package / "skills/core/new-skill/skill.md"
        new_source.parent.mkdir(parents=True)
        new_source.write_text("# New Codex skill\n")
        new_links, _ = self.plan()
        with self.assertRaises(ValueError):
            onboard.apply_links(self.root, new_links, check=True)
        onboard.apply_links(self.root, new_links)
        self.assertEqual(onboard.apply_links(self.root, new_links, check=True), 0)
        self.bundle["components"]["tasks"] = ["scheduled"]
        self.write_json(self.bundle_path, self.bundle)
        with self.assertRaises(ValueError):
            self.plan()
        # Removing a selection does not grant deletion authority for its existing links.
        self.bundle["components"]["tasks"] = []
        self.bundle["components"]["skills"] = []
        self.write_json(self.bundle_path, self.bundle)
        onboard.apply_links(self.root, self.plan()[0], check=True)
        self.assertTrue((self.root / ".agents/skills/new-skill/skill.md").exists())


if __name__ == "__main__":
    unittest.main()
