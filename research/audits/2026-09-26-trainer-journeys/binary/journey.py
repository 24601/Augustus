"""Reproducible stages; run prepare, fit word1, fit word8, freeze, confirm."""
import os
for variable in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[variable] = "1"

import argparse
from collections import Counter, defaultdict
import hashlib
import json
import platform
import re
import resource
import subprocess
import sys
import time
import unicodedata
import urllib.request
import warnings
import zipfile
from pathlib import Path

import joblib
import numpy as np
from scipy.sparse.csgraph import connected_components
from sklearn.exceptions import ConvergenceWarning
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import NearestNeighbors
from sklearn.pipeline import make_pipeline

from sms import action, digest, infer, load

ROOT = Path(__file__).resolve().parent
WORK = ROOT / "work"
URL = "https://archive.ics.uci.edu/static/public/228/sms+spam+collection.zip"
ZIP_HASH = "1587ea43e58e82b14ff1f5425c88e17f8496bfcdb67a583dbff9eefaf9963ce3"
warnings.simplefilter("error", ConvergenceWarning)


def write(path, value):
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")


def read(path):
    return json.loads(path.read_text())


def norm(text):
    return " ".join(unicodedata.normalize("NFKC", text).casefold().split())


def losses(y, pred):
    return np.where((y == 0) & (pred == 1), 5, np.where((y == 1) & (pred == 0), 1, 0))


def group_losses(rows, values):
    groups = defaultdict(list)
    for row, value in zip(rows, values):
        groups[row["group"]].append(float(value))
    return np.array([np.mean(groups[g]) for g in sorted(groups)])


def metrics(rows, pred):
    y = np.array([r["y"] for r in rows])
    costs = losses(y, pred)
    fp = int(np.sum((y == 0) & (pred == 1)))
    fn = int(np.sum((y == 1) & (pred == 0)))
    return {"n": len(y), "ham": int(sum(y == 0)), "spam": int(sum(y == 1)),
            "fp": fp, "fn": fn, "tp": int(sum((y == 1) & (pred == 1))),
            "tn": int(sum((y == 0) & (pred == 0))),
            "row_loss": float(np.mean(costs)),
            "group_loss": float(np.mean(group_losses(rows, costs))),
            "ham_fpr": fp / int(sum(y == 0)), "spam_recall": 1 - fn / int(sum(y == 1))}


def prepare():
    WORK.mkdir(exist_ok=False)
    archive = ROOT / "corpus.zip"
    if not archive.exists():
        urllib.request.urlretrieve(URL, archive)
    assert digest(archive) == ZIP_HASH, "source changed: do not silently accept new data"
    with zipfile.ZipFile(archive) as z:
        raw = z.read("SMSSpamCollection")
        readme = z.read("readme")
    buckets = defaultdict(list)
    counts = Counter()
    raw_rows = []
    for i, line in enumerate(raw.decode("utf-8").splitlines(), 1):
        label, text = line.split("\t", 1)
        assert label in ("ham", "spam") and text.strip()
        row = {"id": f"line-{i}", "text": text, "y": int(label == "spam")}
        buckets[norm(text)].append(row)
        raw_rows.append(row)
        counts[label] += 1
    conflicts = [k for k, rows in buckets.items() if len({r["y"] for r in rows}) > 1]
    rows = [values[0] for k, values in buckets.items() if k not in conflicts]
    # Label-blind grouping only. This vectorizer is NOT reused for training.
    templates = [re.sub(r"\d+", "#", re.sub(r"https?://\S+|www\.\S+", "URL", norm(r["text"]))) for r in rows]
    features = TfidfVectorizer(analyzer="char", ngram_range=(3, 5)).fit_transform(templates)
    graph = NearestNeighbors(metric="cosine", radius=0.10, n_jobs=1).fit(features).radius_neighbors_graph(features)
    n_groups, groups = connected_components(graph, directed=False)
    for row, group in zip(rows, groups):
        row["group"] = int(group)
    order = np.random.default_rng(20260926).permutation(n_groups)
    a, b = int(n_groups * .6), int(n_groups * .8)
    parts = {}
    for role, ids in (("fit", order[:a]), ("search", order[a:b]), ("confirm", order[b:])):
        selected = set(map(int, ids))
        parts[role] = [r for r in rows if r["group"] in selected]
        write(WORK / f"{role}.json", parts[role])
    manifest = {role: [{"id": r["id"], "group": r["group"], "text_sha256": hashlib.sha256(r["text"].encode()).hexdigest()} for r in rs] for role, rs in parts.items()}
    write(WORK / "split-manifest.json", manifest)
    assert sum(len(rs) for rs in parts.values()) == len(rows)
    assert not (set(r["group"] for r in parts["fit"]) & set(r["group"] for r in parts["confirm"]))
    audit = {"zip_sha256": ZIP_HASH, "raw_sha256": hashlib.sha256(raw).hexdigest(),
             "readme_sha256": hashlib.sha256(readme).hexdigest(), "raw_counts": dict(counts),
             "raw_rows": len(raw_rows), "normalized_unique": len(buckets),
             "conflicting_keys": len(conflicts), "excluded_conflict_rows": sum(len(buckets[k]) for k in conflicts),
             "deduplicated_rows": len(rows), "groups": n_groups,
             "max_group_size": max(Counter(groups).values()),
             "split_manifest_sha256": digest(WORK / "split-manifest.json"),
             "parts": {role: {"rows": len(rs), "groups": len({r["group"] for r in rs}),
                               "sha256": digest(WORK / f"{role}.json")} for role, rs in parts.items()}}
    write(ROOT / "data-receipt.json", audit)
    joblib.dump({"version": "sms-review-v1", "threshold": 1., "model": None}, WORK / "incumbent.joblib")
    print(json.dumps(audit, indent=2))


