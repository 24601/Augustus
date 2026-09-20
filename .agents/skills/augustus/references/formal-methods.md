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
- A Jev (or any judge) **score sold as eval truth** without
  auditing data, scorer, runs, or claims
  ([dinostomp](https://github.com/collapseindex/dinostomp):
  checks the instrument, not just the score; `dinostomp jev`
  tests a question like an if-statement; 99 of 189 findings
  against itself; `notes.md` §62).
- Keyword privilege sold as a safety case
  ([construct-auto-classifier](https://github.com/godspede/construct-auto-classifier):
  `sudo status` can be a safe read; contracts on effects, not
  tokens; `notes.md` §63).
- A stop-hook “green” sold as permission to skip review
  ([jev-lens](https://github.com/rashedInt32/jev-lens): never
  says green unless sure; never blocks the agent;
  `notes.md` §63).
- Sync “Jev routing” sold without measuring decision-model
  latency ([slo-router](https://github.com/zeeshan8281/slo-router):
  same routes, p95 77.93→490.38 ms *theirs*; `notes.md` §63).
- A cookbook question set sold as verified without numbers
  ([jev-packs](https://github.com/dtduc-git/jev-packs):
  measurement owns endorsement; `notes.md` §64).
- A positive decision-model score sold as authorization
  ([actiongate-jev](https://github.com/omkarghugarkar007/actiongate-jev):
  Jev supplies evidence, code owns authority; `notes.md` §64).
- Vendor "calibrated" sold as frequency units you can
  hard-threshold
  ([does-jev-confidence-mean-anything](https://github.com/Adilmp/does-jev-confidence-mean-anything):
  ranking ≠ calibration; stated ~75% vs human ~10%;
  `notes.md` §64).
- Jev `done` sold as the browser task succeeded
  ([ego-jev](https://github.com/jiangkoumo/ego-jev): `--until`
  in code; `notes.md` §65).
- LLM summary sold as compaction
  ([jev-compactor](https://github.com/edwardyen724-g/jev-compactor):
  summarizer invented a path; pointer cannot; `notes.md` §65).
- The model's own hides sold as training labels
  ([x-reply-filter](https://github.com/zhuyansen/x-reply-filter):
  confirm-queue; never self-reinforce; `notes.md` §65).
- A leaderboard sold as a capability map
  ([jev-capability-atlas](https://github.com/Zaious/jev-capability-atlas):
  receipts, not a ranking; type-safe ≠ correct; `notes.md` §66).
- "Jev is weaker than 4B" sold without the thinking budget
  ([jev-frontier-100](https://github.com/softpudding/jev-frontier-100):
  4B off 56.0% vs 2048 96.7%; `notes.md` §66).
- In-domain ECE sold as OOD honesty
  ([jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration):
  sign flips by type; unknowable policy still gets mean p 0.74;
  `notes.md` §66).
- A local one-pass softmax sold as a Noul
  ([jevmlx](https://github.com/bnsd55/jevmlx): schema-valid ≠
  calibrated; `notes.md` §66).
- A TLA+ run sold as "Jev is never wrong"
  ([jev-labs](https://github.com/copyleftdev/jev-labs): the
  invariant is never *confidently* wrong; escalate is
  allowed; 0 of 1,080 golden is not a proof of zero;
  synthetic, not clinical; `notes.md` §67).
- A Main Score sold as calibration, or a partial run sold
  as a rank
  ([jevbench](https://github.com/fstandhartinger/jevbench):
  Brier/ECE reported **not scored**; native ≠ verbalized;
  `notes.md` §67).
- A typed answer sold as permission to advance
  ([seal](https://github.com/Reasonofmoon/seal): no seal, no
  advance; coverage.path visible; mint ≠ product brain;
  `notes.md` §67).
- Jev `confidence` sold as the strictest reading of the
  vector
  ([how-sure-is-jev](https://github.com/adarc8/how-sure-is-jev):
  Choice confidence = max_prob, the most generous metric;
  `notes.md` §67).
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
**Eval-instrument (Empirical as FINDINGS ledger):**
[dinostomp](https://github.com/collapseindex/dinostomp) —
the score is not the evidence; `dinostomp jev` is question
hygiene beside jevals, not a Harbor taskset (`notes.md` §62).
**Permission vs probability (Empirical as measured
suppression):** [omp-greenlight](https://github.com/SemetricLabs/omp-greenlight)
— host deny is the constraint; Jev is the sensor; operator
owns the criterion (`notes.md` §62).
**Contracts on effects, not tokens (Empirical as
certification; hunch as FM angle):**
[construct-auto-classifier](https://github.com/godspede/construct-auto-classifier)
— the named constraint is blast radius / reversibility, not
a privilege keyword. Independent risk Nouls are sensors;
`minConfidence` ∩ `riskThreshold` ∩ fast-deny is policy.
Fail-closed when the sensor is missing. Privilege ≠ verdict
(`notes.md` §63).
**Attention filter ≠ permission (Empirical as README):**
[jev-lens](https://github.com/rashedInt32/jev-lens) — never
blocks the agent; never authorizes a write. Complements
skill-broker and omp-greenlight (`notes.md` §63).
**Jev supplies evidence, code owns authority (Empirical
as slogan):**
[actiongate-jev](https://github.com/omkarghugarkar007/actiongate-jev)
— deterministic policy is the hard gate; Jev is soft
evidence. A positive score never overrides RBAC/schema/limit
(`notes.md` §64).
**Turnstile clone (Empirical as README):**
[turnstile](https://github.com/zyphr-labs/turnstile) —
policy first; Jev remainder; receipts + replay; missing
Jev → Review (`notes.md` §66).
**TLA+ compose with a Jev-class oracle (Empirical as spec
+ chaos table; 2026-09-19 ~02:38):**
[jev-labs](https://github.com/copyleftdev/jev-labs)
— TLC owns the protocol invariant; Jev is the noisy
sensor; **escalate** is the actuator when quorum is
unstable. Inverse of sensor-as-constraint: the kernel
**must not** return a confident wrong, and **may** hand
off to a human. 1,080 golden 0 wrong *theirs*;
underdetermined 34/120 still decided both ways.
Synthetic, not clinical (`notes.md` §67).
**Advance/coverage ledger (Empirical as README +
BEYOND-JEV.md):**
[seal](https://github.com/Reasonofmoon/seal)
— Strike/Jev is the sensor; Seal + coverage.path is the
constraint; Effects are the actuator. Exception queue
visible. Mint ≠ product brain (`notes.md` §67).

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

This hour's exact envelopes (`notes.md` §87) are examples of the
split, not schema copied onto every FM card: Telegram char /
`callback_data` limits; HA writes (allowlist, freshness,
idempotency, post-state); ordinary test assertions; closed verb
menus / HP floors; n8n IF/Code arithmetic; compaction
`minReductionRatio` fail-open. Hard-gating a Noul as CI pass
(jevtest 0.85), HA actuator, or authorship proof is the same
theater as totally-tim/jev-gate.

This hour's follow-on envelopes (`notes.md` §88):
gitignore / symlink skip / listing (findme);
`test.skip` / deleted assertions (stanley-code `notChecked`);
pinned Agent model + conversation prompt-cache
(jevsubrouter). Soft Noul ≠ hard safety: Jeff-1 ECE,
stanley 0.6/0.55/0.15, findme beam scores, jevsubrouter
balanced-on-low-conf. Empty findings as approval, or auto-promoting an agent-written workflow, is the same theater.

1144 envelopes (`notes.md` §89), still outside the extras
template: BAML exhaustive `match` / `"something else"`
(feelings `.feels()`); grok-bot-jev kill switch + skill
honor; Essentiel-Jev never authority + read-back;
enzo-mcp UNKNOWN + `allow_external_jev`; pigeonhole OTHER skip
+ missing-folder off; static no-network playground;
`gmail.readonly` (jevmail); Trash not delete (mailjay).
Soft Noul ≠ hard safety: `.feels()` 0.5, apa 0.85,
Essentiel 0.75, pigeonhole 0.6, jev-lab 0.65/0.70.
Hard-gating a default 0.5 bool, quoting “mathematically
fulfilled,” or pasting jev-test bars as results is the
same theater.

1241 envelopes (`notes.md` §90), still outside the extras
template: Ego Lite locators / ZHUBoer/ego-jev reserved
`__none__` / runWorkflow completed ≠ success; jsort
scores are relative; groundedness 0.5 label on Noul;
playground 0 promotions; s1_ruby `?` vs `undecided?`
abstain; tpellet/hunch exit 3 + never-execute list;
tidy 0.8 + none-of-folders stay; tab-bouncer
pinned/audio/current never closed; lkclean Show
fail-open; jev-yt-time-saver Show anyway; ORIGIN
pause-if-no-Jev + validResponse sums-to-1; crawlers
verify grounding not exec + review queue; jevbrain
AUTO_ACT is not a Noul. Soft Noul ≠ hard safety:
jsort logits, Jev 0.5 groundedness, tidy 0.8, lkclean
70/35/60, hunch 0.5/0.65, file-search 0.8, jevbrain
0.80 are **sensors**. Hard-gating AUTO_ACT, treating
ranking logits as frequencies, pasting 95.2% / 83%
plumbing / 36/120 NL2Bash as class ceilings, or
letting Jev send/delete/close pinned tabs is the
same theater.

1347 envelopes (`notes.md` §91), still outside the extras
template: judgekit YAML classify/score/route/verify;
typed-judge-kit verdict-in-code; alsoleg89/decide packing
VOI + 0.8 ≠ 80% accuracy; jev-calibration-arena never
acts; Jev-Calibration Platt ECE 0.117→0.052;
ctmx/openrouter-jev-mcp Decision-as-Plugin;
FrancoisChastel/jev-code ≠ npm jev-code;
claudecode-jev-marketplace fail-open not hot path;
pedroknigge/mcp_jev packs not ask_jev;
cyrusasco/typesafe-mcp noul deadband 0.35–0.65;
codaaiteam/jev-skill jevtypesafeai.com ≠ TypeSafe;
hermes-switchyard ≠ hermes-jev-router ≠ hermes-plugin-jev;
nanoprune 2.8MB ECE 2.58%; smartdio/jev-browser-agent ≠
ZHUBoer/ego-jev; Dakai/omp-jev-web DONE ≠ proof;
hari007sh/jev ≠ dannote/jev; 0thernet/system-one-skills
deterministic verify; typed-gate band [0.40,0.60] is
refusal; pi-jev-gate fail-closed; choice is the verdict.
Soft Noul ≠ hard safety: 0.7 / 0.8 / ~0.6 / 0.75 /
0.85 / 0.6 / [0.40,0.60] are **sensors**.
Choice-as-verdict without a mid-band is still a
sensor.
Hard-gating argmax as safety, pasting 97.7% n=130 / 0
hallucination / 8,026 tokens as class ceilings, or
treating a skill named System One as a judge is the
same theater.

1441 envelopes (`notes.md` §92), still outside the extras
template: Foq ~25ms/2.2GB local; rev prefill-only + HF jev-0.5b;
robfrase/jev planning memo; typesafe_agent_gates 27/27 / 31/31;
EpicEric/safe-sh static remainder; pastepilot Confirm before act;
Jev-Reranker live Jev not yet measured; sessionwise opt-in relevance;
jev-search pointer sieve; 400ms Salesforce WebMCP;
Always **savka777/jev-search**. **≠** kazuhideoki/jev-search
**≠** superagents-lab/jev-search.
typesafe-scheduler-diagnostics advisory; droidjev screenshot-free;
Tewoto1 jevcu planner still writes; ha-conversation-jev Jev→Grok;
dsh-jev can only gate; jev-classification-benchmark specified not run;
jev-luna-pagerduty p≥0.50; meldltd/meldecision laya-go ONNX;
laya-doom never pixels; logixism/laya-api empty README;
akpsahan/laya ≠ Archer; choxos/jevchess engine owns truth;
jev-drive sim not AV; story-arc Jev never authors;
jev-hs-assistant HS6; golergka/jev-plays-starcraft-2 UI-verified ≠ API Victory;
awesome-jev-use-cases catalog; Nibir1/typesafe-go ≠ official.
Soft Noul ≠ hard safety: Foq 0.95 / gates 0.5/0.6/0.8 /
Confirm ≥0.75 / FAST_MIN 0.80 / p≥0.50 / compose 0.7/0.5/0.6
are **sensors**. rh-guard owns the gate cousins.
Hard-gating Confirm as optional, pasting Foq 100%/ECE 0.2% /
Reranker 0.1667 / 400 ms / akpsahan vs-Jev as class ceilings,
or treating Qwen3.8-27B as Archer is the same theater.

SIGNAL §93 envelopes (`notes.md` §93), still outside
the extras template: fingerprint after redact;
recall vs decide; publish fingerprints+answers;
CI replay as Harbor cousin; Cache hit ≠ correctness;
hyperspaceai/jevcache ≠ kushals256/jevcache;
human labels only; score never auto-accepts;
production capture flywheel; sutro-sh/jev-align ≠
caiovicentino/jev-align.
Soft Noul ≠ hard safety: a HIT and a training
score are **sensors**. Treating a ledger HIT as
correctness or auto-accepting GEPA because the
score rose is the same theater.

SIGNAL §94 envelopes (`notes.md` §94), still outside
the extras template: guidance ≠ hook; catalysts ≠
summaries; compile-time System One; unofficial ≠
TypeSafe; format_version modernbert-jev/1;
Argos1111/jev_local ≠ us/jev-local ≠
kunchenguid/local-jev; LFM default ≠ ModernBERT
backend; Nemotron ≠ TypeSafe Jev;
not a calibrated replacement; djev-dev complements
djev-spark; images as Choice options; Laya essay
numbers *theirs*; Router/OOD confidence;
hosted bootstrap ≠ silent TypeSafe.
Soft Noul ≠ hard safety: `when asked`, unofficial
local p, Nemotron p, and Laya 0.85 are
**sensors**. Hard-gating catalyst similarity as
deny, treating unofficial JA ModernBERT as TypeSafe
calibration, treating enzyme hosted bootstrap as
silent TypeSafe, collapsing LFM default into JA
softmax, or treating Nemotron as a calibrated
replacement is the same theater.

1541 envelopes (`notes.md` §95), still outside the extras
template: difficulty + policy thresholds + JSONL trace;
jev-codex-pilot model + reasoning depth;
keep/shadow/hybrid/reject; quarry evidence projection;
Frank-ZY-Dou/awesome-jev robotics/3D/control;
one-dollar-tahoe TypeSafe Jev defense eval;
jevguard calibrator/cache/escape;
jev-ci-selector CI shadow mode;
llama-jev llama.cpp replica.
petercr/jev-orchestrator ≠ FleeexCorp/jev-orchestrator.
seb4ez/jevguard ≠ AseemPrasad/JevGuard ≠ pablozr/JevGuard.
webNeat/llama-jev ≠ WiktorB2004/llama-index-jev.
Soft Noul ≠ hard safety: 0.95 FINISH / 0.55 min p /
0.40 calibrator / 0.15 margin / 0.05 skip_below /
p&lt;0.5 quarry drop are **sensors**. rh-guard owns
the injection-firewall / CI-gate cousins.
Hard-gating skip_below as merge policy, inventing
one-dollar-tahoe ASR/FPR, pasting OpenRoboto $ as a
success-rate, or treating numbered-choice softmax as
a Noul is the same theater.

1639 envelopes (`notes.md` §96), still outside the extras
template: OpenCode jev-pruner context sieve;
observe→score-candidates→prune; jev-zen / jev-1.13-free;
zen-chat ≠ Noul; fail-open original; keepScore >0.1 floor;
host port of tamaratran/jev-pruner;
indiejoseph/opencode-jev-pruner ≠ nrdz-labs/fast-jev-opencode;
jev-webagent-bench empty stub;
Kiln-AI/jev_jsonschema noul_threshold 0.5;
NSStudent/JevSwiftSDK unofficial.
Soft Noul ≠ hard safety: keepThreshold 0.5 / zen-chat
parsed JSON / schema boolean @ 0.5 are **sensors**.
Hard-gating prune as proof of irrelevance, treating
zen-chat as calibrated Jev, or inventing an empty-stub
Harbor score is the same theater.

SIGNAL gliner-native-runtime envelopes (`notes.md` §97),
still outside the extras template: GLiNER2 native Apple
path; unofficial Swift/Core ML GLiNER 2.5-small; entity
spans + confidence; not Choice/Score/Noul; not TypeSafe;
label descriptions as schema; on-device ANE economics;
honesty locks; shershah1024/gliner-native-runtime ≠ Fastino;
≠ gliner25-compaction ≠ gliner2-ultrafast ≠ Eran-BA/Jev_from_GLiNER2 ≠ NSStudent/JevSwiftSDK ≠ jevmlx;
default threshold 0.1 still soft.
Soft Noul ≠ hard safety: 0.1 / null >0.5 / README 0.99
are **sensors**. Hard-gating 0.1 as NER quality, treating
spans as Choice/Score/Noul, filing it as keep/drop of
held candidates or as position 4 Selector, or inventing
ANE Harbor is the same theater.

1740 envelopes (`notes.md` §98), still outside the extras
template: Decision Graph Protocol frame→assess→commit;
app retains permissions/effects; Jev-first
assessor-neutral; guarded commit / receipt/next frame;
assessment batching; hard-gating DGP as safety theater;
numerous-com/dgp ≠ TypeSafe official; jegrep calibrated
path+range Nouls; no embeddings/index/daemon;
~$0.01–0.03 typical; agent --json;
can1357/jegrep ≠ Bentlybro/jevgrep ≠ uehaj/jev-semgrep;
Archer-arch fidelity; kev family OOD 0.76–0.77 vs Jev
0.86; block-causal isolation; pointer/readout
CE-trained; /v1/systemone drop-in; replica honesty.
Soft Noul ≠ hard safety: assessment p / mock outcomes /
106 tests / 0.4/0.2 / $0.01–0.03 / 0.76 / 0.77 / 0.86
/ ECE ~0.1 / 0.62 rule-pairs are **sensors**. A receipt
proves the *commit happened under the guards*, not that
the assessor was correct. Hard-gating DGP as safety
theater, hard-gating a miss as “the concept is absent,”
mixing OpenRouter/TypeSafe auto-failover as one Noul
(silent FALLBACK), or pasting OOD acc as “close enough
to ship as Jev” is the same theater. rh-guard owns the
silent-FALLBACK cousin. rh-guard **does not own**
protocol envelope / ranking fail-open / replica honesty.

1843 envelopes (`notes.md` §99), still outside the extras
template: cost-sensitive decision theory × System One
probabilities → control flow; thresholds derived from
costs not hard-coded; YES / NO / UNSURE from
cost_false_yes / cost_false_no / cost_human;
auto-batching same-object questions; Kungie/gut ≠
tpellet/hunch ≠ carldaws/hunch; judgment vs generation;
deterministic execution after probabilistic judgment;
exactly one app-owned callback; explicit uncertain
branch; Illusion47586/judge ≠ lexingtonhibiki/judgekit ≠
Ascurse/typed-judge-kit; variable-N option scoring as
the trainable object; dynamic candidate bags not fixed
label sets; zwliJay/jev-forge ≠ NanoJev; NAR local
drop-in; open replica economics / latency vs closed Jev;
wfzyx/von late-catch HIGH; competing NAR claims /
replica honesty; typed judgments vs chat judges on
guardrailing; ishaannk/llm-vs-jev cross-note only;
deeper integrity fold is rh-guard; nothing wins
outright; can be argued out of guarding.
Soft Noul ≠ hard safety: 0.038 / `min_confidence` /
0.579 / 0.637 / T=0.9717 / 93.0% / 91.23% / 62 ms /
15 ms / T=1.0367 / T=1.1692 / n=78 / 77.9% / ECE 0.053
/ 14.3% steer are **sensors**. The cost table is
policy; the Noul is a SENSOR. Hard-gating 0.038 as a
safety proof, merging Needle 52.6% with n=78 93%,
“guaranteeing” calibration, or pasting “Jev wins
guardrailing” is the same theater. gut/judge are
overlays, not species. rh-guard owns steerability.

1943 envelopes (`notes.md` §100), still outside the extras
template: Jev IS the if-statement; judgments/probabilities
drive branches; text model only writes prose; interpreter
owns variables/loops/budgets/replay; otherwise maybe /
confidence gate; chaos samples after the gate;
southpolesteve/probably ≠ carldaws/hunch ≠ feelings ≠
Kungie/gut ≠ Illusion47586/judge ≠ tidymodels/probably;
133★ / forks 10 live; build calibrated classifiers from
human feedback; retrieve by relevance not resemblance;
one calibrated yes/no per memory in one request; pointer
mode 17/18 19/20 *theirs*; embedding resemblance misses
the allergy; samdotmak/jev-recall ≠ jev-search ≠ jev-sift
≠ carryforward ≠ chopratejas/invalidate; memory leases
ended by new evidence; six Nouls then fixed rules in
code; 0 of 157 false invalidations; questions/plans/
directives are not evidence; unsure → review queue; host
keeps the store; name↔body / comment truth / test-claims;
mizchi/jev-lint is mizchi/jevlint rename; no shipped rule
has severity error; ~1 in 5 findings wrong *theirs*;
mizchi/jev-lint ≠ huntedman/JevLint ≠
MichitoSugawara/jev-lint; JSON Schema → typed JSON via
Jev; noul_threshold 0.5 decoder not a proof;
IncompatibleSchemaError lists every bad property;
on-device Laya CoreML ANE; ~5 ms P50 short decisions;
189/189 FP16 checkpoint parity; 10× not achieved;
mizorewww/laya-coreml ≠ gliner-native-runtime ≠ jevmlx ≠
NandhaKishorM/laya; softmax over allowed tokens ≠ Noul;
question-first cache; Micha0827/snapjudge ≠
githubnext/localjev ≠ jevmlx ≠ cendress/SnapJudge;
Jev-first Pi agent loop; slow-LLM fallback; explicit
action menu / CandidateSource unimplemented; 62 tests
wiring not quality; direwolfiy/JevPi ≠
standardagents/jevpilot ≠ pi-jev-control.
Soft Noul ≠ hard safety: 80% / 17/18 / 0 of 157 /
4.98 ms / 189/189 / 0.5 / 62 tests are **sensors**.
The interpreter / lease policy / schema envelope / AST
matcher is exact work. Hard-gating `feels`, pasting
17/18 as Harbor, hard-gating 0 of 157 as a proof,
treating boolean @ 0.5 as safety, claiming 10×, treating
softmax as a Noul, or treating wiring tests as quality
is the same theater.

2041 envelopes (`notes.md` §101), still outside the extras
template: resume-screening bias audit methodology;
name×resume factorial independent Nouls;
callback determined by resume quality;
mean-probability name gaps operationally negligible;
natemoo-re/bias-bench ≠ BBQ;
Plan/PRD panel → code-owned pass|review|block;
cheerleading out of scope;
austindixson/planalyzer ≠ single-goodness Noul;
cost-aware multi-model routing/escalation;
decide vs do;
successful-task cost;
cannacre8ive/switchboard-ai ≠ ha-switchboard ≠ hermes-switchyard;
frozen-protocol zero-shot bench;
TypeSafe Jev vs PrismNLI vs Laya;
contamination caveat;
elcronos/jev-vs-open-decision-models ≠ JevBench ≠ DMB;
context-window admission control;
VOI gate which tokens are worth the expensive model;
fail polarity per lens;
on small inputs lenses lose money;
cvsgireesh/jevusher ≠ jev-sift ≠ winnow;
typed decision control plane;
receipt ≠ authorization;
historical-v0 zero retained cases;
MokiMeow/jev-fabric ≠ jev-forge ≠ dgp;
live 15-dim typed rubric re-score per pause;
scoring economics exemplar;
OpenJev/Codiv ≠ TypeSafe hosted;
jose-troche/live-rubric ~$0.000004 desc / ~$0.000006 README;
adversarial pre-registered Jev eval;
28 predictions before data;
123,805 requests;
confidence does not track ignorance;
polite injection 65% / crude 0%;
willkelly/jev-evaluation ≠ jevals ≠ jev-baselines-eval;
provider-neutral Elixir/BEAM Noul/Choice/Score SDK;
class infrastructure;
nshkrdotcom/system_one_sdk ≠ typesafe_sdk ≠ dannote/jev.
Soft Noul ≠ hard safety: 25.0% / 0.72 / V0.4 / 0.587 /
0.725 / 6,866 / zero retained cases / $0.000004 /
$0.000006 / ECE 0.075 / 47% / 65% are **sensors**.
The factorial design / panel aggregation / routing
policy / PROTOCOL / fail polarity / Fabric packs /
rubric compiler / pre-registered plan is exact work.
Treating a zero binary name gap as a fairness
certificate, letting Jev emit the verdict string,
pasting PrismNLI's lead without the contamination
caveat, treating J7 pass as safe to obey, treating a
receipt as authorization, or hard-gating confidence
≥0.95 is the same theater. rh-guard owns injection.

2145 envelopes (`notes.md` §102), still outside the extras
template:
question-linting of Jev questions themselves;
nine jaggedness rules, no API key, no labelled data;
static lint ≠ measured separation;
yodablocks/jevq ≠ tenbin ≠ JevLint ≠ commitjev;
open-weights Laya as class exemplar (binding);
Nx/Bumblebee runtime;
host chooses backend;
ChristianAlexander/laya_ex ≠ system_one_sdk ≠ dannote/jev ≠ NandhaKishorM/laya;
on-chain/edge Laya deploy;
parity_verified stays false;
model output never grants Tx;
humandebri/IC-Laya ≠ laya_ex;
auditable weekend replica;
Jev outputs never used for training;
soft human-vote distributions;
unpaired 0.577 vs 0.727;
agilabs-ai/jev48 ≠ JevBench ≠ Mapika/decider;
adversarial dual-judge / framing attack surface;
comparative framing is the usable judgment;
prior injection crowds out evidence;
copyleftdev/ember ≠ ember.js;
Laya specialist fine-tune pipeline;
training still GPU-pending;
PIXELZX0/XERON ≠ convaiinnovations/laya;
Hub Laya replica drop;
daliborsb/laya ≠ convaiinnovations/laya ≠ NandhaKishorM/laya;
System One student distillation corpus;
gold is programmatic;
teacher is closed-API clone;
do not distill Jev as teacher of record;
MagaBitmex/jev-4b-distill-data ≠ missing student checkpoint;
non-LLM VIN System One;
planning depth not chat;
lewislululu/jevon ≠ douglance/jevon;
source-bound evidence checks;
local quote mismatch needs no API;
exit 0 ≠ claim truth;
WaynezProg/jev-kit ≠ jonathanavis96/jev-kit (Airlock) ≠ jev-use ≠ jev-mcp.
Soft Noul ≠ hard safety: 0.03s / 62 tests / 4.8 MiB /
0.577 / +26,744 / maze 1.0000 / exit 0 are **sensors**.
The jaggedness regex / Nx backend / canister schema
stamp + mock ledger / weekend freeze / kernel+doctrine /
programmatic gold / VIN recurrence / local quote match
is exact work. Treating a clean jevq run as measured
separation, treating 62 tests as Laya parity, letting a
Score grant Tx, pasting AUROC as a phishing win,
injecting priors as help, treating v4 as a controller,
distilling Jev as teacher of record, or treating exit 0
as claim truth is the same theater.

2246 envelopes (`notes.md` §103), still outside the extras
template:
independent System One evidence catalog;
19 reviewed records;
scores not one leaderboard;
no external record currently reproduced;
TokenTrim no-Jev matched hybrid 62.4%;
reachjalil/system-one-bench ≠ mallahyari/system-one-benchmark;
21 tasks · 134 items · 208 questions;
scenes from public GitHub contracts, not production logs;
SivletLabs/jev-eval ≠ willkelly/jev-evaluation ≠ 4esv/jev-eval ≠ xxkuboxx/jev-eval ≠ onlyoneaman/jev-eval ≠ dayhaysoos/jevals;
option isolation (sibling-blind);
permutation-equivariant;
Hub OWNER not published;
nafisazizir/hev ≠ jaredpalmer/kev;
frozen local LLM logits, no trained decision head;
residual-head 9,222-param decreased 73/96→67/96;
confidence = 1−normalized entropy, not P(correct);
yuki-oshio/mini-jev ≠ r-ms/mini-jev;
Jev classifier as autoregressive next-token predictor;
ChatJev-style soundness theater;
erik-dunteman/ChatJev ≠ dannote/jev ≠ jev-gpt;
calibrated decision head × AlphaProof value head;
implementation-layer isomorphism, semantic difference;
timeout = censoring;
do not launder Noul as proof;
parallel rank-prediction vs serial selection;
independent questions can conflict;
zzzzzec/jevsort ≠ keltokhy/jsort;
curated open System One ecosystem catalog;
rupeshpoojary9/awesome-open-system-one ≠ AnotiaWang/awesome-jev;
arXiv paper radar with Jev relevance scoring;
ranking ≠ calibration / 0.5 still soft;
fail-open failed evals not marked seen.
Soft Noul ≠ hard safety: 62.4% / 208 questions / 80.00% /
93.25% / 73/96→67/96 / “kinda works” / 0.5 are **sensors**.
The catalog labels / freeze / option mask / logit read /
Choice tree (jev-gpt) / Lean kernel / serial selection /
open-side list / fetch+persist is exact work. Treating a
catalog row as a bake-off win, putting Jev in an AR
next-token loop, laundering a Noul as a Lean step, treating
timeout-dropped samples as a full distribution, or
hard-thresholding paper-radar 0.5 as frequency is the same
theater.

2340 envelopes (`notes.md` §104), still outside the extras
template:
train calibrated ~27M from scratch;
typed Q→prob dist / one forward pass / no LLM decode;
hyusi2003/MiniSystemOne ≠ Colvin0315/MiniSystemOne;
description-only stub / size 5;
ESCI hard probe fails four of six;
jev_bool ECE 0.242 inversion 0.255;
do not re-fold §60 six-gates as new;
constrained logprob + temp/Platt ≠ Noul;
OpenJevPro pastes openjev-sglang JevBench as own;
PolyForm Noncommercial;
distill-Jev UI stub / do not distill Jev as teacher of record;
Jairik/jev-distiller size 1;
demo P(True) 0.5052 / Choice conf 0.2872 / Score conf 0.0055;
README claims MIT / GitHub license null / no LICENSE file;
hashed n-gram encoder / rival-aware attention;
shuffled-context control 0.335.
Soft Noul ≠ hard safety: ~27M / 0.242 / 0.255 / size 1 /
95.5% pasted / 0.5052 / 0.916 are **sensors**. The
from-scratch encoder / SQL secondary key / grammar mask /
Brier training / commit-pin / rival attention is exact work.
Treating a description-only stub as a checkpoint, re-folding
six-gates as new, distilling Jev as teacher of record,
pasting openjev-sglang as OpenJevPro, treating constrained
logprob as a Noul, or quoting 0.916 as a class ceiling is
the same theater.

0042 envelopes (`notes.md` §105), still outside the extras
template:
structured probability readouts;
distribution > argmax;
Noul 0.5 midpoint;
score is expectation not integer;
bare HTTP not SDK;
Arohtea/jev-readout;
Jev-style Choice/Score/Noul from ordinary models;
optional DSH plugin;
schema-valid ≠ calibrated;
gulagala001/jevify ≠ Mintzs/jevify;
Laya RLCD benchmark;
40.3% below constant-answer;
open-weight measurement;
mourad-ghafiri/laya-rlcd-benchmark ≠ yibie/laya-jev-lab;
cheap fail-open semantic edge;
second signal not sole;
FastLoopError catch;
SupremeDreamZ/jev-fastloop ≠ jev-ultrafast;
asking more questions in one call;
0.980 at every N;
nearly not fully deterministic;
TheWebDevel/jev-fanout;
Qwen3-VL perception + Jev decisions train RL;
0 model calls at deployment;
VLM alone 1.7 vs +Jev 4.4;
harneet2512/reflexrl ≠ khordoo/jev-reflex-autonomy-lab;
independent Jev API vs Laya;
cascade 0.60 matches 78% at 1.8×;
noul facts not judgements;
yibie/laya-jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab;
GLiNER vs GLiFormer vs Laya vs Jev;
extractors ≠ decision engines;
Laya dict-instructions collapse 58.3%;
umstek/zero-shot-ie-bench;
decisions-per-minute & cost;
204 moves vs 73;
throughput not intelligence;
angelgalvisc/snake-arena-jev-vs-llms ≠ vtrivedy/jev-plays-games;
behavioral contracts;
pin expectations eval upgrades;
raw 0.94 is not a release;
sathariels/jevcheck ≠ dayhaysoos/jevals ≠ SivletLabs/jev-eval;
evidence-linked dependency upgrade;
Jev never generates filenames;
no_direct_evidence ≠ safe to merge;
GaneshVG18/upgrade-radar ≠ LYchoon/paper-radar-jev;
discography theme/mood/complexity;
five atomic questions one call;
lirantal/discoprint.
Soft Noul ≠ hard safety: 0.5 / 40.3% / 0.980 / 4.40 /
78% / 0.60 / 21 pts / 0.94 / `no_direct_evidence` are
**sensors**. Bare HTTP bytes / adapter normalization /
constant-answer / first-signal retrieval / packed-question
experiment / pixels-only policy / cascade as compromise /
extractor spans / pin+replay / code-owned spans / catalog
fetch are exact work. Treating displayed p as proof,
schema-valid JSON as a calibrated Noul, 40.3% without the
constant-answer, fused fastloop p as safety, 0.0000 sd as
universal determinism, 2.95× as Harbor, cascade 0.60 as a
hard gate, locate as decide, snake points as intelligence,
jevcheck as a correctness proof, `no_direct_evidence` as
merge-safe, or a theme Choice as a music-theory certificate
is the same theater.

0145 envelopes (`notes.md` §106), still outside the extras
template:
Turn any open LLM into System-One Jev;
uspraveen/Jevify ≠ Mintzs/jevify ≠ gulagala001/jevify;
description-only stub / size 0;
Exu is a toolkit, not a method;
strictly proper scoring rule;
JSON parse of generated text ≠ Noul;
hard budget filter before Jev;
Jev never asked to perform budget arithmetic;
Jev judges the next state, XState enforces transitions;
simulation uses synthetic keyword fixtures;
classifier.dev fast tier 84.8 is Jev behind its own API;
do not re-fold §78 v1.2 board as new;
do not reopen or amend PR #23.
Soft Noul ≠ hard safety: 90.5s / 91.1% / 46x / 92.58% /
84.8 / ★339 / T=1.75 are **sensors**. The budget filter
in code / XState envelope / from-scratch recipe /
strictly proper scoring / catalog map are exact work.
Treating a Jevify two-liner as a checkpoint, letting Jev
do budget arithmetic, treating XState as Jev, treating
JSON parse as a Noul, or quoting 84.8 as a class ceiling
is the same theater.


0243 envelopes (`notes.md` §107), still outside the extras
template:
Benchmark-driven Jev router and judge;
cheap alone is not success;
Jev does not write, sum prices, or claim accuracy %;
hard budget/threshold/fallback stay in code;
previous_ticket_count >= 3 is code;
MIN_CONFIDENCE 0.6 still soft;
confidence ≥ 0.85 hard-gate is theater;
generative AI banned from scientific plots;
100/100 easy T/F is not Harbor;
label_mass ≠ correctness;
PR #1 now closed unmerged;
do not re-fold §71 claim-audit as a beat;
structured ≠ correct;
do not reopen or amend PR #23 or #24.
Soft Noul ≠ hard safety: 94.2 / 89.7 / 62.3% / 4.5pp /
0.85 / 100/100 / 77.10% / 107★ / T=1.05 are **sensors**.
The router threshold/fallback/budget / ticket count>=3 /
generative-AI-ban-on-plots / Hub recipe without weights
are exact work. Treating a 0.85 figure FAST_PATH as a
proof, 100/100 easy T/F as Harbor, label_mass as
correctness, 77.10% as beating Jev, hard-gating ticket
0.6 as safety, or re-folding §71 as a beat is the same
theater.




0345 envelopes (`notes.md` §108), still outside the extras
template:
bonzi-27b-v2 / ternary-8b / 27b-v1 GGUF family densify;
Bonsai 1 27B Q1_0 runs on stock llama.cpp;
ternary still needs PrismML fork;
parser owns the wall clock;
titles selected not generated;
mechanical tells in code;
select_threshold returns inf;
T never changes argmax;
confidence ≠ top-label p;
Jev agreement is similarity, never ground truth;
no aggregate quality grade or merge gate;
do not reopen or amend PR #23 or #24 or #25.
Soft Noul ≠ hard safety: 74.6% / 0.980 / 0.058 / 0.855 /
12/12 / 63/63 / 0.466→0.081 are **sensors**. The parser
clock / regex mechanical tells / select_threshold inf /
PrismML-fork vs stock llama.cpp split / titles selected
not generated are exact work. Treating injection ECE
0.058 as a hard gate, 40-row T as production, 12/12 as
pipeline equality, rank 1 without question-asymmetry,
or WANLI-256 as Harbor is the same theater.

0439 envelopes (`notes.md` §109), still outside the extras
template:
Gemma-4 26B-A4B jevify classification+calibration;
Hub jevify merged LoRA ships weights;
PAWS 0.580/ece 0.288 is the weak cell;
proposed ≠ authorized;
git-confess code owns counting/blame/ratio;
source receipts + confidence slider re-policy without re-inference;
7 bands 6/10 vs 40 bands 0/10;
pointer-not-generator 400 human-authored responses;
confidence is function of p_max (r=1.000);
MASSIVE no detectable difference at n=600;
do not reopen or amend PR #23 or #24 or #25 or #26.
Soft Noul ≠ hard safety: 0.834 / 0.844 / 88.3→77.3 /
32/32 / 85.0% / 11% / +12.40% are **sensors**. Physics /
git blame / KG authorization / reply bank / fills/PnL /
Worker thresholds / pre-registration are exact work.
Treating jevify ECE 0.061 as a hard gate, 0.8 evidence as
proof, /judge 0.5 as truth, 32/32 as production, gated
100% as production, git-confess 11% as a person verdict,
or paper-trader fills as edge is the same theater.

0541 envelopes (`notes.md` §110), still outside the extras
template:
“0.9 is not one number”; ranking ≠ calibration;
Score is 0..n-1 expectation not 0–1;
Noul has no confidence field;
type reliability is not a reason to choose Jev (json_schema 5/5);
treating 0.85 as 85% / minProbability hard-gate as Harbor;
VERIFY acquires discriminating evidence, never same-pool confidence-only rescoring;
fast/full/max are ceilings not sizes;
Solar writes, Jev chooses NEXT ACTION;
pattern exact, judgement must clear floor;
no matching pattern → no model call;
not a correctness oracle;
Jev judges / agent reasons / user decides;
selecting an option is not permission to implement;
Spec vs artifact remainder;
r = c - p_a;
Independent primitive;
do not reopen or amend PR #23 or #24 or #25 or #26 or #27.
Soft Noul ≠ hard safety: 0.9 / 0.85 / 8/8 / 0.021 / 0.464 are
**sensors**. Parse/extract / regex/pattern / VERIFY envelope /
user decision / mdast/root jail / search ceilings / json_schema
request-body fields are exact work. Treating 0.85 as 85% /
minProbability hard-gate as Harbor, 0.9 as one number, 8/8 as
conversion lift, Score as 0–1, or Noul.confidence as existing
is the same theater.

Hourly 0541 uniqueness lock: Blackwood tracker ABSENT; likes 2 gated manual; ECE 0.021; acc 0.807 vs warmup 0.746; calibration beyond ~500 tokens unmeasured; 11.57s vs 54.10s · 4.67× · 120/128 *theirs*; default path is pretrained Gemma probs not trained RLCD head; GH Meanblock 404; lock leesk212/JEV-CPU; softmax over letter slots ≠ Noul; WANLI 0.741 vs openjev v2 0.77 *theirs*; 3-way NLI ≠ Noul; priority 0.464 = majority floor; banking77 contaminated; raw margins not probabilities; GH jev-haiku-benchmarking 404; do not distill Jev as teacher of record (they distilled Haiku); banking77 0.8–0.9 stated 0.86 actual 0.73 over-confident *theirs*; ≠ Praveenrajus/jev-bench ≠ fstandhartinger/jevbench; $0.0000153–$0.0000226 vs circulating $0.0004 (~20×); TCP floor 198.8 ms; gateway tax not one number; Function-only 5/8 vs hybrid 8/8; 4/8 without Jev; 8 designed cases not conversion lift; ≠ RadRebelSam/awesome-jev; 200-row pilot Jev 86.5% 173/200 vs Gemini Flash-Lite 86.0% 172/200 vs Pro 87.0% 174/200 *theirs*; NLI Tetris argmax P(entail)−P(contradict); 情緒測謊器; 1q 396ms / 30q 567ms; ±0.03; 33q $0.000045 vs Gemini ~5× slower ~60× cost *theirs*; ≠ realZachi/jevtest; 8-example Jev vs GPT-5.6 Sol ~64× cost 5.4× latency *theirs*; synthetic; no inference; ≠ JevBench v1.2 §78; Judged 3317 / listed 2560; Jev judges, code applies policy; catalog ≠ endorsement; APA “microsecond policy / zero hallucination” overclaim; Client-side quiz; pointer from held docs; scanned-PDF warn; CSP only api.typesafe.ai; degraded fallback; $0.00022 vs chat $0.00306 *theirs*; SemIf 2186★ (+20 vs §109 2166); jevlike 1038★ (+7 vs 1031); TypeAR 14★ flat; AnotiaWang 96★ (+1 vs 95); yibie/awesome-jev 490★; Laya likes 802 (was 783); tracker likes 64 flat, lastModified UNCHANGED; do not reopen or amend PR #23/#24/#25/#26/#27.




0743 envelopes (`notes.md` §113), still outside the extras
template:
None of the systems are particularly good at knowing when to stop and ask;
A provider failure, timeout, malformed output, or missing answer is **not** a policy outcome;
confidence is descriptive provider output, not a substitute for probability;
Quality denominators include only valid scored answers;
an exact halfway tie chooses the lower level;
The pages never call Jev;
Low support becomes decision: "review";
The local path does not claim to turn a smaller checkpoint into Jev;
结构兼容，不是 Jev 模型能力;
They skip the question and call a tool directly;
100% schema pass;
40–48 rows too small to ship T;
T never changes argmax;
Finding 1: Brier on stated confidence alone is a trap;
do not reopen or amend PR #23 or #24 or #25 or #26 or #27 or #28 or #29 or #30 or #32.
Soft Noul ≠ hard safety: 77.0% / 0.85 / 90.53% / ACT / 0.0207 are
**sensors**. Contracts / denominators / halfway ties / cache / gold
audit / validators / ERROR/FATAL protection are exact work. Treating
77.0% as Harbor, 0.85 as 85%, 100% schema as correctness, ACT as a
provider proof, or TF-IDF ECE as beating Jev is the same theater.

Hourly 0743 uniqueness lock: Heman10x-NGU/Verdict-open-jev ≠ Heman10x-NGU/openJev-verdict-2.0; TF-IDF + LogReg ECE 0.0207 vs Jev 0.1440; Verdict-open-jev 48.07% vs Jev 90.80%; abstention combined recall 10.00%; p50 35.58 ms; K=25 (maximum capacity) 72.00%; 0.85 coverage 84.60% selective risk 1.18%; 26.1× faster than standard Qwen JSON generation; Jevify 90.0% / 167 ms CUDA graphs disabled; Finding 1: Brier on stated confidence alone is a trap; grpo_rlcr 0.78 / ECE 0.084; reliability 0.007 but resolution 0.000; 27 900 schema-driven decisions; 13 600 / 13 600 questions; candidate mass min 0.99999624; 22 configs · 166,054 rows · 4 calibration-gold; sha a39eba3f; Student B MAE 0.148 / Pearson 0.836 / 86.0%; pngwn/open-jev-laya-bench README 404; sha 9f69c742 likes 2; HDFS 0.9933 (745/750) / retain 0.0084; BGL ERROR/FATAL protection 1.0000; 2,479 / 2,500 HDFS uncertain; cache hit 0.9648 (2412/2500); $0.153936 estimated; E2 recomputes from saved probabilities; Space sha eda59e0a; MASSIVE English 0.783 / Khmer 0.033 / Hindi 0.133; 40–48 rows too small to ship T; T never changes argmax; siren2345/jev-single-decode-transformers ≠ siren2345/jev-single-decode; Split Transformers experiment from llama.cpp runtime; tanayvasishtha/jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab ≠ yibie/laya-jev-lab; Four experiments stress-testing TypeSafe's Jev: calibration, bundle bias, label bias, and ensembling; second pass must be $0.00 from cache; The pages never call Jev; Gemma 4 31B 77.0% / Jev 1.13.0 61.4% / Laya 322M 0.0%; restriction state 95.0% against 84.4%; None of the systems are particularly good at knowing when to stop and ask; They skip the question and call a tool directly; 100% schema pass; six-field joint 48.8% vs 72.8%; ywchiu/jev_benchmark ≠ Running-Dolphins/jev-bench ≠ Praveenrajus/jev-bench; ACT / REVIEW / FALLBACK; A provider failure, timeout, malformed output, or missing answer is **not** a policy outcome; confidence is descriptive provider output, not a substitute for probability; Quality denominators include only valid scored answers; an exact halfway tie chooses the lower level; aiwithenoch/Jev-Skill ≠ simplosophy/jev-skill ≠ laguagu/jev-skills; The local path does not claim to turn a smaller checkpoint into Jev; Low support becomes decision: "review"; MIT-0 SPDX NOASSERTION; current-llm; 结构兼容，不是 Jev 模型能力; altryne/jevify ≠ Mintzs/jevify ≠ gulagala001/jevify ≠ uspraveen/Jevify; Find where Jev belongs. Design the questions. Measure the difference; TypeAR-AI/TypeAR 301 → TypeLLM/TypeLLM; TypeLLM/TypeLLM 16★; SemIf 2237★ (+30 vs §111 2207); jevlike 1049★ (+6 vs 1043); AnotiaWang 98★ (+1 vs 97); yibie/awesome-jev 521★ (+15 vs 506); Laya likes 861 (was 822); tracker likes 66 (+2 vs 64); lastModified UNCHANGED `2026-09-20T04:29:16.000Z`; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#32; notes.md §113

0646 envelopes (`notes.md` §111), still outside the extras
template:
Calibration is not alpha;
default 0.5 keeps zero non pinned;
judges results it never sees;
task-finish eval not built yet;
paired Jev accuracy-difference intervals include zero;
not evidence of equivalence;
softmax over A/B/C ≠ Noul;
overconfident;
40-line windows cannot prove whole function;
default threshold 0.8 still soft;
contract_passed is not a claim of guaranteed factual truth;
Wilson lower bound 0.85 floor;
missing key cannot break the experience;
do not reopen or amend PR #23 or #24 or #25 or #26 or #27 or #28.
Soft Noul ≠ hard safety: 0.5 / 0.8 / 0.85 / 0.0421875 / 90.53% are
**sensors**. Threshold / policy / replay / windows / token spans /
Wilson floor / fees/slippage are exact work. Treating ECE as alpha,
0.5 compaction as safety, 0.8 as 80% correctness, or contract_passed
as truth is the same theater.

Hourly 0646 uniqueness lock: Calibration is not alpha; NO CURRENT ALPHA CANDIDATE; ΔR² approximately +0.00084; Brier 0.2131387; ECE 0.0421875; Adding Jev probability to deterministic volatility improved Brier by only 1.4058e-05; default 0.5 keeps zero non pinned; keepResult median 0.14 to 0.17; keepCall median 0.28 to 0.35; usable range is about 0.10 to 0.25; 7.8% to 57.9%; judges results it never sees; task-finish eval not built yet; $0.002 per compaction; slavadubrov/sgr-judge-bench ≠ slavadubrov/jev-judge-bench; Jev 108/120 $0.083 0.34 s; Luna SGR 114/120; paired Jev accuracy-difference intervals include zero; not evidence of equivalence; GLM SGR 26/120 93 format failures; Terra-planned Jev hybrid 55/120; rule-based by default, optionally Jev-backed; empty README; missing key cannot break the experience; prefill plus exactly one decode; softmax over A/B/C ≠ Noul; BBQ 9,053/10,000 (90.53%); ECE 0.0890; Mean confidence 0.9943; overconfident; score and noul not implemented; DGUI 12 rows (was 6); INSTRUCT 119 rows likes 2; encode the state once, decide everything in parallel; 0.740 accuracy against a 0.508 majority; ECE 0.047; fine-tune's advantage ends where its 384-token training data does; jasonkneen/open-jev ≠ pngwn/open-jev; same sha d41dc3cd; Space does not call Jev; recomputes routing from saved probabilities; 200-case Jev 97.0% / 100.0% / 95.0% / MAE 9.22; synthetic repository benchmark; Jev evaluations are advisory; YehuiTang0316/jev-nlgrep ≠ Bentlybro/jevgrep ≠ can1357/jegrep ≠ uehaj/jev-semgrep; default threshold 0.8 still soft; 40-line windows cannot prove whole function; token-native sequential start/end Choice; Gemini/Haiku stubs not configured yet; handful of hand-written examples, not a benchmark; Jev judged exactly what it was given; laguagu/jev-skills ≠ laguagu/jev-evidence-lab ≠ Pleo2/awesome-jev-agent-skills; contract_passed is not a claim of guaranteed factual truth; Wilson lower bound 0.85 floor; fixture mode no savings claim; SemIf 2207★ (+21 vs §110 2186); jevlike 1043★ (+5 vs 1038); TypeAR 15★ (+1 vs 14); AnotiaWang 97★ (+1 vs 96); yibie/awesome-jev 506★ (+16 vs 490); Laya likes 822 (was 802); tracker likes 64 flat, lastModified UNCHANGED; do not reopen or amend PR #23/#24/#25/#26/#27/#28.

0806 envelopes (`notes.md` §112), still outside the extras
template:
Jev vs GPT-5.6 bakeoffs are a category error;
encoder / ZS classifiers;
softmax/ZS scores still ≠ calibrated Noul;
soft scores ≠ hard gates;
do not invent accuracy numbers;
do not reopen or amend PR #23 or #24 or #25 or #26 or #27 or #28 or #29.
Soft Noul ≠ hard safety: 0.504 / 0.479 are **sensors**.
Policy / allowlist / thresholds are exact work. Treating a
ZS softmax as a fail-closed safety bar is the same theater.

User-provided 0806 uniqueness lock: people who compare Jev against GPT-5.6 has never fine-tuned BERTForXYZ for living and it shows; zero shot classifiers; scale them as much as decoder only models; many problems solved with LLMs could have been solved with them, it was a skill issue; opt for DeBERTa and ModernBERT ones; BERTForXYZ → DeBERTa → ModernBERT; Jev vs GPT-5.6 bakeoffs are a category error; encoder / ZS classifiers; institutional HF voice; quote *theirs*; do not invent accuracy numbers; softmax/ZS scores still ≠ calibrated Noul; soft scores ≠ hard gates; @mervenoyann; likes 421 / 189; impressions 35498 / 9613; multimodal image<>text ZS as perception front-end; hf:MoritzLaurer/deberta-v3-large-zeroshot-v2.0 likes 139; hf:MoritzLaurer/ModernBERT-large-zeroshot-v2.0 likes 72; Bart, bert, deberta, modernbert, these are all LLMs; Maziyar quoted; Jev is exemplar not the mandate; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29.

Propose two placements if the hole is mixed (e.g. TLA+ on the protocol
+ DST on the SDK + judgment triaging failing seeds). Do not invent a
hybrid "verified by Noul" API.

Related: `formal-semi-formal.md` (one screen); `mental-models.md`;
`mappings.md` §6–§19; `methods-catalog.md` verification rows;
`composition-algebra.md` positions 3 and 9; `mixed-architecture.md`
preference lint; `faq.md`; `boundary-audit.md`.
