"""Separate preparation, bounded search, frozen confirmation; outputs outside Git."""
import os
for variable in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[variable] = "1"

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import resource
import shutil
import subprocess
import sys
import time
import unicodedata
import urllib.request
import warnings

import joblib
import numpy as np
from sklearn.exceptions import ConvergenceWarning
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import FeatureUnion
from sklearn.svm import LinearSVC

from router import Router, decide, review

HERE = Path(__file__).resolve().parent
CONTRACT = json.loads((HERE / "contract.json").read_text())


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write(path, value):
    Path(path).write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")


def read(path):
    return json.loads(Path(path).read_text())


def normalize(text):
    return " ".join(re.findall(r"\w+", unicodedata.normalize("NFKC", text).casefold()))


def prepare(root):
    root.mkdir(parents=True, exist_ok=False)
    source = root / "source"
    source.mkdir()
    revision = CONTRACT["source_commit"]
    provenance = {"repository": "https://github.com/clinc/oos-eval", "revision": revision,
                  "retrieved_at": datetime.now(timezone.utc).isoformat(), "files": {}}
    for name in ("README.md", "LICENSE", "data/data_full.json"):
        url = f"https://raw.githubusercontent.com/clinc/oos-eval/{revision}/{name}"
        dest = source / Path(name).name
        with urllib.request.urlopen(url, timeout=60) as response:
            dest.write_bytes(response.read())
        provenance["files"][name] = {"url": url, "sha256": digest(dest)}
    provenance["license"] = "CC BY 3.0 Unported; retained verbatim in source/LICENSE"
    provenance["attribution"] = "Larson et al. (2019), An Evaluation Dataset for Intent Classification and Out-of-Scope Prediction, https://aclanthology.org/D19-1131/"
    provenance["changes"] = "Normalized-duplicate removal; labels unchanged; training-only TF-IDF features"
    provenance["skill_sha256"] = {str(p.relative_to(HERE.parents[3])): digest(p)
        for p in (HERE.parents[3] / ".agents/skills").glob("*/SKILL.md")}
    data = read(source / "data_full.json")
    labels = sorted({label for _, label in data["train"]})
    assert len(labels) == 150 and "oos" not in labels
    write(root / "taxonomy.json", {label: {"action": "route", "queue": "support." + label,
        "operator_task": "Triage the " + label.replace("_", " ") + " request; obtain required context and authorization before any effect."} for label in labels})
    seen, splits, removed = {}, {}, []
    raw_counts = {key: len(value) for key, value in data.items()}
    for role, original in (("fit", "train"), ("dev", "val"), ("confirm", "test")):
        rows = []
        for part in (original, "oos_" + original):
            for index, (text, label) in enumerate(data[part]):
                assert isinstance(text, str) and text.strip() and label in labels + ["oos"]
                row = {"id": f"{part}:{index}", "text": text, "label": label}
                norm = normalize(text)
                if norm in seen:
                    removed.append({"id": row["id"], "owner": seen[norm][0],
                                    "conflicting_label": label != seen[norm][1]})
                else:
                    seen[norm] = (row["id"], label)
                    rows.append(row)
        splits[role] = rows
        write(root / (role + ".json"), rows)
    # Diagnostic near-duplicate audit. Never exposes confirmation utterances/scores
    # to search. Similarity does not establish paraphrase-family independence.
    vectorizer = TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 3), max_features=30000)
    fit = vectorizer.fit_transform([r["text"] for r in splits["fit"]])
    near = {}
    for role in ("dev", "confirm"):
        matrix = vectorizer.transform([r["text"] for r in splits[role]])
        maxima = []
        for start in range(0, matrix.shape[0], 100):
            maxima.extend((matrix[start:start + 100] @ fit.T).max(axis=1).toarray().ravel())
        near[role] = {"cosine_ge_0.95_vs_fit": int(np.sum(np.array(maxima) >= .95)),
                      "max_cosine": float(max(maxima))}
    audit = {"raw_counts": raw_counts, "removed": removed,
             "retained_counts": {k: len(v) for k, v in splits.items()},
             "label_counts": {k: dict(Counter(r["label"] for r in v)) for k, v in splits.items()},
             "near_duplicate_diagnostic": near, "normalization": "NFKC, casefold, Unicode word tokens, join spaces",
             "limits": "No seed/worker/time identifiers; paraphrase siblings and source label noise remain unknown. No independent relabeling.",
             "split_sha256": {k: digest(root / (k + ".json")) for k in splits}}
    write(root / "audit.json", audit)
    write(root / "provenance.json", provenance)
    shutil.copyfile(HERE / "contract.json", root / "contract.json")


