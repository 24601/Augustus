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
27. **Decision-validated UI** (gram-render + jev2ui):
    position 4 (Selector over derived candidates) then
    position 2 (compiler / schema as constraint). Jev
    never authors text. Valid GramSpec/A2UI ≠ good screen.
    Remix samples the already-returned Score distribution
    (item 32 cousin). Full cards: `mixed-architecture.md`,
    `faq.md`.
28. **Decision-as-assert** (jevtest): position 3 is
    *tempting* (hard-gate as CI pass) and **rejected** —
    the matcher is a sensor. Ambiguous band is anti-round
    (fails both polarities). Exact envelope stays in
    ordinary assertions. Record/replay is measurement, not
    a live Noul-as-proof. Full cards: `faq.md`,
    `formal-methods.md`, `question-design.md`.
29. **Hybrid S1 / closed verb menu** (anima3): position 3
    (hard safety proves the irreversible act) then
    position 4 (Selector among remaining verbs). Logprob ≠
    Noul. Encoder confidently-flat on magnitude is a
    family mismatch. Full cards: `mixed-architecture.md`,
    `agent-self-assessment.md`.
30. **Pointer search** (JevFind): position 4 then copy
    (same as extractive keep/drop). Path filter is VOI
    (item 6). Thresholds still soft. Full cards:
    `applied-mappings.md` §2, `mappings.md` §4.
31. **Harbor bake-off trio** (frontier-bench /
    gliclass-bench / job-posting-triage): position 11
    (measurement construct). Three shapes: vs frontier
    LLMs; product bakeoff ≠ architecture duel; four
    *kinds* of engine. Always name the majority floor.
    Calibration ≠ discrimination. LLM-as-judge is not the
    System One score. Full cards: `validation.md`,
    `faq.md`.
32. **Full-distribution optimizer** (jevloop): position 8
    (judgment as a *value function* inside a search that
    is not an LM-program climb). UCB1+CEM over operators
    in code; no LLM in the loop. Mock default ≠ quality.
    Distinct from Ax/DSPy (item: climb LM knobs) and
    slo-router (Jev as a *feature*). Full cards:
    `optimizer-integration.md`, `faq.md`.
33. **Physical-world S1 portable** (ha-switchboard):
    position 3 (HA execution envelope) × position 1
    (Jev SENSOR). Distinct from HA-Jev (gallery still
    17★). Not for locks. Full cards: `mappings.md` §8,
    `mixed-architecture.md`.
34. **n8n classify/route/score**: position 6 (Router) with
    an explicit Low Confidence abstention output.
    Arithmetic stays in Code/IF. Unofficial. Full cards:
    `applied-mappings.md` §4, `faq.md`.
35. **Compaction-pi namesake lock**
    (fast-jev-compaction-pi): same job as item 26's
    pointer species, different product. **≠**
    pi-jev-compact **≠** pi-jev-compaction. Fail-open to
    host summarizer. Full cards: `applied-mappings.md` §1.
36. **Deferred class: vision / competing NAR / grounding**
    (laya-vision, Cerebellum-2B, laya-grounded): position
    10 (perception) vs position 4 (pointer over
    candidates) vs a **fine-tune that is not a drop-in**.
    Wire-compat (`/v1/decide`) and agent-routing are
    separate Harbor axes. Platt ≠ temperature.
    Entropy-confidence ≠ max_prob. Competing NAR is an
    audit object (kinship item: openJev-verdict). Full
    cards: `judgment-class.md`, `validation.md`,
    `faq.md`.
37. **Open LoRA replica namesake** (GestaltLabs/Jeff-1):
    position 4 (typed decide) with an acc/ECE tradeoff.
    Wire `/v1/systemone` ≠ identical judgments. **≠**
    logan-markewich/jeff (item: GLiFormer encoder).
    Reused eval set is Harbor honesty. Full cards:
    `judgment-class.md`, `validation.md`, `faq.md`.
38. **Empty findings ≠ approval** (stanley-code):
    position 3 (exact signals + `notChecked` ledger) ×
    position 1 (Jev SENSOR). Human promote is the
    actuator. Soft router thresholds. Full cards:
    `applied-mappings.md` §5, `mappings.md` §8.
39. **Beam-search FS** (findme): position 8 (search
    algorithm yours; S1 ranks listed candidates).
    Distinct from JevFind path-then-window (item 30
    cousin). Full cards: `mappings.md` §9, `faq.md`.
40. **Price workers, not the conversation**
    (jevsubrouter): position 6 (Router) with the
    prompt-cache as the exact envelope. Binding ≠
    advice. Fail-open. Counts ≠ dollars. Full cards:
    `applied-mappings.md` §5, `faq.md`.
41. **Typed if** (feelings): position 2 (language
    primitive). `.feels()` default 0.5 is
    Noul-0.5-never-rounded. Exhaustive `match` is
    the exact envelope. **≠** hunch **≠** Probably.
    Full cards: `mappings.md` §3, `faq.md`.
42. **Shadow then honor** (apa-agent-harness /
    grok-bot-jev): position 9 (shadow harness) with
    skill honor. Unpublished npm. A/B proxies ≠
    tokens. **≠** AntonioCoppe/jev-harness. Full
    cards: `mixed-architecture.md`, `faq.md`.
43. **Persona state-machine** (apa-persona-engine):
    position 19 (effect-oriented SM). <250 ms ≠
    microsecond. Full cards: `mappings.md` §3.
44. **Human every action** (Essentiel-Jev): position
    1 (sensor) × human actuator. Never authority.
    Full cards: `mappings.md` §8, `applied-mappings.md`
    §7.
45. **Atom then sense** (enzo-mcp): position 3 after
    deterministic evidence. UNKNOWN useful. **≠**
    jev-sift. Full cards: `applied-mappings.md` §1.
46. **File by Choice** (pigeonhole): position 2
    (keep/drop among folders). `OTHER` skip. Full
    cards: `applied-mappings.md` §2.
47. **Question preflight** (jev-reliability /
    clduab11/jev-test / jev-rag-benchmark /
    dairui1/jev-lab): measurement owns endorsement.
    Nothing about accuracy. Bars ≠ scores. “Jev
    wins” is not an assumption. Full cards:
    `validation.md`, `question-design.md`.
48. **Inbox read-only vs write** (jevmail / mailjay):
    ranking trays vs proposed archive/trash.
    **≠** mailordinal. Full cards:
    `applied-mappings.md` §4, §8.
49. **Observe→score→act namesake** (ZHUBoer/ego-jev):
    position 2 (keep/drop among observed candidates)
    × position 9 (search/control loop). Reserved
    `__none__`. `choose` does no act. runWorkflow
    completed ≠ success. **≠** jiangkoumo/ego-jev.
    Full cards: `applied-mappings.md` §9, `faq.md`.
50. **Decision-as-ranking** (jsort): position 4
    (bounded rerank) with Bradley-Terry pairwise.
    Scores relative. Noul not Choice for scale.
    Full cards: `mappings.md` §4, `faq.md`.
51. **Native vs schema-guided Harbor**
    (groundedness-judge-bench): same rubric, two
    adapters. Fastest/cheapest ≠ quality.
    implicit_true included in yes. **≠**
    jev-judge-bench. Full cards: `validation.md`.
52. **0 promotions / authored vs real**
    (jev_playground): measurement owns endorsement.
    Plumbing green ≠ quality. routing-backtest
    0.0447%. Full cards: `validation.md`.
53. **Offload + classifier-not-generator**
    (yuyang2230/jev-agent-skill /
    jev-techstack-classifier): leftover writer vs
    cheap decide; ranks listed options only.
    jev-1.13-free. stack_config.json. Full cards:
    `applied-mappings.md` §5.
54. **Collapse late** (s1_ruby): position 2
    (language primitive). `?` collapses;
    `undecided?` abstains. **≠** hunch **≠**
    feelings. Full cards: `mappings.md` §3.
55. **Unofficial toolbelt** (judgement /
    typesafeai-sdk-community): packaging ≠ new
    species. confidence ≠ winner p. License null
    on the Go CLI. Full cards: `judgment-class.md`.
