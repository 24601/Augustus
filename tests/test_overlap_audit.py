from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / ".agents/skills/augustus/scripts/overlap_audit.py"
SPEC = importlib.util.spec_from_file_location("overlap_audit", SCRIPT)
audit = importlib.util.module_from_spec(SPEC)
sys.modules["overlap_audit"] = audit
SPEC.loader.exec_module(audit)


def manifest(fit, confirm):
    return {"schema_version": 1, "partitions": [
        {"name": "fit", "items": fit},
        {"name": "confirm", "confirmation": True, "items": confirm},
    ]}


class OverlapAuditTests(unittest.TestCase):
    def test_a_disjoint_split_is_clean(self):
        result = audit.audit(manifest(
            [{"id": "a", "text": "first"}, {"id": "b", "text": "second"}],
            [{"id": "c", "text": "third"}],
        ))
        self.assertEqual(result["assessment"], "clean")
        self.assertEqual(result["partition_sizes"], {"confirm": 1, "fit": 2})

    def test_identical_text_across_the_confirmation_boundary_is_a_leak(self):
        result = audit.audit(manifest(
            [{"id": "a", "text": "the same sentence"}],
            [{"id": "c", "text": "the same sentence"}],
        ))
        self.assertEqual(result["assessment"], "leak")
        finding = result["confirmation_leaks"][0]
        self.assertEqual(finding["kind"], "identical_text")
        self.assertEqual(finding["partitions"], {"fit": ["a"], "confirm": ["c"]})

    def test_the_leaked_text_is_hashed_not_echoed(self):
        """A leak report must not become a second copy of the data."""
        secret = "a confirmation row nobody should be able to read here"
        result = audit.audit(manifest([{"id": "a", "text": secret}], [{"id": "c", "text": secret}]))
        rendered = json.dumps(result)
        self.assertNotIn(secret, rendered)
        self.assertEqual(result["confirmation_leaks"][0]["text_sha256"],
                         hashlib.sha256(secret.encode("utf-8")).hexdigest())

    def test_the_callers_normalized_text_decides_what_counts_as_the_same_row(self):
        """Normalization is the caller's decision, not this tool's."""
        result = audit.audit(manifest(
            [{"id": "a", "text": "Hello, World!", "normalized_text": "hello world"}],
            [{"id": "c", "text": "hello world", "normalized_text": "hello world"}],
        ))
        self.assertEqual(result["assessment"], "leak")
        self.assertEqual(result["confirmation_leaks"][0]["compared_on"], ["normalized_text"])
        # Without the caller's normalization, these two exact texts differ and
        # the audit says so rather than guessing.
        clean = audit.audit(manifest(
            [{"id": "a", "text": "Hello, World!"}], [{"id": "c", "text": "hello world"}]))
        self.assertEqual(clean["assessment"], "clean")

    def test_a_shared_group_leaks_even_when_no_text_matches(self):
        """Paraphrases and generation families are one unit."""
        result = audit.audit(manifest(
            [{"id": "a", "text": "how do I reset my password", "group": "seed-17"}],
            [{"id": "c", "text": "what is the way to reset a password", "group": "seed-17"}],
        ))
        self.assertEqual(result["assessment"], "leak")
        self.assertEqual(result["confirmation_leaks"][0]["kind"], "shared_group")
        self.assertEqual(result["confirmation_leaks"][0]["key"], "seed-17")

    def test_a_duplicate_id_across_partitions_is_a_leak(self):
        result = audit.audit(manifest(
            [{"id": "shared", "text": "one"}], [{"id": "shared", "text": "two"}]))
        self.assertEqual(result["assessment"], "leak")
        self.assertEqual(result["confirmation_leaks"][0]["kind"], "duplicate_id")

    def test_an_item_with_nothing_to_compare_is_unverifiable_not_clean(self):
        """Fail closed: an audit that cannot see a leak must not report its absence."""
        result = audit.audit(manifest(
            [{"id": "a", "text": "first"}], [{"id": "c"}]))
        self.assertEqual(result["assessment"], "unverifiable")
        self.assertEqual(result["uncheckable_items"], {"confirm": ["c"]})
        self.assertEqual(result["confirmation_leaks"], [])

    def test_a_leak_outranks_unverifiable(self):
        result = audit.audit(manifest(
            [{"id": "a", "text": "same"}], [{"id": "c", "text": "same"}, {"id": "d"}]))
        self.assertEqual(result["assessment"], "leak")
        self.assertEqual(result["uncheckable_items"], {"confirm": ["d"]})

    def test_overlap_between_two_training_partitions_is_reported_but_is_not_a_leak(self):
        document = {"schema_version": 1, "partitions": [
            {"name": "fit", "items": [{"id": "a", "text": "same"}]},
            {"name": "calibration", "items": [{"id": "b", "text": "same"}]},
            {"name": "confirm", "confirmation": True, "items": [{"id": "c", "text": "other"}]},
        ]}
        result = audit.audit(document)
        self.assertEqual(result["assessment"], "clean")
        self.assertEqual(result["confirmation_leaks"], [])
        self.assertEqual(result["other_overlap"][0]["partitions"], {"fit": ["a"], "calibration": ["b"]})

    def test_a_three_way_collision_names_every_partition_and_item(self):
        document = {"schema_version": 1, "partitions": [
            {"name": "fit", "items": [{"id": "a", "text": "same"}, {"id": "a2", "text": "same"}]},
            {"name": "calibration", "items": [{"id": "b", "text": "same"}]},
            {"name": "confirm", "confirmation": True, "items": [{"id": "c", "text": "same"}]},
        ]}
        finding = audit.audit(document)["confirmation_leaks"][0]
        self.assertEqual(finding["partitions"],
                         {"fit": ["a", "a2"], "calibration": ["b"], "confirm": ["c"]})

    def test_malformed_manifests_are_errors_not_findings(self):
        cases = {
            "schema_version": {"schema_version": 2},
            "at least two partitions": {"partitions": [{"name": "only", "items": [{"id": "a"}]}]},
            "confirmation: true": {"partitions": [
                {"name": "fit", "items": [{"id": "a"}]},
                {"name": "dev", "items": [{"id": "b"}]}]},
            "duplicate partition name": {"partitions": [
                {"name": "fit", "items": [{"id": "a"}]},
                {"name": "fit", "confirmation": True, "items": [{"id": "b"}]}]},
            "items must be a nonempty list": {"partitions": [
                {"name": "fit", "items": []},
                {"name": "confirm", "confirmation": True, "items": [{"id": "b"}]}]},
        }
        for message, override in cases.items():
            with self.subTest(case=message):
                document = manifest([{"id": "a", "text": "x"}], [{"id": "c", "text": "y"}])
                document.update(override)
                with self.assertRaisesRegex(ValueError, message):
                    audit.audit(document)

    def test_cli_exits_nonzero_on_a_leak_and_on_unverifiable(self):
        """A pipeline that ignores the body still stops."""
        cases = {
            "clean": (manifest([{"id": "a", "text": "x"}], [{"id": "c", "text": "y"}]), 0),
            "leak": (manifest([{"id": "a", "text": "x"}], [{"id": "c", "text": "x"}]), 1),
            "unverifiable": (manifest([{"id": "a", "text": "x"}], [{"id": "c"}]), 1),
        }
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "manifest.json"
            for name, (document, expected) in cases.items():
                with self.subTest(case=name):
                    path.write_text(json.dumps(document), encoding="utf-8")
                    run = subprocess.run([sys.executable, str(SCRIPT), str(path)],
                                         capture_output=True, text=True)
                    self.assertEqual(run.returncode, expected, run.stderr)
                    self.assertEqual(json.loads(run.stdout)["assessment"], name)
            path.write_text("{not json", encoding="utf-8")
            broken = subprocess.run([sys.executable, str(SCRIPT), str(path)],
                                    capture_output=True, text=True)
            self.assertEqual(broken.returncode, 2)
            self.assertNotIn("Traceback", broken.stderr)


if __name__ == "__main__":
    unittest.main()
