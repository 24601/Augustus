# Improve the data, model or program within a fixed budget

**Placement:** an application with a runnable incumbent, evaluator and candidate
surface. This is a search policy, not a claim that hill climbing converges to the
best system. Search assumes the development signal is useful; confirmation tests
that assumption on independent evidence. When it fails, keep the incumbent.

## Freeze what makes scores comparable

Record the starting incumbent's artifact and policy, target population, independent
unit, loss and hard constraints, evaluator version, data roles and actual hashes.
Set allowed edits, maximum trials/time/spend, per-run limits, no-progress stopping
rule and final acceptance plan. Protect confirmation access in the actual workflow;
writing “held out” in a manifest is not isolation. Use existing project tooling,
not a new orchestration framework.

An application can change many components without training new weights. Choose
the next trial from an observed failure:

| Observed failure | Candidate change | Evidence that would reject the hypothesis |
| --- | --- | --- |
| Inconsistent gold or missing context | Adjudicate/relabel a versioned subset, repair evidence collection | Independent audit still disagrees, or downstream errors do not improve |
| Rare costly failures or new population | Acquire targeted examples plus representative samples | Slice recall/utility remains poor, or common-case regressions exceed limits |
| Good ranking, wrong action tradeoff | Threshold/fallback change; calibration only if probability use needs it | Frozen policy costs or risk/coverage do not improve |
| Features miss domain distinctions | Encoder/head/feature change, then bounded fine-tune if justified | Equal-budget development comparison does not justify complexity |
| Semantic instructions or examples mislead | Prompt/rubric/example selection or bounded program edit | Independent outcome evaluator fails despite a better self-score |
| Useful model but slow serving | Batch, cache, quantize, change runtime or hardware | Tolerance, tail latency, memory or hard constraint regression |

Keep permissions, effect boundaries and acceptance criteria outside the optimizer.
A proposed loss/ontology change creates a new evaluation question, not an apparent
win over the old score. Correct a discovered scorer bug, invalidate affected
claims and rerun comparable candidates; do not preserve a bad evaluator merely
to keep its hash unchanged.

## Execute a real search loop

For each trial, state a falsifiable hypothesis, materialize the changed artifact,
run the actual application seam on paired development units, and store raw
predictions/actions, loss, violations, resource use and error slices. Compare each
candidate to the original incumbent as well as the current best. Keep failed and
interrupted trials with their reason; planned or unrun candidates have no scores.

Development rows may be reused, including in prompt reflection or hyperparameter
search. Mark the result descriptive; do not attach an independent-test guarantee
to the best of repeated searches. Fresh challenge data can expose overfitting but
is not compulsory every round. Change one mechanism when attribution matters;
bounded multi-component search is valid when interactions justify it. Count all
candidate, teacher, evaluator and human-label costs against the declared budget.

Stop when the next useful experiment is outside budget, improvements stall under
the specified rule, constraints fail, or enough evidence supports freezing a
finalist. Save the actual finalist bundle, not just its recipe. Refitting after
confirmation or changing a threshold produces a new candidate.

## Confirm on outcomes that did not select the candidate

Freeze finalist(s), sample size/design, comparison count, margin, loss, policy,
critical slice gates and tolerances before revealing confirmation outcomes.
Evaluate both finalist and incumbent on matched independent units. For repeated
rows within an account/query/episode, aggregate with the prespecified unit loss;
do not use row count as independent sample size. Name weighting and the population
it targets. A unit-weighted average is not automatically a request-weighted average.

Use adjudicated labels for predictive claims; use observed workflow outcomes and
a design that identifies the contrast for causal claims. Logged outcomes under
one action do not reveal what another action would have caused. Proxy/teacher or
fixture outcomes remain labeled as such, regardless of sample size.

For paired bounded losses, the companion
`scripts/compare_workflows.py` accepts this
small **search arithmetic fixture**, not evidence of a useful candidate:

```json
{
  "schema_version": 1, "phase": "search",
  "incumbent_id": "rules-v1", "candidate_id": "specialist-v1",
  "dataset_id": "fixture-v1", "outcome_definition": "cost per independent case",
  "sampling_unit": "case", "evidence_kind": "fixture", "loss_bound": 4,
  "pairs": [
    {"id": "case-a",
     "incumbent": {"loss": 4, "cost": 0, "latency_ms": 1, "violations": []},
     "candidate": {"loss": 0, "cost": null, "latency_ms": 3, "violations": []}},
    {"id": "case-b",
     "incumbent": {"loss": 0, "cost": 0, "latency_ms": 1, "violations": []},
     "candidate": {"loss": 1, "cost": null, "latency_ms": 3, "violations": []}}
  ]
}
```