56. **Pointer shell** (tpellet/hunch): position 2
    × never-execute list. Exit 3 abstains. **≠**
    carldaws/hunch. Full cards: `mappings.md` §3,
    `applied-mappings.md` §7.
57. **Preview-first VOI / rubric rewrite**
    (jev-file-search / jev-linkmap): gather as an
    act; scores not calibrated accuracy; Jev never
    sees S2 prose. Full cards: `mappings.md` §6.
58. **Life fail-open covers** (jev-mail / tidy /
    tab-bouncer / lkclean / jev-yt-time-saver):
    ranking fail-open. Metadata only. none-of-
    folders stay. pinned/audio/current never
    closed. Show anyway. Full cards:
    `applied-mappings.md` §2, §4, §7.
59. **S1 decide / S2 plan** (ORIGIN-CIVILIZATION):
    position 1 (sensor) × pause-if-no-Jev envelope.
    validResponse sums-to-1. **≠** Essentiel-Jev.
    Full cards: `mappings.md` §8, `faq.md`.
60. **Seed/expand/judge/verify** (jev-crawlers):
    position 8 (search) with risk bands never raw
    boolean. Verify grounding, not exec. Full
    cards: `applied-mappings.md` §3.
61. **Local daemon ≠ Jev** (jevbrain): overlap
    sensor, not a Noul. AUTO_ACT is not a Noul.
    Full cards: `judgment-class.md`, `faq.md`.
62. **Judge harness as control API** (judgekit /
    typed-judge-kit): position 2 (keep/drop among
    YAML/recipe tasks) × measurement. judgekit YAML classify/score/route/verify. typed-judge-kit verdict-in-code. **≠** JudgeBench **≠** DeepEval.
    Full cards: `applied-mappings.md` §5, `faq.md`.
63. **Batch packing VOI** (alsoleg89/decide):
    position 6 (gather as an act). alsoleg89/decide packing VOI. 0.8 ≠ 80% accuracy. **≠** jev-sift.
    Full cards: `mappings.md` §6, `faq.md`.
64. **Calibration as product** (Jev-Calibration /
    jev-calibration-arena): jevals surface. Jev-Calibration Platt ECE 0.117→0.052. jev-calibration-arena never acts. **≠** jev-arena. Full cards:
    `validation.md`, `faq.md`.
65. **Decision-as-Plugin** (openrouter-jev-mcp /
    typesafe-mcp / FrancoisChastel/jev-code /
    claudecode-jev-marketplace / mcp_jev /
    jev-skill): packaging ≠ new species.
    ctmx/openrouter-jev-mcp Decision-as-Plugin.
    FrancoisChastel/jev-code ≠ npm jev-code.
    claudecode-jev-marketplace fail-open not hot path. pedroknigge/mcp_jev packs not ask_jev.
    cyrusasco/typesafe-mcp noul deadband 0.35–0.65.
    codaaiteam/jev-skill jevtypesafeai.com ≠ TypeSafe.
    Full cards: `judgment-class.md`, `faq.md`.
66. **Policy-constrained skill select**
    (hermes-switchyard): position 1 (sensor) ×
    eligibility in the plugin. hermes-switchyard ≠ hermes-jev-router ≠ hermes-plugin-jev. Never
    loads skills. Full cards:
    `applied-mappings.md` §5, `faq.md`.
67. **Tiny local econ pruner** (nanoprune):
    position 4 (bounded rerank) as a local encoder
    gate. nanoprune 2.8MB ECE 2.58%. Distill ≠
    hosted Noul. Full cards: `mappings.md` §4,
    `judgment-class.md`.
68. **Observe→score→act cousins**
    (jev-browser-agent / omp-jev-web / hari007sh/jev):
    position 9. smartdio/jev-browser-agent ≠ ZHUBoer/ego-jev. Dakai/omp-jev-web DONE ≠ proof.
    hari007sh/jev ≠ dannote/jev. Full cards:
    `applied-mappings.md` §9, `faq.md`.
69. **Deterministic verify ≠ System One**
    (system-one-skills): exact wrapper, not a Noul.
    0thernet/system-one-skills deterministic verify.
    Full cards: `judgment-class.md`, `faq.md`.
70. **Soft-score vs hard-argmax** (typed-gate /
    pi-jev-gate): read p; mid-band is refusal.
    typed-gate band [0.40,0.60] is refusal.
    pi-jev-gate fail-closed; choice is the verdict.
    rh-guard owns the gate cousin. Full cards:
    `mixed-architecture.md`, `faq.md`.
71. **Self-hosted econ** (Foq / rev / robfrase/jev):
    local typed decide. Foq ~25ms/2.2GB local.
    rev prefill-only + HF jev-0.5b.
    robfrase/jev planning memo. Sample 32.4 ms is
    not a bench. Full cards: `judgment-class.md`,
    `faq.md`.
72. **Soft-judgment gate integrity**
    (typesafe_agent_gates / safe-sh / pastepilot):
    remainder after exact rules. typesafe_agent_gates 27/27 / 31/31.
    EpicEric/safe-sh static remainder.
    pastepilot Confirm before act. rh-guard owns.
    Full cards: `applied-mappings.md` §7, `faq.md`.
73. **Retrieval as calibrated decision space**
    (Jev-Reranker / sessionwise / jev-search):
    position 4. Jev-Reranker live Jev not yet measured.
    sessionwise opt-in relevance.
    jev-search pointer sieve. Score ≠ truth.
    Always **savka777/jev-search**. **≠**
    kazuhideoki/jev-search **≠** superagents-lab/jev-search.
    Full cards: `mappings.md` §4, `faq.md`.
74. **Enterprise reflexes** (400ms-agentic-sf /
    scheduler-diagnostics): categorization leaving
    the IDE. 400ms Salesforce WebMCP.
    typesafe-scheduler-diagnostics advisory. Does
    not place Pods. Full cards: `faq.md`.
75. **Screenshot-free / CU** (droidjev / jevcu):
    mappings §9 search/control (observe→score→act).
    droidjev screenshot-free.
    Tewoto1 jevcu planner still writes. **≠**
    closed-vote. Full cards:
    `applied-mappings.md` §9 (not closed-vote cousins),
    `methods-catalog.md` computer-use row, `faq.md`.
76. **Hybrid S1/S2** (ha-conversation-jev / dsh-jev):
    position 1 × leftover writer. ha-conversation-jev Jev→Grok.
    dsh-jev can only gate. **≠** HA-Jev. Full cards:
    `mappings.md` §8, `faq.md`.
77. **Harbor-jevals / SRE**
    (classification-benchmark / luna-pagerduty):
    measurement owns endorsement.
    jev-classification-benchmark specified not run.
    jev-luna-pagerduty p≥0.50. Full cards:
    `validation.md`, `faq.md`.
78. **Laya densifies** (meldecision / laya-doom /
    laya-api / akpsahan/laya): packaging ≠ new
    species. meldltd/meldecision laya-go ONNX.
    laya-doom never pixels.
    logixism/laya-api empty README.
    akpsahan/laya ≠ Archer. **≠** Qwen3.8-27B.
    Full cards: `judgment-class.md`, `faq.md`.
79. **Demos / unofficial toolbelt** (jevchess /
    jev-drive / story-arc / hs-assistant / SC2 /
    awesome-jev-use-cases / typesafe-go): engine
    owns truth. choxos/jevchess engine owns truth.
    jev-drive sim not AV. story-arc Jev never authors.
    jev-hs-assistant HS6.
    golergka/jev-plays-starcraft-2 UI-verified ≠ API Victory.
    awesome-jev-use-cases catalog.
    Nibir1/typesafe-go ≠ official. Full cards:
    `faq.md`.

Hourly 1441 items 71–79 (`notes.md` §92). Do **not**
re-fold 1347 items 62–70. soft Noul ≠ hard safety.
80. **Decision ledger / memoization**
    (hyperspaceai/jevcache): memoize typed
    decisions. fingerprint after redact.
    recall vs decide. publish fingerprints+answers.
    CI replay as Harbor cousin. Cache hit ≠
    correctness. hyperspaceai/jevcache ≠
    kushals256/jevcache. Not Hyperspace KV
    attention cache. Full cards: `mappings.md` §6,
    `faq.md`.
