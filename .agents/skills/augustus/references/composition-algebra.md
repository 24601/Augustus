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
    Full cards: `mappings.md` §4, `faq.md`.
74. **Enterprise reflexes** (400ms-agentic-sf /
    scheduler-diagnostics): categorization leaving
    the IDE. 400ms Salesforce WebMCP.
    typesafe-scheduler-diagnostics advisory. Does
    not place Pods. Full cards: `faq.md`.
75. **Screenshot-free / CU** (droidjev / jevcu):
    position 9. droidjev screenshot-free.
    Tewoto1 jevcu planner still writes. **≠**
    closed-vote. Full cards:
    `applied-mappings.md` §9, `faq.md`.
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
