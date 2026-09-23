# The toolbox sweep: how to find approaches and applications for a new primitive

This is a repeatable method for deriving placements from classical tools rather
than brainstorming product ideas. The sweep itself is a
**Hypothesis-generating method**. Each placement remains untested until a
recorded experiment supports or rejects it; lack of a disproof is not validation.

## Why toolbox substitution instead of brainstorming

Start from a method whose mechanics and preconditions you understand. Ask:

> Which component is a fast semantic judgment over a bounded answer space,
> given the available state?

Substitute only that component. Preserve arithmetic, search, solvers, proof,
authorization, effects, and outcome probes. This produces inspectable designs
because the classical method supplies the skeleton and the violated
precondition supplies the rejection test.

```text
known method -> component inventory -> judgment-shaped hole
-> placement -> explicit policy -> falsifying experiment
```

## The sweep procedure

1. **Pin the task and output contract.** Start with the decision and evidence.
   If a provider is already selected, re-read its live contract for semantics,
   limits, state envelope, batching, errors, and calibration claims. Do not
   infer semantic equivalence from a compatible API, constrained output, or
   softmax. Keep performance as a measurement, not a universal premise.
2. **Inventory one toolbox family.** Statistics, decision theory, search,
   operations research, signal processing, formal methods, control, human
   factors, economics, or a domain workflow.
3. **Write its components and preconditions.** For each component state what
   theorem or guarantee depends on it: independence, admissibility, stationarity,
   candidate coverage, calibrated probabilities, exact transitions, and so on.
4. **Test for a judgment-shaped hole.** It should be answerable quickly by a
   knowledgeable person from the supplied state, have a bounded answer space,
   and not require arithmetic, proof, missing knowledge, or open-ended writing.
5. **Place it using `composition-algebra.md`.** Operand, post-judge, gate,
   selector, comparator, prior, state estimator, metric, verifier sensor,
   discretizer, or budget signal.
6. **Classify the substitution.**
   - **Marginal:** replaces a heuristic, generative judge, or manual glance.
   - **Newly feasible:** enables a volume or cadence previously uneconomic.
   - **Invalid:** violates a boundary or destroys a method precondition.
7. **Separate evidence from policy.** Test statistical validity first; define
   acts, costs, reversibility, fallback, and authorization separately. Model
   output informs policy and never grants permission.
8. **Falsify before promotion.** Compare with a simple baseline on held-out,
   deployment-like cases; test perturbations and the entire action loop.

## Substitution patterns per family

| Family | Judgment-shaped component | What remains exact | Status |
|---|---|---|---|
| Decision theory | belief evidence for act/abstain/gather | loss table and argmin | Theory placement; local calibration empirical |
| Signal detection | noisy semantic evidence | criterion, ROC/PR, prevalence/cost | Theory placement |
| MCDA | named semantic criteria | weights, vetoes, Pareto analysis | Hypothesis per rubric |
| Search | branch priority/prune/leaf heuristic | frontier, budget, transitions, goal probe | Pattern shape; local Hypothesis |
| Control | state estimate | controller, hysteresis, interlock, probe | Pattern shape; local Hypothesis |
| Retrieval | relevance comparator | candidate generation and citations | Pattern shape; local Hypothesis |
| Formal workflow | counterexample/property triage | spec, checker, proof obligation | Hypothesis; never proof |
| Operations research | affinity/value feature | constraints and solver | Hypothesis |
| Experimental design | semantic rater | sampling, labels, statistics | Hypothesis per rater |
| Human workflow | attention/priority cue | role, authority, procedure | Hypothesis |

Standing invalid substitutions are listed under Rejected in `methods-catalog.md`.

## The application-finding procedure (top-down, domain-first)

1. Enumerate decision points where a human glances and answers quickly, or a
   boolean/enum/rank hides behind brittle heuristics.
2. Classify each as exact, bounded judgment, generation, missing observation,
   or authorization. Only bounded judgment is a direct candidate.
3. Apply the economics inversion without assuming a number: what design becomes
   practical if this judgment is materially cheaper/faster at the required
   volume? Measure the actual provider in context.
4. Shape state so each question has its evidence. Retrieve or measure missing
   facts; keep irrelevant context out; name candidate provenance.
5. Define policy: acts, loss table, thresholds, abstention, fallback, human role,
   reversibility, and exact constraints. Model family does not dictate failure
   policy.
6. Run a shadow or offline experiment, then a guarded end-to-end test. Evaluate
   action cost and outcomes, not just model accuracy.

Cross-domain examples:

- Knowledge work: broad search stays exact; semantic relevance reranks a
  shortlist; citations remain source-linked.
- Business: semantic fit becomes one feature; credit limits and capacity remain
  solver constraints.
- Personal workflow: urgency informs snooze/reply triage; send/delete remains a
  user-authorized effect.
- Software: model prioritizes failing traces; test runner and exit status own
  the result.
- Safety: model flags hazard cues; interlocks and trained operators own control.

## Falsification checklist

```text
Simple non-model baseline:
Representative labeled holdout and population slices:
Calibration/discrimination test appropriate to the output:
Option-order, paraphrase, distractor, and evidence-ablation tests:
Candidate recall and missing-option test:
Policy selected on split A and reported on split B:
Fallback measured, including human delay/error:
Action-level harm, cost, latency, and recovery:
Outcome probe independent from model evidence:
Result that would reject this placement:
```

## The second generator: the composition algebra

The sweep asks whether a classical method contains a judgment-shaped hole.
`composition-algebra.md` asks where judgment may sit relative to that component.
Crossing constructs with positions is useful only when each cell carries its
precondition and falsifier; otherwise it is metaphor multiplication.

## Escalation for very new problem shapes

When no mapping fits, identify the closest classical problem first: screening,
sequential testing, search, assignment, control, retrieval, measurement, or
verification. Study its assumptions, then rerun the sweep. If no bounded
judgment remains after exact work is removed, record the rejection. Grow
`mappings.md` one focused, evidence-labeled card at a time; keep vendor census and research history
outside this reference.