def costs(labels, results):
    return np.array([.3 if r["action"] == "manual_review" else
                     0. if r["intent"] == y and y != "oos" else 1.
                     for y, r in zip(labels, results)])


def metrics(rows, results):
    labels = [r["label"] for r in rows]
    loss = costs(labels, results)
    counts = Counter(labels)
    weights = np.array([(1000 / 5500 if y == "oos" else 4500 / 5500 / 150) / counts[y]
                        for y in labels])
    routed = np.array([r["action"] == "route" for r in results])
    oos = np.array([y == "oos" for y in labels])
    return {"n": len(rows), "mean_cost": float(loss.mean()),
            "weighted_cost": float(np.dot(loss, weights)), "coverage": float(routed.mean()),
            "misroutes": int((loss == 1).sum()), "reviews": int((~routed).sum()),
            "correct_routes": int((loss == 0).sum()),
            "oos_routed": int(routed[oos].sum()), "oos_n": int(oos.sum()),
            "oos_misroute_rate": float(routed[oos].mean()),
            "per_intent": {y: {"n": counts[y], "correct_route_recall": float(np.mean(loss[np.array(labels) == y] == 0))}
                           for y in sorted(counts) if y != "oos"}}


def features(name):
    word = TfidfVectorizer(ngram_range=(1, 2), max_features=30000, sublinear_tf=True)
    char = TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 5), max_features=30000, sublinear_tf=True)
    return {"word-svc": word, "char-svc": char,
            "word-char-svc": FeatureUnion([("word", word), ("char", char)])}[name]


def fit(root):
    resource.setrlimit(resource.RLIMIT_CPU, (1200, 1200))
    started = time.process_time()
    wall = time.perf_counter()
    train, dev = read(root / "fit.json"), read(root / "dev.json")
    labels = sorted(read(root / "taxonomy.json"))
    out = root / "search"
    out.mkdir(exist_ok=False)
    candidates, best = [], None
    for name in CONTRACT["candidates"]:
        begin = time.process_time()
        vectorizer = features(name)
        X = vectorizer.fit_transform([r["text"] for r in train])
        model = LinearSVC(C=1, max_iter=3000, dual="auto", random_state=17)
        with warnings.catch_warnings():
            warnings.simplefilter("error", ConvergenceWarning)
            model.fit(X, [r["label"] for r in train])
        bundle = {"features": vectorizer, "model": model, "labels": labels,
                  "policy": {"top": -0.5, "gap": 0}, "version": CONTRACT["version"], "name": name}
        # Use the serving seam to obtain development margins once, then apply
        # exactly the shared policy function for every frozen-grid policy.
        Z = vectorizer.transform([r["text"] for r in dev])
        scores = model.decision_function(Z)
        policies = []
        for top in CONTRACT["policy_grid"]["top_margin_min"]:
            for gap in CONTRACT["policy_grid"]["top_runnerup_gap_min"]:
                policy = {"top": top, "gap": gap}
                result = [decide(model.classes_, s, n, policy) for s, n in zip(scores, Z.getnnz(axis=1))]
                m = metrics(dev, result)
                policies.append({"policy": policy, **{k: v for k, v in m.items() if k != "per_intent"}})
                rank = (m["weighted_cost"], -gap, -top, name)
                if m["oos_misroute_rate"] <= .2 and m["weighted_cost"] < .3 and (best is None or rank < best[0]):
                    best = (rank, name, policy)
        joblib.dump(bundle, out / (name + ".joblib"))
        np.savez_compressed(out / (name + "-development.npz"), scores=scores, ids=[r["id"] for r in dev], classes=model.classes_)
        candidates.append({"candidate": name, "cpu_seconds": time.process_time() - begin,
                           "features": X.shape[1], "policies": policies})
        write(out / "trials.json", candidates)
    assert best is not None, "No candidate beats incumbent; keep router.py incumbent"
    bundle = joblib.load(out / (best[1] + ".joblib"))
    bundle["policy"] = best[2]
    finalist = root / "finalist"
    finalist.mkdir()
    joblib.dump(bundle, finalist / "model.joblib")
    # Seam equivalence against grid path on all development rows.
    seam = Router(bundle).infer([{"text": r["text"]} for r in dev])
    assert abs(metrics(dev, seam)["weighted_cost"] - best[0][0]) < 1e-12
    write(finalist / "manifest.json", {"model_sha256": digest(finalist / "model.joblib"),
        "candidate": best[1], "policy": best[2], "contract_sha256": digest(root / "contract.json"),
        "taxonomy_sha256": digest(root / "taxonomy.json"),
        "fit_sha256": digest(root / "fit.json"), "dev_sha256": digest(root / "dev.json"),
        "confirm_file_not_read": True, "frozen_at": datetime.now(timezone.utc).isoformat(),
        "source_sha256": {p.name: digest(p) for p in HERE.glob("*.py")},
        "dependencies_sha256": digest(HERE / "requirements.lock")})
    write(root / "search-summary.json", {"finalist": best[1], "policy": best[2],
        "development": metrics(dev, seam), "cpu_seconds": time.process_time() - started,
        "wall_seconds": time.perf_counter() - wall,
        "peak_rss_mib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024,
        "fits": 3, "policies": 72, "stop": "predeclared sweep complete; no confirmation read"})


