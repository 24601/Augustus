# Mappings: classical methods → judgment-class designs

Each card: what transfers, what does NOT, a composition sketch, a non-ticket
example, a counterexample, an acceptance test. Jev is the documented
exemplar in the sketches; family choice (open head / GLi\* encoder /
listwise / vision) is `judgment-class.md`. Status words: **Contract**
(documented), **Empirical recipe** (dated observation), **Hypothesis** (test
before relying). Cross-domain frames: `mental-models.md`. Formal /
semi-formal ownership: `formal-methods.md` / `formal-semi-formal.md`.
Cards §6–§19 are **Hypothesis as domain-general products** until an
acceptance test runs; do not promote them from analogy. Read each card's
own labels rather than the range: §8's ownership split (sensor ≠
constraint) is **Contract** as a rule and §9's jev-mcts example is
**Empirical**, and what those cards claim *beyond* those components is
Hypothesis like the rest. Curriculum cards §10–§16 (spec pipeline,
Alloy loop, RV sandwich, DST triage, durable agents, assignment hybrid,
situated density) are the same rule. §17–§18 add paraphrase-stability
and structural-prove ∩ remainder (jevgate / OCR-router *shapes* are
Empirical; the cross-domain reading is Hypothesis). §19 is the
effect-oriented loop: soft Choice on the transition, host owns the effect.

## 1. Semantic judgments → features and explicit utility

**Method**: feature engineering, ordinal measurement, multi-criteria decision
analysis. **Transfers**: turning unstructured evidence into named, reusable
numeric features (Noul probabilities, Score distributions, stable Choice
categories). Judge once; explore many policies without rerunning inference —
sliders, weights, filters, Pareto views, or a supervised model on top.
**Does not transfer**: Score has no natural units. Normalizing by the top
level aligns ranges only — not spacing, importance, or cross-concept
comparability. Weighted sums express a chosen compensating policy; hard
exclusions stay as separate rules. A downstream model (e.g. CatBoost,
**Empirical recipe** per the autoresearch cookbook) learns only what labeled,
held-out outcomes establish — split data before label-driven rubric/feature
discovery and version feature definitions with the model.

```text
state = {paper: {...}, question: "..."}
questions = {is_rct: Noul(...), reports_mace: Noul(...),
             evidence_strength: Score([...4 levels...])}
code: shortlist, rank, filter — weights adjustable without re-inference
```

**Example**: research-reading map — extract reusability dimensions once, let
researchers re-rank and re-filter interactively. **Beyond SWE
(Hypothesis until labeled):** vendor bid/no-bid (fit, urgency, risk
Nouls; price and deadline exact); apartment shortlist (commute/light/
noise Scores; rent exact); hiring scorecard (evidence Nouls; labor-law
vetoes in policy). Full gallery: `mental-models.md` §MCDA.
**Counterexample** (from **Contract** Score docs): levels 0,1,2 with
distributions `[0,1,0]` vs `[0.5,0,0.5]` both score 1.0 with radically
different extreme-outcome risk — always read probabilities beside the
score. **Test**: beat a simple baseline and survive reasonable
weight/wording perturbations.
Links: Score docs, composite-scoring pattern, autoresearch cookbook.

## 2. Probabilistic judgments → cost-sensitive decisions

**Method**: selective classification, decision theory, cascades. **Transfers**:
choosing among act / decline / gather-evidence / escalate from the
distribution, with thresholds owned by each action's consequences. For a
calibrated binary probability with FP/FN costs: `t = C_FP/(C_FP+C_FN)`.
**Does not transfer**: universal thresholds (no magic 0.8); model probability
is not auto-calibrated on YOUR population — plot confidence vs accuracy on
your data (**Contract**: confidence summarizes distribution shape, nothing
more); Noul 0.5 ≠ medium-anything; top-Choice probability ≠ probability the
action succeeds when several options are acceptable.

```text
if confidence < floor: human review
elif action low-stakes: act
else: act only if confidence > high bar, else confirm
```

