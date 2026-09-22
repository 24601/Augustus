# Formal, semi-formal, and crossover placement

This card places bounded model judgment relative to proof, model checking,
contracts, runtime verification, and systematic testing. TypeSafe Jev is the
default hosted decision-model exemplar; it is not a prover. Tool documentation
owns syntax and current capabilities.

Statuses: **Formal claim** only when a named formal tool establishes it under a
stated model/logic/bound; **Empirical result** when a reproducible test ran;
**Hypothesis** for a proposed judgment placement. Never promote a hypothesis
because the output is typed or confident.

## 1. Judgment vs proof ownership

| Claim | Evidence required | Owner |
|---|---|---|
| Model has no counterexample to property P within scope/bound | completed model-check/model-find result and exact scope | model checker/finder |
| Program satisfies contract P | checked proof obligations in the trusted fragment | verifier/proof assistant/kernel |
| Implementation did not violate P in explored runs | reproducible systematic tests and searched schedule/fault space | DST/PBT/systematic tester |
| Production trace violates a temporal property | authoritative events and runtime monitor | runtime verifier |
| Artifact appears to fit class/rubric R | evaluated typed judgment | model evidence + policy |

```text
proof / model checking / contracts -> formal claim over model or fragment
DST / PBT / simulation             -> searched executions; seed is evidence
judgment model                      -> belief about supplied state
code / policy / interlock           -> authority, effects, stop criteria
```

Judgment is a **sensor**. Proof/types are **constraints**. Systematic testing is
a **searchlight**. Policy is the controller and code is the actuator. A model
may prioritize proof obligations, counterexamples, or traces; it cannot discharge
them. If removing the model call leaves no independent enforcement of the
claimed safety property, the formal boundary is suspect. A policy may consume
model evidence without making that evidence a proof.

## 2. Design-time model finders and checkers

| Tool/family | What it establishes | Boundary | Judgment-shaped hole |
|---|---|---|---|
| Alloy Analyzer | relational instances/counterexamples in a finite signature scope; Alloy 6 also checks temporal traces | record object bounds, temporal mode, backend, and completed result; not arbitrary object counts or deployed code | cluster or prioritize instances (**Hypothesis**) |
| TLA+ with TLC | explicit-state exploration of a TLA+ spec | state space/config and modeled behavior | map logs to behaviors; triage counterexamples (**Hypothesis**) |
| TLA+ with Apalache | symbolic SMT-backed checking/analysis of supported TLA+ fragments | bounded/symbolic assumptions and encoding | prioritize properties/outputs (**Hypothesis**) |
| Quint | executable specification language with simulation and checker integrations | simulation is not verification; backend determines claim | UI/trace triage (**Hypothesis**) |
| P | asynchronous state machines plus systematic testing | explored schedules of the P model/program | failing-schedule clustering (**Hypothesis**) |
| NuSMV family | CTL/LTL checking on encoded finite-state model | correctness of model and property encoding | result triage (**Hypothesis**) |
| PRISM family | probabilistic model checking of DTMC/CTMC/MDP models | probabilities belong to the mathematical model, not model judgment | requirements/results triage (**Hypothesis**) |
| Event-B/Rodin | refinement and generated proof obligations | discharged obligations for written refinements | prioritize failed obligations (**Hypothesis**) |

### Alloy Analyzer vs Apalache (do not collapse)

