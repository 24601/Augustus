# Fit, export and use a task specialist

**Placement:** a bounded component with an agreed label definition and deployment
contract. The recipes below are implementation starting points, not measured
product wins. Assume the data roles in [data and splits](data-and-splits.md) are
already assigned. A fit that only memorizes development examples or cannot reload
in the target environment is rejected; leave the incumbent available.

## Choose what to fit, not just which model to download

| Evidence or constraint | Concrete fit path | What can reject it |
| --- | --- | --- |
| Useful lexical/tabular signal, cheap CPU serving | TF-IDF or validated record features → regularized linear/logistic model; trees for nonlinear tabular structure | Held-out semantic variants or critical slices fail |
| Useful pretrained representation, modest labels | Pinned encoder → specified pooling/normalization → frozen-feature head; cache embeddings | Domain/language features omit the target; head changes do not help |
| Representation needs task separation | SetFit contrastive adaptation plus head, or supervised encoder fine-tuning | Pair sampling overfits, label noise dominates, or incremental cost exceeds benefit |
| Stable instructions with variable evidence/options | Prompt/examples or constrained readout first when compatible; SFT/LoRA if justified | Surface validity, unseen options/tasks, no-match or runtime budget fails |
| Retrieval/ranking | Train on query-document relevance or preference pairs; include realistic hard negatives | Retrieval misses the right candidate or query-level utility falls |
| Continuous/ordinal target | Regression/ordinal objective with target units/order fixed | Bad residuals, large tail errors or changed scale; class accuracy is not the metric |

For a frozen head, save the exact encoder, revision, pooling, normalization and
head together. For SetFit, bound contrastive pairs/steps as well as epochs: all
pairs can grow quadratically. For encoder training, record truncation, optimizer,
learning rate, batch/accumulation, trainable layers, seed, stopping rule and selected
checkpoint. For adapters, save the base revision and adapter/merge configuration.
Check upstream APIs for the pinned library version; a checkpoint name is not a recipe.

For SFT or distillation, specify the exact input/output surface, loss masking and
permitted targets; sample teacher outputs before buying a large generation run.
For program optimization, edit only declared prompts/examples/code parameters,
keep the evaluator independent and test the resulting program's behavior. These
methods are alternatives or justified combinations, not mandatory stages.

General instruction-conditioned training is a different scope: represent each
example's criteria, evidence, candidate set and answer; diversify tasks; hold out
whole task definitions and candidate vocabularies; test invariance and unknowns.
Do not advertise the binary example below as learning that capability.

## Runnable CPU starting point for a binary text task

This deliberately small example uses ordinary scikit-learn, not a trainer framework
or a benchmark driver. Adapt it in the application's source tree. It assumes
canonical integer labels `0` (routine) and `1` (needs escalation), unique string
IDs and nonempty text. It does not perform splitting, adjudication, confirmation
or deployment. Sparse text is a candidate, not the right representation for every task.

Create an isolated environment and lock the resolved dependencies for the artifact:

```sh
python3 -m venv .venv-train
.venv-train/bin/pip install 'scikit-learn==1.7.2'
.venv-train/bin/pip freeze > training-requirements.lock
```

Save this as `fit.py`. Supply only fit and development files; no confirmation data
is required by or sent to this program. One JSONL row is
`{"id":"a","text":"customer report","y":1}`.

```python
import hashlib
import json
from pathlib import Path
import sys
import warnings

import joblib
import sklearn
from sklearn.exceptions import ConvergenceWarning
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

def rows(path):
    data = [json.loads(line) for line in Path(path).read_text().splitlines() if line.strip()]
    if not data or any(not isinstance(r.get("id"), str) or not r["id"] for r in data):
        raise ValueError("nonempty rows with string IDs required")
    if len({r["id"] for r in data}) != len(data):
        raise ValueError("duplicate IDs")
    if any(not isinstance(r.get("text"), str) or not r["text"].strip() for r in data):
        raise ValueError("fit/search text must be nonempty")
    if any(type(r.get("y")) is not int or r["y"] not in (0, 1) for r in data):
        raise ValueError("adjudicate/map labels to integers 0/1 first")
    return data

fit_path, dev_path, out_path = sys.argv[1:]
fit, dev = rows(fit_path), rows(dev_path)
if {r["y"] for r in fit} != {0, 1}:
    raise ValueError("both classes required for this logistic candidate")
if {r["id"] for r in fit} & {r["id"] for r in dev}:
    raise ValueError("fit/search ID overlap; also audit groups and text separately")
out = Path(out_path)
out.mkdir(parents=True, exist_ok=False)  # Never overwrite a prior trial.
model = make_pipeline(
    TfidfVectorizer(ngram_range=(1, 2), max_features=50000),
    LogisticRegression(C=1.0, max_iter=1000, random_state=17),
)
with warnings.catch_warnings():
    warnings.simplefilter("error", ConvergenceWarning)
    model.fit([r["text"] for r in fit], [r["y"] for r in fit])
positive = list(model.classes_).index(1)  # Never assume column order.
scores = model.predict_proba([r["text"] for r in dev])[:, positive]
with (out / "development.jsonl").open("w") as stream:
    for row, p in zip(dev, scores):
        stream.write(json.dumps({"id": row["id"], "p": float(p), "y": row["y"]}) + "\n")
joblib.dump(model, out / "model.joblib")
manifest = {
    "model_id": out.name, "sklearn": sklearn.__version__,
    "labels": {"0": "routine", "1": "needs_escalation"},
    "score": "estimate of P(y=1 | text); calibration unestablished",
    "input_sha256": {role: hashlib.sha256(Path(path).read_bytes()).hexdigest()
                     for role, path in (("fit", fit_path), ("development", dev_path))},
    "model_sha256": hashlib.sha256((out / "model.joblib").read_bytes()).hexdigest(),
}
(out / "manifest.json").write_text(json.dumps(manifest, indent=2))
```

