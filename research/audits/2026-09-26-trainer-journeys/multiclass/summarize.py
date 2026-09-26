"""Compact receipts and post-freeze overlap sensitivity; never changes selection."""
import json
from pathlib import Path
import platform
import subprocess
import sys

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

from experiment import digest, metrics, read, write, HERE


root, output = map(Path, sys.argv[1:])
train, dev, confirm = [read(root / (role + ".json")) for role in ("fit", "dev", "confirm")]
predictions = read(root / "confirmation/predictions.json")
assert [r["id"] for r in confirm] == [r["id"] for r in predictions]
vectorizer = TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 3), max_features=30000)
fit = vectorizer.fit_transform([r["text"] for r in train])
search = vectorizer.transform([r["text"] for r in dev])
test = vectorizer.transform([r["text"] for r in confirm])
near = []
for start in range(0, test.shape[0], 100):
    batch = test[start:start + 100]
    maxima = np.maximum((batch @ fit.T).max(axis=1).toarray().ravel(),
                        (batch @ search.T).max(axis=1).toarray().ravel())
    near.extend(maxima >= .95)
near = np.array(near)
slices = {}
for name, mask in (("near_fit_or_dev_cosine_ge_0.95", near), ("remaining", ~near)):
    rows = [r for r, keep in zip(confirm, mask) if keep]
    result = [r for r, keep in zip(predictions, mask) if keep]
    slices[name] = {k: v for k, v in metrics(rows, result).items() if k != "per_intent"}
    # This slice may lack some labels: fixed-taxonomy weighted_cost would then
    # have incomplete probability mass, so do not report it for this diagnostic.
    del slices[name]["weighted_cost"]
audit = read(root / "audit.json")
summary = read(root / "confirmation-summary.json")
search_summary = read(root / "search-summary.json")
trials = read(root / "search/trials.json")
receipt = {
    "evidence_kind": "Reproduced CLINC150 application proxy, not production or causal evidence",
    "environment": {"python": platform.python_version(), "platform": platform.platform(), "device": "CPU", "numerical_threads": 1},
    "provenance": read(root / "provenance.json"),
    "candidate_skill_files": {p: digest(HERE.parents[3] / p) for p in subprocess.check_output(
        ["git", "ls-files", ".agents/skills"], cwd=HERE.parents[3], text=True).splitlines()},
    "audit": audit,
    "search": {k: v for k, v in search_summary.items() if k != "development"},
    "development": {k: v for k, v in search_summary["development"].items() if k != "per_intent"},
    "trials": [{"candidate": trial["candidate"], "cpu_seconds": trial["cpu_seconds"],
                "features": trial["features"], "policy_count": len(trial["policies"]),
                "best_eligible": min((p for p in trial["policies"] if p["oos_misroute_rate"] <= .2),
                                     key=lambda p: (p["weighted_cost"], -p["policy"]["gap"], -p["policy"]["top"]))}
               for trial in trials],
    "confirmation": summary,
    "post_freeze_overlap_sensitivity": {"slices": slices,
        "limits": "Descriptive only, no model/policy changes. Remaining rows are not proven independent semantic families. Near slice intentionally retained as labeled diagnostics."},
    "interface": read(root / "interface-checks.json"),
    "generated_sha256": {str(p.relative_to(root)): digest(p) for p in [
        root / "taxonomy.json", root / "search/trials.json", root / "confirmation/predictions.json"]},
}
write(output, receipt)
print(json.dumps({"decision": summary["decision"], "confirmation_cost": summary["metrics"]["mean_cost"],
                  "sensitivity": slices}, indent=2))