81. **GEPA alignment loop** (sutro-sh/jev-align):
    GEPA + System One; inverse of Jev-as-metric.
    human labels only. score never auto-accepts.
    production capture flywheel. sutro-sh/jev-align ≠
    caiovicentino/jev-align. Full cards:
    `optimizer-integration.md`, `faq.md`.

SIGNAL §93 items 80–81 (`notes.md` §93). Do **not**
re-fold 1441 items 71–79. Unique fragments
(consecutive): fingerprint after redact; recall vs decide; publish fingerprints+answers; CI replay as Harbor cousin; Cache hit ≠ correctness; hyperspaceai/jevcache ≠ kushals256/jevcache; human labels only; score never auto-accepts; production capture flywheel; sutro-sh/jev-align ≠ caiovicentino/jev-align.
soft Noul ≠ hard safety.
82. **Compile-time System One / questions-as-index**
    (byenzyme/enzyme): Jev at compile; runtime
    catalysts. guidance ≠ hook. catalysts ≠
    summaries. compile-time System One. Soft
    guidance ≠ hard gate. hosted bootstrap ≠
    silent TypeSafe. Full cards: `mappings.md`
    §6, `faq.md`.
83. **Unofficial JA ModernBERT cross-encoder**
    (argos1111/modernbert-ja-310m-jev): pair
    scoring → softmax. unofficial ≠ TypeSafe.
    format_version modernbert-jev/1.
    Argos1111/jev_local ≠ us/jev-local ≠
    kunchenguid/local-jev. LFM default ≠
    ModernBERT backend. Full cards:
    `judgment-class.md`, `faq.md`.
84. **NAR class legitimacy / multimodal /
    Router-OOD** (Gemma X / Nemotron_Jev /
    djev-dev / Laya essay): Nemotron ≠ TypeSafe
    Jev. not a calibrated replacement. djev-dev
    complements djev-spark. images as Choice
    options. Laya essay numbers *theirs*.
    Router/OOD confidence. Full cards:
    `judgment-class.md`, `faq.md`.

SIGNAL §94 items 82–84 (`notes.md` §94). Do **not**
re-fold §93 items 80–81. Unique fragments
(consecutive): guidance ≠ hook; catalysts ≠ summaries; compile-time System One; unofficial ≠ TypeSafe; format_version modernbert-jev/1; Argos1111/jev_local ≠ us/jev-local ≠ kunchenguid/local-jev; LFM default ≠ ModernBERT backend; Nemotron ≠ TypeSafe Jev; not a calibrated replacement; djev-dev complements djev-spark; images as Choice options; Laya essay numbers *theirs*; Router/OOD confidence; hosted bootstrap ≠ silent TypeSafe.
soft Noul ≠ hard safety.

Hourly 1541 unique consecutive fragments:
difficulty + policy thresholds + JSONL trace;
jev-codex-pilot model + reasoning depth;
keep/shadow/hybrid/reject;
quarry evidence projection;
Frank-ZY-Dou/awesome-jev robotics/3D/control;
one-dollar-tahoe TypeSafe Jev defense eval;
jevguard calibrator/cache/escape;
jev-ci-selector CI shadow mode;
llama-jev llama.cpp replica.
petercr/jev-orchestrator ≠ FleeexCorp/jev-orchestrator.
seb4ez/jevguard ≠ AseemPrasad/JevGuard ≠ pablozr/JevGuard.
webNeat/llama-jev ≠ WiktorB2004/llama-index-jev.

85. **Decision-as-plugin for SWE**
    (orchestrator / pilot / replacement):
    position 1 × leftover writer. Jev proposes the
    next bounded act; code owns policy.
    difficulty + policy thresholds + JSONL trace.
    jev-codex-pilot model + reasoning depth.
    keep/shadow/hybrid/reject. GitHub “difficulty”
    is not a live Score. Full cards: `faq.md`,
    `applied-mappings.md` §8.
86. **Evidence projection** (quarry):
    position 4. Fetch to disk; Jev scores line
    ranges. quarry evidence projection.
    Pointer, never paraphrase. Fail-open 5 s.
    Full cards: `mappings.md` §4, `faq.md`.
87. **Soft judgment integrity**
    (jevguard / jev-ci-selector): remainder after
    exact rules. jevguard calibrator/cache/escape.
    jev-ci-selector CI shadow mode. Shadow default;
    enforce opt-in. rh-guard owns gates. Full cards:
    `applied-mappings.md` §7, `faq.md`.
88. **Physical/control first-class domain**
    (Frank-ZY-Dou/awesome-jev): mappings §9
    search/control. Frank-ZY-Dou/awesome-jev robotics/3D/control.
    Text-state, not pixels. One seed-0 ≠ a rate.
    Full cards: `mappings.md` §9, `faq.md`.
89. **Harbor-jevals / injection-firewall**
    (one-dollar-tahoe): measurement owns endorsement.
    one-dollar-tahoe TypeSafe Jev defense eval.
    ~74 demo; README has no ASR/FPR. Do not copy
    attacks. rh-guard owns. Full cards:
    `validation.md`, `faq.md`.
90. **llama.cpp replica** (llama-jev): packaging ≠
    new species. llama-jev llama.cpp replica.
    Numbered-choice softmax ≠ Noul. **≠** TypeSafe
    **≠** pcdServer. Full cards: `judgment-class.md`,
    `faq.md`.

Hourly 1541 items 85–90 (`notes.md` §95). Do **not**
re-fold 1441 items 71–79. soft Noul ≠ hard safety.

91. **OpenCode stdout-prune host port**
    (indiejoseph/opencode-jev-pruner):
    position 2 (keep/drop among stdout chunks) ×
    hard envelope. OpenCode jev-pruner context sieve.
    observe→score-candidates→prune.
    jev-zen / jev-1.13-free. zen-chat ≠ Noul.
    fail-open original. keepScore >0.1 floor.
    host port of tamaratran/jev-pruner.
    indiejoseph/opencode-jev-pruner ≠ nrdz-labs/fast-jev-opencode.
    Full cards:
    `applied-mappings.md` §1, `faq.md`.
92. **Schema/SDK adapters + empty bench**
    (watch / tooling): packaging ≠ new species.
    jev-webagent-bench empty stub.
    Kiln-AI/jev_jsonschema noul_threshold 0.5
    (decoder, not a proof).
    NSStudent/JevSwiftSDK unofficial.
    Full cards: `faq.md`, `judgment-class.md`.

Hourly 1639 items 91–92 (`notes.md` §96). Do **not**
re-fold 1541 items 85–90. Soft Noul ≠ hard safety.

SIGNAL gliner-native-runtime unique consecutive
fragments:
GLiNER2 native Apple path;
unofficial Swift/Core ML GLiNER 2.5-small;
entity spans + confidence;
not Choice/Score/Noul;
not TypeSafe;
label descriptions as schema;
on-device ANE economics;
honesty locks;
shershah1024/gliner-native-runtime ≠ Fastino;
≠ gliner25-compaction ≠ gliner2-ultrafast ≠ Eran-BA/Jev_from_GLiNER2 ≠ NSStudent/JevSwiftSDK ≠ jevmlx;
default threshold 0.1 still soft.

93. **GLiNER2 native Apple path**
    (shershah1024/gliner-native-runtime):
    position 10 (Discretizer/encoder: schema+text
    → labeled spans) × on-device remainder.
    Not position 4 Selector of F. Spans are
    encoder-proposed; not keep/drop over offsets
    code already holds. unofficial Swift/Core ML
    GLiNER 2.5-small. entity spans + confidence.
    not Choice/Score/Noul. not TypeSafe.
    label descriptions as schema.
    on-device ANE economics. honesty locks.
    default threshold 0.1 still soft.
    Full cards: `judgment-class.md`, `faq.md`.

SIGNAL §97 item 93 (`notes.md` §97). Do **not**
re-fold 1639 items 91–92. Soft Noul ≠ hard safety.

