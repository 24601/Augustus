"""Offline checks for the optional Claude plugin-eval suite. No model calls."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest

import yaml


REPO = Path(__file__).resolve().parents[1]
SUITE = REPO / "tests/plugin-evals"
# Documented prompt.md fields; claude plugin eval rejects any other key.
PROMPT_FIELDS = {
    "schema_version", "name", "description", "tags", "plugins", "runs", "expected_outcome",
    "model", "max_turns", "timeout_seconds", "allowed_tools", "append_system_prompt", "env",
}
# The Skill input names the loaded plugin directory (.agents) or the installed plugin.
SKILL_CALLS = ('{"skill":".agents:augustus"}', '{"skill":"augustus:augustus"}', '{"skill":"augustus"}')


def split(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    head, separator, body = text[4:].partition("\n---\n")
    if not text.startswith("---\n") or not separator:
        raise AssertionError(f"{path} needs YAML frontmatter")
    front = yaml.safe_load(head) or {}
    if not isinstance(front, dict):
        raise AssertionError(f"{path} frontmatter must be a mapping")
    return front, body.strip()


class PluginEvalSuiteTests(unittest.TestCase):
    def setUp(self) -> None:
        self.scenarios = json.loads((REPO / "tests/skill_cases.json").read_text(encoding="utf-8"))["cases"]
        self.cases = sorted(path.parent for path in SUITE.glob("*/prompt.md"))

    def test_scenarios_have_unique_ids_and_fixed_fields(self) -> None:
        ids = [scenario["id"] for scenario in self.scenarios]
        self.assertEqual(len(ids), len(set(ids)))
        for scenario in self.scenarios:
            self.assertEqual({"id", "prompt", "expected"}, set(scenario), scenario.get("id"))

    def test_cases_load_the_skill_and_mirror_a_scenario_prompt(self) -> None:
        prompts = {scenario["id"]: scenario["prompt"] for scenario in self.scenarios}
        tags = set()
        self.assertTrue(self.cases)
        for case in self.cases:
            with self.subTest(case=case.name):
                front, body = split(case / "prompt.md")
                self.assertLessEqual(set(front), PROMPT_FIELDS)
                plugins = front.get("plugins")
                self.assertIsInstance(plugins, list)
                self.assertEqual([(REPO / ".agents").resolve()], [(case / path).resolve() for path in plugins])
                self.assertIn("Skill", front.get("allowed_tools", []))
                self.assertIn(front.get("tags"), (["trigger"], ["nontrigger"]))
                tags.update(front["tags"])
                self.assertEqual(prompts.get(case.name), body)
        self.assertEqual({"trigger", "nontrigger"}, tags)

    def test_skill_graders_match_every_namespace_and_scores_stay_comparable(self) -> None:
        for case in self.cases:
            with self.subTest(case=case.name):
                trigger = split(case / "prompt.md")[0]["tags"] == ["trigger"]
                graders = [split(path)[0] for path in sorted((case / "graders").glob("*.md"))]
                skill = [grader for grader in graders if grader.get("type") == "tool_used" and grader.get("tool") == "Skill"]
                self.assertEqual(1, len(skill))
                pattern = re.compile(skill[0]["input_match"])
                for call in SKILL_CALLS:
                    self.assertRegex(call, pattern)
                self.assertNotRegex('{"skill":"other:augustus-notes"}', pattern)
                bounds = (skill[0].get("min"), skill[0].get("max"), skill[0].get("arm"))
                if trigger:
                    # Skill graders are unscored in a two-arm run; score something else.
                    self.assertEqual((None, None, None), bounds)
                    self.assertGreater(len(graders), 1)
                else:
                    self.assertEqual((0, 0, "both"), bounds)


if __name__ == "__main__":
    unittest.main()
