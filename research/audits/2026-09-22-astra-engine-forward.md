# Augustus 0.7.0 independent engine forward test

Date: 2026-09-22. This document records actual forward answers and an executed
offline implementation. It supplies evidence for coordinator review; it does
not grade the skill or make a release decision.

## Independence and provenance

The parent supplied the six prompts below. I read no repository scenario
expectations, prior audits/answers, git diff, source reports, or prior research
findings. No model/provider calls, third-party programs, installs, network,
paid work, external writes, git writes, or subagents were used. Local shell and
Python standard-library operations read the runtime and executed my harness
and the bundled comparison helper. Temporary implementation files are under
`/tmp/augustus-astra-engine-forward.EFfm8L`; their complete substantive contents are retained below.

Requested routing (parent's spawn record): `gpt-6-astra`,
`reasoning_effort=xhigh`, `fork_turns=none`. Observed: scheduler identity
`/root/astra_engine_forward`; generic child instructions describe GPT-6.
The resolved backend model/build and effective effort are not independently
exposed. Requested routing is not treated as attested runtime identity.

Runtime root: `.agents/skills/augustus`. Its SKILL.md declares version 0.7.0.
I hashed all 22 files recursively, excluding only `__pycache__` contents
and files with `.pyc` or `.pyo` suffixes. The bundle hash is SHA-256 of
UTF-8 manifest lines sorted by relative path, each
`<file_sha256>  <relative_posix_path>\n`.

- Before: `d651c185d4c04fa7f853f2a2e0c61f5a85a56d178659dcb930d5146f09a1d664`.
- After execution: `d651c185d4c04fa7f853f2a2e0c61f5a85a56d178659dcb930d5146f09a1d664`.
- Python used: 3.14.7.
- Runtime files were not edited. This audit is my only repository write.

Instructions/references read completely:

- `AGENTS.md`.
- `CONTRIBUTING.md`.
- `.agents/skills/augustus/SKILL.md`.
- `.agents/skills/augustus/references/composition-algebra.md`.
- `.agents/skills/augustus/references/validation.md`.
- `.agents/skills/augustus/references/optimizer-integration.md`.
- `research/protocol.md` and `research/prompts/research-fold.md` as repository
  procedure, not as source evidence or authority to expand this forward test.
- `.agents/skills/augustus/scripts/compare_workflows.py` (complete source).

I also listed and hashed the runtime files; hashing the other references did
not involve reading their prose as behavioral guidance. The first combined
reference display was truncated in validation.md, so I reread that file
completely in a separate call. No surprising behavior occurred in the harness
or helper. Repository checks and the integrated diff are left to the parent,
as requested; I did not run `make check` or open test expectations.

## Actual answers

### 1. Selected downstream traffic

**Prompt:** Our second-stage classifier has 5 percent error on all tickets.
A new first-stage gate sends it only difficult tickets, 20 percent of traffic.
Can we budget system errors as 0.2 times 0.05 and keep its old calibration?

**Answer:** No. If G means reaching the second stage, its contribution is
`P(G) P(error | G) = 0.2 P(error | G)`, not automatically 1%. The 5% rate
is marginal. On the same population, all its errors could lie in that 20%:
then its selected error rate would be 25% and the contribution 5%.
The unselected branch and gate-induced errors also belong in system accounting;
for exhaustive branches, total loss is
`0.2 E[L | G] + 0.8 E[L | not G]`.

Freeze the gate and measure the second stage on held-out tickets that actually
reach it, including calibration and cost-weighted routing errors. Selection
can change `P(Y | score,G)`, so old calibration does not automatically
transfer. Requalification may show the existing calibrator still works;
refitting is needed only if the evidence and consuming policy require it.
Also evaluate the whole workflow, branch coverage, fallbacks, and delays.
Reject the proposed budget if conditional or total loss exceeds the agreed
bound.

### 2. Interchangeability with background information

**Prompt:** Y and C are independent fair bits. Signal A=C and signal B=Y XOR C
each tell us nothing about Y alone. Our downstream program already knows C.
Are A and B interchangeable components? What does this teach us about replacing
decision models?

**Answer:** They are not interchangeable. Given C, A repeats information the
program already has, leaving Y a fair bit. B together with C determines Y
exactly: `Y = B XOR C`. Under 0–1 prediction loss, the best error is 1/2
using (A,C) and zero using (B,C).

Equal standalone information or accuracy does not establish substitutability.
Compare a replacement jointly with the consumer's existing evidence, selection
policy, feasible actions, loss, and dependencies. A replacement must preserve
the relevant conditional behavior at the join; matching an output schema or
isolated score is insufficient. A paired end-to-end comparison with C present
would immediately falsify the interchangeability claim.

### 3. Reused eval set and promotion plan

**Prompt:** We improved a refund-routing prompt through 80 rounds on the same
200 eval tickets. The model-judge score is up 12 points. Each round had a 95
percent confidence interval. Build the next evaluation and promotion plan,
including what to implement and what to keep fixed.

**Answer:** Treat those 200 tickets as development data now. The 12-point
increase is an adaptively selected gain on a model-judge proxy; per-round
nominal 95% intervals do not confer a 95% guarantee on the selected winner.
Resplitting those already exposed tickets does not create an untouched test.

Implement a versioned paired runner for the frozen incumbent and selected
challenger, a case/entity split and contamination ledger, and per-case traces
containing raw outputs, proposed routes, fallbacks, actual outcome labels,
constraint events, inference/review/retry costs and timing. Preserve all 80
trials and identify precisely which prompt won. Implement an outcome scorer
using adjudicated refund-intent labels and explicit false-positive/
false-negative costs; independently check judge agreement and repeatability
on frozen outputs before relying on its score. Judge score stays secondary
unless its relationship to the actual decision objective is established.

Collect fresh deployment-representative units with independent labels. Split
by customer, conversation, template, or time as necessary to prevent shared
information leaking between development, calibration/policy selection, and
confirmation. If the new prompt's probabilities feed thresholds, requalify
calibration on a separate set; do not require a new calibrator if the old one
passes. Use calibration/selection data for any threshold changes, then freeze
both arms.

Before confirmation, fix the primary paired loss, meaningful improvement or
noninferiority margin, sample size/power plan, comparison family and alpha,
required slices, cost/latency limits, hard constraints, missing-data policy,
and rejection rule. Use one frozen challenger versus incumbent if that is the
only needed comparison; 80 historical development rounds do not require
pretending 80 fresh confirmation comparisons will occur. Respect clustering
and obtain sufficient support for the reporting units the policy requires.
For fixed-sample confirmation, do not peek and stop opportunistically. A
planned sequential procedure is an alternative only under its assumptions.

Keep authorization, payment effects, schema/label definitions, loss units,
gold labels, data roles, confirmation margins, and action-state checks outside
prompt search. Refund intent must not itself authorize a refund payment.
If confirmation is inspected and then used to revise the prompt, retire those
cases from untouched confirmation and obtain fresh evidence or a justified
adaptive-valid design.

Promote only if the prespecified outcome and constraint gates pass, with the
authorized owner approving the rollout. A speed or cost tradeoff can be
accepted under the agreed utility/noninferiority policy; every metric need
not improve. Retain the incumbent when evidence is inconclusive or gates
fail. A later authorized shadow/canary should retain rollback and independent
outcome monitoring; shadow disagreement alone cannot reveal outcomes of
unexecuted actions. No provider calls or rollout are implemented or authorized
by this planning answer.

### 4. Entropy and thermodynamic analogy

**Prompt:** A blog says entropy minimization and a thermodynamic free-energy
analogy prove that an ensemble of decision models will improve every agent
workflow. Should Augustus promote this into its core calculus? If not, how
could we still develop a useful method from it?

**Answer:** No universal improvement rule follows. A perfectly accurate
baseline duplicated in an ensemble has unchanged decision quality and extra
cost; an overconfident wrong model can have lower entropy while making worse
decisions. Thermodynamic terminology does not supply a theorem about workflow
outcomes.

Treat the blog claim as a hypothesis and develop one bounded mechanism:
for example, acquire a second judgment only on uncertain routing cases and
test whether the extra information reduces cost-weighted routing loss enough
to justify acquisition. Map model distributions to a fixed label/event space,
entropy to nats, task loss to the declared business loss unit, acquisition to
measured cost and latency, and any tradeoff coefficient to units that convert
them. If proposing `F = expected_loss + k * acquisition_cost - t * entropy`,
then k and t need specified conversion units; F is a chosen optimization
objective, not physical free energy or a guarantee. Explain whether entropy
is over labels, model weights, or something else, and why its sign has the
claimed effect.

State assumptions about label alignment, evidence access, dependence,
calibration when probabilities drive policy, and the consumer's capacity to
use the signal. Compare a single model, a simple deterministic policy, and
the bounded ensemble on fresh paired outcomes at a stated budget. Ablate the
second model and uncertainty gate; count correlated errors, fallback workload,
cost and latency. Reject the mechanism if the prespecified utility/risk
comparison loses. Only a result that changes a particular design decision,
with its scope and counterexample retained, merits a targeted runtime update.
This answer assesses the supplied claim; it does not claim to have inspected
an unidentified blog or reproduced its result.

### 5. Simple rewrite

**Prompt:** Rewrite this sentence more clearly: The meeting was moved because
the room was unavailable.

**Answer:** The room was unavailable, so the meeting was moved.

No decision-model placement or evaluation is needed for this prose rewrite.

### 6. Executed refund-intent routing build

**Prompt:** BUILD REQUEST: Build and execute a small offline paired evaluation
for refund-INTENT routing, not payment authorization. Synthetic cases
(id, classifier probability, gold intent): a,.1,0; b,.3,0; c,.45,1; d,.5,0;
e,.55,1; f,.65,0; g,.7,1; h,.9,1. Incumbent routes positive at p>=.4;
challenger at p>=.6. A false positive costs 2 units and false negative 3 units;
correct costs 0. Normalize by 3 for bounded loss. Use one case per unit.
Incumbent per-case inference cost is .01 and latency 20 ms; challenger cost
is .005 except unknown on case f, and latency 10 ms. Neither arm has observed
hard-constraint violations in this synthetic fixture. Deliver the runnable
eval harness, generated outcome receipt and actual comparison output using
the installed helper if suitable. State what we can and cannot decide about
the challenger and next real experiment. This is a local fixture exercise,
not permission to call a provider or deploy. Do not replace implementation
with a recommendation.

**Answer and observed implementation result:** Built and executed the harness
below using the reviewed installed comparison helper. Each case is one paired
unit; labels, cost and latency are supplied synthetic facts. It generates
route decisions, actual FP/FN losses and a versioned outcome receipt, then
executes the helper as a local subprocess. The receipt uses `phase=search`
and `evidence_kind=fixture`; there is no fabricated confirmation plan.

| Quantity | Incumbent | Challenger |
| --- | ---: | ---: |
| Positive routes | c,d,e,f,g,h | f,g,h |
| False positives | d,f (2) | f (1) |
| False negatives | none (0) | c,e (2) |
| Total penalty units | 4 | 8 |
| Mean bounded loss | 1/6 | 1/3 |
| Supplied mean latency | 20 ms | 10 ms |
| Known inference-cost observations | 8/8 | 7/8 |
| Mean inference cost | .01 | unknown |
| Observed fixture constraint violations | 0 | 0 |

Challenger-minus-incumbent mean bounded loss is +1/6: the challenger loses
on the specified routing-loss objective in this fixture. Moving d to the
negative route saves 2 units, while missing c and e adds 6. All cases receive
a route; the positive-route fraction is not abstention coverage.

Incumbent total inference cost is .08. Challenger's known subtotal is .035
plus the unknown cost on f; its total is lower only if that cost is below
.045. There is no justified overall mean of .005 and no justified cost-saving
claim. Do not add these inference costs to the intent penalty without an
explicit common-unit conversion and tradeoff policy.

The helper returned `fixture_evidence_only`, preserved the unknown mean
cost as null, and produced no confirmation interval. This verifies local
arithmetic and receipt plumbing, not model quality, probability calibration,
real service latency, real-world superiority, independence, or compliance.
Zero listed fixture violations is not proof of an effective interlock.
There is no payment-authorizing code or provider call.

Keep the incumbent for the current routing-loss decision. The challenger
could be reconsidered if a prespecified real objective values latency enough
to accept a measured loss tradeoff, but this fixture supplies neither that
policy nor deployment evidence. With calibrated probabilities and only the
stated intent-error losses, the Bayes threshold would be 2/(2+3)=.4;
the supplied numbers are not proof of calibration.

The next real experiment should freeze the two policies and collect fresh,
representative, independently adjudicated intent cases, clustering repeated
customer/conversation units when needed. Use complete inference-cost and
latency telemetry, including errors/retries/fallbacks; record missingness
without imputation. Prespecify improvement or a noninferiority/latency tradeoff,
confirmation sample/family, required slices and constraint gates. Offline
paired labels can establish routing error under that sampling design;
claims about service outcomes from actually rerouted cases may need a
separately authorized controlled rollout. Such collection/provider calls
and deployment are not performed here.

## Complete reproduction artifacts

Save the following code and CSV blocks as `eval_refund_intent.py` and
`fixture.csv` in a fresh directory. With the reviewed Augustus runtime at
the path shown, execute:

```sh
python3 eval_refund_intent.py fixture.csv /Users/basitmustafa/Developer/Augustus/.agents/skills/augustus/scripts/compare_workflows.py results
```

Actual invocation used absolute temporary artifact paths; it exited 0:

```sh
python3 /tmp/augustus-astra-engine-forward.EFfm8L/eval_refund_intent.py /tmp/augustus-astra-engine-forward.EFfm8L/fixture.csv /Users/basitmustafa/Developer/Augustus/.agents/skills/augustus/scripts/compare_workflows.py /tmp/augustus-astra-engine-forward.EFfm8L/results
```

The script pins the comparison helper hash and records the fixture and
harness hashes in the generated receipt. The embedded code/CSV include a
trailing newline, as do the files used in the run. It writes only the named
output directory and executes only the local helper. It is a bounded
fixture harness, not a general provider adapter.

### eval_refund_intent.py

```python
#!/usr/bin/env python3
"""Offline fixture evaluation; routes intent and never authorizes payment."""
import argparse
import csv
import hashlib
import json
import math
from pathlib import Path
import subprocess
import sys

HARNESS_VERSION = "refund-intent-paired-v1"
HELPER_SHA256 = "9955ddba36c0a060abfe1446909b8a74d4676ee7f3470094d3b014d2cfde4288"


def load_cases(path):
    with path.open(newline="", encoding="utf-8") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != ["id", "p", "gold_intent"]:
            raise ValueError("expected id,p,gold_intent columns")
        cases, seen = [], set()
        for row in reader:
            identity = row["id"]
            if not identity or identity in seen or None in row:
                raise ValueError("empty/duplicate id or malformed CSV row")
            p = float(row["p"])
            if not math.isfinite(p) or not 0 <= p <= 1:
                raise ValueError("probability must be finite and in [0,1]")
            if row["gold_intent"] not in ("0", "1"):
                raise ValueError("gold_intent must be 0 or 1")
            seen.add(identity)
            cases.append((identity, p, int(row["gold_intent"])))
    if not cases:
        raise ValueError("fixture is empty")
    return cases


def arm(p, gold, threshold, inference_cost, latency):
    route = int(p >= threshold)
    error = "FP" if route and not gold else "FN" if gold and not route else None
    penalty = 2 if error == "FP" else 3 if error == "FN" else 0
    return {"route_positive": route, "error": error, "penalty_units": penalty,
            "loss": penalty / 3, "cost": inference_cost,
            "latency_ms": latency, "violations": []}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixture", type=Path)
    parser.add_argument("helper", type=Path)
    parser.add_argument("output_dir", type=Path)
    args = parser.parse_args()
    helper = args.helper.resolve()
    if hashlib.sha256(helper.read_bytes()).hexdigest() != HELPER_SHA256:
        raise ValueError("helper differs from the reviewed version")
    cases = load_cases(args.fixture)
    pairs = [{"id": identity, "p": p, "gold_intent": gold,
              "incumbent": arm(p, gold, .4, .01, 20),
              "candidate": arm(p, gold, .6, None if identity == "f" else .005, 10)}
             for identity, p, gold in cases]
    receipt = {
        "schema_version": 1, "phase": "search",
        "incumbent_id": "intent-threshold-ge-0.4-v1",
        "candidate_id": "intent-threshold-ge-0.6-v1",
        "dataset_id": "synthetic-refund-intent-eight-v1",
        "outcome_definition": "(2*false_positive + 3*false_negative)/3 per case",
        "sampling_unit": "case", "evidence_kind": "fixture", "loss_bound": 1,
        "versions": {"harness": HARNESS_VERSION, "model": "supplied-synthetic-p-v1",
                     "rubric": "supplied-gold-refund-intent-v1",
                     "calibration": "unknown; none fitted", "loss": "fp2-fn3-div3-v1"},
        "provenance": {
            "labels": "user-supplied synthetic gold intent",
            "cost_latency": "user-supplied fixture values; not measured service telemetry",
            "violations": "user reports none observed in this fixture; not enforcement proof",
            "fixture_sha256": hashlib.sha256(args.fixture.read_bytes()).hexdigest(),
            "helper_sha256": HELPER_SHA256,
            "harness_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
        "pairs": pairs}
    args.output_dir.mkdir(parents=True, exist_ok=True)
    receipt_path = args.output_dir / "outcomes.json"
    receipt_path.write_text(json.dumps(receipt, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    run = subprocess.run([sys.executable, str(helper), str(receipt_path)],
                         capture_output=True, text=True, check=True)
    result = json.loads(run.stdout)
    if result["paired_units"] != len(cases) or result["evidence_kind"] != "fixture":
        raise ValueError("helper comparison identity mismatch")
    if result["candidate"]["mean_cost"] is not None:
        raise ValueError("unknown candidate cost was lost")
    (args.output_dir / "comparison.json").write_text(run.stdout, encoding="utf-8")
    print(run.stdout, end="")


if __name__ == "__main__":
    main()
```

### fixture.csv

```csv
id,p,gold_intent
a,.1,0
b,.3,0
c,.45,1
d,.5,0
e,.55,1
f,.65,0
g,.7,1
h,.9,1
```

### Generated outcomes.json (complete)

```json
{
  "schema_version": 1,
  "phase": "search",
  "incumbent_id": "intent-threshold-ge-0.4-v1",
  "candidate_id": "intent-threshold-ge-0.6-v1",
  "dataset_id": "synthetic-refund-intent-eight-v1",
  "outcome_definition": "(2*false_positive + 3*false_negative)/3 per case",
  "sampling_unit": "case",
  "evidence_kind": "fixture",
  "loss_bound": 1,
  "versions": {
    "harness": "refund-intent-paired-v1",
    "model": "supplied-synthetic-p-v1",
    "rubric": "supplied-gold-refund-intent-v1",
    "calibration": "unknown; none fitted",
    "loss": "fp2-fn3-div3-v1"
  },
  "provenance": {
    "labels": "user-supplied synthetic gold intent",
    "cost_latency": "user-supplied fixture values; not measured service telemetry",
    "violations": "user reports none observed in this fixture; not enforcement proof",
    "fixture_sha256": "7b6b27284558384aef2a20dec04e9c576dbbda57ac97be3aa6df320d2e232d02",
    "helper_sha256": "9955ddba36c0a060abfe1446909b8a74d4676ee7f3470094d3b014d2cfde4288",
    "harness_sha256": "afcf9ef024c102fd3f3e9460a78d3e53f0b488ff7b190aecb92bccbfbfb84fba"
  },
  "pairs": [
    {
      "id": "a",
      "p": 0.1,
      "gold_intent": 0,
      "incumbent": {
        "route_positive": 0,
        "error": null,
        "penalty_units": 0,
        "loss": 0.0,
        "cost": 0.01,
        "latency_ms": 20,
        "violations": []
      },
      "candidate": {
        "route_positive": 0,
        "error": null,
        "penalty_units": 0,
        "loss": 0.0,
        "cost": 0.005,
        "latency_ms": 10,
        "violations": []
      }
    },
    {
      "id": "b",
      "p": 0.3,
      "gold_intent": 0,
      "incumbent": {
        "route_positive": 0,
        "error": null,
        "penalty_units": 0,
        "loss": 0.0,
        "cost": 0.01,
        "latency_ms": 20,
        "violations": []
      },
      "candidate": {
        "route_positive": 0,
        "error": null,
        "penalty_units": 0,
        "loss": 0.0,
        "cost": 0.005,
        "latency_ms": 10,
        "violations": []
      }
    },
    {
      "id": "c",
      "p": 0.45,
      "gold_intent": 1,
      "incumbent": {
        "route_positive": 1,
        "error": null,
        "penalty_units": 0,
        "loss": 0.0,
        "cost": 0.01,
        "latency_ms": 20,
        "violations": []
      },
      "candidate": {
        "route_positive": 0,
        "error": "FN",
        "penalty_units": 3,
        "loss": 1.0,
        "cost": 0.005,
        "latency_ms": 10,
        "violations": []
      }
    },
    {
      "id": "d",
      "p": 0.5,
      "gold_intent": 0,
      "incumbent": {
        "route_positive": 1,
        "error": "FP",
        "penalty_units": 2,
        "loss": 0.6666666666666666,
        "cost": 0.01,
        "latency_ms": 20,
        "violations": []
      },
      "candidate": {
        "route_positive": 0,
        "error": null,
        "penalty_units": 0,
        "loss": 0.0,
        "cost": 0.005,
        "latency_ms": 10,
        "violations": []
      }
    },
    {
      "id": "e",
      "p": 0.55,
      "gold_intent": 1,
      "incumbent": {
        "route_positive": 1,
        "error": null,
        "penalty_units": 0,
        "loss": 0.0,
        "cost": 0.01,
        "latency_ms": 20,
        "violations": []
      },
      "candidate": {
        "route_positive": 0,
        "error": "FN",
        "penalty_units": 3,
        "loss": 1.0,
        "cost": 0.005,
        "latency_ms": 10,
        "violations": []
      }
    },
    {
      "id": "f",
      "p": 0.65,
      "gold_intent": 0,
      "incumbent": {
        "route_positive": 1,
        "error": "FP",
        "penalty_units": 2,
        "loss": 0.6666666666666666,
        "cost": 0.01,
        "latency_ms": 20,
        "violations": []
      },
      "candidate": {
        "route_positive": 1,
        "error": "FP",
        "penalty_units": 2,
        "loss": 0.6666666666666666,
        "cost": null,
        "latency_ms": 10,
        "violations": []
      }
    },
    {
      "id": "g",
      "p": 0.7,
      "gold_intent": 1,
      "incumbent": {
        "route_positive": 1,
        "error": null,
        "penalty_units": 0,
        "loss": 0.0,
        "cost": 0.01,
        "latency_ms": 20,
        "violations": []
      },
      "candidate": {
        "route_positive": 1,
        "error": null,
        "penalty_units": 0,
        "loss": 0.0,
        "cost": 0.005,
        "latency_ms": 10,
        "violations": []
      }
    },
    {
      "id": "h",
      "p": 0.9,
      "gold_intent": 1,
      "incumbent": {
        "route_positive": 1,
        "error": null,
        "penalty_units": 0,
        "loss": 0.0,
        "cost": 0.01,
        "latency_ms": 20,
        "violations": []
      },
      "candidate": {
        "route_positive": 1,
        "error": null,
        "penalty_units": 0,
        "loss": 0.0,
        "cost": 0.005,
        "latency_ms": 10,
        "violations": []
      }
    }
  ]
}
```

### Actual comparison.json / helper stdout (complete)

```json
{
  "schema_version": 1,
  "incumbent_id": "intent-threshold-ge-0.4-v1",
  "candidate_id": "intent-threshold-ge-0.6-v1",
  "dataset_id": "synthetic-refund-intent-eight-v1",
  "outcome_definition": "(2*false_positive + 3*false_negative)/3 per case",
  "sampling_unit": "case",
  "phase": "search",
  "evidence_kind": "fixture",
  "paired_units": 8,
  "loss_bound": 1.0,
  "incumbent": {
    "mean_loss": 0.16666666666666666,
    "units_with_violations": 0,
    "known_cost_units": 8,
    "mean_cost": 0.01,
    "known_latency_ms_units": 8,
    "mean_latency_ms": 20.0
  },
  "candidate": {
    "mean_loss": 0.3333333333333333,
    "units_with_violations": 0,
    "known_cost_units": 7,
    "mean_cost": null,
    "known_latency_ms_units": 8,
    "mean_latency_ms": 10.0
  },
  "mean_loss_delta": 0.16666666666666669,
  "confirmation": null,
  "assessment": "fixture_evidence_only",
  "limits": [
    "Arithmetic on supplied outcomes, not verification of labels, independence, causal identification, or dataset isolation.",
    "Confirmation needs a prespecified sample/family, frozen policies/loss, and representative independent units; no optional stopping or adaptive test reuse.",
    "Zero observed violations is not proof of constraint compliance; missing costs/latencies remain unknown.",
    "A loss bound does not satisfy separate latency, cost, subgroup, safety, or deployment gates. No policy is promoted or executed."
  ],
  "input_sha256": "614c6e1c9061696140b9d74a6de8b2c0e44488a74b574593a76c7d2389148919"
}
```

### Additional arithmetic read-back

A separate Python standard-library read-back summed the generated integer
penalties and used `fractions.Fraction(total, 3 * number_of_cases)`:

```text
incumbent routes: [0,0,1,1,1,1,1,1]
incumbent FP=2, FN=0, total penalty=4, exact normalized mean=1/6
incumbent known inference subtotal=0.08, unknown units=0
candidate routes: [0,0,0,0,0,1,1,1]
candidate FP=1, FN=2, total penalty=8, exact normalized mean=1/3
candidate known inference subtotal=0.035, unknown units=1
```

The float delta in the helper output (0.16666666666666669) is the ordinary
floating-point representation of the paired mean; the integer-penalty
calculation gives the exact difference 1/6.

### Bundle-hash reproduction

Run this from the repository root before and after a reproduction:

```python
from pathlib import Path
import hashlib

root = Path(".agents/skills/augustus")
files = sorted(
    p for p in root.rglob("*")
    if p.is_file() and "__pycache__" not in p.parts
    and p.suffix not in (".pyc", ".pyo")
)
manifest = "".join(
    f"{hashlib.sha256(p.read_bytes()).hexdigest()}  "
    f"{p.relative_to(root).as_posix()}\n"
    for p in files
)
print(len(files), hashlib.sha256(manifest.encode()).hexdigest())
```
