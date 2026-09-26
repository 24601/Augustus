"""Local SMS routing; load only your own trusted, digest-verified joblib bundle."""
import argparse
import hashlib
import json
import math
import sys
from pathlib import Path

import joblib


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(path, expected):
    if digest(path) != expected:
        raise ValueError("artifact digest mismatch")
    bundle = joblib.load(path)  # A hash verifies identity, not trust in the producer.
    if bundle["version"] != "sms-review-v1" or not 0 <= bundle["threshold"] <= 1:
        raise ValueError("invalid bundle")
    if bundle["model"] is not None and list(bundle["model"].classes_) != [0, 1]:
        raise ValueError("invalid labels")
    return bundle


def action(score, threshold):
    return "spam-review" if score >= threshold else "ham"


def infer(bundle, row):
    result = {"action": "ham", "status": "invalid_input", "score": None,
              "policy": "sms-review-v1"}
    text = row.get("text") if isinstance(row, dict) else None
    if not isinstance(text, str) or not text.strip() or len(text) > 10000:
        return result
    if bundle is None:
        result["status"] = "artifact_unavailable"
        return result
    if bundle["model"] is None:
        result["status"] = "incumbent"
        return result
    try:
        model = bundle["model"]
        features = model[0].transform([text])
        if features.nnz == 0:
            result["status"] = "no_features"
            return result
        score = float(model[1].predict_proba(features)[0, 1])
        if not math.isfinite(score) or not 0 <= score <= 1:
            raise ValueError("invalid score")
        result.update(action=action(score, bundle["threshold"]), status="ok", score=score)
    except Exception:
        result["status"] = "inference_failed"
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("bundle")
    parser.add_argument("--sha256", required=True)
    args = parser.parse_args()
    try:
        bundle = load(args.bundle, args.sha256)
    except Exception:
        bundle = None
    for line in sys.stdin:
        try:
            row = json.loads(line)
        except (ValueError, TypeError):
            print(json.dumps({"action": "ham", "status": "malformed_json", "score": None,
                              "policy": "sms-review-v1"}))
            continue
        print(json.dumps(infer(bundle, row), allow_nan=False))


if __name__ == "__main__":
    main()