**Example**: trading bot acts on high-confidence reads, stands down when the
book state is ambiguous (jev-trader `late → hold`). **Beyond SWE
(Hypothesis until labeled):** inbox reply/snooze/archive; "is this paper
on-question?"; "call this lead / nurture / drop" — same act/abstain/
gather table, costs written in hours or dollars, threshold per *action*.
VOI: pay for the full PDF or the customer call only if expected decision
change beats the cost (`mental-models.md` §VOI, §decision).
**Counterexample**: a flat Choice over three fine categories may still
name a harmless best pick — low confidence need not veto a low-stakes
preference. **Test**: cost/coverage curve on held-out slices; score the
fallback too (escalation is not automatically correct). Links:
Confidence docs, confidence-routing pattern.

**Cascade / prefilter beside this card**: the same cost model, applied *before*
an expensive generator rather than after a decision. Drop or stub confident-
irrelevant chunks, log lines, or tool results so the LLM never sees them;
fail-open on retrieval (false drop loses evidence), fail-closed on dispatch
(wrong tool is an action). Detail cards: `references/applied-mappings.md`
(context sieve, keep/drop, ranking). Do not invent request fields here —
live docs own the call shape.

## 3. Semantic predicates → decision circuits

**Method**: decision tables, Boolean circuits, DAGs, finite-state machines.
**Transfers**: Jev estimates predicates too fuzzy for exact rules (tone,
aboutness, support); code owns branching, compatibility, transitions,
execution. **Does not transfer**: statistical independence — `P(A)·P(B)` is
NOT `P(A∧B)`; operation+target head pairs can be invalid (browser-use asks
both heads per request but executes only the matching target after
validation); relational judgments ("does passage support claim?") must stay
one question, not two split classifications; exact computation stays in code.

**Example**: game director — Jev judges whether player dialogue is
conciliatory or threatening; code enforces inventory, prerequisites,
chronology, reachable scenes (cf. HEIST//ONE: six guards batched, simulation
validates every proposal). **Counterexample**: decomposing tool-trace
verification into per-call schema nouls works; asking "is the trace correct"
as one Noul hides nine judgments. **Test**: full truth table / transition
cases incl. contradictory outputs, stale observations, invalid combos.
Links: how-to-build guide (decompose-state/questions), smart-home demo.

**Rejected beside this card**: "many Jev checks = independent verification."
Shared evidence, rubrics, and biases correlate failures. Ground checks in
authoritative evidence or executable constraints (citation_check,
classifying-RAG-passages, llm_guardrails cookbooks) and evaluate the
combined verifier as one system.

## 4. Retrieval → bounded semantic reranking

**Method**: candidate generation + expensive relevance function.
**Transfers**: retrieve broadly (index, filters, embeddings, BM25), then one
shared Score rubric for graded relevance, Nouls for binary relations, Choice
for picking among a bounded candidate set. **Does not transfer**: Choice
probabilities across DIFFERENT candidate pools are not comparable absolute
scores; a shared rubric is necessary but not sufficient for comparability
(evidence per candidate must be sufficient and consistent); reranking cannot
recover missing candidates; the 255-option limit is not a dataset-size limit.

**Example**: 1018-paper triage — cheap summarizer + one Jev Choice over 24
topics ($3.99 + $0.08). **Counterexample**: top-1 accuracy measured only when
the right answer is already shortlisted flatters the reranker — always
measure retrieval recall separately from rerank quality, end-to-end top-k +
cost. **Test**: recall split + end-to-end top-k + $/query.
Links: rerank, semantic_find, entity_alignment cookbooks.

**Budget note beside this card**: exhaustive pointwise scoring of huge sets
is not intrinsically wrong (offline, modest corpora) but it is not an index —
per-query work still scales with candidates. Low latency ≠ no retrieval.

