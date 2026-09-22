# Mental models: placing typed judgment across domains

Augustus places **typed, bounded judgment** inside a larger decision system.
TypeSafe Jev (Choice / Score / Noul) is the default hosted exemplar; the
placement rules apply to the wider class of decision models. This is not an
API guide and it does not assume that every compatible-looking model is
calibrated or interchangeable.

```text
state -> model evidence -> explicit policy -> checked action -> observed outcome
```

The model estimates; policy authorizes. Exact work stays in code, rules,
ledgers, contracts, checklists, or physical controls. Open-ended writing stays
with a person or generative model. Proof belongs to proof tools. A typed output
does not move any of those boundaries.

Statuses: **Theory** is a classical result under stated preconditions;
**Reported** requires a named source; **Reproduced** requires an identified run;
**Hypothesis** needs local evidence; **Rejected** violates a boundary or a
method's preconditions. No empirical result transfers automatically.

## Pillars

| Pillar | Contribution | Governing question |
|---|---|---|
| Decision theory / selective classification | act, abstain, gather, escalate | Which act minimizes expected loss? |
| Calibration / cost-sensitive policy | reliability and action thresholds | Does this number mean what policy assumes here? |
| Value of information | decide whether to buy evidence | Can new evidence change the act enough to repay its cost? |
| MCDA | explicit criteria and trade-offs | Which criteria compensate, and which are vetoes? |
| Search / control | heuristic, sensor, state estimate | What remains exact in the loop? |
| Signal detection | separability versus criterion | Is failure evidence quality or policy placement? |
| Org / safety | sensor versus constraint | What prevents harm when the sensor is wrong? |
| Formal methods | proof, search, contracts | Is the claim exhaustive, bounded, or estimated? |

Pick the pillar from the decision hole, then the judgment family, then the
provider. Do not start from a vendor or benchmark.

## Decision theory and selective classification

Let the model return evidence about state `s`. Policy enumerates acts `a`, a
loss table `L(a,y)`, and abstain/gather/escalate acts:

```text
a* = argmin_a E[L(a,Y) | evidence(s)]
```

The model does not choose the loss table. Abstention has delay, human-load, and
missed-opportunity costs and must be evaluated too.

| Domain | Evidence | Policy-owned acts | Exact owner |
|---|---|---|---|
| SWE | hunk appears relevant | stage / skip / ask | diff and patch application |
| Business | lead appears valuable | call / nurture / drop | price, quota, CRM updates |
| Knowledge work | paper appears on-question | read / defer / discard | citation and source custody |
| Personal workflow | email appears urgent | reply / snooze / archive | send and calendar actions |
| Agent harness | step appears stalled | continue / retry / inspect | tool execution and probes |

These are **Hypotheses** until held-out local cases beat a non-model baseline.
A ranking or classifier family does not determine fail-open/fail-closed
behavior; the consequence of the act does. A failed reranker may preserve the
original order, while a failed low-stakes classifier may use a declared
fallback. Neither pattern grants the model authorization power.

## Boundary map: extractable from state (placement judgment)

Classify every question:

1. **Exact from state**: parse, count, compare, validate, or look up in code.
2. **Semantic from state**: a bounded model judgment may help.
3. **Needs outside knowledge or a new observation**: retrieve, measure, ask, or
   abstain; confidence cannot manufacture missing evidence.
4. **Open-ended construction**: a person or generator writes; a decision model
   may route or inspect the result.

Falsifier: remove or scramble the purported evidence. If output barely changes,
the question is prior-driven, underspecified, or outside the state boundary.

## Calibration and cost-sensitive thresholds

Calibration is a population property: among cases assigned probability `p`,
roughly `p` should be positive on the evaluated distribution. It does not
certify an individual case, survive shift automatically, or turn listwise
affinity into `P(permit)`.

For a calibrated binary probability and positive versus negative action, with
false-positive and false-negative costs `C_FP` and `C_FN`:

```text
t = C_FP / (C_FP + C_FN)
```

This is **Theory** if the probability is calibrated for the deployment
population and the loss table is adequate. Rebalancing training data does not
replace the policy calculation. Abstention adds boundaries derived from reject
cost, not a universal confidence cutoff.

Keep separate:

- **Statistical validity**: discrimination, calibration, shift, sample size,
  dependence, and uncertainty.
- **Action policy**: costs, reversibility, law, fallback, and authorization.

Test with reliability plots/Brier or log loss, ROC or precision-recall,
coverage-versus-risk, temporal/subgroup slices, and confidence intervals.
Choose thresholds on one split and report on another. Perturb option order,
wording, distractors, and candidate-set membership.

## Value of information

The value of another observation is improvement in the decision, not merely a
sharper score:

```text
EVSI = min_a E[L(a,Y) | current]
       - E_z[min_a E[L(a,Y) | current,z]]
buy z only when EVSI > cost(z)
```

This is **Theory** given credible outcome and observation-cost models. Using
model outputs as a numeric EVSI calculator is a **Hypothesis** until act/outcome
logs validate it. Re-asking can expose response variability, but supplies no
new world evidence on its own.

