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

**Harness productization this hour (draft Watch):**
[Stagehand #2951–#2955](https://github.com/browserbase/stagehand/pull/2955)
puts the same DOM-as-text loop inside Browserbase Stagehand: Jev
picks; code copies or acts; LLM fallback. Extract pick-and-copy is
a fast path, not a replacement (`notes.md` §57). Do not copy the
opt-in flag.

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
| Open a file / URL into agent context | **Fail open** (closer look on error / truncation / uncertain) (`jev-sift`) | False drop loses evidence. Errors and truncation are not irrelevance. Transport failure ≠ "irrelevant" |
| Withhold a draft because the judge is silent | **Fail open** (heartbeat / proceed or escalate; do not hold forever) | Missing verdict is not a block and not a pass. Contrast Abide `<0.5` silence (the *edit proceeds*) |
| Prune Bash stdout before the LLM | **Fail closed** to original (`jev-pruner`) | Dropping the log is irreversible. ≤10k / JSON-diff-whole-doc prove pass-through; archive/Jev/incomplete-score failure keeps the result. Harbor plugin-eval cannot reach Jev → cannot prune |
| Skip waking a sleeping agent | **Fail open** (wake on error / unsure / no key) (`wakegate`) | Skip is the irreversible act. User-message, skip-limit, nothing-to-judge, and p in 0.2–0.5 all wake. Contrast pi-jev-approver fail-closed without a key |
| Merge a red CI run | **Fail closed** on `--gate` (`latch`); reporter stays fail-open | False PASS merges a real bug. Missing key never fails Playwright; the gate is a separate step. Judge never says ignore alone |
| Plain-English PR check | **Fail closed** on error / empty / low confidence (`if-ai`) | A skipped or timed-out check is not a pass. Threshold is policy, not measured correctness |
| Route to a tool / start a side effect | **Fail closed** (don't call) | A wrong tool is an action |
| Execute a proposed tool call | **Fail closed** on block / timeout / guard error (`toolgate`) | Execution is the irreversible act. `review` needs authenticated human approval, not self-approval. Jev is not authorization. Distinct from ndolinschi allow/ask_human/deny *vocab*. Distinct from **capability kernel** (`interlock`): secrets never in the agent; closed action space; Jev is SENSOR; `policy.py` BLOCK/ASK/ALLOW |
| Kill a live process / port | **Fail closed** to human confirm (`port-cleanup`) | Jev recommends; human is the only trigger. Identity re-check before signal; shields override; mapped explanations, not raw model prose. Kill recs need conf ≥ 0.8 |
| Actuate an observed browser control | **Fail closed** (code validates the node) | Freshness / visibility / disabled / occlusion in code; model never emits selectors (`gliner2-ultrafast`, jev-ultrafast, solari-reflex). `DONE` does not authorize "success". Cua-S1: dry-run default; `execute`/`submit` opt-in; fail-closed unknown checkbox; fill execution fails closed without token `set_value`. Stagehand: same; LLM fallback when Jev abstains |
| Replay a cached browser action | **Fail open** on the freshness check (`stagehand` cacheCheck) | Errors/timeouts never block replay; a stale verdict re-infers. Opt-in: the check costs a snapshot + a request |
| Skip the LLM on extract / act | **Fail open** to the generator (Stagehand pick/judge) | Schema/gate/screenshot envelope in code; pick is a fast path, not a replacement. Invalid extract → LLM |
| Publish a public wall ask without a key | **Fail open** (allowlist; UI says Jev offline) (`ask-jev-ai`) | Missing judge is not a block and not a silent pass. Safety p≥0.6 still blocks when the judge is on |
| Assign PR attention P2 | **Fail closed** incomplete → `uncertainPriority` never P2 (`egma-ai/jev-reviewer`) | Attention ≠ correctness. Deterministic `alwaysReviewPaths` P0. Do not treat a Noul as a proof the PR is good |
| Pick a session model | **Fail closed** to a declared standard (`jev-adaptive-thinking`) | Timeout / no session / missing first-round text locks `gpt-5.6-sol`. Contrast jev-gateway fail-open passthrough if Jev is down |
| Drop a meaning-search hit | **Fail open** as ranking (`jevgrep`) | False drop loses the file. Keyword tools still win exact strings |
| Rerank a retrieved list | Fail open: keep retrieval order (`WiktorB2004/llama-index-jev`, **Empirical recipe** on BEIR nfcorpus: MiniLM 0.340 nDCG@5 → MiniLM+Jev 0.396; rerank fails open, *select* fails closed). Listwise/cross-encoder scores belong here, not on the row above. One-run cousin: Jev-RAG vs Spark *rerank* (full-context Spark still faster) | Ranking errors are quality; selection errors are control-flow |
| Auto-act an email / ticket | **Fail closed** to review when Noul ≈ 0.5, Score conf = 0.0, or a hard flag fires (`jav-email-cascade`) | Noul 0.5 is cannot-tell, never rounded. Injection always review. LLM leftover is optional |
| `ORDER BY prob LIMIT k` | **Fail open** as ranking; ties need a secondary key (`jev-orderby-bench`) | Two-decimal quantization; 53-way 0.99 tie is engine-dependent. Calibration ≠ sortable |
| Run an irreversible browser/OS act in closed-vote CU | **Fail closed** unless a separate risk vote is low (`JevOnly` `risk ≥ 0.50` never default; waymode host confirmation / p ≥ 0.7) | Code builds options; Jev only picks. `completed` ≠ verified success. Host handlers/permissions still decide |
| OMP/pi acceptance gate or subagent route | **Fail open** if Jev missing / timeout / malformed (`omp-jev-extensions`; `confidence: 0`) | A flaky decision service must not trap the agent. Contrast pi-jev-approver fail-closed without a key |
| Suppress an OMP tool-approval prompt | **Fail closed** to prompt the human unless the operator-owned bar says allow (`omp-greenlight`) | Not a sandbox. Host `bash.patterns: deny` stays the floor and fires first. Plugin never self-tunes the bar. 0/94 is the labelled corpus, not live traffic |
| Grant a specialised skill pack | **Fail closed** to foundation-only; never broaden access (`skill-broker` outline) | Jev scores relevance; code owns grants. Candidates ≠ grants. **Hypothesis / outline — not a production recipe** |
| Treat a Jev score as eval truth | **Fail closed** until the instrument is audited (`dinostomp`) | Check data/scorer/runs/claims, not just the number. `dinostomp jev` tests a question like an if-statement |
| Pick an LLM backend with live Jev on the hot path | **Fail open** to local deterministic features (`slo-router`) | Jev is a feature, not the sole gate. Same routes/accuracy on their fixture; p95 **77.93 → 490.38 ms**. Exactness raises the quality floor; never overrides capability. Eight-row demo is not a benchmark |
| Allow a proposed shell command | **Fail closed** on missing / low-conf / high-risk / failed call (`construct-auto-classifier`) | Privilege ≠ verdict (`sudo status` can be safe). Fast-allow/deny prove; Jev Choice + independent risk Nouls on the remainder. 0 dangerous / 975 *theirs*; chat models leaked |
| Tell a human the agent work is green / skip | **Fail closed** to "look" unless sure (`jev-lens`); **never block** the agent | Attention filter / VOI, not a permission gate. Never edits files. `JEV_LENS_GREEN` 0.9. Distinct from jev-gates (stops writes) |
| Endorse a question pack | **Fail closed** until recorded evidence (`jev-packs`) | No numbers, no `verified`. Pin model version. Abstention/`unknown` mandatory. Runner named, not shipped this pass |
| Authorize a proposed tool call | **Fail closed** on a deterministic security failure (`actiongate-jev`) | Jev supplies evidence; code owns authority. Positive score never overrides RBAC/schema/limit. Financial/destructive/credential fail closed if Jev is down |
| Auto-act on a raw decision-model p | **Fail closed** until domain recalibration (`does-jev-confidence` / `jevcal`) | Ranking ≠ calibration. Vendor "calibrated" often means rank-correlation. Stated ~75% vs human ~10% *theirs* |
| Compact a long agent history (middleware) | **Fail open** to uncompacted history if Jev is down (`jev-compactor`); **fail closed** on pending destructive/exfil | Dual polarity in one product. Regex floor always local. Contrast gliner25-compaction fail-closed `keep_full`. Never rewrite kept bytes |
| Click / type from an indexed viewport | **Fail closed** to code-owned `--until` / stuck / no-guess fill (`ego-jev`) | Jev `done` is not business success. Malformed text-model JSON does not guess a value. Stale refs aborted |
| Collapse a social reply | **Fail open** as hide-not-delete (`x-reply-filter`); local rules first | Auto-hides are not training labels until a human confirms. Never self-reinforce on the model's own negatives |
| Rank the next skill from live context | **Fail open** on the Claude hook (`skillranker`); CLI keeps real exit codes | Advisory ranking; none-of-these is first-class. A failed recommendation must not block the agent. Distinct from skill-broker (grants) |
| Authorize a proposed tool after policy permit | **Fail closed** on explicit deny; **Review** if Jev is missing (`turnstile`) | Jev never grants what policy denied. Replay thresholds on saved scores; starting 0.85/0.35 are not calibrated. Observe mode is not enforcement |
| Endorse a capability claim / bake-off slogan | **Fail closed** until receipts (`jev-capability-atlas`); attach thinking budget (`jev-frontier-100`) | Not a leaderboard. Schema-valid ≠ correct. "Weaker than 4B" needs the thinking condition |
| Threshold raw p on an unseen rule | **Fail closed** until type-specific recalibration (`jev-ood-calibration`) | AUC ≠ ECE. Choice/Score overconfident (T~3.3); boolean underconfident (T 0.66) on the same tickets. Unknowable policy labels still get mean p 0.74 |
| Gate a vector on Jev `confidence` alone | **Fail closed** until you inspect entropy/margin (`how-sure-is-jev`) | Choice confidence = max_prob (most generous). 75/25 → 0.5 vs entropy 0.19. Bands are policy |
| Advance a sealed effect | **Fail closed** until Seal + coverage (`seal`) | Jev answers questions; SEAL answers whether the world may change. Open escalations keep Effects locked |
| Return a confident pharmacy/protocol verdict under chaos | **Fail closed** to escalate (`jev-labs`) | Never confidently wrong. 1,080 golden 0 wrong *theirs* is not a proof of zero. Stability ≠ answerability |
| Auto-approve a PR from four typed questions | **Fail closed** to human-review unless operator bar says so (`ci-gatekeeper-bot-jev`) | Conservative default escalated trivial diffs. Distinct from latch (finished red run) |
| Rank Codex capabilities / excerpts | **Fail open** to lexical overlap (`jev-in-codex`) | Ranking unbenchmarked. Rec ≥ 0.5 is a heuristic. Caller supplies the catalog |
| Drop a meaning-grep line | **Fail open** as ranking (`jev-semgrep`); keyword still wins exact strings | AND/OR/NOT over line Nouls. Japanese meanings noisier near threshold |

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
- **Files / URLs before the main agent reads** —
  [jev-sift](https://github.com/kbhuw/jev-sift): classify first,
  read selectively. Batch path/url/text → Jev; the main LLM opens
  survivors. Uncertain/errors/truncation ≠ irrelevant. Topology A
  MCP (LLM outer loop). Transport tests ≠ accuracy. No LICENSE this
  pass (`notes.md` §56). Do not copy plugin how-to.
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
  context; two-pass + none-of-these; Claude hook **fail-open** (quiet
  exit 0); CLI keeps real exit codes; local calibration/replay. 52★.
- `WiktorB2004/llama-index-jev` selectors — which query engine handles the
  query; fail closed or a declared default.
- Toolrouter (product, X 2026-09-18) / open JevRouter harnesses — request →
  tool. Treat as **Hypothesis** until you measure on your catalog.
- `rajdhakad9826/routeKit` — Jev estimates requirements; a deterministic
  policy picks the model. Jev does not choose the LLM. **Hypothesis**
  until your catalog (`notes.md` §33).
- [jev-adaptive-thinking](https://github.com/jxu-dev-c/jev-adaptive-thinking)
  (~18:46) — session-sticky first-prompt Choice; lock for the
  session; fail-closed to `gpt-5.6-sol`. License null. Live testing
  left to the deployer (`notes.md` §58). Do not copy dylib/YAML.
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
MCP): it peels the catalog *before* the generator sees it.
[`kbhuw/jev-sift`](https://github.com/kbhuw/jev-sift) **is** topology A
MCP: the LLM still owns the outer loop; Jev is a tool that classifies
paths/URLs/text before the agent reads them (`notes.md` §56). Do not
merge with jev-routing. **Does not:** the decision model as the planner — neither inventing tools
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
**Harbor-shaped decide→policy leftover (measured compare arms,
2026-09-18 ~20:43):**
[jav-email-cascade](https://github.com/skiingfalcon/jav-email-cascade)
— shared Answer schema; jev / gen-json / gen-logprob; policy
auto/review/llm; Noul 0.5 never rounded. Mock gen-json
flat-confidence is *their mock*. License null this pass
(`notes.md` §60).
**Closed-vote computer-use, no planner LLM (2026-09-18
~21:39):**
[JevOnly](https://github.com/buluoray/JevOnly) — code builds
options, Jev only picks; fact register + verify/undo; type
without generation. Apache-2.0. Distinct from Stagehand LLM
fallback (`notes.md` §61).
**Host-owned product surface:**
[waymode](https://github.com/mossburgh/waymode) — app retains
handlers/permissions/validation/state; Jev over live typed
actions; `completed` is Jev's reading. 24/26 and 34/36
*theirs* — bounded evidence, not a self-driving proof
(`notes.md` §61).

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
| Hold-before-publish moderation | Hazard Nouls + harm Score | Block/review/pass policy | Near Here / firehose family; **x-reply-filter** (local rules first; never auto-train on own hides) |
| Tool / engine / skill select | Choice + fits-Noul | Dispatch, auth, reject-all | skillranker, LlamaIndex selectors, Toolrouter |
| Preference lint | Per-rule Score/Noul on a diff | Rule text, linter for hard rules, bands + fail-open | jev-pref (contract), Abide (productized), JevLint; if-ai (plain-English PR check, fail-closed on error); jev-marshal (Watch / empty repo) |
| Context / log prune | Per-line or per-block relevance; or a retention Choice + spans; or a Noul per stdout chunk | Always-keep set, recall keys; mutation envelope in code; shadow before replace; size/format envelope then Noul; archive dropped spans | jevprune, winnow; fast-jev-compaction / pi-jev-compaction / fast-jev-compaction-pi (Jev session; pi host port); gliner25-compaction (GLiNER2.5 session); jev-pruner (Jev Bash stdout); **jev-compactor** (framework-agnostic middleware + regex floor + Foreman; fail-open if Jev down) |
| Exact hunk staging | Per-hunk include/exclude/mixed | `git diff`, atomic apply | git-jev-stage |
| Semantic `WHERE` | Noul/`jev_prob` over a row | SQL, indexes, LIMIT | jevql (CLI; DB sees ordinary SQL); sqlite-jev (in-engine extension) |
| Formula / query embedding | JUDGE as a function | Spreadsheet/SQL engine | judge-sheets, jevql, sqlite-jev |
| Soft ABR / live encoder | Choice over a ladder | Probe × headroom, thermal, battery | bitrate-advisor |
| Voice → typed act | Choice/Noul on a transcript | ASR producer; macOS actions | jev-voice-control (README stub) |
| Host-adapter routing | Choice next-tool + done-Noul | Shrink `tools[]`; compaction | jev-routing (not MCP); **jev-in-codex** (Codex MCP; ranking unbenchmarked; lexical fallback) |
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
| Structured observe → decide → act | Score / Choice among numbered a11y/DOM controls | Guard check; deny-list absence; no screenshots; no generated selectors; TYPE is the only generation; `DONE` ≠ verified success | solari-reflex (Jev); jev-ultrafast (Jev); gliner2-ultrafast (GLiNER2); laya-mind2web (Laya, DOM indices); cua-s1 (option-attention fill/check/click/skip; not TypeSafe Jev; source-only); Stagehand experimental Jev (harness; draft #2951–#2955); **ego-jev** (ego-lite indexed table; operation+target; `--until` in code) |
| Harness pick-and-copy extract | Choice among a11y candidates; completion Noul | Schema plan + validation gate in code; screenshot always LLM; LLM fallback; pick ≠ replacement | Stagehand #2955 (`off`/`judge`/`pick`; 37/75 no-LLM ~0.5s vs 4.37s *their* card) |
| Specialist form S1 (plan ≠ execute) | Option-attention among observed elements | Dry-run default; snapshot-bound tokens; reobserve; submit opt-in; fail-closed checkbox/fill | cua-s1 (`cua-s1-form-v0` profile; no weights this pass) |
| Hybrid local decide + remote fill | Local encoder scores observed controls | Code owns actuators; remote OpenAI-compat helper writes field text only | gliner2-ultrafast (GLiNER2 local + Mercury 2.5 default) |
| Dataframe semantic columns | Noul / Choice / Score per row; full `p__` | pandas/Polars, indexes, never silent renormalize | jevpandas; jevframe (PyPI + Polars) |
| Route ≠ memory | Intent Choice before a turn | Config + flat tools on easy routes; memory stays on for hard ones | jev-hermes |
| Advisory sidecar receipts | Typed answers as `no_action` evidence | Host routing / executor / policy unchanged | agent-workflow-typesafe-ai |
| Structure induction over a bag | Pairwise dependency Noul/Choice | DAG / scheduler in code | dag-jev (experiment) |
| Simulated world control vs content | Intent / page-type Choice | Generator writes documents; Zod + deterministic compiler; SQLite world | jev-agentworld-web-simulator |
| AST ∩ semantic lint | Typed questions on Tree-sitter units | Parser, selection, fail-on; does not execute scanned code | jevscan (`tenbin` owns the lint skill); jev-oxlint (skills→oxlint remainder; Phoenix experiment; not a hard gate) |
| Model router | Requirement Scores; policy in code | Eligibility, cost/quality/latency objective | routeKit; jev-adaptive-thinking (session-sticky first-prompt; fail-closed fallback) |
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
| Classify-first agent I/O | Relevance / typed questions on path/url/text | Hard envelope (50 / 60k / 2MB / public-IP); main LLM opens survivors; uncertain/errors/truncation ≠ irrelevant | jev-sift (MCP topology A; mocks ≠ accuracy; no LICENSE this pass) |
| Generative UI decide | Intent / layout Choice | Zod + deterministic compiler; model cannot add components | json-render + jev-agentworld-web-simulator |
| Robotics text-state | Choice on geometry-as-text | Code owns kinematics / Hz; two-call split; not pixels | MuJoCo showcase; jev-drone; Doom JSON. Drawing-pixel claim is not Archer |
| Draft-gate heartbeat | Quality Noul / Score | Fail-open / heartbeat on silence; missing verdict ≠ hold forever | jevable draft-gate fail mode; contrast Abide `<0.5` (edit proceeds) |
| Living class-pattern atlas | (not a model) | Cross-link exemplars; do not dump 342 titles | jevable.com (342 is *their* count; JSON-LD first page 36) |
| Verbatim session recall | Noul "still live for this task?" | JSONL ledger; constraints/corrections always-keep; fail-open dump | carryforward (9×3 hint, not proof) |
| Pre-exec tool gate | allow / block / review | Permissions, arg validation, transaction limits in code; timeout stops | toolgate (72-case synthetic, not independently annotated; Jev ≠ authorization) |
| Capability kernel | parallel hazard Nouls (sensor) | Closed action space; canaries/placeholders; BLOCK/ASK/ALLOW in `policy.py`; secrets never in the agent | interlock (ring 0 vs LLM ring 3; type-safe ≠ correct; 38-case local-judge set, not a blind paper). Distinct from toolgate |
| Typed control plane around an LM program | classifier over a closed ontology | Ontology validation, security override, confidence, state machine, tool allow-list in code; DSPy drafts AFTER route+action | jev-dspy-control-plane (OpenJEV / DSPy / JSON Schema share ontology; offline heuristic ≠ quality) |
| Engine owns truth / Jev owns judgment | severity / error-class / interrupt Noul+Score+Choice | Engine eval/lines/swing; templates + capped writing model; silence is a feature | game-coach (Wave 0 PRD; Stockfish WASM; GPL-3.0; anti-soundness-theater with egma attention≠correctness) |
| Human-confirmed OS kill | Stop / Keep / Your-decision Choice | Identity re-check; shields override; mapped explanations; TCP only | port-cleanup (conf ≥ 0.8 for kill recs; tiny pidfd-less race) |
| Native-probability calibration arena | noul/choice/score on analytic worlds | Oracle stub; Brier/ECE/reliability/risk-coverage; fan-out batches | jev-arena (live 145 noul Brier 0.0059 / ECE 0.0620 *theirs*; overconfident in low bins). Fan-out suite: jev-sonar (heatmap-as-policy); jev-vickrey (Jev never bids); jev-bracket (Brier vs Elo; live trailed Elo) |
| Meaning-as-spec UI test | pick among observed controls | Playwright acts; lockfile replay; refuse below 0.6 | jevcumber (.feature only; no step glue) |
| Conceptual PR labels | type/area/size Choice | Fixed taxonomy; never invent names; security/breaking never auto-removed | jev-pr-labeler (size = conceptual scope, not line counts; 0.75 abstain) |
| Healthcare S1 + S2 | NEWS2 remainder / med recon / inbox route | Code owns NEWS2, recon, routing; S2 blinded review | explore-typesafe-ai (synthetic FHIR; not clinically validated) |
| Public judgment wall | Six parallel questions (yes/no/depends, safety, mood, topic) | Policy-in-code; allowlist; p≥0.6 block; cost-to-1M from tokens | ask-jev-ai (license null; no-key UI says Jev offline) |
| Meaning-search without embeddings | Packed parallel relevance; two-stage outline→zoom | Keyword still wins exact strings; finds, does not explain | jevgrep (79% top-5 vs BM25 40% / grep 20% on stripped repos) |
| PR attention ≠ correctness | P0/P1/P2 attention | OpenAI writes deltas; alwaysReviewPaths P0; incomplete never P2 | egma-ai/jev-reviewer (**not** choxos pointer-not-generator) |
| Skills → oxlint | Remainder Noul/Choice after AST/precheck | Guidance whole-file in state; survey/calibrate/propose; not a hard gate | jev-oxlint (Phoenix fixtures; experiment; tenbin owns lint skill) |
| Session-sticky model route | First-prompt Choice | Lock for session; fail-closed declared fallback | jev-adaptive-thinking (license null; same family as routeKit) |
| Measured RAG rerank | Relevance vs a generative reranker | Evidence set / retrieval order on error; name the no-RAG arm | Jev-RAG (one-run ≥70%/72% vs Spark rerank; full-context Spark still faster) |
| Decide→policy→LLM leftover | 8 typed questions; shared Answer schema | auto / review / llm in code; Noul 0.5 never rounded; Score conf 0.0 never acted on; injection always review | jav-email-cascade (license null; mock gen-json flat-confidence is *their mock*; ~$0.034/1k *theirs*) |
| Domain specialist LoRA | soft-target Choice on independent gold | Threshold/deferral/EU in code; hosted few-shot when only argmax | Domain-jev-maker (CLINC labels, not Jev teacher-copy; KL 0.168 vs 0.580 banking *theirs*) |
| Wire-compat encoder backend | choice / score / noul on GLiFormer-400M | typesafe-sdk `base_url`; T=3.2; isolate nouls; tokens ≠ Jev billing | jeff (license null; ~$2.6 vs $15.6 L4 HTTP ~6×; A10G direct ~$0.65 ~24×; AG News 75.5% vs 90.5% *theirs*; not a Jev replica) |
| Loopback System One gateway | pass-through of whoever answers | Policy auto / prefer-local / prefer-hosted / local-only / hosted-only; credential from env never config; no weights | sysone (MIT; early; not a model) |
| ORDER BY ranking measurement | pairwise inversion / Score ordinality / ties | Gate SQL on results.json; secondary key on two-decimal ties; measure request shape | jev-orderby-bench (six gates pass; Score 0.143 weak link; 53-way 0.99 tie; recodelabs batch-40 fails ranking) |
| Closed-vote CU (no planner) | Choice among code-built options; done / off-path / next | Fact register; verify/undo; type without generation; irreversible risk never default | JevOnly (Apache-2.0; 11 steps / 43 calls / ~$0.014 / 17 s *theirs*) |
| Host-owned System One product | Choice among live typed actions | Host handlers, permissions, validation, state; prove writes from server state; p ≥ 0.7 default | waymode (MIT; 24/26 + 34/36 *theirs*; not on npm; not a self-driving proof) |
| OMP/pi acceptance + route | Choice `{accepted, rejected}`; topology/tier Choice | Fail-open missing Jev (`confidence: 0`); out-of-set answers → default | omp-jev-extensions (MIT; contrast pi-jev-approver fail-closed) |
| OMP prompt suppression | Parallel verdict + severity + in-scope | Operator owns presets; plugin never self-tunes; host deny fires first; agent prose withheld | omp-greenlight (MIT; 1,013/10; default 40.9% / 0 of 94 *theirs*; not a sandbox) |
| Pre-agent skill intervention | Relevance/confidence over authorised candidates | Code owns catalog/policy/grants; Jev never grants access; foundation-only on failure | skill-broker (**Hypothesis / outline**; not a production recipe) |
| Eval-instrument audit | Accuracy / ECE / blank lean / rewording of a Jev question | Check data/scorer/claims; 99 of 189 findings against itself | dinostomp (README Apache-2.0 / GitHub NOASSERTION; `dinostomp jev`; ECE 0.062 *theirs* on 24 examples) |
| Constrained optimizer + S1 features | task / exactness / external-evidence | Controller owns SLO/quality floors; fail-open local features; exactness never overrides capability | slo-router (license null; p95 **77.93 → 490.38 ms** same routes *theirs*; 3/8 label disagreements did not change routes; eight-row demo is not a benchmark) |
| Effect-based shell gate | Choice allow/deny + nine independent risk Nouls | Fast-allow/deny <1 ms; operator-owned minConfidence/riskThreshold; fail-closed | construct-auto-classifier (Apache-2.0; Jev **0** dangerous / 975; every chat model leaked 16–104; privilege ≠ verdict) |
| Attention filter / human-review VOI | Per-file need-a-look / kind / debris Nouls | Never blocks the agent; never edits; never green unless sure | jev-lens (MIT; `JEV_LENS_GREEN` 0.9) + jev-lens.nvim (MIT; popup only, no key). Distinct from jev-gates |
| Evidence-packet explorer | Rank BM25 shortlist; packet source_of_truth / tests / callers | Index once; agent still reads cited files; read-only | jev-semantic-explorer / jevex (1/8→6/8 n=8 *theirs*; HitFile 0.233 diagnostic) |
| Meaning-grep | Per-line Noul; AND/OR/NOT in code | Thresholds / `--level`; JP↔EN; name collision with Semgrep SAST | jev-semgrep (MIT LICENSE; 0.94/0.98 *theirs*) |
| Active-learning triage | Confidence routes accept / teacher / human | Soft-label full distributions; real outcomes stay training targets; do **not** distill Jev as teacher | jev-triage (MIT; ~68% ceiling anti-pattern) |
| Evaluation-model-first SDK | predicate / classifier / rubric as data | check / evaluate / filter / partition / rank; cancellable; never auto-retry | sysone-help/sysone (MIT TS; first adapter Jev via Vercel AI Gateway). **Not** hraness/sysone (loopback gateway) |
| Evidence-gated question pack | accuracy / ECE / cost / latency on a pinned version | Pack is `provisional` until evidence.md; `unknown` mandatory | jev-packs (CC0; nine verified *theirs*; jevassert 404 this pass — runner not released) |
| Runtime authorize (evidence ≠ authority) | Six narrow semantic Nouls | RBAC/schema/limits in code; positive p never overrides a hard fail | actiongate-jev (Apache-2.0; slogan: Jev supplies evidence, code owns authority; 500-case is label-baseline, not accuracy) |
| Ranking ≠ calibration | AUC vs ECE/Brier vs human rates | Recalibrate on labelled domain data; do not threshold raw p | does-jev-confidence (8,000 judgments; stated ~75% vs human ~10%; ~96% ECE removed) + jevcal (~100 rows) |
| Hot-click CU (indexed viewport) | operation + per-op target in one request | Code owns observe/execute/stale-ref/loop/`--until`; text model only for type; never guess fill | ego-jev (MIT; HN 4.9s vs 9.7s / wiki 5.4s vs 10.1s *theirs* n=3; not a bench). Cousin of jev-ultrafast |
| Framework-agnostic compact + gate | keep/drop per message + Foreman Nouls | Pins/dedup/regex floor in code; never rewrite; compaction fail-open if Jev down; safety fail-closed | jev-compactor (MIT; 64.5% / 366ms / $0.0004 / 0 hallucinated / 4 of 4 *theirs*, one session). Claude Code: fast-jev-compaction; OpenCode: fast-jev-opencode |
| Local-rules-then-remainder feed | four remainder Nouls after `rules.js` | Collapse not delete; auto-hides need human confirm before they become examples | x-reply-filter (MIT; 3-sample e2e 0.90/0.93 vs 0.08/0.10). Cousin of bohutang/sift |
| Control-plane combinators | Then / Gate / Vote / Cascade / Weighted over Choice/Score/Noul | AND/OR aggregation stays in code (do not multiply); trace is the oscilloscope | decision-combinators (TS; README MIT / GitHub license null; no measurements). Not a new Jev API |
| Skill-library VOI | two-pass Choice then fit Nouls; none-of-these | Hook fail-open; Quill prefilter >254; advisory; local replay | skillranker (Rust; 52★; MIT + rider / GitHub NOASSERTION). Correction vs §7: hook is not fail-closed |
| Receipts-not-leaderboard map | hold vs break with API receipts | Schema-valid ≠ correct; retrieve first | jev-capability-atlas (10★ this pass; axis already §49; this hour is the eval-integrity cluster) |
| Jev vs thinking-budget small models | 100 four-choice tasks × 3; freeze questions | Attach the thinking condition; exploratory not preregistered | jev-frontier-100 (MIT; Jev 77.0% vs Qwen3.5 4B/2048 96.7%; 4B off 56.0%). Not a ceiling |
| OOD calibration / AUC ≠ ECE | ECE with noise floor; refit T by type | Calibrate per question; do not threshold `confidence` | jev-ood-calibration (MIT; 900 tickets; ECE 0.107 = 4.4× floor; priority 44.7% / mean p 0.74 / T 3.40) |
| Replayable evidence≠authority gate | policy first; Jev remainder; allow/review/deny | Missing Jev → Review; hard denials stay hard on replay | turnstile (Apache-2.0; experimental alpha; no npm). Actiongate-class clone |
| MLX one-pass schema→JSON | per-field probs in one forward pass | Softmax ≠ Noul; no local leaderboard yet | jevmlx (MIT; 28★; Apple Silicon replica economics). Distinct from system-one-benchmark Harbor table |
| TLA+ consensus around a noisy oracle | five paraphrased votes; stability gate; quorum 3/5 | Escalate when unstable; TLA+ owns the protocol; never confidently wrong | jev-labs (MIT; 1,080 golden 0 wrong *theirs*; TLC 1,049,750 states / 0 errors; synthetic, not clinical) |
| Advance / coverage ledger | Strike fills Candidates; Seal advances | coverage.path auto\|code\|human\|escalate visible; Effects locked while escalations open; mint ≠ product brain | seal (MIT; BEYOND-JEV.md; zero runtime deps) |
| Sureness over a probability vector | max_prob / margin / entropy / gini / perplexity | Bands are policy; Choice confidence = max_prob (generous) | how-sure-is-jev (MIT; zero-dep; 60-q reverse-engineer) |
| Scored Jev-class bake-off | Capability / Speed / Cost → Main Score | Calibration reported, **not scored**; native vs verbalized; partial runs not ranked | jevbench v1.1 (MIT; unofficial; Jev 1.13.0 Main 87.6 *theirs*) |
| Pre-review typed PR gate | should_review / risk / route / touches_secrets | Operator-owned thresholds; secondary LLM only on human-review + elevated risk | ci-gatekeeper-bot-jev (`package.json` MIT / GitHub SPDX null; 504–629 ms *theirs*) |
| Codex MCP host adapter | select_capability / search / triage Nouls | Caller supplies catalog; lexical fallback; scores advisory; ranking unbenchmarked | jev-in-codex (MIT; experimental MVP). Distinct from jev-routing (not MCP) |

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
not copy the inherited vs-Jev table. **Complete browser
int8 cousin (distinct):**
[`gqgs/laya-onnx`](https://github.com/gqgs/laya-onnx)
(496.8 MiB; conversion smoke, not accuracy; `notes.md`
§64). **Local ModernBERT approximation, not
equivalence:**
[`kunchenguid/local-jev`](https://github.com/kunchenguid/local-jev)
— distinct from jev-local stub and jeff. GLiNER (locate) / GLiClass (categorize) /
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