Hourly 1740 unique consecutive fragments:
Decision Graph Protocol frame→assess→commit;
app retains permissions/effects;
Jev-first assessor-neutral;
guarded commit / receipt/next frame;
assessment batching;
hard-gating DGP as safety theater;
numerous-com/dgp ≠ TypeSafe official;
jegrep calibrated path+range Nouls;
no embeddings/index/daemon;
~$0.01–0.03 typical;
agent --json;
can1357/jegrep ≠ Bentlybro/jevgrep ≠ uehaj/jev-semgrep;
Archer-arch fidelity;
kev family OOD 0.76–0.77 vs Jev 0.86;
block-causal isolation;
pointer/readout CE-trained;
/v1/systemone drop-in;
replica honesty.

94. **Decision Graph Protocol envelope**
    (numerous-com/dgp):
    position 3 (guard / authorize) × host-owned
    remainder. Immutable frame → typed assessment →
    guarded commit → receipt/next frame. App retains
    permissions/effects. Jev-first assessor-neutral.
    assessment batching. Commit fail-closed in the
    application; assessment is a sensor.
    hard-gating DGP as safety theater.
    numerous-com/dgp ≠ TypeSafe official.
    **≠** waymode **≠** ctmx/openrouter-jev-mcp
    Decision-as-Plugin **≠** petercr/jev-orchestrator
    **≠** AgentGhost wrap-as-execution.
    Full cards: `mixed-architecture.md`, `faq.md`,
    `formal-methods.md`.
95. **Calibrated meaning-grep over a live tree**
    (can1357/jegrep):
    position 4 (Selector of F) × cascade IR.
    jegrep calibrated path+range Nouls.
    no embeddings/index/daemon.
    ~$0.01–0.03 typical. agent --json.
    Ranking fail-open. No published Harbor.
    OpenRouter/TypeSafe auto-failover is silent
    FALLBACK, not the same Noul. Auto-τ-lowering
    is not a 0.4 proof. beam “gate Noul” is ranking,
    not a safety envelope.
    can1357/jegrep ≠ Bentlybro/jevgrep ≠ uehaj/jev-semgrep.
    Full cards: `applied-mappings.md` §4, `faq.md`.
96. **Archer-arch fidelity + measured calibration
    gap** (jaredpalmer/kev family; not a rewrite of
    §45):
    position 1 (replacement of a classifier step) ×
    trained decision-only family.
    Archer-arch fidelity. block-causal isolation.
    pointer/readout CE-trained. /v1/systemone drop-in.
    kev family OOD 0.76–0.77 vs Jev 0.86.
    replica honesty. Architecture confirmation ≠
    Jev identity. Score confidence is a stand-in
    (*theirs*); wire ≠ TypeSafe confidence.
    Jev-omni owns the replica/code fold.
    Full cards: `judgment-class.md`, `faq.md`.

Hourly 1740 items 94–96 (`notes.md` §98). Do **not**
re-fold 1639 items 91–92 / SIGNAL §97 item 93.
Soft Noul ≠ hard safety.

Hourly 1843 unique consecutive fragments:
cost-sensitive decision theory × System One probabilities → control flow;
thresholds derived from costs not hard-coded;
YES / NO / UNSURE from cost_false_yes / cost_false_no / cost_human;
auto-batching same-object questions;
Kungie/gut ≠ tpellet/hunch ≠ carldaws/hunch;
judgment vs generation;
deterministic execution after probabilistic judgment;
exactly one app-owned callback;
explicit uncertain branch;
Illusion47586/judge ≠ lexingtonhibiki/judgekit ≠ Ascurse/typed-judge-kit;
variable-N option scoring as the trainable object;
dynamic candidate bags not fixed label sets;
zwliJay/jev-forge ≠ NanoJev;
open replica economics / latency vs closed Jev;
NAR local drop-in;
wfzyx/von late-catch HIGH;
competing NAR claims / replica honesty;
typed judgments vs chat judges on guardrailing;
ishaannk/llm-vs-jev cross-note only;
deeper integrity fold is rh-guard;
nothing wins outright;
can be argued out of guarding.

97. **Cost-derived YES/NO/UNSURE control flow**
    (Kungie/gut; PRIMARY):
    position 3 (Gate) × EU/Chow/Elkan remainder.
    cost-sensitive decision theory × System One
    probabilities → control flow.
    thresholds derived from costs not hard-coded.
    YES / NO / UNSURE from cost_false_yes /
    cost_false_no / cost_human.
    auto-batching same-object questions.
    Overlay, **not** a new class-table species.
    Default `on_unsure="raise"` is app policy,
    not a System One hard gate.
    Kungie/gut ≠ tpellet/hunch ≠ carldaws/hunch.
    Full cards: `mental-models.md`, `faq.md`.
98. **Typed-callback twin**
    (Illusion47586/judge):
    position 3 (Gate) / 4 (Selector of F) ×
    app-owned remainder.
    judgment vs generation.
    deterministic execution after probabilistic
    judgment.
    exactly one app-owned callback.
    explicit uncertain branch.
    Provider-neutral core; Jev default.
    Illusion47586/judge ≠ lexingtonhibiki/judgekit
    ≠ Ascurse/typed-judge-kit.
    Full cards: `mixed-architecture.md`, `faq.md`.
99. **Variable-N option scoring as the trainable
    object** (zwliJay/jev-forge):
    position 1 (replacement of a classifier step)
    × decide-family training object.
    dynamic candidate bags not fixed label sets.
    Not a new class-table species. Not GLiClass
    categorize. Do not clone weights/corpora.
    zwliJay/jev-forge ≠ NanoJev.
    Full cards: `judgment-class.md`, `faq.md`.
100. **Open NAR replica economics** (wfzyx/von
     late-catch HIGH):
     position 1 × local NAR drop-in.
     NAR local drop-in.
     open replica economics / latency vs closed Jev.
     competing NAR claims / replica honesty.
     Do not merge Needle 52.6% with n=78 93%.
     Do not dump weights.
     Full cards: `judgment-class.md`, `faq.md`.
101. **Typed vs chat judges on guardrailing**
     (ishaannk/llm-vs-jev; cross-note):
     position 2 (Post-judge) / 9 (Verifier) eval.
     typed judgments vs chat judges on guardrailing.
     nothing wins outright.
     can be argued out of guarding.
     ishaannk/llm-vs-jev cross-note only.
     deeper integrity fold is rh-guard.
     Full cards: `validation.md`, `faq.md`.

Hourly 1843 items 97–101 (`notes.md` §99). Do **not**
re-fold 1740 items 94–96 / SIGNAL §97 item 93.
Soft Noul ≠ hard safety.

Jev IS the if-statement; judgments/probabilities drive branches; text model only writes prose; interpreter owns variables/loops/budgets/replay; otherwise maybe / confidence gate; chaos samples after the gate; southpolesteve/probably ≠ carldaws/hunch ≠ feelings ≠ Kungie/gut ≠ Illusion47586/judge ≠ tidymodels/probably; 133★ / forks 10 live; build calibrated classifiers from human feedback; retrieve by relevance not resemblance; one calibrated yes/no per memory in one request; pointer mode 17/18 19/20 *theirs*; embedding resemblance misses the allergy; samdotmak/jev-recall ≠ jev-search ≠ jev-sift ≠ carryforward ≠ chopratejas/invalidate; memory leases ended by new evidence; six Nouls then fixed rules in code; 0 of 157 false invalidations; questions/plans/directives are not evidence; unsure → review queue; host keeps the store; name↔body / comment truth / test-claims; mizchi/jev-lint is mizchi/jevlint rename; no shipped rule has severity error; ~1 in 5 findings wrong *theirs*; mizchi/jev-lint ≠ huntedman/JevLint ≠ MichitoSugawara/jev-lint; JSON Schema → typed JSON via Jev; noul_threshold 0.5 decoder not a proof; IncompatibleSchemaError lists every bad property; on-device Laya CoreML ANE; ~5 ms P50 short decisions; 189/189 FP16 checkpoint parity; 10× not achieved; mizorewww/laya-coreml ≠ gliner-native-runtime ≠ jevmlx ≠ NandhaKishorM/laya; softmax over allowed tokens ≠ Noul; question-first cache; Micha0827/snapjudge ≠ githubnext/localjev ≠ jevmlx ≠ cendress/SnapJudge; Jev-first Pi agent loop; slow-LLM fallback; explicit action menu / CandidateSource unimplemented; 62 tests wiring not quality; direwolfiy/JevPi ≠ standardagents/jevpilot ≠ pi-jev-control

