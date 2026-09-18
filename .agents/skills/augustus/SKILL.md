---
name: augustus
description: "Use when placing typed probabilistic judgment (Jev-class System One / decision models) with mathematical, logical, or algorithmic mental models — in AI, software, business, knowledge work, or life, not only SWE; deciding where a fast cheap categorization/classification/scoring model belongs versus generation, exact policy/code, or proof; applying expected utility, selective classification/abstention, calibration, cost-sensitive thresholds, value of information, MCDA, signal detection, search/control substitutions, or Leveson-style org/safety; using NATM/snap-fit/Norman as design intuition; designing mixed architecture (decision model + LLM writing); auditing an existing system, PR, workflow, or non-software practice for judgment-shaped holes and code smells; debugging a question that hovers near 0.5, clusters mid-scale, or hides two judgments; placing agent self-supervision gates (pre-action, output judge, done-check, stuck-detector, context sieve); coupling a typed judge as an optimizer metric (Ax, DSPy); choosing among TypeSafe Jev, open heads (Laya, kev, openjev-lm, Nimble, encoder DeBERTa, LoRA distill), announced open decision-model (Watch), constrained-AR (TypeAR, pcdServer), diffusion structured reads, GLiNER/GLiClass/GLiGuard encoder family (locate vs categorize vs safety-schema classify vs local multi-head), listwise rankers, or vision scorers; placing judgment beside TLA+/Alloy/Apalache/Dafny/DST (Antithesis, Resonate, PufferLib) without laundering a Noul as a proof; answering \"it's just classification\", \"is Jev probabilistic programming\" (marginals vs joint, not a PPL), \"low/medium/high entropy\" (allocator, not a meter), \"perception specialist then judgment vs shared multimodal System One\", \"eval path\", \"jevals\", \"Harbor taskset\", \"pipeline / measure / hill-climb perception into a decision\", \"Ax vs DSPy\", \"held-out\", \"correctness is not confidence\", \"is this only for software?\", Alloy vs Apalache, GLiNER vs Jev, \"is GLiGuard Jev?\", LLM-as-judge, paraphrase brittleness, allowlist then judge, TOCTOU-of-Noul, vacuous specs, open weights vs constrained decoding vs encoder vs LoRA vs kev, whether a decision needs a model at all (meta-VOI), env-break vs policy-break, sqlite-jev / in-engine vs CLI store index, hard safety envelope (Jev proposes, code clamps), host-adapter routing (not MCP), distill-to-device memory gate, or \"formally verify with Jev\" with a placement, not a stack replacement or a vendor how-to. Formal methods are one pillar. Not a substitute for the official typesafe-ai skill (live Jev API contracts)."
license: MIT
metadata:
  version: 0.3.0
  typesafe_skill: v0.5.7
  typesafe_skill_commit: 65a39f3
  tribute: "Named for Augustus De Morgan (1806-1871), mentor of William Stanley Jevons."
---

# Augustus

Design-judgment skill for **placing typed probabilistic judgment** (the
Jev-class of System One / decision models) using mathematical, logical, and
algorithmic mental models — across **AI, software, business, knowledge
work, and life**. Not limited to software engineering. Formal methods
are one pillar (`references/formal-methods.md`); the portable frames
are `references/mental-models.md`.

TypeSafe Jev is the documented **exemplar** (typed Choice / Score /
Noul), not the monopoly. This skill owns **where judgment belongs**;
the official `typesafe-ai` skill plus the live docs own Jev integration
contracts — read them before writing Jev API code. Neighbor skills
`tenbin` (lint/measure) and `decision-first` (try-Jev-first habit) own
their jobs. Do not collapse into a TypeSafe how-to, a Laya install, a kev
serve, or a GLiClass or GLiNER tutorial.

Pick the **pillar** from the hole (expected utility, VOI, MCDA, signal
detection, search/control, org/safety, formal methods), then the
**family** (`references/judgment-class.md`), then the vendor. Default
placement is **mixed architecture**: exact work in code/policy, narrow
judgment on a System One–class model, generation only where something
must be written.

Central model: **evidence → semantic judgments → explicit policy → checked
action → observed outcome.** Every design must name what the judgment
model estimates, what remains exact, what (if anything) is still
generated, and what experiment could prove the idea wrong.

