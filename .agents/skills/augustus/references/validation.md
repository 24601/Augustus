# Validation: decisions, policies, and complete workflows

An evaluation should determine whether this insertion improves the user's
outcome at acceptable cost and risk. A valid response shape, a passing
unit test, and a successful model call answer different questions.

## The design gate

Before inference, name the baseline, evidence source, representable answer,
action owner, costs, fallback, and a result that rejects the proposal.
Keep exact constraints enforced regardless of model output. Record model,
rubric, candidate-source, calibration, policy, and runtime versions.
For each policy-consumed number, keep a score record: event/output semantics,
resolved model/checkpoint, question and label-set hashes, population/window,
calibrator, operating threshold, held-out metrics with intervals, and recheck
trigger. A changed model, rubric, label set, route, or population requires
requalification rather than inheriting a previous threshold.

Separate three data uses: development (including prompt search), calibration
and policy selection, and final evaluation. Split by source entity, document,
user, template, or time where rows share information; a random row split
can leak near-duplicates. Keep a test-set contamination ledger. Labels from
a teacher model are measurements with their own errors, not independent
gold. Use adjudication or observed outcomes appropriate to the task.

## Choose measurements by the consumer

| Consumer | Measure | What it does not establish |
| --- | --- | --- |
| Binary/categorical prediction | Proper scores (Brier, log loss), confusion matrix, base rate | Optimal action policy |
| Probability threshold | Reliability with counts, calibration by slice, action errors | Per-case correctness or transfer to new traffic |
| Abstaining classifier | Risk versus decided coverage; escalation cost and delay | Safety merely because coverage is low |
| Ranker | nDCG, recall, pairwise errors, downstream utility | Absolute calibrated probabilities |
| Extractor/perception | Span precision/recall, localization/tracking errors | Correct downstream decisions |
| Stateful workflow | Completed outcome, trajectory failures, recovery, total cost | Reliability inferred from isolated steps |

Include the cheap baseline: existing rules, majority/base-rate predictor,
classical supervised model, or existing workflow. For the same task compare
matched evidence, candidates, budgets, and label splits. Include appropriate
generative baselines if they are credible alternatives; architecture labels
do not disqualify a competitor. A public leaderboard is candidate discovery,
not a deployment winner.

ECE depends on binning, sample size, and the statistic being calibrated.
Report bin definitions and counts, proper scores, and action errors beside
it. Low ECE can coexist with poor discrimination; high AUC can coexist with
poor calibration. Multiclass top-label calibration, classwise calibration,
and binary event calibration are different quantities. Do not compare
incompatible channels as one metric.

Report uncertainty on paired differences. Respect clustering when resampling
documents, tasks, or trajectories. A confidence interval crossing zero is
not proof of equivalence; use a prespecified equivalence/noninferiority
margin and sufficient power. Zero observed failures is not zero failure
probability. State sample size and the range still compatible with it.

## Costs, abstention, and operating points

For calibrated `p = P(y=1 | evidence)`, correct actions with zero loss,
false-positive cost `C_FP`, and false-negative cost `C_FN`, the binary Bayes
threshold is `C_FP / (C_FP + C_FN)`. These assumptions matter. If correct
actions have costs, utilities vary by case, or `p` is uncalibrated, use the
full expected-loss calculation and validate it.

Abstention is an action with a handler, queue, cost, delay, and possible
error. Compare `L(positive) = (1-p) C_FP`, `L(negative) = p C_FN`, and the
specified loss of abstention. A reject band derived from constant review
cost assumes the stated review behavior; it does not make a human perfect.
Measure reviewer accuracy and queue capacity separately. Record provider
errors and timeouts as explicit events, not low-confidence predictions.

Choose operating points on calibration/validation data and freeze them
before final evaluation. Report both sides of the policy, abstentions,
decided coverage, selective error, and total population cost. If no cases
are decided, selective error is undefined, not zero. Include always-positive,
always-negative, and defer-all baselines when they are feasible policies.

## Conformal prediction and risk control