102. **Jev IS the if-statement** (southpolesteve/probably; PRIMARY):
     positions 3 (Gate) / 4 (Selector) / 11 (Bounds) as *language
     constructs*. judgments/probabilities drive branches.
     text model only writes prose.
     interpreter owns variables/loops/budgets/replay.
     otherwise maybe / confidence gate.
     chaos samples after the gate.
     Language, not a library overlay.
     southpolesteve/probably ≠ carldaws/hunch ≠ feelings ≠
     Kungie/gut ≠ Illusion47586/judge ≠ tidymodels/probably.
     Full cards: `mental-models.md`, `faq.md`.
103. **GEPA alignment live delta** (sutro-sh/jev-align):
     position 8 inverse (definition search; Jev is the cheap
     executor). 133★ / forks 10 live.
     build calibrated classifiers from human feedback.
     HEAD/README SHA unchanged vs §93.
     Full cards: `optimizer-integration.md`, `faq.md`.
104. **Retrieve by relevance not resemblance** (samdotmak/jev-recall):
     position 5 (Comparator) × ∀ over a candidate set.
     one calibrated yes/no per memory in one request.
     pointer mode 17/18 19/20 *theirs*.
     embedding resemblance misses the allergy.
     samdotmak/jev-recall ≠ jev-search ≠ jev-sift ≠
     carryforward ≠ chopratejas/invalidate.
     Full cards: `applied-mappings.md`, `faq.md`.
105. **Memory leases ended by new evidence** (chopratejas/invalidate):
     position 9 (Verifier) × 3 (Gate) on write.
     six Nouls then fixed rules in code.
     0 of 157 false invalidations.
     questions/plans/directives are not evidence.
     unsure → review queue.
     host keeps the store.
     Full cards: `formal-methods.md`, `faq.md`.
106. **Contract-of-artifact lint** (mizchi/jev-lint):
     position 9 (Verifier) ∩ AST prove remainder.
     name↔body / comment truth / test-claims.
     mizchi/jev-lint is mizchi/jevlint rename.
     no shipped rule has severity error.
     ~1 in 5 findings wrong *theirs*.
     mizchi/jev-lint ≠ huntedman/JevLint ≠
     MichitoSugawara/jev-lint.
     Full cards: `mixed-architecture.md`, `faq.md`.
107. **JSON Schema question compiler** (Kiln-AI/jev_jsonschema):
     position 10 (Discretizer / encoder).
     JSON Schema → typed JSON via Jev.
     noul_threshold 0.5 decoder not a proof.
     IncompatibleSchemaError lists every bad property.
     Full cards: `question-design.md`, `faq.md`.
108. **On-device Laya CoreML ANE** (mizorewww/laya-coreml):
     position 1 × local replica economics.
     on-device Laya CoreML ANE.
     ~5 ms P50 short decisions.
     189/189 FP16 checkpoint parity.
     10× not achieved.
     mizorewww/laya-coreml ≠ gliner-native-runtime ≠ jevmlx ≠
     NandhaKishorM/laya.
     Full cards: `judgment-class.md`, `faq.md`.
109. **Local logit `/v1/systemone`** (Micha0827/snapjudge):
     position 1 × constrained-AR local drop-in.
     softmax over allowed tokens ≠ Noul.
     question-first cache.
     Micha0827/snapjudge ≠ githubnext/localjev ≠ jevmlx ≠
     cendress/SnapJudge.
     Full cards: `judgment-class.md`, `faq.md`.
110. **Jev-first Pi agent loop** (direwolfiy/JevPi):
     positions 4 (Selector of F) × 3 (Gate) with S2 leftover.
     Jev-first Pi agent loop.
     slow-LLM fallback.
     explicit action menu / CandidateSource unimplemented.
     62 tests wiring not quality.
     direwolfiy/JevPi ≠ standardagents/jevpilot ≠ pi-jev-control.
     Full cards: `agent-self-assessment.md`, `faq.md`.

resume-screening bias audit methodology; name×resume factorial independent Nouls; callback determined by resume quality; mean-probability name gaps operationally negligible; natemoo-re/bias-bench ≠ BBQ; Plan/PRD panel → code-owned pass|review|block; cheerleading out of scope; austindixson/planalyzer ≠ single-goodness Noul; cost-aware multi-model routing/escalation; decide vs do; successful-task cost; cannacre8ive/switchboard-ai ≠ ha-switchboard ≠ hermes-switchyard; frozen-protocol zero-shot bench; TypeSafe Jev vs PrismNLI vs Laya; contamination caveat; elcronos/jev-vs-open-decision-models ≠ JevBench ≠ DMB; context-window admission control; VOI gate which tokens are worth the expensive model; fail polarity per lens; on small inputs lenses lose money; cvsgireesh/jevusher ≠ jev-sift ≠ winnow; typed decision control plane; receipt ≠ authorization; historical-v0 zero retained cases; MokiMeow/jev-fabric ≠ jev-forge ≠ dgp; live 15-dim typed rubric re-score per pause; scoring economics exemplar; OpenJev/Codiv ≠ TypeSafe hosted; jose-troche/live-rubric ~$0.000004 desc / ~$0.000006 README; adversarial pre-registered Jev eval; 28 predictions before data; 123,805 requests; confidence does not track ignorance; polite injection 65% / crude 0%; willkelly/jev-evaluation ≠ jevals ≠ jev-baselines-eval; provider-neutral Elixir/BEAM Noul/Choice/Score SDK; class infrastructure; nshkrdotcom/system_one_sdk ≠ typesafe_sdk ≠ dannote/jev

111. **Resume-screening bias audit** (natemoo-re/bias-bench; PRIMARY):
     position 9 (Verifier) × SDT operating point. name×resume
     factorial independent Nouls. callback determined by resume
     quality. mean-probability name gaps operationally negligible.
     natemoo-re/bias-bench ≠ BBQ.
     Full cards: `mental-models.md`, `faq.md`.
112. **MCDA panel + code-owned verdict** (austindixson/planalyzer):
     positions 5 (Comparator) × 3 (Gate). Plan/PRD panel →
     code-owned pass|review|block. cheerleading out of scope.
     austindixson/planalyzer ≠ single-goodness Noul.
     Full cards: `mixed-architecture.md`, `faq.md`.
113. **EU cost-aware routing** (cannacre8ive/switchboard-ai):
     positions 4 (Selector) × 3 (Gate) with S2 leftover.
     cost-aware multi-model routing/escalation. decide vs do.
     successful-task cost.
     cannacre8ive/switchboard-ai ≠ ha-switchboard ≠ hermes-switchyard.
     Full cards: `mixed-architecture.md`, `faq.md`.
114. **Frozen-protocol class bake-off** (elcronos/jev-vs-open-decision-models):
     position 8 (Metric). frozen-protocol zero-shot bench.
     TypeSafe Jev vs PrismNLI vs Laya. contamination caveat.
     elcronos/jev-vs-open-decision-models ≠ JevBench ≠ DMB.
     Full cards: `validation.md`, `faq.md`.
115. **VOI admission** (cvsgireesh/jevusher):
     position 3 (Gate) × 6 (VOI gather). context-window admission
     control. VOI gate which tokens are worth the expensive model.
     fail polarity per lens. on small inputs lenses lose money.
     cvsgireesh/jevusher ≠ jev-sift ≠ winnow.
     Full cards: `applied-mappings.md`, `faq.md`.
116. **Typed decision control plane** (MokiMeow/jev-fabric):
     positions 3 (Gate) × 11 (Bounds). typed decision control plane.
     receipt ≠ authorization. historical-v0 zero retained cases.
     MokiMeow/jev-fabric ≠ jev-forge ≠ dgp.
     Full cards: `formal-methods.md`, `faq.md`.
117. **Scoring economics / live MCDA** (jose-troche/live-rubric):
     position 8 (Metric) × fan-out. live 15-dim typed rubric
     re-score per pause. scoring economics exemplar.
     OpenJev/Codiv ≠ TypeSafe hosted.
     jose-troche/live-rubric ~$0.000004 desc / ~$0.000006 README.
     Full cards: `judgment-class.md`, `faq.md`.
