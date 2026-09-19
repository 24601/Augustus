# Formal, semi-formal, and crossover placement

This card is **where a System One judgment sits relative to proof,
model-checking, contracts, and simulation** — not a TLA+/Dafny tutorial
and not a TypeSafe API guide. Jev is the documented exemplar of the
judgment-class (`judgment-class.md`); the ownership split does not depend
on the vendor. Portable frames for EU, VOI, MCDA, SDT, and org/safety
live on `mental-models.md`. Formal methods are **one pillar**, not the
skill.

Curriculum landed 2026-09-18
(`research/archive/curriculum/FORMAL-METHODS-SYSTEM-ONE.md` plus
1-pager, source list). Named rows are folded here. The one-screen
alias is `formal-semi-formal.md`. Do not duplicate doctrine.

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

Low- and medium-entropy decisions are where contracts, property tests,
and gates attach; high-entropy writing is where specs stay soft —
Atallah's buckets are product rhetoric, not an entropy meter
(`judgment-class.md`).

Judgment is a **sensor**. Proof and types are **constraints**. DST is a
**searchlight**. Code is the **actuator**. A Noul is allowed to inform
the controller; it is not allowed to *be* the constraint.

**Open weights vs a proprietary API (one check, not a doctrine).**
Holding the weights lets you run local differential tests and DST
around the decision boundary — same inputs, quant versus full
precision, candidate-set perturbations — because the artifact is on
disk. A proprietary decision API does not hand you that artifact;
probes stay black-box. Either result is still a sensor: a boundary
that moved is evidence about the model, not a discharged proof
obligation. An announced open-weight drop is **Watch**, not a shipped
checker (`research/notes.md` §31, §32, §33; placement card in
`judgment-class.md`). Hume's driver is healthcare AU data-residency /
deployment control, not a feud with TypeSafe. Holding those weights,
when they exist, still does not discharge a proof.
A constrained-AR softmax (TypeAR, pcdServer) is still a sensor: it is
not a discharged proof because the next token stayed in a declared set
(`notes.md` §42). A local kev pointer-softmax is the same sensor on the
trained decision-only path (`notes.md` §45).

Existing grammar: composition-algebra position 9 (verifier) — verdicts
are evidence, not enforcement. Position 3 (gate) — a filter is not
authorization. Estimate ≠ measure: irreversible acts concede only to a
post-execution probe. A Noul at t0 that authorizes an act at t1 is
TOCTOU-of-Noul (§5), not a discharged obligation.

