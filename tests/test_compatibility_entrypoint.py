from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / ".agents/skills/augustus/scripts/uniqueness_gate.py"


class CompatibilityEntryPointTests(unittest.TestCase):
    def test_repository_entrypoint_runs_the_structural_checker(self):
        result = subprocess.run([sys.executable, str(SCRIPT)], capture_output=True, text=True)
        self.assertEqual(0, result.returncode, result.stderr + result.stdout)

    def test_installed_copy_explains_the_repository_boundary(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "augustus/scripts/uniqueness_gate.py"
            target.parent.mkdir(parents=True)
            shutil.copyfile(SCRIPT, target)
            result = subprocess.run([sys.executable, str(target)], capture_output=True, text=True)
        self.assertNotEqual(0, result.returncode)
        self.assertIn("repository-maintainer check", result.stderr)
        self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