118. **Pre-registered calibration science** (willkelly/jev-evaluation):
     position 8 (Metric) as Harbor-jevals practice. adversarial
     pre-registered Jev eval. 28 predictions before data.
     123,805 requests. confidence does not track ignorance.
     polite injection 65% / crude 0%.
     willkelly/jev-evaluation ≠ jevals ≠ jev-baselines-eval.
     Full cards: `validation.md`, `faq.md`.
119. **Class infrastructure SDK** (nshkrdotcom/system_one_sdk):
     position 1 (Operand) as unofficial client, not a species.
     provider-neutral Elixir/BEAM Noul/Choice/Score SDK.
     class infrastructure.
     nshkrdotcom/system_one_sdk ≠ typesafe_sdk ≠ dannote/jev.
     Full cards: `judgment-class.md`, `faq.md`.

Hourly 2041 items 111–119 (`notes.md` §101). Do **not**
re-fold 1943 items 102–110 / 1843 items 97–101 / 1740
items 94–96 / SIGNAL §93 mechanism. Soft Noul ≠ hard
safety.

question-linting of Jev questions themselves; nine jaggedness rules, no API key, no labelled data; static lint ≠ measured separation; yodablocks/jevq ≠ tenbin ≠ JevLint ≠ commitjev; open-weights Laya as class exemplar (binding); Nx/Bumblebee runtime; host chooses backend; ChristianAlexander/laya_ex ≠ system_one_sdk ≠ dannote/jev ≠ NandhaKishorM/laya; on-chain/edge Laya deploy; parity_verified stays false; model output never grants Tx; humandebri/IC-Laya ≠ laya_ex; auditable weekend replica; Jev outputs never used for training; soft human-vote distributions; unpaired 0.577 vs 0.727; agilabs-ai/jev48 ≠ JevBench ≠ Mapika/decider; adversarial dual-judge / framing attack surface; comparative framing is the usable judgment; prior injection crowds out evidence; copyleftdev/ember ≠ ember.js; Laya specialist fine-tune pipeline; training still GPU-pending; PIXELZX0/XERON ≠ convaiinnovations/laya; Hub Laya replica drop; daliborsb/laya ≠ convaiinnovations/laya ≠ NandhaKishorM/laya; System One student distillation corpus; gold is programmatic; teacher is closed-API clone; do not distill Jev as teacher of record; MagaBitmex/jev-4b-distill-data ≠ missing student checkpoint; non-LLM VIN System One; planning depth not chat; lewislululu/jevon ≠ douglance/jevon; source-bound evidence checks; local quote mismatch needs no API; exit 0 ≠ claim truth; WaynezProg/jev-kit ≠ jonathanavis96/jev-kit (Airlock) ≠ jev-use ≠ jev-mcp

120. **Question-lint of the question text** (yodablocks/jevq; PRIMARY):
     position 9 (Verifier) as static checker, not a System One.
     nine jaggedness rules, no API key, no labelled data.
     static lint ≠ measured separation.
     yodablocks/jevq ≠ tenbin ≠ JevLint ≠ commitjev.
     Full cards: `question-design.md`, `faq.md`.
121. **Open Laya BEAM binding** (ChristianAlexander/laya_ex):
     position 1 (Operand) as unofficial class head, not a species.
     open-weights Laya as class exemplar (binding).
     Nx/Bumblebee runtime. host chooses backend.
     ChristianAlexander/laya_ex ≠ system_one_sdk ≠ dannote/jev ≠
     NandhaKishorM/laya.
     Full cards: `judgment-class.md`, `faq.md`.
122. **On-chain/edge Laya deploy** (humandebri/IC-Laya):
     positions 3 (Gate) × 11 (Bounds). model output never grants Tx.
     parity_verified stays false.
     humandebri/IC-Laya ≠ laya_ex.
     Full cards: `formal-methods.md`, `faq.md`.
123. **Auditable weekend replica** (agilabs-ai/jev48):
     position 8 (Metric) as unpaired public aggregates.
     Jev outputs never used for training. unpaired 0.577 vs 0.727.
     agilabs-ai/jev48 ≠ JevBench ≠ Mapika/decider.
     Full cards: `validation.md`, `faq.md`.
124. **Adversarial dual-judge / framing** (copyleftdev/ember):
     positions 5 (Comparator) × 9 (Verifier). comparative framing
     is the usable judgment. prior injection crowds out evidence.
     copyleftdev/ember ≠ ember.js.
     Full cards: `question-design.md`, `faq.md`.
125. **Laya specialist FT + Hub replica** (PIXELZX0/XERON; daliborsb/laya):
     position 1 (Operand) densifies the open head. training still
     GPU-pending. Hub Laya replica drop.
     PIXELZX0/XERON ≠ convaiinnovations/laya.
     daliborsb/laya ≠ convaiinnovations/laya ≠ NandhaKishorM/laya.
     Full cards: `judgment-class.md`, `faq.md`.
126. **Student distillation corpus** (MagaBitmex/jev-4b-distill-data):
     position 8 (Metric) as training-data VOI. gold is programmatic.
     teacher is closed-API clone. do not distill Jev as teacher of record.
     MagaBitmex/jev-4b-distill-data ≠ missing student checkpoint.
     Full cards: `toolbox-mapping.md`, `faq.md`.
127. **Non-LLM VIN System One** (lewislululu/jevon):
     position 4 (Selector of F) on a grid, not chat.
     planning depth not chat.
     lewislululu/jevon ≠ douglance/jevon.
     Full cards: `judgment-class.md`, `faq.md`.
128. **Source-bound evidence + bounded judgments** (WaynezProg/jev-kit):
     positions 9 (Verifier) × 2 (exact quote match). local quote
     mismatch needs no API. exit 0 ≠ claim truth.
     WaynezProg/jev-kit ≠ jonathanavis96/jev-kit (Airlock) ≠ jev-use ≠ jev-mcp.
     Full cards: `applied-mappings.md`, `faq.md`.

Hourly 2145 items 120–128 (`notes.md` §102). Do **not**
re-fold 2041 items 111–119 / 1943 items 102–110 / 1843
items 97–101 / 1740 items 94–96 / SIGNAL §93 mechanism.
Soft Noul ≠ hard safety.

independent System One evidence catalog; 19 reviewed records; scores not one leaderboard; no external record currently reproduced; TokenTrim no-Jev matched hybrid 62.4%; reachjalil/system-one-bench ≠ mallahyari/system-one-benchmark; 21 tasks · 134 items · 208 questions; scenes from public GitHub contracts, not production logs; SivletLabs/jev-eval ≠ willkelly/jev-evaluation ≠ 4esv/jev-eval ≠ xxkuboxx/jev-eval ≠ onlyoneaman/jev-eval ≠ dayhaysoos/jevals; option isolation (sibling-blind); permutation-equivariant; Hub OWNER not published; nafisazizir/hev ≠ jaredpalmer/kev; frozen local LLM logits, no trained decision head; residual-head 9,222-param decreased 73/96→67/96; confidence = 1−normalized entropy, not P(correct); yuki-oshio/mini-jev ≠ r-ms/mini-jev; Jev classifier as autoregressive next-token predictor; ChatJev-style soundness theater; erik-dunteman/ChatJev ≠ dannote/jev ≠ jev-gpt; calibrated decision head × AlphaProof value head; implementation-layer isomorphism, semantic difference; timeout = censoring; do not launder Noul as proof; parallel rank-prediction vs serial selection; independent questions can conflict; zzzzzec/jevsort ≠ keltokhy/jsort; curated open System One ecosystem catalog; rupeshpoojary9/awesome-open-system-one ≠ AnotiaWang/awesome-jev; arXiv paper radar with Jev relevance scoring; ranking ≠ calibration / 0.5 still soft; fail-open failed evals not marked seen

129. **Independent evidence catalog** (reachjalil/system-one-bench; PRIMARY):
     position 8 (Metric) as reviewed receipts, not a leaderboard.
     19 reviewed records.
     scores not one leaderboard.
     no external record currently reproduced.
     TokenTrim no-Jev matched hybrid 62.4%.
     reachjalil/system-one-bench ≠ mallahyari/system-one-benchmark.
     Full cards: `validation.md`, `faq.md`.