For genuinely new problem shapes, use the toolbox sweep
(`references/toolbox-mapping.md`): find the judgment-shaped component of a
classical method you already trust, substitute it, classify the win
(marginal / newly-feasible / invalid), and falsify.

## Protocol

1. If the request is "replace the LLM/stack with Jev", "isn't this just
   classification?", "is Jev probabilistic programming?" (marginals vs
   joint — not a PPL), "low vs high entropy / frontier model for
   this?", "is Jev the only model?", "is this only for
   software?", "formally verify with Jev / replace TLA+ / Dafny /
   DST", "Alloy vs Apalache", "GLiNER vs Jev", "LLM-as-judge",
   "paraphrase brittleness", "allowlist then judge", "TOCTOU-of-Noul",
   "Jev inside the database / sqlite-jev", or "Jev picks bitrate / join
   order / the model":
   read `references/faq.md`,
   then `references/mental-models.md`, then
   `references/mixed-architecture.md`, then
   `references/judgment-class.md` before any mapping. Proof,
   model-checking, contracts, DST, and judgment-vs-proof ownership: also
   read `references/formal-methods.md` (Alloy vs Apalache; DST trio
   Antithesis / Resonate HQ / PufferLib; TOCTOU-of-Noul). One-screen
   alias: `references/formal-semi-formal.md`. Answer with a **placement**
   (sieve / keep-drop / triage / rank / route / gate / perceive /
   abstain / gather / replace-one-classifier-step) and a **pillar +
   family**, not a rewrite, a vendor tutorial, or a Noul-as-proof. If it
   is an existing system, PR, workflow, or practice: also run the
   boundary audit (`references/boundary-audit.md`). Classify each step
   as exact / bounded judgment / generation; recommend the smallest
   insertion, not a redesign. Greenfield with no replacement framing:
   start at step 2.
2. Start from the desired behavior: what the software, person, or
   organization shows, selects, changes, or hands off. Work backward to
   the judgments it needs. Name the domain and the pillar
   (`references/mental-models.md`), then pick the family whose
   *objective* matches the action's fail policy
   (`references/judgment-class.md`). Do not start from a logo.
3. Keep exact work in code, policy, checklists, ledgers, law, and
   recipes: arithmetic, counting, dates, lookups, authorization, safety
   interlocks, control flow, side effects, money. Keep open-ended
   writing, explanation, and code generation on a generative model or a
   person; a judgment-class model may gate, route, or verify around that
   call. Proof, model-checking, contracts, and DST stay with their
   tools — a Noul is a sensor, not a discharged proof obligation
   (`references/formal-methods.md`).
4. Give the provider one narrow judgment per question (a knowledgeable
   person could answer in a second given the state). Split multi-factor
   judgments; fuse in code with visible weights. Jev's option/envelope
   limits are Jev's, not the class's — large or changing label sets may
   prefer a GLiClass one-pass (categorize). GLiNER (locate) substitutes
   only where the answer *is* a span in the text
   (`judgment-class.md` species map).
5. Exploit the family's cheap fan-out: batch independent questions in
   one request when the provider supports it; encode text + all labels
   once for GLi\* heads; score many prompts against one
   embedding for dual-encoder vision. Sequence a second call only when
   its state or options depend on an earlier answer.
6. Route on uncertainty with per-action thresholds tuned on your own
   data. Ranking scores **order** (fail open); decision scores
   **authorize** (fail closed). Do not threshold a listwise or affinity
   number as if it were P(permit). The same judgment can authorize a
   reversible path and must not authorize an irreversible one.
7. Ship a decision-design card (below) and the smallest falsifying
   experiment. Name the eval path. A card without one is incomplete
   (`references/validation.md#eval--hill-climb`). Record family, model,
   rubric, candidate-source, and policy versions. Keep questions,
   criteria, and thresholds in one reviewable module; store raw
   judgments separately from derived actions.

## Mapping index

