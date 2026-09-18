# Formal & semi-formal methods × System One judgment (Jev-class)
**Date:** 2026-09-18 (America/Boise)  
**Audience:** Augustus De Morgan skill (design-judgment) + CloudAgent skill edits  
**Companion:** `MENTAL-MODELS-ACROSS-DOMAINS.md` (math/logic/algos across life & work — FM is one pillar)  
**Curriculum:** `FORMAL-METHODS-CURRICULUM.md` (Basit source list)

**TypeSafe Jev / System One class:** fast discriminative judgment — shared state + typed questions → Choice / Score / Noul distributions; **code owns policy**. Species includes Jev, Laya, GLiClass/GLiNER, listwise scorers, jev-visual. This note is about *placement* of that class relative to specs, checkers, monitors, simulators — not about cloning weights.

Statuses (Augustus): **Contract** / **Empirical recipe** / **Hypothesis**.

---

## 0. One sentence

Formal methods own **what must be true of a model**; semi-formal methods own **shared design vocabulary**; System One owns **fast semantic estimates under uncertainty**. Mixing them is powerful when ownership is explicit — and catastrophic when soft judgment is laundered as proof, or when a Noul gate pretends to be an atomic safety check (TOCTOU).

---

## 1. Crossover metaphors — judgment placement as engineering tolerance

Crossover Project (Hillel Wayne) and Vanderburg (*Real Software Engineering*) argue SE borrows poorly when it copies slogans and well when it copies **measurement + feedback under load**. Map those metaphors onto *where* a Jev-class judgment sits:

