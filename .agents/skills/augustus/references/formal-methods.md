# Formal, semi-formal, and crossover placement

This card is **where a System One judgment sits relative to proof,
model-checking, contracts, and simulation** — not a TLA+/Dafny tutorial
and not a TypeSafe API guide. Jev is the documented exemplar of the
judgment-class (`judgment-class.md`); the ownership split does not depend
on the vendor.

A curriculum list may later land as `FORMAL-METHODS-SYSTEM-ONE.md`. When
it does, fold named rows into the tables below. Until then this file is
the working map from the 2026-09-18 brief.

Status: **Contract** only for TypeSafe docs you re-read live. Tool
characterizations here are **Empirical recipe** (named docs) or
**Hypothesis** (placement). Metaphors are labeled as such: they place
judgment; they are not mappings until a named precondition survives
(`methods-catalog.md`).

## 1. Judgment vs proof ownership

Three different claims, three owners. Mixing them is the rejected design.

| Claim | What would make it true | Owner |
|---|---|---|
| This *model* has no deadlock / this *function* cannot overflow | Exhaustion or a discharged proof obligation, relative to the model/annotations | Model-finder, model-checker, or deductive tool |
| This *implementation*, under these faults, never violated property P in the runs we searched | A reproducible counterexample or a long deterministic search that did not find one | DST / systematic testing. Absence of a bug is **not** a proof |
| This *state* looks like class C / satisfies rubric R, cheaply enough to run per item | A typed score, distribution, or label you can threshold | Judgment-class model + policy in code |

```text
proof / types / contracts     →  exhaustive over a model or a fragment
DST / PBT / linearizability   →  high-coverage search; counterexample is gold
judgment-class model          →  belief about a given state; never exhaustive
code / policy / interlock     →  side effects, authorization, stop-criteria
```

Judgment is a **sensor**. Proof and types are **constraints**. DST is a
**searchlight**. Code is the **actuator**. A Noul is allowed to inform
the controller; it is not allowed to *be* the constraint.

Existing grammar: composition-algebra position 9 (verifier) — verdicts
are evidence, not enforcement. Position 3 (gate) — a filter is not
authorization. Estimate ≠ measure: irreversible acts concede only to a
post-execution probe.

**What transfers** into a mixed stack: triage which counterexample,
property, or failing seed a human looks at first; score whether a
production trace resembles a spec behavior; lint an artifact against a
*named, project-written* rule (`mixed-architecture.md` preference lint).
**What does not:** closing a proof obligation, replacing TLC/Apalache/
GNATprove, or treating "DST hasn't failed this week" as a safety case.

Counterexample: "formally verify this agent with Jev." That sentence
names the wrong owner. Test: if removing the judgment-class call would
change what the system is *allowed* to do, the design is wrong
(composition-algebra rule 4).

## 2. Design-time model finders and checkers

These tools exhaust (or symbolically search) a **model you wrote**. They
do not judge production text. Docs, not this card, own syntax.