**Store as the index (Empirical as a *shape*, 2026-09-18):**
[`kylemclaren/jevql`](https://github.com/kylemclaren/jevql) judges
schema-conditioned row objects; vanilla Postgres never sees `jev()`.
Cheap SQL first; the remainder is a typed Choice/Noul/Score over rows.
Row contents leave the database (same residency warning as AU health).
[`ant4g0nist/joxide`](https://github.com/ant4g0nist/joxide): zoxide owns
the directory index; Jev scores a shortlist; destinations are existing
local paths only; fail-open. `notes.md` §42.

## 5. Hierarchy → bounded heuristic search

**Method**: beam search over a meaningful taxonomy or candidate graph.
**Transfers**: Choice distributions as branch-priority heuristics; keep K
paths where early ambiguity matters; code owns frontier, budget,
termination, final selection. **Does not transfer**: the geometric-mean path
score is a ranking heuristic, NOT a calibrated leaf probability; multiplying
related-question outputs is not a path probability without a coherent
conditional structure; pruned branches never recover.

**Example**: patent/retail/biomedical/code hierarchies (cookbook,
**Empirical recipe** jev-1.12, 4 labeled cases: beam K=3 fixed 2 greedy
failures). **Empirical beside this card (255 cap, synthetic n=180,
2026-09-18):** [`reachjalil/jev-tree-choice-cap`](https://huggingface.co/datasets/reachjalil/jev-tree-choice-cap)
walks an authored region→service→mode tree so each Choice stays under
Jev's 255. Truncate-to-255 is **90/180** and **0/90 on the tail** (Cape
Town sits past index 255). Authored tree **180/180** (3 calls). Keyword
also 180/180 on this invented catalog — do not sell the tree as beating
lexical lookup; sell it as *not silently dropping the tail*. Flat
auto-partition 179/180. Tournament brackets stay rejected. Code:
[jev-tree](https://github.com/reachjalil/jev-tree). `notes.md` §33.
**Counterexample**: an arbitrary 255-way tournament bracket over
an unstructured shortlist — grouping changes judgments, early elimination
discards global top-k, log rounds ≠ sublinear work. Prefer retrieval or a
real hierarchy; tournaments are benchmarks, not defaults. **Test**: greedy vs
beam vs flat-shortlist baseline on realistic cases; inspect pruning failures;
judge finalists under one common leaf criterion.
Links: hierarchical_classification, skill_suggestion cookbooks.

**Empirical recipe beside this card (MCTS+Jev, launch week — verified in the
archive, not yet independently reproduced):** two implementations now exist.
`lhemerly/mcts-agent` splits roles: a generator proposes candidate actions
(once per expansion), then **one batched call** does all Jev work — Noul
prunes invalid actions (all candidates in parallel, keep ≥0.8) and gates
early stop (≥0.85); Choice supplies PUCT policy priors P(s,a) and picks the
branching factor from primes by uncertainty; Score (1–10 rubric) is the leaf
value V(s), replacing random rollouts. Q normalized /10; unvisited children
inherit the parent's value (first-play urgency) so one lucky child doesn't
starve siblings. `paulobueno164/jev-mcts` is the correction that makes the
pattern defensible:

1. **Fidelity is typed, not commented.** `grounded` environments (a real
   simulator exists) get depth up to 24; `speculative` ones (no simulator —
   every `apply()` is a guess) are hard-capped at depth 2, and `rollout()`
   throws. A tree built on guessed transitions scored by another model
   composes error instead of reducing it; the cap lives in code, not prose.
2. **Only probes concede.** Agent claims ("it worked") go to the journal and
   decide nothing; exit-code probes measured after execution are the sole
   source of granted milestones. "The tree supposes; the probe measures; only
   the probe concedes."
3. **Calibrate before thresholding.** Raw cutoffs (0.8/0.85) are replaced by
   a confidence curve calibrated against exact-search ground truth.
4. **Debias position.** Candidate order is shuffled with a seeded RNG and a
   second debias pass averages judgments with reversed order.
5. **Measured result** (24 scenarios, known ground truth, evaluator-prior
   arm): MCTS 24/24 vs greedy 1/24 — the win comes from a delayed-reward
   trap a 1-ply heuristic cannot see; evaluator-supplied priors changed cost,
   not outcome: 5893→2743 calls, 8.0→7.0 turns, $0.101→$0.047. First-call
   latency ~2s (handshake), then ~0.5s/judgment on a hobby key.

Still true, and sharpened: the Score value heuristic is the weakest link —
trust it only where the environment validates outcomes, and keep the
grounded/speculative split in types. Any depth beyond a simulator is
estimation wearing a measurement costume.

## 6. Value of information → gather as an enumerated act

**Method**: Raiffa-line decision analysis, EVPI / EVSI. **Transfers**:
another observation is an *act* whose cost you know (a test, a search, a
human, another batch of Nouls, an LLM autopsy). Pay iff expected
reduction in *decision loss* beats that cost — improvement in the
probability is not the quantity
(`mental-models.md` §VOI). Cheap fan-out of independent questions is
often +VOI because the second question is nearly free (composition:
width is cheap). **Does not transfer**: infinite clarifying questions;
paying for a paragraph when a Noul would do; treating another LLM call
as free information; a numeric EVPI computed from uncalibrated scores
and labeled Contract.

```text
belief  = current Noul / Choice / Score
acts    = {decide now, buy observation, abstain, escalate}   # you enumerate
loss    = table you wrote
pay iff E[loss | now] − E[loss | after paying] > cost
```

**Example (Empirical as a *shape*, OpenSmoke / env triage):** LLM autopsy
only on flags — a negative flag has no VOI in the autopsy
(`applied-mappings.md` §3). **SREGym-Lite (Empirical as a *shape*):**
Jev ranks the *next diagnostic test* among candidates the agent already
holds; it does not run the test and does not diagnose
(`notes.md` §33). Pay for the next kubectl/log only if EV(decision)
improves — a high review score cannot buy missing evidence.
**Meta-VOI (Empirical as a 149-row receipt, 2026-09-18):**
[`wotai-dev/typesafe-jev-tools`](https://github.com/wotai-dev/typesafe-jev-tools)
asks whether the decision needs a model at all: regex/DNS/query → no
model; one-second human from shown text → System One; multi-step or
prose → frontier. Same 149 business rows: Jev 79.9% vs Haiku 4.5 83.2%;
Jev 1.6× faster, not 20–200×; Jev confidence monotonic, Haiku inverts
in 0.80–0.95. If you do not *branch on confidence*, use whatever you
already have (`notes.md` §42).
**Beyond SWE (Hypothesis until you log
act/outcome pairs):** full PDF vs abstract; customer call vs CRM fields
that already fail a hard rule (credit limit is exact); blood test vs
wait. **Counterexample**: gathering until p = 0.99 on an irreversible
act that needed a probe, not another Noul. **Test**: a labeled log
where the extra observation changed the *act* often enough to pay;
score the cost of the observation too. Until that log exists, this card
stays **Hypothesis**. Links: `mental-models.md` §VOI, §decision.

## 7. Signal detection → criterion, not accuracy

**Method**: Green & Swets detection theory; ROC / PR operating points.
**Transfers**: a yes/no Noul is a noisy evidence variable; **d′** is
separability on *your* population; the **criterion** t is where policy
places the bar given base rates and costs. Shift t when the base rate
shifts (incident week, flu season, inbox after a launch) without
retraining "to be more careful." Fail-open vs fail-closed is a criterion
choice. **Does not transfer**: accuracy as the summary when the class is
rare; copying 0.7 from a blog; treating d′ as a vendor property;
thresholding a listwise or CLIP affinity as if it were P(signal)
(`judgment-class.md`).

```text
Noul ≈ evidence variable (noisy)
criterion t from costs and base rate     # policy
ROC / PR on YOUR labeled cases           # you owe this plot
report hits / false alarms at the operating point, not accuracy
```

**Example (Empirical as family shape):** firehose / Near Here moderation
— judge once, re-policy in code.
[`jp-sns-jev7-estimator`](https://huggingface.co/kokuren/jp-sns-jev7-estimator)
is the rare-class warning in one table: seven distilled teacher scores
that the card says are **not** calibrated probabilities, and `threat`
F1@0.5 = 0.0000 while mean accuracy@0.5 looks fine. Criterion, not
accuracy (`notes.md` §33). **Beyond SWE (Hypothesis until plotted):**
phishing screen; "is this a real deadline?"; hiring screen (base rate of
qualified applicants is the thing that moves). **Counterexample**:
retrain the model because last week's incident made you "want fewer
misses" — that was a criterion shift. **Test**: ROC/PR on held-out *your*
cases; report the operating point you actually ship. **Hypothesis** for
non-SWE plots. Links: `mental-models.md` §SDT; evaluator script for
threshold/cost sweep.

## 8. Control structure → sensor ≠ constraint (Leveson)

**Method**: STAMP / STPA — safety is a control problem, not a
component-accuracy problem
([Leveson STAMP intro](https://psas.scripts.mit.edu/home/wp-content/uploads/2016/04/STAMP-Intro-2016.pdf)).
**Transfers**: judgment as a *sensor* in a loop you own; constraints in
code, policy, checklist, two-person rule, physical interlock. STPA asks
what happens when the sensor is wrong, delayed, spoofed, or TOCTOU.
**Does not transfer**: a 99% Noul as the safety constraint; "the model
was confident" as the excuse for an unsafe control action; deleting the
interlock because ECE looked excellent in-distribution.

```text
constraint  = "do not give the drug without the allergy list"   # policy
sensor      = Noul("does this note mention an allergy?")        # model
actuator    = the person, the agent, the pump                   # not the model
STPA        = table of unsafe control actions if the sensor lies
```

**Example (Empirical as instrumentation shape):** OpenSmoke — cheap
judgment over every step so humans only autopsy flags. That is NATM
instrumentation of the control structure, not a safety case.
**Beyond SWE (Hypothesis):** hospital allergy list vs note-mentions-allergy;
kitchen thermometer vs "looks done"; two-person wire rule vs "this
invoice looks right"; incident command head-count vs "still contained?"
**Counterexample**: the agent proceeds because Noul 0.99. **Test**: name
the constraint that remains when the sensor is deleted; fill the unsafe-
control-action table. Ownership split is **Contract** as a rule
(`formal-methods.md`); the domain examples are **Hypothesis** until
labeled. Links: `mental-models.md` §Leveson; `boundary-audit.md` TOCTOU.

## 9. Search / control loops → one substituted classifier step

**Method**: beam, A*, MCTS, hiring funnel, literature snowball, sales
stages, cook/rest/check. **Transfers**: the *algorithm* stays yours. The
judgment-shaped hole is a prior, a prune, a leaf value, or a "does this
branch still look live?" Noul (`methods-catalog.md` search rows;
mapping §5 is the taxonomy-beam special case). Economics inversion:
per-node judgments were known and too expensive; they are now default.
Control: hysteresis, continue / stop / retry / verify — the model
estimates named probabilities; the controller is a table with memory.
**Does not transfer**: Jev as the planner that picks its next tool in a
loop; bandits without observed rewards; speculative depth without a
simulator; PufferLib Ocean scores as a capability claim
(`formal-methods.md` DST trio).

```text
loop     = yours (beam / funnel / stages / MCTS / incident command)
hole     = prior | prune | leaf | "still live?"
probe    = simulator / thermometer / CRM amount / exit code
estimate ≠ measure — irreversible milestones concede only to the probe
```

**Example (Empirical):** jev-mcts grounded vs speculative fidelity in
types; probes-only concession (mapping §5). **Beyond SWE (Hypothesis):**
snowball citations ("still on-question?"); sales stages ("still a real
opp?" — amount and close date stay exact); cook/rest/check ("looks done?"
— thermometer is the probe). **Counterexample**: a weekly LLM summary of
"how the project feels" instead of per-item instrumentation (the rejected
opposite of NATM). **Test**: greedy vs looped baseline on realistic cases;
inspect pruning failures; the probe, not the estimate, concedes. Links:
`mental-models.md` §search; `formal-methods.md` PufferLib row.

**Game loops as a calibration substrate (Empirical as a *shape*):**
[`vtrivedy/jev-plays-games`](https://github.com/vtrivedy/jev-plays-games)
— legal moves from code, one Choice over that set, text state, no
screenshot. Choice probabilities are **not** win odds. Author probe (12
calls, both option orders): both chess mates found; Connect Four
immediate win missed once reversed; Fool's-mate confidence 31%/37% so a
0.50 gate would reject correct mates. pcdServer Tetris is the same
hole on the constrained-AR surface. Not a strength rating.
`notes.md` §42; `validation.md`.

## 10. Spec property pipeline (Hypothesis)

**Method**: NL/ADR → candidate properties → human strengthens →
MC/ITP/DST → CEX triage → repair. **Transfers**: Choice/Score to *rank*
which candidate props to spend checker budget on; Noul/Choice to
cluster CEXs after the tool ran. **Does not transfer**: ranking ≠
validity. An LLM-written TLA+/Alloy sketch plus a Noul "looks good" is
double theater (`formal-methods.md` §5).

```text
candidates = LLM or human drafts from NL/ADR     # generation or a person
rank       = Choice/Score over the candidate set  # judgment
strengthen = human                                # exact values
check      = TLC / Apalache / Alloy Analyzer / DST / Dafny
triage     = cluster+severity of CEXs             # judgment, evidence only
```

**Example (Hypothesis):** Lamport-Agent drafts TLA+ from a codebase; a
human validates; the checker is source of truth in-model. **Counterexample:**
Hillel tautology (`canImport = P ∨ Q` then "prove" the definition).
**Test:** a property that fails on a planted concurrency bug; ranking
must not mark the tautology as "strong." Status: **Hypothesis**.
Links: `formal-methods.md` Alloy composition table; Amazon TLA+ PDF.

## 11. Alloy instance loop (Hypothesis)

**Method**: `run`/`check` → instances/CEXs → cluster+severity → edit
spec or scope → re-analyze. **Transfers**: post-judge and comparator
positions around the Analyzer. **Does not:** a Noul closing the check;
scope-blind "verified."

```text
Analyzer finds instances | CEXs in this scope
Jev clusters / scores novelty and severity
code or human edits the spec, the scope, or the scenario library
re-run — Analyzer is source of truth for the bounded claim
```

**Boundary:** Analyzer owns in-scope truth. **Test:** planted CEX is
not dropped by the triage Noul. **Hypothesis.** Links:
`formal-methods.md` §2.

## 12. Runtime assurance sandwich (Hypothesis)

**Method**: conformal / System One abstain → symbolic monitor / RV →
act. Curriculum names GUARDIAN / TemporalGuard / Perceive-with-Confidence
as *shapes*, not recipes. **Transfers:** judgment as the statistical
layer *around* a monitor. **Does not:** conformal sets as a proof of
the protocol; skipping exchangeability assumptions.

```text
estimate  = Noul / Score / conformal set     # statistical safety around learning
monitor   = RV / ptLTL / named invariant     # exact, compiled
act       = code, only if monitor admits
```

**Counterexample:** "the model was confident" as the monitor.
**Test:** inject a monitor-violating trace the Noul would have admitted;
the sandwich must refuse. **Hypothesis.** Links: `mental-models.md`
conformal; `formal-methods.md` help list.

## 13. DST multiverse triage (Hypothesis)

**Method**: Antithesis / Resonate DST artifacts → failure taxonomy →
patch → regress under the **same seed/timeline**. **Transfers:**
cluster failing timelines; Choice over root-cause hypotheses *after*
replay artifacts exist. **Does not:** guided-exploration coverage as
proof; Noul instead of an assert in-harness.

```text
harness states properties; DST searches; seed reproduces
judgment clusters novelty / suspected component
patch; re-run the same seed
```

**Test:** two failing timelines that share a symptom collapse to one
cluster; a distinct bug does not. **Hypothesis.** Links:
`formal-methods.md` §4.

## 14. Durable agent control (Hypothesis)

**Method**: Resonate HQ checkpoints own durability; Jev-class owns
semantic gates *inside* a step; the protocol oracle owns correctness of
promise state. **Transfers:** Choice/Score for human-in-the-loop resume
priority; Noul gates inside `ctx.run`. **Does not:** "agent-native" as
"judgment replaces Lean/oracle"; a done-Noul settling a promise.

```text
Resonate  = crash-resume, promise settlement     # protocol
Jev-class = semantic gate / route inside a step  # estimate
oracle    = differential disagreement            # probe
```

**Counterexample:** `if noul(done) > τ: complete_workflow()`.
**Test:** kill the process mid-step; the promise is still protocol-true
without consulting the Noul. **Hypothesis.** Links:
`formal-methods.md` Resonate row.

## 15. Assignment hybrid — soft affinity + hard solver (Hypothesis)

**Method**: operations-research assignment / scheduling. **Transfers:**
Score affinity or risk as a *cost feature*; ILP/heuristic owns
capacity, legality, fairness. **Does not:** replacing a VRP/assignment
solver with a Choice; soft costs violating a hard constraint.

```text
affinity = Score/Noul per pair (reviewer↔paper, agent↔incident)
solver   = code (capacity, skills, hours, law)
policy   = starvation/fairness rules in code
```

**Example (Hypothesis):** incident-commander assignment; grant-panel
paper allocation; GPU scheduling. **Counterexample:** Choice over
assignees that ignores load. **Test:** a feasible assignment the solver
finds that the Score alone would skip because it "felt" worse; hard
constraints never yield. Links: `mental-models.md` §OR.

## 16. Situated density (Shirky) (Hypothesis)

**Method**: [Situated software](https://gwern.net/doc/technology/2004-03-30-shirky-situatedsoftware.html)
— form-fit to a named group; refuse false scale. **Transfers:** dense
full-traffic judgment *inside* a named community (one team, one
product, one agent). Local Choice sets, local τ. **Does not:**
copying those thresholds to another population (calibre:
thresholds don't transfer); enterprise ArchiMate theater for N=30.

```text
community boundary named (team / product / practice)
aggressive soft loops allowed only inside it
outside: retrieval, law, public metrics, FM where wrongness is intolerable
```

**Test:** the same τ on a second population; if cost/coverage moves,
the card was situated and must stay labeled. **Hypothesis.** Links:
`formal-methods.md` Shirky; `mental-models.md` harm "scale mismatch."

## 17. Input brittleness → sensitivity, calibration, selective abstention (Hypothesis)

**Method**: Chow reject-option / selective classification plus a
*stability* test. The model is a noisy sensor; question wording is part
of the stimulus. **Transfers**: semantically equivalent paraphrases that
swing p are a reason to **abstain** or to fix the question, not a reason
to ship the first number. Behavioral evals must include paraphrase pairs
(`validation.md`). **Does not transfer**: a single p as invariant to
wording; "the model is calibrated" as a license to skip sensitivity;
treating jitter as a vendor defect you can ignore (it is a *design*
constraint — [@brandonjcarl, 2026-09-18](https://x.com/brandonjcarl/status/2100976725660192989));
copying the ≤0.18 below as a jitter constant — that is jevgate's
measurement on jevgate's command set, a universal jitter bound stays
Hypothesis (`composition-algebra.md` open positions), and the number you
owe is your own observed spread.

```text
ask φ and paraphrase(φ) on the same state
if |p − p′| large → abstain / rewrite the question / raise t
threshold width ≥ observed jitter (jevgate: identical requests differ ≤0.18;
  a comment moved git checkout -- . from 0.91 → 0.37)
```

**Example (Empirical as published cautions, not a constant):** identity
match Noul ("Is this the same person as X?" vs "Same person as X?");
jevgate comment-injection. **Beyond SWE (Hypothesis):** "is this the
same invoice?" vs "same invoice?"; "does this look done?" vs "done?";
hiring "same candidate as the referral?" **Counterexample**: averaging
ten paraphrases and calling the mean Contract. **Test**: a labeled
paraphrase set where the *act* must not change when the wording is
synonymous; if it does, abstain. Until that set exists on *your*
questions, **Hypothesis**. Links: `mental-models.md` §thresholds;
`question-design.md` diagnosis; `validation.md` behavioral tests.

## 18. Structural prove ∩ soft remainder (Hypothesis as domain-general; Empirical as named shapes)

**Method**: code (or a recipe, a law, a text layer) **proves** the easy
cases; a System One model judges only what the structure cannot decide.
Composition-algebra position 3 *after* a constraint, not instead of one.
**Transfers**: allowlist / refused-in-code / unknown→judge
([jevgate](https://github.com/thevibeworks/jevgate): Proven / Refused /
Unknown; cannot block; Jev alone leaks). Same sandwich as page OCR
([doc-router](https://github.com/misbahsy/doc-router): pdf-inspector
first, "needs OCR?" Noul on the remainder — 155→87 pages billed, **1.74×**
$ on 19 docs / 155 pages). **Does not:** putting the model first so a
comment or a watermark talks it into a write; treating 0 unsafe-unasked
on 59 held-out rows as a sandbox; copying 0.2 or 1.74×.

```text
if structure proves safe     → allow (no model)
if structure proves unsafe   → refuse / ask (no model)
else                         → typed questions on the remainder
fail open unless a real sandbox/interlock sits underneath
```

**Example (Empirical as shapes):** jevgate 249 labelled, worst-of-three,
held-out unsafe unasked 0/59, safe-unasked 30/35 vs allowlist 15/35;
doc-router 9 OCR-misses vs 28 for rules-only.
[`poponline63/hermes-jev-north-star`](https://github.com/poponline63/hermes-jev-north-star):
deterministic shell checks first; empty evidence refuses to judge; then
one Jev call on the remainder. Empty state was self-contradictory —
that is why the refuse-empty rule exists. **Beyond SWE (Hypothesis):**
recipe book ∩ "does this leftover look done?"; labor-law allowlist ∩
hiring-fit Noul; SPF/DKIM pass ∩ phishing Noul on the body. **Counterexample:**
Jev on `/bin/ls` as the first tier. **Test:** planted writers never
reach the model; planted remainder cases *do*; removing the model must
not admit anything the allowlist forbade. Domain examples stay
**Hypothesis** until labeled. Links: `formal-methods.md` sensor≠constraint;
`mental-models.md` §Leveson; composition-algebra gate after a constraint.

## 19. Effect-oriented state-machine loops (Hypothesis)

**Method**: decision circuits / FSMs (§3) inside an effect system.
Soft predicate on the transition; **code owns the transition** and
whatever effect it runs. Extends dual orchestration topology B
(`mixed-architecture.md`): the decision model answers the edge; a
generator, if any, is a callee; the host still executes.

**Transfers**: each turn the host mints the finite set of actions legal
in *this* state. One Choice asks which of these advances the state, or
a Noul asks a fuzzy edge the rules cannot name ("does this look
finished?"). The handler runs the effect (MCP, store, no-tool writing)
and returns continue-with-new-state or done. Only a compact view and
the option descriptions cross to the model; the action value stays
typed in the host. Unknown ids fail closed before the effect. Exact
edges (inventory, chronology, a hard iteration cap) never leave the
host.

**Does not transfer**: reading the tweet title "Effect Oriented" as the
TypeScript Effect library, or as a tutorial in either system. The image
is a ZIO loop in
[jamesward/zio-typesafe-ai](https://github.com/jamesward/zio-typesafe-ai)
(Ward's *Effect Oriented Programming* is Scala/ZIO). That client's
combinator is not the Jev HTTP contract and not an Augustus API. The
model does not invent the next state or the side effect. An id outside
the offered set is a protocol violation, not a branch. A Noul or an
encoder score is not a discharged invariant. Do not multiply edge
predicates into a joint probability. Handler time and a generative
callee's tokens are not model cost. The 1–255 option cap is Jev's, not
the class's.

```text
options(state) → finite legal actions the host minted
Choice / Noul  → which action, or is this fuzzy edge true?
handler        → effect, then continue(next) | done
unknown id     → fail closed; do not run the effect
exact edge     → host only; the model is not called
```

**Example (illustration, not a recipe):** the posted counter, where
"increment" continues and "finish" returns the state
([James Ward, 2026-09-18](https://x.com/JamesWard/status/2100981305009664299)).
Load-bearing sentence on the image: an action handler may run arbitrary
ZIO effects — MCP calls, database operations, or a no-tool generative
model call — while Jev remains the outer decision loop. **Beyond that
client (Hypothesis):** clinic intake — Choice picks the next question,
the chart write is the effect; hiring — advance / hold / stop is the
Choice, the letter is written inside the handler; a kitchen — "is this
step done?" is the predicate, the timer and the knife stay in the
recipe. **Counterexample:** free-text "what state next?", or a
generator emitting a tool name it might hallucinate. **Test:** a
planted illegal action is never offered; a planted unknown id does not
run; a deterministic edge never calls the model; a handler failure
still leaves that turn's distribution in the log. Until that labeled
trace exists, **Hypothesis**. Links: §3; `mixed-architecture.md` dual
orchestration; `notes.md` §28.
