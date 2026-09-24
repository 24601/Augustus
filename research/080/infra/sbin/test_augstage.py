"""Tests for the acquisition custody tool. Stdlib only."""

from __future__ import annotations

import hashlib
import importlib.machinery
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parent / "augstage"
SPEC = importlib.util.spec_from_loader(
    "augstage", importlib.machinery.SourceFileLoader("augstage", str(SCRIPT)))
augstage = importlib.util.module_from_spec(SPEC)
sys.modules["augstage"] = augstage
SPEC.loader.exec_module(augstage)


class WeightsPublicationTests(unittest.TestCase):
    def tree(self, files):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        root = Path(directory.name)
        for name, content in files.items():
            path = root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content)
        manifest = {"files": {name: hashlib.sha256(content).hexdigest()
                              for name, content in files.items()}}
        return root, manifest

    def test_a_clean_weights_tree_publishes(self):
        root, manifest = self.tree({"model.safetensors": b"w", "config.json": b"{}"})
        report = augstage.check_weights(root, "Qwen/Qwen3-1.7B", {"Qwen/Qwen3-1.7B"}, manifest)
        self.assertTrue(report["publishable"])
        self.assertEqual(report["files"], 2)

    def test_a_dataset_file_under_the_weights_root_is_refused(self):
        """The exact failure the two-root split exists to catch."""
        root, manifest = self.tree({"model.safetensors": b"w", "train-00000.parquet": b"rows"})
        report = augstage.check_weights(root, "Qwen/Qwen3-1.7B", {"Qwen/Qwen3-1.7B"}, manifest)
        self.assertFalse(report["publishable"])
        self.assertIn({"check": "dataset_file_under_weights_root",
                       "file": "train-00000.parquet"}, report["problems"])

    def test_a_repo_outside_the_design_lock_is_refused(self):
        root, manifest = self.tree({"model.safetensors": b"w"})
        report = augstage.check_weights(root, "someone/else", {"Qwen/Qwen3-1.7B"}, manifest)
        self.assertFalse(report["publishable"])
        self.assertEqual(report["problems"][0]["check"], "repo_id_not_in_design_lock")

    def test_a_tampered_file_fails_its_digest(self):
        root, manifest = self.tree({"model.safetensors": b"w"})
        (root / "model.safetensors").write_bytes(b"tampered")
        report = augstage.check_weights(root, "r/x", {"r/x"}, manifest)
        self.assertEqual(report["problems"][0]["check"], "digest_mismatch")

    def test_a_file_absent_from_the_manifest_is_refused(self):
        root, manifest = self.tree({"model.safetensors": b"w"})
        (root / "extra.safetensors").write_bytes(b"surprise")
        report = augstage.check_weights(root, "r/x", {"r/x"}, manifest)
        self.assertIn("file_not_in_acquisition_manifest",
                      [problem["check"] for problem in report["problems"]])


class PartitionTests(unittest.TestCase):
    def publish(self, rows, *, confirmation=True, labels=("label",)):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        root = Path(directory.name)
        source = root / "rows.json"
        source.write_text(json.dumps(rows), encoding="utf-8")
        record = augstage.publish_partition(source, root / "stage", root / "ctl",
                                            "confirm", set(labels), confirmation)
        published = json.loads((root / "stage/confirm/rows.json").read_text(encoding="utf-8"))
        return record, published, root

    def test_confirmation_inputs_are_published_without_their_labels(self):
        rows = [{"id": "a", "text": "hello", "label": "toxic"},
                {"id": "b", "text": "world", "label": "clean"}]
        record, published, root = self.publish(rows)
        self.assertEqual(published, [{"id": "a", "text": "hello"}, {"id": "b", "text": "world"}])
        self.assertNotIn("toxic", json.dumps(published))
        self.assertEqual(record["label_columns_removed"], ["label"])

    def test_the_labels_are_retained_under_ctl_for_the_grader(self):
        rows = [{"id": "a", "text": "hello", "label": "toxic"}]
        _, _, root = self.publish(rows)
        retained = json.loads((root / "ctl/confirm-labels.json").read_text(encoding="utf-8"))
        self.assertEqual(retained, [{"id": "a", "label": "toxic"}])

    def test_a_non_confirmation_partition_keeps_its_labels(self):
        rows = [{"id": "a", "text": "hello", "label": "toxic"}]
        _, published, root = self.publish(rows, confirmation=False)
        self.assertEqual(published, rows)
        self.assertFalse((root / "ctl").exists())

    def test_a_row_without_an_id_is_refused_because_a_label_cannot_rejoin_it(self):
        with self.assertRaisesRegex(ValueError, "needs an id"):
            self.publish([{"text": "hello", "label": "toxic"}])

    def test_several_label_columns_are_all_removed(self):
        rows = [{"id": "a", "text": "t", "label": "x", "gold": "y", "rationale": "z"}]
        _, published, _ = self.publish(rows, labels=("label", "gold"))
        self.assertEqual(published, [{"id": "a", "text": "t", "rationale": "z"}])


if __name__ == "__main__":
    unittest.main()