| Tool | What it actually does | Exhausts | Judgment-shaped hole | Stays in the tool |
|---|---|---|---|---|
| [Alloy](https://alloytools.org/) | Relational modeling; SAT/SMT *finds* instances and counterexamples in a finite scope | Small scopes. A green check is "no counterexample in this bound" | Which scope; is this instance interesting; cluster counterexamples | Analyzer, facts, scopes |
| [TLA+](https://lamport.azurewebsites.net/tla/tla.html) / TLC / Apalache | Temporal logic of actions; check invariants and (some) liveness on a state machine | Finite instances / symbolic unrolling of *the spec* | Which property is "obvious" vs "subtle"; map logs to behaviors | Spec, checker, refinement mapping |
| [Quint](https://quint.sh/docs/what-does-quint-do) | Executable fragment of TLA with programming-style syntax; simulator + Apalache/TLC | Same as TLA+ when you *verify*; `quint run` is a simulator, **not** a proof ([Quint FAQ](https://quint.sh/faq): no TLAPS) | Same as TLA+; simulator traces are DST-adjacent | Spec, types/effects, checker |
| [P](https://p-org.github.io/P/) | Async event-driven state machines; systematic testing of P programs | Explored schedules of the P program, not the handwritten C# you forgot to model | Which monitor; which failing schedule to inspect | P checker, runtime |
| [NuSMV](https://nusmv.fbk.eu/) | Symbolic SMV; CTL/LTL on finite-state models | The finite Kripke structure you encoded | Encoding choices; which property to add after a miss | Model, engines |
| [PRISM](https://www.prismmodelchecker.org/) | Probabilistic model checking (DTMC/CTMC/MDP) | The Markov *model*. Model-p is not a Noul | Interpreting model probabilities vs a judgment-class p; which rewards | Model, engines |
| [Event-B](https://wiki.event-b.org/index.php/Main_Page) / Rodin | Set-theoretic modeling + refinement; proof obligations between levels | Discharged POs for the refinement you wrote | Which PO is "prover timeout" vs "spec too weak" vs "real bug" (**Hypothesis** until labeled) | Rodin, provers |

Rule: a System One model may sit *around* these tools (triage, route,
explain a counterexample to a human). It may not sit *instead*. Quint's
own split is the teaching example: simulator finds bugs faster; model
checker is what lets you claim the invariant on that model
([What does Quint do?](https://quint.sh/docs/what-does-quint-do)).

## 3. Deductive and contract languages

These prove **code against annotations**, not vibes against a README.

| Tool | What it actually does | Judgment-shaped hole | Stays in the tool |
|---|---|---|---|
| [Dafny](https://dafny.org/) | Verification-aware language; Boogie/SMT on methods vs contracts | Which module to annotate first; classify a failed VC | Verifier, annotations |
| [OpenJML](https://www.openjml.org/) / JML | Design-by-contract for Java | Same shape: rank hot methods; never "this Java looks safe" | ESC, runtime assertions |
| [Frama-C](https://frama-c.com/) / ACSL | C static analysis plugins; WP, value analysis | Which alarm is a true overflow vs a precision miss (**Hypothesis**) | Kernel, plugins, ACSL |
| [SPARK](https://www.adacore.com/about-spark) / GNATprove | Ada subset; flow + proof of contracts | Same as Dafny, at higher assurance | GNATprove, SPARK subset |

A failed verification condition is a *structured* object (goal,
hypotheses, location). Ranking those is in-class. A Noul "the lemma
holds" is out of class — that is a proof obligation with the prover
deleted.

## 4. Deterministic simulation testing (semi-formal)

DST is the missing middle: not a proof, not a unit test, not a
judgment. It **searches executions** under a deterministic scheduler
and asks whether *stated properties* held. A found bug is a
reproducible seed. A clean run is coverage of that search, not
correctness of the program.

| System | What it actually does | Judgment-shaped hole |
|---|---|---|
| [Antithesis](https://antithesis.com/docs/introduction/how_antithesis_works/) | Whole-system deterministic hypervisor; faults + inputs; property-based exploration; reproducible timelines | Cluster failing timelines; is this the same incident; which property to add after a miss |
| [Resonate](https://docs.resonatehq.io/evaluate/how-resonate-is-tested) | Three layers: executable Lean 4 protocol spec, differential testing vs an in-memory oracle, DST of the TypeScript SDK (seeded faults, CI replays the seed twice to catch nondeterminism) | Same as Antithesis for the DST layer; the Lean spec is still a spec |

Resonate is the ownership split in one product: Lean owns the protocol
claim; DST owns "this SDK, these faults, this seed"; unit tests own the
rest. A judgment-class model is not a fourth way to skip any of those
layers. It can sit where OpenSmoke already sits: cheap flags over every
failing seed so a human (or an LLM autopsy) only sees the cluster.

Rejected: "we ran DST, then Jev said the traces look healthy, ship it."
The property ran or it did not. Judgment does not get a vote on P.

## 5. Harms

### TOCTOU-shaped soft checks

Time-of-check-time-of-use: you judged state at t0 and acted on it at
t1. The world moved. Classic: `stat` then `open`. Agent-shaped: Noul
"this plan is safe" → tools run → files, prices, and permissions
change → execute. Also: using a Noul *as* the lock — the check was
never atomic because it was never a check.

Fix, in order: make the real interlock in code (types, auth, sandbox,
compare-and-swap); re-probe after the world can have moved
(composition: irreversible acts concede only to a post-execution
probe); treat the t0 judgment as advisory routing, not permission.
Fail-closed authorize cannot be a stale Noul.

### Soundness theater

Claiming a proof-shaped conclusion from a non-proof:

- Bounded check with a toy scope, sold as "verified."
- Tautological properties that only restated the definition ([Hillel
  Wayne, March 2026](https://buttondown.com/hillelwayne/archive/llms-are-bad-at-vibing-specifications/):
  `canImport = P ∨ Q` then "prove" `¬P ∧ ¬Q ⇒ ¬canImport`).
- "Formally verified" marketing on a model that omitted the bug class.
- Noul 0.95 presented as a safety case. Calibration describes *groups*,
  in-distribution (`faq.md`; Archer Hume OOD collapse).
- "DST hasn't failed" as correctness.
- A listwise or CLIP affinity as fail-closed authorize
  (`judgment-class.md`).

If the artifact would still say "verified" after you delete the
checker, it was theater.

### Vibing specs (Hillel)

[LLMs are bad at vibing specifications](https://buttondown.com/hillelwayne/archive/llms-are-bad-at-vibing-specifications/)
(10 Mar 2026): a growing share of public TLA+ (he clocked **4% of
GitHub TLA+ files mentioning Claude**) is unrun, non-compiling, or
only "obvious" invariants (forgot a guard) — not the *subtle*
concurrency, nondeterminism, and liveness properties that are why you
bothered. Experts can use LLMs as a force multiplier *because they run
the checker and can demand a strong property*. Beginners get green
syntax and tautologies.

Augustus implication: an LLM-written spec plus a System One Noul "does
this spec look good?" is **double theater**. The checker, DST harness,
or prover ran, or it did not. Judgment may triage *outputs of* those
tools. It may not certify the spec.

## 6. Crossover metaphors (placement intuition)

Portable, not SWE-only. The general design-intuition card is
`mental-models.md` §crossover. Repeated here only as they apply to
**proof vs judgment**.

**NATM / observational method.**
[New Austrian tunnelling method](https://en.wikipedia.org/wiki/New_Austrian_tunnelling_method):
you do not prove the mountain in advance. You excavate a round,
*instrument* deformation, adapt support, stop if the readings demand
it. Judgment = the cheap, frequent instrument reading (semantic, noisy).
Lining, bolts, and stop-criteria = code, policy, proof. Full-traffic
judgment (per-hunk, per-step, per-frame) is NATM instrumentation.
Treating a strain gauge as a certificate that the mountain is stable
is the harm.

**Snap-fit.**
A designed undercut plus designed deflection: the joint *clicks* or it
does not — that click, once seated, is a **probe** in the mechanical
domain. The *choice of where a snap-fit is allowed* (toy housing vs
pressure vessel) is the placement question. Judgment is designed give:
acceptable slop on reversible joints. Proof, types, and sandboxes are
fasteners and welds. Do not snap-fit a fail-closed authorize.

**Norman — gulfs of execution and evaluation.**
[Two UX gulfs](https://www.nngroup.com/articles/two-ux-gulfs-evaluation-execution/)
(Hutchins, Hollan, Norman; *Design of Everyday Things*): execution is
"can I do the thing I meant?"; evaluation is "did it happen?" Judgment
shrinks the gulf of **evaluation** over candidates you already hold
("is this the hunk / the visible element / the log line?"). Forcing
functions — types, proofs, confirms, interlocks — shrink the gulf of
**execution** for irreversible acts. Knowledge in the world (AX tree,
diff, schema) beats knowledge in the head (caption the screenshot,
then judge). Pixel-free computer-use is Norman (`judgment-class.md`
vision pattern 1).

**Leveson — STAMP / STPA.**
Safety is a **control** problem, not a component-failure rate
([Leveson, STAMP intro](https://psas.scripts.mit.edu/home/wp-content/uploads/2016/04/STAMP-Intro-2016.pdf)).
Hazards are missing enforcement of safety constraints. A 99% Noul is a
*sensor*, not a *constraint*. Unsafe control action: the agent proceeds
because the model was confident. STPA asks what happens when the sensor
is wrong, delayed, spoofed, or TOCTOU. Org/safety placement: judgment
informs operators and cheap gates; it does not replace the constraint
in the control structure.

```text
NATM        instrument often; adapt support in code
snap-fit    designed give only where a miss is reversible
Norman      judgment evaluates candidates; forcing functions execute safely
Leveson     judgment senses; constraints live in the control structure
```

## Decision-design extras (proof × judgment)

When the request mixes formal methods with a System One model:

```text
What must remain exhaustive (proof / MC / types / DST property):
What is a sensor (judgment-class family + hole):
What is a control constraint in code/policy (Leveson):
TOCTOU: is check atomic with use, or is there a re-probe?
How we would detect soundness theater / tautological specs (Hillel):
Smallest experiment that could reject this split, not this vendor:
```

Propose two placements if the hole is mixed (e.g. TLA+ on the protocol
+ DST on the SDK + judgment triaging failing seeds). Do not invent a
hybrid "verified by Noul" API.

Related: `methods-catalog.md` verification rows; `composition-algebra.md`
positions 3 and 9; `mixed-architecture.md` preference lint; `faq.md`.
