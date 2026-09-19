# Composition algebra: where a judgment-class model sits relative to any method, operator, or algorithm

The catalog substitutes a judgment-class model *into* constructs (Jev is
the notation because it is the documented exemplar). This card enumerates
the **positions** a typed judgment can occupy relative to any
function/operator/algorithm F — the full grammar of "judgment as X". Same
rule as everywhere else: the position determines what the judgment may be
trusted for, and each carries its governing caveat. Family choice (decision
API vs listwise ranker vs vision scorer) is `judgment-class.md` — a listwise
number in a verifier position is the rejected design. Statuses per
mappings.md conventions.

## The positions

| # | Position | Form | Launch-week example | Governing rule | Status |
|---|---|---|---|---|---|
| 1 | **Operand** | F(Jev(...)) — judgment's number feeds the function | Nouls as CatBoost features; Score as PUCT leaf value | It's a calibrated belief in your rubric's units, not a natural quantity; version feature/question defs with the consumer | **Empirical recipe** |
| 2 | **Post-judge** | F(x) → Jev judges the result | Output judge (leaks_secret, failure_class); citation check on generated text | Only the post-judge sees what the call printed; the pre-gate cannot | **Empirical recipe** |
| 3 | **Gate** | if Jev(x): apply F — Jev decides *whether* F runs, or whether F's result is admitted | Pre-action gates (destructive .90/exfil .70); winnow context sieve; pi-heed side-effect check | A gate is a filter, not authorization — validate operation+target in code. Error paths fail **per action**, not always open: an advisory guard fails open *because* a hard interlock or sandbox sits underneath; a gate that selects or authorizes a side effect fails closed (`mixed-architecture.md` prefilter table; `mappings.md` §18) | **Empirical recipe** |
| 4 | **Selector (of F or its parameters)** | Jev picks which F runs: Choice over functions/models/effort levels | jev-router (cheapest model), jev-codex-router (model+effort), DiffJury review_depth, jeffrey next-tool | Dispatch stays in code; per-option consequences are your cost model; confidence-gate the selection. **Pick ≠ fill:** the LLM may write args; Jev does not | **Empirical recipe** |
| 5 | **Comparator** | Replace a semantic comparator inside sort/rank: "more relevant / more severe" as a key | Rerank; skillranker; order statistics over semantic keys | Comparability needs a shared rubric; measure recall separately from rerank quality | **Empirical recipe** |
| 6 | **Prior / initializer** | Jev distribution seeds a deterministic method that refines it | MCTS PUCT priors; beam-search branch priority | It's a heuristic prior, not a posterior; refine with real observations | **Empirical recipe** |
| 7 | **State estimator, F = controller** | Jev estimates named probabilities; deterministic policy with hysteresis acts | foreman (progress/stuck/complete → continue/stop/retry/verify) | The model never commands; interventions enumerated in code | **Empirical recipe** |
| 8 | **Metric / loss** | Jev as the judge inside an optimizer loop (GEPA, DSPy teleprompters) | Judge-variance recipe before trusting any optimizer metric | Optimizer metrics must be repeatable; Jev judge spread 224–279× lower than GPT judge — still verify on your data | **Empirical recipe** |
| 9 | **Verifier / constraint source** | Jev judges spec-conformance: property holds/violated/unverifiable | pi-warden (violated rule named back into context); citation checks | Verdicts are evidence, not enforcement; the checker enumerates requirements in code. A Noul does not discharge a proof obligation. TOCTOU-of-Noul is not a constraint (`formal-methods.md`) | **Empirical recipe** |
| 10 | **Discretizer / encoder** | Unstructured state → typed values downstream code requires (enum, level, boolean) | jev-browser element selection; pre-parsed value extraction | Jev selects from candidates you produce; it never generates | **Empirical recipe** |
| 11 | **Bounds / budget holder** | Jev decides how far to continue (early stop, keep-looking) | Early-stop noul ≥0.85 (mcts-agent); winnow hide threshold | Termination conditions stay conservative and code-owned | **Empirical recipe** |

## Logical operators over Jev outputs

- **¬**: `p(¬φ) = 1 − p(φ)` — valid, it's a probability. But ask the
  question in the form you'll branch on; double negatives in the *question
  text* cost accuracy (jaggedness).