| Familiar method | Judgment shape | Detail |
|---|---|---|
| Mental models across domains (not SWE-only) | EU, abstention, VOI, MCDA, SDT, search/control, Leveson, NATM/Norman/snap-fit | `references/mental-models.md` |
| Judgment-model class (Jev is exemplar, not monopoly) | Species: decide / locate (GLiNER) / categorize (GLiClass) / rank / perceive; open heads include encoder DeBERTa, LoRA distill, openjev-lm, kev | `references/judgment-class.md` |
| Open weights vs constrained decoding vs proprietary API | Three open paths: encoder open-jev / AR constrained decode (TypeAR + pcdServer) / trained decision-only (Laya, Nimble, kev, Archer Watch). Softmax over allowed tokens ≠ Noul | `references/judgment-class.md` (when-to-use table) |
| Entropy as allocator (low / medium / high) | Typed low+medium decisions → System One marginals; high-entropy synthesis → frontier decoder. Product rhetoric, not a meter. **Hypothesis** | `references/judgment-class.md` |
| Formal / semi-formal (proof vs judgment) | Sensor vs constraint vs searchlight; Alloy vs Apalache; DST trio; TOCTOU-of-Noul, AI×FM | `references/formal-methods.md` (one-screen: `references/formal-semi-formal.md`) |
| Mixed architecture (judgment model + LLM) | Provider judges, LLM writes, code owns control; not a stack replacement | `references/mixed-architecture.md` |
| Context sieve | Relevance Noul per block; always-keep set in code; stub + recall key | `references/applied-mappings.md#1-context-sieve` |
| Exact-text keep / drop | Choice include/exclude/mixed over candidates code already holds | `references/applied-mappings.md#2-exact-text-keep--drop` |
| Environment / harness triage | Scan every step for env failure; LLM autopsy only on flags | `references/applied-mappings.md#3-environment--harness-triage` |
| Moderation and ranking | Hold-before-publish vs graded rerank; fail policy per action | `references/applied-mappings.md#4-moderation-and-ranking` |
| Skill / tool routing | Choice over a closed catalog + whether-anything-fits; code dispatches | `references/applied-mappings.md#5-skill--tool-routing` |
| Expensive observation router | Structural prove (text layer) ∩ remainder Noul (needs OCR?) | `references/applied-mappings.md#6-expensive-observation-router` |
| Agent preference lint / semantic gates | Project-defined rules as criteria; provider classifies evidence; code maps outcome | `references/mixed-architecture.md#preference-lint-and-gates` |
| Dual orchestration (Jev ∩ LLM ∩ MCP) | Jev-as-tool vs Jev-as-outer-loop; schemas are exact state | `references/mixed-architecture.md#dual-orchestration-jev--llm--mcp` |
| "It's just classification" / "not probabilistic programming" / stack-replacement FAQ | Typed judgment is a software primitive, not a new task; marginals are not a joint; Jev is not the only model | `references/faq.md` |
| Feature engineering / multi-criteria analysis | Nouls + Score distributions as named features, weights in code | `references/mappings.md#1-semantic-judgments--features-and-explicit-utility` |
| Selective classification / decision theory | Thresholds from action costs, abstention paths | `references/mappings.md#2-probabilistic-judgments--cost-sensitive-decisions` |
| Decision tables / circuits / state machines | Judgment predicates, code owns transitions | `references/mappings.md#3-semantic-predicates--decision-circuits` |
| Retrieve + expensive relevance fn | Bounded rerank of a retrieved shortlist | `references/mappings.md#4-retrieval--bounded-semantic-reranking` (independent TREC DL2019 benchmark: Jev zero-shot best MAP 0.4748, nDCG@10 0.683 vs tuned monoBERT 0.718 — competitive, not dominant) |
| Store as semantic index (SQL / SQLite / zoxide) | Cheap exact predicates first; typed questions on the remainder. In-engine extension (sqlite-jev) vs CLI rewrite (jevql) vs path index (joxide) | `references/mappings.md#4-retrieval--bounded-semantic-reranking` |
| Soft judgment inside a hard envelope | Model may only match the deterministic policy or be more conservative (bitrate ABR; query-planner override-when-confident) | `references/mappings.md#12-runtime-assurance-sandwich-hypothesis`; `references/mappings.md#18-structural-prove--soft-remainder-hypothesis-as-domain-general-empirical-as-named-shapes` |
| Value of information / gather as an act | Pay for another observation only if EV(decision) improves more than cost; abstain from calling *any* model when a regex already answers (meta-VOI) | `references/mappings.md#6-value-of-information--gather-as-an-enumerated-act` (**Hypothesis** until a labeled act/outcome log; 149-row receipt is Empirical as a shape) |
| Signal detection / ROC | Criterion and operating point from costs and base rate, not accuracy | `references/mappings.md#7-signal-detection--criterion-not-accuracy` (**Hypothesis** for non-SWE plots) |
| Org / safety control structure | Sensor ≠ constraint (Leveson); STPA if the sensor lies | `references/mappings.md#8-control-structure--sensor--constraint-leveson` |
| Search / control loops (any domain) | Algorithm stays yours; judgment substitutes one classifier step | `references/mappings.md#9-search--control-loops--one-substituted-classifier-step` |
| Spec property pipeline | Rank candidate props; checker owns validity | `references/mappings.md#10-spec-property-pipeline-hypothesis` (**Hypothesis**) |
| Alloy instance loop | Cluster CEXs; Analyzer owns in-scope truth | `references/mappings.md#11-alloy-instance-loop-hypothesis` (**Hypothesis**) |
| Runtime assurance sandwich | Abstain → RV/monitor → act | `references/mappings.md#12-runtime-assurance-sandwich-hypothesis` (**Hypothesis**) |
| DST multiverse triage | Cluster failing seeds/timelines; regress on the same seed | `references/mappings.md#13-dst-multiverse-triage-hypothesis` (**Hypothesis**) |
| Durable agent control | Resonate protocol settles promises; Jev gates inside a step | `references/mappings.md#14-durable-agent-control-hypothesis` (**Hypothesis**) |
| Assignment hybrid | Soft affinity + hard solver | `references/mappings.md#15-assignment-hybrid--soft-affinity--hard-solver-hypothesis` (**Hypothesis**) |
| Situated density (Shirky) | Aggressive soft loops only inside a named community | `references/mappings.md#16-situated-density-shirky-hypothesis` (**Hypothesis**) |
| Input brittleness / paraphrase stability | Synonymous wording that swings p → abstain or rewrite | `references/mappings.md#17-input-brittleness--sensitivity-calibration-selective-abstention-hypothesis` (**Hypothesis**) |
| Structural prove ∩ soft remainder | Allowlist/text-layer/law first; judge only leftovers | `references/mappings.md#18-structural-prove--soft-remainder-hypothesis-as-domain-general-empirical-as-named-shapes` (**Hypothesis**; jevgate/OCR shapes Empirical) |
| Effect-oriented state-machine loops | Soft predicates on transitions; code owns the transition | `references/mappings.md#19-effect-oriented-state-machine-loops-hypothesis` (**Hypothesis**; ZIO client, not Effect.ts) |
| Agent self-supervision / on-track detection | Pre-gate → output judge → done-check → supervisor nouls | `references/agent-self-assessment.md` |
| Optimizer/program frameworks (Ax, DSPy) | Typed fields → one provider request; judge metrics; threshold discipline. Ax and DSPy climb LM-program knobs only | `references/optimizer-integration.md` |
| Perception → decision pipeline / measure / hill-climb | Stages with a versioned state contract; frozen taskset; DSPy/Ax only on the LM-program slice. **Hypothesis**. Same section as the row below | `references/validation.md#eval--hill-climb` |
| Eval & hill-climb | Decision-stage jevals hygiene; Harbor taskset × harness × runtime; one score-composition table | `references/validation.md#eval--hill-climb` |
| (meta) Finding new mappings & applications | Toolbox sweep: judgment-shaped component of a known method, substituted + falsified | `references/toolbox-mapping.md` |
| Named methods / operators / theorems | Substitution tiers: operand-judgments, preconditioned theorems, non-substitutable | `references/methods-catalog.md` |
| (meta) Where a judgment model sits relative to any construct | 11 positions + logical-operator rules + position×construct traversal as the application generator | `references/composition-algebra.md` |
| Question mechanics & debugging | Instruction/criteria/state shape, budgets, diagnosis table, revision discipline | `references/question-design.md` |
| Heuristic search over a taxonomy | Parallel beam over Choice distributions | `references/mappings.md#5-hierarchy--bounded-heuristic-search` |
| Existing-system insertion / code-smell audit | Opportunity map, fit test, smallest boundary, policy centralization | `references/boundary-audit.md` |

