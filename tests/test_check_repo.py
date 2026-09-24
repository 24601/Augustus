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
        (root / "README.md").write_text(f"# Augustus\n\nVersion {version}: `git clone --branch v{version}`.\n", encoding="utf-8")
        (root / "CITATION.cff").write_text(f'version: {version}\ndate-released: "2026-01-02"\n', encoding="utf-8")
        (root / "CHANGELOG.md").write_text(f"# Changelog\n\n## [{version}] - 2026-01-02\n", encoding="utf-8")
        notes = root / "docs" / f"release-notes-v{version}.md"
        notes.parent.mkdir()
        notes.write_text("# Release notes\n", encoding="utf-8")
        return root

    def add_skill(self, root: Path, name: str, *, version: str = "1.2.3", body: str = "# Second\n", register: bool = True) -> Path:
        """Add a second skill, optionally registering it in the marketplace."""
        skill = root / f".agents/skills/{name}/SKILL.md"
        skill.parent.mkdir(parents=True)
        skill.write_text(
            "---\n"
            f"name: {name}\n"
            "description: A second compact skill.\n"
            "metadata:\n"
            f"  version: {version}\n"
            "---\n"
            f"{body}",
            encoding="utf-8",
        )
        if register:
            marketplace = root / ".claude-plugin/marketplace.json"
            data = json.loads(marketplace.read_text(encoding="utf-8"))
            data["plugins"][0]["skills"].append(f"./skills/{name}")
            marketplace.write_text(json.dumps(data), encoding="utf-8")
        return skill

    def rewrite_skill(self, root: Path, old: str, new: str) -> None:
        skill = root / ".agents/skills/augustus/SKILL.md"
        text = skill.read_text(encoding="utf-8")
        self.assertIn(old, text)
        skill.write_text(text.replace(old, new, 1), encoding="utf-8")

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

    def test_runtime_links_must_survive_standalone_skill_install(self) -> None:
        root = self.make_repo(skill_body="[repo](../../../README.md)\n[guide](references/guide.md)\n")
        reference = root / ".agents/skills/augustus/references/guide.md"
        reference.parent.mkdir(parents=True)
        reference.write_text("# Guide\n[repo](../../../../README.md)\n")
        issues = [item for item in check_repository(root) if item.code == "broken-link"]
        self.assertEqual(len(issues), 2)
        self.assertTrue(all("escapes" in item.message for item in issues))

    def test_nested_reference_budget_and_links_are_not_skipped(self) -> None:
        root = self.make_repo(skill_body="[guide](references/nested/guide.md)\n")
        reference = root / ".agents/skills/augustus/references/nested/guide.md"
        reference.parent.mkdir(parents=True)
        reference.write_text("# Guide\n[missing](missing.md)\n\n" + "x" * 181000)
        self.assertTrue({"size-budget", "reference-total-budget", "broken-link"}.issubset(self.codes(root)))

    def test_fence_with_trailing_text_does_not_hide_later_real_link(self) -> None:
        root = self.make_repo(skill_body="```md\n```not-closing\n```\n[missing](missing.md)\n")
        self.assertIn("broken-link", self.codes(root))

    def test_semver_accepts_build_and_prerelease_but_rejects_malformed_versions(self) -> None:
        for version in ("1.2.3-rc.1+build.07", "0.0.0", "0.6.1-dev"):
            with self.subTest(version=version):
                self.assertEqual([], check_repository(self.make_repo(version=version)))
        for version in ("01.2.3", "1.2.3-01", "1.2.3-rc..1", "1.2.3+", "1.2.3+build..1"):
            with self.subTest(version=version):
                self.assertTrue({"skill-version", "marketplace-version"}.issubset(self.codes(self.make_repo(version=version))))

    def test_malformed_urls_and_directory_cards_report_issues_not_tracebacks(self) -> None:
        root = self.make_repo(skill_body="[bad](https://[)\n`references/directory.md`\n")
        reference = root / ".agents/skills/augustus/references/directory.md"
        reference.mkdir(parents=True)
        codes = self.codes(root)
        self.assertIn("broken-link", codes)
        self.assertIn("active-reference", codes)
        self.assertIn("unreadable-file", codes)

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

    def test_frontmatter_stays_within_the_portable_skill_spec(self) -> None:
        for old, new, code in (
            ("description: A compact decision-model skill.", "description: Route a <threshold> case.", "skill-description"),
            ("metadata:\n", "when_to_use: Routing requests.\nmetadata:\n", "skill-frontmatter"),
            ("metadata:\n", "compatibility: " + "x" * 501 + "\nmetadata:\n", "skill-compatibility"),
            ("metadata:\n", "metadata:\n  source_commit: 1234567\n", "skill-metadata"),
        ):
            with self.subTest(code=code):
                root = self.make_repo()
                self.rewrite_skill(root, old, new)
                self.assertIn(code, self.codes(root))
        root = self.make_repo()
        self.rewrite_skill(root, "metadata:\n", "license: MIT\ncompatibility: Python 3.11 or later.\nallowed-tools: Read Grep\nmetadata:\n")
        self.assertEqual([], check_repository(root))

    def test_release_version_requires_matching_public_surfaces(self) -> None:
        root = self.make_repo(version="1.2.3")
        (root / "README.md").write_text("# Augustus\n\n`git clone --branch v1.2.2`\n", encoding="utf-8")
        (root / "CITATION.cff").write_text('version: 1.2.2\ndate-released: "2026-01-01"\n', encoding="utf-8")
        (root / "docs/release-notes-v1.2.3.md").unlink()
        (root / "docs/index.md").write_text("# Home\n\nCurrent release: release-notes-v1.2.2.html\n", encoding="utf-8")
        messages = [issue.message for issue in check_repository(root) if issue.code == "release-parity"]
        for expected in ("pinned v1.2.3 install", "'1.2.2' != skill version '1.2.3'", "2026-01-02 != CITATION date-released 2026-01-01",
                         "release notes", "release-notes-v1.2.3.html"):
            with self.subTest(expected=expected):
                self.assertTrue(any(expected in message for message in messages), messages)

    def test_release_readme_may_pin_with_marketplace_or_tree_url(self) -> None:
        for readme in ("claude plugin marketplace add o/r@v1.2.3\n",
                       "npx skills add https://github.com/o/r/tree/v1.2.3/.agents/skills/x\n"):
            with self.subTest(readme=readme):
                root = self.make_repo(version="1.2.3")
                (root / "README.md").write_text("# Augustus\n\n" + readme, encoding="utf-8")
                self.assertNotIn("release-parity", self.codes(root))

    def test_development_version_is_named_in_readme_and_skips_release_surfaces(self) -> None:
        root = self.make_repo(version="1.2.4-dev")
        (root / "CITATION.cff").write_text('version: 1.2.3\ndate-released: "2026-01-01"\n', encoding="utf-8")
        (root / "docs/release-notes-v1.2.4-dev.md").unlink()
        self.assertEqual([], check_repository(root))
        (root / "README.md").write_text("# Augustus\n\nPublished release: 1.2.3.\n", encoding="utf-8")
        self.assertEqual({"release-parity"}, self.codes(root))

    def test_ui_optional_invocation_policy_accepts_boolean_not_string(self) -> None:
        root = self.make_repo()
        ui = root / ".agents/skills/augustus/agents/openai.yaml"
        ui.write_text(ui.read_text() + "policy:\n  allow_implicit_invocation: false\n")
        self.assertNotIn("ui-policy", self.codes(root))

    def test_second_registered_skill_passes_and_is_budgeted_on_its_own(self) -> None:
        root = self.make_repo()
        skill = self.add_skill(root, "augustus-train")
        self.assertEqual([], check_repository(root))
        reference = skill.parent / "references" / "recipes.md"
        reference.parent.mkdir()
        reference.write_text("# Recipes\n\n" + "x " * 10_000 + "\n", encoding="utf-8")
        skill.write_text(skill.read_text(encoding="utf-8") + "\nSee `references/recipes.md`.\n", encoding="utf-8")
        codes = self.codes(root)
        self.assertIn("size-budget", codes)
        self.assertNotIn("unreferenced-reference", codes)

    def test_unregistered_second_skill_is_reported(self) -> None:
        root = self.make_repo()
        self.add_skill(root, "augustus-train", register=False)
        self.assertEqual({"marketplace-skill"}, self.codes(root))

    def test_skills_must_share_one_version(self) -> None:
        root = self.make_repo(version="1.2.3")
        self.add_skill(root, "augustus-train", version="1.2.4")
        self.assertIn("version-mismatch", self.codes(root))

    def test_skill_name_must_match_its_directory(self) -> None:
        root = self.make_repo()
        skill = self.add_skill(root, "augustus-train")
        skill.write_text(skill.read_text(encoding="utf-8").replace("name: augustus-train", "name: augustus-trainer"), encoding="utf-8")
        self.assertIn("skill-name", self.codes(root))

    def test_a_skill_without_a_ui_manifest_is_not_an_error(self) -> None:
        root = self.make_repo()
        self.add_skill(root, "augustus-train")
        self.assertNotIn("missing-file", self.codes(root))

    def test_a_card_copied_between_skills_is_a_duplicate(self) -> None:
        root = self.make_repo()
        paragraph = ("This paragraph is long enough to be compared across skills, "
                     "so copying it from one reference card into another is reported. " * 2)
        first = root / ".agents/skills/augustus/references/shared.md"
        first.parent.mkdir(parents=True)
        first.write_text(f"# Shared\n\n{paragraph}\n", encoding="utf-8")
        self.rewrite_skill(root, "# Augustus\n", "# Augustus\n\nSee `references/shared.md`.\n")
        skill = self.add_skill(root, "augustus-train", body="# Second\n\nSee `references/shared.md`.\n")
        copied = skill.parent / "references" / "shared.md"
        copied.parent.mkdir()
        copied.write_text(f"# Shared\n\n{paragraph}\n", encoding="utf-8")
        self.assertIn("duplicate-paragraph", self.codes(root))


if __name__ == "__main__":
    unittest.main()
