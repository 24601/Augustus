"""Independent arithmetic and serving checks; no additional model selection."""
import importlib.metadata
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import joblib
import numpy as np

from journey import ROOT, WORK, group_losses, losses, metrics, read, write
from sms import action, digest, infer, load


class Checks(unittest.TestCase):
    def test_costs_and_units(self):
        rows = [{"y": 0, "group": 2}, {"y": 1, "group": 2}, {"y": 1, "group": 5}]
        self.assertEqual(losses(np.array([0, 1, 1]), np.array([1, 0, 1])).tolist(), [5, 1, 0])
        self.assertEqual(group_losses(rows, [5, 1, 0]).tolist(), [3, 0])
        result = metrics(rows, np.array([1, 0, 1]))
        self.assertEqual(result["row_loss"], 2)
        self.assertEqual(result["group_loss"], 1.5)
        self.assertEqual(result["spam_recall"], .5)

    def test_splits(self):
        parts = {role: read(WORK / f"{role}.json") for role in ("fit", "search", "confirm")}
        for key in ("id", "group", "text"):
            sets = [set(r[key] for r in rows) for rows in parts.values()]
            for i in range(3):
                for j in range(i):
                    self.assertFalse(sets[i] & sets[j])
        for role, rows in parts.items():
            self.assertEqual({r["y"] for r in rows}, {0, 1})
            self.assertEqual(digest(WORK / f"{role}.json"), read(ROOT / "data-receipt.json")["parts"][role]["sha256"])

    def test_dependencies(self):
        for line in (ROOT / "requirements.lock").read_text().splitlines():
            name, version = line.split("==")
            self.assertEqual(importlib.metadata.version(name), version)

    def test_policy(self):
        self.assertEqual(action(.45, .45), "spam-review")
        self.assertEqual(action(np.nextafter(.45, 0), .45), "ham")
        self.assertEqual(action(np.nextafter(.45, 1), .45), "spam-review")
        self.assertEqual(infer(None, {"text": "hello"})["status"], "artifact_unavailable")
        self.assertEqual(infer({"model": None}, {"text": "hello"})["status"], "incumbent")
        self.assertEqual(infer({"model": object()}, {"text": "hello"})["status"], "inference_failed")

    def test_bad_bundles(self):
        with tempfile.TemporaryDirectory(dir=WORK) as directory:
            path = Path(directory) / "broken.joblib"
            path.write_bytes(b"not a pickle")
            with self.assertRaises(Exception):
                load(path, digest(path))
            joblib.dump({"version": "wrong", "threshold": .5, "model": None}, path)
            with self.assertRaises(ValueError):
                load(path, digest(path))
            command = [sys.executable, str(ROOT / "sms.py"), str(path.parent / "missing"), "--sha256", "0"*64]
            output = subprocess.run(command, input='{"text":"hello"}\n', text=True, capture_output=True, check=True)
            self.assertEqual(json.loads(output.stdout)["status"], "artifact_unavailable")

    def test_isolated_serving_bundle(self):
        # Only the bundle and serving code in cwd. Corpus remains elsewhere, not
        # an OS sandbox; the serving module contains no corpus read or fit path.
        frozen = read(WORK / "frozen.json")
        bundle = WORK / (frozen["trial"] + ".joblib")
        with tempfile.TemporaryDirectory(dir=WORK) as directory:
            d = Path(directory)
            (d / "sms.py").write_bytes((ROOT / "sms.py").read_bytes())
            (d / "model.joblib").write_bytes(bundle.read_bytes())
            output = subprocess.run([sys.executable, "sms.py", "model.joblib", "--sha256", digest(bundle)],
                                    cwd=d, input='{"text":"free prize"}\n{"text":"Meet me at home"}\n',
                                    text=True, capture_output=True, check=True, timeout=5)
            self.assertEqual([json.loads(line)["action"] for line in output.stdout.splitlines()], ["spam-review", "ham"])


if __name__ == "__main__":
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Checks))
    write(ROOT / "verification-receipt.json", {"tests": result.testsRun, "passed": result.wasSuccessful(),
          "verification_source_sha256": digest(Path(__file__)),
          "total_recorded_stage_cpu_seconds": sum(read(p)["stage_cpu_seconds"] for p in ROOT.glob("timing-*.json"))})
    sys.exit(not result.wasSuccessful())