Examples: fetch a full paper only if the abstract leaves a decision live; run
an expensive diagnostic only if it could change treatment; invoke a generative
autopsy only for flagged traces; ask a customer only when exact CRM facts do not
already settle a hard rule.

## MCDA

Multiple-criteria decision analysis exposes criteria rather than hiding them in
one “goodness” score. Model evidence may populate semantic criteria; policy
owns weights, vetoes, and the choice:

```text
U(x) = sum_i w_i u_i(x)       # only if compensability is intended
```

Preconditions: criteria and rubric levels are stable, utilities are scaled as
claimed, and compensating trade-offs are legitimate. Hard exclusions are rules,
not huge negative weights. Read full Score distributions: equal expectations can
hide different tail risk. Falsify with weight-sensitivity, paraphrase,
missing-criterion, and dominated-alternative tests.

## Search and control (where judgment substitutes)

In beam search, A*, MCTS, hiring funnels, and literature snowballs, judgment may
be a prior, prune signal, comparator, or leaf estimate. The algorithm, budget,
transition model, and outcome probe remain application-owned. Validate any
simulator's scope and fidelity. A heuristic is not a
posterior; depth without a trustworthy simulator compounds guesses.

In control, the model is a sensor or state estimator. Policy owns hysteresis,
interventions, and termination:

```text
enter alert when p >= t_enter
leave alert when p <= t_exit      # t_exit < t_enter
```

This avoids chatter but does not prove stability. A post-action probe, not a
pre-action estimate, concedes an irreversible milestone. Evaluate the closed
loop, including stale observations and recovery, not isolated accuracy.

## Signal detection

Signal detection separates evidence quality from policy. `d'` measures class
separation under distributional assumptions; the criterion sets the operating
point from prevalence and cost. Accuracy confounds them and misleads on rare
events.

```text
model evidence -> ROC/PR behavior
policy criterion -> hits, misses, false alarms, correct rejections
```

Revisit the criterion when costs change and update probability estimates or
calibration when base rates shift; evaluate whether retraining is needed when
evidence quality or distribution changes. Moderation, fraud review, incident triage,
medical screening, and deadline detection share this structure, not thresholds.

## Org and safety (Leveson)

Safety is a control-structure property. Judgment may say “the note appears to
mention an allergy”; code, procedure, authorization, or a physical interlock
must enforce “do not administer without a checked allergy record.” Ask what
happens when the sensor is wrong, late, spoofed, unavailable, or evaluated at
`t0` while the action occurs at `t1`.

Rejected: confidence waives a safety constraint; a soft gate is the only
permission check; a clean verdict replaces an executable probe.

## Mechanism design and operations research

Semantic evidence may become one input to an allocation, matching, scheduling,
or routing problem; the mechanism and solver still own eligibility, capacity,
incentives, fairness constraints, and feasibility. A model's affinity score is
not a bid, entitlement, or proof of truthful reporting. **Hypothesis** until an
end-to-end comparison shows better outcomes without constraint violations or
distributional harm.

## Epistemology and evidence

Keep source evidence, model evidence, policy, and outcome distinct. A judgment
is a defeasible claim conditioned on the supplied state, not a new source fact.
Record provenance and versions; preserve raw distributions separately from
derived acts; let later policy replay the same evidence. Corroboration requires
new information or an independently justified channel, not merely a second
prompt over the same text.

## Crossover metaphors (general design intuition)

- **NATM**: frequent observations inform support changes; instruments are not
  structural lining.
- **Snap-fit**: designed tolerance belongs on reversible joints, not pressure
  vessels. Reversibility determines acceptable slop.
- **Norman**: judgment can shrink the gulf of evaluation over visible
  candidates; forcing functions shrink the gulf of execution.
- **Leveson**: sensors inform controllers; constraints remain in the control
  structure.

These are intuitions, not evidence. A metaphor becomes a mapping only when its
assumptions, owner, and falsifier are explicit.

## Domain gallery (exposure, not a product catalog)

| Domain | Candidate judgment | Non-model authority | Initial status |
|---|---|---|---|
| Context management | relevance per block | always-keep rules and recovery cache | Hypothesis |
| Retrieval | shortlist relevance | retrieval recall and citation custody | Hypothesis |
| Tool routing | best documented capability | grants, schemas, dispatch | Hypothesis |
| Formal workflow | counterexample triage | checker and property | Hypothesis |
| Inbox | urgency/aboutness | send/delete/calendar controls | Hypothesis |
| Operations | incident similarity | command structure and probes | Hypothesis |

## Decision-design extras (any domain)

```text
Desired behavior and current baseline:
State evidence available / missing:
Exact work and authority owner:
Narrow judgments and classical pillar:
Family and statistical-validity evidence:
Acts, loss table, fallback, and reversibility:
Constraint that survives model failure:
Smallest held-out experiment that could reject the placement:
```

Related: `mappings.md`, `methods-catalog.md`, `toolbox-mapping.md`,
`composition-algebra.md`, `formal-methods.md`, `judgment-class.md`.