def fit(name):
    assert not (WORK / "frozen.json").exists(), "finalist already frozen"
    assert name in ("word1", "word8", "char8")
    assert not (WORK / f"{name}.joblib").exists(), "trial already run"
    fit_rows, dev = read(WORK / "fit.json"), read(WORK / "search.json")
    y = np.array([r["y"] for r in fit_rows])
    assert float(np.mean(y)) < float(5 * np.mean(1-y)), "incumbent not cheapest constant"
    char = name == "char8"
    model = make_pipeline(TfidfVectorizer(analyzer="char_wb" if char else "word",
                         ngram_range=(3, 5) if char else (1, 2), min_df=2, sublinear_tf=True,
                         max_features=60000),
                          LogisticRegression(C=1 if name == "word1" else 8, solver="liblinear",
                                             max_iter=1000, random_state=17))
    start = time.process_time()
    model.fit([r["text"] for r in fit_rows], y)
    bundle = {"version": "sms-review-v1", "threshold": .5, "model": model, "id": name}
    scores = np.array([infer(bundle, r)["score"] or 0. for r in dev])
    thresholds = sorted(set(np.round(np.arange(.1, .901, .05), 10)) | {5/6})
    sweep = [{"threshold": float(t), **metrics(dev, (scores >= t).astype(int))} for t in thresholds]
    best = min(sweep, key=lambda m: (m["group_loss"], -m["threshold"]))
    bundle["threshold"] = best["threshold"]
    joblib.dump(bundle, WORK / f"{name}.joblib")
    pred = (scores >= best["threshold"]).astype(int)
    write(WORK / f"{name}-predictions.json", [{"id": r["id"], "score": float(s), "prediction": int(p), "y": r["y"]} for r, s, p in zip(dev, scores, pred)])
    errors = [{"id": r["id"], "y": r["y"], "score": float(s), "text": r["text"]} for r, s, p in zip(dev, scores, pred) if p != r["y"]]
    write(WORK / f"{name}-errors.json", errors)
    receipt = {"trial": name, "cpu_seconds": time.process_time() - start,
               "best": best, "threshold_sweep": sweep,
               "incumbent": metrics(dev, np.zeros(len(dev), dtype=int)),
               "artifact_sha256": digest(WORK / f"{name}.joblib"),
               "fit_sha256": digest(WORK / "fit.json"), "search_sha256": digest(WORK / "search.json")}
    write(ROOT / f"{name}-receipt.json", receipt)
    print(json.dumps({k: v for k, v in receipt.items() if k != "threshold_sweep"}, indent=2))


def freeze():
    receipts = [read(p) for p in ROOT.glob("*-receipt.json") if p.name.startswith(("word", "char"))]
    best = min(receipts, key=lambda r: (r["best"]["group_loss"], r["trial"] != "word1", r["trial"]))
    frozen = {"trial": best["trial"], "artifact_sha256": best["artifact_sha256"],
              "contract_sha256": digest(ROOT / "contract.json"),
              "split_manifest_sha256": digest(WORK / "split-manifest.json"),
              "selection": "minimum development group loss; no refit"}
    assert not (WORK / "frozen.json").exists()
    write(WORK / "frozen.json", frozen)
    write(ROOT / "frozen-receipt.json", frozen)
    print(json.dumps(frozen, indent=2))


