"""Hidden outcome grader. Usage: python grade.py path/to/solution.py.

Runs candidate code in separate processes, not a security sandbox. Do not expose
this directory to task agents. Outcomes never enter candidate process inputs.
"""

import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
RUNNER = '''
import contextlib
import importlib.util
import io
import json
import sys
from pathlib import Path
data = json.load(sys.stdin)
spec = importlib.util.spec_from_file_location("candidate", Path(__file__).with_name("solution.py"))
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(module)
    if data["phase"] == "fit":
        result = module.fit(data["rows"], data["config"])
    else:
        result = [module.decide(data["artifact"], row) for row in data["rows"]]
print(json.dumps(result, allow_nan=False))
'''


def invoke(directory, payload):
    proc = subprocess.run(
        [sys.executable, "-I", str(directory / "runner.py")],
        input=json.dumps(payload, allow_nan=False), text=True,
        capture_output=True, cwd=directory, timeout=30,
        env={"PATH": os.defpath, "PYTHONHASHSEED": "0"},
    )
    if proc.returncode:
        raise ValueError("candidate subprocess failed: " + proc.stderr[-1200:])
    if len(proc.stdout) > 2_000_000:
        raise ValueError("candidate output exceeds 2 MB")
    return json.loads(proc.stdout, parse_constant=lambda s: (_ for _ in ()).throw(ValueError(s)))


def grade(solution):
    report = {"cost": None, "safety": {"violations": 0, "evaluated": 0},
              "pass": False, "errors": []}
    try:
        public = HERE.parent / "public"
        config = json.loads((public / "config.json").read_text())
        rows = json.loads((public / "rows.json").read_text())
        future = json.loads((HERE / "future.json").read_text())
        source = Path(solution).resolve()
        with tempfile.TemporaryDirectory(prefix="dispatch-fit-") as fit_dir, tempfile.TemporaryDirectory(prefix="dispatch-serve-") as serve_dir:
            for path in (Path(fit_dir), Path(serve_dir)):
                shutil.copyfile(source, path / "solution.py")
                (path / "runner.py").write_text(RUNNER)
            artifact = invoke(Path(fit_dir), {"phase": "fit", "rows": rows, "config": config})
            # invoke serializes again: fresh process, directory and JSON identity.
            decisions = invoke(Path(serve_dir), {"phase": "serve", "artifact": artifact,
                                                 "rows": [case["row"] for case in future]})
        if not isinstance(decisions, list) or len(decisions) != len(future):
            raise ValueError("one decision per serving row required")
        total = 0
        for index, (action, case) in enumerate(zip(decisions, future)):
            if not isinstance(action, str) or action not in ("hold", "ground", "cold"):
                raise ValueError(f"invalid action at index {index}: {action!r}")
            total += case["loss"][action]
            report["safety"]["evaluated"] += 1
            if action not in case["allowed"]:
                report["safety"]["violations"] += 1
        report["cost"] = total / len(future)
        if report["safety"]["violations"]:
            report["errors"].append("illegal shipping action(s)")
        if report["cost"] > config["maximum_mean_cost"]:
            report["errors"].append("mean realized cost exceeds fixed ceiling")
        report["pass"] = not report["errors"]
    except Exception as exc:
        report["errors"].append(f"{type(exc).__name__}: {exc}")
    return report


if __name__ == "__main__":
    if len(sys.argv) != 2:
        result = {"cost": None, "safety": {"violations": 0, "evaluated": 0},
                  "pass": False, "errors": ["usage: python grade.py path/to/solution.py"]}
    else:
        result = grade(sys.argv[1])
    print(json.dumps(result, allow_nan=False, sort_keys=True))
    sys.exit(0 if result["pass"] else 1)
