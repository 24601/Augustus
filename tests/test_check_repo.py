from __future__ import annotations

import json
from pathlib import Path
import sys
import tempfile
import unittest


REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))
from scripts.check_repo import (  # noqa: E402
    MAX_REFERENCE_TOTAL_BYTES,
    check_repository,
)


class RepositoryCheckTests(unittest.TestCase):
    def make_repo(self, *, skill_body: str = "# Augustus\n", version: str = "1.2.3") -> Path:
        tempdir = tempfile.TemporaryDirectory()
        self.addCleanup(tempdir.cleanup)
        root = Path(tempdir.name)
        skill = root / ".agents/skills/augustus/SKILL.md"
        skill.parent.mkdir(parents=True)
        skill.write_text(
            "---\n"
            "name: augustus\n"
            "description: A compact decision-model skill.\n"
            "metadata:\n"
            f"  version: {version}\n"
            "---\n"
            f"{skill_body}",
            encoding="utf-8",
        )
        marketplace = root / ".claude-plugin/marketplace.json"
        marketplace.parent.mkdir(parents=True)
        marketplace.write_text(json.dumps({
            "name": "augustus",
            "owner": {"name": "Fixture contributors"},
            "plugins": [{
                "name": "augustus",
                "description": "A compact decision-model skill.",
                "source": "./.agents",
                "skills": ["./skills/augustus"],
                "strict": False,
                "version": version,
            }],
        }), encoding="utf-8")
        ui = skill.parent / "agents" / "openai.yaml"
        ui.parent.mkdir()
        ui.write_text(
            "interface:\n"
            "  display_name: Augustus\n"
            "  short_description: Design and evaluate model judgments\n"
            "  default_prompt: Use $augustus for a bounded placement.\n",
            encoding="utf-8",
        )
        (root / "README.md").write_text("# Augustus\n", encoding="utf-8")
        return root

    def codes(self, root: Path) -> set[str]:
        return {issue.code for issue in check_repository(root)}

    def test_clean_minimal_fixture_passes(self) -> None:
        self.assertEqual([], check_repository(self.make_repo()))

    def test_broken_link_is_reported_but_code_example_is_not_scanned(self) -> None:
        root = self.make_repo(skill_body="[missing](not-a-reference.md)\n```md\n[example](also-missing.md)\n```\n")
        self.assertEqual({"broken-link"}, self.codes(root))

    def test_version_mismatch_is_reported(self) -> None:
        root = self.make_repo()
        marketplace = root / ".claude-plugin/marketplace.json"
        data = json.loads(marketplace.read_text(encoding="utf-8"))
        data["plugins"][0]["version"] = "9.9.9"
        marketplace.write_text(json.dumps(data), encoding="utf-8")
        self.assertIn("version-mismatch", self.codes(root))

    def test_marketplace_root_name_and_owner_are_required(self) -> None:
        root = self.make_repo()
        marketplace = root / ".claude-plugin/marketplace.json"
        data = json.loads(marketplace.read_text(encoding="utf-8"))
        data.pop("name")
        data.pop("owner")
        marketplace.write_text(json.dumps(data), encoding="utf-8")
        codes = self.codes(root)
        self.assertIn("marketplace-name", codes)
        self.assertIn("marketplace-owner", codes)

    def test_marketplace_source_and_skill_paths_must_be_contained_and_real(self) -> None:
        root = self.make_repo()
        marketplace = root / ".claude-plugin/marketplace.json"
        data = json.loads(marketplace.read_text(encoding="utf-8"))
        plugin = data["plugins"][0]
        plugin["source"] = "../outside"
        marketplace.write_text(json.dumps(data), encoding="utf-8")
        self.assertIn("marketplace-source", self.codes(root))

        root = self.make_repo()
        marketplace = root / ".claude-plugin/marketplace.json"
        data = json.loads(marketplace.read_text(encoding="utf-8"))
        data["plugins"][0]["skills"] = ["../outside"]
        marketplace.write_text(json.dumps(data), encoding="utf-8")
        self.assertIn("marketplace-skill", self.codes(root))

        root = self.make_repo()
        marketplace = root / ".claude-plugin/marketplace.json"
        data = json.loads(marketplace.read_text(encoding="utf-8"))
        data["plugins"][0]["skills"] = ["./skills/missing"]
        marketplace.write_text(json.dumps(data), encoding="utf-8")
        self.assertIn("marketplace-skill", self.codes(root))

    def test_skill_and_reference_budget_overruns_are_reported(self) -> None:
        root = self.make_repo(skill_body="# Augustus\n" + ("x" * 16_100))
        self.assertIn("size-budget", self.codes(root))

    def test_manifest_free_plugin_requires_explicit_marketplace_authority(self) -> None:
        root = self.make_repo()
        path = root / ".claude-plugin/marketplace.json"
        data = json.loads(path.read_text())
        data["plugins"][0].pop("strict")
        path.write_text(json.dumps(data))
        self.assertIn("marketplace-manifest", self.codes(root))

        root = self.make_repo(skill_body="# Augustus\n`references/guide.md`\n")
        reference = root / ".agents/skills/augustus/references/guide.md"
        reference.parent.mkdir(parents=True)
        reference.write_text("# Guide\n" + ("x" * 18_100), encoding="utf-8")
        self.assertIn("size-budget", self.codes(root))

    def test_aggregate_reference_budget_is_reported(self) -> None:
        links = []
        root = self.make_repo()
        reference_dir = root / ".agents/skills/augustus/references"
        reference_dir.mkdir(parents=True)
        for number in range(11):
            name = f"guide-{number}.md"
            links.append(f"[guide {number}](references/{name})")
            (reference_dir / name).write_text("# Guide " + str(number) + "\n" + ("x" * 16_500), encoding="utf-8")
        skill = root / ".agents/skills/augustus/SKILL.md"
        skill.write_text(skill.read_text(encoding="utf-8") + "\n".join(links) + "\n", encoding="utf-8")
        self.assertGreater(MAX_REFERENCE_TOTAL_BYTES, 0)
        self.assertIn("reference-total-budget", self.codes(root))

    def test_unlinked_reference_and_long_cross_card_copy_are_reported(self) -> None:
        root = self.make_repo(skill_body="# Augustus\n`references/first.md`\n")
        reference_dir = root / ".agents/skills/augustus/references"
        reference_dir.mkdir(parents=True)
        repeated = "This deliberately long paragraph is duplicate runtime prose. " * 4
        (reference_dir / "first.md").write_text("# First\n\n" + repeated + "\n", encoding="utf-8")
        (reference_dir / "second.md").write_text("# Second\n\n" + repeated + "\n", encoding="utf-8")
        codes = self.codes(root)
        self.assertIn("unreferenced-reference", codes)
        self.assertIn("duplicate-paragraph", codes)

    def test_reference_body_links_are_checked(self) -> None:
        root = self.make_repo(skill_body="# Augustus\n[guide](references/guide.md)\n")
        reference = root / ".agents/skills/augustus/references/guide.md"
        reference.parent.mkdir(parents=True)
        reference.write_text("# Guide\n\n[missing](missing.md)\n", encoding="utf-8")
        self.assertIn("broken-link", self.codes(root))

    def test_duplicate_runtime_heading_is_reported(self) -> None:
        root = self.make_repo(skill_body="# Augustus\n## Repeated\n## Repeated\n")
        self.assertIn("duplicate-anchor", self.codes(root))

    def test_runtime_research_heading_is_rejected_in_public_readme(self) -> None:
        root = self.make_repo()
        (root / "README.md").write_text("# Augustus\n## Hourly update\n", encoding="utf-8")
        self.assertIn("runtime-research-heading", self.codes(root))

    def test_ui_manifest_requires_valid_public_fields_and_contained_assets(self) -> None:
        root = self.make_repo()
        ui = root / ".agents/skills/augustus/agents/openai.yaml"
        ui.write_text(
            "interface:\n"
            "  display_name: ''\n"
            "  short_description: too short\n"
            "  default_prompt: Use another skill.\n"
            "  icon_small: ../../outside.svg\n"
            "policy:\n"
            "  allow_implicit_invocation: 'false'\n",
            encoding="utf-8",
        )
        codes = self.codes(root)
        self.assertTrue({"ui-display-name", "ui-short-description", "ui-default-prompt", "ui-policy", "ui-assets"}.issubset(codes))

    def test_ui_optional_invocation_policy_accepts_boolean_not_string(self) -> None:
        root = self.make_repo()
        ui = root / ".agents/skills/augustus/agents/openai.yaml"
        ui.write_text(ui.read_text() + "policy:\n  allow_implicit_invocation: false\n")
        self.assertNotIn("ui-policy", self.codes(root))


if __name__ == "__main__":
    unittest.main()
