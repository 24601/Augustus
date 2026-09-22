# Formal / semi-formal — one screen

Canonical detail: `formal-methods.md`. This is an executive placement, not a
second doctrine.

**Claim.** Formal methods own precise claims over explicit models, logics, and
bounds. Systematic testing owns searched executions and reproducible seeds.
Decision models own fast semantic evidence about supplied state. **Policy and
the host own authorization and effects.** TypeSafe Jev is the default hosted
decision-model exemplar, not a proof tool.

```text
proof / model checking / contracts -> claim over a model or fragment
DST / PBT / simulation             -> searched executions; absence is not proof
runtime verification               -> property over authoritative event trace
decision model                     -> evidence about supplied state
code / policy / interlock           -> authority, effects, stop criteria
```

## Placement

| Need | Right owner | Optional judgment role |
|---|---|---|
| Find relational instances in a finite scope | Alloy Analyzer | cluster/prioritize instances |
| Check a TLA+ model | TLC or Apalache, according to task/fragment | triage counterexamples |
| Prove code against contracts | Dafny/OpenJML/Frama-C/SPARK/proof assistant | rank obligations or repairs |
| Search faulted executions reproducibly | DST/systematic tester | cluster failing traces |
| Monitor a stated trace property | runtime monitor | anomaly signal beside monitor |
| Prevent an enforceable violation | interlock/shield/controller with explicit timing and recovery assumptions | proposal only; cannot waive the constraint |
| Decide which artifact deserves attention | policy using model evidence | primary judgment role |

**Alloy vs Apalache:** Alloy uses finite relational scopes; Alloy 6 can check
bounded temporal traces or, with a suitable backend, all traces in that finite
scope. Apalache is an SMT-backed symbolic checker/analyzer for supported TLA+
tasks/fragments. TLC explicitly explores TLA+ states. Do not collapse object
bounds, temporal horizons, tools, or the claims their green runs support.

**DST boundary:** Antithesis-style deterministic execution, Resonate-style
layered protocol/oracle/SDK testing, and simulator environments such as
PufferLib can produce traces, properties, rewards, and reproducible failures.
They do not turn a learned “healthy” or “done” score into proof or settlement.

## Useful hypotheses

- rank candidate properties, then have a human approve and run the checker;
- cluster counterexamples or deterministic failing seeds while preserving
  unique-bug recall;
- rank failed verification conditions or repair candidates;
- map production traces to candidate spec behaviors for review;
- place a soft anomaly sensor beside preventive interlocks and authoritative
  outcome monitors; a post-action alarm cannot undo an irreversible effect;
- use mutation and vacuity tests to reject weak generated properties.

Each remains **Hypothesis** until its checker-backed acceptance test runs.

## Rejected designs

- Noul, classifier, ranker, or generator as proof;
- soft score as permission or safety interlock;
- bounded search marketed as unbounded verification;
- simulation or clean DST campaign described as correctness;
- tautological/vacuous properties or proof of the wrong model;
- listwise affinity treated as `P(permit)`;
- silent spec/contract edits that make the proof pass by weakening it;
- pre-action judgment accepted after state or authority changes
  (**TOCTOU-of-Noul**).

## Review card

```text
Claim and formal/test owner:
Scope, bound, fragment, or explored schedule space:
Property plus mutation/non-vacuity check:
Judgment triage role and statistical-validity test:
Constraint and authorization that survive model failure:
Authoritative recheck at use time and outcome probe:
Falsifier for the composition:
```

Crossover intuition: NATM gauges are not structural lining; snap-fit tolerance
belongs on reversible joints; Norman separates evaluation from execution;
Leveson separates sensors from safety constraints. Use these to place judgment,
not to claim proof.
