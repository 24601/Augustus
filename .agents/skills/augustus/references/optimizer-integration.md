# Build and hill-climb decision programs

Use this card to implement and improve decision-driven or Software 3.0 systems:
ordinary code plus learned prompts, rubrics, parameters and routing components.
It is not a claim that every program should become learned, or an API guide.
[Ax](https://github.com/ax-llm/ax) and DSPy optimizers search an LM
program's prompts, demonstrations, modules, and sometimes model choice. They do
not inherit authority over application policy, permissions, or state.

## Agent execution loop

Deliver working artifacts when asked to build, not just a design card. Reuse the
host's framework and evaluation tools when suitable; this skill is a method for
the agent, not a replacement application framework.

1. **Find the leverage point.** Trace the current workflow and outcome failures;
   use the toolbox sweep and composition graph to propose the smallest useful
   learned component. State the mechanism, baseline, expected benefit and falsifier.
2. **Build the seam.** Implement a versioned provider adapter, score contract,
   explicit policy/fallback, effect boundary and trace recorder. Include missing
   evidence, timeouts, retries and no-match cases. Keep the incumbent runnable.
3. **Build the eval before climbing.** Define outcome loss and hard constraints;
   create independently labeled/observed, unit-separated search and confirmation
   data. Log case/episode ID, policy/model/rubric versions, raw scores, actions,
   full costs, timestamps and outcome provenance. Cluster repeats by their real
   independent unit. Unobserved counterfactual outcomes are not negative labels.
4. **Run bounded search.** Freeze allowed edits, metric, data roles and budget.
   Generate a candidate from a concrete failure, compare it with the incumbent
   on matched search cases, inspect regressions and retain or reject it. A greedy
   climb is a baseline, not a global optimum; use multi-candidate search when
   complementarity or noisy evaluations justifies its cost. Preserve failed trials.
5. **Confirm a frozen candidate.** Use untouched confirmation units with a
   prespecified sample/comparison plan. Measure paired end-to-end loss, constraints,
   risk/coverage, slices and total cost. After inspecting confirmation outcomes,
   those cases are no longer untouched for further adaptive tuning. Fresh data or
   a justified adaptive-valid procedure is needed, not another nominal 95% interval.
6. **Promote only with authority and observe.** If agreed gates pass, use an
   authorized shadow/canary rollout, independent outcome probes, drift checks and
   rollback to the recorded incumbent. Stop at the task's authority boundary.
   Return the run command, receipts, incumbent/candidate revisions, decision and
   remaining uncertainty—even when the right decision is to keep the incumbent.

Search may improve a proxy while harming actual outcomes. Audit proxy validity
and retain the earlier active constraints, not only the newest requirement.
Fixed-n intervals do not permit repeated peeking; confidence sequences can
support specified sequential questions under their own assumptions, not arbitrary
test reuse or dependent episodes. See [time-uniform inference](https://arxiv.org/abs/1810.08240).

### A small executable outcome comparison

Use the bundled [compare_workflows.py](../scripts/compare_workflows.py) for paired
bounded episode losses, or adapt an existing harness with the same boundaries:

```sh
python3 <skill-dir>/scripts/compare_workflows.py outcomes.json
```

Minimal synthetic input (an arithmetic fixture, not deployment evidence):

```json
{
  "schema_version": 1, "phase": "search",
  "incumbent_id": "rules-v1", "candidate_id": "classifier-v2",
  "dataset_id": "fixture-v1", "outcome_definition": "unit-normalized episode loss",
  "sampling_unit": "episode", "evidence_kind": "fixture", "loss_bound": 1,
  "pairs": [{
    "id": "example-1",
    "incumbent": {"loss": 0.4, "cost": 0.02, "latency_ms": 30, "violations": []},
    "candidate": {"loss": 0.2, "cost": null, "latency_ms": 40, "violations": []}
  }]
}
```

Search reports are descriptive. Confirmation additionally supplies `alpha`,
`minimum_improvement` and `comparison_count` fixed before evaluation. For n
independent paired units, losses in `[0,B]`, and K prespecified comparisons,
the helper computes a conservative one-sided upper bound for candidate-minus-
incumbent mean loss: `mean_delta + B * sqrt(2*log(K/alpha)/n)`, capped at B.
The accumulated upper rounds upward; a reported equality never supports a
strict margin. The transcendental radius uses ordinary floating-point math.
This is a fixed-sample Hoeffding/union-bound calculation, not a sequential test.

The helper rejects malformed/unpaired inputs, reports observed violations despite
a loss improvement, hashes the input and preserves unknown costs. It does not
verify caller-supplied labels, sampling, isolation or causal identification;
`observed`/`adjudicated` are provenance declarations, not attestations. Proxy and
fixture evidence stay labeled. A supported loss margin neither enforces separate
SLAs nor authorizes deployment. Supply real complete-workflow costs and check all
product gates separately. This local tool never calls models or executes actions.

Optional `excluded_units` (nonnegative integer) and `missing_outcome_policy`
(text) preserve declared attrition; absent/null is unknown, not zero exclusions.
Summaries cover supplied pairs only. These fields do not correct selection bias
or establish the confirmation assumptions.

## Judgment: what these optimizers may climb (Hypothesis)

An optimizer may search:

- instructions and criteria text;
- few-shot examples;
- decomposition and module arrangement;
- generator prompts and model choices;
- a bounded rubric used as a semantic metric, if that metric is independently
  validated.

Keep outside the search:

- authorization, tool grants, and irreversible-action policy;
- exact ontology and schema invariants;
- train/validation/test splits and frozen outcome labels;
- candidate sources and coverage guarantees;
- state-machine transitions and recovery rules;
- the final confirmatory threshold.

Do not ask an LM-program optimizer to tune perception, retrieval recall,
calibration, and application policy as one opaque objective. Each stage needs
its own evidence and acceptance test.

## The converging integration pattern

```text
input state
  → exact preparation and candidate construction
  → one batched bounded-decision step for typed fields
  → policy code
  → generative program for freeform leftovers
  → validation and observed outcome
```

Typed and freeform outputs should remain distinct even when a framework exposes
one prediction interface. Boolean-like, enum, and ordered fields can use a
decision provider; prose and code remain generative. If a later generated field
depends on typed results, pass those results as explicit inputs rather than
splicing them into hidden prompt state.

Constrained autoregressive fields are a valid alternative, but their schema
validity and token probabilities do not acquire a decision head's semantics.
Classical supervised models may be better for stable labeled fields. Span
extractors, rankers, and vision scorers keep their family-specific objectives.

## Design rules that transfer

- Validate field descriptions, criteria, labels, and duplicate keys before any
  model call.
- Keep threshold conversion in application policy. One global boolean threshold
  rarely matches different action costs.
- Preserve full distributions for evaluation; do not discard them after
  booleanization.
- Batch independent typed fields over shared state. Sequence only when later
  candidates depend on earlier answers.
- Include `other`/`none` when label coverage is open.
- Record provider/model, rubric, candidates, optimizer version, policy version,
  and dataset version.
- Treat provider errors as a distinct outcome. Do not silently relabel a
  generator or heuristic fallback as the primary decision model.
- Re-check state and authority before executing the chosen action; optimization
  does not remove time-of-check/time-of-use risk.

## Optimizers (GEPA / DSPy teleprompters): what to couple, what not

[GEPA](https://arxiv.org/abs/2507.19457) uses reflective feedback from program
traces to search prompts and maintains candidate tradeoffs. Its reported gains
are task- and budget-specific, not proof that reflection will improve this
judgment. Compare against a fixed prompt and a simpler search at equal total
evaluation cost; keep the final test outside the reflection loop.

A bounded judgment can occupy two different seats:

1. **Executor:** the optimizer improves criteria/examples for typed output, and
   the decision model executes that surface cheaply.
2. **Metric:** the decision model scores a generated artifact against a narrow
   rubric while the optimizer searches the generator program.

Do not collapse these seats. If the same model both generates labels and judges
the candidates trained on those labels, the loop can optimize imitation rather
than real outcomes.

For a semantic metric:

- first measure repeated-run variance on frozen outputs;
- validate against independent human or outcome labels;
- separate search, threshold selection, and confirmation data;
- cap metric calls and account for correlated repeated judgments;
- inspect failures, not only the optimizer's aggregate score.

[sutro-sh/jev-align](https://github.com/sutro-sh/jev-align) is a useful example
of the inverse arrangement: an optimizer edits the function definition, humans
supply acceptance labels, and the bounded model is the executor. The score must
not auto-accept its own new definition.

## Calibration and measurement obligations

Before relying on an optimized decision surface, evaluate:

- accuracy/F1 or task-appropriate discrimination with class/base-rate context;
- Brier or log loss and reliability plots where probabilities matter;
- selective risk versus coverage across frozen thresholds;
- subgroup, paraphrase, option-order, and distribution-shift slices;
- candidate-generation recall and no-match behavior;
- invalid output, provider failure, and fallback provenance;
- end-to-end cascade and trajectory success.

“Trained for calibration,” a low ECE on one split, or a temperature value is not
a general guarantee. Re-measure after changing rubric, candidates, model,
runtime, or population. A shared comparison dataset such as
[open-jev-laya-bench](https://huggingface.co/datasets/pngwn/open-jev-laya-bench)
can test instrumentation, but it does not replace product data.

Freeze the confirmatory threshold before the final run. Do not select the best
row from a sweep and report that same row as independent evidence.

## Where the gaps are

Framework adapters often prove only that typed fields execute. They may not
provide:

- per-action thresholds;
- independent calibration data;
- candidate-coverage accounting;
- robust error/fallback provenance;
- optimizer-aware split discipline;
- trajectory-level evaluation;
- authority/state re-checks.

Treat missing items as engineering work, not implied framework behavior. Read
the actual adapter and current framework docs before writing integration code.

## Typed control plane around DSPy (not more knobs)

The control plane stays ordinary, reviewable code:

```text
decision output
→ ontology validation
→ deterministic security and business overrides
→ per-action threshold / abstention
→ state transition
→ tool allowlist and authority check
→ optional generator draft
```

The generator may write after route and action are fixed. It cannot introduce a
new route, tool, or permission. [jev-dspy-control-plane](https://github.com/manikanda-kumar/jev-dspy-control-plane)
illustrates comparing typed backends under a shared ontology; its offline wiring
checks are not proof of model quality.

## Specialist as metric vs few-shot as classifier

Use a hosted few-shot decision API as a baseline when it meets the task and
deployment constraints. Train a specialist when measured task performance,
privacy, latency, scale, or control needs justify the data and maintenance cost.
Either surface may supply a full distribution; consuming it is not by itself a
reason to train. Qualify score meaning, calibration where needed, and the
downstream policy in the intended runtime.

Qualification requires held-out independent labels or observed outcomes.
Where the source's terms allow it, training may use provider or teacher
distributions as features, weak labels, or distillation targets; those targets
are not independently established truth. Check terms before any provider output
enters a training path (labels, targets, features, filtering, or example
selection). TypeSafe's Master Customer Agreement §2.3(b) (updated 2026-09-19)
bars using Jev Output for model distillation, to train a model imitating it, or
to develop a competing product. Treat every path above as covered unless the
contract owner confirms a use is allowed.
[jev-triage](https://github.com/ThyFriendlyFox/jev-triage) captures the useful
pattern, uncertainty choosing what deserves expensive labeling while real
outcomes remain the target; its uncertainty source needs the same check.

Compare specialists and hosted decisions on the same holdout and deployment
runtime. Include serving latency, cold start, human-label cost, retraining, and
fallback—not merely per-call price.

## ProgramAsWeights: materializing a judgment locally (Hypothesis)

Compiling a stable fuzzy program into a small local artifact is plausible when
the surface is high-volume and slow-changing. It is premature when criteria,
labels, or population move daily.

A safe materialization loop is:

```text
independent gold + optional teacher features (terms permitting)
→ train/compile local artifact
→ frozen holdout and shift tests
→ shadow comparison in the deployment runtime
→ policy-controlled promotion
→ drift monitor and rollback
```

Do not claim equivalence because a local service shares a wire format or agrees
on a small sample. Distillation can inherit teacher errors; teacher agreement
alone does not establish correctness. Evaluate against independent outcomes.

[jevloop](https://huggingface.co/spaces/async-dime/jevloop) is a distinct idea:
code searches deterministic edit operations using a full-distribution critic.
It is not an Ax/DSPy prompt climb, and mock mode demonstrates control plumbing,
not judgment quality.

## Cascade and optimizer acceptance card

```text
Program slice being optimized:
Typed executor and generator roles:
Exact control-plane invariants:
Evidence/candidate source and coverage gaps:
Independent gold and split discipline:
Metric validity and repeated-run variance:
Threshold selection and frozen confirmation rule:
Provider error and generator/human fallback:
Authority/state re-check before action:
Stage metrics and full trajectory metrics:
Expected cost: model + latency + fallback + human + recovery:
Rollback / drift trigger:
Result that would reject the integration:
```

The optimizer's best score is not the acceptance criterion. The product must
improve on a frozen baseline under realistic errors, fallbacks, and trajectories.