def confirm(root):
    out = root / "confirmation"
    out.mkdir(exist_ok=False)
    # Freeze receipt must exist before opening confirmation rows.
    frozen = read(root / "finalist/manifest.json")
    router = Router.load(root / "finalist")
    rows = read(root / "confirm.json")
    inputs = [{"text": r["text"]} for r in rows]
    begin = time.process_time()
    results = router.infer(inputs)
    m = metrics(rows, results)
    write(out / "predictions.json", [{"id": row["id"], "label": row["label"], **result}
                                     for row, result in zip(rows, results)])
    # Fresh process, temporary cwd, only bundle and JSON input (no training paths).
    payload = "".join(json.dumps(r) + "\n" for r in inputs)
    start = time.perf_counter()
    replay = subprocess.run([sys.executable, str(HERE / "router.py"), str(root / "finalist")],
                            input=payload, text=True, capture_output=True, check=True, cwd="/tmp")
    replay_wall = time.perf_counter() - start
    fresh = [json.loads(line) for line in replay.stdout.splitlines()]
    assert len(fresh) == len(results)
    actions_equal = all((a["action"], a["intent"], a["queue"], a["reason"]) ==
                        (b["action"], b["intent"], b["queue"], b["reason"]) for a, b in zip(results, fresh))
    drift = max(abs(a["margin"] - b["margin"]) for a, b in zip(results, fresh) if a["margin"] is not None)
    latency = []
    for request in inputs[:200]:
        start = time.perf_counter()
        router.infer([request])
        latency.append((time.perf_counter() - start) * 1000)
    start = time.perf_counter()
    subprocess.run([sys.executable, str(HERE / "router.py"), str(root / "finalist")],
                   input=json.dumps(inputs[0]) + "\n", text=True, capture_output=True, check=True, cwd="/tmp")
    cold = time.perf_counter() - start
    upper = m["mean_cost"] - .3 + np.sqrt(np.log(20) / (2 * len(rows)))
    rss = max(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
              resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss) / 1024
    gates = {"cost_upper_lt_minus_0.03": bool(upper < -.03),
             "oos_misroute_le_0.20": m["oos_misroute_rate"] <= .2,
             "all_intent_recall_ge_0.30": min(v["correct_route_recall"] for v in m["per_intent"].values()) >= .3,
             "fresh_actions_equal": actions_equal, "fresh_score_drift_le_1e-10": drift <= 1e-10,
             "p95_under_100ms": bool(np.percentile(latency, 95) < 100),
             "cold_under_10s": cold < 10, "rss_under_1024mib": rss < 1024}
    write(root / "confirmation-summary.json", {"finalist": frozen, "metrics": m,
        "incumbent_mean_cost": .3, "paired_delta": m["mean_cost"] - .3,
        "hoeffding_upper": float(upper), "gates": gates,
        "decision": "accept_local_proxy_candidate" if all(gates.values()) else "retain_incumbent",
        "warm_single_p95_ms": float(np.percentile(latency, 95)), "cold_seconds": cold,
        "fresh_replay_n": len(fresh), "fresh_replay_wall_seconds": replay_wall,
        "max_margin_drift": drift, "cpu_seconds_excluding_child": time.process_time() - begin,
        "peak_rss_mib": rss, "limits": "Row-IID bound is conditional; crowdsourced paraphrase groups unknown. Not causal or production evidence."})


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("phase", choices=["prepare", "fit", "confirm"])
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    globals()[args.phase](args.output.resolve())