- **∧ / ∨ over parallel nouls**: do NOT multiply — same-state answers are
  not independent. Either ask the compound question directly (one question,
  one distribution) or combine in code with an explicit, labeled policy.
- **∀ over a candidate set**: batch one Noul per item in ONE request
  (parallel, cheap), then aggregate in code (min = AND, max = ∃) with an
  explicit escalation rule — the quantifier's aggregation policy is code,
  never the model.
- **→ (implication) / chains**: decompose into gate → act → post-judge;
  never encode multi-hop logic in one question (indirection costs accuracy).
- **Named combinators** ([jev-combinators](https://github.com/voidning/jev-combinators);
  renamed from decision-combinators, same repo):
  Then / Gate / Vote / Cascade / Weighted plus **extended**
  Router / Loop / Retry / Fallback / Memory are
  **control-plane** wiring, not a license to treat parallel
  Nouls as independent. Digital-design slogan (transistors /
  logic gates / chip) is a *metaphor* for soft classifiers;
  ∧/∨ aggregation still follows the rule above. Fallback is
  the fail-closed node;   Memory gates what to remember. No
  measurements. `notes.md` §66, §69.
- **Decider ≠ executor** ([jeffrey](https://github.com/thomasbrueggemann/jeffrey)):
  position 4 (Selector of next F) stays Jev; arg fill is
  generation, not a Jev position. The loop is Jev→tool→Jev.
  Pick ≠ fill. Mapping §9 still rejects the fused
  planner-writer. `notes.md` §70.
- **Selector of the next word** ([jev-gpt](https://github.com/florian-hoenicke/jev-gpt)):
  position 4 applied to generation itself. Each token is a
  Choice over a closed lexicon; the model never
  free-generates. Architecture demo (~400 calls / 75 s /
  2¢ *theirs*). Distinct from jeffrey (selector of next
  *tool*). `notes.md` §71.
- **Hand no-text steps** ([jev-use](https://github.com/shitianfang/jev-use)):
  selector + gate; writing stays generation. Vercel drops
  confidence so margin is a different statistic.
  `notes.md` §71.
- **TLA+ kernel around votes** ([jev-labs](https://github.com/copyleftdev/jev-labs)):
  aggregation (quorum, stability, escalate) is the spec,
  not a multiplied joint of five Nouls. `notes.md` §67.

## Rules that hold across every position

1. **Width is cheap, depth is linear** — batch everything that shares a
   state; add a second call only when next options depend on an earlier
   answer. The composition grammar is where the dependency tree gets
   decided: positions 1, 3, 4, 10 fan out; positions 2, 5, 7 usually
   depend on an executed state and must wait.
2. **Estimate ≠ measure**: in every position, a Jev output is an estimate
   over the state as given. Anything irreversible concedes only to a
   post-execution probe (position 2), never to a Jev estimate in any other
   position. A Noul at t0 that authorizes an act at t1 is TOCTOU-of-Noul,
   not a discharged obligation.
3. **Calibration is positional**: thresholds are per-position and
   per-action (gate thresholds ≠ judge thresholds ≠ hide thresholds).
   Tune each on split A, report on split B.
4. **The oracle has no side effects.** Whatever the position, Jev never
   performs the action — F does. If removing Jev would change what the
   system is allowed to do, the design is wrong.

## The application generator (traversal, not brainstorming)

Novel applications come from crossing the two axes instead of free-
associating: **positions (1–11 above) × constructs (the toolbox/methods
catalog)**. Each cell asks one question — "what does it mean for F and a
Jev judgment to stand in THIS position?" — and the economics inversion
filters the results.

Traversal procedure:

1. **Pick a construct** whose math you actually know (a specific operator,
   theorem, algorithm, or a workflow step from a domain you know).
2. **Walk the positions** (1→11), asking for each: is there a judgment-
   shaped hole at this position? Most are trivially no; a few will light up.
3. **For each lit cell, apply the economics inversion**: was this step
   previously impossible because a judgment cost seconds and cents? If yes
   → newly-feasible candidate (high yield). If it replaces an LLM call or
   hand rule → marginal. If it violates a governing rule → record as
   rejected, move on.
4. **Name the caveat that governs the position** (from the table) and make
   it a code-level check. No nameable caveat = metaphor.
5. **Falsify**: labeled cases, split A/B, judge-variance if a judge is in
   the loop, behavioral perturbations. A candidate that survives becomes a
   row in the methods catalog with a status.

Why this generates rather than brainstorms: brainstorming samples the
("domain × idea") space through whatever the model associates; the
traversal enumerates the actual product space — ~11 positions per known
construct — and every cell is checkable against a boundary. The creativity
lives in knowing more constructs (math, algorithms, domain workflows),
not in prompting harder. The limit is your toolbox inventory, which is
exactly why knowing CatBoost, Bayes, Neyman–Pearson, or foreman's
supervision pattern is the resource: each known construct × the grammar
generates its candidate list mechanically.

Escalation rule stands: a candidate becomes a mappings.md card only with
an acceptance test that ran.

## Open positions (candidates, not yet evidenced)

- **Jev as reward shaper inside RL** — needs observed rewards; current
  evidence only supports Jev-as-feature for reward MODELING. Hypothesis.
- **Jev as grammar/sampling constraint provider** (which productions are
  semantically valid next) — inverse of its selection role; untested.
- **Jev as spec-inference**: deriving the criteria set itself from labeled
  failures (optimizer-coupled criteria search). Untested; the honest
  current claim is "criteria are designed, not yet learned."
- **Jev as VOI calculator**: numeric EVPI/EVSI from returned
  distributions. Placement (gather as an act) is the method; the
  calculator is Hypothesis until act/outcome logs exist (`mappings.md` §6).
- **Alloy/DST/RV as open product rows**: instance-loop triage, DST
  multiverse clustering, runtime-assurance sandwich, durable-agent
  gates inside Resonate steps (`mappings.md` §10–§14). Hypothesis
  until an acceptance test runs. Do not promote from the curriculum
  note alone.
- **Paraphrase stability as a numeric law:** wording-invariant p.
  Placement (abstain when paraphrases disagree) is `mappings.md` §17;
  a universal jitter bound is Hypothesis.

## Verified application families (Empirical, dabit3/jev-experiments + archive corpus)

Reusable shapes when generating applications:

1. **Streaming judge** (moderation, log triage, inbox): one fan-out request per item
   (6–7 Nouls + 1 Choice); hold-and-release at chat speed; ~95 judgments/s via ~96
   concurrent requests. **Judge once, re-policy in code**: store raw probabilities,
   move thresholds client-side, re-filter thousands of already-judged items with
   zero new requests.
2. **Keystroke-loop re-rank** (launcher, semantic lint, instant search): no debounce,
   one request per keystroke with sequence tags, apply newest-first, discard stale;
   lexical (BM25) retrieves top-30, Jev re-ranks to top-1 (measured 50%→100%).
3. **Pre-execution guards** (shell/commit/send): judge every action before it runs;
   three-tier policy — pass silently / warn / block — driven by question type +
   confidence; hooks (zsh accept-line, pre-commit, composer pause).
4. **Agents-in-the-loop**: skill/tool routing (94.4% vs 70.8% lexical), agent
   self-assessment, control-loop position: code predicts conflicts, Jev picks the
   instruction, code validates and executes.
5. **Swarm/game policies**: local perception (~1k tokens) → move/boost/pursue per
   ~400 ms tick; 32 agents, 65 decisions/s, ~$10/h.
6. **Realtime human flows**: turn-taking/barge-in decisions on partial transcripts;
   meeting action items ~150 ms after each utterance.
7. **Formula embedding**: JUDGE/SCORE/CHOOSE as first-class spreadsheet formulas.
8. **Pixel-free computer use**: accessibility tree → compact actionable-JSON → one
   batched question set per step → execute via AX actions. Encoder-backend
   cousin: gliner2-ultrafast scores observed a11y/DOM controls with
   local GLiNER2; code clicks; `DONE` ≠ success (`notes.md` §52).
   Specialist-form cousin: Cua-S1 option-attention (fill/check/click/skip);
   not TypeSafe Jev; plan ≠ execute; source-only (`notes.md` §54).
9. **Shadow-mode harness** (jev-harness): policy + confidence gate + shadow mode +
   offline eval CLI replaying fixtures, asserting on actions; 24-row filter 48.9 s
   (Claude CLI) vs 1.3 s Jev at concurrency 8. Compaction rollout:
   gliner25-compaction public default `shadowMode: true` (log proposed
   reduction; do not replace history) (`notes.md` §50).
   Stdout-prune cousin: [jev-pruner](https://github.com/tamaratran/jev-pruner)
   archives full stdout before scoring; fail-safe keep original
   (`notes.md` §53). Marketplace id still `fast-jev-output`.
   Recovery cousin: [jevons](https://github.com/LilDojd/jevons) default
   recovery **shadow** (record, do not interrupt); steering never
   generates commands (`notes.md` §51).

Calibration warning (calibre): routing thresholds and ROI do **not** transfer across
datasets — every gate is a per-dataset measurement (see validation.md).

10. **Mixed-architecture cascade** (2026-09-18 discourse + topic:jev movers):
    Jev as gate/selector/verifier *around* a generator, never instead of one.
    Cost-sensitive prefilter (drop chunks/lines/hunks before the LLM);
    tool/skill routing (Choice + fits-Noul, code dispatches); preference lint
    (project-defined *soft* rules as criteria; linter owns hard rules;
    Abide is the productized path, `notes.md` §47). Fail-open vs fail-closed is per
    action — LlamaIndex Jev rerank fails open (keep retrieval order), select
    fails closed. Full card: `references/mixed-architecture.md`.
11. **Structural prove ∩ remainder judge** (jevgate, doc-router, Abide): code
    (allowlist, text layer, linter) decides the easy cases; typed questions only
    on leftovers; fail-open unless a real sandbox sits under. Full card:
    `mappings.md` §18.
12. **1-token selector / tree of Choices** (chakuho, jev-gpt): the
    generator is reduced to a next-label or next-word Choice. Softmax
    over declared labels is not a Noul. Numeric rules and writing stay
    exact. Full cards: `judgment-class.md`, `mixed-architecture.md`.
13. **Productized System One HTTP** (classifier-dev): the public
    contract is label + calibrated confidence, not a paragraph. Batch
    state, escalate-under-threshold, and a `FALLBACK` marker are
    *code*. Full cards: `mixed-architecture.md`, `validation.md`.
14. **Evidence-synthesis pointer** (choxos/jev-reviewer, ≠ egma-ai):
    Jev picks line ids; code copies verbatim; a second absolute Noul
    checks "does this line itself answer?"; *Not found* is an answer;
    the human tick is the product. Full cards: `applied-mappings.md`
    §2, `mixed-architecture.md`.
15. **Prompted-JSON wire** (githubnext/localjev, ≠ kunchenguid/local-jev):
    the TypeSafe SDK talks to a local `/v1/systemone`; the model
    *writes* probabilities rather than exposing logits. Entropy
    confidence is computed in code from that vector. Full cards:
    `judgment-class.md`, `mixed-architecture.md`, `validation.md`.
16. **Script-before-p router** (NandhaKishorM/laya packaging of Hub
    Laya): pick the checkpoint from script/lang/task *before* the
    forward pass, because confidence will not drop on OOD (Khmer
    0.000@0.952). Post-T ECE is not raw ECE; 0.85 is still soft.
    Full cards: `judgment-class.md`, `mixed-architecture.md`,
    `faq.md`, `validation.md`.
17. **External class census** (@airesearch12 / Benchmark
    Heaven): a named list is not a rank; GLiNER2 and
    routers on the list are a class-boundary, not
    identity; incompleteness is lag. Watch the board
    URL; do not paste live scores into the census card.
    Full cards: `mixed-architecture.md`, `faq.md`,
    `validation.md`, `toolbox-mapping.md`.
18. **Geometric-mean product** (JevBench v1.2): four
    axes at 25% each; a weak axis cannot be bought
    back; weighting is a product design, not a law;
    calibration on the rank is a choice (v1.1 kept it
    off); instruction models in the same table as NAR
    rebuilds; ×2 latency and est. costs are assumptions
    to name. Full cards: `mixed-architecture.md`,
    `validation.md`, `faq.md`, `mental-models.md`.
19. **Already-folded class as a recipe** (hourly 0842):
    when the named HIGHs are already on the branch,
    extract how-to-apply instead of re-carding —
    wire-compat ≠ logit-equiv; productize label+p and
    mark `FALLBACK`; packaging ≠ new species / script-
    before-p; pointer-not-generator (two-pass; *Not
    found*; human tick); external census ≠ scored
    bake-off / geo-mean weights are a design. Skip
    thin noise. Hard-gating a Noul as a PR/quality
    gate is soundness theater. Full cards:
    `mixed-architecture.md`, `faq.md`,
    `mental-models.md`, `validation.md`.
20. **S1 keeps flying / S2 one-use** (khordoo/jev-reflex-autonomy-lab
    delta of §46): position 4 (Selector of next
    *action*) stays on the reflex every tick;
    position 7 (state estimator) is the optional
    planner — advice, not a command. Escalate-
    under-threshold **without stalling**. Log
    consumption, not arrival. Local rule-based vs
    Live API is an A/B of backends, not a scored
    bake-off; Local controller **≠** githubnext/localjev.
    Seed = geometry ≠ async replay. No pixels.
    Confidence ≠ selected probability. 20% still
    soft. S2 never grants. Full cards:
    `mixed-architecture.md`, `faq.md`,
    `mental-models.md`, `agent-self-assessment.md`,
    `validation.md`.
21. **OCR+AX observe→score→act** (awlevin/typesafe-computer-use):
    position 10 (Discretizer: screen → numbered items)
    then position 4 (Selector of next action). Writer
    is generation, not a Jev position. Split kind/item/site
    is width-is-cheap. Overlap is concentration theater.
    Perception in code rebuilds pixel-free reasoning.
    Decision never ships screenshots; the answer reader
    may. 155× is one screenshot *theirs*. Full cards:
    `mixed-architecture.md`, `faq.md`,
    `applied-mappings.md` §9, `validation.md`.
22. **ASR observe→score→act** (moritzkremb/jev-voice-browser):
    position 10 (Discretizer: waveform → transcript +
    numbered elements) then position 4 (Selector).
    Width-is-cheap: 9–11 questions on one request.
    Partial-speech wait is VOI (closed-set vs free-text).
    Spoken confirm is not a grant. Overlay numbers are
    exact, not a second model. Compose with item 21
    (OCR). Full cards: `mixed-architecture.md`, `faq.md`,
    `applied-mappings.md` §9, `validation.md`.
23. **Wrap-as-execution ALLOW/ASK/DENY** (reddpy/AgentGhost):
    position 3 (constraint on the actuator path) then
    position 4 (Selector on leftovers). Rules prove;
    Jev remainder; ASK is an error not a log line.
    Fail-closed on judge error. Distinct from actiongate
    (evidence ≠ authority) and jev-use (fail-open).
    Full cards: `mixed-architecture.md`, `faq.md`,
    `applied-mappings.md` §7, `mappings.md` §8/§18.
24. **Application genre atlas** (@studio_yebisu):
    position 11 (catalog of holes, not a score).
    Stars are research-time. Same discipline as item 17
    (class census ≠ bake-off). Full cards:
    `mixed-architecture.md`, `faq.md`, `validation.md`.
25. **External pedagogy / how-to-apply** (@akshay_pachaar):
    position 11 (explainer of already-owned placements,
    not a new construct). LLM hammer; code owns
    branches; schema-safe ≠ correct; shadow +
    questions-as-code. 200×/400× are TypeSafe ceiling.
    Full cards: `mixed-architecture.md`, `faq.md`,
    `mental-models.md`.
26. **Boolean composition of soft Nouls** (uehaj/jev-semgrep):
    position 5 (Comparator over lines) then code ∧/∨/¬
    on *thresholded* bits — never multiply parallel p
    (the logical-operator caveat above). Proposition ≠
    embedding (contrast-set refund). Not a Gate (position
    3). **≠** jev-combinators digital-design metaphor
    **≠** semgrep.dev. Full cards: `mixed-architecture.md`,
    `faq.md`, `applied-mappings.md` §4, `mappings.md` §4.
