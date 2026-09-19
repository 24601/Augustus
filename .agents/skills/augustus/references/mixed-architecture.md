# Mixed architecture: judgment-class model + generator + code

This card is the default *placement* for the judgment-model class, not a
product catalog and not an API guide. TypeSafe Jev is the documented
exemplar; families (open heads, GLiNER/GLiClass species, listwise rankers,
vision scorers) live on `judgment-class.md`. Integration contracts for
Jev live in the official `typesafe-ai` skill and the live docs
(`https://docs.typesafe.ai/llms.txt`). Re-read those before writing a
Jev request body. Other families own their own cards/READMEs.

Central claim: **a judgment-class model is not a cheaper LLM and not a
new kind of classification.** It is a software primitive for *narrow,
typed, (when trained for it) calibrated judgments* that code can
threshold. Generation, exact computation, and authorization stay where
they already belong. Pick the family from the hole; do not start from a
vendor.

Status words follow `mappings.md`: **Contract** (docs), **Empirical recipe**
(dated artifact), **Hypothesis** (discourse or unmeasured).

## Neighbor skills (load the right one)

| Skill | Owns | Not for |
|---|---|---|
| `typesafe-ai` | Live API/SDK contracts, primitives, cookbooks | Classical-method mapping |
| `tenbin` | Design-time question lint, eval, threshold files | Where judgment *belongs* |
| `decision-first` | Try-a-typed-decision-before-a-regex habit + lab log | Method substitution / falsification |
| **Augustus** | Placement, *family* choice, method mapping, what would prove the design wrong | Curl snippets, field names, SDK versions |

If the request is "how do I call Jev?", stop and load `typesafe-ai`. If it
is "should this step be a judgment-class model, an LLM, a regex, or a
trained classifier — and which family?", stay here. Family table:
`judgment-class.md`. Cross-domain frames: `mental-models.md`. Proof vs
judgment: `formal-methods.md`. [wellposed](https://github.com/suraj-phanindra/wellposed)
is an Empirical *recipe* of tenbin's lint hole (missing `other` →
confidence 1.00 wrong); it is not a second Augustus skill
(`notes.md` §46).

## Default architecture

```text
evidence (filtered, structured, current)
    → exact work in code
    → judgment-class model: bounded semantic judgments (typed answers + distributions, or affinities/ranks — see family)
    → explicit policy in code (thresholds, weights, abstain, permit)
    → LLM only where text must be written or candidates invented
    → checked action (code validates operation+target)
    → observed outcome (probe, not a self-report)
```

Three layers, one owner each:

- **Code** — control flow, arithmetic, dates, auth, side effects, candidate
  generation (regex, index, UI tree, git hunks, SQL).
- **Judgment-class model** — one-second judgments over a closed answer
  space given that state: route, gate, score, select, verify. Default
  exemplar is Jev; family from `judgment-class.md`.
- **LLM** — writing, explanation, code generation, open synthesis. The
  judgment model may sit *before* (prefilter/route), *after*
  (verify/cite), or *around* (both). It does not sit *instead*.

