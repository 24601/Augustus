"""Offline JSONL queue recommendation seam; never executes account actions."""
import hashlib
import json
from pathlib import Path
import sys

import joblib
import numpy as np


def review(reason):
    return {"action": "manual_review", "queue": "support.manual_review",
            "intent": None, "margin": None, "gap": None, "reason": reason}


def decide(classes, scores, nonempty, policy):
    order = np.argsort(scores, kind="stable")
    winner, runner = int(order[-1]), int(order[-2])
    top, gap = float(scores[winner]), float(scores[winner] - scores[runner])
    label = str(classes[winner])
    result = review("low_margin")
    result.update(margin=top, gap=gap)
    if not nonempty:
        return review("no_features")
    if not np.isfinite(scores).all():
        return review("invalid_score")
    if label == "oos":
        result["reason"] = "predicted_oos"
    elif gap == 0:
        result["reason"] = "ambiguous"
    elif top >= policy["top"] and gap >= policy["gap"]:
        result.update(action="route", queue="support." + label,
                      intent=label, reason="accepted")
    return result


class Router:
    def __init__(self, bundle):
        self.bundle = bundle

    @classmethod
    def load(cls, path):
        # Only load locally generated trusted pickle; digest is integrity, not trust.
        path = Path(path)
        manifest = json.loads((path / "manifest.json").read_text())
        data = (path / "model.joblib").read_bytes()
        if hashlib.sha256(data).hexdigest() != manifest["model_sha256"]:
            raise ValueError("bundle digest mismatch")
        bundle = joblib.load(path / "model.joblib")
        if sorted(bundle["model"].classes_) != sorted(bundle["labels"] + ["oos"]):
            raise ValueError("bundle label mismatch")
        return cls(bundle)

    def infer(self, requests):
        answers = [review("invalid_input") for _ in requests]
        valid = [(i, r["text"]) for i, r in enumerate(requests)
                 if isinstance(r, dict) and set(r) == {"text"}
                 and isinstance(r["text"], str) and r["text"].strip()
                 and len(r["text"]) <= 2000]
        if valid:
            features = self.bundle["features"].transform([text for _, text in valid])
            scores = self.bundle["model"].decision_function(features)
            for (i, _), score, nonempty in zip(valid, scores, features.getnnz(axis=1)):
                answers[i] = decide(self.bundle["model"].classes_, score, nonempty,
                                    self.bundle["policy"])
        return answers


def main():
    router = None
    if sys.argv[1] != "incumbent":
        try:
            router = Router.load(sys.argv[1])
        except (OSError, ValueError, KeyError):
            pass  # Unavailable artifact fails closed, one response per input.
    for line in sys.stdin:
        try:
            request = json.loads(line)
        except (ValueError, TypeError):
            result = review("invalid_json")
        else:
            result = (router.infer([request])[0] if router else
                      review("incumbent" if sys.argv[1] == "incumbent" else "unavailable_artifact"))
        print(json.dumps(result, allow_nan=False), flush=True)


if __name__ == "__main__":
    main()