130. **Typed eval freeze** (SivletLabs/jev-eval):
     position 8 (Metric) as Harbor-jevals practice, not Harbor.
     21 tasks · 134 items · 208 questions.
     scenes from public GitHub contracts, not production logs.
     SivletLabs/jev-eval ≠ willkelly/jev-evaluation ≠ 4esv/jev-eval ≠ xxkuboxx/jev-eval ≠ onlyoneaman/jev-eval ≠ dayhaysoos/jevals.
     Full cards: `validation.md`, `faq.md`.
131. **Option-isolated tiny replica** (nafisazizir/hev):
     position 1 (Operand) as trained decision-only open path.
     option isolation (sibling-blind). permutation-equivariant.
     Hub OWNER not published.
     nafisazizir/hev ≠ jaredpalmer/kev.
     Full cards: `judgment-class.md`, `faq.md`.
132. **Frozen-LLM typed decisions** (yuki-oshio/mini-jev):
     position 1 (Operand) as logit-read, not a trained head.
     frozen local LLM logits, no trained decision head.
     residual-head 9,222-param decreased 73/96→67/96.
     confidence = 1−normalized entropy, not P(correct).
     yuki-oshio/mini-jev ≠ r-ms/mini-jev.
     Full cards: `judgment-class.md`, `faq.md`.
133. **AR next-token anti-pattern** (erik-dunteman/ChatJev):
     do **not** occupy generation. Jev classifier as autoregressive
     next-token predictor. ChatJev-style soundness theater.
     erik-dunteman/ChatJev ≠ dannote/jev ≠ jev-gpt.
     Full cards: `mixed-architecture.md`, `faq.md`.
134. **Formal compose with scoring** (wufuju2023-cell/jev-alpha-proof-analysis):
     positions 3 (Gate) × 11 (Bounds) × searchlight. calibrated
     decision head × AlphaProof value head. implementation-layer
     isomorphism, semantic difference. timeout = censoring.
     do not launder Noul as proof.
     Full cards: `formal-methods.md`, `faq.md`.
135. **Parallel rank vs serial selection** (zzzzzec/jevsort):
     position 5 (Comparator) as algorithmic scoring mental model.
     parallel rank-prediction vs serial selection.
     independent questions can conflict.
     zzzzzec/jevsort ≠ keltokhy/jsort.
     Full cards: `mental-models.md`, `faq.md`.
136. **Open-side ecosystem catalog** (rupeshpoojary9/awesome-open-system-one):
     position 1 (Operand) as class map, not a species.
     curated open System One ecosystem catalog.
     rupeshpoojary9/awesome-open-system-one ≠ AnotiaWang/awesome-jev.
     Full cards: `judgment-class.md`, `faq.md`.
137. **Knowledge-work paper radar** (LYchoon/paper-radar-jev):
     position 4 (Selector of F) as relevance ranking.
     arXiv paper radar with Jev relevance scoring.
     ranking ≠ calibration / 0.5 still soft.
     fail-open failed evals not marked seen.
     Full cards: `applied-mappings.md`, `faq.md`.

Hourly 2246 items 129–137 (`notes.md` §103). Do **not**
re-fold 2145 items 120–128 / 2041 items 111–119 / 1943
items 102–110 / 1843 items 97–101 / 1740 items 94–96 /
SIGNAL §93 mechanism.
Soft Noul ≠ hard safety.

train calibrated ~27M from scratch; typed Q→prob dist / one forward pass / no LLM decode; hyusi2003/MiniSystemOne ≠ Colvin0315/MiniSystemOne; description-only stub / size 5; ESCI hard probe fails four of six; jev_bool ECE 0.242 inversion 0.255; do not re-fold §60 six-gates as new; jobbyjev one-request-per-company from batch-size result; find/design/evaluate TypeSafe Jev decision loops; karanb192/jev-architect ≠ samtay32/jev-system-architect; Jairik/jev-distiller size 1; distill-Jev UI stub / do not distill Jev as teacher of record; post-launch scored use-case map / Jev self-scores then human curation; licensedsaucer9-web/jev-opportunities; Jev-inize a use case into classifier/router; gavinHuang/jevinize → simple-jev not TypeSafe; featherless-ai/simple-jev; compare saved decisions / same label can still change the branch; VihaanAgarwal/jev-diff ≠ Saik0s/diffusiongemma-jev-macos; not tested with a live Jev API key; constrained logprob + temp/Platt ≠ Noul; OpenJevPro pastes openjev-sglang JevBench as own; zhangcy122/OpenJevPro ≠ IamBusy/OpenJev ≠ ekzhang/openjev-sglang; PolyForm Noncommercial; SmolLM-135M / sub-70ms / 0 output tokens; demo P(True) 0.5052 / Choice conf 0.2872 / Score conf 0.0055; README claims MIT / GitHub license null / no LICENSE file; patelvishwa112/jev-system-one-rlcd ≠ arnabgho/rlcd-lite ≠ blackwood-rlcd; source-backed Awesome Jev radar / 306+ commit-pinned; logicrw/awesome-jev-projects ≠ AnotiaWang/awesome-jev ≠ yibie/awesome-jev ≠ cobanov/awesome-jev ≠ rupeshpoojary9/awesome-open-system-one; auto GitHub sync / Issue-only submissions; hashed n-gram encoder / rival-aware attention; olanotolu/jevbetter vs jevlike starter; synthetic hard menus top-1 0.916 vs 0.873 / ECE 0.0182 vs 0.0367 / 40 vs 4608 menus/sec; shuffled-context control 0.335

138. **From-scratch calibrated decision model** (hyusi2003/MiniSystemOne; PRIMARY):
     position 1 (Operand) as trained decision-only open path, not LoRA-on-LLM.
     train calibrated ~27M from scratch.
     typed Q→prob dist / one forward pass / no LLM decode.
     hyusi2003/MiniSystemOne ≠ Colvin0315/MiniSystemOne.
     description-only stub / size 5.
     Full cards: `judgment-class.md`, `faq.md`.
139. **ORDER BY ranking upgrade** (yodablocks/jev-orderby-bench ESCI):
     position 5 (Comparator) as ranking, not a frequency.
     ESCI hard probe fails four of six.
     jev_bool ECE 0.242 inversion 0.255.
     do not re-fold §60 six-gates as new.
     Full cards: `validation.md`, `faq.md`.
140. **Find/design/evaluate decision loops** (karanb192/jev-architect):
     position 8 (Metric) as workflow inspection before the API.
     find/design/evaluate TypeSafe Jev decision loops.
     karanb192/jev-architect ≠ samtay32/jev-system-architect.
     Full cards: `mixed-architecture.md`, `faq.md`.
141. **Distill-Jev UI stub** (Jairik/jev-distiller):
     do **not** occupy teacher-copy. Jairik/jev-distiller size 1.
     distill-Jev UI stub / do not distill Jev as teacher of record.
     Full cards: `mixed-architecture.md`, `faq.md`.
142. **Post-launch scored opportunity map** (licensedsaucer9-web/jev-opportunities):
     position 4 (Selector of F) then a human ranks TOP.
     post-launch scored use-case map / Jev self-scores then human curation.
     Full cards: `applied-mappings.md`, `faq.md`.
143. **Jev-inize a use case** (gavinHuang/jevinize):
     position 1 (Operand) as a scaffold against an open classifier server.
     Jev-inize a use case into classifier/router.
     gavinHuang/jevinize → simple-jev not TypeSafe.
     Full cards: `applied-mappings.md`, `faq.md`.
144. **Saved-decision regression** (VihaanAgarwal/jev-diff):
     position 8 (Metric) as an instrument, not a score.
     compare saved decisions / same label can still change the branch.
     not tested with a live Jev API key.
     Full cards: `validation.md`, `faq.md`.
145. **Constrained-logprob production API** (zhangcy122/OpenJevPro):
     do **not** occupy Noul. constrained logprob + temp/Platt ≠ Noul.
     OpenJevPro pastes openjev-sglang JevBench as own. PolyForm Noncommercial.
     Full cards: `judgment-class.md`, `faq.md`.