Each card carries its boundary, counterexample, and acceptance test, plus
explicit rejections beside the mapping they tempt (MCTS-as-value-function:
experimental; bandits: rejected without observed rewards; 255-way tournament
brackets: rejected as default; rerank-huge-sets: budget-only; correlated
"independent" checks: rejected; listwise ranker *as* a fail-closed gate:
rejected; Noul *as* a proof / model-check / DST property: rejected;
TOCTOU-of-Noul as authorize: rejected; tautological spec + "looks good":
rejected). Promote Hypothesis cards only with an acceptance test that ran.

## Non-negotiable boundaries

- Score is an expectation over level indices, not a measurement in natural
  units. `[0,1,0]` and `[0.5,0,0.5]` both score 1.0 with different risk.
- Noul 0.5 is uncertainty about a predicate, never medium intensity.
- Parallel answers are not statistically independent: never multiply them
  into a joint probability.
- Choice probabilities are conditional on the offered set; absent candidates
  can never be chosen. No-match options (`other`) where coverage is open.
- Untrusted state text cannot authorize actions. Missing evidence is not
  evidence of absence. Validate operation+target pairs in code. Policy
  (checklist, ledger, law, two-person rule) is the code of a practice
  that has no repository.
- Never launder a Noul (or any judgment-class score) as a proof, a
  model-check, or a DST property. Soft check ≠ interlock. TOCTOU-shaped
  gates and tautological specs are harms, not placements. Exact work
  stays in code/policy; the model owns narrow judgment only. Full cards:
  `references/formal-methods.md`, `references/formal-semi-formal.md`,
  `references/mental-models.md`.