**Stack replacement is the rejected design.** Discourse on 2026-09-18
converged here without us asking: "too early to treat as a stack
replacement; mixed architecture: a decision model for classification, an
LLM for writing" ([@seb_jsilva](https://x.com/i/status/2100957104567685310));
"replace classification *steps*" not the agent
([@sydneyrunkle](https://x.com/i/status/2100956747729080714));
"route certain decisions beforehand, afterward, or altogether"
([@kurtbuhler](https://x.com/i/status/2100956205065597266)). Same shape as
the official patterns: fan-out, confidence-routing, intent-routing, LLM
guardrails, classifying RAG passages — see live docs, not this card, for
request shape.

Extreme form that still obeys the split: a loop with **no LLM at all** when
nothing needs writing. `yousudip/lizard-agent` (**Hypothesis** as a product,
**Empirical** as a decomposition): perception builds a closed action space
from the page; Jev picks among visible elements; code enforces prices/dates;
answers are *located*, never composed. The day the task needs a paragraph,
an LLM re-enters — that is mixed architecture, not a different religion.

**Component node, not internals-as-FSM.** Place the judgment model as a
node in *your* state machine; do not describe its internals as one.
Atlas teaching (`notes.md` §49): paraphrase_support and
reversed_meaning_high_overlap are distributed LM understanding, not
keyword rules. Code still owns transitions (`mappings.md` §3).

**Browser-use strength is DOM-as-text + speculative fan-out, not
vision.** Translate a screenshot task into a structured DOM snapshot
as `state`; fan out over candidate elements in one call. Text-only
models then sit in their strong zone (extractable from fed state).
Same placement as lizard-agent / solari-reflex; not blackwood
screenshot-in. **Backend-agnostic this hour:**
[gliner2-ultrafast](https://github.com/sahibzada-allahyar/gliner2-ultrafast)
is that hole with local GLiNER2 instead of Jev — observe → score
among a11y/DOM candidates → code acts (`notes.md` §52). Hybrid:
local decide; remote fill only for TYPE. `DONE` is not verified
success.

**Dual-process cascade (Kahneman productized; routing accuracy
unmeasured).**
[`taro1985/dual-process-ai`](https://github.com/taro1985/dual-process-ai)
(MIT): S1 typed decision + confidence; S2 generates only when
`confidence < τ`. Routing **fails open**; safety **fails closed**.
Degraded keyword mode without a key is **not** equivalent S1. Crossover
for business/life, not only SWE: cheap classify/route/gate on S1;
write/reason on S2. Same split as jev-reflex-autonomy-lab (S1 keeps
control) and jev-hermes (route ≠ memory). Do not copy hooks. Tune τ
on *your* escalation log.

## It's just classification

Canonical answer: `references/faq.md`. Short form: classification is not
new; typed, batched judgment as a software primitive *is* the
placement question. Wins vs ad-hoc LLM-classify when you need schema-valid
outputs you can threshold and re-policy; loses to working regexes, trained
heads on stable taxonomies, and generation. Which *family* supplies that
primitive is a second question (`judgment-class.md`): a listwise ranker
and a decision API are both "classifiers" and they are not interchangeable
at a fail-closed gate. Discourse citations and the longer win/lose list
stay below as evidence, not as a second FAQ.

Classification *is* the oldest AI task. Agree with the skeptic
([@dt_sqr](https://x.com/i/status/2100957356389511173)) on that fact, then
answer the design question they actually asked: **where does a typed
judgment beat ad-hoc LLM-classify, and where does it lose?**

Typed Jev judgment wins when most of these hold:

- Software needs a **schema-valid** enum/bool/level, not prose to parse.
  "Hallucination-free" means type-valid, not truth-valid (**Contract**,
  jaggedness docs).
- You will **threshold, abstain, or re-policy** from a distribution. An LLM
  JSON classifier that sometimes omits a key cannot do this.
- The same state needs **many independent questions** (fan-out). Serial
  LLM calls are the cost you are avoiding (**Contract**, parallel-questions
  cookbook).
- Economics invert the design: per-line, per-hunk, per-message, per-chunk
  judgments were known methods that were too expensive. At ~100ms / fractions
  of a millicent they become default (**Empirical recipes** below).
- Policy must be **reviewable in code** (weights, per-action bars, permit
  independent of confidence). Prompt-buried policy is the failure mode.

Typed Jev judgment **loses** to:

- A regex, schema, or lookup that already solves it — keep the exact tool
  (`boundary-audit.md`).
- A **trained classical classifier** on a stable, labeled, closed taxonomy
  with enough of *your* data. XGBoost/CatBoost on Jev features is a mapping
  (`mappings.md` §1); XGBoost *instead of* Jev is often correct
  ([@hughesanalytics](https://x.com/i/status/2100957428799967514) — flexibility
  vs a fit model). Measure; don't slogan.
- Open-ended writing, multi-hop derivation, counting, date math — jaggedness
  **Contract**. Decompose or don't use Jev.
- Claiming calibration as a unique moat. Community ECE comparisons on X
  (e.g. ModernBERT vs Jev) are **Hypothesis** until reproduced on *your*
  population. In-distribution ECE can look excellent and still collapse OOD
  (Archer Hume: 32% on novel two-step word problems — `notes.md` §7).

The product is not "we invented classification." The product is **placing a
fast scoring primitive inside software that already has a generator and a
control loop**, with the family's objective matched to the fail policy
(`judgment-class.md`).

## Cost-sensitive prefilter

Detail cards: context sieve, exact-text keep/drop, env triage, and
moderation/ranking in `references/applied-mappings.md`. This section is the
cascade thesis only.

A cascade, not a chatbot with a cheaper first word:

```text
retrieve / emit a large set
    → judgment-class relevance (Noul / Score / encoder affinity / listwise score)
    → drop / stub / hold the confident-no
    → expensive LLM or human sees only what survived
```

Code still owns recall: the scorer cannot recover a candidate you never retrieved
(`mappings.md` §4). Prefilter **fail-open vs fail-closed is per action**,
not a global virtue:

| Action | Typical failure policy | Why |
|---|---|---|
| Drop a RAG chunk or log line | **Fail open** (keep on error) | A false drop loses evidence; a false keep costs tokens |
| Compact / drop a completed tool result | **Fail closed** to keep-full (`gliner25-compaction`) | Compaction is a destructive edit of memory. Uncertain *looks* like keep-on-error from the evidence side; name the *reduction* as the act. Contrast Abide / jevgate fail-open |
| Omit a session-memory fact from the brief | **Fail open** (dump the whole ledger) (`carryforward`) | Scoring failure must not hide a rule. Constraints/corrections always return; Jev never votes on them |
| Prune Bash stdout before the LLM | **Fail closed** to original (`jev-pruner`) | Dropping the log is irreversible. ≤10k / JSON-diff-whole-doc prove pass-through; archive/Jev/incomplete-score failure keeps the result. Harbor plugin-eval cannot reach Jev → cannot prune |
| Skip waking a sleeping agent | **Fail open** (wake on error / unsure / no key) (`wakegate`) | Skip is the irreversible act. User-message, skip-limit, nothing-to-judge, and p in 0.2–0.5 all wake. Contrast pi-jev-approver fail-closed without a key |
| Merge a red CI run | **Fail closed** on `--gate` (`latch`); reporter stays fail-open | False PASS merges a real bug. Missing key never fails Playwright; the gate is a separate step. Judge never says ignore alone |
| Plain-English PR check | **Fail closed** on error / empty / low confidence (`if-ai`) | A skipped or timed-out check is not a pass. Threshold is policy, not measured correctness |
| Route to a tool / start a side effect | **Fail closed** (don't call) | A wrong tool is an action |
| Execute a proposed tool call | **Fail closed** on block / timeout / guard error (`toolgate`) | Execution is the irreversible act. `review` needs authenticated human approval, not self-approval. Jev is not authorization. Distinct from ndolinschi allow/ask_human/deny *vocab* |
| Actuate an observed browser control | **Fail closed** (code validates the node) | Freshness / visibility / disabled / occlusion in code; model never emits selectors (`gliner2-ultrafast`, jev-ultrafast, solari-reflex). `DONE` does not authorize "success". Cua-S1: dry-run default; `execute`/`submit` opt-in; fail-closed unknown checkbox; fill execution fails closed without token `set_value` |
| Rerank a retrieved list | Fail open: keep retrieval order (`WiktorB2004/llama-index-jev`, **Empirical recipe** on BEIR nfcorpus: MiniLM 0.340 nDCG@5 → MiniLM+Jev 0.396; rerank fails open, *select* fails closed). Listwise/cross-encoder scores belong here, not on the row above. | Ranking errors are quality; selection errors are control-flow |

Worked placements (2026-09-18 topic:jev hour + prior archive):

- **Chunks before the LLM** — discourse dominant theme (48 tagged samples).
  Official cousin: classifying RAG passages cookbook (**Contract**).
- **Command output before context** — `ibrahemid/jevprune`: per-line
  relevance against the task; last-N lines and error signatures kept in
  *code* before Jev sees anything; full output recoverable by id. Same
  shape as winnow/fast-jev-compaction (`agent-self-assessment.md`).
  Encoder-backend cousin:
  [gliner25-compaction](https://github.com/m-newhauser/gliner25-compaction)
  — GLiNER2.5 retention Choice + exact spans; fail closed to
  `keep_full`; `shadowMode` default true (`notes.md` §50). Not Jev.
  Stdout-prune cousin, same family, different job:
  [jev-pruner](https://github.com/tamaratran/jev-pruner) — Jev Noul on
  residual noisy Bash after a hard ≤10k/format envelope; fail-safe
  original; archive for recovery (`notes.md` §53). Marketplace id
  still `fast-jev-output`.
- **Session ledger before the next task** —
  [carryforward](https://github.com/Dharundp6/jev-carryforward):
  verbatim facts; Jev scores which are still live; rules never
  judged; fail-open dump (`notes.md` §55).
- **Evidence set before the generator** —
  [decision-native-rag-skills](https://github.com/emergency-lee/decision-native-rag-skills):
  retrieve wide → decide → evidence set → LLM. Embeddings stay
  candidate generators. No universal benchmark (`notes.md` §55).
- **Diff hunks before `git add`** — `ibrahemid/git-jev-stage`: one Choice
  per hunk (`include` / `exclude` / `mixed`); mixed and low-confidence stay
  unstaged; lines never split; staging is an exact patch after confirm.
  Candidates come from `git diff`, not from Jev.
- **Every agent-step before an LLM autopsy** — `aaravriyer193/OpenSmoke`:
  Jev over all steps (cheap enough to skip sampling); LLM only on flagged
  runs for root cause. Prefilter of *analyst attention*. The named cut
  this hour: Noul `env_broken` *as opposed to* the agent's own bug;
  silent vs disclosed vs recovered vs clean. Pre-mortem of a new
  sandbox *before* users meet it (`notes.md` §42). Merge-gate of the
  same split: [latch](https://github.com/CaseReed/latch) clusters in
  code, labels with Jev, policy owns PASS/BLOCK (`notes.md` §51).
- **Realtime hold-before-publish** — community moderation claims ~200ms
  (**Hypothesis** as a number; **Empirical** as a family via Near Here /
  jev-experiments firehose in the archive). Thresholds stay yours.

Falsify a prefilter with: recall of must-keep items, cost/tokens saved,
fail-open behavior on timeout, and a cost curve for false-drop vs false-keep.

## Tool and skill routing

Detail card: `references/applied-mappings.md#5-skill--tool-routing`. This
section is the selector thesis only.

Selector position (`composition-algebra.md` #4), not "the model chooses its
next tool in a loop" (that remains a red flag in `boundary-audit.md`).

```text
closed catalog (tools, skills, query engines, models)
    → Choice: which candidate, conditional on the offered set
    → Noul: does *anything* fit? (reject-all is a first-class outcome)
    → code dispatches, validates args, authorizes, executes
```

Always include a no-match option when coverage is open. Suggest at most one
skill per turn so prefix caches hold (`validation.md`, skill_suggestion
cookbook **Contract**). Rank-then-verify: cheap pass over descriptions, then
a second request over a shortlist with full bodies.

Live ecosystem (examples of the *shape*, not SDKs to copy):

- Official skill_suggestion cookbook; GodsBoy router 94.4% vs 70.8% lexical.
- `Dicklesworthstone/skillranker` — next-step skill rank from live session
  context; fail-closed; calibration loop.
- `WiktorB2004/llama-index-jev` selectors — which query engine handles the
  query; fail closed or a declared default.
- Toolrouter (product, X 2026-09-18) / open JevRouter harnesses — request →
  tool. Treat as **Hypothesis** until you measure on your catalog.
- `rajdhakad9826/routeKit` — Jev estimates requirements; a deterministic
  policy picks the model. Jev does not choose the LLM. **Hypothesis**
  until your catalog (`notes.md` §33).
- [`trietphan/jev-claw`](https://github.com/trietphan/jev-claw) — same
  hole for OpenClaw: Jev classifies task/complexity/risk; `decide()` in
  code maps to a route; a sensitive-path regex floors risk. Confidence
  is the **min** across heads. 11 offline policy tests; live 10/10 is
  the author's 10 samples (`notes.md` §44).
- [`nekowasabi/jev-routing`](https://github.com/nekowasabi/jev-routing)
  — host **adapter** (Go binary), not an MCP server, in front of
  Claude Code / Codex / Grok Build. Compacts tool results, then one
  Choice + done-Noul, then one schema. Adding it via `mcp add` makes
  the catalog worse. No key → on-device classifier. Do not copy ports.
- Higgsfield API auto-routing ([tweet](https://x.com/higgsfield_ai/status/2101022473248727177))
  is the same hole on a video/image catalog. **Claim**, no labeled
  receipt.
- Function-calling cookbook (**Contract**): function *names* and closed-set
  args as questions; code still validates the call.
- [jev-gateway](https://github.com/vinilana/jev-gateway) (~16:48) — host
  adapter: Jev picks the tool (and closed-set args); LLM fills open
  args or is skipped (`direct`). Fail-open passthrough if Jev is down.
  Harbor on/off measurement: [jev-gateway-bench](https://github.com/vinilana/jev-gateway-bench)
  (one-run signal, not a measurement; `notes.md` §51). Do not copy ports.

Routing ROI does not transfer across datasets (`validation.md`, calibre).
`FirasSX914/Janus` exists to *measure* when Jev vs another model wins on
your data, then route — that measurement loop is the design, not a
universal gate.

## Dual orchestration (Jev ∩ LLM ∩ MCP)

Two topologies, same ownership split
([James Ward, 2026-09-18](https://x.com/JamesWard/status/2100976393546772628)):

```text
A. LLM outer loop; Jev is a *tool* that selects among the MCP calls offered
B. Jev outer loop; LLM is a *tool* that writes
MCP output schemas are the exact state a decision model judges over
```

**Transfers:** schemas as exact structure; judgment among a closed tool
catalog; code dispatches. Topology B is mixed architecture with the
generator as a callee (`applied-mappings.md` §5). Topology A is an LLM
agent that *asks* a decision model instead of stuffing a system prompt.
SREGym-Lite is topology A: Jev ranks next tests/evidence; the agent
still runs them and still diagnoses (`notes.md` §33).
[`runta-dev/jot`](https://github.com/runta-dev/jot) is topology B with
a *closed* tool catalog (the host executes; the calculator does the
math). "First general-purpose System One agent" is a claim.
[`nekowasabi/jev-routing`](https://github.com/nekowasabi/jev-routing) is
a host adapter in front of an existing coding CLI (not topology B, not
MCP): it peels the catalog *before* the generator sees it. **Does not:** the decision model as the planner — neither inventing tools
nor picking its own next tool in a loop (standing red flag, above and in
`boundary-audit.md`); skipping schemas so the model "just knows";
treating a workflow AST as a proof. The outer loop stays with the LLM or
with code. **Hypothesis** as "Jev builds the AST"; **Empirical** as named
topologies. Not an MCP how-to.

**S1 keeps control; S2 is one-use advice.** Topology B under latency:
the reflex (typed Choice over legal actions) never hands the stick to
the planner. Optional System 2 is *advice* on low confidence, one-use,
asynchronous — the reflex does not pause
([jev-reflex-autonomy-lab](https://github.com/khordoo/jev-reflex-autonomy-lab);
experimental drone viz, not a flight controller; GitHub license null
this pass). Same Kahneman split as the toolbox row (S2 proposes, S1
discriminates; never the reverse). `notes.md` §46.
`agent-self-assessment.md`. **Route ≠ memory** is the same split on a
turn: [jev-hermes](https://github.com/de-niji/jev-hermes) cheap-gates
calendar/mail/status off the memory tour; complex keeps Honcho
(`notes.md` §48). **Advisory sidecar:**
[agent-workflow-typesafe-ai](https://github.com/ngallodev-software/agent-workflow-typesafe-ai)
emits `no_action` receipts and **never** changes host routing.
**Productized Kahneman cascade:**
[dual-process-ai](https://github.com/taro1985/dual-process-ai) — S1
decides, S2 writes; routing accuracy **not measured**; keyword
fallback is not S1 (`notes.md` §49).

**Effect-oriented loop (same author, later post).** Topology B inside
an effect system
([tweet](https://x.com/JamesWard/status/2100981305009664299)): the host
offers the finite legal actions; one Choice picks the transition; the
handler runs the effect and returns continue or done. "An action
handler may run arbitrary ZIO effects—MCP calls, database operations,
or a no-tool generative model call—while Jev remains the outer decision
loop." Code owns transitions (§3). **Hypothesis** card:
`mappings.md` §19. The pixels are that ZIO client, not an Effect.ts
snippet and not the Jev HTTP contract.

## Preference lint and gates

Verifier position (`composition-algebra.md` #9) over **rules the project
already wrote**. Jev does not invent taste.

`doeixd/jev-pref` states the contract we want every agent-gate to copy
(**Empirical recipe** as a boundary, not as an API):

```text
YOU define the rule.
JEV classifies the evidence.
CODE maps the answer to an outcome (approve / advisory / block).
THE AGENT acts — or doesn't.
```

A useful check is externally defined, evidence-grounded, narrow, actionable,
calibratable, and complementary to ESLint/types/tests. Poor checks: "is this
good architecture?", "are these tests sufficient?", "is this clean?" Those
ask Jev to own the standard of quality. Good checks: "does this diff
introduce new mutable module-level state?", "API impact: none / additive /
behavioral / breaking?"

[`coldteadotai/abide`](https://github.com/coldteadotai/abide) is the
fuller **productized** path of that contract (compile / calibrate /
tune / replay / audit; Claude Code / Codex / OpenCode). Soft
AGENTS.md / CLAUDE.md rules → one Score per rule on the **diff**,
never the conversation; hard, linter-checkable rules stay with the
linter — same layering family as jevgate's hard envelope (`mappings.md`
§18). Edit-phase vs turn-phase is an observation-window question
("added more than asked" has no answer after edit 1 of 12;
`question-design.md`). Product bands: ≥0.8 repair, 0.5–0.8 note, <0.5
silence — **their** operating point, not a universal 0.8 (`mappings.md`
§2). Fail-open: no key / no network → the edit proceeds; hooks exit 0.
`.abide/rubric.json` quotes source lines; false positives are rule
rewrites, not a model swap. Replay of 93 sessions with an independent
reviewer: edit precision ~26%, turn ~73% (`notes.md` §47;
`validation.md`). Text/diff only — not multimodal. Complementary to
[`24601/rh-guard`](https://github.com/24601/rh-guard) (eval-integrity /
reward-hacking on tool use vs project soft rules on diffs): same
hook-host lessons, different judgment class; do not merge products.
Do not copy hooks.

Related placements:

- **AGENTS.md / project prefs as criteria** — jev-pref states the
  contract; Abide productizes it; pi-warden rule breaks 6→0 on 150
  paired runs (`agent-self-assessment.md`; `notes.md` §47).
  [if-ai](https://github.com/Victor-Casado/if-ai): one plain-English
  condition + required min-confidence; fail-closed on error
  (`notes.md` §51). [jev-marshal](https://github.com/LightningK0ala/jev-marshal)
  is Watch / empty.
- **Confidence gates + shadow mode** — `AntonioCoppe/jev-harness` (48.9s
  Claude CLI vs 1.3s Jev on a 24-row filter). Log would-do until evals
  pass. Selective abstention (`mappings.md` §2): low confidence is
  `review`, not a guess. Coppe on SREGym regressions: inspect whether
  confidence was high on the wrong Choice (`notes.md` §33). This hour
  the *practice* is first-class: eval CLI asserts on the **action**,
  not on prose; recipes span alerts / RTB / sports-bet / prediction
  markets (`notes.md` §44). LLM-as-judge is not the primary System One
  score (`faq.md`). Compaction rollout of the same instinct:
  [gliner25-compaction](https://github.com/m-newhauser/gliner25-compaction)
  public default `shadowMode: true` (analyze + log; do not replace
  history until explicitly enabled) (`notes.md` §50). Do not copy the
  client.
- **Hybrid countable + judgment rules** — `DanRWilloughby/snifftest`:
  deterministic tells score 1.00; judgment rules flag only outside the
  unsure band. Explicit: a reading near 0.5 is *no judgment*, never a pass.
  That is the Noul-0.5-is-uncertainty non-negotiable, implemented.
- **Rubric-then-prose review** — `frostney/clean-code-review`: Jev against a
  named rubric (Clean Code), then an LLM writes the review. Mixed
  architecture, not "Jev is the reviewer."
- **Convention lint (file-level)** — `huntedman/JevLint`: plain-English
  rules → file-level Noul ≥ 0.8; write→check→fix; no line-level, no
  generated names, no auto-fix. Sibling of jev-pref. Independent, not
  TypeSafe. Pointer: `notes.md` §26.
- **Malicious-before-run** — `luantak/is-malicious`. High-stakes gate:
  fail closed, shadow first, never treat a Jev yes as authorization to
  execute untrusted code. Code still sandboxes.
- **Meta-VOI / "does this need a model?"** —
  [`wotai-dev/typesafe-jev-tools`](https://github.com/wotai-dev/typesafe-jev-tools):
  three-way test (regex vs System One vs frontier); never blocks.
  149-row receipt: Haiku was more accurate; Jev's confidence was the
  monotonic one. If you do not branch on confidence, use whatever you
  already have (`notes.md` §42). Do not copy the hook.

Permit is independent of confidence (`Kevthetech143/super-jev`): domain
rules veto regardless of model certainty.

## Placement gallery (2026-09-18 movers)

Use these as *existence proofs of a position*, then write your own
decision-design card. Do not clone APIs from READMEs.

| Placement | Judgment | Stays in code | Artifact |
|---|---|---|---|
| Hold-before-publish moderation | Hazard Nouls + harm Score | Block/review/pass policy | Near Here / firehose family |
| Tool / engine / skill select | Choice + fits-Noul | Dispatch, auth, reject-all | skillranker, LlamaIndex selectors, Toolrouter |
| Preference lint | Per-rule Score/Noul on a diff | Rule text, linter for hard rules, bands + fail-open | jev-pref (contract), Abide (productized), JevLint; if-ai (plain-English PR check, fail-closed on error); jev-marshal (Watch / empty repo) |
| Context / log prune | Per-line or per-block relevance; or a retention Choice + spans; or a Noul per stdout chunk | Always-keep set, recall keys; mutation envelope in code; shadow before replace; size/format envelope then Noul; archive dropped spans | jevprune, winnow; fast-jev-compaction / pi-jev-compaction (Jev session); gliner25-compaction (GLiNER2.5 session); jev-pruner (Jev Bash stdout) |
| Exact hunk staging | Per-hunk include/exclude/mixed | `git diff`, atomic apply | git-jev-stage |
| Semantic `WHERE` | Noul/`jev_prob` over a row | SQL, indexes, LIMIT | jevql (CLI; DB sees ordinary SQL); sqlite-jev (in-engine extension) |
| Formula / query embedding | JUDGE as a function | Spreadsheet/SQL engine | judge-sheets, jevql, sqlite-jev |
| Soft ABR / live encoder | Choice over a ladder | Probe × headroom, thermal, battery | bitrate-advisor |
| Voice → typed act | Choice/Noul on a transcript | ASR producer; macOS actions | jev-voice-control (README stub) |
| Host-adapter routing | Choice next-tool + done-Noul | Shrink `tools[]`; compaction | jev-routing (not MCP) |
| Multi-model route | Classify axes; policy maps | Escalation `if`, path regex | jev-claw, routeKit |
| Finish-line gate | Noul/Score/Choice on evidence | Deterministic shell checks first | hermes-jev-north-star |
| Home automation read | Choice/Score/Noul as an entity | Automations, device I/O | `AboveColin/HA-Jev` |
| Browser loop without generation | Action Choice over visible elements | Perception, constraints, click | lizard-agent |
| Screenshot / DOM candidates → Choice | Omni decide over letters code marked | Click/act in code; fail-open to specialist OCR | blackwood-rlcd (CC BY-NC; not Archer) |
| Android / macOS computer-use | Choice over prevalidated candidates | UI tree / AX / OmniParser; no generated coordinates | jev-mobile, jev-macos-loop |
| S1 reflex + optional S2 advice | Typed action Choice; planner one-use on low p | Collision, legality, the stick stays with S1 | jev-reflex-autonomy-lab (experimental) |
| Decision-as-business-tool | Named judgment; gate is part of the result | Registry, arithmetic, hard guards | jev-decision-layer (unofficial) |
| NL cases → checked e2e | Jev selects observed controls | Playwright expectations; PASS/FAIL/BLOCKED | jev-e2e (alpha) |
| Extractive quotes / pointer evidence | Per-sentence, per-line-id, or char-offset Noul/Choice | Verbatim join; place; `redecide` / CSV; model never writes the excerpt | testimonial-miner; jev-reviewer; gliner25-compaction |
| Structured observe → decide → act | Score / Choice among numbered a11y/DOM controls | Guard check; deny-list absence; no screenshots; no generated selectors; TYPE is the only generation; `DONE` ≠ verified success | solari-reflex (Jev); jev-ultrafast (Jev); gliner2-ultrafast (GLiNER2); laya-mind2web (Laya, DOM indices); cua-s1 (option-attention fill/check/click/skip; not TypeSafe Jev; source-only) |
| Specialist form S1 (plan ≠ execute) | Option-attention among observed elements | Dry-run default; snapshot-bound tokens; reobserve; submit opt-in; fail-closed checkbox/fill | cua-s1 (`cua-s1-form-v0` profile; no weights this pass) |
| Hybrid local decide + remote fill | Local encoder scores observed controls | Code owns actuators; remote OpenAI-compat helper writes field text only | gliner2-ultrafast (GLiNER2 local + Mercury 2.5 default) |
| Dataframe semantic columns | Noul / Choice / Score per row; full `p__` | pandas/Polars, indexes, never silent renormalize | jevpandas; jevframe (PyPI + Polars) |
| Route ≠ memory | Intent Choice before a turn | Config + flat tools on easy routes; memory stays on for hard ones | jev-hermes |
| Advisory sidecar receipts | Typed answers as `no_action` evidence | Host routing / executor / policy unchanged | agent-workflow-typesafe-ai |
| Structure induction over a bag | Pairwise dependency Noul/Choice | DAG / scheduler in code | dag-jev (experiment) |
| Simulated world control vs content | Intent / page-type Choice | Generator writes documents; Zod + deterministic compiler; SQLite world | jev-agentworld-web-simulator |
| AST ∩ semantic lint | Typed questions on Tree-sitter units | Parser, selection, fail-on; does not execute scanned code | jevscan (`tenbin` owns the lint skill) |
| Model router | Requirement Scores; policy in code | Eligibility, cost/quality/latency objective | routeKit |
| Bulk-judgment coprocessor | Choice/Noul off the frontier context | Counts, policy, fail-open gate | jev-mode |
| Closed-catalog System One shell | Choice over host tools | Execute, arithmetic, credentials | jot |
| Jump-by-description | Noul relevance on a local shortlist | zoxide index, local paths only | joxide |
| Game move | Choice over legal actions | Rules, legality, win check | jev-plays-games |
| Analyst attention cascade | Step-level silent-failure Nouls | Grouping, LLM autopsy | OpenSmoke |
| CI merge-gate (flaky vs real) | Cause Choice per clustered signature | Cluster + fingerprint + PASS/BLOCK table; reporter never fails the runner | latch (`notes.md` §51) |
| Fail-open wake / resume | p(wake) on waitingFor × event | Sleep duration, skip-limit, user-message always wakes | wakegate |
| Claim/evidence Stop | supports / contradicts / not-addressed per claim | Keyword retrieve session lines; firm-confidence floor never blocks | clear-head |
| Harbor on/off routing | Tool Choice per turn | Hidden verifier; fail-open if Jev down | jev-gateway + jev-gateway-bench (one-run signal) |
| Device-loop Choice | Folder among a closed catalog | Never invent folders; extension-map fallback | jev-downloads-sorter |
| S1 extract + escalate-S2 index | GLiNER spans / relations on the bulk | Graph in code; LLM only if backend loaded and low conf; query does not invent edges | s1-graphify-indexer (10–50× unfilled) |
| S1 specialists + S2 coordinator | Typed {value, probability} | Coordinator / hysteresis in code | reification-labs/foreman (**description-only** Phoenix scaffold; not the super-jev loop) |
| Bounded Pi supervisor | Skills / recovery / review / verify | Shadow default; never generates commands | jevons |
| Judgment as language primitive | `chance` / `pick` / `rate` (Noul / Choice / Score) | English-as-config; stub backend; fail polarity per action (`rescue nil` at save ≠ spam gate) | hunch (Ruby library, not a new language; cousin of probably-lang) |
| Decision-native RAG | Relevance / evidence / freshness / authority Nouls + Score | Evidence-set builder, conflict/temporal logic, provenance; embeddings generate candidates only | decision-native-rag-skills (no bundled harness; Hypothesis as a measured win) |
| Verbatim session recall | Noul "still live for this task?" | JSONL ledger; constraints/corrections always-keep; fail-open dump | carryforward (9×3 hint, not proof) |
| Pre-exec tool gate | allow / block / review | Permissions, arg validation, transaction limits in code; timeout stops | toolgate (72-case synthetic, not independently annotated; Jev ≠ authorization) |
| Healthcare S1 + S2 | NEWS2 remainder / med recon / inbox route | Code owns NEWS2, recon, routing; S2 blinded review | explore-typesafe-ai (synthetic FHIR; not clinically validated) |

On-device / Home Assistant / mobile are newly-feasible via the economics
inversion, not proven ports of every app. Named placements this hour
(`notes.md` §33): `Friedjof/jev-mobile` (USB Android, Mobile MCP task
delegation, Jev sees only prevalidated candidates); `jcpsimmons/jev-macos-loop`
(local OmniParser/OCR/AX; text-only Jev; pixels stay on the Mac; Finder
demo independently verified). HA-Jev unchanged. Do not copy env, MCP
URLs, or install steps.

Reproduce/open heads (`rongxinzy/LightJev`, openjev family,
[`convaiinnovations/laya`](https://huggingface.co/convaiinnovations/laya),
encoder [`open-jev-deberta-v3-large`](https://huggingface.co/com-kotobalabs/open-jev-deberta-v3-large),
LoRA [`jev-gate-student-b`](https://huggingface.co/SargeDev/jev-gate-student-b),
companion packaging [`laya-typed-decisions`](https://huggingface.co/convaiinnovations/laya-typed-decisions),
[`jaredpalmer/kev`](https://github.com/jaredpalmer/kev),
[`BlackwoodAI/blackwood-rlcd`](https://huggingface.co/BlackwoodAI/blackwood-rlcd))
are evidence that the *interface* (Choice/Score/Noul, or yes/no logits
as P(relevant)) is the transferable part — not a request to implement a
backbone or a second API skill. Laya: self-hostable, text-only, 512
tokens/question; vendor benches vs Jev are **claims**. Encoder open-jev:
public gold, OOD drop. LoRA student: teacher-copy. **kev**: public gold,
pointer readout, System One API drop-in; ID ECE only; not a teacher-copy
(`notes.md` §45). Hub fetch:
[`jaredpalmer/kev-0.5b`](https://huggingface.co/jaredpalmer/kev-0.5b).
**blackwood-rlcd**: open multimodal RLCD, Jev-compatible
shim, CC BY-NC; Jev still leads general text; not Archer Watch
(`notes.md` §46). Hume's 27B
decision-model drop is **Watch**. Closed calibrated API vs open weights
is a self-eval tradeoff (`research/notes.md` §18, §33, §45). When-to-use
axes: `judgment-class.md`. TypeSafe remains the documented *exemplar*,
not the class monopoly. **Local CUDA/PyTorch replica this hour:**
[`Mintzs/jevify`](https://github.com/Mintzs/jevify) — Qwen2.5-1.5B
Choice/Score/Noul *shape*; **uncalibrated likelihoods ≠ Noul**; no
LICENSE this pass (`notes.md` §55). **Local contract drop-in this hour:**
[`us/jev-local`](https://github.com/us/jev-local) speaks `/v1/systemone`;
**default scorer is a deterministic stub** until `JEVLOCAL_SCORER=hf`
(`notes.md` §48). **ONNX replica path:**
[`Mattepiu/laya-onnx`](https://huggingface.co/Mattepiu/laya-onnx) — do
not copy the inherited vs-Jev table. GLiNER (locate) / GLiClass (categorize) /
GLiNER2.5 (local multi-head; extractive compaction is a named *job* on
that family, `notes.md` §50; computer-use selection is a *different*
named job on GLiNER2 `gliner2-multi-v1`, `notes.md` §52), listwise, and vision families:
`judgment-class.md`.

## Design-card extras for mixed systems

When the request is mixed-architecture, fill the usual card plus:

```text
Family (from judgment-class.md) and why the objective matches the fail policy:
What the judgment model estimates (and which primitive / score type):
What the LLM is still for (or why this loop has no LLM):
What code guarantees even if the judgment model is wrong:
Cascade costs: false drop vs false keep vs wrong route:
Fail-open or fail-closed, per action:
Classical alternative that might still win (regex, XGBoost, cross-encoder, human):
Live docs + typesafe-ai skill revision actually used (when the family is Jev):
```

Propose three *placements* (prefilter vs post-verify vs replace-this-one-
classifier-step), recommend one, and name the experiment that kills it.