146. **SmolLM RLCD reproduction** (patelvishwa112/jev-system-one-rlcd):
     position 1 (Operand) as NAR heads on a tiny decoder.
     SmolLM-135M / sub-70ms / 0 output tokens.
     demo P(True) 0.5052 / Choice conf 0.2872 / Score conf 0.0055.
     Full cards: `judgment-class.md`, `faq.md`.
147. **Source-backed Awesome radar** (logicrw/awesome-jev-projects):
     position 1 (Operand) as class map, not a bake-off.
     source-backed Awesome Jev radar / 306+ commit-pinned.
     auto GitHub sync / Issue-only submissions.
     Full cards: `judgment-class.md`, `faq.md`.
148. **Rival-aware one-pass scorer** (olanotolu/jevbetter):
     position 1 (Operand) as rival-aware vs sibling-blind.
     hashed n-gram encoder / rival-aware attention.
     olanotolu/jevbetter vs jevlike starter.
     shuffled-context control 0.335.
     Full cards: `judgment-class.md`, `faq.md`.

Hourly 2340 items 138–148 (`notes.md` §104). Do **not**
re-fold 2246 items 129–137 / 2145 items 120–128 / 2041
items 111–119 / 1943 items 102–110 / 1843 items 97–101 /
1740 items 94–96 / SIGNAL §93 mechanism / §60 six-gates.
Soft Noul ≠ hard safety.

structured probability readouts; distribution > argmax; Noul 0.5 midpoint; score is expectation not integer; bare HTTP not SDK; Arohtea/jev-readout; Jev-style Choice/Score/Noul from ordinary models; optional DSH plugin; schema-valid ≠ calibrated; gulagala001/jevify ≠ Mintzs/jevify; Laya RLCD benchmark; 40.3% below constant-answer; open-weight measurement; mourad-ghafiri/laya-rlcd-benchmark ≠ yibie/laya-jev-lab; cheap fail-open semantic edge; second signal not sole; FastLoopError catch; SupremeDreamZ/jev-fastloop ≠ jev-ultrafast; asking more questions in one call; 0.980 at every N; nearly not fully deterministic; TheWebDevel/jev-fanout; Qwen3-VL perception + Jev decisions train RL; 0 model calls at deployment; VLM alone 1.7 vs +Jev 4.4; harneet2512/reflexrl ≠ khordoo/jev-reflex-autonomy-lab; independent Jev API vs Laya; cascade 0.60 matches 78% at 1.8×; noul facts not judgements; yibie/laya-jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab; GLiNER vs GLiFormer vs Laya vs Jev; extractors ≠ decision engines; Laya dict-instructions collapse 58.3%; umstek/zero-shot-ie-bench; decisions-per-minute & cost; 204 moves vs 73; throughput not intelligence; angelgalvisc/snake-arena-jev-vs-llms ≠ vtrivedy/jev-plays-games; behavioral contracts; pin expectations eval upgrades; raw 0.94 is not a release; sathariels/jevcheck ≠ dayhaysoos/jevals ≠ SivletLabs/jev-eval; evidence-linked dependency upgrade; Jev never generates filenames; no_direct_evidence ≠ safe to merge; GaneshVG18/upgrade-radar ≠ LYchoon/paper-radar-jev; discography theme/mood/complexity; five atomic questions one call; lirantal/discoprint

149. **Structured probability readouts** (Arohtea/jev-readout; PRIMARY):
     position 8 (Metric) as the displayed distribution, not the argmax.
     structured probability readouts.
     distribution > argmax.
     Noul 0.5 midpoint.
     score is expectation not integer.
     bare HTTP not SDK.
     Full cards: `mental-models.md`, `faq.md`.
150. **Ordinary-model Jev-shape** (gulagala001/jevify):
     position 1 (Operand) as adapter, not a replica.
     Jev-style Choice/Score/Noul from ordinary models.
     optional DSH plugin.
     schema-valid ≠ calibrated.
     gulagala001/jevify ≠ Mintzs/jevify.
     Full cards: `judgment-class.md`, `faq.md`.
151. **Open-weight Laya measurement** (mourad-ghafiri/laya-rlcd-benchmark):
     position 8 (Metric) vs a constant-answer baseline.
     Laya RLCD benchmark.
     40.3% below constant-answer.
     open-weight measurement.
     mourad-ghafiri/laya-rlcd-benchmark ≠ yibie/laya-jev-lab.
     Full cards: `validation.md`, `faq.md`.
152. **Cheap fail-open semantic edge** (SupremeDreamZ/jev-fastloop):
     positions 4 (Selector of F) × 3 (Gate, fail-open).
     cheap fail-open semantic edge.
     second signal not sole.
     FastLoopError catch.
     SupremeDreamZ/jev-fastloop ≠ jev-ultrafast.
     Full cards: `mixed-architecture.md`, `faq.md`.
153. **Fan-out measurement** (TheWebDevel/jev-fanout):
     position 8 (Metric) on packed parallel questions.
     asking more questions in one call.
     0.980 at every N.
     nearly not fully deterministic.
     TheWebDevel/jev-fanout.
     Full cards: `question-design.md`, `faq.md`.
154. **VLM+Jev RL teacher** (harneet2512/reflexrl):
     positions 6 (Advisor of F) × 10 (Teacher, then steps aside).
     Qwen3-VL perception + Jev decisions train RL.
     0 model calls at deployment.
     VLM alone 1.7 vs +Jev 4.4.
     harneet2512/reflexrl ≠ khordoo/jev-reflex-autonomy-lab.
     Full cards: `mixed-architecture.md`, `faq.md`.
155. **Independent Jev API vs Laya** (yibie/laya-jev-lab):
     positions 4 (Selector) × 8 (Metric) as local-first cascade.
     independent Jev API vs Laya.
     cascade 0.60 matches 78% at 1.8×.
     noul facts not judgements.
     yibie/laya-jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab.
     Full cards: `validation.md`, `faq.md`.
156. **Locate vs decide** (umstek/zero-shot-ie-bench):
     position 1 (Operand) as species map, not a bake-off win.
     GLiNER vs GLiFormer vs Laya vs Jev.
     extractors ≠ decision engines.
     Laya dict-instructions collapse 58.3%.
     umstek/zero-shot-ie-bench.
     Full cards: `judgment-class.md`, `faq.md`.
157. **Throughput arena** (angelgalvisc/snake-arena-jev-vs-llms):
     position 8 (Metric) as decisions-per-minute, not intelligence.
     decisions-per-minute & cost.
     204 moves vs 73.
     throughput not intelligence.
     angelgalvisc/snake-arena-jev-vs-llms ≠ vtrivedy/jev-plays-games.
     Full cards: `validation.md`, `faq.md`.
158. **Behavioral contracts** (sathariels/jevcheck):
     position 9 (Verifier) as pin-then-eval.
     behavioral contracts.
     pin expectations eval upgrades.
     raw 0.94 is not a release.
     sathariels/jevcheck ≠ dayhaysoos/jevals ≠ SivletLabs/jev-eval.
     Full cards: `validation.md`, `faq.md`.
159. **Evidence-linked upgrade review** (GaneshVG18/upgrade-radar):
     positions 2 (exact spans) × 9 (Verifier); Jev remainder only.
     evidence-linked dependency upgrade.
     Jev never generates filenames.
     no_direct_evidence ≠ safe to merge.
     GaneshVG18/upgrade-radar ≠ LYchoon/paper-radar-jev.
     Full cards: `applied-mappings.md`, `faq.md`.
160. **Knowledge-work discography** (lirantal/discoprint):
     position 4 (Selector of F) as theme/mood/complexity.
     discography theme/mood/complexity.
     five atomic questions one call.
     lirantal/discoprint.
     Full cards: `applied-mappings.md`, `faq.md`.

Hourly 0042 items 149–160 (`notes.md` §105). Do **not**
re-fold 2340 items 138–148 / 2246 items 129–137 / 2145
items 120–128 / 2041 items 111–119 / 1943 items 102–110 /
1843 items 97–101 / 1740 items 94–96 / SIGNAL §93
mechanism. Do **not** merge from merged **#22**.
Soft Noul ≠ hard safety.