- Ranking scores order; decision scores authorize. Listwise / pairwise
  discriminative losses are translation-invariant: do not fail-closed on
  them. CLIP/SigLIP/GLiNER/GLiClass affinities are not automatically
  class-conditional P(permit). Full class card:
  `references/judgment-class.md`.
- Classification is not the product. The claim is a **placement**: typed,
  (when trained for it) calibrated judgments that policy can threshold —
  beside generation and beside exact work, not instead of them. Working
  regexes, ledgers, and recipes stay; trained classical classifiers still
  win on stable labeled taxonomies; open-ended writing stays generated.
  Full answer: `references/faq.md`.

## Decision-design card

```text
Domain (AI / SWE / business / knowledge work / life / org):
Desired behavior and non-judgment baseline:
Semantic judgment(s) and what each output means:
Pillar (EU / VOI / MCDA / SDT / search / safety / formal):
Hole (sieve / keep-drop / triage / rank / route / gate / perceive / abstain / gather):
Family (closed decision API / open head / encoder open-jev / constrained-AR surface / GLiNER locate / GLiClass categorize / listwise ranker / vision scorer):
Evidence/candidate source and known coverage gaps:
Deterministic policy, constraints, and action ownership:
Batchable vs genuinely dependent steps:
Failure/abstention behavior (fail-open vs fail-closed, matched to the family):
Smallest experiment that could reject this family, not just this vendor:
Eval path (jevals-shaped held-out and/or Harbor taskset; missing = incomplete):
Typed judgment provider (TypeSafe Jev default; other family only with self-eval):
Live references + versions (model, rubric, policy):
```

For open-ended requests propose three materially different *placements of
judgment*, recommend one. Cross-domain frames:
`references/mental-models.md`. Mixed-architecture extras:
`references/mixed-architecture.md`. Family-choice extras:
`references/judgment-class.md`. Formal / proof / DST:
`references/formal-methods.md`. Applied SWE placements (sieve, keep/drop,
env triage, moderation/ranking, skill routing):
`references/applied-mappings.md`. Hypothesis cards (VOI, SDT, Leveson,
search/control, spec pipeline, Alloy loop, RV sandwich, DST triage,
durable agents, assignment, situated density, paraphrase stability,
structural-prove ∩ remainder, effect-oriented state-machine loops)
stay labeled until an acceptance test
runs: `references/mappings.md` §6–§19. For concrete
requests skip the brainstorm and build.

## Evidence labels

- **Contract**: current documented behavior — refresh from live docs.
- **Empirical recipe**: worked on a stated dataset/model/version — retest.
- **Hypothesis**: plausible, unestablished — label and test before relying.