Conformal prediction can wrap a score into prediction sets with marginal
coverage under exchangeability and the selected method's assumptions.
It does not make the underlying scores calibrated or guarantee every
subgroup, every case, or an adaptive trajectory. A singleton set is not an
authorization. Review the actual theorem and calibration protocol before
claiming a guarantee. Start with
[the conformal introduction](https://arxiv.org/abs/2107.07511).

[Conformal risk control](https://arxiv.org/abs/2208.02814) extends this idea
to expected monotone losses. Define the loss, boundedness, monotonicity,
sampling assumptions, and target population; do not automatically apply
its guarantee to conditional selective error, which need not be monotone.
Repeated policy selection and distribution shift need their own valid
procedure. Evaluate efficiency (set size, coverage, review volume) as well
as validity. Ordinary threshold sweeps in this repository do not implement
conformal guarantees.

## Behavioral stress tests

Test candidate removal, no-match and unknown cases, option-order shuffles,
irrelevant-option additions, paraphrase pairs, missing/conflicting evidence,
hostile instructions, truncated inputs, unsupported languages, and stale
observations. Record whether the **action** changes, not just the score.
An API need not promise invariance for stability to matter to the product.

Exercise malformed responses, non-finite scores, duplicate IDs, unsupported
operations, provider outages, and fallback activation. Distinguish primary
model outcomes from fallback outcomes. End-to-end success must include all
attempts, retries, failures, and human work, not only accepted cases.

## Eval & hill-climb

Freeze the taskset and success criteria; define each stage's input/output
contract; measure stages and the complete workflow; improve one controlled
component at a time. Include perception, retrieval, judgment, policy, and
execution. A judgment-stage gain may lose at the product level through
poor recall, extra calls, slow fallback, or correlated errors.

Tools such as jevals can organize decision examples; Harbor can organize
agent tasksets, harnesses, and runtimes; DSPy/Ax/GEPA can optimize supported
program components. None is a quality certificate or mandatory substrate
for non-agent domains. Use a reproducible evaluation appropriate to the
task, with discriminating success criteria and retained artifacts.

For cascades and routing, report conditional accuracy on the actual routed
population, referral rates, total latency/cost, and final success. Repeated
use of correlated judgments needs trajectory evaluation. Do not multiply
per-step accuracies into a success guarantee. Use actual rewards for bandits;
model confidence cannot substitute for observed reward.

Shadow mode records proposed actions while the current policy acts. It can
expose disagreement and workload, but cannot directly observe outcomes of
actions that were never taken. Use an appropriate controlled rollout or
causal design before claiming counterfactual benefit. Monitor distribution,
policy overrides, error slices, and escalation load after deployment.

## Offline evaluator

The bundled [binary evaluator](../scripts/evaluate_decisions.py) reads JSONL
with unique nonempty `id`, finite `p` in `[0,1]`, binary `y`, optional string
`group`, and optional `p_base`. It checks input, reports Brier/reliability,
and supports explicit policy analysis. It does not call a model.

```bash
python3 scripts/evaluate_decisions.py --help
python3 scripts/evaluate_decisions.py --self-test
python3 scripts/evaluate_decisions.py labels.jsonl --lower-threshold 0.2 --upper-threshold 0.8 --cost-fp 5 --cost-fn 2 --cost-abstain 0.5
```

Run from the installed skill directory. Full paired baseline comparison
requires `p_base` on every row. Quantile ECE keeps identical probabilities
in one bin, so bins may be uneven or fewer than requested. Label all
cost-based selection on a file as in-sample policy fitting; freeze the
selected policy and use a different file for final reporting. The tool
cannot verify label provenance, data independence, or deployment fitness.

The example thresholds and costs are illustrative, not recommendations.
Complete binary threshold reports use `action_rate` for the positive-action
fraction; the old programmatic `coverage` alias is deprecated. Selective
reports instead use `decided_coverage`, with inclusive negative/positive
boundaries and abstention strictly between them. The zero-action comparator
is an explicit `always_negative` policy. Abstention cost is caller-specified;
the evaluator does not simulate perfect human review.
Binary `log_loss` is unclipped: an exact zero probability on an observed
outcome reports `inf`, not an arbitrary epsilon-adjusted success. The helper
does not compute intervals, per-group reports, or a full risk-coverage curve;
the presence of a `group` field does not establish slice evaluation.

## Acceptance and evidence status

Record the hypothesis, baseline, pinned inputs, commands, observed results,
limitations, and reject/accept decision. Use Contract, Reported, Reproduced,
Hypothesis, or Unknown consistently. A reported experiment becomes
reproduced only when the relevant run and artifacts exist. Passing repository
lint proves structural checks passed; behavioral skill quality still needs
independent realistic scenarios and review.