### 1.1 NATM / sequential excavation ("design as you monitor")
[New Austrian Tunneling Method](https://en.wikipedia.org/wiki/New_Austrian_tunneling_method): mobilize inherent rock strength; thin primary lining; **instrument and adapt**; classify ground and only then choose support.  
**Jev placement:** observational sensors (Noul/Score on traces, tickets, UX signals) = convergence gauges. **Code + FM** = shotcrete schedule and invert closure (hard structural ring). Do not thicken soft judgment into a "structural" wall — that is Heathrow-style NATM *abuse*: method blamed when management skipped monitoring and contracts.

### 1.2 Snap-fit tolerances
Snap-fits succeed when **clearance, lead-in, and retention** are designed as geometric tolerances, not vibes.  
**Jev:** clearance = abstention band; lead-in = cheap prefilters; retention = irreversible-action thresholds with hysteresis. Soft score spacing ≠ mechanical interference fit (**Contract** Score docs: equal scores can hide different tail risk).

### 1.3 Norman — gulfs of execution & evaluation
*Design of Everyday Things*: gulf of execution (intent → action); gulf of evaluation (world → perception).  
**Jev:** shrink evaluation gulf (typed reads of messy state); **never** claim to close execution gulf for privileged acts — code/UI/FM close that. Product & org design: judgment UIs that show distributions + confidence beat fake binary "AI said OK."

### 1.4 Leveson STAMP/STPA
Accidents from **inadequate control**, not only component failure. Hazards = violations of safety constraints in a control structure.  
**Jev:** judgment is a *sensor* or *controller estimate*, not the safety constraint. STPA-style: list unsafe control actions if a Noul is wrong, late, or missing; escalate with human/process controllers. Org: "we have a classifier" ≠ "we have a safety control."

### 1.5 Kent — Data and Reality
Models are approximations of messy reality; naming is load-bearing.  
**Jev:** question text / Choice sets / Score rubrics *are* the ontology. Wrong predicates → proof of the wrong world (see §7 harms). Spec languages force naming; System One makes naming cheap to *apply* at scale — both can encode a bad ontology.

### 1.6 Shirky — situated software
[Situated Software](https://gwern.net/doc/technology/2004-03-30-shirky-situatedsoftware.html): form-fit to a social group; rely on external reputation; refuse false scale.  
**Jev:** economics enable dense judgment *inside* a situated loop (team, product, agent). Do not universalize thresholds across populations (**Contract** calibration is positional). Semi-formal ADRs + local invariants beat enterprise ArchiMate theater when N is small.

### 1.7 Vanderburg / "Real SE"
Engineering = models under uncertainty + measurement closing the loop.  
**Augustus rule:** traverse **composition positions × constructs**; each cell needs a named caveat and a falsifier. FM and System One both fail when used as decoration.

**Metaphor → ownership table**

| Metaphor | Soft judgment owns | Hard/FM/code owns |
|---|---|---|
| NATM gauges | classify ground class, urgency | lining thickness, invert close, stop-work |
| Snap-fit | "feels seated" Score | geometry, go/no-go gauge |
| Norman | evaluation of state | executable actions & affordances |
| STAMP | estimate of process variable | enforced constraint / interlock |
| Kent | proposed names/features | schema + integrity constraints |
| Shirky | local meaning | community contracts & reputation outsides |

---

## 2. Spec languages & checkers (who owns what)

Amazon's [Use of Formal Methods at AWS](https://lamport.azurewebsites.net/tla/formal-methods-amazon.pdf) (Newcombe et al., 2014): TLA+/PlusCal as **exhaustively testable pseudo-code** for distributed designs; finds 35-step bugs reviews miss; does **not** prove code implements spec; weak on emergent soft real-time collapse. Still the industrial north star for "precise design before code."

### 2.1 Landscape (curriculum + adjacent)

| Tool | Role | Jev-class fit (**Hypothesis** unless noted) |
|---|---|---|
| **TLA+ / TLC / Apalache** | Temporal specs; exhaustive/symbolic MC | Prioritize which invariants to check; triage CEXs; NL→candidate props (**Hypothesis** — Hillel: LLMs write *weak* props) |
| **Quint** ([quint.sh](https://quint.sh)) | Executable specs, ITF traces, agent-friendly | Spec as CI artifact; Jev post-judge whether a trace "looks like" a known failure class |
| **P** ([p-org/P](https://github.com/p-org/P)) | Actors + systematic testing of concurrency | Failure-class Choice on bug reports; not a substitute for P's exploration |
| **Alloy** ([alloytools.org](https://alloytools.org)) | Relational FOL + transitive closure; **bounded instance finding** via SAT (Kodkod) — **not** Apalache | Deep section §2.2 |
| **NuSMV** | Symbolic MC for finite-state | Same as TLA: CEX triage, property ranking |
| **PRISM** | Probabilistic MC (Hillel dreidel essays) | System One ≠ PRISM; don't confuse Noul p with MC probability |
| **Event-B** | Refinement + proof obligations | Lemma/obligation triage |
| **mCRL2** | Process algebra | Niche; same triage pattern |
| **KeYmaera X** | Hybrid systems (discrete+continuous) | Domain experts own models; Jev for scenario labeling only |

**Apalache vs Alloy (non-negotiable distinction):** Apalache is a **TLA+** model checker (symbolic). Alloy Analyzer is a **relational** model finder / bounded checker for Alloy specs. Do not conflate in Augustus mappings.

### 2.2 Alloy — deep composition with Jev-class

Alloy = signatures + relations + predicates/assertions; Analyzer finds **instances** (examples) or **counterexamples** within a finite scope. Industrial/academic use: security models, config, API design, SysML executability (NIST IR 8388 Alloy for SysML behaviors).

**Frontier (2024–2026):**
- LLMs writing Alloy formulas — effectiveness study: https://arxiv.org/html/2502.15441  
- Anvil (MODELS 2026): LLM synthesis/validation/repair of Alloy — https://conf.researchr.org/details/models-2026/models-2026-research-papers/5/Anvil-LLM-Powered-Synthesis-Validation-and-Repair-of-Alloy-Specifications  
- LLM repair of declarative specs (Empir. Softw. Eng.): https://link.springer.com/article/10.1007/s10664-025-10687-1  
- DSN 2025 hybrid traditional+LLM Alloy repair: https://doi.org/10.1109/dsn64029.2025.00023  
- *foundry* — LLM concept design verified in Alloy 6 BMC: https://arxiv.org/html/2607.15718  
- Hillel *LLMs are bad at vibing specifications* (2026-03): https://buttondown.com/hillelwayne/archive/llms-are-bad-at-vibing-specifications — vibed Alloy with tautological asserts, missing `open util/boolean`, never run.

**Composition patterns (Alloy × Jev):**

| Position (composition-algebra) | Pattern | Ownership |
|---|---|---|
| Prior / selector | Choice over candidate predicates/assertions from NL | Analyzer accepts/rejects; human strengthens props |
| Post-judge | Score/Choice: severity & novelty of each instance/CEX | Soft triage only |
| Gate | Noul "is this CEX spurious wrt informal intent?" | **Never** closes the check — Analyzer does |
| Comparator | Rank which `check`/`run` commands to spend SAT budget on | Budget in code |
| Verifier (evidence only) | Noul "does instance match stakeholder scenario?" | Scenario library in code/tests |
| Operand | Features from instance graphs → CatBoost/policy | Version features with consumer |

**Help:** NL→candidate Alloy sketches; cluster similar CEXs; UI that narrates instances; filter "boring" examples when exploring `run` commands; repair-loop ranking (which conjunct to edit).

**Harm:** Soft judgment ≠ Analyzer check. A Noul that a formula "looks right" is **soundness theater**. Tautological asserts (Hillel) + LLM confidence = false assurance. Scope bounds mean absence of CEX ≠ proof outside scope. Wrong signatures = proof of wrong ontology (Kent).

### 2.3 Semi-formal specifically (Choice / Score / Noul / agents)

| Artifact | Use with System One | Keep in code/FM |
|---|---|---|
| UML/SysML state machines, Harel statecharts | Noul on "are we in suspicious region?"; Choice of repair playbook | Transition guards, timing, verified subsets (Gamma, SAVVS, Alloy translations) |
| ArchiMate | Score alignment of as-is vs to-be concerns | Governance gates |
| Structured English / GWT / EARS | Extract candidate invariants → Quint/TLA/Alloy | Acceptance tests |
| Decision tables/trees | Jev fills fuzzy cells; table is policy | Exhaustive table completeness |
| BPMN / sequence diagrams "as contracts" | Post-judge trace conformance (soft) | Executable monitors / RV |
| DbC lite / ADRs with invariants | Noul "ADR invariant threatened?" | CI checks, types, FM where critical |
| SysML v2 + LTL/Alloy/Isabelle pipelines (2024–25) | Triage proof failures | Proof/MC backends |

**Agent systems:** semi-formal diagrams are **shared memory** for humans+agents; System One classifies observations into diagram vocabulary; agents must not treat a sequence diagram as a runtime enforcer unless compiled to a monitor.

---

## 3. Deductive verification & code contracts

| Stack | Notes | Jev role |
|---|---|---|
| **Dafny** | Spec+impl; annotation bottleneck | Candidate invariants/annotator loops; **dafny-annotator** / **DafnyPro** (2024–26) |
| **JML / OpenJML** | Java contracts | Rank warnings; never auto-suppress |
| **Frama-C** | C ACSL + plugins (WP, Eva abstract interp.) | Alarm triage |
| **SPARK Ada** | Industrial proof + testing | Obligation prioritization |
| **Lean 4 / Rocq / Agda / HOL4 / PVS / ACL2** | ITP / dependent types | Lemma ranking, proof-step proposals; kernel decides |
| **seL4, CompCert** | Landmark verified stacks | Out of band for Jev — inspiration for "proof owns safety" |
| **SMT (Z3, CVC5)** | Backend to many tools | Soft models must not rewrite goals unchecked |
| **PBT / contracts / oracles** | Hypothesis, QuickCheck, etc. | Shrink/triage failures; oracle candidates (**Hypothesis**) |

**Frontier cites:**
- dafny-annotator: https://arxiv.org/html/2411.15143  
- DafnyPro: https://arxiv.org/pdf/2601.05385  
- Neuro-symbolic seL4/Isabelle proof search (~77.6%): https://arxiv.org/html/2603.19715v2  
- VerIbmc local LLM + ESBMC invariants: https://arxiv.org/html/2606.16886v1  
- Memory-aware specs + Coq refutation: https://arxiv.org/pdf/2603.13414  

**Rule:** LLM/Jev propose; **verifier refutes/accepts**. DafnyPro-style: forbid silent base-code edits that "make proof pass."

---

## 4. DST / exploration — Antithesis, Resonate, PufferLib

### 4.1 Antithesis (deterministic simulation / autonomous testing)
Docs: https://antithesis.com/docs/introduction/how_antithesis_works/  
Custom deterministic hypervisor; fault injection + input fuzz; **property-based** goals; RL-guided exploration of "multiverse" timelines; perfect repro. etcd robustness blog (2025): https://etcd.io/blog/2025/autonomus_testing_with_antithesis/

**Compose with Jev-class:**

| Role | Pattern |
|---|---|
| Oracle candidates | Humans/agents draft properties; Antithesis falsifies — Jev does not "pass" properties |
| Filters | Score which failing timelines are novel vs duplicate symptom |
| Triage | Choice over root-cause hypotheses *after* deterministic replay artifacts exist |
| Policy over exploration | Budget which properties/modules to emphasize next (**Hypothesis**) |
| Harm | Treating guided exploration coverage as proof; using Noul instead of an assert in-harness |

### 4.2 Resonate HQ — verified product identity
**Resonate HQ = durable async execution** (Distributed Async Await), **not** an unrelated "Resonate AI" brand.  
Docs: https://docs.resonatehq.io/ · Why: https://docs.resonatehq.io/evaluate/why-resonate · How tested: https://docs.resonatehq.io/evaluate/how-resonate-is-tested
Alt public testing writeup may live under docs.resonatehq.io / docs.resonatehq.io — verify current path; Lean+DST+differential oracle stack is the product claim.  

Correctness stack:
1. **Lean 4 executable abstract machine** + property catalogue (normative; prose loses to Lean) — https://github.com/resonatehq/resonate-specification  
2. **Differential random testing** vs independent in-memory **oracle**  
3. **DST** on TypeScript SDK (seeded, multi-OS CI)  
4. Protocol hooks for determinism (`debug_time`)  

**Compose with Jev-class:**
- Durable agent loops: Jev gates/reroutes **inside** `ctx.run` steps; Resonate owns crash-resume.
- Choice/Score for human-in-the-loop resume priority; **promises settle in protocol**, not via Noul.
- Triage differential-oracle disagreements (soft cluster → human).
- Harm: "agent-native" ≠ "judgment replaces Lean/oracle"; soft done-checks on workflows that must be protocol-true.

### 4.3 PufferLib
High-perf RL env library (~1M+ steps/s Ocean envs); PuffeRL; Protein sweeps.  
Paper: https://rlj.cs.umass.edu/2025/papers/RLJ_RLC_2025_151.pdf · https://puffer.ai/docs.html  

**Compose with Jev-class (mostly Hypothesis — matches composition-algebra open position "reward shaper"):**
- **Reward shaping / preference**: Score as *feature* into a learned reward model — not as online RL reward without observed outcomes (Augustus: speculative trees capped).
- **Done / success checks**: Noul only if environment also has hard probes; else probe owns concession (jev-mcts pattern).
- **Curriculum Choice**: select next env/task from bounded set.
- **Policy eval triage**: classify failure modes across millions of steps (batch Nouls).
- Harm: soft reward laundering; using Jev as physics; correlating judgments as if independent.

---

## 5. AI × FM frontier (2024–2026) — citations

| Item | URL | Takeaway for Augustus |
|---|---|---|
| Amazon FM PDF | https://lamport.azurewebsites.net/tla/formal-methods-amazon.pdf | Precise designs; MC finds deep bugs; code≠spec |
| Lamport Agent | https://zfhuang99.github.io/github%20copilot/formal%20verification/tla+/2025/11/14/lamport-agent.html | Agents draft TLA+ from codebases; human validates |
| CRAQ.tla example | https://github.com/zfhuang99/lamport-agent/blob/main/spec/CRAQ/CRAQ.tla | Artifact trail matters |
| Coming AI Revolution (Huang) | https://zfhuang99.github.io/github%20copilot/formal%20verification/tla+/2025/05/24/ai-revolution-in-distributed-systems.html | Automation narrative |
| Cauli — EuroSys 2026 obsolete | https://claudiacauli.com/2026/03/08/my-eurosys-2026-paper-is-obsolete | Effort numbers collapse; **vacuous models** risk rises; domain understanding must not go to zero |
| Hillel — vibing specs BAD | https://buttondown.com/hillelwayne/archive/llms-are-bad-at-vibing-specifications | Weak/tautological properties; experts extract more than beginners |
| Hillel — dreidel / PRISM | https://buttondown.com/hillelwayne/archive/i-formally-modeled-dreidel-for-no-good-reason | Right tool joy + limits of languages |
| Watchdogs & Oracles (RV×LLM) | https://arxiv.org/pdf/2511.14435v1.pdf | Bidirectional RV↔LLM |
| RvLLM | https://arxiv.org/abs/2505.18585 | Domain ESL + runtime checks on LLM outputs |
| TemporalGuard (ptLTL conversations) | SAIV 2026 / Springer chapter via BIU | Grounding NL→atoms is the hard part — **System One natural fit** |
| Neurosymbolic conformal classification | https://ar5iv.labs.arxiv.org/html/2409.13585 | Logic constraints + conformal sets |
| GUARDIAN runtime dual invariants | https://arxiv.org/html/2511.20570 | Calibrated neural + symbolic monitors |
| Perceive with Confidence | https://proceedings.mlr.press/v270/dixit25a.html | Conformal perception + planner |
| FIPER failure prediction | https://tum-lsy.github.io/fiper_website/ | Conformal OOD + entropy at runtime |
| ProofBridge / LeanMarathon / Theo | arXiv 2510.15681, 2606.05400, 2606.31134 | Autoformalization harnesses > single-shot vibe |
| PROOFGYM / ITPEval | OpenReview / arXiv 2607.19407 | Cross-ITP translation still hard |
| SysML formalization | NIST IR 8388; MODEVVA 2024 SAVVS; Springer SysML+LTL 2025 | Semi-formal → checkable |

**Cauli ∩ Hillel synthesis:** cost of producing *something that typechecks* plummeted; cost of producing **strong properties + validated models** did not. System One helps the *workflow around* FM (triage, ranking, UI, monitors) and must not mint fake strength.

---

## 6. TOCTOU — archetype of check-vs-act gap

[TOCTOU](https://en.wikipedia.org/wiki/Time-of-check_to_time-of-use): check property; act on result; concurrent change → act on stale truth. Classic `access`/`open`; still causing cloud outages (e.g. DNS plan races).

**Jev-class anti-pattern:**  
`if Noul(safe) > τ: perform_irreversible()`  
Even if τ is calibrated, the world (permissions, markets, agent state, tool outputs) can change before the act. Soft check is **not** an atomic interlock.

**Mitigations (map to Augustus boundary-audit):**
- EAFP: attempt privileged op with OS/DB enforcement; handle failure  
- Bind check to use (O_NOFOLLOW, transactions, compare-and-swap, capability tokens)  
- For agents: **pre-judge → code validates → act → post-judge**; only **probes** concede success (composition-algebra rule 2)  
- Hysteresis / time-bounded certificates; re-check inside the critical section  
- STPA: list unsafe control actions if judgment is skipped, delayed, or spoofed  

**Semi-formal:** sequence diagrams that show a check message then a later act message without an atomicity note are TOCTOU diagrams.

---

## 7. Where Jev-class HELP vs HARM formal pipelines

### 7.1 Help (keep / amplify)
1. **Oracle / property candidates** from NL & code (human or Lamport-Agent style) — always run through MC/ITP/DST.  
2. **Candidate filters** before expensive SAT/MC/proof.  
3. **CEX / failing-trace triage** (novelty, severity, suspected component).  
4. **Lemma / obligation / repair ranking.**  
5. **UI for specs** — narrate instances (Alloy), timelines (Antithesis), Quint ITF.  
6. **Runtime monitors** — ground NL events to atoms (TemporalGuard-shaped); conformal abstention.  
7. **Calibration layer** beside FM — statistical safety *around* learning components (PwC, GUARDIAN), not instead of proofs of protocols.  
8. **Semi-formal hygiene** — keep ADRs/decision tables filled; flag invariant drift.

### 7.2 Harm / anti-patterns ("soundness theater")
1. **Laundering soft judgment as proof** — "Noul 0.97 ⇒ safe to ship."  
2. **Hard-gating safety solely on Noul** — TOCTOU + false calibration.  
3. **Fake confidence** — confidence summarizes distribution shape; not P(world).  
4. **Proof of the wrong model** — vacuous specs (Cauli); tautological asserts (Hillel); omitted failure modes (Amazon liveness gaps).  
5. **Independent-Noul fallacy** — multiplying nouls ≠ joint probability (mappings §3).  
6. **Silent code changes to satisfy Dafny/Lean.**  
7. **Scope blindness** — Alloy/TLA finite models treated as ∀.  
8. **PRISM/MC probabilities confused with Jev probabilities.**  
9. **Reward laundering in PufferLib-class loops.**  
10. **DST coverage mistaken for verification of unstated properties.**

### 7.3 Harmful-uses checklist (copy into PR templates)
- [ ] Does a probabilistic gate authorize an irreversible act without a hard interlock?  
- [ ] Is any "verified" claim referring only to a model the team has not validated by breaking it?  
- [ ] Are properties strong (concurrency, multi-step) or tautological?  
- [ ] Are Choice options / Score rubrics versioned with the consumer?  
- [ ] Is abstention defined per-action with costs?  
- [ ] Are CEX/triage judgments stored as evidence, not enforcement?  
- [ ] Alloy vs Apalache vs TLC named correctly?  
- [ ] Resonate protocol settlement vs agent "done" Noul separated?  
- [ ] Antithesis properties written as harness asserts, not chat opinions?  
- [ ] Speculative MCTS/RL depth capped without a real simulator?

---

## 8. Augustus skill card drafts

### 8.1 New / extended mappings (extend decision-circuits card)

**Card A — Semantic predicates → decision circuits** *(exists; extend)*  
Add FM nodes as **exact** siblings: state machine transitions, Alloy preds, TLA conjuncts, Quint actions, monitor automata. Jev estimates only fuzzy predicates; circuit edges stay code/FM.

**Card B — Spec property pipeline** *(Hypothesis → promote with test)*  
`NL/ADR → candidate props (LLM/Jev rank) → human strengthen → MC/ITP/DST → CEX triage (Jev) → repair`.  
**Does not transfer:** ranking ≠ validity.

**Card C — Alloy instance loop**  
`run/check → instances/CEXs → Jev cluster+severity → edit spec or scope → re-analyze`.  
**Boundary:** Analyzer is source of truth for bounded claims.

**Card D — Runtime assurance sandwich**  
`conformal/System One abstain → symbolic monitor / RV → act`.  
Fits GUARDIAN/TemporalGuard shapes.

**Card E — DST multiverse triage**  
Antithesis/Resonate DST artifacts → Jev failure taxonomy → patch → regress under same seed/timeline.

**Card F — Durable agent control**  
Resonate checkpoints own durability; Jev owns semantic gates inside steps; protocol oracle owns correctness of promise state.

### 8.2 Non-negotiable boundaries (boundary-audit addenda)
1. Estimate ≠ measure; probe concedes.  
2. Soft check ≠ atomic check (TOCTOU).  
3. Weak property ≠ assurance.  
4. Vacuous model ≠ safety.  
5. Thresholds positional & dataset-local.  
6. FM tool identity must be precise (Alloy ≠ Apalache).  
7. System One does not generate open-ended proofs/code without a checker in the loop for high assurance.

### 8.3 Toolbox-sweep seeds (composition-algebra traversal)
Walk positions × constructs: TLC CEX, Alloy `check`, Quint ITF, P tester bug, Frama alarm, Dafny obligation, Lean goal, Z3 unsat core, Antithesis timeline, Resonate differential diff, PufferLib episode failure, SysML state, BPMN token, ADR invariant, STPA unsafe control action, NATM "convergence gauge", snap-fit go/no-go, Norman evaluation gulf.

### 8.4 Recommended CloudAgent skill-edit plan (prefer over hasty PR)
Repo `24601/Augustus`:
1. Append cards B–F sketches to `references/mappings.md` with Hypothesis status + acceptance tests.  
2. Add `references/formal-semi-formal.md` pointing at this archive note.  
3. Extend `boundary-audit.md` red flags with TOCTOU-of-Noul + vacuous-spec.  
4. Extend `composition-algebra.md` open positions with Alloy/DST/RV rows once tests exist.  
5. Optional: `carcinize-corp/Jev-omni` `docs/research/` copy of this file — parent/CloudAgent.

---

## 9. Semi-formal + agent systems (short)

Agents should treat semi-formal artifacts as **schemas for questions** (Choice sets = states/events; Nouls = guard suspicions; Scores = risk indices). Compilation path: semi-formal → Quint/TLA/Alloy/monitor whenever enforcement is required. Situated deployments (Shirky) may keep soft monitors longer — still label them soft.

---

## 10. Related archive
- `MENTAL-MODELS-ACROSS-DOMAINS.md` — decision theory, VOI, control, OR, epistemology, everyday placement  
- `FORMAL-METHODS-1PAGER.md` — executive  
- `FORMAL-METHODS-CURRICULUM.md` — source list  
- Augustus refs: mappings.md (decision circuits), composition-algebra.md, boundary-audit.md  