def confirm():
    frozen = read(WORK / "frozen.json")
    assert frozen["contract_sha256"] == digest(ROOT / "contract.json")
    path = WORK / (frozen["trial"] + ".joblib")
    bundle = load(path, frozen["artifact_sha256"])
    rows = read(WORK / "confirm.json")
    latencies, results = [], []
    for row in rows:
        start = time.perf_counter()
        results.append(infer(bundle, row))
        latencies.append((time.perf_counter() - start) * 1000)
    pred = np.array([int(r["action"] == "spam-review") for r in results])
    y = np.array([r["y"] for r in rows])
    delta = group_losses(rows, losses(y, pred) - y)
    rng = np.random.default_rng(71)
    bootstrap = [float(np.mean(rng.choice(delta, len(delta)))) for _ in range(5000)]
    upper = float(np.quantile(bootstrap, .95))
    # New process imports no corpus and receives only decision-time text over stdin.
    payload = "".join(json.dumps({"text": r["text"]}) + "\n" for r in rows)
    command = [sys.executable, str(ROOT / "sms.py"), str(path), "--sha256", frozen["artifact_sha256"]]
    cold_start = time.perf_counter()
    cold = subprocess.run(command, input=json.dumps({"text": "Meet me at home"})+"\n", text=True, capture_output=True, check=True)
    cold_seconds = time.perf_counter() - cold_start
    reloaded = [json.loads(line) for line in subprocess.run(command, input=payload, text=True, capture_output=True, check=True).stdout.splitlines()]
    assert len(reloaded) == len(results)
    for expected, actual in zip(results, reloaded):
        assert expected["action"] == actual["action"] and expected["status"] == actual["status"]
        assert expected["score"] is actual["score"] or abs(expected["score"] - actual["score"]) <= 1e-12
    probes = [{"text": ""}, {"text": "x" * 10001}, {"text": None}, [], {},
              {"text": "🦄🦄🦄"}, {"text": "今夜一緒に夕食"},
              {"text": "free prize"}, {"text": "Meet me at home"}]
    probe_payload = "not json\n" + "".join(json.dumps(r)+"\n" for r in probes)
    probe_output = [json.loads(line) for line in subprocess.run(command, input=probe_payload, text=True, capture_output=True, check=True).stdout.splitlines()]
    assert [r["status"] for r in probe_output[:6]] == ["malformed_json"] + ["invalid_input"]*5
    assert probe_output[6]["status"] == "no_features"
    broken = command[:-1] + ["0"*64]
    fallback = json.loads(subprocess.run(broken, input='{"text":"test"}\n', text=True, capture_output=True, check=True).stdout)
    assert fallback["action"] == "ham" and fallback["status"] == "artifact_unavailable"
    threshold = bundle["threshold"]
    assert action(threshold, threshold) == "spam-review"
    assert action(float(np.nextafter(threshold, -np.inf)), threshold) == "ham"
    result = metrics(rows, pred)
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024
    warm = float(np.quantile(latencies, .95))
    accepted = upper < -.005 and result["ham_fpr"] <= .01 and result["spam_recall"] >= .6 and warm < 50 and cold_seconds < 5 and rss < 1024
    active = path if accepted else WORK / "incumbent.joblib"
    write(WORK / "active.json", {"bundle": active.name, "sha256": digest(active)})
    write(WORK / "confirmation-predictions.json", results)
    receipt = {"evidence": "conditional public proxy, approximate group bootstrap", "finalist": frozen,
               "incumbent": metrics(rows, np.zeros(len(rows), dtype=int)), "candidate": result,
               "paired_group_mean_delta": float(np.mean(delta)), "bootstrap_upper_95": upper,
               "confirmation_groups": len(delta), "accepted_proxy": accepted,
               "active": read(WORK / "active.json"), "reload_rows": len(reloaded),
               "warm_p95_ms": warm, "cold_seconds": cold_seconds, "peak_rss_mib": rss,
               "statuses": dict(Counter(r["status"] for r in results)),
               "probe_outputs": probe_output, "digest_failure": fallback,
               "slices": {name: metrics([r for r, keep in zip(rows, mask) if keep], pred[mask]) for name, mask in
                          (("short_le_60", np.array([len(r["text"]) <= 60 for r in rows])),
                           ("long_gt_160", np.array([len(r["text"]) > 160 for r in rows])))},
               "environment": {"python": platform.python_version(), "platform": platform.platform()},
               "source_sha256": {p.name: digest(p) for p in (ROOT / "journey.py", ROOT / "sms.py", ROOT / "requirements.lock")}}
    write(ROOT / "confirmation-receipt.json", receipt)
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    # Hard per-process CPU ceiling; completed stages also count toward cumulative budget.
    used = sum(read(p)["stage_cpu_seconds"] for p in ROOT.glob("timing-*.json"))
    remaining = int(1200 - used)
    assert remaining > 0, "CPU budget exhausted"
    resource.setrlimit(resource.RLIMIT_CPU, (remaining, remaining))
    parser = argparse.ArgumentParser()
    parser.add_argument("stage", choices=["prepare", "fit", "freeze", "confirm"])
    parser.add_argument("trial", nargs="?")
    args = parser.parse_args()
    start_cpu, start_wall = time.process_time(), time.perf_counter()
    assert np.array_equal(losses(np.array([0, 1, 0, 1]), np.array([1, 0, 0, 1])), [5, 1, 0, 0])
    if args.stage == "fit":
        fit(args.trial)
    else:
        globals()[args.stage]()
    child_cpu = resource.getrusage(resource.RUSAGE_CHILDREN)
    write(ROOT / f"timing-{args.stage}-{args.trial or 'run'}.json",
          {"stage_cpu_seconds": time.process_time()-start_cpu+child_cpu.ru_utime+child_cpu.ru_stime,
           "wall_seconds": time.perf_counter()-start_wall})