```sh
.venv-train/bin/python fit.py fit.jsonl development.jsonl candidate-01
```

This pipeline fits its vocabulary on training rows only. Its default lowercasing,
tokenization and feature cap are task choices to inspect, not universal cleaning
rules. Change them under a new candidate ID if they remove important evidence.
The manifest must travel with the split/label guide, source lineage, fit script
revision, lockfile and measured environment; it does not reconstruct those for you.

## Select a policy before freezing inference

When binary probability semantics apply, run the companion
`scripts/evaluate_decisions.py`:

```sh
python3 "$AUGUSTUS/scripts/evaluate_decisions.py" candidate-01/development.jsonl \
  --cost-fp 1 --cost-fn 4 --thresholds 0.2,0.4,0.6,0.8
```

The costs above are an example, not a prescribed matrix. `AUGUSTUS` is the
installed companion directory. Input is unique `{id,p,y}` JSONL; `p` must mean
probability assigned to `y=1`, not the maximum class confidence. Optional `p_base`
is compared for Brier only if present on all rows. `group` is validated but not
reported per group; compute important slices yourself. This is not a multiclass,
ordinal, ranking or arbitrary-score evaluator.

The printed `cost_optimal` choice is **in-sample development selection**, never
independent performance evidence. Sweep bounds/abstention policy on development
data as needed, including always-negative/always-positive and the real incumbent.
`action_rate` is predicted-positive fraction, not selective coverage. The helper
reports `decided_coverage` separately with `--lower-threshold`, `--upper-threshold`
and (for cost) `--cost-abstain`. Its deprecated `coverage` alias means action rate.

If probability reliability is needed, fit a suitable calibration map on data not
used to fit the base (or out-of-fold predictions), assess it on separate evidence,
and export it too. A raw score threshold can be selected empirically without
calling that score a calibrated probability. Class frequency, ranking correctness
and reliability are different measurements. Calibrating is not compulsory when
the output consumer needs only a validated rank or action.

For the following executable illustration, place this `policy.json` beside the
model. These cutoffs and input length are illustrative: replace them from the
application contract and development results before confirmation. The abstention
interval is a policy choice; a model cannot silently shrink it to gain coverage.

```json
{"policy_id":"illustration-v1","lower":0.3,"upper":0.7,"max_chars":10000}
```

Save as `infer.py`. It prints decisions; it performs no external action. Only
load a trusted, verified artifact: joblib/pickle loading can execute code.
In production validate the approved bundle digest before deserialization and
handle startup failure by retaining the incumbent, not by serving an empty model.

```python
import json
from pathlib import Path
import sys

import joblib
import numpy as np

bundle = Path(sys.argv[1])
policy = json.loads((bundle / "policy.json").read_text())
lower, upper = policy["lower"], policy["upper"]
if not 0 <= lower < upper <= 1 or type(policy["max_chars"]) is not int or policy["max_chars"] < 1:
    raise ValueError("invalid policy")
model = joblib.load(bundle / "model.joblib")  # Trusted local artifact only.
if set(model.classes_) != {0, 1}:
    raise ValueError("wrong label map")
positive = list(model.classes_).index(1)
for line in sys.stdin:
    row = json.loads(line)
    text = row.get("text")
    result = {"id": row["id"], "p": None, "action": "manual_review",
              "status": "invalid_input", "policy_id": policy["policy_id"]}
    if isinstance(text, str) and text.strip() and len(text) <= policy["max_chars"]:
        features = model[0].transform([text])
        result["status"] = "no_features"
        if features.nnz:
            p = float(model[1].predict_proba(features)[0, positive])
            if not np.isfinite(p) or not 0 <= p <= 1:
                raise ValueError("invalid model score")
            result.update(p=p, status="ok", action=(
                "routine" if p <= lower else "escalate" if p >= upper else "manual_review"))
    print(json.dumps(result, allow_nan=False))
```

```sh
.venv-train/bin/python infer.py candidate-01 < inputs.jsonl > decisions.jsonl
```

The host validates JSON/request IDs, imposes timeouts and handles process failure;
malformed transport is not a negative decision. Zero vocabulary overlap is only
one missing-evidence check, not a general out-of-distribution detector. Log model
and input revision alongside the emitted policy version. Join labels by ID in the
evaluator, never by file position. Keep fallback/error rows in whole-policy loss;
do not send `p: null` to the binary evaluator or silently drop failures to improve it.

## Verify the exported artifact, not only the in-memory fit

In a new process/environment with the locked dependencies, load the bundle without
training files and replay held-out inputs. Test positive and negative cases,
empty/unseen/overlong text, malformed requests, ties at each policy boundary,
unknown classes and missing artifacts. Confirm semantic label mapping, not just
array shape. Ensure the no-match/abstain path reaches a real application fallback.

Before changing precision, batching, runtime or merging adapters, declare acceptable
score drift and action/constraint regressions for representative and boundary
cases. Compare the reference and optimized artifacts under those tolerances.
Exact deterministic equivalence may be required for a particular contract, but
floating-point identity is not a universal serving requirement. A change smaller
than average score tolerance can still cross an important action threshold.

Measure cold start, warm throughput, realistic batch/length mix, tail latency,
peak memory, failure/fallback frequency and total workflow cost. Test the actual
runtime/device, not just training hardware. Hash the final artifact, policy,
preprocessing, calibration and environment together. Changing any of them creates
a new candidate requiring the affected checks and, if acceptance was used, renewed
independent confirmation. Promotion follows [bounded improvement](improve-and-confirm.md).