```sh
python3 "$AUGUSTUS/scripts/compare_workflows.py" paired-outcomes.json
```

`AUGUSTUS` is the installed companion directory. Each side supplies `loss` in
`[0,loss_bound]`, nonnegative `cost`/`latency_ms` or null, and `violations` as a list
of strings. Pair IDs must be unique. Candidate-minus-incumbent mean loss here is
−1.5; that is descriptive arithmetic, not significance. Keep fallback/failed cases
and record `excluded_units`/`missing_outcome_policy` when relevant. The helper
cannot repair selection bias from omitted outcomes.

Confirmation changes `phase` to `confirm` and supplies prespecified `alpha`,
`minimum_improvement`, positive integer `comparison_count`, and
`sampling_design: "equal_probability"`. Choose the method before examining its
result: `hoeffding` uses the declared loss bound; `empirical_bernstein` also uses
paired spread; `sign_exact` requires losses in `{0,loss_bound}` and zero margin,
and tests direction only. `mode: "superiority"` seeks a loss improvement;
`"non_inferiority"` supports at most the declared acceptable worsening, not a win.
Read the companion's `references/optimizer-integration.md` for the full contract.

These are fixed-sample methods assuming independent representative units, frozen
policies and no adaptive confirmation reuse. Equal inclusion is not independence.
Oversampled or convenience data need a different analysis; do not label them equal
probability to obtain a result. Repeated peeking or multiple finalists require
their declared comparison/sequential plan. The helper checks schema and arithmetic,
not sample independence, label validity, causal identification, hard-SLA acceptance
or permission to deploy. Check those in the application.

Once confirmation outcomes influence a new candidate, they are spent for that
independent claim. Obtain fresh confirmation or use a justified adaptive-valid
procedure with its actual assumptions. If neither is affordable, report the
search result and retain the incumbent. Small data can still guide exploration;
it cannot manufacture a confirmatory guarantee.

## Use the ledger to check declarations, not to run the search

For a multi-round run whose declarations need replay, use the companion
`scripts/climb_ledger.py`:

```sh
python3 "$AUGUSTUS/scripts/climb_ledger.py" climb.json
```

Read its installed `--help` and schema before writing a ledger. It takes
`schema_version: 1`, immutable `config` with `evaluator_hash`, `split_hash`,
`anchor_id`, `max_rounds` and optional `budget`, plus ordered `rounds`. Each round
records `index`, `candidate_id`, `delta_vs_anchor`, evaluator/split hashes,
`challenge_row_ids`, optional `spend`, and named `probes` with `pass`, `fail` or
`not_run`. Store full external run/receipt identities alongside those declarations.

The companion's default challenge mode requires fresh rows. Use its explicit
`config.search_reuse: true` mode when rounds reuse descriptive development data;
do not relabel the same rows to evade freshness checks. Record explicit
`confirmation_row_ids` disjoint from search and a `frozen_finalists` list; only a
candidate actually run and independently accepted may be `confirmed_candidate`.
If an older installed helper lacks this mode, preserve search reuse in the
application's run records and update the companion before relying on its replay.
Do not make fresh labeling every round a universal training requirement.

The ledger executes no model, search, acquisition, hash verification or confirmation
test. Even `promoted_candidate` means a supported **declaration**, not that anything
was deployed or that the acceptance evidence is true. Verify actual hashes,
receipts and confirmation outside it. It does not replace the paired comparison
or the application's constraints. Likewise, a failed exploratory candidate can be
rejected without discarding otherwise valid trials; preserve its failure rather
than declaring its probes passed to obtain a promotion-looking terminal state.

## Retain or activate with a concrete reason

- **Candidate accepted:** report the confirmed contrast, all gates and costs,
  artifact/policy/evaluator/data versions, and limits of the evidence. Activate
  only within existing authority, initially shadow/canary where appropriate.
- **Incumbent retained:** state whether the challenger lost, breached a constraint,
  lacked independent evidence, or cost too much. Keep the useful candidate artifact
  and negative result without advertising an improvement.
- **Blocked/paused:** give the missing labels, permission, resource or unresolved
  definition. Do not turn a budget stop into a completed fit.

For activation, keep the exact incumbent bundle and rollback command, independent
outcome monitoring, drift triggers, fallback capacity and an accountable effect
boundary. Exercise correction/recovery through the application. A monitor after
an irreversible action detects harm; it does not prevent it. The final deliverable
is a working inference path and an evidence-limited decision, not a ledger status.
