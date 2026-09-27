"""Validate independent arithmetic anchors, frozen evidence, and bad policies."""

import collections
import json
from pathlib import Path
import subprocess
import sys
import tempfile

import build_fixture
import reference

HERE = Path(__file__).resolve().parent


def run_source(source):
    with tempfile.TemporaryDirectory(prefix="dispatch-validation-") as tmp:
        candidate = Path(tmp) / "solution.py"
        candidate.write_text(source)
        proc = subprocess.run([sys.executable, str(HERE / "grade.py"), str(candidate)],
                              capture_output=True, text=True, timeout=70)
        result = json.loads(proc.stdout)
        assert proc.returncode == (0 if result["pass"] else 1), (proc.returncode, result)
        assert not proc.stderr, proc.stderr
        return result


def main():
    config = json.loads((HERE.parent / "public/config.json").read_text())
    history = json.loads((HERE.parent / "public/rows.json").read_text())
    future = json.loads((HERE / "future.json").read_text())
    anchors = json.loads((HERE / "anchors.json").read_text())
    assert len(anchors) == 11
    for a in anchors:
        actual = build_fixture.truth(a["row"], a["ground_transit"], a["cold_transit"])
        assert actual["allowed"] == a["allowed"], a["name"]
        assert actual["loss"] == a["loss"], a["name"]
        assert reference.decide(config, a["row"]) == a["reference_action"], a["name"]
    # Concrete hand calculation: 5 ground arrivals, four late at deadline 4.
    # Ground 6 + 4/5 * 100 = 86; cold 16 + 100 = 116; hold 60 wins.
    lucky = next(a for a in anchors if a["name"] == "lucky-arrival-not-expected-cost")
    assert sum(build_fixture.truth(lucky["row"], t, 2)["loss"]["ground"]
               for t in (3, 4, 5, 6, 7)) / 5 == 86
    for case in future:
        r = case["row"]
        assert not {"historical_action", "observed_transit_hours", "observed_on_time"} & r.keys()
        t = case["actual_transit"]
        assert case == {"row": r, **build_fixture.truth(r, t["ground"], t["cold"])}
    assert [reference.decide(config, c["row"]) for c in future[-4:]] == ["ground", "hold", "hold", "ground"]
    assert all(r["observed_on_time"] is None for r in history if r["historical_action"] == "hold")
    assert all(r["historical_action"] == "hold" for r in history if r["legacy_risk_score"] >= 0.55)
    ref = (HERE / "reference.py").read_text()
    result = {"reference": run_source(ref)}
    assert result["reference"]["pass"]
    assert result["reference"]["safety"]["violations"] == 0
    # Run actual policies, not text checks. Wrappers retain the known safety
    # implementation where appropriate, isolating the decision-design mistake.
    policies = {
        "always_hold": "def fit(rows, config): return {}\ndef decide(a, r): return 'hold'\n",
        "always_cold": "def fit(rows, config): return {}\ndef decide(a, r): return 'cold'\n",
        "always_ground": "def fit(rows, config): return {}\ndef decide(a, r): return 'ground'\n",
        "selected_label_risk_gate": ref + '''
original = decide
def decide(a, r):
    return 'hold' if r['legacy_risk_score'] >= 0.55 else original(a, r)
''',
        "safe_cheapest_freight_ignores_lateness": ref + '''
original = decide
def decide(a, r):
    a = dict(a, late_base=0, late_value_fraction=0)
    return original(a, r)
''',
        "old_release_overrides_revocation": ref + '''
original = decide
def decide(a, r):
    import copy
    r = copy.deepcopy(r)
    r['certificates'] = [x for x in r['certificates'] if x['revision'] == 1]
    return original(a, r)
''',
        "stale_order_id_cache": ref + '''
original = decide
cache = {}
def decide(a, r):
    if r['order_id'] not in cache:
        cache[r['order_id']] = original(a, r)
    return cache[r['order_id']]
''',
    }
    for name, source in policies.items():
        result[name] = run_source(source)
        assert not result[name]["pass"], (name, result[name])
    contracts = {
        "non_json_artifact": "def fit(r,c): return {1,2}\n",
        "non_finite_artifact": "def fit(r,c): return float('nan')\n",
        "fit_global_not_restored": "def fit(r,c):\n global fitted\n fitted = 'hold'\n return c\ndef decide(a,r): return fitted\n",
        "invalid_action": "def fit(r,c): return {}\ndef decide(a,r): return 'approve'\n",
    }
    for name, source in contracts.items():
        result[name] = run_source(source)
        assert not result[name]["pass"] and result[name]["errors"], name
        assert result[name]["cost"] is None and result[name]["safety"]["evaluated"] == 0, name
    assert "NameError" in result["fit_global_not_restored"]["errors"][0]
    result["anchors_passed"] = len(anchors)
    result["future_rows"] = len(future)
    result["historical_actions"] = dict(collections.Counter(r["historical_action"] for r in history))
    result["reference_actions"] = dict(collections.Counter(reference.decide(config, c["row"]) for c in future))
    result["fixed_ceiling"] = config["maximum_mean_cost"]
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
