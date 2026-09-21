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

Turn any open LLM into System-One Jev; uspraveen/Jevify ≠ Mintzs/jevify ≠ gulagala001/jevify; Jevify-any-LLM architecture probe; description-only stub / size 0; Train encoder-only calibrated decision models from a task sentence; Exu is a toolkit, not a method; strictly proper scoring rule; Pre-alpha; Ruivalim/exu-base; scratch-trained calibrated decision model; typed Q → probability dists; Colvin0315/MiniSystemOne ≠ hyusi2003/MiniSystemOne; no published weights download URL; 90.5 seconds / 29.2% pipeline evidence; p_i/p_j independent of other candidates; Recipe for calibrated decision models — small model out; init → synth → train → eval → serve; 91.1 % / ECE 0.022 *theirs*; Jev zero-shot 75.1; scienthoon/luce; Put Jev's three headline claims on trial; 0.5B local GPU; 46x speedup / accuracy identical; ECE 0.624 sentiment catastrophe; bigger model worse calibration; RichardoMrMu/jev-mini ≠ yuki-oshio/mini-jev ≠ r-ms/mini-jev; System-1 decision engine for local LLMs; structured choices only; JSON parse of generated text ≠ Noul; TypefAI JEV / Journal Entry Voucher; tapsin/jev-local ≠ us/jev-local ≠ Argos1111/jev_local; Jev 1.13 reward-model eval across 8 benchmark tracks; 40,940 examples / 0 API errors; RewardBench v1 92.58%; Precise IF 50.63%; goya4140/jev-reward-model-evaluation; Scaffolding in progress; Jev vs LLM support-ticket routing; static + live decision bench; TypeSafe's own published benchmark; illustrative simulations, not live API calls; JevBench v1 — smart/cheap/fast/reliable; I/C/S/K 25% geometric mean; classifier.dev fast tier 84.8 is Jev behind its own API; do not re-fold §78 v1.2 board as new; Laya (421M) 70.1 now on board; Zero-shot/few-shot LLM routing; hard budget filter before Jev; Jev never asked to perform budget arithmetic; Jev judges the next state, XState enforces transitions; simulation uses synthetic keyword fixtures; catalog gravity; v-modal/awesome-jev-tools; ★339 live REST; curation is not endorsement; crawler-maintained directory; Daily GitHub + npm sweep, human-merged; RadRebelSam/awesome-jev ≠ AnotiaWang ≠ yibie ≠ cobanov ≠ logicrw ≠ v-modal; HF peft SPLADE/BGE reranker; rdxtremity/jev-reranking ≠ carlaiau/jev-reranking; query-side encoders, not a Jev replica; ONNX System One Qwen3.5-4B scorer; source:pngwn/system-one-qwen3.5-4b-scorer; CC-BY-NC-4.0; temperature 1.75; transformers.js AutoModel cannot load this graph; Consistency benchmark Space; This Space contains no benchmark result yet; 12-case plumbing fixture; do not reopen or amend PR #23

161. **Jevify-any-LLM architecture probe** (uspraveen/Jevify; PRIMARY):
     position 1 (Operand) as a probe, not a checkpoint.
     Turn any open LLM into System-One Jev.
     uspraveen/Jevify ≠ Mintzs/jevify ≠ gulagala001/jevify.
     description-only stub / size 0.
     Full cards: `judgment-class.md`, `faq.md`.
162. **Encoder-only from a task sentence** (Ruivalim/exu-base):
     position 1 (Operand) as trained decision-only open path.
     Train encoder-only calibrated decision models from a task sentence.
     Exu is a toolkit, not a method. strictly proper scoring rule. Pre-alpha.
     Full cards: `judgment-class.md`, `faq.md`.
163. **Scratch-trained recipe upgrade** (Colvin0315/MiniSystemOne):
     position 1 (Operand) as from-scratch one-pass scorer.
     scratch-trained calibrated decision model. typed Q → probability dists.
     Colvin0315/MiniSystemOne ≠ hyusi2003/MiniSystemOne.
     no published weights download URL. 90.5 seconds / 29.2% pipeline evidence.
     p_i/p_j independent of other candidates.
     Full cards: `judgment-class.md`, `faq.md`.
164. **Recipe small model out** (scienthoon/luce):
     position 1 (Operand) as LoRA + decision head on an open backbone.
     Recipe for calibrated decision models — small model out.
     init → synth → train → eval → serve.
     do not distill Jev as teacher of record.
     Full cards: `judgment-class.md`, `faq.md`.
165. **Headline claims trial** (RichardoMrMu/jev-mini):
     position 8 (Metric) as an instrument, not a score.
     Put Jev's three headline claims on trial. 0.5B local GPU.
     46x speedup / accuracy identical. ECE 0.624 sentiment catastrophe.
     bigger model worse calibration.
     RichardoMrMu/jev-mini ≠ yuki-oshio/mini-jev ≠ r-ms/mini-jev.
     Full cards: `validation.md`, `faq.md`.
166. **Local structured-choice engine** (tapsin/jev-local):
     do **not** occupy Noul. JSON parse of generated text ≠ Noul.
     System-1 decision engine for local LLMs. structured choices only.
     TypefAI JEV / Journal Entry Voucher.
     tapsin/jev-local ≠ us/jev-local ≠ Argos1111/jev_local.
     Full cards: `judgment-class.md`, `faq.md`.
167. **Reward-model 8-track eval** (goya4140/jev-reward-model-evaluation):
     position 8 (Metric) as Harbor-jevals practice, not Harbor.
     Jev 1.13 reward-model eval across 8 benchmark tracks.
     40,940 examples / 0 API errors. RewardBench v1 92.58%. Precise IF 50.63%.
     Full cards: `validation.md`, `faq.md`.
168. **Ticket-router scaffold** (SarathChandraBellam/jev-vs-llm-ticket-router):
     position 8 (Metric) as a hole, not a result.
     Jev vs LLM support-ticket routing. Scaffolding in progress.
     Full cards: `validation.md`, `faq.md`.
169. **Cost bench** (Shilin237/jev-vs-llm-cost):
     position 8 (Metric) as vendor-published economics.
     static + live decision bench. TypeSafe's own published benchmark.
     illustrative simulations, not live API calls.
     Full cards: `applied-mappings.md`, `faq.md`.
170. **JevBench v1.2.3 densify** (fstandhartinger/jevbench):
     position 8 (Metric) as geometric-mean weak-axis pull.
     JevBench v1 — smart/cheap/fast/reliable. I/C/S/K 25% geometric mean.
     classifier.dev fast tier 84.8 is Jev behind its own API.
     do not re-fold §78 v1.2 board as new. Laya (421M) 70.1 now on board.
     Full cards: `validation.md`, `faq.md`.
171. **Budget-in-code then Jev remainder** (AIGNLAI/ReflexRoute):
     positions 3 (Gate) × 11 (Bounds). code proves budget; Jev selects remainder.
     Zero-shot/few-shot LLM routing. hard budget filter before Jev.
     Jev never asked to perform budget arithmetic.
     Full cards: `formal-methods.md`, `faq.md`.
172. **XState proves transitions** (priyankark/jev-state):
     positions 3 (Gate) × 1 (Operand). FSM proves; Jev judges next state.
     Jev judges the next state, XState enforces transitions.
     simulation uses synthetic keyword fixtures.
     Full cards: `formal-methods.md`, `faq.md`.
173. **Catalog gravity** (v-modal/awesome-jev-tools):
     position 1 (Operand) as class map, not a bake-off.
     catalog gravity. v-modal/awesome-jev-tools. ★339 live REST.
     curation is not endorsement.
     Full cards: `judgment-class.md`, `faq.md`.
174. **Crawler-maintained directory** (RadRebelSam/awesome-jev):
     position 1 (Operand) as class map, not a species.
     crawler-maintained directory. Daily GitHub + npm sweep, human-merged.
     RadRebelSam/awesome-jev ≠ AnotiaWang ≠ yibie ≠ cobanov ≠ logicrw ≠ v-modal.
     Full cards: `judgment-class.md`, `faq.md`.
175. **HF peft retrieval port** (rdxtremity/jev-reranking):
     position 4 (Selector of F) as dual-encoder retrieval, not Choice/Score/Noul.
     HF peft SPLADE/BGE reranker. query-side encoders, not a Jev replica.
     rdxtremity/jev-reranking ≠ carlaiau/jev-reranking.
     Full cards: `judgment-class.md`, `faq.md`.
176. **ONNX System One scorer port** (onnx-community/system-one-qwen3.5-4b-scorer-ONNX):
     position 1 (Operand) as community port, not a new species.
     ONNX System One Qwen3.5-4B scorer. source:pngwn/system-one-qwen3.5-4b-scorer.
     CC-BY-NC-4.0. temperature 1.75. transformers.js AutoModel cannot load this graph.
     Full cards: `judgment-class.md`, `faq.md`.
177. **Consistency Space plumbing** (mjyoke1111/jev-consistency-benchmark):
     position 8 (Metric) as a protocol, not a score.
     Consistency benchmark Space. This Space contains no benchmark result yet.
     12-case plumbing fixture.
     Full cards: `validation.md`, `faq.md`.


Benchmark-driven Jev router and judge; cheap alone is not success; Jev does not write, sum prices, or claim accuracy %; Sol 94.2 / Luna 83.9 / Jev path 89.7; 19.2% Sol / 62.3% cost save / 4.5pp miss of 2pp non-inferiority; p50 latency worse than Sol due to routing overhead; erendikmenn/jev-llm-router-benchmark ≠ jev-rag-benchmark ≠ ryantsai/jev-llm-router; Express + node:sqlite; mock and Jev decision engines; previous_ticket_count >= 3 is code; MIN_CONFIDENCE 0.6 still soft; substring false positives; aesaganda/jev-ticket-router ≠ SarathChandraBellam/jev-vs-llm-ticket-router; Universal Figure & Diagram Router; confidence ≥ 0.85 hard-gate is theater; generative AI banned from scientific plots; six visual branches; hoangngochuong24947-gif/jev-figure-router; human-labeled (state, question, label); 166,054 rows / 22 configs; soft_label for human uncertainty; Praveenrajus/jev-bench ≠ fstandhartinger/jevbench; ternary bonsai System One GGUF; openjev's mechanism, Bonsai's weights; Hub does not ship weights; 100/100 easy T/F is not Harbor; label_mass ≠ correctness; stock llama.cpp Q2_0 silently gibberish; NicolaiMTLassen/open-bonzi-jev ≠ NicolaiLassen; transformers.js DeBERTa ONNX; source:com-kotobalabs/open-jev-deberta-v3-large; temperature 1.05; AutoModel from_pretrained works; onnx-community/open-jev-deberta-v3-large-ONNX ≠ system-one-qwen3.5-4b-scorer-ONNX; 107★ densify; GH 151M vs README 149.6M; PR #1 now closed unmerged; do not re-fold §71 claim-audit as a beat; typed decisions, RLCD, confidence-gated routing; structured ≠ correct; mock not live API; 26 tests; wjdjdakf17/jev-study ≠ baekenough/jev-study; do not reopen or amend PR #23 or #24

178. **Benchmark-driven router + judge** (erendikmenn/jev-llm-router-benchmark; PRIMARY):
     positions 3 (Gate) × 8 (Metric) × 11 (Bounds). code owns threshold/fallback/budget; Jev SENSOR.
     Benchmark-driven Jev router and judge. cheap alone is not success.
     Jev does not write, sum prices, or claim accuracy %.
     Sol 94.2 / Luna 83.9 / Jev path 89.7.
     19.2% Sol / 62.3% cost save / 4.5pp miss of 2pp non-inferiority.
     p50 latency worse than Sol due to routing overhead.
     erendikmenn/jev-llm-router-benchmark ≠ jev-rag-benchmark ≠ ryantsai/jev-llm-router.
     Full cards: `formal-methods.md`, `validation.md`, `faq.md`.
179. **Support ticket router** (aesaganda/jev-ticket-router):
     positions 3 (Gate) × 1 (Operand). count>=3 proves in code; 0.6 is a SENSOR.
     Express + node:sqlite. mock and Jev decision engines.
     previous_ticket_count >= 3 is code. MIN_CONFIDENCE 0.6 still soft.
     substring false positives.
     aesaganda/jev-ticket-router ≠ SarathChandraBellam/jev-vs-llm-ticket-router.
     Full cards: `mixed-architecture.md`, `faq.md`.
180. **Universal figure router** (hoangngochuong24947-gif/jev-figure-router):
     positions 3 (Gate) × 11 (Bounds). generative-AI ban is CONSTRAINT; 0.85 FAST_PATH is theater.
     Universal Figure & Diagram Router. confidence ≥ 0.85 hard-gate is theater.
     generative AI banned from scientific plots. six visual branches.
     Full cards: `formal-methods.md`, `faq.md`.
181. **Human-labeled feedstock** (Praveenrajus/jev-bench):
     position 8 (Metric) as labeled triples, not a board.
     human-labeled (state, question, label). 166,054 rows / 22 configs.
     soft_label for human uncertainty.
     Praveenrajus/jev-bench ≠ fstandhartinger/jevbench.
     Full cards: `validation.md`, `faq.md`.
182. **Ternary bonsai GGUF** (NicolaiMTLassen/open-bonzi-jev):
     position 1 (Operand) as a recipe port, not shipped weights.
     ternary bonsai System One GGUF. openjev's mechanism, Bonsai's weights.
     Hub does not ship weights. 100/100 easy T/F is not Harbor.
     label_mass ≠ correctness. stock llama.cpp Q2_0 silently gibberish.
     NicolaiMTLassen/open-bonzi-jev ≠ NicolaiLassen.
     Full cards: `judgment-class.md`, `faq.md`.
183. **DeBERTa ONNX t.js port** (onnx-community/open-jev-deberta-v3-large-ONNX):
     position 1 (Operand) as a community port of an already-folded encoder.
     transformers.js DeBERTa ONNX. source:com-kotobalabs/open-jev-deberta-v3-large.
     temperature 1.05. AutoModel from_pretrained works.
     onnx-community/open-jev-deberta-v3-large-ONNX ≠ system-one-qwen3.5-4b-scorer-ONNX.
     Full cards: `judgment-class.md`, `faq.md`.
184. **verdict NAR densify** (Heman10x-NGU/openJev-verdict-2.0):
     position 8 (Metric) as claim-audit densify, not a beat.
     107★ densify. GH 151M vs README 149.6M.
     PR #1 now closed unmerged. do not re-fold §71 claim-audit as a beat.
     Full cards: `validation.md`, `faq.md`.
185. **Study notes densify** (wjdjdakf17/jev-study):
     positions 1 (Operand) × 3 (Gate). code consumes p; mock ≠ live API.
     typed decisions, RLCD, confidence-gated routing.
     structured ≠ correct. mock not live API. 26 tests.
     wjdjdakf17/jev-study ≠ baekenough/jev-study.
     Full cards: `mental-models.md`, `faq.md`.


bonzi-27b-v2 / ternary-8b / 27b-v1 GGUF family densify; Hub still does not ship weights; WANLI-256 74.6% / 65.2% / 71.1% *theirs*; Bonsai 1 27B Q1_0 runs on stock llama.cpp; ternary still needs PrismML fork; hf:heman10x/openJev-verdict-2.0 twin tokenizer-only; OpenJev Vision image classification + uncertainty; CLEVR-4 held-out joint 0%; hfdataset:IamBusy/OpenJev-Vision-Research-v0.1 12,832; 294,912 derived targets not independent samples; Laya multilingual ONNX WebGPU typed-decisions port; 63/63 selected answers / 5.1e-4 CPU / 1.2e-2 WebGPU; UpHash-Network/mini-jev is yuki-oshio transfer; jev-injection-bench 11,900 labelled prompts; Jev best ranking / Haiku better ECE 0.021 vs 0.058; 0.5–0.9 band is where Jev's numbers do not mean what they say; Prompt wording moves panic 28%; manojlds/jev-dspy-bench ≠ dspachos/jev-dspy ≠ jmanhype/jev-dspy-lab; Jev agreement is similarity, never ground truth; no aggregate quality grade or merge gate; AbstentionBench-on-Jev rank 1 of 20 vs 2025 field; question-asymmetry; forward-looking 0.465 never extreme; openkev calibration layer not a runtime; ECE vs coverage independent; select_threshold returns inf; escalation catches uncertainty not ignorance; misakaikato/openkev ≠ jaredpalmer/kev; pdf-race Docling→Jev vs Gemini; parser owns the wall clock; 12/12 tie is a tie; titles selected not generated; flopcheck 16 calibrated tweet judgments; mechanical tells in code; ZeroX-01/jev-atlas ≠ Zaious/jev-capability-atlas ≠ gorock007/jev-atlas; catalog not endorsement; Laya calibration lab Gradio MCP; T never changes argmax; confidence ≠ top-label p; easy probe set refused; 40–48 rows too small to ship T; do not reopen or amend PR #23 or #24 or #25; do not reopen or amend PR #23/#24/#25.

186. **Bonsai 27B v2 family card** (NicolaiMTLassen/bonzi-27b-v2-jev):
     position 1 (Operand) as a family measurement card, not shipped weights.
     bonzi-27b-v2 / ternary-8b / 27b-v1 GGUF family densify.
     WANLI-256 74.6% *theirs*. ternary still needs PrismML fork.
     Full cards: `judgment-class.md`, `faq.md`.
187. **Ternary Bonsai 8B family card** (NicolaiMTLassen/bonzi-8b-ternary-v1-jev):
     position 1 (Operand). WANLI-256 65.2% *theirs*. Same PrismML fork.
     Full cards: `judgment-class.md`, `faq.md`.
188. **Bonsai 1 27B family card** (NicolaiMTLassen/bonzi-27b-v1-jev):
     position 1 (Operand). Bonsai 1 27B Q1_0 runs on stock llama.cpp.
     Do **not** collapse into §107 Q2_0 gibberish.
     Full cards: `judgment-class.md`, `faq.md`.
189. **Laya multilingual ONNX WebGPU** (mizchi/laya-multilingual-onnx):
     position 1 (Operand) as an independent port.
     Laya multilingual ONNX WebGPU typed-decisions port.
     63/63 selected answers / 5.1e-4 CPU / 1.2e-2 WebGPU. 63/63 argmax ≠ ECE.
     Full cards: `judgment-class.md`, `faq.md`.
190. **OpenJev Vision** (IamBusy/OpenJev-Vision):
     position 1 (Operand) × 8 (Metric). perceive species, not TypeSafe Jev.
     OpenJev Vision image classification + uncertainty. CLEVR-4 held-out joint 0%.
     Full cards: `judgment-class.md`, `validation.md`.
191. **HF verdict twin** (heman10x/openJev-verdict-2.0):
     position 8 (Metric) as tokenizer-only twin, not a beat.
     hf:heman10x/openJev-verdict-2.0 twin tokenizer-only.
     Full cards: `validation.md`, `faq.md`.
192. **Vision research dataset** (IamBusy/OpenJev-Vision-Research-v0.1):
     position 8 (Metric) as feedstock, not independent samples.
     hfdataset:IamBusy/OpenJev-Vision-Research-v0.1 12,832.
     294,912 derived targets not independent samples.
     Full cards: `validation.md`, `faq.md`.
193. **mini-jev residual-head densify** (UpHash-Network/mini-jev):
     position 1 (Operand). UpHash-Network/mini-jev is yuki-oshio transfer.
     residual-head 9,222-param decreased 73/96→67/96.
     Full cards: `judgment-class.md`, `faq.md`.
194. **Prompt-injection ranking vs calibration** (ASEVlad/jev-injection-bench; PRIMARY):
     positions 3 (Gate) × 8 (Metric). ranking ≠ calibration.
     jev-injection-bench 11,900 labelled prompts.
     Jev best ranking / Haiku better ECE 0.021 vs 0.058.
     0.5–0.9 band is where Jev's numbers do not mean what they say.
     Prompt wording moves panic 28%.
     Full cards: `formal-methods.md`, `validation.md`, `faq.md`.
195. **Jev vs DSPy quality-evaluator** (manojlds/jev-dspy-bench):
     position 8 (Metric) as similarity, never GT.
     manojlds/jev-dspy-bench ≠ dspachos/jev-dspy ≠ jmanhype/jev-dspy-lab.
     Jev agreement is similarity, never ground truth.
     no aggregate quality grade or merge gate.
     Full cards: `validation.md`, `faq.md`.
196. **AbstentionBench-on-Jev** (sshariqali/jev-abstentionbench):
     positions 3 (Gate) × 8 (Metric). question-asymmetry.
     AbstentionBench-on-Jev rank 1 of 20 vs 2025 field.
     forward-looking 0.465 never extreme.
     Full cards: `mental-models.md`, `validation.md`.
197. **openkev calibration layer** (misakaikato/openkev):
     position 8 (Metric) as a layer, not a runtime.
     openkev calibration layer not a runtime.
     ECE vs coverage independent. select_threshold returns inf.
     escalation catches uncertainty not ignorance.
     misakaikato/openkev ≠ jaredpalmer/kev.
     Full cards: `validation.md`, `formal-methods.md`.
198. **Docling→Jev vs Gemini race** (goodrahstar/pdf-race):
     positions 1 (Operand) × 8 (Metric) × 11 (Bounds).
     parser owns the wall clock; titles selected not generated.
     pdf-race Docling→Jev vs Gemini. 12/12 tie is a tie.
     Full cards: `formal-methods.md`, `faq.md`.
199. **Public TypeSafe JEV index** (ZeroX-01/jev-atlas):
     position 8 (Metric) as a catalog, not eval.
     ZeroX-01/jev-atlas ≠ Zaious/jev-capability-atlas ≠ gorock007/jev-atlas.
     catalog not endorsement.
     Full cards: `faq.md`.
200. **flopcheck tweet judgments** (samyakjain0606/jev-is-here):
     positions 1 (Operand) × 3 (Gate). mechanical tells in code.
     flopcheck 16 calibrated tweet judgments. Knowledge work / life.
     Full cards: `mental-models.md`, `faq.md`.
201. **Laya calibration lab** (BunsDev/laya-calibration-lab):
     position 8 (Metric). T never changes argmax.
     Laya calibration lab Gradio MCP. confidence ≠ top-label p.
     easy probe set refused. 40–48 rows too small to ship T.
     Full cards: `validation.md`, `faq.md`.

202. **Gemma-4 26B-A4B jevify** (hf:kushalpatil/jevify-gemma4-26b-a4b):
     positions 1 (Operand) × 8 (Metric). Gemma-4 26B-A4B jevify classification+calibration.
     Hub jevify merged LoRA ships weights.
     PAWS 0.580/ece 0.288 is the weak cell.
     kushalpatil/jevify-gemma4 ≠ Mintzs/jevify ≠ gulagala001/jevify ≠ uspraveen/Jevify.
     GH kushalpatil07/jevify 404.
     Full cards: `judgment-class.md`, `validation.md`, `faq.md`.
203. **26B-A4B LoRA twin** (hf:kushalpatil/jevify-gemma4-26b-a4b-lora):
     position 1 (Operand). LoRA adapter twin not independent eval.
     Full cards: `faq.md`.
204. **Gemma-4 E4B jevify** (hf:kushalpatil/jevify-gemma4-e4b):
     positions 1 (Operand) × 8 (Metric).
     smaller E4B slightly better OOD ECE than 26B-A4B.
     Full cards: `validation.md`, `faq.md`.
205. **E4B LoRA stub** (hf:kushalpatil/jevify-gemma4-e4b-lora):
     position 1 (Operand). E4B LoRA stub card.
     Full cards: `faq.md`.
206. **Bonsai-8B v1** (hf:NicolaiMTLassen/bonzi-8b-v1-jev):
     position 1 (Operand). bonzi Bonsai-8B v1 GGUF densify.
     WANLI-256 64.5% *theirs*. rank #4 of 6.
     Full cards: `validation.md`, `faq.md`.
207. **Bonsai-1.7B v1** (hf:NicolaiMTLassen/bonzi-1.7b-v1-jev):
     position 1 (Operand). Bonsai-1.7B v1. WANLI-256 52.0% *theirs*.
     Full cards: `validation.md`.
208. **Bonsai-4B v1** (hf:NicolaiMTLassen/bonzi-4b-v1-jev):
     position 1 (Operand). Bonsai-4B v1. WANLI-256 60.2% *theirs*.
     Full cards: `validation.md`.
209. **JulesHuisman scaffolding** (JulesHuisman/jev-eval):
     position 8 (Metric) as scaffolding, not a board.
     JulesHuisman/jev-eval scaffolding / README SHA c356a584 (was empty e69de29b).
     JulesHuisman/jev-eval ≠ SivletLabs/jev-eval ≠ willkelly/jev-evaluation ≠ 4esv ≠ xxkuboxx ≠ onlyoneaman ≠ dayhaysoos/jevals.
     Full cards: `faq.md`.
210. **Table-tennis typed paddle** (LiuHao-1443/jev-table-tennis):
     positions 1 (Operand) × 11 (Bounds). physics local; option label IS the pixel.
     7 bands 6/10 vs 40 bands 0/10. Knowledge work / play.
     Full cards: `mental-models.md`, `faq.md`.
211. **Evidence lab receipts** (laguagu/jev-evidence-lab):
     positions 3 (Gate) × 8 (Metric). 0.8 still soft.
     source receipts + confidence slider re-policy without re-inference.
     32/32 synthetic is smoke not production.
     Full cards: `formal-methods.md`, `faq.md`.
212. **HF dataset typed classify** (hemanth/hfjev):
     position 1 (Operand). classify HF datasets across typed semantic dimensions.
     Full cards: `faq.md`.
213. **ultra_laya REVIEW fork** (roadius2/ultra_laya):
     position 1 (Operand). roadus2 watch misspelling; lock roadius2/ultra_laya.
     ultra_laya REVIEW defects. default branch claude/laya-jev-review-gg5ppo.
     Full cards: `judgment-class.md`, `faq.md`.
214. **RU calibration audit** (AHTOOOXA/jev-cyrillic-audit; PRIMARY):
     positions 3 (Gate) × 8 (Metric). language OOD.
     XNLI EN 88.3% ECE 0.032 → RU 77.3% ECE 0.096.
     Δ −11.0 pp [−14.2,−7.8]; ECE +0.063.
     MASSIVE no detectable difference at n=600.
     confidence is function of p_max (r=1.000).
     Full cards: `formal-methods.md`, `validation.md`, `faq.md`.
215. **Pointer-not-generator “LLM”** (akash-kamat/jev-llm):
     positions 1 (Operand) × 11 (Bounds). bank of replies is exact.
     pointer-not-generator 400 human-authored responses.
     Full cards: `mixed-architecture.md`, `faq.md`.
216. **Evidence-backed KG** (chenmingtang830/jevgraph):
     positions 3 (Gate) × 11 (Bounds). proposed ≠ authorized.
     FewRel 160: Jev 85.0% vs lexical 13.125%.
     gated 100% (95/95) coverage 59.375%.
     Full cards: `formal-methods.md`, `faq.md`.
217. **J++ composition language** (Towow-ai/jpp):
     position 1 (Operand) as a language, not a vendor.
     J++ composable semantic computation language.
     Full cards: `composition-algebra.md`, `faq.md`.
218. **judge-jev Worker** (Mishkun/judge-jev):
     position 3 (Gate). judge-jev 0.5 still soft.
     Full cards: `faq.md`.
219. **what-is-jev rubric census** (tunahansahin897/what-is-jev):
     position 8 (Metric) as a rubric, not a board.
     947 repos scored; A 273 / B 302 / C 372. LLM rubric ≠ benches.
     Full cards: `faq.md`.
220. **Use-case gallery** (whyashthakker/awesome-jev-use-cases):
     position 8 (Metric) as a catalog, not eval.
     No benchmark winner is claimed.
     Full cards: `faq.md`.
221. **System One guide** (dog-last/awesome-jev):
     positions 1 (Operand) × 8 (Metric). atomize then sense.
     phishing: naive 62.6% vs regex 91.8%; 5-atomic + LR 95.0% *theirs*.
     Full cards: `mental-models.md`, `faq.md`.
222. **AITuber tension** (shinshin86/jev-aituber-tension-sample):
     position 1 (Operand). life/knowledge-work.
     AITuber tension ±15.
     Full cards: `mental-models.md`.
223. **JSON reranker** (shinpr/jev-reranker):
     position 1 (Operand). README npm global; repo is Rust.
     Full cards: `faq.md`.
224. **git-confess** (AHTOOOXA/git-confess):
     positions 1 (Operand) × 11 (Bounds). git-confess code owns counting/blame/ratio.
     httpx exhibit 11% (13/119) *theirs*.
     Full cards: `formal-methods.md`, `faq.md`.
225. **Paper trader honest negative** (waterme7on/jev-paper-trader):
     position 8 (Metric). 90d trend +12.40% vs random +12.75% vs BH +41.71%.
     5m win rate 25%.
     Full cards: `mental-models.md`, `validation.md`, `faq.md`.


226. **Blackwood census densify** (hf:BlackwoodAI/blackwood-rlcd):
     position 1 (Operand). Blackwood tracker ABSENT; likes 2 gated manual.
     Census densify, not landed. Archer still promised_not_landed.
     Full cards: `judgment-class.md`, `faq.md`.
227. **Qwen3-0.6B RLCD** (hf:anthonym21/qwen3-0.6b-rlcd-decision):
     positions 1 (Operand) × 8 (Metric). r = c - p_a.
     ECE 0.021; acc 0.807 vs warmup 0.746. calibration beyond ~500 tokens unmeasured.
     Full cards: `mental-models.md`, `validation.md`, `faq.md`.
228. **Gemma E2B Independent** (hf:larkooo/gemma-e2b-rlcd):
     positions 1 (Operand) × 8 (Metric). Independent primitive.
     11.57s vs 54.10s · 4.67× · 120/128 *theirs*.
     default path is pretrained Gemma probs not trained RLCD head.
     Full cards: `judgment-class.md`, `faq.md`.
229. **Hub JEV-CPU twin** (hf:Meanblock/JEV-CPU):
     position 1 (Operand). GH Meanblock 404; lock leesk212/JEV-CPU.
     softmax over letter slots ≠ Noul.
     Full cards: `faq.md`, `judgment-class.md`.
230. **Mímir LFM openjev** (hf:impacte/mimir-lfm-openjev):
     positions 1 (Operand) × 8 (Metric). WANLI 0.741 vs openjev v2 0.77 *theirs*.
     3-way NLI ≠ Noul.
     Full cards: `validation.md`, `faq.md`.
231. **System One distilled** (hf:shreyanbr/system-one-distilled):
     positions 1 (Operand) × 8 (Metric). priority 0.464 = majority floor.
     banking77 contaminated. raw margins not probabilities.
     do not distill Jev as teacher of record (they distilled Haiku).
     Full cards: `judgment-class.md`, `faq.md`.
232. **System One gold** (hf:shreyanbr/system-one-gold):
     position 1 (Operand). Gold = dataset labels. Teacher-copy vs gold vs zeroshot.
     Full cards: `faq.md`.
233. **System One zeroshot** (hf:shreyanbr/system-one-zeroshot):
     position 1 (Operand). Zeroshot = base NLI.
     Full cards: `faq.md`.
234. **jev-bench ranking ≠ calibration** (Running-Dolphins/jev-bench):
     position 8 (Metric). “0.9 is not one number”. ranking ≠ calibration.
     banking77 0.8–0.9 stated 0.86 actual 0.73 over-confident *theirs*.
     ≠ Praveenrajus/jev-bench ≠ fstandhartinger/jevbench.
     Full cards: `validation.md`, `mental-models.md`, `faq.md`.
235. **jev-measured economics** (WallerChen/jev-measured):
     position 8 (Metric). $0.0000153–$0.0000226 vs circulating $0.0004 (~20×).
     Score is 0..n-1 expectation not 0–1. Noul has no confidence field.
     TCP floor 198.8 ms. type reliability is not a reason to choose Jev (json_schema 5/5).
     gateway tax not one number.
     Full cards: `validation.md`, `formal-methods.md`, `faq.md`.
236. **decision-lab hybrid** (RadRebelSam/jev-decision-lab):
     positions 2 (Filter) × 11 (Bounds). Function-only 5/8 vs hybrid 8/8.
     4/8 without Jev. 8 designed cases not conversion lift.
     ≠ RadRebelSam/awesome-jev.
     Full cards: `mixed-architecture.md`, `faq.md`.
237. **BigQuery 200-row pilot** (jackojacko05/compare-jev-bigquery-ai-functions):
     position 8 (Metric). 200-row pilot Jev 86.5% 173/200 vs Gemini Flash-Lite 86.0% 172/200 vs Pro 87.0% 174/200 *theirs*.
     not a ranking.
     Full cards: `validation.md`, `faq.md`.
238. **NLI Tetris fighting ring** (Trecto34/openjev-fighting-ring):
     position 4 (Selector). NLI Tetris argmax P(entail)−P(contradict).
     Full cards: `applied-mappings.md`, `faq.md`.
239. **情緒測謊器** (joshhu/jevtest):
     positions 3 (Gate) × 8 (Metric). 情緒測謊器. 1q 396ms / 30q 567ms. ±0.03.
     33q $0.000045 vs Gemini ~5× slower ~60× cost *theirs*.
     ≠ realZachi/jevtest. Knowledge work / life.
     Full cards: `mental-models.md`, `faq.md`.
240. **JevBenchmark Space** (hfspace:aahf/JevBenchmark):
     position 8 (Metric). 8-example Jev vs GPT-5.6 Sol ~64× cost 5.4× latency *theirs*.
     synthetic; no inference. ≠ JevBench v1.2 §78.
     Full cards: `validation.md`, `faq.md`.
241. **rhc98 catalog** (rhc98/awesome-jev):
     position 1 (Operand). Judged 3317 / listed 2560. Jev judges, code applies policy.
     catalog ≠ endorsement.
     Full cards: `faq.md`.
242. **APA catalog** (AiPersonacademy/Awesome-jev-use):
     position 1 (Operand). APA “microsecond policy / zero hallucination” overclaim.
     catalog ≠ endorsement.
     Full cards: `faq.md`.
243. **questionator** (erseco/questionator):
     positions 1 (Operand) × 4 (Selector). Client-side quiz; pointer from held docs; scanned-PDF warn.
     CSP only api.typesafe.ai. Knowledge work.
     Full cards: `applied-mappings.md`, `faq.md`.
244. **grill-jev user decides** (grgy078033/grill-jev):
     positions 3 (Gate) × 11 (Bounds). Jev judges / agent reasons / user decides.
     selecting an option is not permission to implement. degraded fallback.
     Full cards: `formal-methods.md`, `faq.md`.
245. **jev-lsp pattern exact** (makefunstuff/jev-lsp):
     positions 2 (Filter) × 3 (Gate). pattern exact, judgement must clear floor.
     no matching pattern → no model call. not a correctness oracle.
     $0.00022 vs chat $0.00306 *theirs*.
     Full cards: `formal-methods.md`, `applied-mappings.md`, `faq.md`.
246. **jev-spec remainder** (nozomi-koborinai/jev-spec):
     positions 3 (Gate) × 9 (Invariant). Spec vs artifact remainder.
     treating 0.85 as 85% / minProbability hard-gate as Harbor.
     Full cards: `formal-methods.md`, `question-design.md`, `faq.md`.
247. **Jev-LLM VERIFY** (202620325-spec/Jev-LLM):
     positions 5 (Gather) × 7 (Policy). VERIFY acquires discriminating evidence, never same-pool confidence-only rescoring.
     fast/full/max are ceilings not sizes. Solar writes, Jev chooses NEXT ACTION.
     Full cards: `mental-models.md`, `formal-methods.md`, `faq.md`.


248. **calibration ≠ alpha** (alakise/calibration-is-not-alpha):
     position 8 (Metric). Calibration is not alpha. NO CURRENT ALPHA CANDIDATE.
     ΔR² approximately +0.00084. Brier 0.2131387. ECE 0.0421875.
     Adding Jev probability to deterministic volatility improved Brier by only 1.4058e-05.
     Full cards: `validation.md`, `mental-models.md`, `faq.md`.
249. **compaction 0.5 theater** (OrMizL/jev-compaction-bench):
     positions 3 (Gate) × 8 (Metric). default 0.5 keeps zero non pinned.
     keepResult median 0.14 to 0.17. keepCall median 0.28 to 0.35.
     usable range is about 0.10 to 0.25. 7.8% to 57.9%.
     judges results it never sees. task-finish eval not built yet. $0.002 per compaction.
     Full cards: `validation.md`, `formal-methods.md`, `faq.md`.
250. **SGR vs native TabFact** (slavadubrov/sgr-judge-bench):
     positions 8 (Metric) × 9 (Verifier). slavadubrov/sgr-judge-bench ≠ slavadubrov/jev-judge-bench.
     Jev 108/120 $0.083 0.34 s. Luna SGR 114/120.
     paired Jev accuracy-difference intervals include zero. not evidence of equivalence.
     GLM SGR 26/120 93 format failures. Terra-planned Jev hybrid 55/120.
     Full cards: `validation.md`, `faq.md`.
251. **atlas replay remainder** (elyashium/atlas-replay-lab):
     positions 2 (Post-judge) × 7 (State estimator). rule-based by default, optionally Jev-backed.
     empty README. missing key cannot break the experience.
     Full cards: `mixed-architecture.md`, `faq.md`.
252. **one-decode softmax ≠ Noul** (siren2345/jev-single-decode):
     position 1 (Operand). prefill plus exactly one decode. softmax over A/B/C ≠ Noul.
     BBQ 9,053/10,000 (90.53%). ECE 0.0890. Mean confidence 0.9943. overconfident.
     score and noul not implemented.
     Full cards: `judgment-class.md`, `validation.md`, `faq.md`.
253. **DGUI flywheel densify** (hf:ctaxnagomi/DGUI_HYPERMEM-JEV):
     position 1 (Operand). DGUI 12 rows (was 6).
     Full cards: `faq.md`.
254. **INSTRUCT densify** (hf:ctaxnagomi/INSTRUCT_JEV):
     position 8 (Metric). INSTRUCT 119 rows likes 2.
     Full cards: `faq.md`.
255. **encode-once Space** (hfspace:pngwn/open-jev):
     positions 1 (Operand) × 8 (Metric). encode the state once, decide everything in parallel.
     0.740 accuracy against a 0.508 majority. ECE 0.047.
     fine-tune's advantage ends where its 384-token training data does.
     Full cards: `judgment-class.md`, `validation.md`, `faq.md`.
256. **jasonkneen Space twin** (hfspace:jasonkneen/open-jev):
     position 1 (Operand). jasonkneen/open-jev ≠ pngwn/open-jev. same sha d41dc3cd.
     Full cards: `faq.md`.
257. **IkerMoel Space densify** (hfspace:IkerMoel/open-alternative-jev):
     position 1 (Operand). Packed one-forward Space of §49.
     Full cards: `faq.md`.
258. **schema-scorer Space densify** (hfspace:mobarmg/jev-schema-scorer):
     position 8 (Metric). Peaked ranking ≠ calibration.
     Full cards: `faq.md`.
259. **jevlogs re-policy** (hfspace:reachjalil/jevlogs-triage-explorer):
     position 3 (Gate). Space does not call Jev. recomputes routing from saved probabilities.
     Full cards: `mixed-architecture.md`, `faq.md`.
260. **financial recorded lab** (IslamBaraka90/jev-typesafe-real-financial-use-cases):
     positions 8 (Metric) × 4 (Selector). Recorded ≠ alpha.
     Full cards: `applied-mappings.md`, `faq.md`.
261. **mailordinal 200-case densify** (Milo318/mailordinal):
     positions 4 (Selector) × 7 (Policy). 200-case Jev 97.0% / 100.0% / 95.0% / MAE 9.22.
     synthetic repository benchmark.
     Full cards: `applied-mappings.md`, `faq.md`.
262. **Pleo2 skills catalog** (Pleo2/awesome-jev-agent-skills):
     position 2 (Post-judge). Jev evaluations are advisory. catalog ≠ endorsement.
     Full cards: `faq.md`.
263. **nlgrep meaning-search** (YehuiTang0316/jev-nlgrep):
     position 5 (Comparator). YehuiTang0316/jev-nlgrep ≠ Bentlybro/jevgrep ≠ can1357/jegrep ≠ uehaj/jev-semgrep.
     default threshold 0.8 still soft. 40-line windows cannot prove whole function.
     Full cards: `applied-mappings.md`, `formal-methods.md`, `faq.md`.
264. **token-native extract** (dangquan1402/jev-extract):
     position 10 (Discretizer). token-native sequential start/end Choice.
     Gemini/Haiku stubs not configured yet.
     Full cards: `applied-mappings.md`, `faq.md`.
265. **jyje LangGraph pilot** (jyje/pilot-typesafeai-jev):
     positions 4 (Selector) × 3 (Gate). handful of hand-written examples, not a benchmark.
     Jev judged exactly what it was given.
     Full cards: `mixed-architecture.md`, `faq.md`.
266. **laguagu skills sibling** (laguagu/jev-skills):
     position 1 (Operand). laguagu/jev-skills ≠ laguagu/jev-evidence-lab ≠ Pleo2/awesome-jev-agent-skills.
     Full cards: `faq.md`.
267. **cost-optimizer 0.85 floor** (lorensation/llm-cost-optimizer-jev):
     positions 4 (Selector) × 11 (Bounds). contract_passed is not a claim of guaranteed factual truth.
     Wilson lower bound 0.85 floor. fixture mode no savings claim.
     Full cards: `formal-methods.md`, `faq.md`.

268. **Category error Jev vs GPT-5.6** (@mervenoyann):
     position 11 (explainer of already-owned class boundary,
     not a new construct). Jev vs GPT-5.6 bakeoffs are a category error.
     Right lineage = encoder / ZS classifiers (BERTForXYZ → DeBERTa → ModernBERT).
     Jev is exemplar not the mandate. Full cards: `mixed-architecture.md`, `faq.md`,
     `judgment-class.md`.
269. **Skill-issue thesis** (@mervenoyann):
     position 11 × replace-one-classifier-step. many problems solved with LLMs
     could have been solved with them, it was a skill issue. Mixed architecture,
     not stack replacement. Full cards: `mental-models.md`, `faq.md`.
270. **Prefer DeBERTa / ModernBERT Hub pointers** (@mervenoyann follow-up):
     position 1 (Operand / family choice). opt for DeBERTa and ModernBERT ones.
     hf:MoritzLaurer/deberta-v3-large-zeroshot-v2.0 likes 139;
     hf:MoritzLaurer/ModernBERT-large-zeroshot-v2.0 likes 72.
     Hub widget bart-large-mnli is **not** her pick. Do not copy `pipeline()`.
     Full cards: `judgment-class.md`, `faq.md`.
271. **Multimodal image<>text ZS as perception front-end**:
     position 10 (perception) then a typed Choice/Noul on the decision.
     Skip Archer. Full cards: `mixed-architecture.md`, `mental-models.md`.
272. **softmax/ZS scores still ≠ calibrated Noul** (Hub widget 0.504/0.479 *theirs*):
     position 3 is *tempting* (hard-gate the ZS score) and **rejected**.
     soft scores ≠ hard gates. Quote *theirs*; do not invent accuracy numbers.
     Full cards: `formal-methods.md`, `validation.md`.


User-provided 0806 items 268–272 (`notes.md` §112). Do **not**
re-fold §85 / §111 items 248–267 / §110 64× Space.
people who compare Jev against GPT-5.6 has never fine-tuned BERTForXYZ for living and it shows; zero shot classifiers; scale them as much as decoder only models; many problems solved with LLMs could have been solved with them, it was a skill issue; opt for DeBERTa and ModernBERT ones; BERTForXYZ → DeBERTa → ModernBERT; Jev vs GPT-5.6 bakeoffs are a category error; encoder / ZS classifiers; institutional HF voice; quote *theirs*; do not invent accuracy numbers; softmax/ZS scores still ≠ calibrated Noul; soft scores ≠ hard gates; @mervenoyann; likes 421 / 189; impressions 35498 / 9613; multimodal image<>text ZS as perception front-end; hf:MoritzLaurer/deberta-v3-large-zeroshot-v2.0 likes 139; hf:MoritzLaurer/ModernBERT-large-zeroshot-v2.0 likes 72; Bart, bert, deberta, modernbert, these are all LLMs; Maziyar quoted; Jev is exemplar not the mandate; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29.
Soft Noul ≠ hard safety.

User-provided 0806 uniqueness lock: people who compare Jev against GPT-5.6 has never fine-tuned BERTForXYZ for living and it shows; zero shot classifiers; scale them as much as decoder only models; many problems solved with LLMs could have been solved with them, it was a skill issue; opt for DeBERTa and ModernBERT ones; BERTForXYZ → DeBERTa → ModernBERT; Jev vs GPT-5.6 bakeoffs are a category error; encoder / ZS classifiers; institutional HF voice; quote *theirs*; do not invent accuracy numbers; softmax/ZS scores still ≠ calibrated Noul; soft scores ≠ hard gates; @mervenoyann; likes 421 / 189; impressions 35498 / 9613; multimodal image<>text ZS as perception front-end; hf:MoritzLaurer/deberta-v3-large-zeroshot-v2.0 likes 139; hf:MoritzLaurer/ModernBERT-large-zeroshot-v2.0 likes 72; Bart, bert, deberta, modernbert, these are all LLMs; Maziyar quoted; Jev is exemplar not the mandate; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29.

273. **ywchiu Harbor-jevals PRIMARY** (ywchiu/jev_benchmark):
     positions 4 (Selector) × 8 (Metric) × 3 (Gate).
     ywchiu/jev_benchmark ≠ Running-Dolphins/jev-bench ≠ Praveenrajus/jev-bench.
     Gemma 4 31B 77.0% / Jev 1.13.0 61.4% / Laya 322M 0.0%.
     restriction state 95.0% against 84.4%. None of the systems are particularly good at knowing when to stop and ask.
     They skip the question and call a tool directly. 100% schema pass. six-field joint 48.8% vs 72.8%.
     Full cards: `validation.md`, `faq.md`, `mental-models.md`.
274. **Transformers one-decode sibling** (siren2345/jev-single-decode-transformers):
     position 1 (Operand). siren2345/jev-single-decode-transformers ≠ siren2345/jev-single-decode.
     Split Transformers experiment from llama.cpp runtime.
     Full cards: `judgment-class.md`, `faq.md`.
275. **tanayvasishtha/jev-lab scaffold** (tanayvasishtha/jev-lab):
     position 8 (Metric). tanayvasishtha/jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab ≠ yibie/laya-jev-lab.
     Four experiments stress-testing TypeSafe's Jev: calibration, bundle bias, label bias, and ensembling.
     second pass must be $0.00 from cache. The pages never call Jev.
     Full cards: `faq.md`.
276. **Praveenrajus densify** (hfdataset:Praveenrajus/jev-bench):
     position 8 (Metric). 22 configs · 166,054 rows · 4 calibration-gold. sha a39eba3f.
     Full cards: `validation.md`.
277. **pngwn laya-bench densify** (hfdataset:pngwn/open-jev-laya-bench):
     position 8 (Metric). pngwn/open-jev-laya-bench README 404. sha 9f69c742 likes 2.
     Full cards: `faq.md`.
278. **jevlogs dataset** (hfdataset:reachjalil/jevlogs-log-triage-benchmark):
     positions 3 (Gate) × 8 (Metric). HDFS 0.9933 (745/750) / retain 0.0084.
     BGL ERROR/FATAL protection 1.0000. E2 recomputes from saved probabilities.
     Full cards: `mixed-architecture.md`, `faq.md`.
279. **BunsDev calibration-lab densify** (hfspace:BunsDev/laya-calibration-lab):
     position 8 (Metric). Space sha eda59e0a. T never changes argmax.
     MASSIVE English 0.783 / Khmer 0.033 / Hindi 0.133. 40–48 rows too small to ship T.
     Full cards: `validation.md`.
280. **mini-jev-runs densify** (hfdataset:Mikhail/mini-jev-runs):
     positions 1 (Operand) × 8 (Metric). 27 900 schema-driven decisions.
     13 600 / 13 600 questions. candidate mass min 0.99999624.
     Full cards: `judgment-class.md`.
281. **Verdict-open-jev NAR** (Heman10x-NGU/Verdict-open-jev):
     positions 1 (Operand) × 8 (Metric).
     Heman10x-NGU/Verdict-open-jev ≠ Heman10x-NGU/openJev-verdict-2.0.
     TF-IDF + LogReg ECE 0.0207 vs Jev 0.1440. Verdict-open-jev 48.07% vs Jev 90.80%.
     Full cards: `judgment-class.md`, `validation.md`, `faq.md`.
282. **Mintzs/jevify densify** (Mintzs/jevify):
     position 1 (Operand). 26.1× faster than standard Qwen JSON generation.
     Jevify 90.0% / 167 ms CUDA graphs disabled.
     Full cards: `faq.md`.
283. **rlcd-lite densify** (arnabgho/rlcd-lite):
     positions 1 (Operand) × 8 (Metric). Finding 1: Brier on stated confidence alone is a trap.
     grpo_rlcr 0.78 / ECE 0.084. reliability 0.007 but resolution 0.000.
     Full cards: `validation.md`, `faq.md`.
284. **distill-corpus student** (hfdataset:SargeDev/jev-distill-corpus):
     position 1 (Operand). Student B MAE 0.148 / Pearson 0.836 / 86.0%.
     Full cards: `faq.md`.
285. **altryne/jevify placement skill** (altryne/jevify):
     position 2 (Post-judge). altryne/jevify ≠ Mintzs/jevify ≠ gulagala001/jevify ≠ uspraveen/Jevify.
     Find where Jev belongs. Design the questions. Measure the difference.
     Full cards: `applied-mappings.md`, `faq.md`.
286. **DecisionOps contracts** (erayyilmmaz/jev-decisionops):
     positions 7 (Policy) × 11 (Bounds). ACT / REVIEW / FALLBACK.
     A provider failure, timeout, malformed output, or missing answer is **not** a policy outcome.
     confidence is descriptive provider output, not a substitute for probability.
     Quality denominators include only valid scored answers.
     an exact halfway tie chooses the lower level.
     Full cards: `formal-methods.md`, `mixed-architecture.md`, `faq.md`.
287. **aiwithenoch/Jev-Skill harness** (aiwithenoch/Jev-Skill):
     positions 1 (Operand) × 3 (Gate).
     aiwithenoch/Jev-Skill ≠ simplosophy/jev-skill ≠ laguagu/jev-skills.
     The local path does not claim to turn a smaller checkpoint into Jev.
     Low support becomes decision: "review". MIT-0 SPDX NOASSERTION.
     Full cards: `applied-mappings.md`, `faq.md`.
288. **simplosophy/jev-skill current-llm** (simplosophy/jev-skill):
     position 1 (Operand). current-llm. 结构兼容，不是 Jev 模型能力.
     Full cards: `applied-mappings.md`, `faq.md`.


289. **Hysteresis as policy** (edgardcham/huncho):
     positions 3 (Gate) × 7 (Policy). A hunch is a probability with a policy attached.
     { enter: 0.8, exit: 0.6 } is hysteresis. replay a policy change without inference.
     Decision models are providers, not the product.
     huncho ≠ Kungie/gut ≠ carldaws/hunch ≠ tpellet/hunch.
     Full cards: `mixed-architecture.md`, `faq.md`, `mental-models.md`.
290. **Instruct-tuning breaks option-logit ECE** (VladUZH/jev-calibration) PRIMARY:
     position 11 (measurement of an already-owned class property).
     pretrained Qwen2.5 base ECE 0.030 (0.5B) / 0.040 (7B); instruct 0.302 / 0.269.
     70.9% → 70.0% mean conf 74.1% → 96.7%. temperature scaling still matches it in-distribution.
     No Jev API was called. Qwen2.5 ≠ Archer. Ranking ≠ calibration.
     Full cards: `validation.md`, `faq.md`.
291. **JA System One encoder + position bias** (hiroki-abe-58/sokudan):
     position 1 (Operand / family) × 10 (option-order as measurement).
     学習済みモデル v0.1 は準備中です. bool AUROC 0.523.
     先頭だと0件、末尾だと250件. 温度を渡さない場合、確率は較正されていません.
     このリポジトリには Jev を呼ぶコードが存在しません.
     Full cards: `judgment-class.md`, `validation.md`.
292. **what-is-jev rename densify** (g0runmezadam/what-is-jev IS tunahansahin897/what-is-jev):
     position 2 (Post-judge / catalog). same GitHub id 1378007307.
     947 repos scored; A 273 · B 302 · C 372; LLM rubric ≠ benches;
     Data as of 2026-09-20; HEAD 895b9498; README SHA 3ae98c56.
     Do **not** mint a second census. catalog ≠ endorsement.
     Full cards: `faq.md`, `applied-mappings.md`.
293. **Advisory Codex audit** (omni-/ask-jev):
     position 3 is *tempting* (block the turn on p) and **rejected**.
     13 focused checks and one mutually exclusive outcome.
     Probabilities are advisory, not calibrated guarantees.
     omni-/ask-jev ≠ pedroknigge/mcp_jev.
     Full cards: `faq.md`, `agent-self-assessment.md`.
294. **Equal-width vs quantile ECE + cost-optimal line** (rlaope/jeval) PRIMARY:
     position 11 × 4 (Selector of operating point from costs).
     pd.cut bins by equal width while jeval bins by quantile; ECE 0.113 and ECE 0.076.
     jeval drift is not implemented yet. rlaope/jeval ≠ dayhaysoos/jevals.
     Full cards: `validation.md`, `mental-models.md`.
295. **Calibration does not compose** (dnakhoa/jev-deferred-crispification) PRIMARY:
     position 9 (composition algebra of hops) × 11 (anti-soundness-theater).
     ECE has exactly zero statistical power to detect the failure mode that kills trajectories.
     25–60× headline withdrawn. P(all-correct): 0.0071 vs 0.0001. TCE / AMS.
     Deferred Crispification. Qwen 3.8 sparring ≠ Archer.
     Full cards: `formal-methods.md`, `validation.md`, `faq.md`.
296. **Screening cutoff theater** (matsuikentaro1/jev-title-abstract-screening):
     position 3 rejected as Harbor. light_cutoff_applied_to_combination 0.
     0.5 sensitivity does not transfer. Full cards: `question-design.md`, `faq.md`.
297. **Recorded-run rover demo** (metrox-eth/moss-jev):
     position 10 (perceive is simulated). recorded run, kinematic animation.
     No live API. Skip Archer. Full cards: `mixed-architecture.md`.
298. **Supervised BERT vs zero-shot Jev is not a ranking** (thisisandreeeee/jev-benchmarks):
     position 11. BANKING77 Accuracy BERT-Base 93.02 Jev 79.90.
     BERT figures are published supervised references, not zero-shot.
     Analyse jev calibration (NLL, ECE) backlog. ranking ≠ calibration.
     Full cards: `validation.md`, `judgment-class.md`.
299. **Use-case catalog as judgment lens** (vamsikrishna2421/jev-usecases):
     position 2. vamsikrishna2421/jev-usecases ≠ whyashthakker/awesome-jev-use-cases.
     catalog ≠ endorsement. Full cards: `applied-mappings.md`, `faq.md`.
300. **Pointer highlighter / BYO key** (yuvalraviv1/highlight):
     position 10 (extractive). Bring your own API key. Sentence Noul/Score + paragraph Choice.
     Pointer-not-generator. Full cards: `mixed-architecture.md`.
301. **Decision circuits / independence recorded** (Barneyjm/decision-circuits):
     positions 3 × 7. AND: product (independence assumed and recorded in the trace).
     chat model's stated confidence is not calibrated. circuit-vl-4b ≠ Archer.
     ≠ voidning/jev-combinators ≠ Illusion47586/judge.
     Full cards: `mixed-architecture.md`, `formal-methods.md`.
302. **Constructed-case study ≠ benchmark** (xiaohuaxi/jev-study):
     position 11. 不是 benchmark; 概率没做 calibration.
     档位措辞效应 分数极差中位 0.50、最大 1.32; 修好后对照组是 0.01.
     ~1,430 API calls, about $0.15.
     xiaohuaxi/jev-study ≠ wjdjdakf17/jev-study ≠ baekenough/jev-study.
     Full cards: `validation.md`, `question-design.md`.

Hourly 0843 items 289–302 (`notes.md` §114). Do **not**
re-fold §113 items 273–288 / §112 items 268–272 / §111 items 248–267 / §109
tunahan census as a sibling. Merged #31 owns items 273–288 / `notes.md` §113 / batch #96 — leave them alone. Qwen/Qwen3.8-27B ≠ Archer.
Archer still promised_not_landed.
Soft Noul ≠ hard safety.


303. **NanoJev unified-games-v1 PRIMARY** (TianyuCodings/NanoJev):
     positions 1 (Operand) × 4 (Selector) × 10 (Discretizer).
     A 0.6B parallel decision model: states and questions in, complete probability distributions out. Zero output-token decoding.
     not TypeSafe Jev; open replica / specialist gameplay S1.
     Full cards: `judgment-class.md`, `mixed-architecture.md`, `faq.md`.
304. **Zero-token parallel / dynamic candidates** (TianyuCodings/NanoJev):
     positions 1 (Operand) × 10 (Discretizer).
     Parallel decisions; Choice 2–255; Boolean; Score 2–10 ordered levels.
     Softmax over a supplied bag ≠ a Noul.
     Full cards: `judgment-class.md`, `faq.md`.
305. **One model, four games / held-out table** (TianyuCodings/NanoJev):
     position 8 (Metric). One model, four games.
     ViZDoom Basic 128/128 vs Jev 56/128; Predict Position 27/128 vs Jev 11/128;
     Maze 225 attempts vs Jev 2738; Snake 30 food / 256 steps;
     held-out Maze 4/10 Snake 8/8 Basic 128/128 Predict 27/128.
     Untuned Qwen3-0.6B baseline. Game success ≠ calibrated Noul.
     Full cards: `validation.md`, `faq.md`.
306. **Dataset / mix / hard_lr1e5** (hf:C-Tianyu/NanoJev + C-Tianyu/NanoJev-Data):
     position 8 (Metric). 18,760 questions per variant; 16,333 ViZDoom;
     896 Predict Position expert episodes; hard_lr1e5;
     mix weights 1/3, 1/3, 1/6, 1/6; Hub C-Tianyu/NanoJev revision unified-games-v1 likes 58;
     dataset C-Tianyu/NanoJev-Data likes 5.
     Full cards: `validation.md`.
307. **Name collisions** (caijinchun/nanojev-arena / liao96312/jev-arena-nanojev / zwliJay/jev-forge):
     namesake lock. caijinchun/nanojev-arena ≠ liao96312/jev-arena-nanojev ≠ zwliJay/jev-forge ≠ NanoJev.
     Full cards: `faq.md`, `judgment-class.md`.
308. **boolean ≠ noul / demo 401 / calibration honesty** (TianyuCodings/NanoJev):
     positions 1 (Operand) × 9 (Verifier — rejected as proof).
     local type boolean ≠ TypeSafe noul.
     A normalized distribution alone does not establish empirical probability calibration.
     Demo HTTP 401 gated; recordings local. soft scores ≠ hard gates.
     Full cards: `formal-methods.md`, `mixed-architecture.md`, `faq.md`.

User-provided 0915 items 303–308 (`notes.md` §115). Do **not**
re-fold §113 items 273–288 / merged #35 §114 items 289–302
/ merged #30 items 268–272 / 0646 items 248–267.
Skip Archer rewrite. Game success ≠ calibrated Noul;
local type boolean ≠ TypeSafe noul;
caijinchun/nanojev-arena ≠ liao96312/jev-arena-nanojev ≠ zwliJay/jev-forge ≠ NanoJev;
do not reopen or amend PR #31/#32/#33/#35.
Soft Noul ≠ hard safety.

User-provided 0915 uniqueness lock: TianyuCodings/NanoJev unified-games-v1 densify; A 0.6B parallel decision model: states and questions in, complete probability distributions out. Zero output-token decoding.; One model, four games; ViZDoom Basic 128/128 vs Jev 56/128; Predict Position 27/128 vs Jev 11/128; Maze 225 attempts vs Jev 2738; Snake 30 food / 256 steps; held-out Maze 4/10 Snake 8/8 Basic 128/128 Predict 27/128; Untuned Qwen3-0.6B baseline; 18,760 questions per variant; 16,333 ViZDoom; 896 Predict Position expert episodes; hard_lr1e5; mix weights 1/3, 1/3, 1/6, 1/6; Hub C-Tianyu/NanoJev revision unified-games-v1 likes 58; dataset C-Tianyu/NanoJev-Data likes 5; HEAD 618cea6d906d54e128360786d12f703fff2b1245; 1289★ / 158 forks / size 64035; README SHA 4190093c64ee75b26e9726daa3b00cbcf6d3157a; MIT; caijinchun/nanojev-arena ≠ liao96312/jev-arena-nanojev ≠ zwliJay/jev-forge ≠ NanoJev; not TypeSafe Jev; open replica / specialist gameplay S1; soft scores ≠ hard gates; Game success ≠ calibrated Noul; local type boolean ≠ TypeSafe noul; invented_signal false; do not reopen or amend PR #31/#32/#33/#35; notes.md §115

309. **Capability-tree retrieve-wide→decide→evidence-set** (NiazMorshed2007/jcr):
     positions 2 (Post-judge) × 4 (Selector) × 5 (Prior).
     NiazMorshed2007/jcr ≠ skill-broker ≠ skillranker ≠ jev-sift ≠ jev-lens ≠ jevusher ≠ jev_select_capability.
     one tool to find documented deterministic commands in a nested capability tree.
     returns context. **does not execute**.
     Full cards: `mappings.md` §4, `faq.md`, `mental-models.md`.
310. **Skills vs capability catalogs** (NiazMorshed2007/jcr):
     position 2 (Post-judge). skills = workflow+judgment; capabilities = individual operations.
     format independent of Jev. proposed open standard exploration.
     Full cards: `applied-mappings.md`, `faq.md`.
311. **0.6 band is application policy** (NiazMorshed2007/jcr):
     positions 3 (Gate) × 7 (Policy).
     keep up to 3 paths ≥60% of best (JCR_BAND_RATIO 0.6).
     soft scores ≠ hard gates. 0.6 band is application policy.
     Full cards: `mixed-architecture.md`, `validation.md`.
312. **Routing ≠ permission / docs ≠ authority to run** (NiazMorshed2007/jcr):
     positions 7 (Policy) × 11 (Bounds).
     routing ≠ permission. docs ≠ authority to run.
     JCR returns documentation. It does not execute commands.
     Full cards: `formal-methods.md`, `faq.md`.
313. **Beam as control (geometric mean)** (NiazMorshed2007/jcr):
     position 4 (Selector). Cookbook cousin (`notes.md` §2 K=3), not a new species.
     classify (Jev) → optional OpenAI decompose compound → beam search geometric mean of routing probs.
     ambiguity / no-match / depth-limit explicit. 16 routing rounds per step.
     Full cards: `mental-models.md`, `question-design.md`.
314. **VOI of context admission** (NiazMorshed2007/jcr):
     position 5 (Prior). Search stays outside the main agent; selected `context` is the evidence set.
     11 groups, 960 nodes, 11,360 items.
     Full cards: `mixed-architecture.md`, `agent-self-assessment.md`.
315. **Measurement honesty / wall-time mixed** (NiazMorshed2007/jcr):
     position 8 (Metric). sol-vs-opus5-20 *theirs*: 20 scenarios × 4 variants = 80 runs.
     lookup+explain only, no execution. n=1 per cell. Not Harbor task-execution.
     Claude Opus 5: agent input 108,585→15,819 (−85%), cost $0.3700→$0.1222 (−67%), wall 105.5s→77.7s.
     Codex GPT-5.6-Sol: 61,952→47,669 (−23%), $0.1377→$0.1151 (−16%), wall 25.3s→62.4s (Sol slower with JCR in 19/20).
     One Sol outlier 372.6s / 193 Jev calls.
     Full cards: `validation.md`, `faq.md`.
316. **Lookup+explain only / Claude and Codex harnesses** (NiazMorshed2007/jcr):
     positions 8 (Metric) × 11 (Bounds). Claude/Codex harnesses. compare mode. 50 scenarios bundled.
     Full cards: `validation.md`.


330. **SemIf rename densify** (TheoLeeCJ/SemIf):
     position 1 (Operand). SemIf was formerly OpenJev. rename is densify not a second census.
     independent; not affiliated with Jev or TypeSafe. homepage openjev.com. default master. MIT.
     live REST 2282★ / 140 forks. HEAD ca3ba65f1429.
     Full cards: `judgment-class.md`, `faq.md`, `mental-models.md`.
331. **Interface pattern ≠ replica** (TheoLeeCJ/SemIf):
     position 1 (Operand). interface pattern reproduction with open models;
     does not reproduce Jev undisclosed model/training.
     wire/agreement ≠ replica of TypeSafe.
     Full cards: `judgment-class.md`, `faq.md`.
332. **Direct logits / 0 tokens / shared-state** (TheoLeeCJ/SemIf):
     positions 1 (Operand) × 8 (Metric). Direct option logits; 0 output tokens; shared-state parallel.
     Full cards: `mixed-architecture.md`, `judgment-class.md`.
333. **MLX Apple Silicon densify** (TheoLeeCJ/SemIf):
     position 1 (Operand). MLX backend for Apple Silicon (`--backend mlx`).
     Tolerate float roundoff in MLX evidence verification.
     typed output does not guarantee semantic correctness.
     Full cards: `judgment-class.md`, `faq.md`.
334. **Speed 5.21× systems comparison** (TheoLeeCJ/SemIf):
     position 8 (Metric). Qwen3.5-4B 3090 direct 1.023s vs AR JSON 5.332s (**5.21×**);
     argmax agree 18/21; systems comparison ≠ semantic equivalence.
     Full cards: `validation.md`, `faq.md`.
335. **Parallel suffixes 20.03 densify** (TheoLeeCJ/SemIf):
     position 8 (Metric). Parallel suffixes 20.03 dec/s on 777 decisions.
     Full cards: `validation.md`.
336. **Browser ladder + cousins** (TheoLeeCJ/SemIf):
     positions 8 (Metric) × 11 (Bounds). authored BA 0.813, pert 0.766,
     TypeSafe subset agreement 0.845 vs Published Jev 0.883 (102 across 20 cases).
     Softmax over options ≠ calibrated Noul. JevBench 74.6 is §78 not this ladder.
     SemIf ≠ kw2828/OpenJev playground ≠ zhihz/openjev ≠ apiplant/semif-rs port ≠ dddanielliu/semif-serve.
     Full cards: `validation.md`, `faq.md`, `mental-models.md`.

User-provided 0922 items 330–336 (`notes.md` §117). Do **not**
re-fold merged #36 §115 items 303–308 / §114 items 289–302 / §113 items 273–288
/ merged #38 §116 items 309–316. Skip open #40 items 322–329.
Soft Noul ≠ hard safety. Ranking ≠ calibration theater.
SemIf 2282★ (+41 vs §113 2241; +45 vs §114 2237);
do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#38.
do not push onto open #39/#40.


User-provided 0920 jcr items 309–316 (`notes.md` §116). Do **not**
re-fold 0743 items 273–288 / merged #30 items 268–272 / 0646 items 248–267.
Merged #35 owns §114 / items 289–302 / batch #97. Merged #36 owns §115 / 303–308 / #98. Open #37 owns §117 / 315–321 / #100 (item overlap 315–316 is #37's remap).
NiazMorshed2007/jcr ≠ skill-broker ≠ skillranker ≠ jev-sift ≠ jev-lens ≠ jevusher ≠ jev_select_capability.
soft scores ≠ hard gates; 0.6 band is application policy;
routing ≠ permission; docs ≠ authority to run;
n=1 per cell; Not Harbor task-execution;
do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34.
Soft Noul ≠ hard safety.
Hourly 0743 items 273–288 (`notes.md` §113). Do **not**
re-fold merged #30 items 268–272 / 0646 items 248–267 / 0541 items 226–247 / 0439 items 202–225 / 0345 items 186–201 / 0243 items 178–185 / 0145 items 161–177 / 0042 items 149–160 / 2340 items 138–148 / 2246 items 129–137 / 2145
items 120–128 / 2041 items 111–119 / 1943 items 102–110 /
1843 items 97–101 / 1740 items 94–96 / SIGNAL §93
mechanism / §60 six-gates / §78 v1.2 board / §71 claim-audit /
pngwn RESULTS / yuki-oshio/mini-jev *93.25%*.
Ranking ≠ calibration theater; softmax over A/B/C ≠ Noul;
0.85 still soft; ACT is policy not proof;
SemIf 2241★ (+34 vs §111 2207);
tracker likes 67 (+3 vs 64), lastModified UNCHANGED;
Laya likes 864 (was 822); Blackwood tracker ABSENT;
Archer still promised_not_landed;
TypeAR-AI/TypeAR 301 → TypeLLM/TypeLLM;
do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#32/#33.
Soft Noul ≠ hard safety.

Hourly 0743 uniqueness lock: Heman10x-NGU/Verdict-open-jev ≠ Heman10x-NGU/openJev-verdict-2.0; TF-IDF + LogReg ECE 0.0207 vs Jev 0.1440; Verdict-open-jev 48.07% vs Jev 90.80%; abstention combined recall 10.00%; p50 35.58 ms; K=25 (maximum capacity) 72.00%; 0.85 coverage 84.60% selective risk 1.18%; 26.1× faster than standard Qwen JSON generation; Jevify 90.0% / 167 ms CUDA graphs disabled; Finding 1: Brier on stated confidence alone is a trap; grpo_rlcr 0.78 / ECE 0.084; reliability 0.007 but resolution 0.000; 27 900 schema-driven decisions; 13 600 / 13 600 questions; candidate mass min 0.99999624; 22 configs · 166,054 rows · 4 calibration-gold; sha a39eba3f; Student B MAE 0.148 / Pearson 0.836 / 86.0%; pngwn/open-jev-laya-bench README 404; sha 9f69c742 likes 2; HDFS 0.9933 (745/750) / retain 0.0084; BGL ERROR/FATAL protection 1.0000; 2,479 / 2,500 HDFS uncertain; cache hit 0.9648 (2412/2500); $0.153936 estimated; E2 recomputes from saved probabilities; Space sha eda59e0a; MASSIVE English 0.783 / Khmer 0.033 / Hindi 0.133; 40–48 rows too small to ship T; T never changes argmax; siren2345/jev-single-decode-transformers ≠ siren2345/jev-single-decode; Split Transformers experiment from llama.cpp runtime; tanayvasishtha/jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab ≠ yibie/laya-jev-lab; Four experiments stress-testing TypeSafe's Jev: calibration, bundle bias, label bias, and ensembling; second pass must be $0.00 from cache; The pages never call Jev; Gemma 4 31B 77.0% / Jev 1.13.0 61.4% / Laya 322M 0.0%; restriction state 95.0% against 84.4%; None of the systems are particularly good at knowing when to stop and ask; They skip the question and call a tool directly; 100% schema pass; six-field joint 48.8% vs 72.8%; ywchiu/jev_benchmark ≠ Running-Dolphins/jev-bench ≠ Praveenrajus/jev-bench; ACT / REVIEW / FALLBACK; A provider failure, timeout, malformed output, or missing answer is **not** a policy outcome; confidence is descriptive provider output, not a substitute for probability; Quality denominators include only valid scored answers; an exact halfway tie chooses the lower level; aiwithenoch/Jev-Skill ≠ simplosophy/jev-skill ≠ laguagu/jev-skills; The local path does not claim to turn a smaller checkpoint into Jev; Low support becomes decision: "review"; MIT-0 SPDX NOASSERTION; current-llm; 结构兼容，不是 Jev 模型能力; altryne/jevify ≠ Mintzs/jevify ≠ gulagala001/jevify ≠ uspraveen/Jevify; Find where Jev belongs. Design the questions. Measure the difference; TypeAR-AI/TypeAR 301 → TypeLLM/TypeLLM; TypeLLM/TypeLLM 16★; SemIf 2241★ (+34 vs §111 2207); jevlike 1051★ (+8 vs 1043); AnotiaWang 98★ (+1 vs 97); yibie/awesome-jev 525★ (+19 vs 506); Laya likes 864 (was 822); tracker likes 67 (+3 vs 64); lastModified UNCHANGED `2026-09-20T04:29:16.000Z`; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#32/#33; notes.md §113

322. **Migration / question-design on-ramp** (alexwestco/llm-to-jev) PRIMARY:
     position 11 (explainer of already-owned placement) × replace-one-classifier-step.
     Turn decision-shaped LLM prompts into proposed Jev primitives.
     Companion to altryne/jevify (find / design / measure) — this is a prompt compiler.
     Full cards: `question-design.md`, `mental-models.md`, `faq.md`.
323. **Soft proposal ≠ production gate**:
     position 3 is *tempting* (ship the export) and **rejected**.
     This is a conversion assistant, not an automatic guarantee of equivalent behavior.
     Generated instructions and criteria must be reviewed before production use.
     Falsifying experiment still required. Full cards: `validation.md`, `faq.md`.
324. **Partial convertibility** (keep generative work with the LLM):
     positions 4 (Selector of which slice is bounded) × mixed-architecture leftover.
     suitability strong/partial/not_a_fit; compatibility full/partial/none.
     Writing new text stays with an LLM. Full cards: `mixed-architecture.md`, `applied-mappings.md`.
325. **Category error — prose stays LLM**:
     position 11 (already-owned class boundary). Prompts requiring open-ended prose are not a fit.
     welcome-email → none / not_a_fit / no systemOne export. Full cards: `faq.md`, `question-design.md`.
326. **Companion to decision-design card + validation gate**:
     position 8 (Metric still owed). The compiler uses deterministic heuristics, not an LLM or evaluation model.
     It understands a deliberately small set of common prompt patterns.
     Roadmap fixture-eval / editable criteria / multi-step / latency-cost compare is **not landed**.
     Full cards: `validation.md`, `question-design.md`.
327. **Heuristic conversion ≠ calibrated Noul** (0–1 → ordered criteria *theirs*):
     position 3 rejected as Harbor. Score ranges such as 0 to 1 are translated into ordered Jev criteria.
     Review the generated Score rubric; Jev scores ordered criteria, not an arbitrary 0-to-1 range.
     softmax/heuristic scores still ≠ calibrated Noul. Full cards: `formal-methods.md`, `validation.md`.
328. **Namesake lock vs jevify family**:
     position 1 (Operand / cousin, not identity).
     alexwestco/llm-to-jev ≠ altryne/jevify ≠ ryana/jevify ≠ fidecastro/jevify ≠ Mintzs/jevify ≠ gulagala001/jevify ≠ uspraveen/Jevify.
     Full cards: `judgment-class.md`, `faq.md`.
329. **Browser-local conversion assistant; key never stored**:
     position 7 (Policy of the tool itself). Everything runs locally in the browser.
     There is no framework, database, account, API, or server-side prompt processing.
     The key is read from the process environment and is never stored or printed.
     connect-src 'none'. Do not copy `npm` / `TYPESAFE_API_KEY`. Full cards: `faq.md`, `mixed-architecture.md`.


337. **jev-as-judge / openevals densify** (memovai/openevals):
     position 8 (Metric). Fast and cheap agent evals. jev as judge.
     judge ≠ actuator. Densify §42 MED. Full cards: `validation.md`, `faq.md`.
338. **skill census judge** (48Nauts-Operator/skill-dash):
     positions 4 (Selector) × 8 (Metric). 18,041 skills from the 200 most-starred repos.
     Not a security scanner. Full cards: `applied-mappings.md`, `judgment-class.md`.
339. **namesake jev-lab demo** (q93304989-bit/jev-lab):
     namesake lock. 最简 Jev 调用演示器. confidence 不是正确率.
     q93304989-bit/jev-lab ≠ tanayvasishtha/jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab ≠ yibie/laya-jev-lab.
     Full cards: `faq.md`, `question-design.md`.
340. **withdrawn routing claim** (33Audits/jev-auto):
     position 6 (Router). 75% cheaper and 18% faster withdrawn.
     jev @0.15 100% recall 87% savings. 33Audits/jev-auto ≠ gargpratyush/jev-router.
     Full cards: `validation.md`, `mixed-architecture.md`.
341. **tool-emitted Score/Noul** (Danu28/pi-jev-harness):
     position 1 (Operand). no Typesafe key, no PI_API_BASE, zero deps.
     tool-emitted Score/Noul ≠ calibrated Noul. Full cards: `faq.md`, `formal-methods.md`.
342. **OneForward logit readout PRIMARY** (Embodied-AI-System/Qwen3.5-OneForward):
     positions 1 (Operand) × 10 (Discretizer). semantic_compatibility: false.
     candidate_mass. softmax over A–H ≠ Noul. Qwen3.5-2B ≠ Archer.
     Full cards: `judgment-class.md`, `validation.md`, `faq.md`.
343. **MCP judge ≠ actuator** (HiepPP/hiep-paseo-plugin):
     position 3 (Guard). Jev evaluates decisions; it cannot run a coding-agent session.
     judge ≠ actuator. Full cards: `mixed-architecture.md`, `agent-self-assessment.md`.
344. **Status: no model yet** (S1LV3RJ1NX/openjev):
     namesake lock. Status: no model yet. S1LV3RJ1NX/openjev ≠ TheoLeeCJ/openjev.
     Full cards: `judgment-class.md`, `faq.md`.
345. **arcade Jev control** (Sunwood-ai-labs/jev-flight-combat):
     position 7 (Controller). 28 accepted decisions; 3 targets; score 800; health 100.
     arcade game not a flight trainer. Full cards: `mixed-architecture.md`.
346. **replay without verified live call** (Tomdachs/jev-replay-lab):
     position 8 (Metric). A successful live TypeSafe call has not been verified for v0.1.0.
     Full cards: `validation.md`.
347. **YouTube tidy namesake** (abhibansal60/tidy):
     namesake lock. No model, Jev included, predicted which channels its owner keeps.
     abhibansal60/tidy ≠ MANISH007700/tidy. Full cards: `faq.md`.
348. **RLCD head Brier climb / honesty die** (AstroHan/decision-head-qwen3.5-4b-rlcd-32k):
     position 8 (Metric). seed 1 selected on a held-out 400-item validation split.
     Brier 0.342 → 0.378. more accurate and more overconfident. Qwen3.5-4B ≠ Archer.
     Full cards: `validation.md`, `judgment-class.md`.
349. **static quants densify** (mradermacher/jevify-gemma4-26b-a4b-GGUF):
     densify §109. static quants of kushalpatil/jevify-gemma4-26b-a4b.
     Full cards: `judgment-class.md`.
350. **retracted labels / zero eligible** (shreyanbr/system-one-training-pairs):
     The labels were corrected, and one earlier result was retracted; zero of 23,869 eligible rows.
     Full cards: `validation.md`.
351. **Exit 1 is not a proof** (jkaloger/spec-judge):
     position 8 (Metric). Exit 1 is not a proof. Full cards: `validation.md`, `faq.md`.
352. **catalogs / Go SDK / parser-first** (anandi1989 + syedabbasshaheer-art + kisshan13 + ryan-sunny/dbt-assay):
     catalog ≠ endorsement. 359 of them; Games & Simulation 82; Education & Learning 1.
     Ratings are heuristics. kisshan13/typesafe-ai-go ≠ Nibir1/typesafe-go ≠ official.
     38 tests that cannot fail in a 356-model warehouse; if a parser can answer it, Jev is never asked.
     anandi1989/awesome-jev-usecases ≠ whyashthakker/awesome-jev-use-cases ≠ walidboulanouar/awesome-jev-use-cases ≠ vamsikrishna2421/jev-usecases.
     syedabbasshaheer-art/jev-atlas ≠ ZeroX-01/jev-atlas ≠ Zaious/jev-capability-atlas ≠ gorock007/jev-atlas.
     Full cards: `faq.md`, `mixed-architecture.md`.


353. **ggmlc GGUF serving substrate PRIMARY** (mys/laya-GGUF family):
     positions 1 (Operand) × 10 (Discretizer). ggmlc GGUF is not llama.cpp.
     Loading them in llama.cpp will fail. one encoder pass.
     serving substrate ≠ calibrated replica.
     Full cards: `judgment-class.md`, `faq.md`.
354. **ONNX cousins** (tozp/laya-onnx):
     namesake lock. Opset 14 FP32 and INT8.
     tozp/laya-onnx ≠ Mattepiu/laya-onnx ≠ gqgs/laya-onnx.
     Softmax over options ≠ calibrated Noul.
     Full cards: `faq.md`, `judgment-class.md`.
355. **docker-laya serving** (chneau/docker-laya):
     position 7 (Policy of the tool itself). Dockerized FastAPI typed decisions.
     serving substrate ≠ calibrated replica. Do not copy `docker pull`.
     Full cards: `mixed-architecture.md`.
356. **laya.cpp RTX ggml CUDA** (lkarlslund/laya.cpp):
     position 7. Native C++ inference. Systems throughput ≠ semantic equivalence.
     Full cards: `judgment-class.md`, `validation.md`.
357. **option-order measurement PRIMARY** (imaddde867/jev-position-test):
     position 8 (Metric). n=6. jevmlx slots 5 of 6. hosted Jev 0 of 6.
     prior_correction made it worse. pick_by_id vs pick_second.
     Full cards: `validation.md`, `faq.md`.
358. **exact-p Minesweeper** (lvk901/jevSweeper):
     position 8 (Metric). mean Spearman ρ −0.274. picked exact-optimal 1/25 (4%).
     31 of 36 still logically decidable. 86% of the time we should not have been asking.
     game success ≠ calibrated Noul. Full cards: `validation.md`, `formal-methods.md`.
359. **LLM2Jev adapter** (Yinsongxu/LLM2Jev):
     position 1 (Operand). 64★ Apache-2.0. not affiliated with or endorsed by Jev or TypeSafe.
     No answer tokens are generated. Full cards: `judgment-class.md`, `faq.md`.
360. **OpenSourceJev llama.cpp** (sabeel111/OpenSourceJev):
     namesake lock. llama.cpp Qwen3-1.7B. Candidate-only softmax ≠ Noul.
     Full cards: `judgment-class.md`.
361. **JEV-MLX Qwen3.5-9B** (CoderInPajamas/JEV-MLX):
     position 1. Qwen3.5-9B ≠ Archer. scores not calibrated probabilities of correctness.
     Full cards: `judgment-class.md`, `validation.md`.
362. **decision-head-rlcd densify** (Astro-Han/decision-head-rlcd):
     densify §119. Qwen3.5-4B 4.9M LoRA. Brier 0.342 → 0.378.
     Qwen3.5-4B ≠ Archer. Full cards: `validation.md`.
363. **fail-open harness + handwritten demo** (litshing/jevcore + ashleyotooligan/jevbrain):
     position 3 (Guard). AUTO_ACT is not a Noul. closed-set fail-open stdlib-only.
     verified=False. The included experience uses a handwritten demo provider.
     Full cards: `mixed-architecture.md`, `faq.md`.
364. **nitro tool-gate economics** (daniel-farina/nitro):
     position 6 (Router). 22 to 40% cheaper *theirs*. first version 70% more expensive.
     0.30 keep-set is application policy. Full cards: `validation.md`, `mixed-architecture.md`.
365. **soft watermarks / BLOCK bands** (healthcare + guardian + TPA):
     position 3 (Guard). urgency 0.92 still soft. BLOCK / QUARANTINE still soft.
     third-person-audit 40% & 60% watermarks still soft.
     Full cards: `mixed-architecture.md`, `agent-self-assessment.md`.
366. **catalogs** (wuyoscar/jev-skill + wh000wh000/awesome-jev-live):
     catalog ≠ endorsement. 109★ 90 scenarios. 673 entries 4★.
     Full cards: `faq.md`, `applied-mappings.md`.
367. **planner writes JEV selects** (rmalde/minecraft-agent + lykycy123/RoboJEV):
     positions 4 (Selector) × 7 (Controller). 214★. 131 JEV decisions. 35 Astra calls.
     nether-final-08 8 minutes 43.300 seconds. structured simulator state not images.
     Full cards: `mixed-architecture.md`, `applied-mappings.md`.
368. **negative-EV honesty + jev-as-judge sensor** (xuboboo/ashare-trader + TrustifAI/typed_evals + heart-risk + fabric):
     策略未通过自己的回测门槛. 36 组参数全部净期望为负. no positive expectation under real costs.
     typed_evals NOT an official TypeSafe AI product. jev-as-judge is a sensor.
     CDC 5,000 Jev 72.2% AUC 0.7725 *theirs*. accuracy is a trap. 9.0% base rate always-no 91.0%.
     111-case benchmark *theirs*. Full cards: `validation.md`, `faq.md`.

Hourly 1049 items 353–368 (`notes.md` §120). Do **not**
re-fold §119 items 337–352 / §118 items 322–329 / §117 items 330–336
/ §116 items 309–316 / §115 items 303–308 / §114 items 289–302.
Skip Archer rewrite.
Qwen3.5-4B ≠ Archer. Qwen3.5-9B ≠ Archer.
serving substrate ≠ calibrated replica; planner writes JEV selects;
catalog ≠ endorsement; pick_by_id vs pick_second.
do not reopen or amend PR #23–#42.
Soft Noul ≠ hard safety.


369. **open recreation PRIMARY** (kshetrajna12/reflex):
     position 1 (Operand). It is an open re-creation of Jev. Qwen3.5-4B.
     WebGPU 0.8B less calibrated. open recreation ≠ calibrated replica.
     Qwen3.5-4B ≠ Archer. Full cards: `judgment-class.md`, `faq.md`.
370. **pngwn / DavidHatley independent not replica**:
     pngwn demo accuracy 0.705 ECE 0.046 ~112 ms *theirs*.
     This dataset and model are independent research artifacts, not reproductions of Jev or RLCD.
     Full cards: `validation.md`, `judgment-class.md`.
371. **semantic lint sensor PRIMARY** (lakeday-org/perch):
     position 8 (Metric) × 3 (Guard). perch 164★ MIT HEAD ba775a9940b6.
     Semantic code linting with Jev. semantic lint is a sensor not a proof.
     Full cards: `formal-methods.md`, `faq.md`.
372. **oxlint cutoff 0.8 still soft** (wobsoriano/oxlint-plugin-jev):
     position 3 (Guard). reports an error when the yes-probability clears cutoff.
     cutoff 0.8 still soft. soft scores ≠ hard gates.
     Full cards: `mixed-architecture.md`, `validation.md`.
373. **jevgrep / patdown / jevvy namesakes** (nassim-arifette + tyler-dot-earth + PanAchy):
     nassim-arifette/jevgrep ≠ Bentlybro/jevgrep ≠ can1357/jegrep ≠ uehaj/jev-semgrep.
     patdown fuzzy linter. PanAchy/jevvy ≠ Atominac/jevvy.
     Full cards: `faq.md`, `applied-mappings.md`.
374. **paired bootstrap CIs PRIMARY** (emretheus/jev-rag-benchmark):
     position 8 (Metric). +0.82 pts XQuAD-EN 95% CI +0.35 to +1.31.
     +7.62 pts SciFact CI +4.88 to +10.38. paired bootstrap CIs *theirs*.
     emretheus/jev-rag-benchmark ≠ erendikmenn/jev-rag-benchmark.
     Full cards: `validation.md`, `faq.md`.
375. **BANKING77 speed-test *theirs*** (MohtashamMurshid/jev-speed-test):
     position 8. BANKING77 500 Jev 81.0% GPT-OSS 82.8% Mercury 73.2% Gemini 85.4% *theirs*.
     Confidence was useful, not a guarantee. Full cards: `validation.md`.
376. **cascade missed parity** (saurabhkumar8112/jev-gpt5-routing-study):
     430/500 vs GPT-5 432/500. This is not demonstrated equal-quality savings.
     Full cards: `validation.md`, `mixed-architecture.md`.
377. **invented-ticket gate** (abh2050/jev-test-confidence-gate):
     24 invented tickets. Routing errors caught by the gate 0 of 3.
     sample too small to establish calibration. Full cards: `validation.md`.
378. **cartpole not TypeSafe Jev** (tinmanlab/cartpole-jev):
     This is not TypeSafe Jev. No real API requests were made.
     Controller owns force. Full cards: `formal-methods.md`, `faq.md`.
379. **laya-jev wire-compat** (KonghaYao/laya-jev):
     按官方接口写的客户端只改一个 base URL. wire-compat ≠ replica.
     serving substrate ≠ calibrated replica. Full cards: `judgment-class.md`.
380. **gqgs laya-onnx densify** (gqgs/laya-onnx):
     densify §120. 496.8 MiB. tozp/laya-onnx ≠ Mattepiu/laya-onnx ≠ gqgs/laya-onnx.
     Full cards: `judgment-class.md`, `faq.md`.
381. **laya_router 35x systems comparison** (glukicov/laya_router):
     Same accuracy, 35x faster *theirs*. systems comparison ≠ semantic equivalence.
     0.600 / 184 ms vs 0.600 / 6,415 ms. Full cards: `validation.md`.
382. **catalogs namesake lock** (BeatAPI/awesome-jev + cousins):
     All 125 projects. catalog ≠ endorsement.
     BeatAPI/awesome-jev ≠ 99hansling/awesome-jev ≠ Vishnurr2k01/awesome-jev ≠ robokrunch/awesome-jev ≠ rudy2steiner/awesome-jev-hub.
     Full cards: `faq.md`, `applied-mappings.md`.
383. **super-jev densify permission ≠ confidence** (Kevthetech143/super-jev):
     densify experimental V0.2.0. not affiliated with TypeSafe AI.
     permission ≠ confidence. Full cards: `mixed-architecture.md`, `agent-self-assessment.md`.
384. **jev-lab namesake + openjev collision + GGUF densify** (Pasblinn + allay-team + mradermacher):
     Pasblinn/jev-lab ≠ tanayvasishtha/jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab ≠ yibie/laya-jev-lab ≠ q93304989-bit/jev-lab.
     Independent project. Not affiliated with TypeSafe.
     allay-team/openjev ≠ piyush-infocusp/openjev ≠ TheoLeeCJ/openjev.
     2022 Mineflayer Jevalent collision. static quants of kushalpatil/jevify-gemma4-e4b.
     Full cards: `faq.md`, `judgment-class.md`.


385. **neurolink decide PRIMARY** (juspay/neurolink):
     position 1 (Operand). decide is not generate. tryDecide returns typed
     calibrated judgments not a token stream. 133★ MIT HEAD 268b0fe83130
     tag v12.19.0. decide ≠ generate ≠ stream.
     Full cards: `judgment-class.md`, `faq.md`.
386. **GLiNER/GLiClass ports cluster** (MacPaw / Knowledgator / fbilhaut / gravitee / apiplant / codesoda / ultrafast):
     GLiNER/GLiClass ports are class members not Jev replicas.
     MacPaw/Gliner2Swift ≠ Knowledgator/GLiClass.c ≠ fbilhaut/gliclass-rs ≠ Knowledgator/GLiClass.js ≠ gravitee-io/GLiNER4j ≠ apiplant/gliner-rs ≠ codesoda/gliner2-rs.
     Locate ≠ decide. Categorize ≠ Noul. Full cards: `judgment-class.md`.
387. **hermes-jev-approvals *theirs*** (anpicasso/hermes-jev-approvals):
     position 8 (Metric). 8.7x faster 4.4x fewer prompts *theirs*.
     153 was a reporting error. corrected 156-case 9.8x / 4.2x *theirs*.
     independent v0.2.1 1.24x vs Mini *theirs*. Approvals only.
     anpicasso/hermes-jev-approvals ≠ hermes-switchyard.
     Full cards: `validation.md`, `faq.md`.
388. **scx-router GLiClass ranker** (SouthernCrossAI/scx-router):
     GLiClass ranks candidate LLMs in one non-generative pass.
     Ranker is categorize, not a Noul. Full cards: `judgment-class.md`.
389. **typesafeai-dotnet-sdk not affiliated** (saibimajdi/typesafeai-dotnet-sdk):
     Not affiliated with TypeSafe AI. Wire client ≠ calibrated replica.
     Full cards: `faq.md`.
390. **jevcache namesake** (kushals256/jevcache):
     hyperspaceai/jevcache ≠ kushals256/jevcache. Intent-cache is not a Noul.
     Full cards: `faq.md`, `applied-mappings.md`.
391. **ST-jeved measures each reply** (mossyfield/ST-jeved):
     position 3 (Guard). Sensor, not a proof. soft scores ≠ hard gates.
     Full cards: `mixed-architecture.md`.
392. **openjev 0.2.1 densify** (razorback16/openjev):
     densify §75. razorback16/openjev:0.2.1 Docker. 400 plain-text for unaskable question.
     wire-compat ≠ logit-equiv. Error contract is not a Noul.
     Full cards: `judgment-class.md`, `validation.md`.
393. **von Option-Marker densify** (wfzyx/von):
     densify §49 + §99. Option-Marker joint attention 93.5% macro *theirs*.
     93.6% micro *theirs*. n=78. T = 1.0367 vs T = 1.1692 two temperatures.
     guaranteeing is soundness theater. 93.5% *theirs* not Harbor.
     Full cards: `validation.md`, `judgment-class.md`.
394. **verdict Heaven 74.9 densify** (Heman10x-NGU/openJev-verdict-2.0):
     densify §71. Benchmark Heaven leaderboard #2 74.9 *theirs*.
     NLL calibration assets. 77.10% still §71 claim-audit.
     do not re-fold as a beat. 74.9 *theirs* not Harbor.
     Full cards: `validation.md`.
395. **kev tarballs + PLAN_Qwen35** (jaredpalmer/kev):
     densify §45 / §98. kev-family weight tarballs. PLAN_Qwen35 proposal for review.
     deadline 0.53→0.82 at 9B *theirs*. Qwen3.5-9B ≠ Archer.
     isolation would fail by construction on DeltaNet.
     Full cards: `judgment-class.md`, `mixed-architecture.md`.
396. **jeff JevBench densify** (logan-markewich/jeff):
     densify §60. JevBench v1.2.2 jeff 66.9 (#9) jev 75.3 (#2) *theirs*.
     logan-markewich/jeff ≠ GestaltLabs/Jeff-1.
     Full cards: `validation.md`, `judgment-class.md`.
397. **TypeLLM thinking mode densify** (TypeLLM/TypeLLM):
     densify §113. thinking=True/False per-field budget.
     type safety does not guarantee factual accuracy.
     Thinking mode is constrained AR, not a Noul. Qwen/Qwen3.8-27B ≠ Archer.
     Full cards: `mixed-architecture.md`, `faq.md`.
398. **remainder clients / specs** (iPaste, jev-social, jev-local, Jev_from_GLiNER2):
     us/jev-local stub until hf. Eran-BA/Jev_from_GLiNER2 spec ≠ replica.
     Full cards: `faq.md`.
399. **name-match collisions** (Layan/Laya HF, layanan, lsu-ub-uu/systemone):
     Layan/Laya HF spaces name-match. lsu-ub-uu/systemone ≠ TypeSafe System One.
     catalog ≠ endorsement. Full cards: `faq.md`.
400. **skip-thin** (SystemOneEngine empty README, Hugo theme, thin name-match):
     SHA move is not a replica. skip-thin. Full cards: `faq.md`.

401. **openjev typesafe-sdk 0.7 densify PRIMARY** (razorback16/openjev):
     densify §75. typesafe-sdk 0.7 Pydantic response models. msgspec dropped.
     The server's output is unchanged and was never wrong. HEAD 6e91dfc031bc.
     Pydantic response models ≠ logit-equiv. msgspec dropped is not a replica.
     Full cards: `judgment-class.md`, `validation.md`.
402. **openjev MLX 400 error contract densify** (razorback16/openjev):
     SchemaError is 400 plain-string detail not 422 list.
     MLX backend 400 plain-text error contract. Error contract is not a Noul.
     wire-compat ≠ logit-equiv. Full cards: `validation.md`, `faq.md`.
403. **kev PLAN_Qwen35 densify PRIMARY** (jaredpalmer/kev):
     densify §45 / §98. HEAD 75cc15ddb8e2 PLAN SHA eca543246f50.
     corrected Qwen3.5 LoRA target names verified.
     in_proj_qkv in_proj_z in_proj_a in_proj_b out_proj. peft 0.21 existence proof.
     PLAN_Qwen35 still proposal for review. Qwen3.5-9B ≠ Archer.
     isolation would fail by construction on DeltaNet.
     Full cards: `judgment-class.md`, `mixed-architecture.md`.
404. **coverage-at-error-budget *theirs*** (jaredpalmer/kev Phase 0):
     OOD-calibration study. coverage-at-error-budget metric in Phase 0.
     coverage-at-error-budget *theirs* not Harbor. deadline 0.53→0.82 at 9B *theirs*.
     Full cards: `validation.md`.
405. **GLiNER locate ports cluster** (urchade / fbilhaut / lmoe / shershah1024):
     GLiNER locate ports are class members not Jev replicas.
     urchade/GLiNER ≠ fbilhaut/gline-rs ≠ lmoe/gliner-onnx.js ≠ shershah1024/gliner-native-runtime.
     Locate ≠ decide. densify §97 not a sibling. Full cards: `judgment-class.md`.
406. **Jev-Vision skip/effect/done *theirs*** (sseanliu/Jev-Vision):
     skip 0.936 effect 0.967 done 0.896 157 ms *theirs*.
     ~160 ms *theirs* not Harbor. HEAD dbd230b57fae README SHA 16d479e1d8b6.
     Wire `/v1/systemone`. trained on screens. specialist S1 ≠ hosted Jev.
     Full cards: `validation.md`, `judgment-class.md`.
407. **PII-Redaction-Tool 0.971 F1 *theirs*** (greeshma-ch/PII-Redaction-Tool):
     0.971 F1 *theirs* not Harbor. Locate ≠ decide. Span F1 is not a Noul.
     Full cards: `validation.md`.
408. **laya-gguf serving substrate** (hf:fr0stbit3/laya-gguf):
     hf:fr0stbit3/laya-gguf serving substrate ≠ calibrated replica.
     serving substrate ≠ calibrated replica. Full cards: `faq.md`, `judgment-class.md`.
409. **SystemOne-Next namesake** (jkcdarunday/SystemOne-Next):
     jkcdarunday/SystemOne-Next ≠ TypeSafe System One.
     catalog ≠ endorsement. Full cards: `faq.md`.
410. **already-catalogued Jev apps** (jev-search / jev-browser / reflex-lab / mcts-agent):
     densify is not a second census. SHA move is not a replica.
     Full cards: `applied-mappings.md`.
411. **remainder GLiNER locate serving** (anonde / docx-anonymizer / ampav-gliner / onnx-webgpu):
     Locate ≠ decide. class members not Jev replicas.
     Full cards: `judgment-class.md`.
412. **remainder Jev clients / routers / MCP judges**:
     catalog ≠ endorsement. wire-compat ≠ logit-equiv.
     Full cards: `faq.md`.
413. **hf fr0stbit3 multilingual / typed-decisions GGUF**:
     serving substrate ≠ calibrated replica. Softmax over options ≠ calibrated Noul.
     Full cards: `faq.md`.
414. **name-match collisions** (SystemOne* remainder, Jev playgrounds):
     jkcdarunday/SystemOne-Next ≠ TypeSafe System One. catalog ≠ endorsement.
     Full cards: `faq.md`.
415. **skip-thin** (empty README, marketing sites, 0★ name-match):
     SHA move is not a replica. skip-thin. Full cards: `faq.md`.
416. **skip Archer** (promised_not_landed):
     Qwen3.5-9B ≠ Archer. Hub archerhume/4rcherhume HTTP 401.
     Full cards: `faq.md`.


417. **openjev STE backends + Codiv densify PRIMARY** (razorback16/openjev):
     densify §75. HEAD cddbd962c88a README SHA a5943415cb92. 195★.
     vLLM NVIDIA + MLX Apple Silicon. Codiv hosted free endpoint.
     STE README rewrite. serving-port densify.
     Hosted Codiv ≠ TypeSafe. SHA move is not a replica.
     Full cards: `judgment-class.md`, `validation.md`.
418. **dual serving is not generate** (razorback16/openjev):
     dual /v1/systemone + /v1/chat/completions. chat 501 on MLX.
     dual serving is not generate. wire-compat ≠ logit-equiv.
     Error contract is not a Noul. Full cards: `faq.md`, `mixed-architecture.md`.
419. **Hosted Codiv ≠ TypeSafe** (openjev serving port):
     Codiv hosted free endpoint. Independent. Not affiliated.
     Hosted Codiv ≠ TypeSafe. serving substrate ≠ calibrated replica.
     Full cards: `faq.md`, `judgment-class.md`.
420. **jev-visual candidate scoring PRIMARY** (hr98w/jev-visual):
     167★ HEAD 19af545f096e README SHA 9f1cf521fc2b.
     Apple Silicon visual candidate scoring.
     candidate probabilities are relative not correctness.
     37.30s → 2.40s at 64 decisions *theirs*.
     hr98w/jev-visual ≠ sseanliu/Jev-Vision.
     Full cards: `judgment-class.md`, `validation.md`.
421. **Breakout 9 bricks *theirs*** (hr98w/jev-visual):
     Breakout 9 bricks 6 returns 2 lives *theirs*.
     80 decisions. simplified demo, not general game-playing.
     Full cards: `validation.md`.
422. **jev-mcp ten tools PRIMARY** (jkudish/jev-mcp):
     156★ HEAD 0b5a3f6d6f57 README SHA 1d7394500edd.
     ten MCP tools. recommendation is advisory.
     the server never blocks on its own.
     jkudish/jev-mcp ≠ burnigtm/jev-mcp.
     Full cards: `mixed-architecture.md`, `faq.md`.
423. **TypeSafe CLERC 5% to 18% *theirs*** (jkudish/jev-mcp rerank cookbook):
     TypeSafe CLERC 5% to 18% *theirs*. not Harbor.
     Full cards: `validation.md`.
424. **litjev off-the-shelf Qwen** (zhengxuyu/litjev):
     28★ HEAD f21216c9fe5a. off-the-shelf Qwen decision layer.
     Probabilities are not calibrated by default.
     Qwen/Qwen3.8-27B ≠ Archer.
     zhengxuyu/litjev ≠ alexwestco/llm-to-jev.
     Full cards: `judgment-class.md`, `faq.md`.
425. **Open-Jev LoRA + scalar head** (Zefan-Cai/Open-Jev):
     HEAD 6d8de5ed72a0. LoRA adapters plus a trained scalar decision head.
     2B 94.71% 9B 97.54% hard test *theirs*.
     LoRA ≠ RLCD replica.
     Zefan-Cai/Open-Jev ≠ TheoLeeCJ/openjev ≠ razorback16/openjev.
     Since last look 2026-09-21 densify: HEAD 4933ee84951f README SHA
     ce1a587219e4. not merged base models. Independent of TypeSafe.
     customer-service P50 local HTTP 85.03 ms vs Jev HTTPS 295.26 ms
     *theirs*. 1024 tokens/32 candidates Open-Jev slower 1015.90 vs
     301.37 *theirs*. systems latency ≠ semantic equivalence.
     prefix caching experimental/off by default.
     Full cards: `judgment-class.md`, `validation.md`.
426. **Open-Jev OOD + 27B in progress** (ZefanCai/Open-Jev-2B / 9B):
     2B OOD 86.02% 9B OOD 91.97% *theirs*. 80,816 training rows.
     27B still in progress. Hub 2B 0c7aa498b162 / 9B 47e966881e48.
     Since last look: dataset ZefanCai/Open-Jev rev c67699e13d0a.
     TREC-DL Jev/Luna/Astra completed. Open-Jev TREC pending.
     hard acc ≠ calibrated Noul. type-valid ≠ exact.
     GPT Luna P50 918.13 ms Astra 1938.39 ms *theirs*.
     website https://zefan-cai.github.io/open-jev/.
     densify §125 not a sibling first sighting.
     Full cards: `validation.md`.
427. **jeq pipe judgments** (cristianoliveira/jeq):
     3★ HEAD 44ea80c90903. intelligence you can pipe.
     pass-min 0.8 still soft. JEQ does not own actions.
     Full cards: `faq.md`, `mixed-architecture.md`.
428. **laya-coreai serving substrate** (hf:AndyInQtr/laya-coreai):
     AndyInQtr/laya-coreai CoreML serving substrate ≠ calibrated replica.
     AndyInQtr/laya-coreai ≠ mizorewww/laya-coreml.
     Full cards: `faq.md`, `judgment-class.md`.
429. **already-catalogued remainder** (pngwn/open-jev / jev-bench 401 / jevify / bonzi):
     densify is not a second census. SHA move is not a replica.
     Hub Praveenrajus/jev-bench HTTP 401. Full cards: `applied-mappings.md`.
430. **gate/router cousins measurement notes** (jev-gate / JevRoute / kev-model-router):
     rh-guard owns primary gates. catalog ≠ endorsement.
     Full cards: `faq.md`.
431. **skip-thin** (empty README, marketing sites, 0★ name-match):
     SHA move is not a replica. skip-thin. Full cards: `faq.md`.
432. **skip Archer** (promised_not_landed):
     Qwen/Qwen3.8-27B ≠ Archer. Hub archerhume/4rcherhume HTTP 401.
     Archer still promised_not_landed. Full cards: `faq.md`.


433. **TypeLLM densify PRIMARY** (TypeLLM/TypeLLM):
     densify §113. HEAD 6a48f9f1e623 README SHA dbdc1f193537. 16★.
     README densify 3k→12k B. thinking=True/False per-field budget.
     type safety does not guarantee factual accuracy.
     Constrained AR ≠ calibrated Noul. Qwen/Qwen3.8-27B ≠ Archer.
     Full cards: `judgment-class.md`, `validation.md`.
434. **TypeLLM Batch 5.8x *theirs*** (TypeLLM/TypeLLM):
     Sequential 9.35 s vs batch 1.61 s K=16 5.8x *theirs*.
     Batch 5.8x *theirs*. not Harbor.
     Full cards: `validation.md`.
435. **kev family densify PRIMARY** (jaredpalmer/kev):
     densify §45. HEAD b339f446a0ef README SHA 86b0a19909f3.
     Kev-0.6B 4B 8B family. 4B new-source 0.790/0.806 *theirs*.
     8B new-source 0.796/0.780 *theirs*. Jev hosted 0.857 *theirs*.
     Questions share the input text but cannot read each other.
     No Jev outputs were used for training. Qwen3 ≠ Archer.
     Full cards: `judgment-class.md`, `validation.md`.
436. **kev 8.2% / option-order *theirs*** (jaredpalmer/kev):
     8.2% ≥0.9 on wrong *theirs*. option order can change an answer.
     isolation ≠ option-order immunity. Full cards: `validation.md`.
437. **pi-jev fail-closed routing densify** (TheoOliveira/pi-jev):
     densify §42. 21★ fail-closed routing. JEV_THRESHOLD 0.65 still soft.
     routing ≠ permission. Full cards: `mixed-architecture.md`, `faq.md`.
438. **jev-sentinel fail closed** (harshwasan/jev-sentinel):
     8★ HEAD 4ae67df78c95. fail closed never auto-allows.
     harshwasan/jev-sentinel ≠ leepokai/jev-guard.
     rh-guard owns primary gates. Full cards: `faq.md`.
439. **MCP tool routers namesake** (jackbarunz/jev-tool-router ≠ esinocchi/jev-tool-router):
     jackbarunz/jev-tool-router ≠ esinocchi/jev-tool-router.
     threshold 0.90 still soft. none_of_the_above.
     Full cards: `faq.md`, `mixed-architecture.md`.
440. **76/81 routing bench *theirs*** (esinocchi/jev-tool-router):
     76/81 vs 77/81 *theirs*. 0.419s vs 2.459s *theirs*.
     $0.00486 vs $0.03673 *theirs*. does not execute.
     not a security boundary. Full cards: `validation.md`.
441. **leanest fail-open** (baronunread/leanest):
     fail-open uncertainty means RUN.
     classifier.dev default Jev/Laya pluggable.
     Full cards: `faq.md`, `mixed-architecture.md`.
442. **jevals estimates not Harbor** (openlayer-ai/jevals):
     estimates not Harbor. classifier ≠ authorizer.
     openlayer-ai/jevals ≠ dayhaysoos/jevals.
     Full cards: `validation.md`, `faq.md`.
443. **MrJev catalog** (MrJev/awesome-jev):
     118 entries catalog ≠ endorsement.
     MrJev/awesome-jev ≠ yibie/awesome-jev.
     Full cards: `faq.md`.
444. **jev-firewall fail closed** (Koushik890/jev-firewall):
     fail closed ask_below 0.7 still soft. Rules can only tighten.
     rh-guard owns primary gates. Full cards: `faq.md`.
445. **jev-codex-approval experimental** (CompleteTech-LLC-AI-Research/jev-codex-approval):
     experimental native not compiled.
     confidence is not a measured probability.
     Full cards: `faq.md`.
446. **HF encoder / quanto serving** (rAVEUK / p-yan / Gtrkrsk):
     hf:rAVEUK/open-jev-deberta-v3-large encoder class member not Jev replica.
     hf:p-yan/laya-quanto serving substrate ≠ calibrated replica.
     hf:Gtrkrsk/laya serving substrate ≠ calibrated replica.
     p-yan/laya-q8 and q4 Hub HTTP 401.
     Full cards: `judgment-class.md`, `faq.md`.
447. **already-catalogued remainder / skip-thin**:
     densify is not a second census. SHA move is not a replica.
     catalog ≠ endorsement. Full cards: `faq.md`.
448. **skip Archer** (promised_not_landed):
     Qwen3 ≠ Archer. Qwen/Qwen3.8-27B ≠ Archer.
     Hub archerhume/4rcherhume HTTP 401.
     Archer still promised_not_landed. Full cards: `faq.md`.

Hourly 1542 items 433–448 (`notes.md` §126). Do **not**
re-fold §125 items 417–432 / §124 items 401–416 / §123 items 385–400
/ §122 protocol / §121 items 369–384 / §120 items 353–368
/ §119 items 337–352 / §118 items 322–329 / §117 items 330–336
/ §116 items 309–316 / §115 items 303–308 / §114 items 289–302.
Skip Archer rewrite.
Constrained AR ≠ calibrated Noul; Batch 5.8x *theirs*;
4B new-source 0.790/0.806 *theirs*; 8.2% ≥0.9 on wrong *theirs*;
JEV_THRESHOLD 0.65 still soft; fail closed never auto-allows;
fail-open uncertainty means RUN; classifier ≠ authorizer;
estimates not Harbor; wire-compat ≠ logit-equiv;
SHA move is not a replica; catalog ≠ endorsement.
do not reopen or amend PR #23–#48.
Soft Noul ≠ hard safety.


Hourly 1441 items 417–432 (`notes.md` §125). Do **not**
re-fold §124 items 401–416 / §123 items 385–400 / §122 protocol / §121 items 369–384
/ §120 items 353–368 / §119 items 337–352 / §118 items 322–329
/ §117 items 330–336 / §116 items 309–316 / §115 items 303–308
/ §114 items 289–302.
Skip Archer rewrite.
dual serving is not generate; Hosted Codiv ≠ TypeSafe;
candidate probabilities are relative not correctness;
recommendation is advisory; LoRA ≠ RLCD replica;
pass-min 0.8 still soft; 37.30s → 2.40s at 64 decisions *theirs*;
2B 94.71% 9B 97.54% hard test *theirs*;
wire-compat ≠ logit-equiv;
SHA move is not a replica; catalog ≠ endorsement.
do not reopen or amend PR #23–#47.
Soft Noul ≠ hard safety.


Hourly 1340 items 401–416 (`notes.md` §124). Do **not**
re-fold §123 items 385–400 / §122 protocol / §121 items 369–384
/ §120 items 353–368 / §119 items 337–352 / §118 items 322–329
/ §117 items 330–336 / §116 items 309–316 / §115 items 303–308
/ §114 items 289–302.
Skip Archer rewrite.
Pydantic response models ≠ logit-equiv; msgspec dropped is not a replica;
Error contract is not a Noul; Locate ≠ decide;
coverage-at-error-budget *theirs* not Harbor; ~160 ms *theirs* not Harbor;
0.971 F1 *theirs* not Harbor; wire-compat ≠ logit-equiv;
SHA move is not a replica; catalog ≠ endorsement.
do not reopen or amend PR #23–#46.
Soft Noul ≠ hard safety.



Hourly 1248 items 385–400 (`notes.md` §123). Do **not**
re-fold §122 protocol / §121 items 369–384 / §120 items 353–368
/ §119 items 337–352 / §118 items 322–329 / §117 items 330–336
/ §116 items 309–316 / §115 items 303–308 / §114 items 289–302.
Skip Archer rewrite.
decide is not generate; GLiNER/GLiClass ports are class members not Jev replicas;
93.5% *theirs* not Harbor; 74.9 *theirs* not Harbor; 8.7x *theirs* not Harbor;
wire-compat ≠ logit-equiv; SHA move is not a replica; catalog ≠ endorsement.
do not reopen or amend PR #23–#45.
Soft Noul ≠ hard safety.

Hourly 1143 items 369–384 (`notes.md` §121). Do **not**
re-fold §120 items 353–368 / §119 items 337–352 / §118 items 322–329
/ §117 items 330–336 / §116 items 309–316 / §115 items 303–308 /
§114 items 289–302.
Skip Archer rewrite.
open recreation ≠ calibrated replica; semantic lint is a sensor not a proof;
cutoff 0.8 still soft; paired bootstrap CIs *theirs*;
Same accuracy, 35x faster *theirs*; systems comparison ≠ semantic equivalence;
permission ≠ confidence; catalog ≠ endorsement.
do not reopen or amend PR #23–#43.
Soft Noul ≠ hard safety.


Hourly 0947 items 337–352 (`notes.md` §119). Do **not**
re-fold §118 items 322–329 / §117 items 330–336 / §116 items 309–316
/ §115 items 303–308 / §114 items 289–302 / §113 items 273–288.
Skip Archer rewrite.
Qwen3.5-2B ≠ Archer. Qwen3.5-4B ≠ Archer.
judge ≠ actuator; softmax over A–H ≠ Noul; catalog ≠ endorsement.
do not reopen or amend PR #23–#40. Do not push onto open #39.
Soft Noul ≠ hard safety.

User-provided 0940 items 322–329 (`notes.md` §118). Do **not**
re-fold §114 items 289–302 / merged #36 §115 items 303–308 /
§113 altryne/jevify as this compiler. Merged #36 IDs left
alone. Merged #38 IDs left alone. Open #37 IDs left alone. Do not reopen #39.
Soft Noul ≠ hard safety.

Hourly 0646 items 248–267 (`notes.md` §111). Do **not**
re-fold 0541 items 226–247 / 0439 items 202–225 / 0345 items 186–201 / 0243 items 178–185 / 0145 items 161–177 / 0042 items 149–160 / 2340 items 138–148 / 2246 items 129–137 / 2145
items 120–128 / 2041 items 111–119 / 1943 items 102–110 /
1843 items 97–101 / 1740 items 94–96 / SIGNAL §93
mechanism / §60 six-gates / §78 v1.2 board / §71 claim-audit /
jev-judge-bench SLA-150 *contract* /
yuki-oshio/mini-jev *93.25%*.
Calibration is not alpha; ranking ≠ calibration theater;
default 0.5 keeps zero non pinned;
softmax over A/B/C ≠ Noul;
SemIf 2207★ (+21 vs §110 2186);
tracker likes 64 flat, lastModified UNCHANGED;
Laya likes 822 (was 802); Blackwood tracker ABSENT;
Archer still promised_not_landed;
do not reopen or amend PR #23/#24/#25/#26/#27/#28.
Soft Noul ≠ hard safety.

Hourly 0646 uniqueness lock: Calibration is not alpha; NO CURRENT ALPHA CANDIDATE; ΔR² approximately +0.00084; Brier 0.2131387; ECE 0.0421875; Adding Jev probability to deterministic volatility improved Brier by only 1.4058e-05; default 0.5 keeps zero non pinned; keepResult median 0.14 to 0.17; keepCall median 0.28 to 0.35; usable range is about 0.10 to 0.25; 7.8% to 57.9%; judges results it never sees; task-finish eval not built yet; $0.002 per compaction; slavadubrov/sgr-judge-bench ≠ slavadubrov/jev-judge-bench; Jev 108/120 $0.083 0.34 s; Luna SGR 114/120; paired Jev accuracy-difference intervals include zero; not evidence of equivalence; GLM SGR 26/120 93 format failures; Terra-planned Jev hybrid 55/120; rule-based by default, optionally Jev-backed; empty README; missing key cannot break the experience; prefill plus exactly one decode; softmax over A/B/C ≠ Noul; BBQ 9,053/10,000 (90.53%); ECE 0.0890; Mean confidence 0.9943; overconfident; score and noul not implemented; DGUI 12 rows (was 6); INSTRUCT 119 rows likes 2; encode the state once, decide everything in parallel; 0.740 accuracy against a 0.508 majority; ECE 0.047; fine-tune's advantage ends where its 384-token training data does; jasonkneen/open-jev ≠ pngwn/open-jev; same sha d41dc3cd; Space does not call Jev; recomputes routing from saved probabilities; 200-case Jev 97.0% / 100.0% / 95.0% / MAE 9.22; synthetic repository benchmark; Jev evaluations are advisory; YehuiTang0316/jev-nlgrep ≠ Bentlybro/jevgrep ≠ can1357/jegrep ≠ uehaj/jev-semgrep; default threshold 0.8 still soft; 40-line windows cannot prove whole function; token-native sequential start/end Choice; Gemini/Haiku stubs not configured yet; handful of hand-written examples, not a benchmark; Jev judged exactly what it was given; laguagu/jev-skills ≠ laguagu/jev-evidence-lab ≠ Pleo2/awesome-jev-agent-skills; contract_passed is not a claim of guaranteed factual truth; Wilson lower bound 0.85 floor; fixture mode no savings claim; SemIf 2207★ (+21 vs §110 2186); jevlike 1043★ (+5 vs 1038); TypeAR 15★ (+1 vs 14); AnotiaWang 97★ (+1 vs 96); yibie/awesome-jev 506★ (+16 vs 490); Laya likes 822 (was 802); tracker likes 64 flat, lastModified UNCHANGED; do not reopen or amend PR #23/#24/#25/#26/#27/#28.

Hourly 0541 items 226–247 (`notes.md` §110). Do **not**
re-fold 0439 items 202–225 / 0345 items 186–201 / 0243 items 178–185 / 0145 items 161–177 / 0042 items 149–160 / 2340 items 138–148 / 2246 items 129–137 / 2145
items 120–128 / 2041 items 111–119 / 1943 items 102–110 /
1843 items 97–101 / 1740 items 94–96 / SIGNAL §93
mechanism / §60 six-gates / §78 v1.2 board / §71 claim-audit /
yuki-oshio/mini-jev *93.25%*.
“0.9 is not one number”; ranking ≠ calibration;
Score is 0..n-1 expectation not 0–1;
Noul has no confidence field;
treating 0.85 as 85% / minProbability hard-gate as Harbor;
SemIf 2186★ (+20 vs §109 2166);
tracker likes 64 flat, lastModified UNCHANGED;
Laya likes 802 (was 783); Blackwood tracker ABSENT;
Archer still promised_not_landed;
do not reopen or amend PR #23/#24/#25/#26/#27.
Soft Noul ≠ hard safety.

Hourly 0541 uniqueness lock: GH jev-haiku-benchmarking 404; jevlike 1038★ (+7 vs 1031); TypeAR 14★ flat; AnotiaWang 96★ (+1 vs 95); yibie/awesome-jev 490★.

Hourly 0439 items 202–225 (`notes.md` §109). Do **not**
re-fold 0345 items 186–201 / 0243 items 178–185 / 0145 items 161–177 / 0042 items 149–160 / 2340 items 138–148 / 2246 items 129–137 / 2145
items 120–128 / 2041 items 111–119 / 1943 items 102–110 /
1843 items 97–101 / 1740 items 94–96 / SIGNAL §93
mechanism / §60 six-gates / §78 v1.2 board / §71 claim-audit /
yuki-oshio/mini-jev *93.25%*.
WANLI-256 64.5% / 60.2% / 52.0% *theirs*;
rank #4 / #5 / #6 of 6;
Awesomejev 656 entries / 38,160 stars;
tracker likes 64 (+4) lastModified UNCHANGED;
Laya present; Blackwood ABSENT; Archer still promised_not_landed;
do not reopen or amend PR #23/#24/#25/#26.
Soft Noul ≠ hard safety.

Hourly 0345 items 186–201 (`notes.md` §108). Do **not**
re-fold 0243 items 178–185 / 0145 items 161–177 / 0042 items 149–160 / 2340 items 138–148 / 2246 items 129–137 / 2145
items 120–128 / 2041 items 111–119 / 1943 items 102–110 /
1843 items 97–101 / 1740 items 94–96 / SIGNAL §93
mechanism / §60 six-gates / §78 v1.2 board / §71 claim-audit /
yuki-oshio/mini-jev *93.25%*.
Soft Noul ≠ hard safety.

Hourly 0243 items 178–185 (`notes.md` §107). Do **not**
re-fold 0145 items 161–177 / 0042 items 149–160 / 2340 items 138–148 / 2246 items 129–137 / 2145
items 120–128 / 2041 items 111–119 / 1943 items 102–110 /
1843 items 97–101 / 1740 items 94–96 / SIGNAL §93
mechanism / §60 six-gates / §78 v1.2 board / §71 claim-audit.
Soft Noul ≠ hard safety.

Hourly 0145 items 161–177 (`notes.md` §106). Do **not**
re-fold 0042 items 149–160 / 2340 items 138–148 / 2246 items 129–137 / 2145
items 120–128 / 2041 items 111–119 / 1943 items 102–110 /
1843 items 97–101 / 1740 items 94–96 / SIGNAL §93
mechanism / §60 six-gates / §78 v1.2 board.
Soft Noul ≠ hard safety.

Hourly 0843 uniqueness lock: A hunch is a probability with a policy attached; { enter: 0.8, exit: 0.6 } is hysteresis; replay a policy change without inference; Decision models are providers, not the product; huncho ≠ Kungie/gut ≠ carldaws/hunch ≠ tpellet/hunch; pretrained Qwen2.5 base ECE 0.030 (0.5B) / 0.040 (7B); instruct 0.302 / 0.269; 70.9% → 70.0% mean conf 74.1% → 96.7%; temperature scaling still matches it in-distribution; No Jev API was called; Qwen2.5 ≠ Archer; Qwen/Qwen3.8-27B ≠ Archer; 学習済みモデル v0.1 は準備中です; bool AUROC 0.523; 先頭だと0件、末尾だと250件; 温度を渡さない場合、確率は較正されていません; このリポジトリには Jev を呼ぶコードが存在しません; g0runmezadam/what-is-jev IS tunahansahin897/what-is-jev (same GitHub id 1378007307); 947 repos scored; A 273 · B 302 · C 372; LLM rubric ≠ benches; Data as of 2026-09-20; HEAD 895b9498; README SHA 3ae98c56; 13 focused checks and one mutually exclusive outcome; Probabilities are advisory, not calibrated guarantees; omni-/ask-jev ≠ pedroknigge/mcp_jev; pd.cut bins by equal width while jeval bins by quantile; ECE 0.113 and ECE 0.076; jeval drift is not implemented yet; rlaope/jeval ≠ dayhaysoos/jevals; calibration does not compose; ECE has exactly zero statistical power to detect the failure mode that kills trajectories; 25–60× headline withdrawn; P(all-correct): 0.0071 vs 0.0001; TCE / AMS; Qwen 3.8 sparring ≠ Archer; Deferred Crispification; light_cutoff_applied_to_combination 0; recorded run, kinematic animation; BANKING77 Accuracy BERT-Base 93.02 Jev 79.90; Analyse jev calibration (NLL, ECE) backlog; BERT figures are published supervised references, not zero-shot; 档位措辞效应 分数极差中位 0.50、最大 1.32; 修好后对照组是 0.01; 不是 benchmark; 概率没做 calibration; ~1,430 API calls, about $0.15; xiaohuaxi/jev-study ≠ wjdjdakf17/jev-study ≠ baekenough/jev-study; AND: product (independence assumed and recorded in the trace); chat model's stated confidence is not calibrated; circuit-vl-4b ≠ Archer; Bring your own API key; vamsikrishna2421/jev-usecases ≠ whyashthakker/awesome-jev-use-cases; catalog ≠ endorsement; SemIf 2237★ (+30 vs §111 2207); jevlike 1049★ (+6 vs 1043); TypeLLM/TypeLLM 16★; AnotiaWang 98★; yibie/awesome-jev 520★ (+14 vs 506); Laya likes 861 (was 822); tracker likes 66 (+2 vs 64) lastModified UNCHANGED; Blackwood likes 2 gated manual; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35; notes.md §114

User-provided 0920 jcr uniqueness lock: NiazMorshed2007/jcr MIT; site https://jcr.niazmorshed.dev; topics ai-agents,jev,mcp; **4★**; HEAD `138b3832`; README SHA `2a49dbc1`; LICENSE SHA `46231303`; size **14850**; Jev Capability Resolver; one tool to find documented deterministic commands in a nested capability tree; returns context; **does not execute**; skills = workflow+judgment; capabilities = individual operations; format independent of Jev; proposed open standard exploration; classify (Jev) → optional OpenAI decompose compound → beam search geometric mean of routing probs; keep up to 3 paths ≥60% of best (JCR_BAND_RATIO 0.6); ambiguity / no-match / depth-limit explicit; soft scores ≠ hard gates; 0.6 band is application policy; routing ≠ permission; docs ≠ authority to run; sol-vs-opus5-20 *theirs*: 20 scenarios × 4 variants = 80 runs; lookup+explain only, no execution; Claude Opus 5: agent input 108,585→15,819 (−85%), cost $0.3700→$0.1222 (−67%), wall 105.5s→77.7s; Codex GPT-5.6-Sol: 61,952→47,669 (−23%), $0.1377→$0.1151 (−16%), wall 25.3s→62.4s (Sol slower with JCR in 19/20); One Sol outlier 372.6s / 193 Jev calls; n=1 per cell; Not Harbor task-execution; Claude/Codex harnesses; compare mode; 50 scenarios bundled; 11 groups, 960 nodes, 11,360 items; 16 routing rounds per step; NiazMorshed2007/jcr ≠ skill-broker ≠ skillranker ≠ jev-sift ≠ jev-lens ≠ jevusher ≠ jev_select_capability; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34; notes.md §116
User-provided 0922 uniqueness lock: SemIf was formerly OpenJev; independent; not affiliated with Jev or TypeSafe; homepage openjev.com; default master; MIT; HEAD ca3ba65f1429; Tolerate float roundoff in MLX evidence verification; pushed 2026-09-19; live REST 2282★ / 140 forks; size 9177; README SHA 74ab7f7f; LICENSE SHA ca562883; interface pattern reproduction with open models; does not reproduce Jev undisclosed model/training; Direct option logits; 0 output tokens; shared-state parallel; MLX backend for Apple Silicon (`--backend mlx`); Qwen3.5-4B 3090 direct 1.023s vs AR JSON 5.332s (**5.21×**); argmax agree 18/21; systems comparison ≠ semantic equivalence; Parallel suffixes 20.03 dec/s on 777 decisions; Browser ladder Qwen3.5-4B authored BA 0.813, pert 0.766, TypeSafe subset agreement 0.845 vs Published Jev 0.883 (102 across 20 cases); Softmax over options ≠ calibrated Noul; typed output does not guarantee semantic correctness; wire/agreement ≠ replica of TypeSafe; SemIf ≠ kw2828/OpenJev playground ≠ zhihz/openjev ≠ apiplant/semif-rs port ≠ dddanielliu/semif-serve; rename is densify not a second census; JevBench 74.6 is §78 not this ladder; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#38; do not push onto open #39/#40; notes.md §117
User-provided 0940 uniqueness lock: Turn decision-shaped LLM prompts into proposed Jev primitives; This is a conversion assistant, not an automatic guarantee of equivalent behavior; The compiler uses deterministic heuristics, not an LLM or evaluation model; It understands a deliberately small set of common prompt patterns; Generated instructions and criteria must be reviewed before production use; Score ranges such as 0 to 1 are translated into ordered Jev criteria; Prompts requiring open-ended prose are not a fit; suitability strong/partial/not_a_fit; compatibility full/partial/none; Writing new text stays with an LLM; Review the generated Score rubric; Jev scores ordered criteria, not an arbitrary 0-to-1 range; Everything runs locally in the browser; There is no framework, database, account, API, or server-side prompt processing; The key is read from the process environment and is never stored or printed; connect-src 'none'; alexwestco/llm-to-jev ≠ altryne/jevify ≠ ryana/jevify ≠ fidecastro/jevify ≠ Mintzs/jevify ≠ gulagala001/jevify ≠ uspraveen/Jevify; HEAD 234058ab372d; README SHA 43cd94fb; LICENSE SHA 5f334006; compiler SHA fdf235d0; 2★; MIT; JavaScript; size 29; Pages https://alexwestco.github.io/llm-to-jev/; invented_signal false; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35; notes.md §118
Hourly 0947 uniqueness lock: Fast and cheap agent evals. jev as judge.; 18,041 skills from the 200 most-starred repos; Not a security scanner; 最简 Jev 调用演示器; confidence 不是正确率; q93304989-bit/jev-lab ≠ tanayvasishtha/jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab ≠ yibie/laya-jev-lab; 75% cheaper and 18% faster withdrawn; jev @0.15 100% recall 87% savings; 33Audits/jev-auto ≠ gargpratyush/jev-router; no Typesafe key, no PI_API_BASE, zero deps; tool-emitted Score/Noul ≠ calibrated Noul; semantic_compatibility: false; candidate_mass; Qwen3.5-2B ≠ Archer; Jev evaluates decisions; it cannot run a coding-agent session; Status: no model yet; S1LV3RJ1NX/openjev ≠ TheoLeeCJ/openjev; 28 accepted decisions; 3 targets; score 800; health 100; arcade game not a flight trainer; A successful live TypeSafe call has not been verified for v0.1.0; abhibansal60/tidy ≠ MANISH007700/tidy; No model, Jev included, predicted which channels its owner keeps; seed 1 selected on a held-out 400-item validation split; Brier 0.342 → 0.378; more accurate and more overconfident; Qwen3.5-4B ≠ Archer; static quants of kushalpatil/jevify-gemma4-26b-a4b; The labels were corrected, and one earlier result was retracted; zero of 23,869 eligible rows; Do not compare cost without checking task success; Exit 1 is not a proof; kisshan13/typesafe-ai-go ≠ Nibir1/typesafe-go ≠ official; 38 tests that cannot fail in a 356-model warehouse; if a parser can answer it, Jev is never asked; 359 of them; Games & Simulation 82; Education & Learning 1; Ratings are heuristics; syedabbasshaheer-art/jev-atlas ≠ ZeroX-01/jev-atlas ≠ Zaious/jev-capability-atlas ≠ gorock007/jev-atlas; anandi1989/awesome-jev-usecases ≠ whyashthakker/awesome-jev-use-cases ≠ walidboulanouar/awesome-jev-use-cases ≠ vamsikrishna2421/jev-usecases; Every headline result above is self-reported; Archer Hume 84.6% MMLU-Pro is a third-party probe not landed Archer; catalog ≠ endorsement; judge ≠ actuator; softmax over A–H ≠ Noul; SemIf 2270★; jevlike 1054★; TypeLLM/TypeLLM 16★; AnotiaWang 98★; yibie/awesome-jev 538★; Laya likes 889; tracker likes 68 lastModified UNCHANGED; Blackwood likes 2 gated manual; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#35/#36/#37/#38/#40; do not push onto open #39; notes.md §119
Hourly 1049 uniqueness lock: ggmlc GGUF is not llama.cpp; Loading them in llama.cpp will fail; one encoder pass; hf:mys/laya-GGUF sha 713ae6f6e39f likes 0 apache-2.0; hf:mys/laya-multilingual-GGUF sha 3b645ae54281; hf:mys/laya-typed-decisions-GGUF sha 1e9e8ba1f527; hf:tozp/laya-onnx sha 0862aeba1e65 Opset 14 FP32 and INT8; tozp/laya-onnx ≠ Mattepiu/laya-onnx ≠ gqgs/laya-onnx; docker-laya MIT HEAD 1b8239a51ddd README SHA 9cb7bdc3; laya.cpp RTX ggml CUDA HEAD 8590937c79a2 README SHA cdd429b9; serving substrate ≠ calibrated replica; Softmax over options ≠ calibrated Noul; Qwen3.5-4B ≠ Archer; Qwen3.5-9B ≠ Archer; jev-position-test n=6 HEAD 7a56ca1c2698 README SHA 23f194c9; jevmlx slots 5 of 6; hosted Jev 0 of 6; prior_correction made it worse; jevSweeper mean Spearman ρ −0.274; picked exact-optimal 1/25 (4%); 31 of 36 still logically decidable; 86% of the time we should not have been asking; game success ≠ calibrated Noul; LLM2Jev 64★ Apache-2.0 HEAD 924618721277 README SHA da35fe61; not affiliated with or endorsed by Jev or TypeSafe; No answer tokens are generated; OpenSourceJev llama.cpp Qwen3-1.7B HEAD 3c41fba3681d; JEV-MLX Qwen3.5-9B HEAD dec24cd929ea; decision-head-rlcd Qwen3.5-4B 4.9M LoRA; AUTO_ACT is not a Noul; closed-set fail-open stdlib-only; verified=False; soft scores ≠ hard gates; 22 to 40% cheaper *theirs*; first version 70% more expensive; 111-case benchmark *theirs*; CDC 5,000 Jev 72.2% AUC 0.7725 *theirs*; accuracy is a trap; 9.0% base rate always-no 91.0%; catalog ≠ endorsement; jev-skill 109★ 90 scenarios HEAD 4f6e899a24d4; awesome-jev-live 673 entries 4★; minecraft-agent 214★ 131 JEV decisions 35 Astra calls; nether-final-08 8 minutes 43.300 seconds; planner writes JEV selects; RoboJEV structured simulator state not images; ashare-trader 策略未通过自己的回测门槛; 36 组参数全部净期望为负; no positive expectation under real costs; typed_evals NOT an official TypeSafe AI product; jev-as-judge is a sensor; third-person-audit 40% & 60% watermarks still soft; The included experience uses a handwritten demo provider; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42; notes.md §120


**Hourly 1143 HIGH (`notes.md` §121).** open recreation ≠ calibrated replica. semantic lint is a sensor not a proof. cutoff 0.8 still soft. paired bootstrap CIs *theirs*. Same accuracy, 35x faster *theirs*. systems comparison ≠ semantic equivalence. serving substrate ≠ calibrated replica. catalog ≠ endorsement. permission ≠ confidence. Do not reopen or amend PR #23–#43. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1143 uniqueness lock: open recreation ≠ calibrated replica; Qwen3.5-4B ≠ Archer; It is an open re-creation of Jev; less calibrated; perch 164★ MIT HEAD ba775a9940b6 README SHA 7ad0403b; semantic lint is a sensor not a proof; oxlint-plugin-jev cutoff 0.8 still soft; nassim-arifette/jevgrep ≠ Bentlybro/jevgrep ≠ can1357/jegrep ≠ uehaj/jev-semgrep; patdown fuzzy linter; PanAchy/jevvy ≠ Atominac/jevvy; No orders, no advice; SmartMoney-Cub 25★ HEAD d93cf493853d; paired bootstrap CIs *theirs*; emretheus/jev-rag-benchmark ≠ erendikmenn/jev-rag-benchmark; +0.82 pts XQuAD-EN 95% CI +0.35 to +1.31; +7.62 pts SciFact CI +4.88 to +10.38; Same accuracy, 35x faster *theirs*; systems comparison ≠ semantic equivalence; BANKING77 500 Jev 81.0% GPT-OSS 82.8% Mercury 73.2% Gemini 85.4% *theirs*; frozen cascade missed its evaluation accuracy target 430/500 vs GPT-5 432/500; This is not demonstrated equal-quality savings; 24 invented tickets; Routing errors caught by the gate 0 of 3; sample too small to establish calibration; This is not TypeSafe Jev; No real API requests were made; wire-compat ≠ replica; KonghaYao/laya-jev 按官方接口写的客户端只改一个 base URL; gqgs/laya-onnx densify 496.8 MiB; tozp/laya-onnx ≠ Mattepiu/laya-onnx ≠ gqgs/laya-onnx; serving substrate ≠ calibrated replica; BeatAPI/awesome-jev ≠ 99hansling/awesome-jev ≠ Vishnurr2k01/awesome-jev ≠ robokrunch/awesome-jev ≠ rudy2steiner/awesome-jev-hub; All 125 projects; catalog ≠ endorsement; Pasblinn/jev-lab ≠ tanayvasishtha/jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab ≠ yibie/laya-jev-lab ≠ q93304989-bit/jev-lab; Independent project. Not affiliated with TypeSafe; Kevthetech143/super-jev densify experimental V0.2.0; permission ≠ confidence; allay-team/openjev ≠ piyush-infocusp/openjev ≠ TheoLeeCJ/openjev; 2022 Mineflayer Jevalent collision; kushalpatil/jevify-gemma4-e4b GGUF densify; static quants; This dataset and model are independent research artifacts, not reproductions of Jev or RLCD; pngwn demo accuracy 0.705 ECE 0.046 ~112 ms *theirs*; cutoff 0.8 still soft; soft scores ≠ hard gates; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43; notes.md §121

**Hourly 1248 HIGH (`notes.md` §123).** decide is not generate. tryDecide returns typed calibrated judgments not a token stream. GLiNER/GLiClass ports are class members not Jev replicas. 93.5% *theirs* not Harbor. 74.9 *theirs* not Harbor. 8.7x *theirs* not Harbor. wire-compat ≠ logit-equiv. SHA move is not a replica. catalog ≠ endorsement. Do not reopen or amend PR #23–#45. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1248 uniqueness lock: decide is not generate; tryDecide returns typed calibrated judgments not a token stream; juspay/neurolink 133★ MIT HEAD 268b0fe83130 README SHA e709cadfa6b6 tag v12.19.0; GLiNER/GLiClass ports are class members not Jev replicas; MacPaw/Gliner2Swift ≠ Knowledgator/GLiClass.c ≠ fbilhaut/gliclass-rs ≠ Knowledgator/GLiClass.js ≠ gravitee-io/GLiNER4j ≠ apiplant/gliner-rs ≠ codesoda/gliner2-rs; 8.7x faster 4.4x fewer prompts *theirs*; 153 was a reporting error; corrected 156-case 9.8x faster 4.2x fewer prompts *theirs*; independent v0.2.1 1.24x vs Mini *theirs*; Approvals only; anpicasso/hermes-jev-approvals ≠ hermes-switchyard; scx-router GLiClass ranks candidate LLMs in one non-generative pass; typesafeai-dotnet-sdk Not affiliated with TypeSafe AI; hyperspaceai/jevcache ≠ kushals256/jevcache; ST-jeved measures each reply; 400 plain-text for unaskable question; razorback16/openjev:0.2.1 Docker densify HEAD 794a81b87131; wire-compat ≠ logit-equiv; Option-Marker joint attention 93.5% macro *theirs*; 93.6% micro *theirs*; n=78; T = 1.0367 vs T = 1.1692 two temperatures; guaranteeing is soundness theater; wfzyx/von densify HEAD bed7e7337791; Benchmark Heaven leaderboard #2 74.9 *theirs*; NLL calibration assets; 77.10% still §71 claim-audit; do not re-fold as a beat; Heman10x-NGU/openJev-verdict-2.0 densify HEAD bff28567cff4; kev-family weight tarballs; PLAN_Qwen35 proposal for review; deadline 0.53→0.82 at 9B *theirs*; Qwen3.5-9B ≠ Archer; isolation would fail by construction on DeltaNet; jaredpalmer/kev densify; JevBench v1.2.2 jeff 66.9 (#9) jev 75.3 (#2) *theirs*; logan-markewich/jeff densify HEAD 34b32f99a727; thinking=True/False per-field budget; type safety does not guarantee factual accuracy; TypeLLM/TypeLLM densify HEAD c4b03ba9e792; us/jev-local stub until hf; Eran-BA/Jev_from_GLiNER2 spec ≠ replica; lsu-ub-uu/systemone ≠ TypeSafe System One; Layan/Laya HF spaces name-match; catalog ≠ endorsement; decide ≠ generate ≠ stream; 93.5% *theirs* not Harbor; 74.9 *theirs* not Harbor; 8.7x *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45; notes.md §123

**Hourly 1340 HIGH (`notes.md` §124).** typesafe-sdk 0.7 Pydantic response models. msgspec dropped. MLX backend 400 plain-text error contract. Pydantic response models ≠ logit-equiv. msgspec dropped is not a replica. Error contract is not a Noul. PLAN_Qwen35 densify. coverage-at-error-budget *theirs* not Harbor. GLiNER locate ports are class members not Jev replicas. Locate ≠ decide. ~160 ms *theirs* not Harbor. SHA move is not a replica. catalog ≠ endorsement. Do not reopen or amend PR #23–#46. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1340 uniqueness lock: typesafe-sdk 0.7 Pydantic response models; msgspec dropped; The server's output is unchanged and was never wrong; MLX backend 400 plain-text error contract; SchemaError is 400 plain-string detail not 422 list; razorback16/openjev densify HEAD 6e91dfc031bc README SHA cbdcc8de0304; Pydantic response models ≠ logit-equiv; msgspec dropped is not a replica; Error contract is not a Noul; wire-compat ≠ logit-equiv; PLAN_Qwen35 densify; corrected Qwen3.5 LoRA target names verified; in_proj_qkv in_proj_z in_proj_a in_proj_b out_proj; peft 0.21 existence proof; OOD-calibration study; coverage-at-error-budget metric in Phase 0; PLAN_Qwen35 still proposal for review; deadline 0.53→0.82 at 9B *theirs*; isolation would fail by construction on DeltaNet; Qwen3.5-9B ≠ Archer; jaredpalmer/kev densify HEAD 75cc15ddb8e2 PLAN SHA eca543246f50; GLiNER locate ports are class members not Jev replicas; urchade/GLiNER ≠ fbilhaut/gline-rs ≠ lmoe/gliner-onnx.js ≠ shershah1024/gliner-native-runtime; Locate ≠ decide; Jev-Vision skip 0.936 effect 0.967 done 0.896 157 ms *theirs*; ~160 ms *theirs* not Harbor; 0.971 F1 *theirs* not Harbor; coverage-at-error-budget *theirs* not Harbor; hf:fr0stbit3/laya-gguf serving substrate ≠ calibrated replica; jkcdarunday/SystemOne-Next ≠ TypeSafe System One; catalog ≠ endorsement; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46; notes.md §124

**Hourly 1441 HIGH (`notes.md` §125).** vLLM NVIDIA + MLX Apple Silicon. Codiv hosted free endpoint. dual /v1/systemone + /v1/chat/completions. chat 501 on MLX. dual serving is not generate. Hosted Codiv ≠ TypeSafe. candidate probabilities are relative not correctness. recommendation is advisory. the server never blocks on its own. LoRA ≠ RLCD replica. pass-min 0.8 still soft. 37.30s → 2.40s at 64 decisions *theirs*. 2B 94.71% 9B 97.54% hard test *theirs*. wire-compat ≠ logit-equiv. SHA move is not a replica. catalog ≠ endorsement. Do not reopen or amend PR #23–#47. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1441 uniqueness lock: vLLM NVIDIA + MLX Apple Silicon; Codiv hosted free endpoint; dual /v1/systemone + /v1/chat/completions; razorback16/openjev densify HEAD cddbd962c88a README SHA a5943415cb92; STE README rewrite; serving-port densify; chat 501 on MLX; dual serving is not generate; Hosted Codiv ≠ TypeSafe; wire-compat ≠ logit-equiv; SHA move is not a replica; Error contract is not a Noul; hr98w/jev-visual 167★ Apple Silicon visual candidate scoring; 37.30s → 2.40s at 64 decisions *theirs*; Breakout 9 bricks 6 returns 2 lives *theirs*; candidate probabilities are relative not correctness; jkudish/jev-mcp 156★ ten MCP tools; recommendation is advisory; the server never blocks on its own; TypeSafe CLERC 5% to 18% *theirs*; jkudish/jev-mcp ≠ burnigtm/jev-mcp; zhengxuyu/litjev off-the-shelf Qwen decision layer; Probabilities are not calibrated by default; Qwen/Qwen3.8-27B ≠ Archer; zhengxuyu/litjev ≠ alexwestco/llm-to-jev; Zefan-Cai/Open-Jev LoRA + scalar head; 2B 94.71% 9B 97.54% hard test *theirs*; 2B OOD 86.02% 9B OOD 91.97% *theirs*; 80,816 training rows; 27B still in progress; LoRA ≠ RLCD replica; Zefan-Cai/Open-Jev ≠ TheoLeeCJ/openjev ≠ razorback16/openjev; cristianoliveira/jeq intelligence you can pipe; pass-min 0.8 still soft; JEQ does not own actions; AndyInQtr/laya-coreai CoreML serving substrate ≠ calibrated replica; AndyInQtr/laya-coreai ≠ mizorewww/laya-coreml; catalog ≠ endorsement; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47; notes.md §125


**Hourly 1542 HIGH (`notes.md` §126).** TypeLLM README densify 3k→12k B. Batch 5.8x *theirs*. Constrained AR ≠ calibrated Noul. kev family densify. 4B new-source 0.790/0.806 *theirs*. 8.2% ≥0.9 on wrong *theirs*. option order can change an answer. fail-closed routing vs fail-open test selection. classifier ≠ authorizer. estimates not Harbor. catalog ≠ endorsement. SHA move is not a replica. Do not reopen or amend PR #23–#48. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1542 uniqueness lock: TypeLLM/TypeLLM densify HEAD 6a48f9f1e623 README SHA dbdc1f193537; README densify 3k→12k B; thinking=True/False per-field budget; type safety does not guarantee factual accuracy; Batch 5.8x *theirs*; Constrained AR ≠ calibrated Noul; Qwen/Qwen3.8-27B ≠ Archer; jaredpalmer/kev densify HEAD b339f446a0ef README SHA 86b0a19909f3; Kev-0.6B 4B 8B family; 4B new-source 0.790/0.806 *theirs*; 8B new-source 0.796/0.780 *theirs*; Jev hosted 0.857 *theirs*; Questions share the input text but cannot read each other; No Jev outputs were used for training; 8.2% ≥0.9 on wrong *theirs*; option order can change an answer; Qwen3 ≠ Archer; wire-compat ≠ logit-equiv; SHA move is not a replica; TheoOliveira/pi-jev 21★ fail-closed routing; JEV_THRESHOLD 0.65 still soft; routing ≠ permission; harshwasan/jev-sentinel fail closed never auto-allows; harshwasan/jev-sentinel ≠ leepokai/jev-guard; jackbarunz/jev-tool-router ≠ esinocchi/jev-tool-router; threshold 0.90 still soft; 76/81 vs 77/81 *theirs*; 0.419s vs 2.459s *theirs*; $0.00486 vs $0.03673 *theirs*; does not execute; not a security boundary; baronunread/leanest fail-open uncertainty means RUN; classifier.dev default Jev/Laya pluggable; openlayer-ai/jevals ≠ dayhaysoos/jevals; estimates not Harbor; classifier ≠ authorizer; MrJev/awesome-jev 118 entries catalog ≠ endorsement; MrJev/awesome-jev ≠ yibie/awesome-jev; Koushik890/jev-firewall fail closed ask_below 0.7 still soft; CompleteTech-LLC-AI-Research/jev-codex-approval experimental native not compiled; confidence is not a measured probability; rh-guard owns primary gates; hf:rAVEUK/open-jev-deberta-v3-large encoder class member not Jev replica; hf:p-yan/laya-quanto serving substrate ≠ calibrated replica; hf:Gtrkrsk/laya serving substrate ≠ calibrated replica; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48; notes.md §126

449. **openjev 0.3.0 densify PRIMARY** (razorback16/openjev):
     densify §75. HEAD febf02e88989 README SHA 242a737dba01. 200★.
     release 0.3.0. re-pin vLLM PR #57250 restructured head.
     pyproject and __init__ agree 0.3.0. MODEL_VERSION stays openjev-0.1.
     uv.lock hygiene. SHA move is not a replica.
     Full cards: `judgment-class.md`, `validation.md`.
450. **restructured vLLM head ≠ logit-equiv** (razorback16/openjev):
     VLLM_COMMIT baa8338. subclass DiffusionAsyncScheduler.
     restructured vLLM head ≠ logit-equiv. wire-compat ≠ logit-equiv.
     dual serving is not generate. Hosted Codiv ≠ TypeSafe.
     Error contract is not a Noul. Full cards: `faq.md`, `mixed-architecture.md`.
451. **clean-code-review typed judgments** (frostney/clean-code-review):
     7★ HEAD f020f8d9106d. typed judgments not opinions.
     documentation is read not judged. Luna writes from Jev findings.
     frostney/clean-code-review ≠ huntedman/JevLint.
     Full cards: `mixed-architecture.md`, `validation.md`.
452. **JMP route vs generate** (morcoan/JMP):
     Joint Model Participation. Models participate. Real tools execute.
     Jev routes actions generators supply arguments. not a swarm.
     decide is not generate. Full cards: `faq.md`, `mixed-architecture.md`.
453. **jevbus thresholds are policy** (zkjoie/jevbus):
     Thresholds are policy not model. Drop < Review < Deliver.
     FanOut or Exclusive. Full cards: `faq.md`, `validation.md`.
454. **Kelbie/hunch namesake** (Kelbie/hunch):
     Agent Skills semantic review.
     Kelbie/hunch ≠ carldaws/hunch ≠ tpellet/hunch ≠ huncho.
     Full cards: `faq.md`.
455. **JevCanvas decide vs diffusion** (SupratikB23/JevCanvas):
     Jev never generates prose JSX or code. Diffusion never decides structure.
     json-render is the only renderer. Full cards: `mixed-architecture.md`.
456. **jevtrafficsim game success ≠ Noul** (skcache/jevtrafficsim):
     Fixed Adaptive Jev. game success ≠ calibrated Noul.
     Full cards: `validation.md`.
457. **remainder namesakes** (open-jev / laya-onnx / jev-use / switchboard / tidy / jevkit / jev-tree):
     Shalimov04/open-jev ≠ razorback16/openjev ≠ TheoLeeCJ/openjev ≠ Zefan-Cai/Open-Jev.
     MstyAI/laya-onnx empty repo ≠ tozp/laya-onnx ≠ Mattepiu/laya-onnx ≠ gqgs/laya-onnx.
     SherifAshraf2003/jev-use ≠ shitianfang/jev-use.
     aniruddh-krovvidi/switchboard ≠ cannacre8ive/switchboard-ai.
     Visorian/TidyUp ≠ abhibansal60/tidy. isiomaC/jevkit ≠ WaynezProg/jev-kit.
     lee-lou2/jev-tree ≠ reachjalil/jev-tree.
     Full cards: `faq.md`.
458. **empty repos skip-thin** (MstyAI/laya-onnx, Royhu1/jev-poker-trainer):
     empty repo ≠ serving substrate. Royhu1/jev-poker-trainer empty repo.
     skip-thin. Full cards: `faq.md`.
459. **NaluKicks field trial / guide / bench**:
     pre-registered field trial. vault-search-bench uses vault links as the answer key.
     *theirs* not Harbor. Full cards: `validation.md`.
460. **HF already-catalogued densify** (Praveenrajus / ZefanCai / emretheus / DGUI / INSTRUCT):
     hf:Praveenrajus/jev-bench HTTP 200 was 401. densify is not a second census.
     hf:ZefanCai/Open-Jev densify dataset. LoRA ≠ RLCD replica.
     hf:emretheus/jev-rag-benchmark ≠ erendikmenn/jev-rag-benchmark.
     hf:ctaxnagomi/DGUI_HYPERMEM-JEV densify sha ab3d3529.
     Full cards: `applied-mappings.md`.
461. **HF first-sighting spaces** (fastrisk / yolo-jev / deberta demo / r512):
     hf:hugging-apps/open-jev-deberta-v3-large-demo encoder class member not Jev replica.
     serving substrate ≠ calibrated replica. Locate ≠ decide.
     Full cards: `judgment-class.md`, `faq.md`.
462. **router cousins measurement notes** (jev-harness-router / pi-jev-model-router / pi-auto-model-router):
     JoacoMarc/jev-harness-router ≠ jackbarunz/jev-tool-router.
     rh-guard owns primary gates. catalog ≠ endorsement.
     Full cards: `faq.md`.
463. **skip-thin** (empty README, marketing sites, 0★ name-match):
     SHA move is not a replica. skip-thin. Full cards: `faq.md`.
464. **skip Archer** (promised_not_landed):
     Qwen3 ≠ Archer. Hub archerhume/4rcherhume HTTP 401.
     Archer still promised_not_landed. Full cards: `faq.md`.

Hourly 1643 items 449–464 (`notes.md` §127). Do **not**
re-fold §126 items 433–448 / §125 items 417–432 / §124 items 401–416
/ §123 items 385–400 / §122 protocol / §121 items 369–384.
Skip Archer rewrite.
restructured vLLM head ≠ logit-equiv; Thresholds are policy not model;
documentation is read not judged; json-render is the only renderer;
game success ≠ calibrated Noul; wire-compat ≠ logit-equiv;
SHA move is not a replica; catalog ≠ endorsement.
do not reopen or amend PR #23–#49.
Soft Noul ≠ hard safety.
**Hourly 1643 HIGH (`notes.md` §127).** openjev release 0.3.0 densify. re-pin vLLM PR #57250 restructured head. restructured vLLM head ≠ logit-equiv. MODEL_VERSION stays openjev-0.1. dual serving is not generate. Hosted Codiv ≠ TypeSafe. typed judgments not opinions. Thresholds are policy not model. Jev never generates prose JSX or code. game success ≠ calibrated Noul. catalog ≠ endorsement. SHA move is not a replica. Do not reopen or amend PR #23–#49. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1643 uniqueness lock: razorback16/openjev densify HEAD febf02e88989 README SHA 242a737dba01; release 0.3.0; re-pin vLLM PR #57250 restructured head; VLLM_COMMIT baa8338; pyproject and __init__ agree 0.3.0; MODEL_VERSION stays openjev-0.1; uv.lock hygiene; dual serving is not generate; Hosted Codiv ≠ TypeSafe; restructured vLLM head ≠ logit-equiv; wire-compat ≠ logit-equiv; SHA move is not a replica; Error contract is not a Noul; frostney/clean-code-review 7★ typed judgments not opinions; documentation is read not judged; Luna writes from Jev findings; morcoan/JMP Joint Model Participation; Models participate. Real tools execute.; Jev routes actions generators supply arguments; not a swarm; zkjoie/jevbus Thresholds are policy not model; Drop < Review < Deliver; FanOut or Exclusive; Kelbie/hunch ≠ carldaws/hunch ≠ tpellet/hunch ≠ huncho; Agent Skills semantic review; SupratikB23/JevCanvas Jev never generates prose JSX or code; Diffusion never decides structure; json-render is the only renderer; skcache/jevtrafficsim Fixed Adaptive Jev; game success ≠ calibrated Noul; Shalimov04/open-jev ≠ razorback16/openjev ≠ TheoLeeCJ/openjev ≠ Zefan-Cai/Open-Jev; MstyAI/laya-onnx empty repo ≠ tozp/laya-onnx ≠ Mattepiu/laya-onnx ≠ gqgs/laya-onnx; SherifAshraf2003/jev-use ≠ shitianfang/jev-use; aniruddh-krovvidi/switchboard ≠ cannacre8ive/switchboard-ai; Visorian/TidyUp ≠ abhibansal60/tidy; isiomaC/jevkit ≠ WaynezProg/jev-kit; lee-lou2/jev-tree ≠ reachjalil/jev-tree; Royhu1/jev-poker-trainer empty repo; JoacoMarc/jev-harness-router ≠ jackbarunz/jev-tool-router; rh-guard owns primary gates; hf:Praveenrajus/jev-bench HTTP 200 was 401; hf:ZefanCai/Open-Jev densify dataset; LoRA ≠ RLCD replica; hf:emretheus/jev-rag-benchmark ≠ erendikmenn/jev-rag-benchmark; hf:ctaxnagomi/DGUI_HYPERMEM-JEV densify sha ab3d3529; hf:hugging-apps/open-jev-deberta-v3-large-demo encoder class member not Jev replica; serving substrate ≠ calibrated replica; catalog ≠ endorsement; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49; notes.md §127

**Hourly 1746 HIGH (`notes.md` §128).** TypeLLM truncated thinking densify. 0.8B thinking On 0/18 *theirs*. forced closure 20/20 type-valid *theirs*. Constrained AR ≠ calibrated Noul. Kev-0.8B completes family. 4B new-source 0.794/0.832 *theirs*. 9B new-source 0.812/0.837 *theirs*. transfer-v9 5%/9%/26% *theirs*. Facts go to code. Judgments go to Jev. Only facts can block. Jev never blocks. five-lines threshold 0.80 still soft. 155/155 argmax *theirs*. Qwen3.5 ≠ Archer. catalog ≠ endorsement. SHA move is not a replica. Do not reopen or amend PR #23–#50. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1746 uniqueness lock: TypeLLM/TypeLLM densify HEAD 702e6a287f3c README SHA 08180db0450b; truncated thinking then constrained decode; typellm_runtime.py typellm_sglang.py; evals/qwen35_small; 0.8B thinking On 0/18 *theirs*; forced closure 20/20 type-valid *theirs*; Constrained AR ≠ calibrated Noul; type safety does not guarantee factual accuracy; Qwen/Qwen3.8-27B ≠ Archer; jaredpalmer/kev densify live HEAD 8465c4c4c294 watch 38087aa0301d README SHA 19664b9ae546; Kev-0.8B completes family; Kev-0.8B 4B 9B Qwen3.5; 4B new-source 0.794/0.832 *theirs*; 9B new-source 0.812/0.837 *theirs*; transfer-v9 Kev-9B 5% Jev 9% Kev-8B 26% *theirs*; SemIf Kev-9B 0.917 Jev 0.965 *theirs*; scienthoon 0.952/0.911 vs 0.897/0.914 *theirs*; transformers >= 5.17; Qwen3.5 ≠ Archer; wire-compat ≠ logit-equiv; SHA move is not a replica; notque/vexjoy-agent 421★ /d routes /do fallback; tamaratran/jev-pruner densify HEAD 47d017c34eab; qkal/Canny Facts go to code. Judgments go to Jev. Only facts can block.; Jev never blocks; jqueryscript/awesome-jev 231 entries catalog ≠ endorsement; jqueryscript/awesome-jev ≠ MrJev/awesome-jev ≠ yibie/awesome-jev; jamescazzetta/five-lines threshold 0.80 still soft; eugeniughelbur/jev-engineering 371ms $0.0000189 300-call *theirs*; tpellet/jevify ≠ altryne/jevify; seb4ez/jevguard-mcp ≠ seb4ez/jevguard; resumocast/jev-mcp ≠ jkudish/jev-mcp; dtduc-git/jev-table first sighting; Adrian-Ernesto/jevsort ≠ zzzzzec/jevsort; MidasMulli/kev-ane 155/155 argmax *theirs*; MidasMulli/kev-ane ≠ jaredpalmer/kev; serving substrate ≠ calibrated replica; empty repo skip-thin; loktar00/llm-lan-party empty repo; rh-guard owns primary gates; catalog ≠ endorsement; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50; notes.md §128

465. **TypeLLM truncated thinking densify PRIMARY** (TypeLLM/TypeLLM):
     densify §113. HEAD 702e6a287f3c README SHA 08180db0450b. 18★.
     truncated thinking then constrained decode. typellm_runtime.py typellm_sglang.py.
     Constrained AR ≠ calibrated Noul. Full cards: `judgment-class.md`, `validation.md`.
466. **qwen35_small thinking On 0/18** (TypeLLM/TypeLLM):
     0.8B thinking On 0/18 *theirs*. forced closure 20/20 type-valid *theirs*.
     type-valid ≠ exact. type safety does not guarantee factual accuracy.
     Qwen/Qwen3.8-27B ≠ Archer. Full cards: `validation.md`.
467. **kev 0.8B family densify PRIMARY** (jaredpalmer/kev):
     densify §45. live HEAD 8465c4c4c294 watch 38087aa0301d README SHA 19664b9ae546.
     Kev-0.8B completes family. Kev-0.8B 4B 9B Qwen3.5.
     4B new-source 0.794/0.832 *theirs*. 9B new-source 0.812/0.837 *theirs*.
     transformers >= 5.17. Qwen3.5 ≠ Archer. Full cards: `judgment-class.md`.
468. **kev transfer / SemIf / scienthoon** (jaredpalmer/kev):
     transfer-v9 Kev-9B 5% Jev 9% Kev-8B 26% *theirs*.
     SemIf Kev-9B 0.917 Jev 0.965 *theirs*. scienthoon 0.952/0.911 vs 0.897/0.914 *theirs*.
     *theirs* not Harbor. Full cards: `validation.md`.
469. **vexjoy /d router** (notque/vexjoy-agent):
     421★ /d routes /do fallback. routing ≠ permission.
     Full cards: `mixed-architecture.md`.
470. **Canny facts-block** (qkal/Canny):
     Facts go to code. Judgments go to Jev. Only facts can block. Jev never blocks.
     Full cards: `faq.md`, `mixed-architecture.md`.
471. **jev-engineering latency** (eugeniughelbur/jev-engineering):
     371ms $0.0000189 300-call *theirs*. observe then honor.
     rh-guard owns primary gates. Full cards: `validation.md`.
472. **namesakes** (awesome-jev / jevify / jevguard-mcp / jev-mcp / jevsort):
     jqueryscript/awesome-jev ≠ MrJev/awesome-jev ≠ yibie/awesome-jev.
     tpellet/jevify ≠ altryne/jevify. seb4ez/jevguard-mcp ≠ seb4ez/jevguard.
     resumocast/jev-mcp ≠ jkudish/jev-mcp. Adrian-Ernesto/jevsort ≠ zzzzzec/jevsort.
     catalog ≠ endorsement. Full cards: `faq.md`.
473. **five-lines 0.80 still soft** (jamescazzetta/five-lines):
     five-lines threshold 0.80 still soft. AST first, remainder Jev.
     Full cards: `formal-methods.md`.
474. **kev-ane argmax** (MidasMulli/kev-ane):
     155/155 argmax *theirs*. serving substrate ≠ calibrated replica.
     MidasMulli/kev-ane ≠ jaredpalmer/kev. Full cards: `judgment-class.md`.
475. **jev-table first sighting / packs densify** (dtduc-git):
     dtduc-git/jev-table first sighting. densify jevassert / jev-packs.
     measurement owns endorsement. Full cards: `validation.md`.
476. **jev-pruner densify** (tamaratran/jev-pruner):
     densify §53. HEAD 47d017c34eab. 128★ star-noise vs first census.
     stdout prune vs session compaction. Full cards: `applied-mappings.md`.
477. **remainder first-sighting** (watermelon / Focus / jdhd / answerfit / others):
     first-sighting cards. catalog ≠ endorsement. Full cards: `faq.md`.
478. **empty skip-thin** (loktar00/llm-lan-party, Rwinkah/token-tracker, Oaklight/jev-explore-site):
     empty repo skip-thin. loktar00/llm-lan-party empty repo.
     Full cards: `faq.md`.
479. **skip-thin playgrounds** (0★ name-match, no README):
     SHA move is not a replica. skip-thin. Full cards: `faq.md`.
480. **skip Archer** (promised_not_landed):
     Qwen3.5 ≠ Archer. Hub archerhume/4rcherhume HTTP 401.
     Archer still promised_not_landed. Full cards: `faq.md`.

Hourly 1746 items 465–480 (`notes.md` §128). Do **not**
re-fold §127 items 449–464 / §126 items 433–448 / §125 items 417–432.
Skip Archer rewrite.
truncated thinking then constrained decode; Constrained AR ≠ calibrated Noul;
Facts go to code. Judgments go to Jev. Only facts can block; Jev never blocks;
Kev-0.8B completes family; 155/155 argmax *theirs*.
Hourly 1746 uniqueness lock: TypeLLM/TypeLLM densify HEAD 702e6a287f3c README SHA 08180db0450b; truncated thinking then constrained decode; typellm_runtime.py typellm_sglang.py; evals/qwen35_small; 0.8B thinking On 0/18 *theirs*; forced closure 20/20 type-valid *theirs*; Constrained AR ≠ calibrated Noul; type safety does not guarantee factual accuracy; Qwen/Qwen3.8-27B ≠ Archer; jaredpalmer/kev densify live HEAD 8465c4c4c294 watch 38087aa0301d README SHA 19664b9ae546; Kev-0.8B completes family; Kev-0.8B 4B 9B Qwen3.5; 4B new-source 0.794/0.832 *theirs*; 9B new-source 0.812/0.837 *theirs*; transfer-v9 Kev-9B 5% Jev 9% Kev-8B 26% *theirs*; SemIf Kev-9B 0.917 Jev 0.965 *theirs*; scienthoon 0.952/0.911 vs 0.897/0.914 *theirs*; transformers >= 5.17; Qwen3.5 ≠ Archer; wire-compat ≠ logit-equiv; SHA move is not a replica; notque/vexjoy-agent 421★ /d routes /do fallback; tamaratran/jev-pruner densify HEAD 47d017c34eab; qkal/Canny Facts go to code. Judgments go to Jev. Only facts can block.; Jev never blocks; jqueryscript/awesome-jev 231 entries catalog ≠ endorsement; jqueryscript/awesome-jev ≠ MrJev/awesome-jev ≠ yibie/awesome-jev; jamescazzetta/five-lines threshold 0.80 still soft; eugeniughelbur/jev-engineering 371ms $0.0000189 300-call *theirs*; tpellet/jevify ≠ altryne/jevify; seb4ez/jevguard-mcp ≠ seb4ez/jevguard; resumocast/jev-mcp ≠ jkudish/jev-mcp; dtduc-git/jev-table first sighting; Adrian-Ernesto/jevsort ≠ zzzzzec/jevsort; MidasMulli/kev-ane 155/155 argmax *theirs*; MidasMulli/kev-ane ≠ jaredpalmer/kev; serving substrate ≠ calibrated replica; empty repo skip-thin; loktar00/llm-lan-party empty repo; rh-guard owns primary gates; catalog ≠ endorsement; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50; notes.md §128

481. **kev own-data JSONL densify PRIMARY** (jaredpalmer/kev):
     densify §45. HEAD bd058057ad0a README SHA 84b872488915. 1033★.
     Fine-tuning on your own data. --data JSONL.
     --init_from warm-start LoRA/head PR #9.
     Kev-0.8B 4B 9B Qwen3.5 family. SHA move is not a replica.
     Full cards: `judgment-class.md`, `validation.md`.
482. **from-scratch ≠ warm-start / JSONL labels ≠ Harbor** (jaredpalmer/kev):
     4B new-source 0.794/0.832 *theirs*. 9B new-source 0.812/0.837 *theirs*.
     0.33 vs 0.84 vs 0.83/0.88 *theirs*. from-scratch ≠ warm-start.
     JSONL labels ≠ Harbor. Kev-0.5B card Qwen3.5 family pointer.
     Full cards: `faq.md`, `mixed-architecture.md`.
483. **dabit3 densify already catalogued** (dabit3/jev-experiments):
     dabit3/jev-experiments densify 340★. densify is not a sibling first sighting.
     Full cards: `applied-mappings.md`.
484. **tenbin densify neighbor skill** (simota/tenbin):
     simota/tenbin densify neighbor skill. Augustus does not absorb it.
     Full cards: `faq.md`.
485. **reconstruction ≠ replica** (kyegomez/open-jev):
     unofficial research implementation with random weights.
     reconstruction ≠ replica.
     kyegomez/open-jev ≠ razorback16/openjev ≠ TheoLeeCJ/openjev ≠ Zefan-Cai/Open-Jev ≠ Shalimov04/open-jev.
     Full cards: `judgment-class.md`, `faq.md`.
486. **assay-001 split verdict** (jourdanlabs/assay-001):
     assay-001 split verdict. CLINC150 ECE 0.0204 *theirs*.
     Banking77 ECE 0.0936 *theirs*. 8,576 responses zero type errors *theirs*.
     *theirs* not Harbor. Full cards: `validation.md`.
487. **jev-ra latency *theirs*** (brnyxx/jev-ra):
     brnyxx/jev-ra 3-5x / ~300 ms *theirs*. 8.50× Wikipedia *theirs*.
     systems comparison ≠ semantic equivalence.
     Full cards: `validation.md`.
488. **awesome-jev catalog namesake** (Promethe-us/awesome-jev):
     Promethe-us/awesome-jev ≠ MrJev/awesome-jev ≠ yibie/awesome-jev.
     catalog ≠ endorsement. Full cards: `faq.md`.
489. **jev-mcp namesake** (ThePFMind/jev-mcp):
     ThePFMind/jev-mcp ≠ jkudish/jev-mcp ≠ burnigtm/jev-mcp.
     serving substrate ≠ calibrated replica. Full cards: `faq.md`.
490. **minesweeper cousins** (comoc/jev-minesweeper, EnesYilmazcode/JevMinesweeper):
     comoc/jev-minesweeper ≠ EnesYilmazcode/JevMinesweeper.
     game success ≠ calibrated Noul. Full cards: `validation.md`.
491. **pi-jev-effort namesake** (namenu/pi-jev-effort):
     namenu/pi-jev-effort ≠ TheoOliveira/pi-jev.
     rh-guard owns primary gates. Full cards: `faq.md`.
492. **HF first-sighting / densify** (mini-Jev / allmix-r512 / laya-*):
     samatv256/mini-Jev ≠ r-ms/mini-jev.
     hf:akhilaaa3/openjev-v1-allmix-r512-merged ≠ hf:akhilaaa3/openjev-r512-handoff-demo.
     serving substrate ≠ calibrated replica.
     Full cards: `judgment-class.md`, `faq.md`.
493. **remainder apps** (fraud / notion / quilt / wrapper / DriftLab / jev-hft / others):
     Nutlope/jev-fraud Kimi K3. jeffloo886/jev-notion.
     classifier ≠ authorizer. catalog ≠ endorsement.
     Full cards: `applied-mappings.md`, `faq.md`.
494. **namesake remainder** (open-jev / awesome-jev / jev-mcp / mini-Jev / minesweeper):
     reconstruction ≠ replica. catalog ≠ endorsement.
     Full cards: `faq.md`.
495. **skip-thin catalogs** (jevguide / awesome-jev-prompt / hellojev):
     catalog ≠ endorsement. skip-thin. Full cards: `faq.md`.
496. **skip Archer** (promised_not_landed):
     Qwen3.5 ≠ Archer. Hub archerhume/4rcherhume HTTP 401.
     Archer still promised_not_landed. Full cards: `faq.md`.

Hourly 1843 items 481–496 (`notes.md` §129). Do **not**
re-fold §128 items 465–480 / §127 items 449–464 / §126 items 433–448.
Skip Archer rewrite.
from-scratch ≠ warm-start; JSONL labels ≠ Harbor;
reconstruction ≠ replica; assay-001 split verdict;
catalog ≠ endorsement; game success ≠ calibrated Noul;
SHA move is not a replica.
do not reopen or amend PR #23–#51.
Soft Noul ≠ hard safety.

**Hourly 1843 HIGH (`notes.md` §129).** kev own-data JSONL densify. --init_from warm-start LoRA/head PR #9. from-scratch ≠ warm-start. JSONL labels ≠ Harbor. 4B new-source 0.794/0.832 *theirs*. 9B new-source 0.812/0.837 *theirs*. 0.33 vs 0.84 vs 0.83/0.88 *theirs*. reconstruction ≠ replica. assay-001 split verdict. catalog ≠ endorsement. SHA move is not a replica. Do not reopen or amend PR #23–#51. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1843 uniqueness lock: jaredpalmer/kev densify HEAD bd058057ad0a README SHA 84b872488915; Fine-tuning on your own data; --data JSONL; --init_from warm-start LoRA/head PR #9; Kev-0.8B 4B 9B Qwen3.5 family; 4B new-source 0.794/0.832 *theirs*; 9B new-source 0.812/0.837 *theirs*; 0.33 vs 0.84 vs 0.83/0.88 *theirs*; from-scratch ≠ warm-start; JSONL labels ≠ Harbor; Kev-0.5B card Qwen3.5 family pointer; No Jev outputs were used for training; option order can change an answer; 8.2% ≥0.9 on wrong *theirs*; Kev-9B 7.5% ≥0.9 on wrong *theirs*; dabit3/jev-experiments densify 340★; simota/tenbin densify neighbor skill; Promethe-us/awesome-jev ≠ MrJev/awesome-jev ≠ yibie/awesome-jev; kyegomez/open-jev reconstruction ≠ replica; unofficial research implementation with random weights; kyegomez/open-jev ≠ razorback16/openjev ≠ TheoLeeCJ/openjev ≠ Zefan-Cai/Open-Jev ≠ Shalimov04/open-jev; jourdanlabs/assay-001 split verdict; CLINC150 ECE 0.0204 *theirs*; Banking77 ECE 0.0936 *theirs*; 8,576 responses zero type errors *theirs*; brnyxx/jev-ra 3-5x / ~300 ms *theirs*; 8.50× Wikipedia *theirs*; ThePFMind/jev-mcp ≠ jkudish/jev-mcp ≠ burnigtm/jev-mcp; namenu/pi-jev-effort ≠ TheoOliveira/pi-jev; samatv256/mini-Jev ≠ r-ms/mini-jev; comoc/jev-minesweeper ≠ EnesYilmazcode/JevMinesweeper; game success ≠ calibrated Noul; Nutlope/jev-fraud Kimi K3; jeffloo886/jev-notion; hf:akhilaaa3/openjev-v1-allmix-r512-merged ≠ hf:akhilaaa3/openjev-r512-handoff-demo; serving substrate ≠ calibrated replica; catalog ≠ endorsement; SHA move is not a replica; wire-compat ≠ logit-equiv; Qwen3.5 ≠ Archer; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51; notes.md §129


497. **sgoedecke/system-one first-sighting PRIMARY** (sgoedecke/system-one):
     position 1 (Operand). Batched single-token choice inference.
     SystemOne.from_pretrained. TypeSafe-compatible ≠ TypeSafe replica.
     cache_prefix=True. LICENSE absent. 20★ HEAD ebde2a2db706.
     Full cards: `judgment-class.md`, `mixed-architecture.md`.
498. **TypeSafe-compatible ≠ TypeSafe replica** (sgoedecke/system-one):
     positions 1 (Operand) × 11 (Bounds). Prefill `choice_index:` and
     constrain logits to index tokens. Open LM logit trick, not RLCD
     and not hosted jev-1.13. Full cards: `faq.md`, `validation.md`.
499. **system-one namesake lock** (sgoedecke / mithalouni / Kathan / babybear):
     sgoedecke/system-one ≠ mithalouni/system-one-open ≠ KathanModh259/system-one ≠ babybear-labs/system-one.
     Full cards: `faq.md`.
500. **mithalouni/system-one-open first-sighting** (mithalouni/system-one-open):
     position 1 (Operand). Gemma 4 E2B / Gemma 3 270M Modal. replica ≠ TypeSafe.
     18★ MIT HEAD 77f1f7cccf8a. HF upload pending. §78 table stays the board.
     Full cards: `judgment-class.md`, `validation.md`.
501. **76.7% vs Jev 86.9% *theirs*** (mithalouni/system-one-open):
     position 8 (Metric). 76.7% vs Jev 86.9% strict common subset *theirs*.
     97 ms H100 *theirs*. 74.8% held-out *theirs*. Soft scores ≠ hard gates.
     *theirs* not Harbor. Full cards: `validation.md`, `faq.md`.
502. **kotoba-lang/typed-decisions first-sighting** (kotoba-lang/typed-decisions):
     position 1 (Operand). ModernBERT / DeBERTa / LLaDA-MoE training record.
     DeBERTa-v3-large 0.855 / 42 ms *theirs*. ModernBERT-base 0.717 / 68 ms *theirs*.
     LLaDA-MoE 0.835 / 676 ms *theirs*. Hub encoder stays §33.
     encoder class member not Jev replica. Full cards: `judgment-class.md`.
503. **kotoba ≠ Laya HF namesake** (kotoba-lang/typed-decisions):
     kotoba-lang/typed-decisions ≠ convaiinnovations/laya-typed-decisions.
     Full cards: `faq.md`.
504. **aisearchio census catalog ≠ endorsement** (@aisearchio 15-link list):
     position 11 (Bounds). 12 already carded 3 gaps this fold.
     catalog ≠ endorsement. Skip Archer. SHA move is not a replica.
     Full cards: `faq.md`, `mental-models.md`.

User-provided 1936 items 497–504 (`notes.md` §130). Do **not**
re-fold §129 items 481–496 / §128 items 465–480 / §127 items 449–464.
Skip Archer rewrite.
TypeSafe-compatible ≠ TypeSafe replica; replica ≠ TypeSafe;
kotoba-lang/typed-decisions ≠ convaiinnovations/laya-typed-decisions;
aisearchio 15-link census catalog ≠ endorsement;
soft scores ≠ hard gates; SHA move is not a replica.
do not reopen or amend PR #23–#52.
Soft Noul ≠ hard safety.

**User-provided 1936 HIGH (`notes.md` §130).** sgoedecke/system-one first-sighting. SystemOne.from_pretrained. TypeSafe-compatible ≠ TypeSafe replica. mithalouni/system-one-open first-sighting. 76.7% vs Jev 86.9% *theirs*. replica ≠ TypeSafe. kotoba-lang/typed-decisions first-sighting. DeBERTa-v3-large 0.855 / 42 ms *theirs*. kotoba-lang/typed-decisions ≠ convaiinnovations/laya-typed-decisions. aisearchio 15-link census catalog ≠ endorsement. soft scores ≠ hard gates. SHA move is not a replica. Do not reopen or amend PR #23–#52. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
User-provided 1936 uniqueness lock: sgoedecke/system-one 20★ HEAD ebde2a2db706 README SHA d331b567e2c3; SystemOne.from_pretrained; Batched single-token choice inference; TypeSafe-compatible; cache_prefix=True; LICENSE absent; sgoedecke/system-one ≠ mithalouni/system-one-open ≠ KathanModh259/system-one ≠ babybear-labs/system-one; TypeSafe-compatible ≠ TypeSafe replica; mithalouni/system-one-open 18★ MIT HEAD 77f1f7cccf8a README SHA 535f33028a68 LICENSE SHA 2f6f2cf1064e; Gemma 4 E2B / Gemma 3 270M Modal; 76.7% vs Jev 86.9% strict common subset *theirs*; 97 ms H100 *theirs*; 74.8% held-out *theirs*; replica ≠ TypeSafe; HF upload pending; kotoba-lang/typed-decisions 1★ Apache-2.0 HEAD 10d7834d3b99 README SHA 4d6bbf4c4e44 LICENSE SHA 513bb5e3cb4c; ModernBERT / DeBERTa / LLaDA-MoE; DeBERTa-v3-large 0.855 / 42 ms *theirs*; ModernBERT-base 0.717 / 68 ms *theirs*; LLaDA-MoE 0.835 / 676 ms *theirs*; kotoba-lang/typed-decisions ≠ convaiinnovations/laya-typed-decisions; encoder class member not Jev replica; aisearchio 15-link census catalog ≠ endorsement; 12 already carded 3 gaps this fold; soft scores ≠ hard gates; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52; notes.md §130
**Open-Jev densify (`notes.md` §125).** DENSIFY the original 1441 card, not a sibling first sighting. HEAD 4933ee84951f README SHA ce1a587219e4. LoRA + scalar head + calibration temperature. not merged base models. customer-service P50 85.03 vs Jev 295.26 *theirs*. 1024/32 slower 1015.90 vs 301.37 *theirs*. systems latency ≠ semantic equivalence. Open-Jev TREC pending. hard acc ≠ calibrated Noul. type-valid ≠ exact. LoRA ≠ RLCD replica. Qwen/Qwen3.8-27B ≠ Archer. SHA move is not a replica. Do not reopen or amend PR #23–#52. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
User-provided Open-Jev densify uniqueness lock: Zefan-Cai/Open-Jev densify HEAD 4933ee84951f README SHA ce1a587219e4; pushed 2026-09-21T01:34Z; Astra TREC commit 1dd56990be7e pushed 2026-09-21T01:17Z; live 3★ (was 0★; star-noise is not the fold); LoRA adapters plus trained scalar decision head and calibration temperature; not merged base models; dataset ZefanCai/Open-Jev rev c67699e13d0a; Open-Jev-2B rev 0c7aa498b162; Open-Jev-9B rev 47e966881e48; 27B still in progress; Independent of TypeSafe; no RLCD/parity claims; LoRA ≠ RLCD replica; customer-service P50 local HTTP 85.03 ms vs Jev HTTPS 295.26 ms *theirs*; 1024 tokens/32 candidates Open-Jev slower 1015.90 vs 301.37 *theirs*; prefix caching experimental/off by default; CUDA prefix caching exceeded tolerance on 9/11 workloads; systems latency ≠ semantic equivalence; GPT Luna P50 918.13 ms Astra 1938.39 ms *theirs*; TREC-DL Jev/Luna/Astra completed; Open-Jev TREC pending; 80,816 training rows; 2B 94.71% / OOD 86.02%; 9B 97.54% / 91.97% *theirs* not Harbor; hard acc ≠ calibrated Noul; type-valid ≠ exact; Qwen/Qwen3.8-27B ≠ Archer; website https://zefan-cai.github.io/open-jev/; launch X thread https://x.com/Zefan_Cai/status/2101782158658695388 https://x.com/Zefan_Cai/status/2101786019607740436 https://x.com/Zefan_Cai/status/2101789698947793231; densify §125 not a sibling first sighting; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52; notes.md §125
505. **X-sentiment does not execute PRIMARY** (brainstormity/Jev-X-Sentiment-Analysis):
     HEAD 5c932f941a92 README SHA bf4134b44cda. 136★.
     platform does not execute trades. Buy/Sell/Hold/Take Profit.
     Full cards: `judgment-class.md`, `validation.md`.
506. **awesome catalogs namesake** (heyjunpenn/awesome-jev):
     heyjunpenn/awesome-jev 485 catalog ≠ endorsement.
     heyjunpenn/awesome-jev ≠ yibie/awesome-jev ≠ MrJev/awesome-jev ≠ Promethe-us/awesome-jev ≠ ckaraca/awesome-jev ≠ yzfly/awesome-jev-zh ≠ shirenchuang/awsomejev ≠ andyrewlee/awesome-system-one.
     Full cards: `faq.md`.
507. **jev-arena *theirs* not gold** (NanmiCoder/jev-arena):
     10k comments 62.69% vs 67.26% *theirs* not gold.
     203.2s $0.84 vs 823.5s $1.50 *theirs*. AI-reviewed labels ≠ gold.
     Full cards: `validation.md`.
508. **robot-control one-trial** (openroboto-ai/jev-robot-control):
     one seed-0 trial *theirs*. Jev $0.018825 vs Astra $5.93 *theirs*.
     one-trial robot ≠ Harbor. Full cards: `validation.md`.
509. **Qwen3.8 JevLike 10.59× uncalibrated** (endman100/research-Qwen3.8-JevLike):
     10.59× *theirs*. 6 class flips. agreement ≠ accuracy.
     probabilities uncalibrated. Qwen3.8 ≠ Archer. 10.59× systems ≠ ECE.
     Full cards: `validation.md`, `faq.md`.
510. **jev-acento Spanish** (marcosmartinez/jev-acento):
     Spanish −6.4 pp XNLI *theirs*. ECE 0.057→0.101 *theirs*.
     72.2% vs 63.4% p_max≥0.9 coverage *theirs*.
     Full cards: `validation.md`.
511. **llm-to-jev desc densify §118** (alexwestco/llm-to-jev):
     description rewrite Convert LLM prompts to Jev prompts.
     SHA unchanged 234058ab372d. 3★. heuristic conversion ≠ calibrated Noul.
     desc rewrite ≠ SHA/behavior change. Full cards: `question-design.md`.
512. **skip Open-Jev #53** (Zefan-Cai/Open-Jev):
     skip Zefan-Cai/Open-Jev densify open #53.
     Full cards: `faq.md`.
513. **skip #54 three** (sgoedecke / mithalouni / kotoba):
     skip sgoedecke/system-one mithalouni/system-one-open kotoba-lang/typed-decisions open #54.
     Full cards: `faq.md`.
514. **already-carded §49/§62/§61** (ikermoel / nrdz-labs / mallahyari):
     ikermoel/open-alternative-jev already §49.
     nrdz-labs/fast-jev-opencode already §62.
     mallahyari/system-one-benchmark already §61.
     Full cards: `faq.md`.
515. **skill-suggester / MCP does not execute** (win4r/jev-skill-suggester, PyModel/typesafe-mcp):
     does not execute. local_only ≠ Jev. host still reasons/edits/executes.
     Full cards: `mixed-architecture.md`.
516. **JevLoop rule-table ≠ model** (Xubqpanda/JevLoop):
     rule-table ≠ model. 12:1 / 7.7% *theirs* not Harbor.
     Full cards: `validation.md`.
517. **omawish/rizzo-flow local ≠ replica** (elberacasa/omawish, Rizzo-AI-Academy/rizzo-flow):
     replica ≠ TypeSafe. serving substrate ≠ calibrated replica.
     33M / 60/66 / 0/124 / 35ms *theirs*. ~250ms Q8 *theirs*.
     Full cards: `judgment-class.md`.
518. **remainder apps** (live-jev / SEO / hub / labs / traders / others):
     catalog ≠ endorsement. does not execute.
     Full cards: `applied-mappings.md`, `faq.md`.
519. **namesake remainder** (awesome-jev / jev-mcp / mini-jev / OpenJev / typesafe-go / system-one / jevvy / jev-lab / pi / jev-harness):
     catalog ≠ endorsement. SHA move is not a replica.
     Full cards: `faq.md`.
520. **skip Archer** (promised_not_landed):
     Qwen3.8 ≠ Archer. Hub archerhume/4rcherhume HTTP 401.
     Archer still promised_not_landed. Full cards: `faq.md`.

Hourly 1946 items 505–520 (`notes.md` §131). Do **not**
re-fold §129 items 481–496 / §128 items 465–480.
Leave 497–504 unused for open #54.
Skip Archer rewrite. Skip Open-Jev #53.
does not execute; catalog ≠ endorsement;
AI-reviewed labels ≠ gold; one-trial robot ≠ Harbor;
10.59× systems ≠ ECE; agreement ≠ accuracy;
desc rewrite ≠ SHA/behavior change;
SHA move is not a replica.
do not reopen or amend PR #23–#52.
Soft Noul ≠ hard safety.

**Hourly 1946 HIGH (`notes.md` §131).** X-sentiment does not execute trades. heyjunpenn/awesome-jev 485 catalog ≠ endorsement. jev-arena 62.69% vs 67.26% *theirs* not gold. 203.2s $0.84 vs 823.5s $1.50 *theirs*. one seed-0 trial *theirs*. Jev $0.018825 vs Astra $5.93 *theirs*. 10.59× *theirs*. 6 class flips. agreement ≠ accuracy. probabilities uncalibrated. Qwen3.8 ≠ Archer. Spanish −6.4 pp XNLI *theirs*. ECE 0.057→0.101 *theirs*. 72.2% vs 63.4% p_max≥0.9 coverage *theirs*. llm-to-jev description rewrite Convert LLM prompts to Jev prompts. SHA unchanged 234058ab372d. 3★. heuristic conversion ≠ calibrated Noul. skip Zefan-Cai/Open-Jev densify open #53. skip #54 three. catalog ≠ endorsement. *theirs* not Harbor. SHA move is not a replica. Do not reopen or amend PR #23–#52. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1946 uniqueness lock: brainstormity/Jev-X-Sentiment-Analysis 136★ HEAD 5c932f941a92 README SHA bf4134b44cda; platform does not execute trades; heyjunpenn/awesome-jev 485 catalog ≠ endorsement; heyjunpenn/awesome-jev ≠ yibie/awesome-jev ≠ MrJev/awesome-jev ≠ Promethe-us/awesome-jev ≠ ckaraca/awesome-jev ≠ yzfly/awesome-jev-zh ≠ shirenchuang/awsomejev ≠ andyrewlee/awesome-system-one; NanmiCoder/jev-arena 10k comments 62.69% vs 67.26% *theirs* not gold; 203.2s $0.84 vs 823.5s $1.50 *theirs*; AI-reviewed labels ≠ gold; openroboto-ai/jev-robot-control one seed-0 trial *theirs*; Jev $0.018825 vs Astra $5.93 *theirs*; one-trial robot ≠ Harbor; endman100/research-Qwen3.8-JevLike 10.59× *theirs*; 6 class flips; agreement ≠ accuracy; probabilities uncalibrated; Qwen3.8 ≠ Archer; 10.59× systems ≠ ECE; marcosmartinez/jev-acento Spanish −6.4 pp XNLI *theirs*; ECE 0.057→0.101 *theirs*; 72.2% vs 63.4% p_max≥0.9 coverage *theirs*; alexwestco/llm-to-jev description rewrite Convert LLM prompts to Jev prompts; SHA unchanged 234058ab372d; 3★; heuristic conversion ≠ calibrated Noul; desc rewrite ≠ SHA/behavior change; skip Zefan-Cai/Open-Jev densify open #53; skip sgoedecke/system-one mithalouni/system-one-open kotoba-lang/typed-decisions open #54; ikermoel/open-alternative-jev already §49; nrdz-labs/fast-jev-opencode already §62; mallahyari/system-one-benchmark already §61; does not execute; catalog ≠ endorsement; *theirs* not Harbor; SHA move is not a replica; local_only ≠ Jev; rule-table ≠ model; replica ≠ TypeSafe; arunav25/jev-mcp ≠ jkudish/jev-mcp ≠ ThePFMind/jev-mcp ≠ burnigtm/jev-mcp; luckberonne/mini-jev ≠ r-ms/mini-jev ≠ samatv256/mini-Jev; Kwwwww74/OpenJev ≠ razorback16/openjev ≠ kyegomez/open-jev ≠ Zefan-Cai/Open-Jev; peach-zhang/typesafe-go ≠ kisshan13/typesafe-ai-go ≠ Nibir1/typesafe-go; laidick/system-one-benchmark ≠ mallahyari/system-one-benchmark; sahasrarjn/system-one ≠ sgoedecke/system-one; aboisvert/jevvy ≠ PanAchy/jevvy; andrest04/jev-lab ≠ javsanesq/jevlab; twilwa/pi-typesafe ≠ TheoOliveira/pi-jev; RuipuCui/jev-harness ≠ ismaelsoilet/jev-harness ≠ AntonioCoppe/jev-harness; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52; notes.md §131

Hourly 2049 items 521–536 (`notes.md` §132). Do **not**
re-fold §131 items 505–520 / §130 items 497–504 / §129 items 481–496.
Skip Archer rewrite. Densify kev on §45. Densify kotoba on §130.
temperature scaling ≠ ECE unless measured;
Hub --revision is a pin not a replica;
trained runtime ≠ TypeSafe; grouped T rejected;
Qwen3.6 ≠ Archer; catalog ≠ endorsement;
*theirs* not Harbor; SHA move is not a replica.
do not reopen or amend PR #23–#55.
Soft Noul ≠ hard safety.

521. **kev night-2 densify PRIMARY** (jaredpalmer/kev):
     HEAD c096660c8da2 PLAN SHA 8d77dd271c66 README SHA unchanged 84b872488915.
     night-2 dates/unknowable/assertion. Full cards: `validation.md`.
522. **KEV_TEMPERATURE T≈2.0** (kev.serve calibrated row):
     KEV_TEMPERATURE T≈2.0. Brier 0.291→0.267 ECE 0.105→0.039 *theirs*.
     7.5%→3.2% *theirs*. grouped T rejected.
     temperature scaling ≠ ECE unless measured.
     Full cards: `validation.md`.
523. **Qwen3.6-35B-A3B smoke** (night-2 trial 1′):
     Qwen3.6-35B-A3B smoke 0.812 *theirs*. 21M LoRA experts frozen.
     Qwen3.6 ≠ Archer. Full cards: `faq.md`.
524. **Hub --revision night2-du** (promotion pin):
     Hub --revision night2-du. Hub --revision is a pin not a replica.
     0.852 OOD *theirs*. Full cards: `judgment-class.md`.
525. **MMLU-Pro 1000 *theirs*** (ekzhang sample):
     MMLU-Pro 1000 Kev-9B 0.511 Jev 0.829 *theirs*.
     *theirs* not Harbor. Full cards: `validation.md`.
526. **kotoba OpenJev runtime densify** (kotoba-lang/typed-decisions):
     HEAD ff7f84e74d04 README SHA unchanged 4d6bbf4c4e44.
     feat expose trained OpenJev decision runtime. open_jev.py.
     tests/test_open_jev.py. Full cards: `judgment-class.md`.
527. **trained runtime ≠ TypeSafe** (OpenJev.from_pretrained):
     OpenJev.from_pretrained. decide_request kind typed-decisions/open-jev-v1.
     generated_text: False. trained runtime ≠ TypeSafe.
     Full cards: `faq.md`.
528. **daftAI2026 catalog namesake** (daftAI2026/awesome-jev):
     daftAI2026/awesome-jev ≠ heyjunpenn/awesome-jev ≠ yibie/awesome-jev ≠ MrJev/awesome-jev ≠ Promethe-us/awesome-jev.
     catalog ≠ endorsement. Full cards: `faq.md`.
529. **swev CoreML on-device** (danielamitay/swev):
     danielamitay/swev CoreML. serving substrate ≠ calibrated replica.
     Full cards: `mixed-architecture.md`.
530. **jev-debtgate CI still soft** (smlayero/jev-debtgate):
     smlayero/jev-debtgate CI gate cutoff still soft.
     Full cards: `validation.md`.
531. **jqv stock Qwen3** (Octalab-Inc/jqv):
     Octalab-Inc/jqv stock Qwen3 decision API. Qwen3.5 ≠ Archer.
     Full cards: `judgment-class.md`.
532. **lev ≠ kev / laya-go ≠ Laya** (franckverrot/lev, neko233-com/laya-go):
     franckverrot/lev ≠ jaredpalmer/kev.
     neko233-com/laya-go ≠ convaiinnovations/laya.
     Full cards: `faq.md`.
533. **Locate ≠ decide / DuckDB / unofficial SDK** (gliner2-skill, duckdb-jev, tryAGI/TypeSafeAI):
     jaanavit/gliner2-skill Locate ≠ decide.
     prasanthj/duckdb-jev SQL predicates.
     tryAGI/TypeSafeAI ≠ official.
     Full cards: `applied-mappings.md`.
534. **legal LoRA ≠ RLCD** (hf:Nebulaw1):
     hf:Nebulaw1 legal LoRA ≠ RLCD replica. Qwen3.5 ≠ Archer.
     Full cards: `validation.md`.
535. **remainder apps / skip-thin** (games, skills, empty repos):
     skip-thin KadePrice123/jev-state-tracking hideri777/jev-application-sample.
     catalog ≠ endorsement. game success ≠ calibrated Noul.
     Full cards: `applied-mappings.md`, `faq.md`.
536. **skip Archer** (promised_not_landed):
     Qwen3.6 ≠ Archer. Qwen3.5 ≠ Archer.
     Hub archerhume/4rcherhume HTTP 401.
     Archer still promised_not_landed. Full cards: `faq.md`.

537. **Open-Jev provider quality densify PRIMARY** (Zefan-Cai/Open-Jev):
     HEAD a00559ea0ab2 README SHA unchanged ce1a587219e4.
     Publish prepared Open-Jev provider quality evaluation pipeline.
     Full cards: `validation.md`.
538. **provider pipeline ≠ completed quality / CPU ≠ GPU** (Open-Jev):
     808 requests 1841 labelled decisions per model.
     Open-Jev GPU inference has not started. 48 CPU tests pass.
     provider pipeline ≠ completed Open-Jev quality. CPU tests ≠ GPU scores.
     Full cards: `faq.md`.
539. **65/76 table *theirs*** (Open-Jev frozen 76-hard):
     65/76 72/76 66/76 60/76 71/76 *theirs*.
     117/140 109/140 135/140 *theirs*. Open-Jev TREC pending.
     Full cards: `validation.md`.
540. **cartpole Kev flip densify** (tinmanlab/cartpole-jev):
     HEAD 922cc61490a0 README SHA 0860958714f3.
     Active model Kev Not TypeSafe Jev. Full cards: `judgment-class.md`.
541. **fine-tuned Kev ≠ TypeSafe / one record of 64** (cartpole):
     81.25% 52/64 *theirs*. one record of 64.
     fine-tuned Kev ≠ TypeSafe Jev. softmax ≠ calibrated Noul.
     Full cards: `faq.md`.
542. **ashare rewrite densify** (xuboboo/ashare-trader):
     HEAD 26c7e95e6828 README SHA 7a860bdfa97b.
     premarket + intradaily. local probability model.
     Full cards: `applied-mappings.md`.
543. **QMT mock/dry no orders / AUC 0.532** (ashare):
     QMT sidecar mock/dry default no orders. AUC 0.532 *theirs*.
     36 组参数全部净期望为负. does not execute.
     Full cards: `validation.md`.
544. **kevin Playwright+Onyx first card** (gauravsaini/kevin):
     Playwright + Onyx. Laya/Kev friends *theirs*.
     3.69ms *theirs* not Harbor. Full cards: `mixed-architecture.md`.
545. **metask 80.1%** (metask-ai/metask-jev / hf:Raymond1122):
     metask-jev-4b 79.6% / 80.1% *theirs*.
     wayfind/metask-jev ≠ metask-ai/metask-jev.
     Full cards: `judgment-class.md`.
546. **lumen / typedecide / bonsai** (class members):
     lumen mixture-of-LoRA conformal.
     ardada2468/typedecide ≠ shkumbinhasani/typedecide.
     87 of 144 order-unstable *theirs*. bonsai 192/231 ECE 0.037 *theirs*. 8GB.
     Full cards: `faq.md`.
547. **vercel 95% Luna** (vercel-labs/jev-ai-sdk-form-router):
     vercel-labs 95% Luna fallback. cutoff 95% still soft.
     Full cards: `validation.md`.
548. **jev-qwen3.8 + train-your-first** (tinmanlab / cexll):
     tinmanlab/jev-qwen3.8-27b Qwen3.8 ≠ Archer.
     train-your-first-jev Qwen2.5-0.5B LoRA.
     Full cards: `judgment-class.md`.
549. **jevfish + snsk JP** (blobfishai / snsk):
     jevfish DecisionScore 78.24 *theirs*. Typed Decision Bench 5387.
     snsk JP 97.6 vs 36.9 *theirs*. Full cards: `validation.md`.
550. **catalogs namesakes** (yunhe-dev/awesomejev):
     yunhe-dev/awesomejev catalog ≠ endorsement.
     yunhe-dev/awesomejev ≠ heyjunpenn/awesome-jev ≠ daftAI2026/awesome-jev.
     sankaku-tech/jev-kit ≠ WaynezProg/jev-kit ≠ isiomaC/jevkit.
     Full cards: `faq.md`.
551. **remainder / skip-thin** (empty SHA, games, skills):
     skip-thin IOCArena laya-mirror empty SHA.
     reflex-gate CoT GBNF ≠ Noul. KaLM-Jev reranker ≠ Jev replica.
     mjyoke1111/jev-lab already §106. mizchi/jev-playground 19★.
     catalog ≠ endorsement. Full cards: `applied-mappings.md`, `faq.md`.
552. **skip Archer** (promised_not_landed):
     Qwen3.8 ≠ Archer. Hub archerhume/4rcherhume HTTP 401.
     Archer still promised_not_landed. Full cards: `faq.md`.


553. **Open-Jev TREC densify PRIMARY** (Zefan-Cai/Open-Jev):
     HEAD 48346d0630f1 README SHA unchanged ce1a587219e4.
     Publish strict Open-Jev TREC evaluation preparation and context proof.
     Full cards: `validation.md`.
554. **TREC prep ≠ completed / context proof ≠ nDCG** (Open-Jev):
     Actual Open-Jev TREC model inference is pending.
     All 79 combined CPU tests pass. 97 queries 43 DL19 54 DL20.
     TREC prep ≠ completed Open-Jev TREC. context proof ≠ nDCG.
     CPU tests ≠ GPU scores. Full cards: `faq.md`.
555. **TypeLLM PyPI densify** (TypeLLM/TypeLLM):
     HEAD 8a8b4aefd443 README SHA 9f6dea3a4c8c.
     Add PyPI packaging and publish workflow. typellm 0.1.1.
     Full cards: `judgment-class.md`.
556. **PyPI packaging ≠ calibrated Noul** (TypeLLM):
     Constrained AR ≠ calibrated Noul. PyPI packaging ≠ calibrated Noul.
     type safety does not guarantee factual accuracy.
     Full cards: `faq.md`.
557. **simple-jev first card PRIMARY novel** (featherless-ai/simple-jev):
     408★ HEAD b02aa81c915a README SHA 4c5be59e9738.
     /v1/systemone alias of /v1/classifier. does not reproduce TypeSafe.
     Full cards: `judgment-class.md`.
558. **logits are not calibrated probabilities** (simple-jev):
     logits are not calibrated probabilities of correctness.
     wire-compat ≠ logit-equiv. Full cards: `faq.md`.
559. **jev-directory catalog** (everyai-com/jev-directory):
     13★ 50 runnable evals 1300+ builds catalog ≠ endorsement.
     Full cards: `applied-mappings.md`.
560. **Jev-Mem LoCoMo *theirs*** (libingzheren/Jev-Mem):
     Jev-Mem 11.0% 6.6× 36.7% *theirs* not Harbor.
     Full cards: `validation.md`.
561. **pi-jev-context namesake** (Nyarlathoteppppp/pi-jev-context):
     Nyarlathoteppppp/pi-jev-context ≠ kevinpita/pi-jev-context.
     Full cards: `mixed-architecture.md`.
562. **necro abandoned LoRA** (FogMoe/necro):
     FogMoe/necro abandoned LoRA retrospective.
     LoRA ≠ RLCD replica. Qwen3.5-0.8B ≠ Archer.
     Full cards: `judgment-class.md`.
563. **hearim / jev-rs serving** (ziozzang/hearim, yijunyu/jev-rs):
     hearim Jev-compatible Go gateway.
     yijunyu/jev-rs any LLM one prefill.
     Full cards: `mixed-architecture.md`.
564. **HF serving packs** (wayfind / FluidInference / Weidows / smdesai):
     wayfind/metask-jev-4b-policy-mix ≠ metask-ai/metask-jev.
     FluidInference/laya-coreml ≠ AndyInQtr/laya-coreai ≠ mizorewww/laya-coreml.
     serving substrate ≠ calibrated replica.
     Full cards: `judgment-class.md`.
565. **namesakes** (alongL / huaizuo2022 / majiayu000 / jev-mcp):
     alongL/openJev ≠ Zefan-Cai/Open-Jev.
     huaizuo2022/jev-ultrafast ≠ browser-use/jev-ultrafast.
     majiayu000/awesome-jev ≠ heyjunpenn/awesome-jev ≠ yibie/awesome-jev.
     rajasekharponakala/jev-mcp ≠ thedv91/jev-mcp ≠ jkudish/jev-mcp.
     Full cards: `faq.md`.
566. **remainder / fail-closed / games**:
     clarity-judge independent community project.
     game success ≠ calibrated Noul. catalog ≠ endorsement.
     Full cards: `applied-mappings.md`, `faq.md`.
567. **skip-thin** (empty SHA / 404):
     skip-thin jev-droid 404 mach empty SHA.
     SHA move is not a replica. Full cards: `faq.md`.
568. **skip Archer** (promised_not_landed):
     Qwen3.5-0.8B ≠ Archer. Hub archerhume/4rcherhume HTTP 401.
     Archer still promised_not_landed. Full cards: `faq.md`.


569. **openjev MLX densify PRIMARY** (razorback16/openjev):
     HEAD 2050fdb8280d README SHA d5322e16e565.
     MLX backend steps>1/think/text gen + image Qs.
     Full cards: `judgment-class.md`.
570. **dual serving is not generate** (openjev MLX):
     dual serving is not generate. Hosted Codiv ≠ TypeSafe.
     wire-compat ≠ logit-equiv. SHA move is not a replica.
     Full cards: `faq.md`.
571. **TypeLLM Release v0.1.1 densify** (TypeLLM/TypeLLM):
     HEAD 8a8b4aefd443 README SHA unchanged 9f6dea3a4c8c.
     GitHub Release v0.1.1. Drop fixed banner height so it scales on PyPI.
     Full cards: `judgment-class.md`.
572. **Constrained AR ≠ calibrated Noul** (TypeLLM):
     Constrained AR ≠ calibrated Noul. PyPI packaging ≠ calibrated Noul.
     type safety does not guarantee factual accuracy.
     Full cards: `faq.md`.
573. **JevLoop independent** (zjunlp/JevLoop):
     6★ HEAD 56cbf2bd6b5d independent not affiliated.
     Full cards: `mixed-architecture.md`.
574. **open-bonsai-jev namesake** (NicolaiLassen/open-bonsai-jev):
     NicolaiLassen/open-bonsai-jev ≠ NicolaiMTLassen/open-bonzi-jev.
     WANLI-256 74.6% *theirs*.
     Full cards: `faq.md`.
575. **jevtok 0 mismatches *theirs*** (LabGuy94/jevtok):
     LabGuy94/jevtok 0 mismatches *theirs* not Harbor.
     Full cards: `validation.md`.
576. **ockev TomatoEggBench *theirs*** (fancyboi999/ockev):
     ockev 35ms 95.8% TomatoEggBench *theirs* not Harbor.
     Full cards: `validation.md`.
577. **n=8 is not Harbor** (zhengbangbo/structured-decision-bench):
     structured-decision-bench n=8 *theirs*. n=8 is not Harbor.
     Full cards: `validation.md`.
578. **option order can change an answer** (novaleolin/jev-evolve):
     option order 0.188 or 0.542 *theirs*. novaleolin/jev-evolve.
     option order can change an answer.
     Full cards: `question-design.md`.
579. **namesakes** (danielhirt / Yang-SS-stack / amoreX / smile-magic):
     danielhirt/jev-lab ≠ tanayvasishtha/jev-lab ≠ dairui1/jev-lab ≠ mjyoke1111/jev-lab.
     Yang-SS-stack/jev-computer-use ≠ Mrchen116/jev-computer-use.
     amoreX/jevvy ≠ PanAchy/jevvy ≠ aboisvert/jevvy.
     smile-magic/laya-mlx-ddz ≠ smile-magic/laya-mlx-wzq.
     Full cards: `faq.md`.
580. **serving substrates** (laya-api / KaLM-Jev / soyelmismo):
     sriramkasyap/laya-api wire-compat ≠ logit-equiv.
     hf:space:Yuki131/KaLM-Jev ≠ KaLM-Embedding/KaLM-Jev.
     KaLM-Jev reranker ≠ Jev replica.
     hf:soyelmismo/laya-multilingual-onnx serving substrate ≠ calibrated replica.
     Full cards: `judgment-class.md`.
581. **does not execute / advisory / ranking** (llm-routing-jiv / page-checker / LCM):
     ranking before lossless condensation.
     llm-routing-jiv does not execute.
     jev-page-checker advisory does not block.
     1deat0r/Jcua Cua-S1 ≠ TypeSafe.
     Jev-Register-Tool catalog only.
     Full cards: `mixed-architecture.md`.
582. **already carded**:
     nexibeo/jev-cookbook already carded.
     leesk212/JEV-CPU already carded.
     kazuhideoki/jev-search already carded.
     Full cards: `applied-mappings.md`.
583. **skip-thin / remainder**:
     skip-thin layacm empty SHA.
     game success ≠ calibrated Noul. catalog ≠ endorsement.
     Full cards: `faq.md`.
584. **skip Archer** (promised_not_landed):
     Hub archerhume/4rcherhume HTTP 401.
     Archer still promised_not_landed. Full cards: `faq.md`.


585. **Open-Jev JevBench public-subset densify PRIMARY** (Zefan-Cai/Open-Jev):
     HEAD f46ff604f794 via afb5226982c7 README SHA e32c4bbd519c.
     Publish audited JevBench public-subset baselines.
     Full cards: `judgment-class.md`.
586. **public-subset ≠ Harbor / 231 ≠ 534** (Open-Jev):
     231 public tasks 72 original 48 easy 111 hard. do not report full-534.
     public-subset ≠ Harbor. 231 ≠ 534. Open-Jev TREC pending.
     Full cards: `validation.md`.
587. **kev 35B MMLU-Pro densify** (jaredpalmer/kev):
     HEAD e0bcf50153f1 README SHA unchanged 84b872488915.
     PLAN correct 35B MMLU-Pro (0.550). Not shipped.
     Full cards: `judgment-class.md`.
588. **evaluate.load honour weights_dtype=bf16** (kev):
     evaluate.load honour weights_dtype=bf16. Qwen3.6 ≠ Archer.
     Hub --revision is a pin not a replica.
     Full cards: `validation.md`.
589. **jev-browser-use 5-10× *theirs*** (wy-coliney/jev-browser-use):
     282★ 5-10× *theirs* not Harbor. Jev clicks Codex thinks and verifies.
     wy-coliney/jev-browser-use ≠ browser-use/jev-ultrafast ≠ Mrlyk/jev-browser ≠ akras14/jevbro.
     Full cards: `mixed-architecture.md`.
590. **fail-open routing ≠ permission** (gargpratyush/jev-router):
     270★ first card fail-open routing ≠ permission.
     33Audits/jev-auto ≠ gargpratyush/jev-router.
     Full cards: `faq.md`.
591. **ordered routing ≠ end-to-end** (BillionsBobby/JevRouter):
     124★ 38% 44% vs 24% *theirs* not Harbor. ordered routing ≠ end-to-end.
     BillionsBobby/JevRouter ≠ gargpratyush/jev-router.
     Full cards: `validation.md`.
592. **softmax next-token ≠ calibrated Noul** (daseinlabs/open-jev):
     75★ Gemma 3 4B MLX. head 0.970 ECE 0.027 *theirs*. shuffled-context 0.258.
     daseinlabs/open-jev ≠ Zefan-Cai/Open-Jev ≠ razorback16/openjev ≠ zhlei07/openjev.
     Full cards: `judgment-class.md`.
593. **potential_match ≠ hiring decision** (skeptrunedev/jev-recruiter):
     potential_match ≠ hiring decision.
     Full cards: `faq.md`.
594. **threshold on held-out** (abhixhek/jevcal):
     threshold on held-out. simulator not a Jev bench. fail-closed without fallback.
     Full cards: `validation.md`.
595. **already carded** (AntonioCoppe/jev-harness):
     AntonioCoppe/jev-harness already carded.
     Full cards: `applied-mappings.md`.
596. **system-one-gemma 64.4% ECE 0.047 *theirs*** (akash-kamat/system-one-gemma):
     64.4% ECE 0.047 *theirs*. 200x *theirs* not Harbor.
     Full cards: `validation.md`.
597. **catalogs / namesakes** (AgentBuff / Alpha-Harper-Franklin):
     AgentBuff/awesome-jev catalog ≠ endorsement.
     AgentBuff/awesome-jev ≠ yibie/awesome-jev ≠ heyjunpenn/awesome-jev.
     Alpha-Harper-Franklin/jev-drive ≠ VennIntelligence/jev-drive.
     Premo-Cloud/typesafe-sdk-java unofficial.
     Full cards: `faq.md`.
598. **skip-thin** (empty SHA):
     skip-thin zhlei07/openjev empty SHA khmuhtadin/n8n-nodes-jev-classification empty SHA.
     SHA move is not a replica. Full cards: `faq.md`.
599. **remainder / games / design-stage**:
     game success ≠ calibrated Noul. does not execute. routing ≠ permission.
     catalog ≠ endorsement. Full cards: `faq.md`.
600. **skip Archer** (promised_not_landed):
     Hub archerhume/4rcherhume HTTP 401.
     Archer still promised_not_landed. Full cards: `faq.md`.

601. **Open-Jev v3 densify PRIMARY** (Zefan-Cai/Open-Jev):
     HEAD ed45657bf726 via 748ae3024294 README SHA 12e0f581e15d.
     Publish audited v3 community data and held-out evaluation protocol.
     Full cards: `judgment-class.md`.
602. **v3 data prepared ≠ retrained released models** (Open-Jev):
     129,288 decision rows 74,921 training. frozen mixture 96,849 training.
     v3 data prepared ≠ retrained released models. Full cards: `validation.md`.
603. **held-out protocol ≠ Harbor / 1,280-row panel ≠ Harbor** (Open-Jev):
     1,280-row / 840-group comparison panel. held-out protocol ≠ Harbor.
     1,280-row panel ≠ Harbor. Open-Jev TREC pending. Full cards: `validation.md`.
604. **finite training loss ≠ quality / website redesign ≠ calibration** (Open-Jev):
     finite training loss ≠ quality improvement. website redesign ≠ calibration.
     27B step 616 pending. Full cards: `validation.md`.
605. **jev-wide naive throws away 83% *theirs*** (123Satyajeet123/jev-wide):
     255 documented ~32,768 tokens real. two-decimal 95.8% floored *theirs*.
     IIA fails +0.31 ... +0.50 *theirs*. Full cards: `validation.md`.
606. **certo KL 0.008 acc 0.844 ECE 0.004 *theirs*** (AltSlate-Labs/certo):
     research preview independent not affiliated. Full cards: `judgment-class.md`.
607. **first-instinct 63.3%→78.1% *theirs* not Harbor** (catoenm/first-instinct):
     371,278 prepared ≠ consumed. RL did not reliably improve held-out.
     independent educational not a recovered Jev recipe. Full cards: `validation.md`.
608. **Jev is a gate not a generator** (endomorphosis/JevOps):
     Lake remains admission. Jev never writes Lean. Full cards: `faq.md`.
609. **dohnuts joint RLCD *theirs*** (PsiACE/dohnuts):
     4★ small multimodal direct decisions. Dohnuts ≠ TypeSafe.
     Full cards: `judgment-class.md`.
610. **community port ≠ TypeSafe** (chy4pro/jev-for-chrome):
     12★. chy4pro/jev-for-chrome ≠ browser-use/jev-ultrafast.
     Full cards: `faq.md`.
611. **question-forge / decision-solver** (gbesse):
     held-out before winner. demo accuracy is synthetic not a Jev benchmark.
     bounded exact enumerator Jev prefs ≠ joint P. Full cards: `validation.md`.
612. **router namesakes** (Akashdb5 / daviddl9):
     Akashdb5/jev-router ≠ gargpratyush/jev-router ≠ daviddl9/jev-router.
     Full cards: `faq.md`.
613. **already carded** (buluoray/JevOnly; yottayoshida/jev-intent-review):
     buluoray/JevOnly already carded. yottayoshida/jev-intent-review already carded.
     Full cards: `applied-mappings.md`.
614. **skip-thin** (empty SHA):
     skip-thin Iskandeur/system1-system2 zhlei07/open-system-one Hand-In/openjev-multimodal gwxcsny53/jev-watchtower empty SHA.
     SHA move is not a replica. Full cards: `faq.md`.
615. **remainder / catalogs / serving**:
     flyryan/ai-news-aggregator 26★ does not execute. serving substrate ≠ calibrated replica.
     game success ≠ calibrated Noul. catalog ≠ endorsement. routing ≠ permission.
     kiuckhuang/laya-jev ≠ KonghaYao/laya-jev.
     tegersdorfer-collab/jevkit ≠ isiomaC/jevkit ≠ WaynezProg/jev-kit.
     Full cards: `faq.md`.
616. **skip Archer** (promised_not_landed):
     Hub archerhume/4rcherhume HTTP 401.
     Archer still promised_not_landed. Full cards: `faq.md`.

617. **GLiClass instruct-large PRIMARY class-peer** (knowledgator Hub):
     43 likes sha 825e5478c1bf apache-2.0.
     GLiClass knowledgator Hub family class-peer catalog not Jev equivalent.
     Full cards: `judgment-class.md`.
618. **GLiClass Hub family** (instruct-base/edge, multilang mini/ultra/edge, v1–v3, SandBox):
     Knowledgator/GLiClass.c already §123. Hub models first card as class-peer entries.
     GLiNER/GLiClass ports are class members not Jev replicas. Full cards: `judgment-class.md`.
619. **typed-decision-leaderboard *theirs* not Harbor** (mayafree):
     JEV 0.7350 ZTC 27B 0.7289 ZTC 397B 0.7272 *theirs* not Harbor.
     2,018 items same labels. three-way tie. Full cards: `validation.md`.
620. **Jevbridge ACP/MCP adapter** (tacticocc/Jevbridge):
     33★ MIT HEAD da443ea453ac README SHA 2178333c4c3b.
     does not generate text. Any LLM as System One. wire-compat ≠ logit-equiv.
     Full cards: `faq.md`.
621. **Cut the slop** (tshmieldev/sharp):
     29★ MIT HEAD 17cbd8d9cc9e README SHA 783a5cde519c.
     Filter your X timeline. Full cards: `applied-mappings.md`.
622. **typesafe-playground / aside-jev** (kavehmz / himomohi):
     real API calls not polished benchmarks. Not a Cua binding.
     Jev is the model Aside is the browser runtime. Full cards: `faq.md`.
623. **nico-martin/open-jev namesake** (browser Transformers.js):
     open reproductions of the shape. Nothing is generated.
     nico-martin/open-jev ≠ razorback16/openjev ≠ Zefan-Cai/Open-Jev ≠ meijustory123/openjev.
     Full cards: `faq.md`.
624. **serving substrate GGUF/MLX/LiteRT/nanodiff**:
     82.3% ECE 0.017 *theirs*. Same decision as bf16 94.4% *theirs*.
     ECE 0.065 → 0.036 *theirs*. 144/144 *theirs*. Qwen3.5-2B ≠ Archer.
     serving substrate ≠ calibrated replica. Full cards: `validation.md`.
625. **journey-evals / dev-0.4b / typed-decisions-synth**:
     A page that says Success is never accepted as proof.
     Banking77 91.33% BoolQ 85.20% *theirs*. encoder class member not Jev replica.
     7,414 cases 25,859 questions. Nobody checked it. Full cards: `validation.md`.
626. **already carded** (Zaious / LocalLLaMA / jevfeed):
     Zaious/jev-capability-atlas already carded.
     LocalLLaMA/typed-decisions already carded.
     fengyiqicoder/jevfeed already carded. Full cards: `applied-mappings.md`.
627. **namesakes** (awesome-jev / reflex / jev-mcp / hunch / switchboard / openjev):
     Zhao-Tian-yi/awesome-jev ≠ Gerry9000/awesome-jev ≠ heyjunpenn/awesome-jev ≠ yibie/awesome-jev.
     kaustav1996/reflex ≠ vuckuola619/reflex. tphakala/jev-mcp ≠ jkudish/jev-mcp.
     ninthspace/hunch ≠ carldaws/hunch ≠ tpellet/hunch.
     ruban-24/switchboard ≠ cannacre8ive/switchboard-ai.
     hf:openjev/openjev ≠ razorback16/openjev. Full cards: `faq.md`.
628. **skip-thin** (empty SHA):
     skip-thin Fibonaccirabbit/Jev-VLN imanshu03/jev-browser-use luca-saggese/laya.c empty SHA.
     SHA move is not a replica. Full cards: `faq.md`.
629. **remainder / catalogs / games**:
     catalog ≠ endorsement. game success ≠ calibrated Noul. does not execute.
     routing ≠ permission. Full cards: `faq.md`.
630. **GLiClass ONNX ports class members**:
     Daecore / Ihor / RooTender / SkyFVII / hesenc86 / winado ONNX class members not Jev replicas.
     Full cards: `judgment-class.md`.
631. ***theirs* not Harbor / routing ≠ permission**:
     0.7350 / 82.3% / 91.33% / 144/144 stay *theirs*. soft scores ≠ hard gates.
     Full cards: `validation.md`.
632. **skip Archer** (promised_not_landed):
     Hub archerhume/4rcherhume HTTP 401.
     Archer still promised_not_landed. Full cards: `faq.md`.

633. **open-cricket PRIMARY BYOM** (JonathanHHenson/open-cricket):
     MIT HEAD d75af22125ed README SHA 7d288a741089.
     Local structured decisions using causal language models.
     default Qwen/Qwen2.5-1.5B-Instruct. independent of TypeSafe.
     wire-compat ≠ logit-equiv. Qwen2.5 ≠ Archer. replica ≠ TypeSafe.
     Full cards: `judgment-class.md`.
634. **jev-decision-arena Greedy vs Oracle** (virtualman333):
     MIT HEAD cf6ae4ed31e8 README SHA 037f75d9610d.
     Greedy 0.90 vs Oracle 0.82 *theirs*. Random conf 0.00 still 20.5% *theirs*.
     ECE 0.180 / 0.106 / 0.205 *theirs*. confidence ≠ P(correct).
     seed 42 n=1 is not Harbor. Full cards: `validation.md`.
635. **typesafe-ai-test 8,400 calls** (dopeCape):
     HEAD ed2adb7740d7 README SHA 183f91c36471.
     8,400 calls $0.39 *theirs*. Noul 0.7 true 44% *theirs*.
     ≥0.9 conf 91.7% AG News *theirs*. versioned model ids rejected.
     *theirs* not Harbor. Full cards: `validation.md`.
636. **werr JevBench 81.65 *theirs* not Harbor** (pCwOrM/werr):
     2★ MIT HEAD 2526cae98891 README SHA b29476734a09.
     WindTunnel 49/49 *theirs* not Harbor.
     0-byte Mandelbrot is not a replica. Full cards: `faq.md`.
637. **OpenJev-Kit training not complete** (meijustory123):
     HEAD c53125982f80 README SHA a4e72c61a973.
     no accuracy. Qwen3.5-0.8B ≠ Archer.
     meijustory123/OpenJev-Kit IS meijustory123/openjev (same GitHub id 1379187719); meijustory123/OpenJev-Kit ≠ Zefan-Cai/Open-Jev.
     Full cards: `faq.md`.
638. **jev-hooks / jury.nvim / evoke**:
     Compose meaning like state. Code enumerates the candidates.
     Jev is the first classifier the design is bound to none.
     Full cards: `applied-mappings.md`.
639. **densify jev-voice-browser §82** (moritzkremb):
     HEAD 198a0764395a README SHA 816309fc22e6 was fa033303.
     context is the conversation so far.
     densify §82 not a sibling first sighting. Full cards: `applied-mappings.md`.
640. **densify is-malicious** (luantak):
     18★ MIT HEAD faf6ba61d7e1 README SHA 4ae098b4b7ae.
     A clean report is not proof. does not sandbox.
     Full cards: `faq.md`.
641. **ChatJEVs / laya-mac-serve / localjev-mlx**:
     ChatJEVs ≠ erik-dunteman/ChatJev.
     generation from Choice is not a language model replica.
     serving substrate ≠ calibrated replica.
     rimusz/localjev-mlx ≠ githubnext/localjev. Full cards: `faq.md`.
642. **jev-agent-router / decision-workbench**:
     does not execute. cutoff 0.8 still soft.
     demo scores are not accuracy measurements. Full cards: `faq.md`.
643. **namesakes** (jev-search / jev-mobile / jev-skill / ask-jev / openjev Hub):
     kylemclaren/jev-search ≠ kazuhideoki/jev-search.
     xinwang-nwpu/jev-mobile ≠ Friedjof/jev-mobile.
     kcd-dev/jev-skill ≠ raphael-liu/jev-skill.
     yanmad27/ask-jev ≠ kuhung/ask-jev.
     hf:akhilaaa3/openjev-v1-40705-nimble-r512-merged ≠ hf:akhilaaa3/openjev-v1-allmix-r512-merged.
     Full cards: `faq.md`.
644. **already carded** (zhuyansen/x-reply-filter):
     zhuyansen/x-reply-filter already carded. Full cards: `applied-mappings.md`.
645. **skip-thin** (empty SHA):
     skip-thin Fibonaccirabbit/Jev-GalGame MadhavBahl/jev-guide advance-lion/dsh-jev-hooks amithgc/local-jev hiro1202/jev-review-gate-poc inlight37-design/decision-model_lab kuhung/ask-jev mmiguez314/jev-lab pomodorozhong/exp-jev vanthiet1/JevGuarAgent empty SHA.
     SHA move is not a replica. Full cards: `faq.md`.
646. **remainder / catalogs / HF / spam**:
     hf:s1lv3rj1nx/openjev-router-healthcare encoder class member not Jev replica.
     jevai spaces catalog ≠ endorsement.
     catalog ≠ endorsement. game success ≠ calibrated Noul. does not execute.
     routing ≠ permission. Full cards: `faq.md`.
647. ***theirs* not Harbor / confidence ≠ P(correct)**:
     Greedy 0.90 / 8,400 calls $0.39 / JevBench 81.65 / WindTunnel 49/49 stay *theirs*.
     seed 42 n=1 is not Harbor. soft scores ≠ hard gates.
     Full cards: `validation.md`.
648. **skip Archer** (promised_not_landed):
     Hub archerhume/4rcherhume HTTP 401.
     Archer still promised_not_landed. Full cards: `faq.md`.









649. **lcc PRIMARY keep-all** (lucasmartins-ai/lcc):
     7★ MIT HEAD a7e86fb60997 README SHA 877831764be9.
     keeps essentially every block 0.0%/−0.5% *theirs*.
     mechanical −70.0% Jev −52.1% *theirs*.
     mock Laya = Jev −22.6% on XL withdrawn.
     Token reduction alone is not cost reduction. N=18 pilot not Harbor.
     Full cards: `judgment-class.md`.
650. **Jev-Compatible softmax gateway** (David-Lolly):
     3★ HEAD e52e963d8539 README SHA 6e5ff22d40a6.
     Chat 1282.3 ms vs gateway 232.1 ms ~1/5.5 *theirs*. 3/3 n=3.
     Softmax over candidate logprobs. Qwen3.8-27B ≠ Archer.
     wire-compat ≠ logit-equiv. Full cards: `validation.md`.
651. **any2jev converter ECE 0.027** (hwfengcs):
     2★ Apache-2.0 HEAD 719b0eb9eefe README SHA 27e0af212cd5.
     independent not affiliated. acc 0.796 ECE 0.027 *theirs*.
     42 ms vs JSON 778 ms *theirs*. Snake acc 0.953 ECE 0.034 *theirs*.
     Qwen3-0.6B ≠ Archer. Full cards: `validation.md`.
652. **NanoJev densify §115 JevHarness** (TianyuCodings):
     HEAD 76fdfc9ecdca README SHA a8f8afeb7e44 was 618cea6d / 4190093c64ee.
     Add JevHarness project link to READMEs.
     densify §115 not a sibling first sighting.
     SHA move is not a replica. Full cards: `applied-mappings.md`.
653. **synthetic survey How you ask** (jjd-lab):
     MIT HEAD 9ca8c4ab94bb README SHA ec1664288d50.
     How you ask mattered more. Noul TVD 0.1530 vs GPT 0.1789 *theirs*.
     ECE 0.1472 *theirs* not Harbor. missed 0.05 bar.
     Full cards: `validation.md`.
654. **jev-arcade Calibration is not yet measured** (CankatSarac):
     MIT HEAD b2e45ed3c1c6 README SHA 1f06af0f4c74.
     snake 70/80 *theirs*. tetris 167 vs heuristic 2333 *theirs*.
     74% conf <0.5 *theirs*. three seeds not Harbor.
     game success ≠ calibrated Noul. Full cards: `validation.md`.
655. **rlcd Yang 2023 ≠ TypeSafe RLCD** (sszxt):
     HEAD 66ca01664d6b README SHA 3da08d46758d.
     ECE 0.490→0.423 Brier 0.487→0.409 *theirs*.
     still overconfident. Qwen2.5 ≠ Archer. Full cards: `faq.md`.
656. **AXERA Laya / openjev-MLX-4bit serving**:
     hf:AXERA-TECH/Laya sha 51a586cd14e2. AX650 NPU 69.991/27.722/69.990 ms *theirs*.
     hf:openjev/openjev-MLX-4bit sha c59bf1eed7d8. ~15 GB 4-bit affine.
     serving substrate ≠ calibrated replica.
     hf:openjev/openjev-MLX-4bit ≠ razorback16/openjev. Full cards: `faq.md`.
657. **Hub Laya namesakes / laya-needle / laya2typesafeapi**:
     GeekyAbs/laya ≠ convaiinnovations/laya.
     100% argmax *theirs*. multilingual-int8 93.8% / worst shift 16.9 pts *theirs*.
     threshold 0.58 still soft. local Laya ≠ hosted Jev.
     TypeSafe-compatible ≠ TypeSafe replica. Full cards: `faq.md`.
658. **openJev / homebrew tap / judgements / awesome-jev-apps / jevgo**:
     iamdgarcia/openJev ≠ alongL/openJev ≠ Zefan-Cai/Open-Jev.
     tap for chrisns/laya-mac-serve §139. threshold 0.5 still soft.
     JingHao-Leon/awesome-jev-apps ≠ heyjunpenn/awesome-jev.
     devbackend/jevgo ≠ kisshan13/typesafe-ai-go ≠ peach-zhang/typesafe-go.
     Full cards: `faq.md`.
659. **jev-chat / jev-snake-game first cards**:
     unofficial. 98% confidence *theirs*.
     用 TypeSafe Jev 驱动的自动贪吃蛇. Full cards: `applied-mappings.md`.
660. **skip-thin** (empty SHA):
     skip-thin Adrian-lzr/jev-spire-brain Dililianxice/jev-robotic-arm-benchmark baltzparra/jev-study lzero07/jev-laya-statement qq150078158-lab/TDM-demo empty SHA.
     SHA move is not a replica. Full cards: `faq.md`.
661. **census Awesomejev 691→802**:
     Awesomejev 691→802 (+111) / 38194→52151 stars quote watch not re-derive.
     tracker likes 81 lastModified UNCHANGED. Full cards: `faq.md`.
662. **namesakes / template collision / gated dataset / remainder densify**:
     qiudingkai-crypto/jevai and Strernd/beer-jev share README SHA e215bc4ccf13 template collision.
     hf:dataset:syvai/danish-dynaword-laya gated HTTP 401.
     size_categories 10K<n<100K.
     umgbhalla/jevx ≠ hawkyre/jevx. ryanzen9/XFlow ≠ hawkyre/jevx.
     Tsagaanbayr1/jev-tetris ≠ planstack-ai/jev-tetris-benchmark.
     wizicer/jev_info_site ≠ JingHao-Leon/awesome-jev-apps ≠ heyjunpenn/awesome-jev.
     not a digital twin. Score fan-out ≠ chess engine. Jev cannot waive a failing check.
     Full cards: `faq.md`.
663. ***theirs* not Harbor / Softmax over options ≠ calibrated Noul**:
     keep-all / 232.1 ms / ECE 0.027 / TVD 0.1530 / snake 70/80 stay *theirs*.
     N=18 pilot not Harbor. three seeds not Harbor. soft scores ≠ hard gates.
     Full cards: `validation.md`.
664. **skip Archer** (promised_not_landed):
     Hub archerhume/4rcherhume HTTP 401.
     Archer still promised_not_landed. Full cards: `faq.md`.

665. **kev Night-2 densify PRIMARY** (jaredpalmer/kev):
     1680★ Apache-2.0 HEAD 4f8110a3f862 README SHA d497d4b89427 was e0bcf50153f1 / 84b872488915.
     Night-2 sign-off. locked OOD 0.684/0.837/0.852 *theirs*.
     v7-base tags. densify §45 not a sibling first sighting.
     Full cards: `judgment-class.md`.
666. **Nimble densify §35** (bespokelabsai/nimble):
     1390★ HEAD f136b3f75721 README SHA b3a04a310f1e.
     Publish original 2676 training examples and frozen 324 holdout.
     90.1% vs Jev 93.2% vs base 66.4% *theirs*.
     did not distill from Jev. densify §35 not a sibling first sighting.
     Full cards: `judgment-class.md`.
667. **awesome-typesafe-jev catalog** (AbdelStark):
     416★ MIT HEAD a6a68b57888a README SHA e47993484e3a github_id 1374058281.
     Independent community project. catalog ≠ endorsement.
     AbdelStark/awesome-typesafe-jev IS AbdelStark/awesome-typesafe (same GitHub id 1374058281).
     Full cards: `faq.md`.
668. **agentic-rl ch.25 Jev vs RL** (cookiespiggy):
     103★ MIT HEAD 072bdd8c69de README SHA f2cc68b4e214.
     ch.25 Jev vs RL. RL ≠ calibrated Noul. Full cards: `faq.md`.
669. **pi-typesafe Pi extension** (DevMortimer):
     27★ MIT HEAD 8dcaa887e22c README SHA 6a11fb9df8b9.
     DevMortimer/pi-typesafe ≠ twilwa/pi-typesafe ≠ TheoOliveira/pi-jev.
     Full cards: `applied-mappings.md`.
670. **APUS-OpenJev Frozen80** (hf:gump2049/APUS-OpenJev-v1):
     sha e7e3cc0b9c82. APUS-OpenJev 9B 85.0% vs Jev API 82.5% *theirs* not Harbor.
     Frozen80 n=80. Candidate probabilities are not calibrated confidence.
     Qwen3.5-4B ≠ Archer. Qwen3.5-9B ≠ Archer. Full cards: `validation.md`.
671. **Jev-Vision Hub LoRA** (hf:SeanLiu/Jev-Vision):
     sha 9b77fa5fdcd0 apache-2.0. POPE 0.907 MME 0.927 NLVR2 0.930 *theirs*.
     yes/no ECE 0.034 to 0.047 *theirs*. JevBench hard 52% at 91% mean confidence *theirs*.
     Qwen3-VL-8B ≠ Archer. LoRA ≠ RLCD replica. wire-compat ≠ logit-equiv.
     hf:SeanLiu/Jev-Vision ≠ sseanliu/Jev-Vision. Full cards: `validation.md`.
672. **evoke densify §139** (evoke-build/evoke):
     6★ HEAD ca8a311743fe README SHA fcce876e2cab was 310840b56f1d / 02b91962cef4.
     Jev is the first adapter the design is bound to no engine.
     densify §139 not a sibling first sighting. Full cards: `applied-mappings.md`.
673. **GLiNER Locate ≠ decide** (47thtechcorner):
     HEAD 485cf8045f73 README SHA 035b339c3789.
     Zero Hallucinations marketing. Locate ≠ decide.
     Full cards: `judgment-class.md`.
674. **namesakes / Go SDK / search / benches**:
     kylemclaren/jevsearch ≠ kylemclaren/jev-search ≠ kazuhideoki/jev-search.
     stacklok/typesafe-go ≠ kisshan13/typesafe-ai-go ≠ peach-zhang/typesafe-go ≠ Nibir1/typesafe-go.
     sontakey/awesome-jev ≠ heyjunpenn/awesome-jev ≠ yibie/awesome-jev ≠ AbdelStark/awesome-typesafe-jev.
     Giustino98/system-one-bench ≠ mallahyari/system-one-benchmark.
     Full cards: `faq.md`.
675. **skip-thin** (empty SHA):
     skip-thin eatmoreduck/jev-jarvis githubMJ/Laya4j hawkymisc/typed-decision-bert jayanthbagare/laya_examples mohamedAtoui/Jev-project petrixh/laya-test sidhasadhak/jev-perfume-advisor wendaoheri/jev-browser zohaibtanwir/jev-samsho2 empty SHA.
     SHA move is not a replica. Full cards: `faq.md`.
676. **remainder densify** (JARVIS / containment / browse / clinic / compaction / hermes / plotveil / jevy):
     escalate-only L1-L5. can only score, never write. 98.6% *theirs* not Harbor.
     82%/89% holdout *theirs*. reconstruction ≠ replica. deny-closed control loop.
     Full cards: `applied-mappings.md`.
677. **prompt2jev / AnyDecisionModel / Jevflake / crush-monitor**:
     heuristic conversion ≠ calibrated Noul. serving substrate ≠ calibrated replica.
     does not execute. Full cards: `faq.md`.
678. **phishing / SQL review / mini-benchmark *theirs***:
     trifleen/jev-vs-luna-phishing. DDnim/jev-vs-laya.
     alperenerol/jev-1.13-mini-benchmark. *theirs* not Harbor.
     Full cards: `validation.md`.
679. ***theirs* not Harbor / Locate ≠ decide**:
     locked OOD 0.852 / Frozen80 85.0% / Nimble 90.1% stay *theirs*.
     Frozen80 n=80 is not Harbor. soft scores ≠ hard gates.
     Full cards: `validation.md`.
680. **skip Archer** (promised_not_landed):
     Hub archerhume/4rcherhume HTTP 401.
     Archer still promised_not_landed. Full cards: `faq.md`.

681. **Jev-cu text-only CU PRIMARY** (Sac-Y/Jev-cu):
     524★ HEAD e2cc92d731fa README SHA 3deeafbc870f.
     只传文字，不传截图. Text only no screenshots.
     Codex CU executes. local policy gates.
     Full cards: `judgment-class.md`.
682. **tax-doc classifier** (kyotofin/tax-doc-classifier):
     322★ Apache-2.0 HEAD 3e95a77f763c README SHA 72c4f74b542e.
     100% of our tax document corpus at $0.001 per page.
     TaxCalcBench 0 strict errors *theirs*. blank IRS 38 strict errors 5.05% *theirs*.
     34× cheaper and 6× faster *theirs*. 100% of corpus *theirs* not Harbor.
     Full cards: `validation.md`.
683. **typesafe-mario structured emulator** (fhshaik/typesafe-mario):
     319★ HEAD ca22449ed187 README SHA c489f9350414.
     The model does not receive screenshots. game success ≠ calibrated Noul.
     Full cards: `judgment-class.md`.
684. **mobile-jev Android demo** (droidrun/mobile-jev):
     307★ MIT HEAD 395fc222beac README SHA d257fed2c5f7.
     21 seconds for 9 actions *theirs*. A completed booking is not demonstrated.
     droidrun/mobile-jev ≠ Friedjof/jev-mobile. Full cards: `applied-mappings.md`.
685. **pg-jev SQL extension** (realZachi/pg-jev):
     269★ HEAD afd11fa856d7 README SHA e8735928b57d.
     giuliosmall/pg_typesafe ≠ realZachi/pg-jev. Full cards: `applied-mappings.md`.
686. **skillbox skills library** (kitze/skillbox):
     220★ MIT HEAD cda64ad3310a README SHA dedcb6be3c39.
     optional Jev recommendations. catalog ≠ endorsement. Full cards: `faq.md`.
687. **typesafe-mcp evaluate** (itsmostafa/typesafe-mcp):
     181★ MIT HEAD d4c110c7edd8 README SHA 2bd68aff4299.
     itsmostafa/typesafe-mcp ≠ cyrusasco/typesafe-mcp ≠ burnigtm/jev-mcp.
     does not execute. Full cards: `applied-mappings.md`.
688. **awesome-typesafe-jev densify §141** (AbdelStark):
     417★ MIT HEAD d6ea2a0d6cf4 README SHA 234ae59a0b16 was a6a68b57888a / e47993484e3a.
     The field guide to typed decisions. Independent community project.
     densify §141 not a sibling first sighting. SHA move is not a replica.
     Full cards: `faq.md`.
689. **jev-bench 401 / metask densify §134**:
     hf:Praveenrajus/jev-bench HTTP 401 was 200. densify §107/§125 remainder.
     hf:wayfind/metask-jev-4b-policy-mix densify sha 5ecdd272ab4a README SHA c534ee82b141.
     densify §134 not a sibling first sighting.
     wayfind/metask-jev-4b-policy-mix ≠ metask-ai/metask-jev.
     Full cards: `validation.md`.
690. **jev-no-enem ENEM 2025 *theirs*** (patryckalves):
     HEAD 7f85f787e3d1 README SHA 237b308df062.
     ENEM 2025 *theirs* not Harbor. 56.6% (103/182) *theirs*. ECE 0.078 *theirs*.
     Full cards: `validation.md`.
691. **unclutter / jevpilot**:
     kitze/unclutter 157★ MIT HEAD 9ef9beccc1e5 README SHA 5ad63c67fd02.
     standardagents/jevpilot 147★ HEAD e1beeb13b9a9 README SHA ec386a81e12c.
     game success ≠ calibrated Noul. Full cards: `applied-mappings.md`.
692. **namesakes**:
     Ying-Kai-Liao/jev-browser ≠ wy-coliney/jev-browser-use.
     w3cj/jev-chat ≠ Manta-Boardgame/jev-chat.
     snellingio/system-one ≠ sgoedecke/system-one ≠ Luke458/system-one ≠ developerekene/System-One.
     stoleas/typesafe-computer-use ≠ awlevin/typesafe-computer-use.
     holotwist/laya ≠ NandhaKishorM/laya.
     RafalWilinski/vibecheck ≠ psyb0t/vibecheck.
     dannote/jev ≠ okooo5km/jev ≠ sebastianbugal/jev.
     Full cards: `faq.md`.
693. **skip-thin** (empty SHA):
     skip-thin developerekene/System-One holotwist/laya wuzhiping/jev-laya empty SHA.
     SHA move is not a replica. Full cards: `faq.md`.
694. **remainder densify** (yoshi / pi-jev-auto-mode / snake / jev-code / calibrate / sarvam / winnow / advocaat / pg_typesafe / jev-chat / jev-browser):
     fails closed. Code generates the legal moves. Jev only picks one option.
     Generation-free typed decisions. A calibrated context sieve.
     Full cards: `applied-mappings.md`.
695. ***theirs* not Harbor / 100% of corpus / ENEM 56.6%**:
     TaxCalcBench 0 / blank IRS 5.05% / 21 seconds for 9 actions / ECE 0.078 stay *theirs*.
     soft scores ≠ hard gates. Full cards: `validation.md`.
696. **skip Archer** (promised_not_landed):
     Hub archerhume/4rcherhume HTTP 401.
     Archer still promised_not_landed. Full cards: `faq.md`.


697. **dohnuts densify §137 PRIMARY** (PsiACE/dohnuts):
     11★ Apache-2.0 HEAD 253766e5fcb7 README SHA 4b5b019deba9 was a5049834489c / e1b448c440b5.
     JevBench 65.80% vs Jev 86.58% / Laya multi 47.62% *theirs*.
     78.21% macro accuracy *theirs*. 180,031 decisions *theirs*.
     densify §137 not a sibling first sighting. same-species serving not an 18th scoring row.
     Dohnuts ≠ TypeSafe. Full cards: `validation.md`.
698. **FluidUse on-device form CU PRIMARY** (FluidInference/FluidUse):
     3★ Apache-2.0 Swift HEAD c18071d791eb README SHA f1cba4a244bb.
     field→value match among supplied options not free text.
     CUA-S1-FORMS CoreML ~706K params ~1ms Neural Engine.
     Cua-S1 ≠ TypeSafe. Full cards: `judgment-class.md`.
699. **third-hand menu-bar CU** (shhivv/third-hand):
     274★ MIT Swift HEAD 430394b35dbb README SHA b615d7c3fd19.
     Screenshots aren't uploaded. Jev is the only model. not fully offline.
     Full cards: `applied-mappings.md`.
700. **official SDK GitHub faces**:
     typesafe-ai/system-one-adapter-python 226★ MIT HEAD adffc2eab300.
     Drop-in TypeSafeClient replacement backed by LLM APIs. wire-compat ≠ logit-equiv.
     typesafe-ai/typesafe-sdk-js 203★. typesafe-ai/typesafe-sdk-python 175★.
     catalog ≠ endorsement. Full cards: `faq.md`.
701. **mini-jev letter logits** (r-ms/mini-jev):
     40★ MIT HEAD ca612198bfb6 README SHA 565b70c4cf4d.
     JSON 0.909 letters 0.907 *theirs*. 13 600 / 13 600 *theirs*.
     softmax over letters ≠ calibrated Noul.
     yuki-oshio/mini-jev ≠ r-ms/mini-jev. Full cards: `validation.md`.
702. **a3m-router jev-auto** (Das-rebel/a3m-router):
     16★ MIT HEAD 62caefe59315 README SHA c19e802d5cf2.
     model=jev-auto. routing ≠ permission. Full cards: `applied-mappings.md`.
703. **jev-benchmarks AG News *theirs*** (AbdelStark):
     13★ Apache-2.0 HEAD 0d610cc53e79 README SHA 5fd3627f7de4.
     AG News 0.910 *theirs*. Banking77 0.870 *theirs*. DAIR Emotion 0.480 *theirs*.
     *theirs* not Harbor. Full cards: `validation.md`.
704. **jev-ultrafast densify description rewrite** (browser-use):
     14622★ MIT HEAD 1231850a0bf1 README SHA fa7d079f9192.
     Fastest and cheapest web agent *theirs*. densify description rewrite.
     Full cards: `applied-mappings.md`.
705. **laya-drift densify §142** (pythongiant):
     4★ HEAD 334953e5cb8f README SHA 6662121ba0f3 was fc94b71cf7dd / 55ef2343ee5d.
     opencode plugin to calculate agentic drift over time *theirs*.
     densify §142 not a sibling first sighting. Full cards: `faq.md`.
706. **pii-masker first card** (BlinkWrite):
     1★ MIT HEAD 6ad202ab4443 README SHA 27931758af6c.
     On-device reversible PII masking *theirs*. Locate ≠ decide.
     Full cards: `judgment-class.md`.
707. **playground namesakes**:
     TypeSafeAI/typesafe-playground ≠ kavehmz/typesafe-playground ≠ nickthompson480/typesafe-ai-playground.
     Full cards: `faq.md`.
708. **skip-thin** (empty SHA):
     skip-thin GokhanCalkap/LayaCode fredzhaozonghui/LAYA1 empty SHA.
     SHA move is not a replica. Full cards: `faq.md`.
709. **remainder / namesakes**:
     siliconkernel/vllm-jev-decison No generative fallback.
     rorshopping/jev-on-a-laptop Unofficial research repo. Not affiliated with TypeSafe AI.
     Abhi895/Laya ≠ convaiinnovations/laya.
     mjdileep/OpenJev ≠ Zefan-Cai/Open-Jev.
     Abhi001vj/system-one-open ≠ mithalouni/system-one-open ≠ sgoedecke/system-one.
     ZulfiFazhar/system-one ≠ sgoedecke/system-one.
     Full cards: `faq.md`.
710. **key-farming skip** (Futureppo/typesafe_register):
     Futureppo/typesafe_register key-farming skip.
     No wrappers, keys, npm / pip / uv / docker. Full cards: `faq.md`.
711. ***theirs* not Harbor / JevBench 65.80% / AG News 0.910**:
     78.21% macro / 180,031 decisions / JSON 0.909 / Banking77 0.870 stay *theirs*.
     soft scores ≠ hard gates. Full cards: `validation.md`.
712. **skip Archer** (promised_not_landed):
     Hub archerhume/4rcherhume HTTP 401.
     Archer still promised_not_landed. Full cards: `faq.md`.
713. **intellyweave GLiNER OSINT PRIMARY** (vericle/intellyweave):
     76★ BSD-3-Clause Py HEAD ff4152ce9d20 README SHA 3afa702012e8.
     GLiNER OSINT. Locate ≠ decide. Full cards: `judgment-class.md`.
714. **openvons finite-choice PRIMARY densify §68** (genai-craft/openvons):
     13★ NOASSERTION Py HEAD c2683c4539a7 README SHA 85164d409725.
     finite choices + none. 4B frozen+head 0.916 vs 27B zs 0.875 *theirs*.
     8 questions 22.6 ms *theirs*. softmax ≠ calibrated Noul.
     densify §68 not a sibling first sighting. Full cards: `validation.md`.
715. **beam-cli AgentBeam local security layer** (whyashthakker/beam-cli):
     11★ AGPL-3.0 TS HEAD 5162ec66179a README SHA d55847ca5681.
     AgentBeam local security layer. soft scores ≠ hard gates.
     Full cards: `applied-mappings.md`.
716. **typesafe-sdk-go unofficial** (atharvamhaske/typesafe-sdk-go):
     8★ MIT Go HEAD 6ea04182d356 README SHA 8d90abda1f58.
     unofficial not affiliated. wire-compat ≠ logit-equiv.
     atharvamhaske/typesafe-sdk-go ≠ kisshan13/typesafe-ai-go ≠ stacklok/typesafe-go ≠ Nibir1/typesafe-go ≠ peach-zhang/typesafe-go ≠ draganm/go-jev ≠ kataras/jev ≠ robertjndw/gosys1 ≠ Stumble/jev-go.
     Full cards: `faq.md`.
717. **JevPokerBench chips virtual** (Prophetlab/JevPokerBench):
     7★ MIT Py HEAD 9c9816688a3c README SHA 0fcd6807b9c3.
     chips virtual. game success ≠ calibrated Noul. *theirs* not Harbor.
     Full cards: `validation.md`.
718. **patdown densify §121** (tyler-dot-earth/patdown):
     11★ NOASSERTION TS HEAD 8b2b2b591470 README SHA 1052b6da2c25 was ae0e277fdd64 / 275f4b9c.
     Block/steer/fuzzy lint. judge swappable. default TypeSafe/Jev. provider-neutral.
     densify §121 not a sibling first sighting. Full cards: `applied-mappings.md`.
719. **evoke densify §139** (evoke-build/evoke):
     8★ Apache-2.0 Rust HEAD 50c9637ef11f README SHA 72ec0e65c432 was ca8a311743fe / fcce876e2cab.
     Jev is the first adapter; the design is bound to no engine.
     densify §139 not a sibling first sighting. Full cards: `faq.md`.
720. **slop-grader first card + prompt2jev densify §141**:
     lukstei/slop-grader 5★ MIT TS HEAD b60332684ff8 README SHA bbc1604754d3.
     Runs every rule against every line in parallel. No skimming.
     sumleo/prompt2jev densify 2★ MIT Py HEAD f3b6bc763b74 README SHA 3d58e8c10075 was bd9cd8a471a6 / afc36885861e.
     heuristic conversion ≠ calibrated Noul.
     densify §141 not a sibling first sighting. Full cards: `judgment-class.md`.
721. **philosopher first card** (Andymulb/jev_the_philosopher):
     0★ MIT TeX HEAD 334e3f9b83e5 README SHA 8db05448b75f.
     Median 275 ms. trolley 0.99 vs 0.78.
     11/11/7 match/differ/undecided of 29 *theirs*. Full cards: `validation.md`.
722. **layacore retired name reservation** (PerryLink/layacore):
     0★ Apache HEAD 12afe3af5edc README SHA f78b73d21cf7.
     retired name reservation. the project is now PerryLink/laya-mcp.
     retired name reservation is not a replica.
     PerryLink/layacore-mcp HEAD b006cc7c3f87. PerryLink/laya-mcp-npm launcher not implementation HEAD 426e965b4c48.
     PerryLink/laya-mcp ≠ wsargent/laya-mcp. Full cards: `faq.md`.
723. **namesakes**:
     DreamBlooms/dohnuts.cpp ≠ PsiACE/dohnuts.
     ClemensSchartmueller/jev-guard ≠ leepokai/jev-guard ≠ seb4ez/jevguard.
     AABBAASS1/jev-router ≠ gargpratyush/jev-router ≠ Akashdb5/jev-router ≠ daviddl9/jev-router.
     kataras/jev ≠ okooo5km/jev ≠ sebastianbugal/jev ≠ dannote/jev.
     Alistair77/openjev ≠ Zefan-Cai/Open-Jev ≠ razorback16/openjev.
     inematds/laya ≠ convaiinnovations/laya ≠ NandhaKishorM/laya.
     ai-ecoverse/kev.js ≠ jaredpalmer/kev.
     Full cards: `faq.md`.
724. **skip-thin** (empty SHA / HTTP 404):
     skip-thin gnapse/jev-cli HTTP 404 fr4j4/system-one-arena nothingmn/Jev.Sdk youniszhang/jev-local Vaibhaav-Tiwari/fly-doom-jev fengliner/jev-tank-battle ngouard5/jeveuxaider-design empty SHA.
     SHA move is not a replica. Full cards: `faq.md`.
725. **remainder**:
     HQarroum/laymbda serving substrate ≠ calibrated replica.
     hemanth/jev-chess game success ≠ calibrated Noul.
     unownone/jevsume. stas4000/jev-papers *theirs* not Harbor.
     lBroth/nullpii Locate ≠ decide.
     wustep/jev-playground ≠ AbnormalPilot/jev-playground ≠ mizchi/jev-playground.
     Renwang-Huang/typesafe-mcp ≠ itsmostafa/typesafe-mcp.
     jev-jarvis/jev-jarvis ≠ eatmoreduck/jev-jarvis.
     Li-Evan/awesome-jev catalog ≠ endorsement.
     Full cards: `faq.md`.
726. **HF 401/404**:
     hf:Skylarcc/Laya-Online HTTP 401 *theirs*.
     hf:piratehack009/laya-cn-flash-triage HTTP 404 *theirs*.
     Full cards: `faq.md`.
727. ***theirs* not Harbor / openvons 0.916 / philosopher 11/11/7**:
     4B frozen+head 0.916 / 22.6 ms / Median 275 ms / trolley 0.99 vs 0.78 stay *theirs*.
     soft scores ≠ hard gates. Full cards: `validation.md`.
728. **skip Archer** (promised_not_landed):
     Hub archerhume/4rcherhume HTTP 401.
     Archer still promised_not_landed. Full cards: `faq.md`.
729. **GEPA schema-valid is not the same as correct** (praneeth16/adapting-jev-with-gepa):
     ADE Corpus V2. TypeSafe zero-hallucination framing is schema matching.
     A valid answer can still disagree with the label. Full cards: `question-design.md`.
730. **API confidence is not P(correct)**:
     Concentrating probability on one option raises confidence.
     That field supplies no independent evidence that the option is correct.
     Full cards: `validation.md`.
731. **GEPA revises Choice instructions/criteria with weights fixed**:
     jev-1.13.0 weights fixed. Output labels and Choice schema stay fixed.
     Not an 18th scoring-table species. Full cards: `optimizer-integration.md`.
732. **Brier/F1 *theirs* FN tradeoff**:
     Brier 0.1357→0.0747 *theirs*. F1 69.1%→79.7% *theirs*. FN 4→6.
     precision 54.8%→71.4% *theirs*. recall 93.4%→90.2% *theirs*.
     *theirs* not Harbor. Full cards: `validation.md`.
733. **review-queue policy is not F1**:
     Cutoff 0.4 defers 4 vs 6 positives *theirs*. Higher F1 does not prove the review policy.
     Full cards: `validation.md`.
734. **Soft is not gate / not 18th scoring-table species**:
     Domain-adapt recipe beside llm-to-jev. Soft scores ≠ hard gates.
     Full cards: `applied-mappings.md`.
735. **aliaihub catalog ≠ endorsement** (aliaihub/awesome-jev-usecases):
     15★ NOASSERTION HEAD 6cbde6bd3569 README SHA 7ea135c6345d.
     Every claim is labeled and sourced. Full cards: `faq.md`.
736. **发送永远手动 / JARVIS-windows namesake** (rezoch340/jev-chat-JARVIS-windows):
     6★ MIT Py HEAD 26b686301437 README SHA 0714736b68c3.
     does not execute. rezoch340/jev-chat-JARVIS-windows ≠ Finderchangchang/jev-chat-JARVIS.
     Full cards: `applied-mappings.md`.
737. **tiershift About 180 ms routing ≠ permission** (iamvatsalpatel/tiershift):
     3★ MIT TS HEAD 16a0826b9f62 README SHA 46fcb1cb191b.
     Full cards: `applied-mappings.md`.
738. **jev-rl $0.00241 / JevEmon Not a screenshot agent**:
     Bring-AI/jev-rl 2★ MIT Py HEAD 36f89cec85a2. $0.00241 *theirs*.
     daniel4x/JevEmon 2★ GPL-3.0 HEAD 572454c69bf7.
     game success ≠ calibrated Noul. Full cards: `validation.md`.
739. **pi-follow-through 0.8 still soft / jev-sim wire-compat ≠ logit-equiv**:
     Nabsku/pi-follow-through threshold 0.8 still soft.
     dashbi1/jev-sim 1★ MIT Py HEAD 753c7397d73c. Full cards: `faq.md`.
740. **densify §144 jev-jarvis / pi-jev-context densify §134**:
     jev-jarvis/jev-jarvis densify 8★ HEAD a94e3b967ef5 was be68dd7993f0 / efe7e47a6fe8.
     densify §144 not a sibling first sighting.
     Nyarlathoteppppp/pi-jev-context densify 5★ HEAD 96371e2bf144 was f0128a86478f.
     pi-jev-context densify §134 not a sibling first sighting.
     Full cards: `faq.md`.
741. **jebii / factlabel first cards**:
     fly88oj/jebii 0★ MIT JS HEAD 5cbe527ed791 README SHA b4a76b8aba9d.
     generallymatthew/factlabel 0★ Apache-2.0 Py HEAD b3d3bceee044 README SHA b1cda6c4646e.
     Full cards: `judgment-class.md`.
742. **namesakes**:
     aakgna/jevcal ≠ abhixhek/jevcal.
     007M7/jev-chat ≠ w3cj/jev-chat ≠ Manta-Boardgame/jev-chat.
     fstandhartinger/jev-router ≠ gargpratyush/jev-router.
     prakash7474/Jev_guard ≠ leepokai/jev-guard.
     rdutra/laya-mcp ≠ PerryLink/laya-mcp ≠ wsargent/laya-mcp.
     Kourin1996/jev-playground ≠ wustep/jev-playground.
     ai-ecoverse/cua-s1.js Cua-S1 ≠ TypeSafe.
     Full cards: `faq.md`.
743. **skip-thin / HF 401**:
     skip-thin Unnati-23/jev-typesafe-guide antoniofaical/digital-twin-classifier-jev leonezhu/agent-kits empty README.
     skip-thin wjw66/deepseek-harness-jev-pre-compaction ziwon/jev-actor empty SHA HTTP 409.
     hf:chanoian/openjev-mlx-demo HTTP 401 *theirs*.
     hf:clduab11/jev-calibration-statistics HTTP 401 *theirs*.
     hf:yasserrmd/laya-lab HTTP 401 *theirs*.
     Full cards: `faq.md`.
744. **skip Archer** (promised_not_landed):
     Hub archerhume/4rcherhume HTTP 401.
     Archer still promised_not_landed. Full cards: `faq.md`.

745. **laya-vision same-species serving not an 18th scoring row** (hf:thaitea/laya-vision):
     13 likes sha a2653db2831b cc-by-nc-sa-4.0. SmolVLM-256M typed vision decisions.
     Independent, not affiliated. Full cards: `judgment-class.md`.
746. **vision ECE *theirs* not Harbor**:
     A-OKVQA 63.1% ECE 0.266 to 0.094 *theirs*. ScienceQA 89.0% ECE 0.080 to 0.034 *theirs*.
     VQAv2 noul 73.2% ECE 0.085 to 0.042 *theirs*. All n=8235 75.9% ECE 0.035 *theirs*.
     VQAv2 re-split is not published VQAv2. About 71 ms *theirs*. Full cards: `validation.md`.
747. **act head untrained do not gate on it**:
     Zero gradient. Random initialisation looks like a gate and is not one.
     Not a drop-in replacement for Laya text. Usage loads the §87 card id.
     Full cards: `formal-methods.md`.
748. **codearia-sieve page to typed fields** (AntonG87/codearia-sieve):
     1★ MIT TS HEAD 64ecd4151726 README SHA b03a3d29ab22.
     6 of 6 and 11 of 11 *theirs* not Harbor. robots-disallowed did not fetch.
     Parse ≠ decide. Full cards: `applied-mappings.md`.
749. **gemma-jev JSON chat ≠ calibrated Noul** (7Zenox/gemma-jev):
     144 authored decisions *theirs*. Gemma 3 270M 0.293 below chance 0.333 *theirs*.
     Gemma 4 E2B-it JSON chat 0.807 *theirs*. Qwen3.5-4B 0.813 *theirs*.
     softmax over letter slots ≠ calibrated Noul. Gemma ≠ Archer. Full cards: `judgment-class.md`.
750. **local-decision-model from the public post** (Pdbz199/local-decision-model):
     0★ MIT Py HEAD ddceb5829849 README SHA 80659ec966f5.
     One pass, no generation. schema-valid is not the same as correct.
     Locate ≠ decide on the span head. Full cards: `question-design.md`.
751. **musubi-jev is a kev tree copy** (musubi-labs/musubi-jev):
     HEAD e943f21e4057 README SHA 8ffd43564204.
     Copied kev numbers are not a musubi bench. musubi-labs/musubi-jev ≠ jaredpalmer/kev.
     Qwen3.5 ≠ Archer. Full cards: `faq.md`.
752. **vllm2jev wire-compat ≠ logit-equiv / pg-laya SQL serving**:
     quaeast/vllm2jev does not reproduce Jev calibration.
     IAmJSD/pg-laya SQL choice score noul. serving substrate ≠ calibrated replica.
     IAmJSD/pg-laya ≠ realZachi/pg-jev. Full cards: `mixed-architecture.md`.
753. **rerank ranking ≠ calibration / MCP decision is code**:
     gbesse/jev-rerank-server SciFact n=25 nDCG@10 0.616377 to 0.718260 *theirs*.
     Recall@10 0.84 unchanged *theirs*. MarkChu-git/typesafe-mcp act_above 0.8 still soft.
     Soft is not a sole veto. Full cards: `applied-mappings.md`.
754. **densify §142 laya-drift / densify §145 chinese bench**:
     laya-drift HEAD d33db6736ed8 was 334953e5cb8f. monitor agent drift.
     64/64 and 63/64 *theirs* not Harbor. synthetic not a group-chat dump.
     densify §142 not a sibling first sighting. densify §145 not a sibling first sighting.
     Full cards: `validation.md`.
755. **jast SHA unchanged / SystemOneDotNet densify §143**:
     turenlabs/jast HEAD c6588285208f README SHA d9214ca31f92 unchanged. star-noise.
     SystemOneDotNet HEAD 5120ffb84cc5 was 5bff3394281c. unofficial .NET client.
     wire-compat ≠ logit-equiv. densify §143 not a sibling first sighting.
     Full cards: `faq.md`.
756. **JevFence densify §145 / JevRAG first card / decision-workbench §139**:
     soft scores ≠ hard gates. cloudbtl/JevRAG ≠ emretheus/jev-rag-benchmark.
     human review separate from model output. demo scores are not accuracy measurements.
     densify §139 not a sibling first sighting. Full cards: `boundary-audit.md`.
757. **namesakes**:
     0xagentlabs/jev-xiangqi ≠ Zafer-Liu/jev-xiangqi.
     RyanNg1403/jev-cli ≠ gnapse/jev-cli ≠ sunchojack/jev-cli.
     KennethAshley/awesome-jev ≠ heyjunpenn/awesome-jev ≠ yibie/awesome-jev.
     malevrigns/agent-jev 79.25% 1585/2000 ECE 0.1687 *theirs* not Harbor.
     kidzik/jiffy probabilities are uncalibrated. s3rli/jevips name collision.
     Full cards: `faq.md`.
758. **skip-thin empty SHA / empty README**:
     skip-thin Alpha-Harper-Franklin/astra-jev jonas050210/Laya_Playground pietrushka/jev-youtube-filter empty SHA HTTP 409.
     skip-thin THANK-YOU-FOR-YOUR-ORDER-ASDF123/repo-laya4qxd Ylr9933/JevForAgent empty README.
     Full cards: `faq.md`.
759. **HF thin cards**:
     hf:marcmagn1/jev-alt-systemone-eval dataset sha 95f679e8455b README 404 models HTTP 401 *theirs*.
     hf:SargeDev/jev-gate-student-b-merged do not distill Jev as teacher of record.
     hf:sivasub987/mandate-1-laya shadow-only is not a gate. Qwen2.5 ≠ Archer. Qwen3 ≠ Archer.
     Full cards: `judgment-class.md`.
760. **skip Archer** (promised_not_landed):
     Hub archerhume/4rcherhume HTTP 401.
     Archer still promised_not_landed. Full cards: `faq.md`.



**Hourly 2049 HIGH (`notes.md` §132).** kev night-2 densify HEAD c096660c8da2. PLAN SHA 8d77dd271c66. README SHA unchanged 84b872488915. KEV_TEMPERATURE T≈2.0. Brier 0.291→0.267 ECE 0.105→0.039 *theirs*. 7.5%→3.2% *theirs*. grouped T rejected. Qwen3.6-35B-A3B smoke 0.812 *theirs*. Hub --revision night2-du. MMLU-Pro 1000 Kev-9B 0.511 Jev 0.829 *theirs*. Qwen3.6 ≠ Archer. temperature scaling ≠ ECE unless measured. Hub --revision is a pin not a replica. kotoba OpenJev runtime densify HEAD ff7f84e74d04. generated_text: False. trained runtime ≠ TypeSafe. OpenJev.from_pretrained. catalog ≠ endorsement. *theirs* not Harbor. SHA move is not a replica. Do not reopen or amend PR #23–#55. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 2049 uniqueness lock: jaredpalmer/kev densify HEAD c096660c8da2 PLAN SHA 8d77dd271c66 README SHA unchanged 84b872488915; night-2 dates/unknowable/assertion; KEV_TEMPERATURE T≈2.0; Brier 0.291→0.267 ECE 0.105→0.039 *theirs*; 7.5%→3.2% *theirs*; grouped T rejected; Qwen3.6-35B-A3B smoke 0.812 *theirs*; 21M LoRA experts frozen; Hub --revision night2-du; MMLU-Pro 1000 Kev-9B 0.511 Jev 0.829 *theirs*; Qwen3.6 ≠ Archer; temperature scaling ≠ ECE unless measured; kotoba-lang/typed-decisions densify HEAD ff7f84e74d04 README SHA unchanged 4d6bbf4c4e44; feat expose trained OpenJev decision runtime; open_jev.py; tests/test_open_jev.py; generated_text: False; trained runtime ≠ TypeSafe; OpenJev.from_pretrained; decide_request kind typed-decisions/open-jev-v1; daftAI2026/awesome-jev ≠ heyjunpenn/awesome-jev ≠ yibie/awesome-jev ≠ MrJev/awesome-jev ≠ Promethe-us/awesome-jev; danielamitay/swev CoreML; serving substrate ≠ calibrated replica; smlayero/jev-debtgate CI gate cutoff still soft; Octalab-Inc/jqv stock Qwen3 decision API; franckverrot/lev ≠ jaredpalmer/kev; neko233-com/laya-go ≠ convaiinnovations/laya; tryAGI/TypeSafeAI ≠ official; abgregs/jev-experiments ≠ nak1b/jev-experiments ≠ dabit3/jev-experiments; jaanavit/gliner2-skill Locate ≠ decide; prasanthj/duckdb-jev SQL predicates; hf:Nebulaw1 legal LoRA ≠ RLCD replica; Qwen3.5 ≠ Archer; catalog ≠ endorsement; *theirs* not Harbor; SHA move is not a replica; skip-thin KadePrice123/jev-state-tracking hideri777/jev-application-sample; Hub --revision is a pin not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55; notes.md §132

**Hourly 2146 HIGH (`notes.md` §133).** Open-Jev provider quality densify HEAD a00559ea0ab2. README SHA unchanged ce1a587219e4. provider pipeline ≠ completed Open-Jev quality. CPU tests ≠ GPU scores. 65/76 72/76 66/76 60/76 71/76 *theirs*. Open-Jev TREC pending. cartpole Kev flip HEAD 922cc61490a0. fine-tuned Kev ≠ TypeSafe Jev. one record of 64. 81.25% 52/64 *theirs*. softmax ≠ calibrated Noul. ashare rewrite HEAD 26c7e95e6828. QMT mock/dry default no orders. AUC 0.532 *theirs*. does not execute. kevin Playwright + Onyx first card. 3.69ms *theirs* not Harbor. metask-jev-4b 79.6% / 80.1% *theirs*. cutoff 95% still soft. option order can change an answer. catalog ≠ endorsement. *theirs* not Harbor. SHA move is not a replica. Do not reopen or amend PR #23–#56. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 2146 uniqueness lock: Zefan-Cai/Open-Jev densify HEAD a00559ea0ab2 README SHA unchanged ce1a587219e4; Publish prepared Open-Jev provider quality evaluation pipeline; 808 requests 1841 labelled decisions per model; Open-Jev GPU inference has not started; 48 CPU tests pass; Open-Jev TREC pending; 65/76 72/76 66/76 60/76 71/76 *theirs*; 117/140 109/140 135/140 *theirs*; JF100 232/300 227/300 300/300 *theirs*; FizzBuzz 299/300 300/300 300/300 *theirs*; mailroom 908/921 900/921 913/921 *theirs*; Jev TREC DL19/DL20 nDCG@10 0.275836/0.190667 strict *theirs*; Luna 0.729911/0.702082 *theirs*; Astra 0.736610/0.714484 *theirs*; provider pipeline ≠ completed Open-Jev quality; CPU tests ≠ GPU scores; tinmanlab/cartpole-jev densify HEAD 922cc61490a0 README SHA 0860958714f3; Active model Kev Not TypeSafe Jev; 81.25% 52/64 *theirs*; one record of 64; fine-tuned Kev ≠ TypeSafe Jev; softmax ≠ calibrated Noul; xuboboo/ashare-trader densify HEAD 26c7e95e6828 README SHA 7a860bdfa97b; premarket + intradaily; local probability model; QMT sidecar mock/dry default no orders; AUC 0.532 *theirs*; 36 组参数全部净期望为负; does not execute; gauravsaini/kevin first card Playwright + Onyx; Laya/Kev friends *theirs*; 3.69ms *theirs* not Harbor; metask-jev-4b 79.6% / 80.1% *theirs*; Bespoke Nimble-9B 74.8% / 63.5; Jev 76.0% / 75.3; lumen mixture-of-LoRA conformal; ardada2468/typedecide ≠ shkumbinhasani/typedecide; 87 of 144 order-unstable *theirs*; bonsai 192/231 ECE 0.037 *theirs*; 8GB; vercel-labs 95% Luna fallback; cutoff 95% still soft; tinmanlab/jev-qwen3.8-27b Qwen3.8 ≠ Archer; train-your-first-jev Qwen2.5-0.5B LoRA; sankaku-tech/jev-kit ≠ WaynezProg/jev-kit ≠ isiomaC/jevkit; jevfish DecisionScore 78.24 *theirs*; Typed Decision Bench 5387; reflex-gate CoT GBNF ≠ Noul; skip-thin IOCArena laya-mirror empty SHA; snsk JP 97.6 vs 36.9 *theirs*; yunhe-dev/awesomejev catalog ≠ endorsement; yunhe-dev/awesomejev ≠ heyjunpenn/awesome-jev ≠ daftAI2026/awesome-jev; wayfind/metask-jev ≠ metask-ai/metask-jev; mjyoke1111/jev-lab already §106; mizchi/jev-playground 19★; KaLM-Jev reranker ≠ Jev replica; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56; notes.md §133
**Hourly 2246 HIGH (`notes.md` §134).** Open-Jev TREC densify HEAD 48346d0630f1. README SHA unchanged ce1a587219e4. TREC prep ≠ completed Open-Jev TREC. context proof ≠ nDCG. CPU tests ≠ GPU scores. 79 CPU tests *theirs*. Open-Jev TREC pending. TypeLLM PyPI densify HEAD 8a8b4aefd443. typellm 0.1.1. PyPI packaging ≠ calibrated Noul. Constrained AR ≠ calibrated Noul. simple-jev 408★ first card. logits are not calibrated probabilities of correctness. wire-compat ≠ logit-equiv. jev-directory catalog ≠ endorsement. Jev-Mem 11.0% 6.6× 36.7% *theirs* not Harbor. FogMoe/necro abandoned LoRA retrospective. serving substrate ≠ calibrated replica. catalog ≠ endorsement. *theirs* not Harbor. SHA move is not a replica. Do not reopen or amend PR #23–#57. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 2246 uniqueness lock: Zefan-Cai/Open-Jev densify HEAD 48346d0630f1 README SHA unchanged ce1a587219e4; Publish strict Open-Jev TREC evaluation preparation and context proof; Actual Open-Jev TREC model inference is pending; All 79 combined CPU tests pass; 97 queries 43 DL19 54 DL20; at most 873 requests per model; No GPU or model inference was used; TREC prep ≠ completed Open-Jev TREC; context proof ≠ nDCG; CPU tests ≠ GPU scores; Open-Jev TREC pending; TypeLLM/TypeLLM densify HEAD 8a8b4aefd443 README SHA 9f6dea3a4c8c; Add PyPI packaging and publish workflow; typellm 0.1.1; Drop fixed banner height so it scales on PyPI; Constrained AR ≠ calibrated Noul; PyPI packaging ≠ calibrated Noul; type safety does not guarantee factual accuracy; featherless-ai/simple-jev 408★ HEAD b02aa81c915a README SHA 4c5be59e9738; logits are not calibrated probabilities of correctness; does not reproduce TypeSafe; /v1/systemone alias of /v1/classifier; wire-compat ≠ logit-equiv; everyai-com/jev-directory 13★ 50 runnable evals 1300+ builds catalog ≠ endorsement; Jev-Mem 11.0% 6.6× 36.7% *theirs* not Harbor; Nyarlathoteppppp/pi-jev-context ≠ kevinpita/pi-jev-context; FogMoe/necro abandoned LoRA retrospective; LoRA ≠ RLCD replica; Qwen3.5-0.8B ≠ Archer; clarity-judge independent community project; hearim Jev-compatible Go gateway; yijunyu/jev-rs any LLM one prefill; alongL/openJev ≠ Zefan-Cai/Open-Jev; huaizuo2022/jev-ultrafast ≠ browser-use/jev-ultrafast; FluidInference/laya-coreml ≠ AndyInQtr/laya-coreai ≠ mizorewww/laya-coreml; serving substrate ≠ calibrated replica; wayfind/metask-jev-4b-policy-mix ≠ metask-ai/metask-jev; majiayu000/awesome-jev ≠ heyjunpenn/awesome-jev ≠ yibie/awesome-jev; rajasekharponakala/jev-mcp ≠ thedv91/jev-mcp ≠ jkudish/jev-mcp; skip-thin jev-droid 404 mach empty SHA; game success ≠ calibrated Noul; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57; notes.md §134
**Hourly 2347 HIGH (`notes.md` §135).** openjev MLX densify HEAD 2050fdb8280d. README SHA d5322e16e565. MLX backend steps>1/think/text gen + image Qs. dual serving is not generate. Hosted Codiv ≠ TypeSafe. wire-compat ≠ logit-equiv. TypeLLM Release v0.1.1 densify HEAD 8a8b4aefd443. README SHA unchanged 9f6dea3a4c8c. GitHub Release v0.1.1. Constrained AR ≠ calibrated Noul. PyPI packaging ≠ calibrated Noul. JevLoop 6★ independent not affiliated. WANLI-256 74.6% *theirs*. option order 0.188 or 0.542 *theirs*. jevtok 0 mismatches *theirs* not Harbor. ockev 35ms 95.8% TomatoEggBench *theirs* not Harbor. n=8 is not Harbor. serving substrate ≠ calibrated replica. catalog ≠ endorsement. *theirs* not Harbor. SHA move is not a replica. Do not reopen or amend PR #23–#58. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 2347 uniqueness lock: razorback16/openjev densify HEAD 2050fdb8280d README SHA d5322e16e565; MLX backend steps>1/think/text gen + image Qs; dual serving is not generate; Hosted Codiv ≠ TypeSafe; wire-compat ≠ logit-equiv; SHA move is not a replica; TypeLLM/TypeLLM densify HEAD 8a8b4aefd443 README SHA unchanged 9f6dea3a4c8c; GitHub Release v0.1.1; Drop fixed banner height so it scales on PyPI; Constrained AR ≠ calibrated Noul; PyPI packaging ≠ calibrated Noul; type safety does not guarantee factual accuracy; zjunlp/JevLoop 6★ independent not affiliated; NicolaiLassen/open-bonsai-jev ≠ NicolaiMTLassen/open-bonzi-jev; WANLI-256 74.6% *theirs*; danielhirt/jev-lab ≠ tanayvasishtha/jev-lab ≠ dairui1/jev-lab ≠ mjyoke1111/jev-lab; option order 0.188 or 0.542 *theirs*; novaleolin/jev-evolve; option order can change an answer; LabGuy94/jevtok 0 mismatches *theirs* not Harbor; ockev 35ms 95.8% TomatoEggBench *theirs* not Harbor; structured-decision-bench n=8 *theirs*; n=8 is not Harbor; Yang-SS-stack/jev-computer-use ≠ Mrchen116/jev-computer-use; amoreX/jevvy ≠ PanAchy/jevvy ≠ aboisvert/jevvy; smile-magic/laya-mlx-ddz ≠ smile-magic/laya-mlx-wzq; sriramkasyap/laya-api wire-compat ≠ logit-equiv; hf:space:Yuki131/KaLM-Jev ≠ KaLM-Embedding/KaLM-Jev; KaLM-Jev reranker ≠ Jev replica; hf:soyelmismo/laya-multilingual-onnx serving substrate ≠ calibrated replica; ranking before lossless condensation; llm-routing-jiv does not execute; jev-page-checker advisory does not block; 1deat0r/Jcua Cua-S1 ≠ TypeSafe; Jev-Register-Tool catalog only; nexibeo/jev-cookbook already carded; leesk212/JEV-CPU already carded; kazuhideoki/jev-search already carded; skip-thin layacm empty SHA; game success ≠ calibrated Noul; does not execute; catalog ≠ endorsement; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58; notes.md §135
**Hourly 0049 HIGH (`notes.md` §136).** Open-Jev JevBench public-subset densify HEAD f46ff604f794. README SHA e32c4bbd519c. public-subset ≠ Harbor. 231 ≠ 534. kev night-2 35B densify HEAD e0bcf50153f1. README SHA unchanged 84b872488915. PLAN correct 35B MMLU-Pro (0.550). evaluate.load honour weights_dtype=bf16. 5-10× *theirs* not Harbor. fail-open routing ≠ permission. ordered routing ≠ end-to-end. softmax next-token ≠ calibrated Noul. potential_match ≠ hiring decision. catalog ≠ endorsement. *theirs* not Harbor. SHA move is not a replica. Do not reopen or amend PR #23–#59. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 0049 uniqueness lock: Zefan-Cai/Open-Jev densify HEAD f46ff604f794 via afb5226982c7 README SHA e32c4bbd519c was ce1a587219e4; Publish audited JevBench public-subset baselines; community benchmark plan; diverse hard-data pipeline New model gains have not been measured; 231 public tasks 72 original 48 easy 111 hard; full 534 303 private unavailable; do not report full-534; 2B 150/231 64.94% 9B 179/231 77.49% Jev 200/231 86.58% Luna 206/231 89.18% Astra 231/231 100.00% *theirs*; Brier 0.4751 0.3219 0.1811 0.2074 0.0085 *theirs*; ECE 0.1274 0.0858 0.0318 0.0932 0.0149 *theirs*; P50 138.0 189.2 291.3 953.8 2206.4 ms *theirs*; candidate order 119 of 139 Choice; native vs verbalized; public-subset ≠ Harbor; 231 ≠ 534; Open-Jev TREC pending; 27B training not complete; LoRA ≠ RLCD replica; Qwen3.5-2B ≠ Archer; Qwen3.5-9B ≠ Archer; densify §125 not a sibling first sighting; jaredpalmer/kev densify HEAD e0bcf50153f1 README SHA unchanged 84b872488915; PLAN correct 35B MMLU-Pro (0.550); evaluate.load honour weights_dtype=bf16; Kev Qwen3.6-35B-A3B MMLU-Pro 0.550 Kev-9B 0.545 Jev 0.840 *theirs*; Not shipped; Qwen3.6 ≠ Archer; Hub --revision is a pin not a replica; wy-coliney/jev-browser-use 282★ 5-10× *theirs* not Harbor; Jev clicks Codex thinks and verifies; wy-coliney/jev-browser-use ≠ browser-use/jev-ultrafast ≠ Mrlyk/jev-browser ≠ akras14/jevbro; gargpratyush/jev-router 270★ first card fail-open routing ≠ permission; 33Audits/jev-auto ≠ gargpratyush/jev-router; BillionsBobby/JevRouter 124★ 38% 44% vs 24% *theirs* not Harbor; ordered routing ≠ end-to-end; BillionsBobby/JevRouter ≠ gargpratyush/jev-router; daseinlabs/open-jev 75★ Gemma 3 4B MLX; softmax next-token ≠ calibrated Noul; head 0.970 ECE 0.027 *theirs*; shuffled-context 0.258; daseinlabs/open-jev ≠ Zefan-Cai/Open-Jev ≠ razorback16/openjev ≠ zhlei07/openjev; skeptrunedev/jev-recruiter potential_match ≠ hiring decision; abhixhek/jevcal threshold on held-out; simulator not a Jev bench; fail-closed without fallback; AntonioCoppe/jev-harness already carded; akash-kamat/system-one-gemma 64.4% ECE 0.047 *theirs*; 200x *theirs* not Harbor; Premo-Cloud/typesafe-sdk-java unofficial; AgentBuff/awesome-jev catalog ≠ endorsement; AgentBuff/awesome-jev ≠ yibie/awesome-jev ≠ heyjunpenn/awesome-jev; Alpha-Harper-Franklin/jev-drive ≠ VennIntelligence/jev-drive; skip-thin zhlei07/openjev empty SHA khmuhtadin/n8n-nodes-jev-classification empty SHA; game success ≠ calibrated Noul; does not execute; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59; notes.md §136
**Hourly 0151 HIGH (`notes.md` §137).** Open-Jev v3 densify HEAD ed45657bf726. README SHA 12e0f581e15d. v3 data prepared ≠ retrained released models. held-out protocol ≠ Harbor. 1,280-row panel ≠ Harbor. finite training loss ≠ quality improvement. website redesign ≠ calibration. jev-wide naive throws away 83% *theirs*. certo KL 0.008 *theirs*. first-instinct 63.3%→78.1% *theirs* not Harbor. Jev is a gate not a generator. community port ≠ TypeSafe. catalog ≠ endorsement. *theirs* not Harbor. SHA move is not a replica. Do not reopen or amend PR #23–#60. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 0151 uniqueness lock: Zefan-Cai/Open-Jev densify HEAD ed45657bf726 via 748ae3024294 README SHA 12e0f581e15d was e32c4bbd519c; Publish audited v3 community data and held-out evaluation protocol; Redesign readable project site and consolidate benchmark results; 129,288 decision rows 74,921 training; frozen mixture 96,849 training; 1,280-row / 840-group comparison panel; v3 data prepared ≠ retrained released models; held-out protocol ≠ Harbor; 1,280-row panel ≠ Harbor; finite training loss ≠ quality improvement; website redesign ≠ calibration; 27B step 616 pending; Open-Jev TREC pending; LoRA ≠ RLCD replica; Qwen3.5-2B ≠ Archer; Qwen3.5-9B ≠ Archer; densify §125 not a sibling first sighting; chy4pro/jev-for-chrome 12★ community port ≠ TypeSafe; chy4pro/jev-for-chrome ≠ browser-use/jev-ultrafast; PsiACE/dohnuts 4★ small multimodal direct decisions; joint RLCD *theirs*; Dohnuts ≠ TypeSafe; catoenm/first-instinct 9B 63.3%→78.1% *theirs* not Harbor; 371,278 prepared ≠ consumed; RL did not reliably improve held-out; independent educational not a recovered Jev recipe; 123Satyajeet123/jev-wide naive throws away 83% *theirs*; 255 documented ~32,768 tokens real; two-decimal 95.8% floored *theirs*; IIA fails +0.31 ... +0.50 *theirs*; AltSlate-Labs/certo KL 0.008 acc 0.844 ECE 0.004 *theirs*; research preview independent not affiliated; endomorphosis/JevOps Jev is a gate not a generator; Lake remains admission; Jev never writes Lean; gbesse/question-forge held-out before winner; demo accuracy is synthetic not a Jev benchmark; flyryan/ai-news-aggregator 26★ does not execute; Akashdb5/jev-router ≠ gargpratyush/jev-router ≠ daviddl9/jev-router; kiuckhuang/laya-jev ≠ KonghaYao/laya-jev; tegersdorfer-collab/jevkit ≠ isiomaC/jevkit ≠ WaynezProg/jev-kit; buluoray/JevOnly already carded; yottayoshida/jev-intent-review already carded; skip-thin Iskandeur/system1-system2 zhlei07/open-system-one Hand-In/openjev-multimodal gwxcsny53/jev-watchtower empty SHA; serving substrate ≠ calibrated replica; game success ≠ calibrated Noul; does not execute; catalog ≠ endorsement; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60; notes.md §137
Hourly 0248 uniqueness lock: hf:knowledgator/gliclass-instruct-large-v1.0 43 likes sha 825e5478c1bf apache-2.0; Efficient zero-shot and few-shot multi-task model via sequence classification; GLiClass knowledgator Hub family class-peer catalog not Jev equivalent; Knowledgator/GLiClass.c already §123; Hub models first card as class-peer entries; GLiNER/GLiClass ports are class members not Jev replicas; hf:space:mayafree/typed-decision-leaderboard 33 likes sha f4fc44077818; typed-decision-leaderboard *theirs* not Harbor; JEV 0.7350 ZTC 27B 0.7289 ZTC 397B 0.7272 *theirs* not Harbor; 2,018 items same labels; three-way tie; tacticocc/Jevbridge 33★ MIT HEAD da443ea453ac README SHA 2178333c4c3b; Jevbridge ACP and MCP adapter; does not generate text; Any LLM as System One; wire-compat ≠ logit-equiv; tshmieldev/sharp 29★ MIT HEAD 17cbd8d9cc9e README SHA 783a5cde519c; Cut the slop; Filter your X timeline; kavehmz/typesafe-playground 11★ HEAD 733991a2924a README SHA 04c0b1f6e7da; real API calls not polished benchmarks; himomohi/aside-jev 7★ MIT HEAD e570db43b0e1 README SHA 288e7c91c307; Jev picks the next action from your defined candidates; Not a Cua binding; Jev is the model Aside is the browser runtime; nico-martin/open-jev 6★ MIT HEAD 52667199e8a5 README SHA 81c0485d5833; open reproductions of the shape; Nothing is generated; nico-martin/open-jev ≠ razorback16/openjev ≠ Zefan-Cai/Open-Jev ≠ meijustory123/openjev; hf:chaoliangUNSW/Jev-Style-Qwen3.5-2B-Decision-GGUF 82.3% ECE 0.017 *theirs*; Same decision as bf16 94.4% *theirs*; Qwen3.5-2B ≠ Archer; serving substrate ≠ calibrated replica; hf:pngwn/nanodiff-350m-typed-decisions ECE 0.065 → 0.036 *theirs*; hf:litert-community/laya-LiteRT 144/144 *theirs*; gargpratyush/journey-evals A page that says Success is never accepted as proof; mpnikhil/dev-0.4b Banking77 91.33% BoolQ 85.20% *theirs*; encoder class member not Jev replica; n4ze3m/typed-decisions-synth 7,414 cases 25,859 questions; Nobody checked it; Zaious/jev-capability-atlas already carded; LocalLLaMA/typed-decisions already carded; fengyiqicoder/jevfeed already carded; Zhao-Tian-yi/awesome-jev ≠ Gerry9000/awesome-jev ≠ heyjunpenn/awesome-jev ≠ yibie/awesome-jev; kaustav1996/reflex ≠ vuckuola619/reflex; tphakala/jev-mcp ≠ jkudish/jev-mcp; ninthspace/hunch ≠ carldaws/hunch ≠ tpellet/hunch; ruban-24/switchboard ≠ cannacre8ive/switchboard-ai; hf:openjev/openjev ≠ razorback16/openjev; catalog ≠ endorsement; skip-thin Fibonaccirabbit/Jev-VLN imanshu03/jev-browser-use luca-saggese/laya.c empty SHA; game success ≠ calibrated Noul; does not execute; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61; notes.md §138
Hourly 0348 uniqueness lock: JonathanHHenson/open-cricket MIT HEAD d75af22125ed README SHA 7d288a741089; Local structured decisions using causal language models; default Qwen/Qwen2.5-1.5B-Instruct; independent of TypeSafe; API follows Jev's general call shapes but model predictions and confidence calibration differ; wire-compat ≠ logit-equiv; Qwen2.5 ≠ Archer; replica ≠ TypeSafe; virtualman333/jev-decision-arena MIT HEAD cf6ae4ed31e8 README SHA 037f75d9610d; Greedy 0.90 vs Oracle 0.82 *theirs*; Random conf 0.00 still 20.5% *theirs*; ECE 0.180 / 0.106 / 0.205 *theirs*; confidence ≠ P(correct); game success ≠ calibrated Noul; seed 42 n=1 is not Harbor; dopeCape/typesafe-ai-test HEAD ed2adb7740d7 README SHA 183f91c36471; 8,400 calls $0.39 *theirs*; Noul 0.7 true 44% *theirs*; ≥0.9 conf 91.7% AG News *theirs*; versioned model ids rejected; *theirs* not Harbor; pCwOrM/werr 2★ MIT HEAD 2526cae98891 README SHA b29476734a09; JevBench 81.65 *theirs* not Harbor; WindTunnel 49/49 *theirs* not Harbor; 0-byte Mandelbrot is not a replica; meijustory123/OpenJev-Kit HEAD c53125982f80 README SHA a4e72c61a973; training not complete; no accuracy; Qwen3.5-0.8B ≠ Archer; meijustory123/OpenJev-Kit IS meijustory123/openjev (same GitHub id 1379187719); meijustory123/OpenJev-Kit ≠ Zefan-Cai/Open-Jev; microchipgnu/jev-hooks HEAD cbf40e64d7b2 README SHA af25fb0aaf70; Compose meaning like state; rashedInt32/jury.nvim 1★ MIT HEAD bf31e9509e7e README SHA a2b088dd0787; Code enumerates the candidates; evoke-build/evoke 1★ Apache-2.0 HEAD 310840b56f1d README SHA 02b91962cef4; Jev is the first classifier the design is bound to none; moritzkremb/jev-voice-browser densify HEAD 198a0764395a README SHA 816309fc22e6 was fa033303; context is the conversation so far; densify §82 not a sibling first sighting; luantak/is-malicious densify 18★ MIT HEAD faf6ba61d7e1 README SHA 4ae098b4b7ae; A clean report is not proof; does not sandbox; skillseedorg/ChatJEVs MIT HEAD 346e7347cf90 README SHA 6ff81d54040f; ChatJEVs ≠ erik-dunteman/ChatJev; generation from Choice is not a language model replica; chrisns/laya-mac-serve MIT HEAD f294500821b6 README SHA 00e39a7d04e2; serving substrate ≠ calibrated replica; rimusz/localjev-mlx HEAD 297836a0d95e README SHA 2d96d20e0b80; rimusz/localjev-mlx ≠ githubnext/localjev; luhayes/jev-agent-router 1★ MIT HEAD bba795a4dc4e README SHA 17a2f44993d1; does not execute; cutoff 0.8 still soft; gbesse/decision-workbench MIT HEAD 8889cf3750a3 README SHA 14a3bf79da7a; demo scores are not accuracy measurements; zhuyansen/x-reply-filter already carded; kylemclaren/jev-search ≠ kazuhideoki/jev-search; xinwang-nwpu/jev-mobile ≠ Friedjof/jev-mobile; kcd-dev/jev-skill ≠ raphael-liu/jev-skill; yanmad27/ask-jev ≠ kuhung/ask-jev; hf:s1lv3rj1nx/openjev-router-healthcare encoder class member not Jev replica; hf:akhilaaa3/openjev-v1-40705-nimble-r512-merged ≠ hf:akhilaaa3/openjev-v1-allmix-r512-merged; jevai spaces catalog ≠ endorsement; skip-thin Fibonaccirabbit/Jev-GalGame MadhavBahl/jev-guide advance-lion/dsh-jev-hooks amithgc/local-jev hiro1202/jev-review-gate-poc inlight37-design/decision-model_lab kuhung/ask-jev mmiguez314/jev-lab pomodorozhong/exp-jev vanthiet1/JevGuarAgent empty SHA; catalog ≠ endorsement; game success ≠ calibrated Noul; does not execute; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62; notes.md §139
Hourly 0445 uniqueness lock: lucasmartins-ai/lcc 7★ MIT HEAD a7e86fb60997 README SHA 877831764be9; keeps essentially every block 0.0%/−0.5% *theirs*; mechanical −70.0% Jev −52.1% *theirs*; mock Laya = Jev −22.6% on XL withdrawn; Token reduction alone is not cost reduction; N=18 pilot not Harbor; David-Lolly/Jev-Compatible 3★ HEAD e52e963d8539 README SHA 6e5ff22d40a6; Chat 1282.3 ms vs gateway 232.1 ms ~1/5.5 *theirs*; 3/3 n=3; Softmax over candidate logprobs; Qwen3.8-27B ≠ Archer; wire-compat ≠ logit-equiv; hwfengcs/any2jev 2★ Apache-2.0 HEAD 719b0eb9eefe README SHA 27e0af212cd5; independent not affiliated; acc 0.796 ECE 0.027 *theirs*; 42 ms vs JSON 778 ms *theirs*; Snake acc 0.953 ECE 0.034 *theirs*; Qwen3-0.6B ≠ Archer; /v1/systemone wire-compat ≠ logit-equiv; TianyuCodings/NanoJev densify HEAD 76fdfc9ecdca README SHA a8f8afeb7e44 was 618cea6d / 4190093c64ee; Add JevHarness project link to READMEs; densify §115 not a sibling first sighting; SHA move is not a replica; jjd-lab/jev-synthetic-survey MIT HEAD 9ca8c4ab94bb README SHA ec1664288d50; How you ask mattered more; Noul TVD 0.1530 vs GPT 0.1789 *theirs*; ECE 0.1472 *theirs* not Harbor; missed 0.05 bar; 67.28% vs 64.78% *theirs*; $4.02 vs ~$136 *theirs*; independent work; CankatSarac/jev-arcade MIT HEAD b2e45ed3c1c6 README SHA 1f06af0f4c74; snake 70/80 *theirs*; tetris 167 vs heuristic 2333 *theirs*; 74% conf <0.5 *theirs*; Calibration is not yet measured; three seeds not Harbor; game success ≠ calibrated Noul; sszxt/rlcd HEAD 66ca01664d6b README SHA 3da08d46758d; ECE 0.490→0.423 Brier 0.487→0.409 *theirs*; Yang 2023 contrastive ≠ TypeSafe RLCD; Qwen2.5 ≠ Archer; still overconfident; hf:AXERA-TECH/Laya sha 51a586cd14e2 apache; AX650 NPU 69.991/27.722/69.990 ms *theirs*; seq 256 up to 4 options; serving substrate ≠ calibrated replica; base convaiinnovations/laya; hf:openjev/openjev-MLX-4bit sha c59bf1eed7d8 cc-by-nc-4.0; ~15 GB 4-bit affine; independent not affiliated; hf:openjev/openjev-MLX-4bit ≠ razorback16/openjev; hf:GeekyAbs/laya sha b65d05b4d9eb; GeekyAbs/laya ≠ convaiinnovations/laya; hf:alfred361/laya-web sha 33f171161da5; 100% argmax *theirs*; multilingual-int8 93.8% / worst shift 16.9 pts *theirs*; 50bbx/laya-needle Apache HEAD 01961bade52f README SHA ecaff4dfd271; threshold 0.58 still soft; local Laya ≠ hosted Jev; yunhai-dev/laya2typesafeapi HEAD 4aeb89be286b README SHA d2e5d114fcd8; TypeSafe-compatible ≠ TypeSafe replica; iamdgarcia/openJev MIT HEAD 62bbc30eece2 README SHA 55614ad8caab; independent educational; not local inference; iamdgarcia/openJev ≠ alongL/openJev ≠ Zefan-Cai/Open-Jev; chrisns/homebrew-laya-mac-serve MIT HEAD 1b3c4c0bdb70 README SHA 5e58082b7e9b; tap for chrisns/laya-mac-serve §139; serving substrate ≠ calibrated replica; nk412/judgements MIT HEAD 6624e53c86cc README SHA 86fe465f7887; pydantic wrapper; threshold 0.5 still soft; JingHao-Leon/awesome-jev-apps MIT HEAD d3ef0254c4b2 README SHA fd38a3c4ff2e; catalog ≠ endorsement; JingHao-Leon/awesome-jev-apps ≠ heyjunpenn/awesome-jev; Manta-Boardgame/jev-chat HEAD 44721bae8c2e README SHA 03272e4b9a9f; unofficial; 98% confidence *theirs*; ximing/jev-snake-game HEAD 1e80283f458e README SHA 0a54b74eb095; 用 TypeSafe Jev 驱动的自动贪吃蛇; hf:dataset:syvai/danish-dynaword-laya gated HTTP 401; size_categories 10K<n<100K; devbackend/jevgo ≠ kisshan13/typesafe-ai-go ≠ peach-zhang/typesafe-go; qiudingkai-crypto/jevai and Strernd/beer-jev share README SHA e215bc4ccf13 template collision; skip-thin Adrian-lzr/jev-spire-brain Dililianxice/jev-robotic-arm-benchmark baltzparra/jev-study lzero07/jev-laya-statement qq150078158-lab/TDM-demo empty SHA; Awesomejev 691→802 (+111) / 38194→52151 stars quote watch not re-derive; tracker likes 81 lastModified UNCHANGED; Softmax over options ≠ calibrated Noul; catalog ≠ endorsement; game success ≠ calibrated Noul; does not execute; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62/#63; notes.md §140
Hourly 0551 uniqueness lock: jaredpalmer/kev densify HEAD 4f8110a3f862 README SHA d497d4b89427 was e0bcf50153f1 / 84b872488915; Night-2 sign-off; dates+unknowable deltas promoted for 0.8B/4B/9B; v7-base tags; PLAN SHA 5e6d2fca508e; locked OOD 0.684/0.837/0.852 *theirs*; test Kev-9B 0.837→0.852 *theirs*; Kev-4B 0.832→0.837 *theirs*; Kev-0.8B 0.668→0.684 *theirs*; T≈2.0 Brier 0.291→0.267 ECE 0.105→0.039 *theirs*; 7.5%→3.2% *theirs*; grouped T rejected; date_facts deadline 9B 0.72→0.80 raw→0.90 preprocessor; unknowable ≥0.9 → 0.00; 35B Not shipped MMLU-Pro 0.550 *theirs*; coverage@5% 0.62 from 0.66 at 9B *theirs*; not a controlled architecture comparison; Qwen3.5 ≠ Archer; Qwen3.6 ≠ Archer; temperature scaling ≠ ECE unless measured; Hub --revision is a pin not a replica; densify §45 not a sibling first sighting; SHA move is not a replica; bespokelabsai/nimble densify HEAD f136b3f75721 README SHA b3a04a310f1e; Publish original 2676 training examples and frozen 324 holdout; 90.1% vs Jev 93.2% vs base 66.4% *theirs*; did not distill from Jev; densify §35 not a sibling first sighting; AbdelStark/awesome-typesafe-jev 416★ MIT HEAD a6a68b57888a README SHA e47993484e3a github_id 1374058281; Independent community project; catalog ≠ endorsement; AbdelStark/awesome-typesafe-jev IS AbdelStark/awesome-typesafe (same GitHub id 1374058281); cookiespiggy/agentic-rl 103★ MIT HEAD 072bdd8c69de README SHA f2cc68b4e214; ch.25 Jev vs RL; RL ≠ calibrated Noul; DevMortimer/pi-typesafe 27★ MIT HEAD 8dcaa887e22c README SHA 6a11fb9df8b9; DevMortimer/pi-typesafe ≠ twilwa/pi-typesafe ≠ TheoOliveira/pi-jev; hf:gump2049/APUS-OpenJev-v1 sha e7e3cc0b9c82; APUS-OpenJev 9B 85.0% vs Jev API 82.5% *theirs* not Harbor; Frozen80 n=80; Candidate probabilities are not calibrated confidence; Qwen3.5-4B ≠ Archer; Qwen3.5-9B ≠ Archer; hf:SeanLiu/Jev-Vision sha 9b77fa5fdcd0 apache-2.0; POPE 0.907 MME 0.927 NLVR2 0.930 *theirs*; yes/no ECE 0.034 to 0.047 *theirs*; JevBench hard 52% at 91% mean confidence *theirs*; Qwen3-VL-8B ≠ Archer; LoRA ≠ RLCD replica; wire-compat ≠ logit-equiv; hf:SeanLiu/Jev-Vision ≠ sseanliu/Jev-Vision; evoke-build/evoke densify 6★ HEAD ca8a311743fe README SHA fcce876e2cab was 310840b56f1d / 02b91962cef4; Jev is the first adapter the design is bound to no engine; densify §139 not a sibling first sighting; 47thtechcorner/RayCodes_GLiNER_V1_Multi densify HEAD 485cf8045f73 README SHA 035b339c3789; Zero Hallucinations marketing; Locate ≠ decide; kylemclaren/jevsearch ≠ kylemclaren/jev-search ≠ kazuhideoki/jev-search; stacklok/typesafe-go ≠ kisshan13/typesafe-ai-go ≠ peach-zhang/typesafe-go ≠ Nibir1/typesafe-go; sontakey/awesome-jev ≠ heyjunpenn/awesome-jev ≠ yibie/awesome-jev ≠ AbdelStark/awesome-typesafe-jev; Giustino98/system-one-bench ≠ mallahyari/system-one-benchmark; skip-thin eatmoreduck/jev-jarvis githubMJ/Laya4j hawkymisc/typed-decision-bert jayanthbagare/laya_examples mohamedAtoui/Jev-project petrixh/laya-test sidhasadhak/jev-perfume-advisor wendaoheri/jev-browser zohaibtanwir/jev-samsho2 empty SHA; game success ≠ calibrated Noul; does not execute; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62/#63/#64; notes.md §141
Hourly 0707 uniqueness lock: Sac-Y/Jev-cu 524★ HEAD e2cc92d731fa README SHA 3deeafbc870f; 只传文字，不传截图; Text only no screenshots; Codex CU executes; local policy gates; kyotofin/tax-doc-classifier 322★ Apache-2.0 HEAD 3e95a77f763c README SHA 72c4f74b542e; 100% of our tax document corpus at $0.001 per page; TaxCalcBench 0 strict errors *theirs*; blank IRS 38 strict errors 5.05% *theirs*; 34× cheaper and 6× faster *theirs*; 261 IRS forms; 100% of corpus *theirs* not Harbor; fhshaik/typesafe-mario 319★ HEAD ca22449ed187 README SHA c489f9350414; The model does not receive screenshots; game success ≠ calibrated Noul; droidrun/mobile-jev 307★ MIT HEAD 395fc222beac README SHA d257fed2c5f7; 21 seconds for 9 actions *theirs*; A completed booking is not demonstrated; droidrun/mobile-jev ≠ Friedjof/jev-mobile; realZachi/pg-jev 269★ HEAD afd11fa856d7 README SHA e8735928b57d; giuliosmall/pg_typesafe ≠ realZachi/pg-jev; kitze/skillbox 220★ MIT HEAD cda64ad3310a README SHA dedcb6be3c39; itsmostafa/typesafe-mcp 181★ MIT HEAD d4c110c7edd8 README SHA 2bd68aff4299; itsmostafa/typesafe-mcp ≠ cyrusasco/typesafe-mcp ≠ burnigtm/jev-mcp; kitze/unclutter 157★ MIT HEAD 9ef9beccc1e5 README SHA 5ad63c67fd02; standardagents/jevpilot 147★ HEAD e1beeb13b9a9 README SHA ec386a81e12c; AbdelStark/awesome-typesafe-jev densify 417★ MIT HEAD d6ea2a0d6cf4 README SHA 234ae59a0b16 was a6a68b57888a / e47993484e3a; The field guide to typed decisions; Independent community project; densify §141 not a sibling first sighting; SHA move is not a replica; hf:Praveenrajus/jev-bench HTTP 401 was 200; densify §107/§125 remainder; *theirs* not Harbor; hf:wayfind/metask-jev-4b-policy-mix densify sha 5ecdd272ab4a README SHA c534ee82b141; densify §134 not a sibling first sighting; wayfind/metask-jev-4b-policy-mix ≠ metask-ai/metask-jev; patryckalves/jev-no-enem HEAD 7f85f787e3d1 README SHA 237b308df062; ENEM 2025 *theirs* not Harbor; 56.6% (103/182) *theirs*; ECE 0.078 *theirs*; Ying-Kai-Liao/jev-browser ≠ wy-coliney/jev-browser-use; w3cj/jev-chat ≠ Manta-Boardgame/jev-chat; snellingio/system-one ≠ sgoedecke/system-one ≠ Luke458/system-one ≠ developerekene/System-One; stoleas/typesafe-computer-use ≠ awlevin/typesafe-computer-use; holotwist/laya ≠ NandhaKishorM/laya; RafalWilinski/vibecheck ≠ psyb0t/vibecheck; dannote/jev ≠ okooo5km/jev ≠ sebastianbugal/jev; skip-thin developerekene/System-One holotwist/laya wuzhiping/jev-laya empty SHA; hf:s1lv3rj1nx/openjev-healthcare-router HTTP 401 *theirs*; hf:s1lv3rj1nx/openjev-heldout HTTP 401 *theirs*; hf:s1lv3rj1nx/openjev-mixture HTTP 401 *theirs*; catalog ≠ endorsement; game success ≠ calibrated Noul; does not execute; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62/#63/#64/#65; notes.md §142

**Hourly 0823 HIGH (`notes.md` §143).** dohnuts densify MODEL_CARD. JevBench 65.80% vs Jev 86.58% / Laya multi 47.62% *theirs*. same-species serving not an 18th scoring row. FluidUse field→value match among supplied options not free text. Screenshots aren't uploaded. Jev is the only model. not fully offline. JSON 0.909 letters 0.907 *theirs*. 13 600 / 13 600 *theirs*. softmax over letters ≠ calibrated Noul. model=jev-auto. AG News 0.910 *theirs*. Banking77 0.870 *theirs*. DAIR Emotion 0.480 *theirs*. Fastest and cheapest web agent *theirs*. densify §137 not a sibling first sighting. densify §142 not a sibling first sighting. densify description rewrite. Cua-S1 ≠ TypeSafe. catalog ≠ endorsement. *theirs* not Harbor. SHA move is not a replica. Do not reopen or amend PR #23–#66. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 0823 uniqueness lock: PsiACE/dohnuts densify 11★ Apache-2.0 HEAD 253766e5fcb7 README SHA 4b5b019deba9 was a5049834489c / e1b448c440b5; MODEL_CARD + training dataset refs; JevBench 65.80% vs Jev 86.58% / Laya multi 47.62% *theirs*; 152 / 231 *theirs*; 78.21% macro accuracy *theirs*; 180,031 decisions *theirs*; Qwen3.5-0.8B; Joint RLCD *theirs*; Dohnuts ≠ TypeSafe; densify §137 not a sibling first sighting; same-species serving not an 18th scoring row; SHA move is not a replica; FluidInference/FluidUse 3★ Apache-2.0 Swift HEAD c18071d791eb README SHA f1cba4a244bb; on-device Mac form CU; Accessibility API; CUA-S1-FORMS CoreML ~706K params ~1ms Neural Engine; field→value match among supplied options not free text; Cua-S1 ≠ TypeSafe; FluidInference/FluidUse ≠ FluidInference/laya-coreml ≠ AndyInQtr/laya-coreai ≠ mizorewww/laya-coreml; serving substrate ≠ calibrated replica; shhivv/third-hand 274★ MIT Swift HEAD 430394b35dbb README SHA b615d7c3fd19; Screenshots aren't uploaded; Jev is the only model; not fully offline; typesafe-ai/system-one-adapter-python 226★ MIT HEAD adffc2eab300 README SHA d01afbf0499e; Drop-in TypeSafeClient replacement backed by LLM APIs; wire-compat ≠ logit-equiv; typesafe-ai/typesafe-sdk-js 203★ MIT HEAD 66880ccded6c README SHA 7e834076c14e; typesafe-ai/typesafe-sdk-python 175★ MIT HEAD 2ce5c65f1364 README SHA 361a3bc13e19; catalog ≠ endorsement; r-ms/mini-jev 40★ MIT HEAD ca612198bfb6 README SHA 565b70c4cf4d; read the option letter's logits instead of generating JSON; yuki-oshio/mini-jev ≠ r-ms/mini-jev; JSON 0.909 letters 0.907 *theirs*; 13 600 / 13 600 *theirs*; softmax over letters ≠ calibrated Noul; Das-rebel/a3m-router 16★ MIT HEAD 62caefe59315 README SHA c19e802d5cf2; model=jev-auto; routing ≠ permission; AbdelStark/jev-benchmarks 13★ Apache-2.0 HEAD 0d610cc53e79 README SHA 5fd3627f7de4; AG News 0.910 *theirs*; Banking77 0.870 *theirs*; DAIR Emotion 0.480 *theirs*; *theirs* not Harbor; browser-use/jev-ultrafast densify 14622★ MIT HEAD 1231850a0bf1 README SHA fa7d079f9192; Fastest and cheapest web agent *theirs*; densify description rewrite; pythongiant/laya-drift densify 4★ HEAD 334953e5cb8f README SHA 6662121ba0f3 was fc94b71cf7dd / 55ef2343ee5d; opencode plugin to calculate agentic drift over time *theirs*; densify §142 not a sibling first sighting; BlinkWrite/pii-masker densify 1★ MIT HEAD 6ad202ab4443 README SHA 27931758af6c; On-device reversible PII masking *theirs*; Locate ≠ decide; TypeSafeAI/typesafe-playground ≠ kavehmz/typesafe-playground ≠ nickthompson480/typesafe-ai-playground; siliconkernel/vllm-jev-decison 8★ MIT HEAD a9362d52b9a8; No generative fallback; Stumble/jev-go 3★ MIT HEAD a475dc925ba6; Twister915/typesafe-ai 11★ Apache-2.0 Rust HEAD d4455efb1d06; rorshopping/jev-on-a-laptop 23★ HEAD 5821d9106103; Unofficial research repo. Not affiliated with TypeSafe AI; Qwen2.5 ≠ Archer; skip-thin GokhanCalkap/LayaCode fredzhaozonghui/LAYA1 empty SHA; Abhi895/Laya ≠ convaiinnovations/laya; mjdileep/OpenJev ≠ Zefan-Cai/Open-Jev; Abhi001vj/system-one-open ≠ mithalouni/system-one-open ≠ sgoedecke/system-one; ZulfiFazhar/system-one ≠ sgoedecke/system-one; Futureppo/typesafe_register key-farming skip; soft scores ≠ hard gates; catalog ≠ endorsement; game success ≠ calibrated Noul; does not execute; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62/#63/#64/#65/#66; notes.md §143

**Hourly 0923 HIGH (`notes.md` §144).** intellyweave GLiNER OSINT. Locate ≠ decide. openvons finite choices + none. 4B frozen+head 0.916 vs 27B zs 0.875 *theirs*. 8 questions 22.6 ms *theirs*. softmax ≠ calibrated Noul. AgentBeam local security layer. soft scores ≠ hard gates. unofficial not affiliated. wire-compat ≠ logit-equiv. chips virtual. game success ≠ calibrated Noul. densify §121 not a sibling first sighting. densify §139 not a sibling first sighting. densify §141 not a sibling first sighting. Runs every rule against every line in parallel. No skimming. Median 275 ms. trolley 0.99 vs 0.78. 11/11/7 match/differ/undecided of 29 *theirs*. retired name reservation is not a replica. catalog ≠ endorsement. *theirs* not Harbor. SHA move is not a replica. Do not reopen or amend PR #23–#67. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 0923 uniqueness lock: vericle/intellyweave 76★ BSD-3-Clause Py HEAD ff4152ce9d20 README SHA 3afa702012e8; GLiNER OSINT; Locate ≠ decide; genai-craft/openvons 13★ NOASSERTION Py HEAD c2683c4539a7 README SHA 85164d409725; finite choices + none; 4B frozen+head 0.916 vs 27B zs 0.875 *theirs*; 8 questions 22.6 ms *theirs*; softmax ≠ calibrated Noul; whyashthakker/beam-cli 11★ AGPL-3.0 TS HEAD 5162ec66179a README SHA d55847ca5681; AgentBeam local security layer; soft scores ≠ hard gates; atharvamhaske/typesafe-sdk-go 8★ MIT Go HEAD 6ea04182d356 README SHA 8d90abda1f58; unofficial not affiliated; wire-compat ≠ logit-equiv; atharvamhaske/typesafe-sdk-go ≠ kisshan13/typesafe-ai-go ≠ stacklok/typesafe-go ≠ Nibir1/typesafe-go ≠ peach-zhang/typesafe-go ≠ draganm/go-jev ≠ kataras/jev ≠ robertjndw/gosys1 ≠ Stumble/jev-go; Prophetlab/JevPokerBench 7★ MIT Py HEAD 9c9816688a3c README SHA 0fcd6807b9c3; chips virtual; game success ≠ calibrated Noul; *theirs* not Harbor; tyler-dot-earth/patdown densify 11★ NOASSERTION TS HEAD 8b2b2b591470 README SHA 1052b6da2c25 was ae0e277fdd64 / 275f4b9c; Block/steer/fuzzy lint; judge swappable; default TypeSafe/Jev; provider-neutral; densify §121 not a sibling first sighting; evoke-build/evoke densify 8★ Apache-2.0 Rust HEAD 50c9637ef11f README SHA 72ec0e65c432 was ca8a311743fe / fcce876e2cab; Jev is the first adapter; the design is bound to no engine; densify §139 not a sibling first sighting; lukstei/slop-grader 5★ MIT TS HEAD b60332684ff8 README SHA bbc1604754d3; Runs every rule against every line in parallel. No skimming; sumleo/prompt2jev densify 2★ MIT Py HEAD f3b6bc763b74 README SHA 3d58e8c10075 was bd9cd8a471a6 / afc36885861e; heuristic conversion ≠ calibrated Noul; densify §141 not a sibling first sighting; Andymulb/jev_the_philosopher 0★ MIT TeX HEAD 334e3f9b83e5 README SHA 8db05448b75f; Median 275 ms; trolley 0.99 vs 0.78; 11/11/7 match/differ/undecided of 29 *theirs*; PerryLink/layacore 0★ Apache HEAD 12afe3af5edc README SHA f78b73d21cf7; retired name reservation; the project is now PerryLink/laya-mcp; retired name reservation is not a replica; PerryLink/layacore-mcp HEAD b006cc7c3f87 README SHA 1177f286f3f8; PerryLink/laya-mcp-npm launcher not implementation HEAD 426e965b4c48 README SHA 98ed0d448b09; PerryLink/laya-mcp ≠ wsargent/laya-mcp; DreamBlooms/dohnuts.cpp ≠ PsiACE/dohnuts; ClemensSchartmueller/jev-guard ≠ leepokai/jev-guard ≠ seb4ez/jevguard; AABBAASS1/jev-router ≠ gargpratyush/jev-router ≠ Akashdb5/jev-router ≠ daviddl9/jev-router; wustep/jev-playground ≠ AbnormalPilot/jev-playground ≠ mizchi/jev-playground; Li-Evan/awesome-jev ≠ Omrigotlieb/awesome-jev ≠ youzizzz1028/Awesome-Jev ≠ heyjunpenn/awesome-jev ≠ yibie/awesome-jev; sunchojack/jev-cli ≠ gnapse/jev-cli; Alistair77/openjev ≠ Zefan-Cai/Open-Jev ≠ razorback16/openjev; jev-jarvis/jev-jarvis ≠ eatmoreduck/jev-jarvis; Renwang-Huang/typesafe-mcp ≠ itsmostafa/typesafe-mcp; inematds/laya ≠ convaiinnovations/laya ≠ NandhaKishorM/laya; kataras/jev ≠ okooo5km/jev ≠ sebastianbugal/jev ≠ dannote/jev; ai-ecoverse/kev.js ≠ jaredpalmer/kev; skip-thin gnapse/jev-cli HTTP 404 fr4j4/system-one-arena nothingmn/Jev.Sdk youniszhang/jev-local Vaibhaav-Tiwari/fly-doom-jev fengliner/jev-tank-battle ngouard5/jeveuxaider-design empty SHA; hf:Skylarcc/Laya-Online HTTP 401 *theirs*; hf:piratehack009/laya-cn-flash-triage HTTP 404 *theirs*; catalog ≠ endorsement; game success ≠ calibrated Noul; does not execute; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62/#63/#64/#65/#66/#67; notes.md §144

**Hourly 1019 HIGH (`notes.md` §145).** praneeth16 GEPA ADE Corpus V2. schema-valid is not the same as correct. API confidence is not P(correct). GEPA revises Choice instructions/criteria with weights fixed. jev-1.13.0 weights fixed. Brier 0.1357→0.0747 *theirs*. F1 69.1%→79.7% *theirs*. FN 4→6. review-queue policy is not F1. Soft is not gate. Not an 18th scoring-table species. Every claim is labeled and sourced. catalog ≠ endorsement. 发送永远手动. About 180 ms. routing ≠ permission. $0.00241 *theirs*. Not a screenshot agent. game success ≠ calibrated Noul. pi-follow-through threshold 0.8 still soft. wire-compat ≠ logit-equiv. densify §144 not a sibling first sighting. pi-jev-context densify §134 not a sibling first sighting. *theirs* not Harbor. SHA move is not a replica. Do not reopen or amend PR #23–#69. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1019 uniqueness lock: praneeth16/adapting-jev-with-gepa ADE Corpus V2 GEPA; schema-valid is not the same as correct; API confidence is not P(correct); GEPA revises Choice instructions/criteria with weights fixed; jev-1.13.0 weights fixed; Brier 0.1357→0.0747 *theirs*; F1 69.1%→79.7% *theirs*; FN 4→6; review-queue policy is not F1; Soft is not gate; Not an 18th scoring-table species; aliaihub/awesome-jev-usecases 15★ NOASSERTION HEAD 6cbde6bd3569 README SHA 7ea135c6345d; Every claim is labeled and sourced; catalog ≠ endorsement; aliaihub/awesome-jev-usecases ≠ anandi1989/awesome-jev-usecases ≠ whyashthakker/awesome-jev-use-cases; rezoch340/jev-chat-JARVIS-windows 6★ MIT Py HEAD 26b686301437 README SHA 0714736b68c3; 发送永远手动; rezoch340/jev-chat-JARVIS-windows ≠ Finderchangchang/jev-chat-JARVIS; iamvatsalpatel/tiershift 3★ MIT TS HEAD 16a0826b9f62 README SHA 46fcb1cb191b; About 180 ms; routing ≠ permission; Bring-AI/jev-rl 2★ MIT Py HEAD 36f89cec85a2 README SHA 6283da6011b7; $0.00241 *theirs*; daniel4x/JevEmon 2★ GPL-3.0 HEAD 572454c69bf7 README SHA 8fc00d12848d; Not a screenshot agent; game success ≠ calibrated Noul; spoonnotfound/soupbase 2★ MIT TS HEAD 3e874e83e710 README SHA 3106bc96d6ab; Nabsku/pi-follow-through 1★ MIT TS HEAD c62ef28ff4ac README SHA 64000451b79e; pi-follow-through threshold 0.8 still soft; dashbi1/jev-sim 1★ MIT Py HEAD 753c7397d73c README SHA 05fd960799d2; wire-compat ≠ logit-equiv; jev-jarvis/jev-jarvis densify 8★ MIT Py HEAD a94e3b967ef5 README SHA e441335b1df0 was be68dd7993f0 / efe7e47a6fe8; densify §144 not a sibling first sighting; Nyarlathoteppppp/pi-jev-context densify 5★ MIT TS HEAD 96371e2bf144 README SHA d4276222a436 was f0128a86478f; pi-jev-context densify §134 not a sibling first sighting; Nyarlathoteppppp/pi-jev-context ≠ kevinpita/pi-jev-context; fly88oj/jebii 0★ MIT JS HEAD 5cbe527ed791 README SHA b4a76b8aba9d; generallymatthew/factlabel 0★ Apache-2.0 Py HEAD b3d3bceee044 README SHA b1cda6c4646e; aakgna/jevcal ≠ abhixhek/jevcal; 007M7/jev-chat ≠ w3cj/jev-chat ≠ Manta-Boardgame/jev-chat; fstandhartinger/jev-router ≠ gargpratyush/jev-router; prakash7474/Jev_guard ≠ leepokai/jev-guard; rdutra/laya-mcp ≠ PerryLink/laya-mcp ≠ wsargent/laya-mcp; Kourin1996/jev-playground ≠ wustep/jev-playground; ai-ecoverse/cua-s1.js Cua-S1 ≠ TypeSafe; skip-thin Unnati-23/jev-typesafe-guide antoniofaical/digital-twin-classifier-jev leonezhu/agent-kits empty README; skip-thin wjw66/deepseek-harness-jev-pre-compaction ziwon/jev-actor empty SHA HTTP 409; hf:chanoian/openjev-mlx-demo HTTP 401 *theirs*; hf:clduab11/jev-calibration-statistics HTTP 401 *theirs*; hf:yasserrmd/laya-lab HTTP 401 *theirs*; catalog ≠ endorsement; game success ≠ calibrated Noul; does not execute; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62/#63/#64/#65/#66/#67/#68/#69; notes.md §145

**Hourly 1110 HIGH (`notes.md` §146).** hf:thaitea/laya-vision SmolVLM typed vision decisions. same-species serving not an 18th scoring row. A-OKVQA 63.1% ECE 0.266 to 0.094 *theirs*. act head untrained do not gate on it. codearia-sieve page to typed fields. 11 of 11 *theirs* not Harbor. gemma-jev JSON chat ≠ calibrated Noul. local-decision-model independent from the public post. musubi-jev README is a kev tree copy. copied kev numbers are not a musubi bench. vllm2jev wire-compat ≠ logit-equiv. pg-laya serving substrate ≠ calibrated replica. jev-rerank ranking ≠ calibration. typesafe-mcp decision is code. act_above 0.8 still soft. densify §142 not a sibling first sighting. densify §145 not a sibling first sighting. densify §143 not a sibling first sighting. densify §139 not a sibling first sighting. catalog ≠ endorsement. *theirs* not Harbor. SHA move is not a replica. Do not reopen or amend PR #23-#70. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1110 uniqueness lock: hf:thaitea/laya-vision 13 likes sha a2653db2831b cc-by-nc-sa-4.0; SmolVLM-256M vision typed choice/score/noul; same-species serving not an 18th scoring row; independent not affiliated; A-OKVQA 63.1% ECE 0.266 to 0.094 *theirs*; ScienceQA 89.0% ECE 0.080 to 0.034 *theirs*; VQAv2 noul 73.2% ECE 0.085 to 0.042 *theirs*; All n=8235 75.9% ECE 0.035 *theirs* not Harbor; VQAv2 re-split not comparable to published VQAv2; about 71 ms *theirs*; option order varies 1.2 points *theirs*; act head untrained do not gate on it; not a drop-in replacement for Laya text checkpoint; usage loads thaitea/laya-vision-smolvlm-256m already §87; hf:thaitea/laya-vision ≠ thaitea/laya-vision-smolvlm-256m card id; AntonG87/codearia-sieve 1★ MIT TS HEAD 64ecd4151726 README SHA b03a3d29ab22; page to typed fields; 6 of 6 *theirs*; 11 of 11 *theirs* not Harbor; robots-disallowed did not fetch; no model required for the parse; 7Zenox/gemma-jev 0★ NOASSERTION Py HEAD 2eed119e03ff README SHA c3b58d6a15a9; generation-free letter slots; 144 authored decisions *theirs*; Gemma 3 270M 0.293 below chance 0.333 *theirs*; Gemma 4 E2B-it JSON chat 0.807 *theirs*; Qwen3.5-4B JSON chat 0.813 *theirs*; JSON chat ≠ calibrated Noul; softmax over letter slots ≠ calibrated Noul; bf16 vs fp32 argmax-agreement check not run; Gemma ≠ Archer; Qwen3.5 ≠ Archer; Pdbz199/local-decision-model 0★ MIT Py HEAD ddceb5829849 README SHA 80659ec966f5; independent project built only from the public post; one pass no generation; schema-valid is not the same as correct; musubi-labs/musubi-jev 0★ Apache-2.0 HEAD e943f21e4057 README SHA 8ffd43564204; README is a kev tree copy; copied kev numbers are not a musubi bench; musubi-labs/musubi-jev ≠ jaredpalmer/kev; quaeast/vllm2jev 0★ NOASSERTION Py HEAD 8a51f94961ea README SHA be92356f1176; does not reproduce Jev calibration; wire-compat ≠ logit-equiv; IAmJSD/pg-laya 0★ Apache-2.0 Rust HEAD 1bc66a4d6a7f README SHA 03476be41744; SQL choice score noul; serving substrate ≠ calibrated replica; IAmJSD/pg-laya ≠ realZachi/pg-jev ≠ giuliosmall/pg_typesafe; gbesse/jev-rerank-server 0★ MIT JS HEAD b28cef5e34a6 README SHA 91167c66c29c; SciFact n=25 nDCG@10 0.616377 to 0.718260 *theirs*; Recall@10 0.84 unchanged *theirs*; ranking ≠ calibration; MarkChu-git/typesafe-mcp 0★ MIT HEAD a064b14207c0 README SHA ae27210cc5af; decision act/review/abstain is code; act_above 0.8 still soft; MarkChu-git/typesafe-mcp ≠ itsmostafa/typesafe-mcp ≠ cyrusasco/typesafe-mcp ≠ Renwang-Huang/typesafe-mcp; pythongiant/laya-drift densify 4★ TS HEAD d33db6736ed8 README SHA 7af1781c28c5 was 334953e5cb8f / 6662121ba0f3; monitor agent drift; densify §142 not a sibling first sighting; Adkid-Zephyr/chinese-workflow-decision-bench densify 1★ MIT Py HEAD b694dc6dbcba README SHA 9ef2b7d76a37 was 6d0a7c2af303 / 4ed71a36cd51; 64/64 and 63/64 *theirs* not Harbor; synthetic not a group-chat dump; densify §145 not a sibling first sighting; turenlabs/jast densify 1★ MIT Rust HEAD c6588285208f README SHA d9214ca31f92 unchanged; star 0 to 1 is star-noise; densify §145 not a sibling first sighting; JabbaKadabra/SystemOneDotNet densify MIT C# HEAD 5120ffb84cc5 README SHA 0809f98d4c93 was 5bff3394281c / 76a9188c180a; unofficial .NET client; wire-compat ≠ logit-equiv; densify §143 not a sibling first sighting; arnavm-codes/JevFence densify HEAD 7e277474ff5e README SHA 2bbb684757de was 6fe62ca7b10c / 5441aaeaace0; soft scores ≠ hard gates; densify §145 not a sibling first sighting; cloudbtl/JevRAG 0★ Apache-2.0 Py HEAD 307ab19ee9cf README SHA 9b814bb6624b; first card revisit tag no prior notes card; cloudbtl/JevRAG ≠ emretheus/jev-rag-benchmark ≠ erendikmenn/jev-rag-benchmark; gbesse/decision-workbench densify MIT JS HEAD 877d1a9add5b README SHA 24cce8900d67 was 8889cf3750a3 / 14a3bf79da7a; human review separate from model output; demo scores are not accuracy measurements; densify §139 not a sibling first sighting; 0xagentlabs/jev-xiangqi ≠ Zafer-Liu/jev-xiangqi; RyanNg1403/jev-cli ≠ gnapse/jev-cli ≠ sunchojack/jev-cli; KennethAshley/awesome-jev ≠ heyjunpenn/awesome-jev ≠ yibie/awesome-jev; malevrigns/agent-jev ≠ hf:aimeigaoshou/agent-jev; 79.25% 1585/2000 ECE 0.1687 *theirs* not Harbor; kidzik/jiffy probabilities are uncalibrated; s3rli/jevips name collision not a decision model; skip-thin Alpha-Harper-Franklin/astra-jev jonas050210/Laya_Playground pietrushka/jev-youtube-filter empty SHA HTTP 409; skip-thin THANK-YOU-FOR-YOUR-ORDER-ASDF123/repo-laya4qxd Ylr9933/JevForAgent empty README; hf:marcmagn1/jev-alt-systemone-eval dataset sha 95f679e8455b README 404 models HTTP 401 *theirs*; catalog ≠ endorsement; game success ≠ calibrated Noul; does not execute; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62/#63/#64/#65/#66/#67/#68/#69/#70; notes.md §146

User-provided glance uniqueness lock: yoheinakajima/glance Apache-2.0 Py HEAD 8f36e063bffb README SHA b57280394bc1 LICENSE SHA d645695673349e; 3★; size 51490; pushed 2026-09-21T17:37:40Z; created 2026-09-21T06:51:38Z; PyPI glance-vlm 0.3.1; tag v0.3.1; site https://glance.yohei.me; topics calibration, image-classification, vision-language-model, vlm, zero-shot; Ask an open vision-language model typed questions about an image and get probabilities back, on your own machine; frozen open VLM default Qwen3-VL-4B Apache-2.0; answer-token logit readout in one forward pass; Glance is a calibration and measurement harness around that readout. It is not a model; trains no weights; images never leave the machine; local server binds 127.0.0.1; noul yes/no choice pick-one score ordered rating; POST /v1/decide; glance fit --unlabeled; yes/no 0.939 pick-one 0.933 rating exact 0.669 *theirs*; Gemini 3.1 Flash-Lite yes/no 0.961 pick-one 0.933 rating 0.763 *theirs*; unlabeled image-quality 0.67 to 0.76 exact *theirs*; about 32 labeled images 0.86 exact ECE about 0.03 *theirs*; non-image-quality rubrics 0.55 exact with 300 labels *theirs*; tilt 0.33 *theirs*; geometric probes diagonals 0.30 largest of four shapes 0.52 eight objects 0.56 *theirs*; stripe direction hidden-state linear probe 0.99 *theirs*; raw yes/no ECE 0.111 and 0.179 overconfident *theirs*; explicit other held-out breeds 7.7% *theirs*; claims ledger: faster or cheaper than Jev do not claim; shares inference object with featherless-ai/simple-jev hr98w/jev-visual zhengxuyu/litjev; request and response shapes follow TypeSafe Jev hosted text; yoheinakajima/glance ≠ TypeSafe Jev; POST /v1/decide ≠ TypeSafe /v1/systemone ≠ IamBusy/OpenJev /v1/decide; trains no weights unlike YOFO and unlike hf:thaitea/laya-vision §146 and unlike Zefan-Cai/Open-Jev; harness not weights; soft probs for threshold abstain rank; soft scores ≠ hard gates; logits are not calibrated probabilities of correctness; *theirs* not Harbor; catalog ≠ endorsement; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62/#63/#64/#65/#66/#67/#68/#69/#70/#71/#72; notes.md §147