**What transfers** into a mixed stack: triage which counterexample,
property, or failing seed a human looks at first; score whether a
production trace resembles a spec behavior; lint an artifact against a
*named, project-written* rule (`mixed-architecture.md` preference lint;
Abide is the productized path of that hole, `notes.md` §47).
Skills→oxlint is the same ownership split on a linter runtime: AST /
precheck *prove* what they can; Jev scores the remainder; do not
hard-gate CI on an uncalibrated Noul
([jev-oxlint](https://github.com/cephalization/jev-oxlint) Phoenix
experiment, `notes.md` §58). PR **attention** is not correctness
([egma-ai/jev-reviewer](https://github.com/egma-ai/jev-reviewer) —
anti-soundness-theater; **not** choxos pointer-not-generator).
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
| [Alloy](https://alloytools.org/) | Relational modeling; SAT/SMT *finds* instances and counterexamples in a finite scope | Small scopes. A green check is "no counterexample in this bound" | Which scope; is this instance interesting; cluster counterexamples; is the property tautological (Hillel) | Analyzer, facts, scopes |
| [TLA+](https://lamport.azurewebsites.net/tla/tla.html) / [TLC](https://lamport.azurewebsites.net/tla/tools.html) | Temporal logic of actions; *explicit-state* check of invariants and (some) liveness | Finite instances of *the spec* (not the C you forgot to model) | Which property is "obvious" vs "subtle"; map logs to behaviors | Spec, checker, refinement mapping |
| [Apalache](https://apalache-mc.org/) | Symbolic SMT checker for TLA+ (Z3); Quint's verify backend | Traces ≤ k, or all lengths *if* an inductive invariant holds | Same as TLA+; plus: was this BMC, random symbolic exec, or inductiveness? | Spec, SMT encoding, k / invariant |
| [Quint](https://quint.sh/docs/what-does-quint-do) | Executable fragment of TLA with programming-style syntax; simulator + Apalache/TLC | Same as TLA+ when you *verify*; `quint run` is a simulator, **not** a proof ([Quint FAQ](https://quint.sh/faq): no TLAPS) | Same as TLA+; simulator traces are DST-adjacent | Spec, types/effects, checker |
| [P](https://p-org.github.io/P/) | Async event-driven state machines; systematic testing of P programs | Explored schedules of the P program, not the handwritten C# you forgot to model | Which monitor; which failing schedule to inspect | P checker, runtime |
| [NuSMV](https://nusmv.fbk.eu/) | Symbolic SMV; CTL/LTL on finite-state models | The finite Kripke structure you encoded | Encoding choices; which property to add after a miss | Model, engines |
| [PRISM](https://www.prismmodelchecker.org/) | Probabilistic model checking (DTMC/CTMC/MDP) | The Markov *model*. Model-p is not a Noul | Interpreting model probabilities vs a judgment-class p; which rewards | Model, engines |
| [Event-B](https://wiki.event-b.org/index.php/Main_Page) / Rodin | Set-theoretic modeling + refinement; proof obligations between levels | Discharged POs for the refinement you wrote | Which PO is "prover timeout" vs "spec too weak" vs "real bug" (**Hypothesis** until labeled) | Rodin, provers |
| [mCRL2](https://mcrl2.org/web/index.html) | Process algebra | Same triage pattern as TLA+ (**Hypothesis**) | mCRL2 tools |
| [KeYmaera X](https://keymaerax.org/) | Hybrid systems (discrete + continuous) | Scenario labeling only; domain experts own the model (**Hypothesis**) | KeYmaera kernel |

Rule: a System One model may sit *around* these tools (triage, route,
explain a counterexample to a human). It may not sit *instead*. Quint's
own split is the teaching example: simulator finds bugs faster; model
checker is what lets you claim the invariant on that model
([What does Quint do?](https://quint.sh/docs/what-does-quint-do)).
Industrial north star for "precise design before code": Amazon's
[Use of Formal Methods at AWS](https://lamport.azurewebsites.net/tla/formal-methods-amazon.pdf)
(Newcombe et al., 2014) — TLA+/PlusCal as exhaustively testable
pseudo-code; finds deep bugs reviews miss; **does not** prove code
implements spec.

### Alloy Analyzer vs Apalache (do not collapse)

They are both bounded constraint engines. They are **not** the same
tool, not the same language, and a green check is not the same claim.
Alloy's own FAQ: the Analyzer is a **model finder**, not a model
checker — given a formula, it finds an instance
([Alloy FAQ: vs model checkers](https://alloytools.org/faq/how_does_the_alloy_analyzer_differ_from_model_checkers.html)).
Apalache is a **symbolic model checker** for TLA+
([apalache-mc.org](https://apalache-mc.org/)).

| | Alloy Analyzer | Apalache |
|---|---|---|
| Input | Relational first-order (sets, relations, traces *if you encode them*) | TLA+ actions / Quint |
| Engine | SAT (Kodkod) in a user *scope* (atoms per sig) | SMT (typically Z3) |
| What "green" means | No counterexample in this finite scope | Depends on the *mode* (below) |
| Built-in idiom | None — structure is the point; partial/declarative models are allowed | State-machine idiom of TLA+ (same assumptions as TLC) |
| Strength | Trees, tables, commuting operations, rich structure without array-encoding | Native TLA+; integers without enumerating every TLC value; Quint / Atomkraft / Solarkraft backend |
| Shared harm | Bounded green ≠ proof of the implementation. TLC enumerates spec states; Apalache unrolls them symbolically; Alloy finds instances of a *different* language. |

Apalache modes — mixing them is soundness theater:

1. Randomized symbolic execution — *some* executions up to length `k`.
2. Bounded model checking — *all* executions up to length `k`.
3. Inductiveness checking — all lengths, **if** the inductive invariant
   actually holds.
4. Custom exploration (JSON-RPC) — a script, not a certificate.

Judgment-shaped hole (same for both): which bound/scope; cluster
counterexamples; is this property tautological (Hillel: `canImport = P ∨ Q`
then "prove" `¬P ∧ ¬Q ⇒ ¬canImport`) vs subtle (concurrency, liveness,
multi-step). Out of class: a Noul "this Alloy looks right" or "Apalache
would agree."

Alloy × Jev composition (all **Hypothesis** as product; Analyzer remains
source of truth in-scope). Positions from `composition-algebra.md`:

| Position | Pattern | Ownership |
|---|---|---|
| Prior / selector | Choice over candidate predicates from NL | Analyzer accepts/rejects; human strengthens |
| Post-judge | Score/Choice: severity and novelty of each instance/CEX | Soft triage only |
| Gate | Noul "is this CEX spurious wrt informal intent?" | **Never** closes the check |
| Comparator | Rank which `check`/`run` to spend SAT budget on | Budget in code |
| Verifier (evidence) | Noul "does instance match a stakeholder scenario?" | Scenario library in tests |
| Operand | Features from instance graphs → a downstream model | Version features with the consumer |

Frontier (do not promote as recipes): LLMs writing Alloy
([arXiv 2502.15441](https://arxiv.org/html/2502.15441)); Anvil
synthesis/repair (MODELS 2026); *foundry* concept design verified in
Alloy 6 BMC. Help: cluster CEXs, narrate instances, rank which conjunct
to edit. Harm unchanged: vibe-specs are often tautological and unrun
(Hillel).

### Semi-formal artifacts (shared vocabulary, not enforcement)

UML/SysML state machines, Harel statecharts, ArchiMate, structured
English / GWT / EARS, decision tables, BPMN, ADRs-with-invariants,
SysML v2 pipelines. **Transfers:** System One classifies observations
into the diagram's vocabulary (Choice sets = states/events; Nouls =
guard suspicions; Scores = risk). **Does not:** a sequence diagram as
a runtime enforcer unless compiled to a monitor / Quint / TLA / Alloy.
Agents must not treat the picture as the interlock. Mapping cards:
`mappings.md` §3 (circuits) and §10–§12.

## 3. Deductive and contract languages

These prove **code against annotations**, not vibes against a README.

| Tool | What it actually does | Judgment-shaped hole | Stays in the tool |
|---|---|---|---|
| [Dafny](https://dafny.org/) | Verification-aware language; Boogie/SMT on methods vs contracts | Which module to annotate first; classify a failed VC | Verifier, annotations |
| [OpenJML](https://www.openjml.org/) / JML | Design-by-contract for Java | Same shape: rank hot methods; never "this Java looks safe" | ESC, runtime assertions |
| [Frama-C](https://frama-c.com/) / ACSL | C static analysis plugins; WP, value analysis | Which alarm is a true overflow vs a precision miss (**Hypothesis**) | Kernel, plugins, ACSL |
| [SPARK](https://www.adacore.com/about-spark) / GNATprove | Ada subset; flow + proof of contracts | Same as Dafny, at higher assurance | GNATprove, SPARK subset |
| Lean 4 / Rocq / Agda / HOL4 / PVS / ACL2 | Interactive theorem provers | Lemma ranking, proof-step *proposals* | The kernel decides |
| SMT (Z3, CVC5) | Backend to many of the rows above | Soft models must not rewrite goals unchecked | Solver, encoding |
| PBT / contracts / oracles (Hypothesis, QuickCheck) | Property tests on implementations | Shrink/triage failures; oracle *candidates* (**Hypothesis**) | The oracle, the runner |
| seL4, CompCert | Landmark verified stacks | Out of band — inspiration for "proof owns safety" | The proof |

A failed verification condition is a *structured* object (goal,
hypotheses, location). Ranking those is in-class. A Noul "the lemma
holds" is out of class — that is a proof obligation with the prover
deleted. Rule from the curriculum (DafnyPro-shaped): **LLM/Jev propose;
the verifier refutes or accepts.** Forbid silent base-code edits that
"make the proof pass."

Option order and an irrelevant extra option are properties of a System
One decision surface, not proofs. Property-test them: shuffle option
order; append an option the policy should ignore and check that odds
among the originals do not move enough to change the act (Hume's
`jev-1.13.0` probes — reconstruction, `notes.md` §31, not a new
invariance contract). A public logit dump for the *read-the-letter*
cousin is [`Mikhail/mini-jev-runs`](https://huggingface.co/datasets/Mikhail/mini-jev-runs)
(rotated-options split; scores not calibrated — `notes.md` §33). A
passing suite is coverage of those generators.
A Noul is still not a proof that the property holds, and a clean PBT run
is not one either. A perception-to-decision handoff is a contract
surface — the schema of objects or utterances, not the pixels or the
waveform: property-test that interface, and do not pretend the Noul is
over raw pixels or raw audio. A shared multimodal *decide* head
(blackwood-rlcd) still judges **marked candidates**, not an open click;
the act stays in code (`notes.md` §46). Hill-climb of that handoff:
`validation.md`.

## 4. Deterministic simulation testing (semi-formal trio)

DST is the missing middle: not a proof, not a unit test, not a
judgment. It **searches executions** under a deterministic scheduler
and asks whether *stated properties* held. A found bug is a
reproducible seed. A clean run is coverage of that search, not
correctness of the program. Antithesis's own explainer:
[how DST works](https://antithesis.com/docs/resources/deterministic_simulation_testing/).

Three different ways to search. None is a proof. None is a Noul.

| System | How it searches | What a seed means | Judgment-shaped hole |
|---|---|---|---|
| [Antithesis](https://antithesis.com/docs/introduction/how_antithesis_works/) | Whole-system **deterministic hypervisor** around software you did not rewrite; faults + inputs; you state properties; RL-guided exploration of timelines; reproducible | The SUT under the hypervisor, that timeline | Cluster failing timelines; novelty vs duplicate; which property to add; **never** "pass" a property |
| [Resonate HQ](https://docs.resonatehq.io/evaluate/how-resonate-is-tested) | **Durable async execution** (Distributed Async Await) — **not** an unrelated "Resonate AI" brand. Three layers: executable [Lean 4 protocol spec](https://github.com/resonatehq/resonate-specification), differential testing vs an in-memory oracle, DST of the TypeScript SDK (seeded faults; CI replays the seed twice). [Why](https://docs.resonatehq.io/evaluate/why-resonate) | SDK + faults + seed. Lean still owns the protocol claim. Promises **settle in protocol**, not via Noul | Same as Antithesis for the DST layer; cluster oracle disagreements; semantic gates *inside* a step (`ctx.run`) |
| [PufferLib](https://puffer.ai/docs.html) | The **environment is already a simulator**. Serial vectorization + explicit seeds for contract debugging; Ocean sanity envs fail if the *trainer* is wrong ([arXiv 2406.12905](https://arxiv.org/abs/2406.12905); authors: never report Ocean as a comparative RL baseline). A seed does **not** make GPU training or third-party simulators bitwise deterministic | Replay of env + seed (seed action-sampling separately). Ocean pass = trainer contract, not policy optimality | Cluster failing episodes; curriculum Choice over a bounded env set; Score as a *feature* into a learned reward model (**Hypothesis**, composition-algebra open "reward shaper"); never "the policy is correct" |

Teaching split:

```text
Antithesis   wrap existing software; you did not rewrite the scheduler
Resonate HQ  durable async + Lean spec + oracle + DST; promises settle in protocol
PufferLib    the world is a sim; DST-shaped testing is seeded serial env
             + Ocean contracts; RL value still needs observed rewards
```

Resonate is the ownership split in one product: Lean owns the protocol
claim; DST owns "this SDK, these faults, this seed"; the runtime owns
crash-resume. A judgment-class model may gate *inside* a durable step;
it does not settle a promise. PufferLib is the search/control cousin:
the loop is yours; a judgment-class model may score traces, not replace
the env contract. Standing rejection unchanged: bandits / RL value from
Jev with no observed rewards (`methods-catalog.md`). Mapping cards:
`mappings.md` §13 (DST triage), §14 (durable agent control).

A judgment-class model is not a fourth way to skip any of those layers.
It can sit where OpenSmoke already sits: cheap flags over every failing
seed so a human (or an LLM autopsy) only sees the cluster.

Rejected: "we ran DST, then Jev said the traces look healthy, ship it."
The property ran or it did not. Judgment does not get a vote on P.
Rejected: reporting Ocean scores as a capability claim for a
judgment-class model.

## 5. Harms

### TOCTOU-of-Noul

Time-of-check-time-of-use: you judged state at t0 and acted on it at
t1. The world moved. The check was never atomic because it was never a
check.

| Shape | t0 | t1 (the miss) |
|---|---|---|
| Classic | `stat` | `open` — the file changed |
| Agent | Noul "this plan is safe" | tools ran; files, prices, permissions changed; execute |
| Lock-shaped | Noul *as* the mutex | concurrent actor never saw a lock |
| Business | "this invoice looks right" / credit Noul | wire after the account emptied |
| Life | "this looks done" / "this looks edible" | eat / serve after a different specimen or a cold center |
| Inbox | "needs a reply today" | send yesterday's draft to the wrong thread |
| Hiring | "transcript shows skill" | offer after answers were about a different job |
| Formal | Noul "this spec looks good" | merge; the checker never ran (also vibing specs) |

Fix, in order: make the real interlock in code or policy (types, auth,
sandbox, compare-and-swap, capability tokens, two-person rule,
thermometer, ledger); **EAFP** — attempt the privileged op with OS/DB
enforcement and handle failure; bind check to use (`O_NOFOLLOW`,
transactions); re-probe after the world can have moved (composition:
irreversible acts concede only to a post-execution probe); hysteresis /
time-bounded certificates; treat the t0 judgment as advisory routing,
not permission. Fail-closed authorize cannot be a stale Noul. Policy is
the code of a practice that has no repository (`mental-models.md`).
Semi-formal: a sequence diagram that shows a check message then a later
act message *without an atomicity note* is a TOCTOU diagram.

### Soundness theater

Claiming a proof-shaped conclusion from a non-proof:

- Bounded check with a toy scope, sold as "verified."
- Apalache *randomized* symbolic exec sold as BMC; BMC at `k=3` sold as
  "all traces"; Quint `run` cited as Quint `verify`.
- Tautological properties that only restated the definition ([Hillel
  Wayne, March 2026](https://buttondown.com/hillelwayne/archive/llms-are-bad-at-vibing-specifications/):
  `canImport = P ∨ Q` then "prove" `¬P ∧ ¬Q ⇒ ¬canImport`).
- "Formally verified" marketing on a model that omitted the bug class.
- Noul 0.95 presented as a safety case. Calibration describes *groups*,
  in-distribution (`faq.md`; Archer Hume OOD collapse).
- "DST hasn't failed" as correctness.
- PufferLib Ocean scores as a comparative baseline (authors forbid this).
- A listwise or CLIP affinity as fail-closed authorize
  (`judgment-class.md`).
- Engine eval / attention score sold as the *verdict*
  ([game-coach](https://github.com/JoelLewis/game-coach) Wave 0:
  Stockfish owns truth, Jev owns judgment; [egma-ai/jev-reviewer](https://github.com/egma-ai/jev-reviewer):
  attention ≠ correctness). A Noul is not a proof the move was a
  blunder or the PR is good (`notes.md` §58, §59).
- "Type-safe" sold as "correct" ([interlock](https://github.com/somoore/interlock):
  irreversible stays behind a threshold **and** a human).

If the artifact would still say "verified" after you delete the
checker, it was theater.

### AI × formal methods (vibing specs and cousins)

[LLMs are bad at vibing specifications](https://buttondown.com/hillelwayne/archive/llms-are-bad-at-vibing-specifications/)
(10 Mar 2026): a growing share of public TLA+ (he clocked **4% of
GitHub TLA+ files mentioning Claude**) is unrun, non-compiling, or
only "obvious" invariants (forgot a guard) — not the *subtle*
concurrency, nondeterminism, and liveness properties that are why you
bothered. The Alloy example did not compile (`open util/boolean`
omitted) and asserted tautologies. Experts can use LLMs as a force
multiplier *because they run the checker and can demand a strong
property*. Beginners get green syntax and tautologies. Related talk:
[How to find bugs in systems that don't exist](https://www.hillelwayne.com/talks/informal-methods/qcon26/)
(QCon London 2026) — spec, environment, and properties are three views;
judgment may score whether a log resembles a spec behavior; it does not
write the environment assumption.

Additional AI×FM harms (same family, not a new owner):

1. **Receipt theater.** An MCP "ran the checker" on a tautology. The run
   is real; the property is vacuous.
2. **Double theater.** LLM-written spec plus a System One Noul "does
   this spec look good?" The checker, DST harness, or prover ran, or it
   did not. Judgment may triage *outputs of* those tools. It may not
   certify the spec.
3. **Mode laundering.** Apalache random-exec or Quint simulator cited as
   unbounded safety.
4. **Sensor as constraint.** Leveson: a 99% Noul is a sensor. Unsafe
   control action: the agent proceeds *because the model was confident*.
5. **Vacuous models (Cauli).** [My EuroSys 2026 paper is
   obsolete](https://claudiacauli.com/2026/03/08/my-eurosys-2026-paper-is-obsolete):
   the cost of producing *something that typechecks* collapsed; the cost
   of **strong properties + validated models** did not. Domain
   understanding must not go to zero.
6. **Silent code changes** to satisfy Dafny/Lean.
7. **PRISM/MC p confused with a Noul.**
8. **DST coverage mistaken for verification of unstated properties.**
9. **Reward laundering** in PufferLib-class loops.

**Cauli ∩ Hillel:** System One helps the *workflow around* FM (triage,
ranking, UI, monitors) and must not mint fake strength. [Lamport
Agent](https://zfhuang99.github.io/github%20copilot/formal%20verification/tla+/2025/11/14/lamport-agent.html)
drafts TLA+ from codebases; a human still validates. Hillel on tool
choice: [dreidel / PRISM](https://buttondown.com/hillelwayne/archive/i-formally-modeled-dreidel-for-no-good-reason).

### Help vs harm (keep this list short)

**Help:** candidate properties (always run MC/ITP/DST); filter before
expensive SAT; CEX/timeline/instance triage; lemma/repair ranking; UI
for specs; runtime monitors + conformal abstention; ADR/decision-table
hygiene.

**Harm checklist** (copy into a PR template; also `boundary-audit.md`):

- [ ] Does a probabilistic gate authorize an irreversible act without a
      hard interlock?
- [ ] Is any "verified" claim only about a model the team has not
      validated by breaking it?
- [ ] Are properties strong (concurrency, multi-step) or tautological?
- [ ] Are Choice options / Score rubrics versioned with the consumer?
- [ ] Is abstention defined per-action with costs?
- [ ] Are CEX/triage judgments stored as evidence, not enforcement?
- [ ] Alloy vs Apalache vs TLC named correctly?
- [ ] Resonate protocol settlement vs agent "done" Noul separated?
- [ ] Antithesis properties written as harness asserts, not chat
      opinions?
- [ ] Speculative MCTS/RL depth capped without a real simulator?

Augustus implication: answer "formally verify with Jev" with a
**placement** (triage failing seeds / rank VCs / NATM-instrument the
control loop), not a hybrid "verified by Noul" API.

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
in the control structure. Mapping card: `mappings.md` §8.
**Capability kernel receipt (Empirical as architecture):**
[interlock](https://github.com/somoore/interlock) — LLM ring 3;
kernel ring 0; Jev SENSOR; `policy.py` constraint; secrets never
in the agent (`notes.md` §59). **Engine ∩ judgment (Empirical as
PRD):** [game-coach](https://github.com/JoelLewis/game-coach) —
Stockfish is the probe; Jev is the coaching sensor; Wave 0.

**Kent — Data and Reality.** Models are approximations; **naming is
load-bearing**. Question text, Choice sets, and Score rubrics *are* the
ontology. Wrong predicates → proof of the wrong world. Spec languages
force naming; System One makes naming cheap to *apply* at scale — both
can encode a bad ontology.

**Shirky — situated software.**
[Situated Software](https://gwern.net/doc/technology/2004-03-30-shirky-situatedsoftware.html):
form-fit to a social group; refuse false scale. Dense judgment *inside*
a named community (team, product, agent) is in-class. Do not
universalize thresholds across populations. Semi-formal ADRs + local
invariants beat enterprise ArchiMate theater when N is small. Mapping:
`mappings.md` §16.

**Vanderburg / Real SE.** Engineering = models under uncertainty +
measurement closing the loop
([series](https://vanderburg.org/blog/series/real-software-engineering)).
Traverse composition positions × constructs; each cell needs a named
caveat and a falsifier. FM and System One both fail as decoration.
Crossover Project (Hillel Wayne) is the same argument: copy
**measurement + feedback under load**, not slogans.

**Agans — Debugging.** See → stabilize → find evidence → fix → verify.
Judgment helps *see/classify*; probes verify. Mapping intuition only.

| Metaphor | Soft judgment owns | Hard / FM / code owns |
|---|---|---|
| NATM gauges | ground class, urgency | lining thickness, invert close, stop-work |
| Snap-fit | "feels seated" Score | geometry, go/no-go gauge |
| Norman | evaluation of state | executable actions and affordances |
| STAMP | estimate of process variable | enforced constraint / interlock |
| Kent | proposed names / features | schema + integrity constraints |
| Shirky | local meaning | community contracts and reputation outsides |

```text
NATM        instrument often; adapt support in code
snap-fit    designed give only where a miss is reversible
Norman      judgment evaluates candidates; forcing functions execute safely
Leveson     judgment senses; constraints live in the control structure
Kent        naming is the ontology; both FM and Jev can encode a bad one
Shirky      dense loops inside a named community; don't fake public scale
```

## Decision-design extras (proof × judgment)

When the request mixes formal methods with a System One model:

```text
What must remain exhaustive (proof / MC / types / DST property):
Which bounded engine (Alloy finder vs TLC vs Apalache mode vs Quint run vs verify):
Which DST layer (Antithesis hypervisor / Resonate Lean+oracle+SDK / PufferLib env+seed):
What is a sensor (judgment-class family + hole):
What is a control constraint in code/policy (Leveson):
TOCTOU: is check atomic with use, or is there a re-probe?
How we would detect soundness theater / tautological specs (Hillel):
Smallest experiment that could reject this split, not this vendor:
```

Propose two placements if the hole is mixed (e.g. TLA+ on the protocol
+ DST on the SDK + judgment triaging failing seeds). Do not invent a
hybrid "verified by Noul" API.

Related: `formal-semi-formal.md` (one screen); `mental-models.md`;
`mappings.md` §6–§19; `methods-catalog.md` verification rows;
`composition-algebra.md` positions 3 and 9; `mixed-architecture.md`
preference lint; `faq.md`; `boundary-audit.md`.