- **Alloy** analyzes relational models in a finite signature scope.
  [Alloy 6](https://alloytools.org/alloy6.html) supports bounded temporal checking
  and, with a suitable backend, complete checking of all traces in that finite
  scope. Object bounds and the temporal horizon are different limits.
- **Apalache** is a symbolic model checker/analyzer for TLA+ using SMT-based
  techniques for supported fragments and tasks.
- **TLC** explicitly explores states of a TLA+ specification.

They differ in modeling language, semantics, solver strategy, and the claim a
green run supports. “The spec looks right” from a decision model occupies none
of these seats. Record tool version, model, property, configuration, scope or
bound, and result.

### Runtime detection vs enforcement

A trace monitor can detect a violation without preventing it. Blocking an
irreversible effect requires a suitable interlock at or before the effect
boundary, not merely a later alarm. State the enforceable property, timing,
authoritative observations, fallback, and recovery assumptions; a finite trace
may leave a temporal claim pending. [Execution-monitor theory](https://www.cs.cornell.edu/fbs/publications/EnfSecPols.pdf)
is conditional on its enforcement model. The concrete placement and falsifier
are in `mappings.md` §12.

### Semi-formal artifacts (shared vocabulary, not enforcement)

State diagrams, decision tables, ADRs, hazard analyses, schemas, and executable
examples can sharpen shared understanding. They become enforcement only when a
machine or accountable procedure checks them. Judgment may help fill or triage
them, but the artifact's review and execution path determines authority.

## 3. Deductive and contract languages

| Tool/family | Formal owner | Potential judgment placement |
|---|---|---|
| Dafny/Boogie/SMT | program versus written pre/postconditions, invariants, termination obligations | rank modules or classify failed VCs (**Hypothesis**) |
| JML/OpenJML | Java contracts through static/runtime checking modes | prioritize alarms; checker owns result (**Hypothesis**) |
| Frama-C/ACSL | C analyses and proof obligations through selected plugins | triage alarms/precision issues (**Hypothesis**) |
| SPARK/GNATprove | Ada/SPARK flow and proof of contracts in supported subset | prioritize obligations; verifier remains authority (**Hypothesis**) |
| Lean/Coq/Isabelle | kernel-checked terms/proofs in formal logic | retrieve lemmas or rank repair candidates (**Hypothesis**) |

A failed verification condition is a structured object with hypotheses, goal,
and location. Ranking it is in class. Answering “the lemma holds” instead of
producing a checked proof is **Rejected**.

Theory preconditions are part of the result: trusted computing base, logic
consistency assumptions, annotation adequacy, supported language subset, and the
relationship between verified model and deployed implementation.

## 4. Deterministic simulation testing (semi-formal trio)

Systematic or deterministic simulation testing explores executions and seeks
reproducible counterexamples. It is not proof. A found failure plus seed/trace is
high-value evidence; a clean campaign means only that the searched executions
did not violate the stated properties.

| System/style | Owns | Judgment may help with |
|---|---|---|
| Antithesis-style DST | deterministic whole-system execution, faults, properties, replay | cluster/review failing timelines (**Hypothesis**) |
| Resonate-style layered verification | durable protocol semantics, reference/differential tests, SDK/systematic testing as separate layers | prioritize divergent traces; never settle promises (**Hypothesis**) |
| PufferLib/environment simulation | fast environment rollouts and observed rewards for learning/evaluation | curriculum, trace triage, bounded state classification (**Hypothesis**) |

The important distinction is not the brand but the ownership:

- environment supplies transitions and observations;
- property/oracle supplies pass/fail evidence;
- replay supplies reproducibility;
- judgment may prioritize attention;
- policy decides response.

Do not launder a learned reward, “done” score, or trace-health judgment into the
environment's ground truth. Evaluate triage by unique-bug recall at a fixed human
budget, not by agreement with itself.

## 5. Harms

### TOCTOU-of-Noul

State is judged at `t0`; an action happens at `t1`; files, prices, permissions,
or identities change. A soft score was never an atomic authorization check.

Mitigation order:

1. Put the real constraint in code, authorization, sandbox, transaction, or
   compare-and-swap.
2. Re-read authoritative state at use time.
3. Probe the outcome after effects.
4. Use earlier judgment only for routing or review priority.

### Soundness theater

- bounded search sold as unbounded proof;
- simulator run described as model checking;
- tautological, vacuous, or irrelevant properties;
- proof of a model that omits the failure mechanism;
- typed/model probability presented as a safety case;
- runtime/DST silence described as correctness;
- listwise affinity thresholded as permission;
- “type-safe” confused with factually correct or authorized.

Run mutation/vacuity checks: a meaningful property should fail on a seeded
countermodel or defect. Require the actual checker receipt, not prose saying it
ran.

### AI x formal methods (vibing specs and cousins)

Generative models can draft specs, invariants, annotations, repairs, and
explanations. Decision models can rank or triage them. Neither supplies formal
strength. The workflow must compile, run the checker, inspect counterexamples,
test non-vacuity, and review whether the model captures the real system.

The key economic distinction: reducing the cost of text that typechecks does
not necessarily reduce the cost of finding strong properties or faithful
abstractions. Treat AI-authored formal artifacts as candidate inputs.

### Help vs harm (keep this list short)

**Useful hypotheses:** property candidate ranking; counterexample clustering;
proof-obligation triage; spec UI; trace-to-model mapping; runtime anomaly sensor
beside a hard monitor.

**Rejected:** Noul as proof; judgment replacing permission; silent contract edits
that weaken the obligation; model-generated reward used as environment truth;
green summary without checker evidence.

## 6. Crossover metaphors (placement intuition)

- **NATM:** observations guide support; gauges are not lining.
- **Snap-fit:** tolerance is designed for reversible joints; pressure boundaries
  need stronger constraints.
- **Norman:** judgment helps evaluate visible candidates; forcing functions help
  execute irreversible intent.
- **Leveson/STAMP:** sensors inform controllers; safety constraints live in the
  control structure.

These are intuitions, not formal mappings. Preserve the source method's
precondition before transferring a metaphor.

## Decision-design extras (proof x judgment)

```text
Precise claim and its owner:
Model/spec/implementation relationship:
Scope, bound, fragment, or explored schedule space:
Formal property and non-vacuity/mutation check:
Judgment-shaped triage hole and supplied evidence:
Exact policy/constraint that survives model failure:
TOCTOU and post-action probe:
Statistical-validity test for the judgment:
Smallest result that rejects this composition:
```

## Hypothesis backlog (do not promote without a run)

- property suggestion pipeline with mutation score as acceptance metric;
- Alloy instance clustering with unique-structure recall;
- checker-first repair ranking for failed obligations;
- DST multiverse triage with unique-bug recall;
- runtime monitor plus conformal/selective soft sensor;
- durable workflow state classification beside exact settlement;
- trace-to-spec alignment with human-audited correspondence.

Related: `formal-semi-formal.md`, `mental-models.md`, `mappings.md` §§10–14,
`composition-algebra.md` positions 3 and 9, `boundary-audit.md`.
