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
| Actuate an observed browser control | **Fail closed** (code validates the node) | Freshness / visibility / disabled / occlusion in code; model never emits selectors (`gliner2-ultrafast`, jev-ultrafast, solari-reflex). `DONE` does not authorize "success". Cua-S1: dry-run default; `execute`/`submit` opt-in; fail-closed unknown checkbox; fill execution fails closed without token `set_value`. Stagehand: same; LLM fallback when Jev abstains. **typesafe-computer-use:** AX press when the item came from AX; mouse fallback; off-screen refusal is a no-op |
| Ship a screenshot to frontier for the *decision* | **Fail closed** (OCR+AX text-state) (`typesafe-computer-use`) | Decision never sends pixels. The one-shot **answer** reader may receive the capture — that is a writer packet, not the Choice. Not omni. Skip Archer |
| Offer overlapping CU action options | **Fail closed** (exclusive set) | Confidence measures concentration; overlap reads as doubt (*theirs*). wellposed cousin. Split `kind`/`item`/`site`/`offscreen` |
| Treat $0.0002 / 155× as a Harbor score | **Fail closed** (one screenshot) | Same screenshot, one decision each *theirs*. Dates.py caveat. Re-measure on *your* taskset |
| Treat `--min-confidence` 0.4 or post-type Noul 0.5 as Harbor τ | **Fail closed** (still soft) | Product copy. schema-safe ≠ correct. Mouse-slam / Accessibility deny are the exact stops |
| Collapse typesafe-computer-use into jev-ultrafast / cua-s1 / camoufox | **Fail closed** (qualify the host) | macOS OCR+AX + hosted Jev. **≠** browser DOM **≠** Cua-S1 **≠** OmniParser loop **≠** Camoufox clone |
| Treat AX as the sole source / mix off-screen into visible items | **Fail closed** (bonus source; separate question) | Spotify 0 *theirs*. A mouse click would land on the wrong pixel |
| Treat `done` as verified success | **Fail closed** (loop termination) | Writer answer is a reader packet. Dry-run prints no answer |
| Ship a waveform / screenshot to Jev because the UI is voice | **Fail closed** (transcript text-state) (`jev-voice-browser`) | ASR is the producer. Jev sees the schema, not audio. Compose with OCR §81. Skip Archer |
| Treat spoken "confirm" as authorization | **Fail closed** (convenience, not a guarantee) | README *theirs*. Anyone who can reach the control port drives the browser. Judgment ≠ permission |
| Truncate free-text on a closed-set wait | **Fail closed** (wait policy is VOI) | Closed-set may act on a partial; search/type wait for final or 600 ms silence *theirs* |
| Call a second model to pick among numbered overlays | **Fail closed** (UI number is exact) | Spoken digit copies an id code already holds |
| Quote 27/27 or $0.0002/call as a Harbor score | **Fail closed** (fixtures) | Integration on captured pages *theirs*. Re-measure. 0.5 / 0.55 / 0.6 still soft |
| Collapse moritzkremb/jev-voice-browser into jev-voice-control / nikolas-j / typesafe-computer-use | **Fail closed** (qualify the host) | Headed Chromium + Web Speech + hosted Jev. **≠** macOS stub **≠** 0★ namesakes **≠** OCR desktop |
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
| Allow a proposed shell command | **Fail closed** on missing / low-conf / high-risk / failed call (`construct-auto-classifier`) | Privilege ≠ verdict. Landed-script trust is a merge-gate receipt, not a name. Headless escalation is deny-and-report, not auto-approve. 0 dangerous / 975 *theirs* |
| Tell a human the agent work is green / skip | **Fail closed** to "look" unless sure ([rashedInt32/jev-lens](https://github.com/rashedInt32/jev-lens)); **never block** the agent | Attention filter / VOI, not a permission gate. Never edits files. Distinct from dizk/jev-lens (pre-send views) and from jev-gates (stops writes) |
| Endorse a question pack | **Fail closed** until recorded evidence (`jev-packs` + landed `jevassert`) | No numbers, no `verified`. Pin model version. Abstention/`unknown` mandatory. `check` runs **offline from recordings** (exit 0/1/2) |
| Treat a public arena as a leaderboard | **Fail closed** until measured findings (`chenmingtang830/jevarena`) | Failure-finding, not crowning winners. Distinct from `meetr1912/jev-arena`. Harness ≠ findings |
| Certify a model "unbiased" from one BBQ run | **Fail closed** (do not) (`jev-bbq-experiment`) | 97.28% / bias 0.04/0.34 *theirs* is one frozen English/U.S. QA template. Not hiring/lending/healthcare |
| Let the LLM plan *and* fill in jeffrey | **Fail closed** to the split | Jev owns next-tool/progress/risk/done; LLM only fills args. Risk ≥ 0.5 pauses mutating tools |
| Fail a build on a missing jevlint verdict | **Fail open** (no verdict ≠ clean) (`mizchi/jevlint`) | Failed request never reads as a clean repo. Distinct from huntedman/JevLint |
| Skip generative review of a safety-escarpment hunk | **Fail closed** (always keep) (`prune-review`) | Concurrency/auth/a11y/startup stay in the packet regardless of Jev. Cost 1.18% with 305% outlier *theirs* |
| Treat empty intent-search as VERIFIED | **Fail closed** to UNKNOWN (`jev-intent-review`) | Empty search ≠ proof. VERIFIED is only as complete as the search |
| Treat GLiNER2 spec JSON numbers as measurements | **Fail closed** (spec-only) (`Jev_from_GLiNER2`) | Design for implementation; no service, no training. Interface ≠ replica. Distinct from jeff |
| Treat grande/laya-jolt/JEV-CPU/local-jev softmax as a Noul | **Fail closed** until calibrated on *your* labels | Packed-vs-separate / byte-parity / CPU logits / ONNX NLI are substrates. local-jev `confidence` omitted; done 30% vs Jev *theirs* |
| Forget user constraints after compaction | **Fail closed** to persisted structured state (`pi-heed`) | Jev never writes policy. Fail-open if Jev is down. Shadow default |
| Treat capability canaries as a quality headline | **Fail closed** until stages finish (`jev-judge-bench`) | SLA-150 frozen; invalid = FN; 21 offline tests; canaries 5/5–10/10 *theirs* are availability. **No quality result shipped.** Distinct from jevarena / jevbench |
| Treat cookbook sample scores as benches | **Fail closed** (do not) (`jev-cookbook`) | 16–36 handmade items; authors say not benchmarks. 425 calls / $0.015 *theirs* is cost/latency, not F1 |
| Click a GUI target below threshold | **Fail closed** to `unknown` (`pi-jev-control`) | Never force-click. Compaction never modifies the on-disk session |
| Treat a missing Vercel `confidence` as vendor Noul | **Fail open** to margin + a lower bar (`jev-use`) | First loop 17/20 escalate then 0/20 at 0.4 *theirs*. Distinct from jev-ultrafast |
| Sell jev-gpt as a product writer | **Fail closed** (architecture demo) | ~400 calls / 75 s / 2¢ *theirs*. The model never free-generates. Distinct from jeffrey pick≠fill |
| Endorse competing NAR from README badges | **Fail closed** until like-for-like + receipts (`openJev-verdict-2.0`) | Open PR #1: throughput≠latency; Laya gap inside CI (parity); correctness-head ECE ≠ distribution ECE. ≠ IamBusy/OpenJev |
| Treat an empty compaction-proxy slogan as a product | **Fail closed** (empty repo) (`IPECTER/jev-context-pruner` **and** `IPECTER/jev-runway`) | context-pruner 409 empty; jev-runway LICENSE-only (created≈pushed 1s). Sibling of fast-jev-compaction / jev-compactor / dizk/jev-lens — no files |
| Threshold chakuho softmax as a Noul | **Fail closed** until labelled calibration (`chakuho`) | Coverage is format-mass, not correctness. 8B stays coverage 1.00 while `__none__` collapses. Arithmetic stays in code. 503 is could-not-judge, never "no" |
| Treat jevinf speedup as a quality headline | **Fail closed** (argmax-parity only) (`jevinf`) | 2.57×/2.27× at 100% argmax *theirs*. MPS only. Wire-compat ≠ TypeSafe replica |
| Collapse typesafe-elixir-sdk into dannote/jev | **Fail closed** (different jobs) | HTTP client over Req ≠ OTP peer GenServer. Code still owns the `cond` |
| Round a commitjev middle band to pass/fail | **Fail closed** to `"review"` | ≥0.65 is the only verdict. Nouls decide; Choice is headline. Regex proves literals. Hook fails open on instrument failure |
| Treat hermes-plugin-jev as TypeSafe Jev | **Fail closed** (identity) | Live backend is Agnes 3.0 Flash chat-completions. Distinct from hermes-jev-router |
| Confuse pi-jev-compact with pi-jev-compaction | **Fail closed** (qualify owners) | compact = Pi summarizer replacement (verbatim keep/drop). compaction = fast-jev-compaction cousin |
| Trust an English Laya checkpoint on non-English | **Fail closed** to the multilingual checkpoint / script router (`laya-multilingual`) | Khmer 0.000 acc at 0.952 confidence *theirs*. Mean conf never < 0.885. Gating cannot catch it |
| Threshold schema-scorer peaked p as frequency | **Fail closed** (ranking ≠ calibration) | Grouped softmax trained on one-hot. Hub MIT; GitHub 404 |
| Ship jev-cli as if v1 existed | **Fail closed** (not ready) | README: commands not implemented. Crate: not ready. Distinct from jevql |
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
| Reinspect a turn's risk from a Stop hook | **Fail open** (Claude finishes anyway) (`jev-preflight`) | Attention redirect, not a merge blocker. assist = one reinspect. 0.85 uncalibrated. Distinct from rashedInt32/jev-lens |
| Shrink a tool result before first send | **Fail closed** to full text for *code* unless confident (`dizk/jev-lens`) | Compress-before-first-send. Post-send prune cost 17% more *theirs*. Distinct from rashedInt32/jev-lens |
| Depend on the agent calling `recall` | **Fail closed** to a SessionStart hook (`carryforward`) | tools≠use. 0/4 *theirs*. MCP sitting there is not enough |
| Compact observational history | **Fail open** (failed Jev does not drain the buffer) (`pi-observational-memory-jev`) | Keep/kind only; verbatim ledger; model-free compact. Do not install beside Alvar `/om` |
| Actuate a lock / heater / smoke alarm from a Noul | **Fail closed** (do not) (`HA-Jev`) | Physical-world S1. Sensors and automations yes; safety actuators no |
| Skip an expensive chat completion via same-intent cache | **Fail open** (call upstream) (`jevcache`) | False HIT serves the wrong answer. 0 FP / recall 0.38 *theirs* n=100. Stream/tools/multimodal bypass |
| Strip the skill roster / recommend none | **Fail open** (Pi keeps listing; no-op without a key) (`pi-jev-skill-suggestion`) | Tool mode is tools≠use: the agent still has to call `skill_suggest`. Auto mode pays a Jev call every prompt |
| Return control to the LLM from a typed baton | **Fail open** (typed escalate, never a blocked agent) (`jev-handoff`) | Gate `allow` never grants. Vercel drops confidence — margin fallback is not calibrated |
| Skip the next Hermes main-model call | **Fail open** (continue to the LLM) (`hermes-jev-router`) | WHETHER/HOW/WHAT. Skip-next needs a core patch. Aggressive defaults. License null |
| Badge a feed item skip / save | **Fail open** (show `?`) ([ThinkyMiner/Winnow](https://github.com/ThinkyMiner/Winnow)) | Worth-your-attention VOI. Distinct from kevinpita/winnow. Templates never prose |
| Fail CI on an adversarial browser finding | **Fail closed** only high conf **and** high severity (`browser-jev`) | Sample from the distribution, not argmax. Code-only checks first. Visual blind. Baseline before trusting |
| Treat `/v1/decide` or SemIf `/v1/systemone` as hosted Jev | **Fail closed** until you name the scorer (OpenJev / semif-serve) | Wire-compat ≠ replica. OpenJev is not TypeSafe. Runoff is a product, not a softmax |
| Collapse conflict and ignorance into one Noul | **Fail closed** to a named Choice escape (`jev-typed-evaluation-collapse`) | Noul 0.50–0.57 vs 0.46–0.48 *theirs*. Binary Choice without escape is lexically biased |
| Treat a security-scan / prepared review / guardrail demo as policy | **Fail closed** (they are sensors) | rh-guard owns reward-hack. Reviews never stop commands. TeoMastro numbers unpublished this pass |
| Drop a meaning-grep line | **Fail open** as ranking (`jev-semgrep`); keyword still wins exact strings | AND/OR/NOT over line Nouls. Japanese meanings noisier near threshold |
| Treat classifier.dev as a chatbot / agent hook | **Fail closed** (it is a classification API) (`classifier-dev`) | Public contract is label + calibrated confidence; batch `{id,text}[]` ~1000. Distinct from ask-jev-ai's six-question wall |
| Escalate every multi-label answer on `tier: smart` | **Fail closed** (do not) | Re-judging made it worse (23 s). Smart re-asks **single-label <0.7** only. 0.7 is *theirs*, not a class constant |
| Quote classifier.dev numbers without `eval/README` | **Fail closed** (do not) | `/benchmark` is tracked `vs-jev.json`, not transcription. n=7 train-on-test; ~0.03 is a coin flip |
| Serve a silent fallback as the advertised model | **Fail closed** (mark `FALLBACK`) | granite-4.0-h-micro F1 **0.546** vs advertised ~**0.800** *theirs* for weeks. rh-guard owns the eval-integrity gate; this is the lived cousin |
| Treat choxos/jev-reviewer as egma-ai PR attention | **Fail closed** (different products) | Systematic-review pointer ≠ code-diff attention. Always write **choxos/jev-reviewer** or “systematic-review Jev Reviewer” |
| Let Jev write the quote / skip *Not found* | **Fail closed** (copy verbatim; *Not found* is an answer) (`choxos/jev-reviewer`) | Pointer-not-generator. Noul ≥ 0.5 *theirs*. Unclear keeps closest lines. No paraphrase invent |
| Auto-accept an unchecked extraction quote | **Fail closed** (human tick is the product) | Checked answers are never overwritten by a reworded question. Jev is SENSOR; the reviewer is the constraint |
| Collapse githubnext/localjev into kunchenguid/local-jev | **Fail closed** (qualify owners) | Bun Chat Completions bridge ≠ ONNX ModernBERT approximation. Always write **githubnext/localjev** |
| Treat githubnext/localjev JSON probs as OpenJev logits | **Fail closed** (wire-compat ≠ logit-equiv) | razorback16 structured-read + logprobs vs prompted JSON → validate/retry → normalize + entropy confidence. SDK drop-in is the *wire* |
| Threshold LocalJev self-reported p as a calibrated Noul | **Fail closed** until labelled calibration on *your* workload (`githubnext/localjev`) | README: evaluate before consequential use. Bake-off: do not treat outputs as calibrated (wrong-BoolQ high conf → large NLL). JSON-valid ≠ picked-right |
| Swap LM Studio in and call it OpenJev parity | **Fail closed** (runner gap) | DiffusionGemma load still open (mlx-engine#336 / bug-tracker#2037 *theirs*, 18 Sep 2026). Chat Completions keeps the prompted-prob path. Structured-read primitives are the path |
| Collapse NandhaKishorM/laya into Hub-only / localjev / TypeSafe drop-in | **Fail closed** (qualify the face) | GitHub/PyPI packaging of Hub Laya; **≠** new species; **≠** githubnext/localjev; **≠** `/v1/systemone` SDK drop-in. Always write **NandhaKishorM/laya** |
| Treat typed-decisions 0.766 as zero-shot | **Fail closed** (fine-tune on that split) | Base ckpts 0.362 / 0.342 vs majority 0.461 *theirs*. Fast base to specialise |
| Hard-act at Laya conf 0.85 | **Fail closed** until Harbor cal on *your* labels | README recipe. Khmer 0.000@0.952 already proves gating cannot catch script OOD. 0.85 is *theirs* |
| Quote the vs-Jev table as independently measured here | **Fail closed** (third-party unpublished-here) | No TypeSafe API access; sample sizes/prompts differ; Banking77 72 vs 77 labels |
| Treat post-T ECE 0.081 as raw ECE | **Fail closed** (name the temperature) | Raw typed-decisions ECE 0.213 vs Jev 0.144. 0.081 is after domain T fit |
| Treat the @airesearch12 census tweet as a scored bake-off | **Fail closed** (it is a list + a promise) | ≠ [jevbench](https://github.com/fstandhartinger/jevbench) v1.1. Watch [jev-models](https://benchmarkheaven.com/jev-models); do not paste live ranks into the census card. **≠** jev-judge-bench / jevarena |
| Collapse GLiNER2 or routers into NAR / TypeSafe clones | **Fail closed** (class-boundary) | GLiNER2 locates/categorizes; Succinct 14M / jev-model-router / Director / Loki route. Same job family ≠ replica. Needle 3 is function-calling (already §67) |
| Treat an incomplete openjev list as our watch being wrong | **Fail closed** (census lag) | Laya, githubnext/localjev, kev, TypeAR, openvons, chakuho, jevinf, grande, laya-jolt, blackwood, classifier-dev missing. Lesson, not a dunk |
| Quote tweet likes/views as quality | **Fail closed** (ephemeral) | SIGNAL ~417/9/3; this pass 564/15/5. Do not copy Stripe |
| Mix v1.1 Main 87.6 with v1.2 Score 75.3 as a drop | **Fail closed** (not comparable) | Different tiers and scoring *theirs*. Cal now ON the composite. Keep v1.1 as historical (`notes.md` §67, §78) |
| Treat 75.3 as a class ceiling without the four axes | **Fail closed** (geo-mean product) | I/C/S/K 25% each. Weak axis dominates. SemIf −0.7. Weighting views reorder ranks |
| Treat Luna I=96.8 as rank #1 | **Fail closed** (Cost 28.2 → rank #7) | Accuracy cannot buy back a weak axis. DeepSeek C=96.7 is rank #11 |
| Ignore the ×2 latency assumption / est. costs | **Fail closed** (Harbor honesty) | Self-host/demo ×2 (+0.15 s) is an **assumption, not a measurement**. Many costs est. from OpenRouter/DeepInfra size-class. Production APIs unadjusted |
| Treat Qwen3.8 27B as Archer | **Fail closed** (official Qwen / Chutes TEE) | Partial, Cost 0 from price, hard 21.4%. Archer still Watch |
| Treat Laya absence as a quality verdict | **Fail closed** (gap, not a named exclusion) | Absent from the scored table **and** from the named exclusion list. Completeness ≠ dunk. GLiNER2 is mapping-excluded *theirs* |
| Collapse instruction models into NAR clones because they share the table | **Fail closed** (class-boundary) | Luna/Gemini/DeepSeek/Qwen3.8 are JSON-schema instruction models. Needle 3 is function-calling (C none → 0). OpenJev on board = razorback16 ≠ IamBusy `/v1/decide` |
| Treat the geometric mean as a natural law | **Fail closed** (weights are a choice) | Limits *theirs*. Balanced no-cal puts SemIf #1; Emphasis Cost puts system-one-open #1 / Jev #5 |
| Re-card localjev / classifier.dev / Laya / choxos / census / v1.2 because they reappear on the hourly | **Fail closed** (already folded) | Apply the five as a recipe (`notes.md` §79). Do not dump the hit list again |
| Hard-gate a Noul as a PR merge / quality seal | **Fail closed** (soundness theater) | Soft Noul attends or escalates; an exact envelope proves the irreversible act. [totally-tim/jev-gate](https://github.com/totally-tim/jev-gate) (0★; MIT; Action/CLI/OpenCode) and [connectedGraph/claude-jev-warden](https://github.com/connectedGraph/claude-jev-warden) (1★; MIT; “Art Director Warden”) are this hour’s skip with that risk. **≠** [vinilana/jev-gateway](https://github.com/vinilana/jev-gateway), [MongLong0214/jev-gate](https://github.com/MongLong0214/jev-gate) (model routing), [SargeDev/jev-gate-student-b](https://huggingface.co/SargeDev/jev-gate-student-b). Cousin: ci-gatekeeper (cheap typed pre-review, operator-owned). Attention filter never blocks ([rashedInt32/jev-lens](https://github.com/rashedInt32/jev-lens)) |
| Stall S1 waiting for S2 / let S2 fly | **Fail closed** (S1 keeps the stick) (`jev-reflex-autonomy-lab`) | Escalate-under-threshold **without blocking**. S2 is one-use advice. Distinct from classifier.dev smart re-ask (that path *does* wait). `notes.md` §80 |
| Treat purple S2 arrival as consumed guidance | **Fail closed** (log consumption) | Purple confidence = that Jev decision used returned S2. Purple S2 bar = arrival. Red = fail. Arrival without a later purple point is unused VOI |
| Collapse Local controller into githubnext/localjev | **Fail closed** (qualify the face) | Built-in **rule-based** reflex, no credentials. **≠** prompted-JSON Bun `/v1/systemone` **≠** ONNX ModernBERT. Always write **Local controller** vs **githubnext/localjev** vs **kunchenguid/local-jev** |
| Treat the 20% starting gate as Harbor τ / a flight interlock | **Fail closed** (still soft) | Selecting Live API sets 20% *theirs* and does **not** start a mission. schema-safe ≠ correct. Calibrate τ on *your* labels |
| Treat the seed as a deterministic async replay | **Fail closed** (geometry only) | Live latency still changes the trajectory. Seed repeats obstacle layout, not timing |
| Send pixels / planner prose into the reflex | **Fail closed** (text-state; no graphical input) | ARCHITECTURE *theirs*: no pixels to either provider; planner narrative excluded from Jev input; code never labels safest. Not omni. Skip Archer |
| Assume Jev confidence = selected probability | **Fail closed** (not assumed) | Application contracts ≠ TypeSafe SDK methods. Physics owns collisions. S2 never grants |

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
discriminates; never the reverse). `notes.md` §46. **Delta
(`notes.md` §80):** escalate-under-threshold **without stalling**;
telemetry marks when guidance was **consumed** (purple confidence =
that Jev decision used returned S2; purple S2 bar = arrival; red =
fail) — arrival ≠ used. **Local controller** is a built-in
rule-based reflex, **≠** githubnext/localjev **≠**
kunchenguid/local-jev. Live API is hosted `POST /v1/systemone`
`jev-latest`; selecting it sets a 20% starting gate *theirs* and
does **not** start a mission. Seed = geometry, not async replay.
No pixels to either provider. Confidence is not assumed equal to
selected probability. S2 never grants. 20% is still soft.
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
- **Sentence-as-rule lint (ast-grep × Jev)** —
  [`mizchi/jevlint`](https://github.com/mizchi/jevlint): matcher
  decides *which* code is looked at (silent miss); a sentence
  `ask:` decides whether it is a problem (loud). 13/15 1.00/1.00
  on their corpus; review mode 2 req / $0.00013. Fail-open no
  verdict. **Always qualify** vs huntedman/JevLint. Independent of
  eslint-plugin-jev (`notes.md` §70).
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
| Preference lint | Per-rule Score/Noul on a diff; or ast-grep subject × sentence | Rule text, linter for hard rules, bands + fail-open; matcher silent / Jev loud | jev-pref (contract), Abide (productized), huntedman/JevLint; **mizchi/jevlint** (13/15 1.00/1.00 *theirs*); if-ai (plain-English PR check, fail-closed on error); jev-marshal (Watch / empty repo) |
| Context / log prune | Per-line or per-block relevance; or a retention Choice + spans; or a Noul per stdout chunk; or keep/kind on a verbatim ledger; or pre-send views of a tool result | Always-keep set, recall keys; mutation envelope in code; shadow before replace; size/format envelope then Noul; archive dropped spans; kind-keyed topic files | jevprune, winnow; fast-jev-compaction / pi-jev-compaction / fast-jev-compaction-pi; gliner25-compaction; jev-pruner; **jev-compactor** (73% / 350 ms product-arm *theirs*); **dizk/jev-lens** (pre-send; 79% fewer tokens); **pi-observational-memory-jev** (keep/kind verbatim) |
| Exact hunk staging | Per-hunk include/exclude/mixed | `git diff`, atomic apply | git-jev-stage |
| Semantic `WHERE` | Noul/`jev_prob` over a row | SQL, indexes, LIMIT | **jevql** (CLI judges; vanilla Postgres never sees `jev()` — judgment outside the store); sqlite-jev / pg-jev (in-engine) |
| Formula / query embedding | JUDGE as a function | Spreadsheet/SQL engine | judge-sheets, jevql, sqlite-jev |
| Soft ABR / live encoder | Choice over a ladder | Probe × headroom, thermal, battery | bitrate-advisor |
| Voice → typed act | Choice/Noul on a transcript | ASR producer; macOS actions | jev-voice-control (README stub; §44) |
| ASR voice-browser CU (productized) | 9–11 questions on a partial transcript; pointer spans | Playwright; debounce; numbered overlay; spoken confirm still soft | moritzkremb/jev-voice-browser (MIT **103★**; `notes.md` §82). **≠** jev-voice-control **≠** nikolas-j **≠** typesafe-computer-use |
| Host-adapter routing | Choice next-tool + done-Noul | Shrink `tools[]`; compaction | jev-routing (not MCP; **delta:** Cursor Agent CLI / Devin CLI this hour); **jev-in-codex** (Codex MCP; ranking unbenchmarked; lexical fallback) |
| Multi-model route | Classify axes; policy maps | Escalation `if`, path regex | jev-claw, routeKit |
| Finish-line gate | Noul/Score/Choice on evidence | Deterministic shell checks first | hermes-jev-north-star |
| Home automation read | Choice/Score/Noul as a sensor | Automations, device I/O, daily budget; **not** locks/heaters/smoke | [HA-Jev](https://github.com/AboveColin/HA-Jev) (MIT; **17★**; confidence gating; Jev-gates-LLM examples) |
| Browser loop without generation | Action Choice over visible elements | Perception, constraints, click | lizard-agent |
| Screenshot / DOM candidates → Choice | Omni decide over letters code marked | Click/act in code; fail-open to specialist OCR | blackwood-rlcd (CC BY-NC; not Archer) |
| Android / macOS computer-use | Choice over prevalidated candidates | UI tree / AX / OmniParser; no generated coordinates | jev-mobile, jev-macos-loop |
| S1 reflex + optional S2 advice | Typed action Choice; planner one-use on low p; escalate **without stalling** | Collision, legality, physics; the stick stays with S1; S2 never grants | jev-reflex-autonomy-lab (experimental viz; **7★**; license null; `notes.md` §46 + §80) |
| Mixed-initiative consumption telemetry | Same Choice; mark when advice was *used* | Green = local context; purple confidence = consumed S2; purple S2 bar = arrival; red = fail | jev-reflex-autonomy-lab charts. Arrival ≠ used |
| Local controller vs Live API (reflex A/B) | Same questions; backend is rule-based vs hosted `jev-latest` | Physics/seed fixed; 20% gate still soft; credentials do not auto-switch | Harbor-adjacent of backends, **not** a scored bake-off. **≠** githubnext/localjev |
| Decision-as-business-tool | Named judgment; gate is part of the result | Registry, arithmetic, hard guards | jev-decision-layer (unofficial) |
| NL cases → checked e2e | Jev selects observed controls | Playwright expectations; PASS/FAIL/BLOCKED | jev-e2e (alpha) |
| Extractive quotes / pointer evidence | Per-sentence, per-line-id, or char-offset Noul/Choice | Verbatim join; place; `redecide` / CSV; model never writes the excerpt | testimonial-miner; jev-reviewer; gliner25-compaction |
| Structured observe → decide → act | Score / Choice among numbered a11y/DOM/OCR+AX controls | Guard check; deny-list absence; no screenshots **on the decision**; no generated selectors; TYPE is the only generation; `DONE` ≠ verified success | solari-reflex (Jev); jev-ultrafast (Jev); gliner2-ultrafast (GLiNER2); laya-mind2web (Laya, DOM indices); cua-s1 (option-attention fill/check/click/skip; not TypeSafe Jev; source-only); Stagehand experimental Jev (harness; draft #2951–#2955); **ego-jev** (ego-lite indexed table; operation+target; `--until` in code); **typesafe-computer-use** (macOS OCR+AX; hosted Jev; MIT **427★**; `notes.md` §81) |
| OCR+AX desktop CU (productized) | kind / item / site / offscreen Choices | Crop+tile OCR; AX bonus never sole; dates.py; writer only for free text; post-type Noul still soft | awlevin/typesafe-computer-use. 155× *theirs* one screenshot. **≠** jev-ultrafast **≠** cua-s1 **≠** camoufox |
| ASR voice-browser CU (productized) | intent / target / site / complete / is_command / destructive + span Choices | Web Speech producer; Playwright acts; numbered overlay; spoken confirm ≠ auth | moritzkremb/jev-voice-browser. 27/27 fixtures *theirs*. **≠** jev-voice-control **≠** typesafe-computer-use |
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
| Verbatim session recall | Noul "still live for this task?" | JSONL ledger; constraints/corrections always-keep; fail-open dump; **SessionStart hook** (tools≠use) | carryforward (9×3 hint; **0/4** recall *theirs*) |
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
| Effect-based shell gate | Choice allow/deny + nine independent risk Nouls | Fast-allow/deny <1 ms; landed-script trust; headless ≠ auto-approve; fail-closed | construct-auto-classifier (Apache-2.0; Jev **0** dangerous / 975; $0.047/1k; privilege ≠ verdict) |
| Attention filter / human-review VOI | Per-file need-a-look / kind / debris Nouls | Never blocks the agent; never edits; never green unless sure | [rashedInt32/jev-lens](https://github.com/rashedInt32/jev-lens) + nvim. Distinct from [dizk/jev-lens](https://github.com/dizk/jev-lens) (pre-send views) and from jev-gates |
| Evidence-packet explorer | Rank BM25 shortlist; packet source_of_truth / tests / callers | Index once; agent still reads cited files; read-only | [jevex](https://github.com/jimmyhealer/jevex) (rename of jev-semantic-explorer; n=16 160s→69s / $8.74→$3.13 / 16/16 *theirs*; keep n=8 1/8→6/8; HitFile diagnostic) |
| Meaning-grep | Per-line Noul; AND/OR/NOT in code | Thresholds / `--level`; JP↔EN; name collision with Semgrep SAST | jev-semgrep (MIT LICENSE; 0.94/0.98 *theirs*) |
| Active-learning triage | Confidence routes accept / teacher / human | Soft-label full distributions; real outcomes stay training targets; do **not** distill Jev as teacher | jev-triage (MIT; ~68% ceiling anti-pattern) |
| Evaluation-model-first SDK | predicate / classifier / rubric as data | check / evaluate / filter / partition / rank; cancellable; never auto-retry | sysone-help/sysone (MIT TS; first adapter Jev via Vercel AI Gateway). **Not** hraness/sysone (loopback gateway) |
| Evidence-gated question pack | accuracy / ECE / cost / latency on a pinned version | Pack is `provisional` until evidence.md; `unknown` mandatory; `jevassert check` offline from recordings | jev-packs (CC0; nine verified *theirs*) + **jevassert landed** (Apache-2.0; Action `@v0`). 2,990-case matrix: Jev/Sonnet 5 accuracy tie, Jev better calibrated 7/9, ~250× cheaper *theirs* |
| Runtime authorize (evidence ≠ authority) | Six narrow semantic Nouls | RBAC/schema/limits in code; positive p never overrides a hard fail | actiongate-jev (Apache-2.0; slogan: Jev supplies evidence, code owns authority; 500-case is label-baseline, not accuracy) |
| Ranking ≠ calibration | AUC vs ECE/Brier vs human rates | Recalibrate on labelled domain data; do not threshold raw p | does-jev-confidence (8,000 judgments; stated ~75% vs human ~10%; ~96% ECE removed) + jevcal (~100 rows) |
| Hot-click CU (indexed viewport) | operation + per-op target in one request | Code owns observe/execute/stale-ref/loop/`--until`; text model only for type; never guess fill | ego-jev (MIT; HN 4.9s vs 9.7s / wiki 5.4s vs 10.1s *theirs* n=3; not a bench). Cousin of jev-ultrafast |
| Framework-agnostic compact + gate | keep/drop per message + Foreman Nouls | Pins/dedup/regex floor in code; never rewrite; compaction fail-open if Jev down; safety fail-closed | jev-compactor (MIT; later product-arm **73%** / 350 ms / 4 of 4 *theirs*; 30–250× cheaper than shipped summarizers). Claude Code: fast-jev-compaction; OpenCode: fast-jev-opencode |
| Local-rules-then-remainder feed | four remainder Nouls after `rules.js` | Collapse not delete; auto-hides need human confirm before they become examples | x-reply-filter (MIT; 3-sample e2e 0.90/0.93 vs 0.08/0.10). Cousin of bohutang/sift |
| Control-plane combinators | Then / Gate / Vote / Cascade / Weighted + Router / Loop / Retry / Fallback / Memory | AND/OR aggregation stays in code (do not multiply); trace is the oscilloscope; Fallback is the fail-closed node | [jev-combinators](https://github.com/voidning/jev-combinators) (renamed from decision-combinators; TS; package MIT / GitHub SPDX null; npm 0.1.0; no measurements). Digital-design metaphor ≠ literal AND/OR. Not a new Jev API |
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
| Stop-hook attention redirect | eight risk Nouls on a redacted turn diff | Fail-open; assist = one reinspect; 0.85 uncalibrated; not a merge blocker | jev-preflight (Go MIT; 1★; Claude Code 2.1.267 owner-run) |
| Pre-send tool-result views | smallest view that still serves the next step | Code builds outline/focus/testlog/…; recall restores lines; code full unless confident | dizk/jev-lens (MIT; 79% fewer tokens / 500 SWE-rebench *theirs*). Distinct from rashedInt32/jev-lens |
| Observational memory | keep / kind Choice | Verbatim ledger; kind-keyed files; model-free compact; failed Jev does not drain buffer | pi-observational-memory-jev (MIT). Sibling of fast-jev-compaction / jev-compactor |
| Independent open-Jev class | LM / vision / voice finite-choice+prob; JevPick menu decode | NOTA; execute/confirm/reject; `/v1/systemone` wire-compat ≠ replica | openvons (Apache-2.0 LICENSE / GitHub SPDX NOASSERTION; 7★; JevPick 3.2–4.8× *theirs*) |
| Same-intent VOI cache | `same_intent` Noul + pick candidate; exact SHA-256 first | Policy bypass stream/tools/multimodal; **fail-open** to upstream | jevcache (MIT; n=100 *theirs*: 0 FP / precision 1 / recall 0.38 / fpr 0 vs Jaccard@0.35 fpr 0.48). Not in v0: streaming HITs |
| Worth-your-attention VOI | read / skim / save / skip from typed answers | Templates never prose; feed batches ≤12; 7-day cache | [ThinkyMiner/Winnow](https://github.com/ThinkyMiner/Winnow) (MIT; 80%/90% *theirs*). **Distinct from** [kevinpita/winnow](https://github.com/kevinpita/winnow) (context sieve) |
| Jev WHETHER / Python HOW / LLM WHAT | compact original chunks; suppress duplicate observational tools; skip next main-model | Fail-open; skip-next needs a Hermes core patch; aggressive defaults | hermes-jev-router (Python; license null; community plugin, not vendor). Cousin dizk/jev-lens + jev-compactor |
| Typed escalate/continue/abort baton | LLM writes; Jev judges; control returns typed | Gate `allow` never grants; fail-open; inverted loop wakes LLM only on escalate | jev-handoff (MIT; alpha v0.1; three backends; Vercel drops confidence). Same author as wakegate |
| Adversarial browser explore | six oracle Nouls + severity Score + next-action Choice | Playwright executes; sample from the distribution not argmax; fail only high conf **and** high severity | browser-jev (TS; license null). Visual blind. CI exit 1 on non-baselined findings |
| Local OpenJev `/v1/decide` | Qwen3-0.6B + LoRA + scalar head | **Not** a TypeSafe drop-in; not RLCD; distinct from hraness/sysone OpenJev runners | IamBusy/OpenJev (Apache-2.0; 45/60 vs v0.2 39/60 *theirs*; Hub OpenJev-Branch-v0.3) |
| SemIf `/v1/systemone` runoff | choice/score/noul from logits; no option ceiling | Wire-compat ≠ replica; confidence inferred; runoff is a product not a softmax | semif-serve (pyproject MIT / GitHub SPDX null; RTX 3080 Ti 1164 ms vs hosted 178 ms *theirs*) |
| Conflict ≠ ignorance | Noul collapses; named Choice escape separates | Binary Choice without escape is lexically biased | jev-typed-evaluation-collapse (license null; NCML field note v0.3 *theirs*) |
| Decision-as-memory flywheel | log every typed decision as a memory event | Append-only; 6 rows is a schema not a corpus | DGUI_HYPERMEM-JEV (HF MIT; sibling INSTRUCT_JEV) |
| Toolbelt sensors (not policy) | local-rules-then-Nouls; prepared reviews; guardrail+intent demo | Not a cert; reviews never stop commands; bench summary 404 this pass; **rh-guard owns reward-hack** | jev-security-scan (MIT) / jev-decisions (MIT; 1★) / TeoMastro (license null) |
| Record/replay pack CI | accuracy / ECE / Brier / cost / latency vs golden | Record outside CI; `check` offline; exit 0/1/2; McNemar compare | jevassert (Apache-2.0; SPEC v0 with jev-packs; adapters typesafe/openai/anthropic) |
| Failure-finding judgment arena | pairwise chosen/rejected; native vs verbalized p | Reviewed failure atlas, not a leaderboard; mock runs never enter a ranking | chenmingtang830/jevarena (Apache-2.0; JevJudge-Bench harness **not** findings). **≠** meetr1912/jev-arena |
| BBQ stereotype/uncertainty/cost | 3-way Choice on BBQ passages | Frozen instruction; unknown is the abstention option; not a bias cert | jev-bbq-experiment (R; license null; 58,492 / 97.28% / $0.3429 *theirs*) |
| Decider ≠ executor agent | next_action / progress / risk / stuck / done | LLM fills args only; risk≥0.5 pause; stuck ladder 2 Jev / 0 steps | jeffrey (MIT). Distinct from jev-handoff baton |
| Sentence-as-rule lint | ast-grep `rule:` × sentence `ask:` | Matcher silent-fail (over-match); Jev loud; fail-open no-verdict | mizchi/jevlint (MIT; 13/15 1.00/1.00 *theirs*). **≠** huntedman/JevLint |
| VOI hunk prune before generative review | per-hunk actionable-finding + required-context | Safety escarpment always keeps; cost not quality | prune-review (README Apache-2.0 / GitHub NOASSERTION; 22-run 1.18% / 305% outlier *theirs*) |
| Whole-repo intent vs the diff | VERIFIED / VIOLATION / UNKNOWN / NOT_APPLICABLE | Empty search ≠ proof; CLI works, Action not written | jev-intent-review (MIT/Apache-2.0; under construction) |
| Persist constraints across compaction | KEEP/LIFT/NARROW/EXCEPTION/REPLACE/UNKNOWN | Jev never writes policy; resources from user words; fail-open | pi-heed (MIT; 3★; v0.8.0+Jev 98.5% / 0 false block *theirs*) |
| Open replica substrates | `/v1/systemone` on Rust/WebGPU, Clojure/Jolt, CPU SemIf, ONNX NLI, GLiNER2 spec, prompted-JSON Bun bridge | Softmax / generated JSON ≠ Noul; isolation/byte-parity/agreement are the tests; spec ≠ product; wire-compat ≠ logit-equiv | grande (license null; JGLUE *theirs*); laya-jolt (Apache-2.0 byte parity); leesk212/JEV-CPU (Meanblock 404); kunchenguid/local-jev (done 30%/shape 57%); githubnext/localjev (**261★**; prompted JSON ≠ razorback16 logits); Eran-BA spec ≠ jeff |
| Harbor SGR-judge contract | Jev vs schema-guided LLM judges; invalid = FN | Frozen SLA-150; human labels; cost/latency first-class; incomplete cohort ≠ headline | jev-judge-bench (README MIT / GitHub SPDX NOASSERTION; 21 offline tests; canaries ≠ quality; **no quality headline yet**). **≠** jevarena / jevbench |
| Hand no-text steps to Jev | did-it-work / which-next / severity / safe | Writing stays with the LLM; PreToolUse deny/ask **fail-open**; Vercel reconstructs confidence as margin | jev-use (MIT v0.4.1; p50 220 ms; 186 vs 2,672 ms; gate 12/12; first loop 17/20 then 0/20 at 0.4 *theirs*). Same author as jev-handoff. **≠** jev-ultrafast |
| Pi System-One control plane | task/model/tool/failure/retry/context/skill/memory/review/GUI | Compaction never writes session; GUI < threshold → unknown; unresolved failures KEEP | pi-jev-control (TS; license null; v0.3.0 private; no live quality numbers). Distinct from omp-jev-extensions / jevons / pi-heed / pi-om |
| Generation as a tree of Choices | one typed question per word, then rank texts | Model never free-generates; embedding tree in code | jev-gpt (Python; license null; ~400 calls / 75 s / 2¢ *theirs*). Architecture demo. Distinct from jeffrey |
| OpenRouter recipe atlas | one call, many narrow questions; policy in code | Samples 16–36, not benches; pick don't extract; review band around every cut | jev-cookbook (JS MIT; 1★; 425 calls / $0.015; browser 5/6 *theirs*). Code prepares, Jev answers |
| Personal-history feed (no social graph) | Choice distribution over candidates = ranking | History local; one request per batch of ten; dwell = nearest-to-middle | jevfeed (JS MIT; 17 tests no network). Distinct from ThinkyMiner/Winnow and kevinpita/winnow |
| Competing NAR claim-audit | Choice/Score/Noul NAR; dual-channel ECE | Like-for-like channels; throughput ≠ latency; n=2000 CI before "SOTA" | openJev-verdict-2.0 (README Apache-2.0 / GitHub SPDX NOASSERTION; 77.10%/0.0636/0.0144 *theirs* unverified; **open PR #1**). **≠** IamBusy/OpenJev `/v1/decide` |
| Empty compaction-proxy skip | slogan only | No files, no fail polarity | IPECTER/jev-context-pruner (409 empty) **and** IPECTER/jev-runway (LICENSE-only). Sibling contrast only |
| 1-token logprob local endpoint | label-mass over caller-enumerated options | Arithmetic/numeric rules in code; 503 ≠ "no"; coverage ≠ correctness | chakuho (MIT; GUI 336 *theirs* 27B 95%/92% vs Jev 89%/82%; `__none__` 97% vs 8B 10%). Cousin jevify / TypeAR / pcdServer / jevmlx. Softmax ≠ Noul |
| Open replica inference engine | segmented forwards + Jev wire | Prefix reuse; families nanojev/decider-2b/laya; MPS only | jevinf (MIT; 2.57×/2.27× 100% argmax *theirs*). Wire-compat ≠ replica |
| Unofficial Elixir HTTP client | typed Noul/Choice/Score over Req | Policy in `cond`; confidence ≠ P(correct) | typesafe-elixir-sdk (MIT; 1★). **≠** dannote/jev OTP peer |
| Files-to-read VOI (rename + n=16) | BM25 shortlist then Jev packet | Index once; agent still Reads; read-only | jimmyhealer/jevex (was jev-semantic-explorer). n=16 160s→69s / $8.74→$3.13 / 16/16 *theirs*; n=8 finish 1/8→6/8 stays |
| Commit pre-review attention≠verdict | seven Nouls + headline Choice; six regex | Middle band = review; Nouls decide; hook fail-open on instrument failure | commitjev (MIT; 0 false on 5 clean *theirs*; small control; same owner as jev-orderby-bench) |
| Hermes plugin branded as Jev | Choice/Noul/Score *shape* | Not TypeSafe; not a Noul | hermes-plugin-jev (README MIT / GitHub SPDX null). Agnes 3.0 Flash chat-completions. **≠** hermes-jev-router |
| Pi verbatim summarizer replacement | one Noul per paired tool call | Keep-windows/pins in code; fail-open to LLM summary if <25% saved | pi-jev-compact (MIT). **≠** vava-nessa/pi-jev-compaction. Pair pi-jev-control / pi-heed |
| Decision-native inbox | nine typed signals | 100-point policy + SLA/tier in code; humans own ambiguity | mailordinal (MIT). Cousin jav-email-cascade. Not affiliated with TypeSafe |
| Unofficial Jev CLI (not ready) | planned exit-status semantic `if` | No release; do not copy MCP add | jev-cli (Apache-2.0 OR MIT; 0.0.0; 17 issues). **≠** jevql |
| Multilingual Laya class expansion | Choice/Noul/Score, mmBERT-base | Route by script before the forward pass; refit T | laya-multilingual (Apache-2.0; 322M; MASSIVE 0.366/0.387 vs English 0.227/0.733 *theirs*; ships uncalibrated) |
| Schema-conditioned encoder scorer | scalar logit per (state, candidate); code softmaxes | Peaked p = ranking | mobarmg/jev-schema-scorer-deberta-v3-large (Hub MIT; GitHub 404; v2 Choice 0.841 *theirs*) |
| Host-adapter surface delta | Choice next-tool + done-Noul | Same binary; more hosts | jev-routing now lists Cursor Agent CLI / Devin CLI (still not MCP; already §44) |
| Productized System One HTTP | caller labels → label + calibrated p; batch `{id,text}[]` | LLM chains are fallback only; policy stays in code | classifier-dev (MIT; **185★**; https://classifier.dev). 400 headlines **650 ms** *theirs*; packing 100 = one-at-a-time. Distinct from ask-jev-ai wall |
| Escalate-under-threshold (smart tier) | re-ask single-label p<0.7; mark `escalated` | Multi-label **ignores** tier (re-judge worse, 23 s) | classifier-dev. Emotion ≥0.9 → 82% / <0.5 → 29% *theirs*. gemini-3.8-flash 87.5→90.0 / 61.8→63.7; other flashes no better. Cousin jev-use |
| Measurement-first public bench | vs_jev / single / escalate / multi-label | Site table = tracked JSON; read eval/README first | classifier-dev. Multi-label F1 **0.887** / **230 ms** vs cascade **0.799** / 1.5 s *theirs* (eval 232 ms). n=7 train-on-test; ~0.03 coin flip. Not a Harbor taskset |
| Silent-fallback honesty | digest names the model that answered | `FALLBACK` marker; alerts on quiet chain | granite-4.0-h-micro F1 **0.546** vs advertised ~**0.800** *theirs*. rh-guard owns the gate; dinostomp owns instrument-not-score |
| Evidence-synthesis pointer (choxos) | Jev picks line ids; code copies verbatim | *Not found* / *Unclear* first-class; human tick never overwritten | choxos/jev-reviewer (MIT; **12★**; https://jevreviewer.xera.ac). **≠** egma-ai. 18-q template **4.6 s / $0.0101** *theirs* (spot check, not a validation study) |
| Two-pass Choice + Noul | relative “which line?” then absolute “does this line itself answer?” | Multi-row tables (Mean SD vs Median IQR) need both | choxos/jev-reviewer. Quotes = Noul ≥ 0.5 *theirs*. Cousin Stagehand extract / jev-sift |
| Institutional local `/v1/systemone` (GitHub Next) | TypeSafe SDK drop-in on DiffusionGemma via Chat Completions | Wire-compat ≠ logit-equiv; entropy-conf is generated | githubnext/localjev (MIT; **261★**). **≠** kunchenguid/local-jev. **≠** razorback16/openjev structured-read. **≠** IamBusy/OpenJev `/v1/decide`. Do not copy bun / `.env` |
| Prompted-JSON bake-off (Harbor-shaped) | AG News / BoolQ / SST-5; 5 models × 120 × 2 lengths = 1,200 | Prompted pipeline, **not** logits; no definitive winner; not calibrated | githubnext/localjev eval *theirs* M5 Max: Qwen3.6 short macro **76.7%**; Gemma 4 26B-A4B **75.0%** (SST-5 MAE **0.533**); DiffusionGemma **74.2%**. Qwen vs Gemma 26B = 2/120. Long-input both **69.2%**. Serving default unchanged |
| Runner gap vs structured-read | Chat Completions host ≠ OpenJev parity | Seeded canvas + read-only denoise + selected-token logits | LM Studio cannot load DiffusionGemma (18 Sep 2026 *theirs*). Cousin djev-spark already §36 |
| Laya packaging (not a new species) | Choice/Score/Noul NAR + Router over three Hub ckpts | Script-before-p; auto_task_detection off | NandhaKishorM/laya (Apache-2.0; **710★**; PyPI). Weights: convaiinnovations/{laya, laya-multilingual, laya-typed-decisions}. **≠** TypeSafe `/v1/systemone`. Do not copy pip |
| Where Jev still leads | High-cardinality Choice; soft-acc; raw ECE | Token budget `head_max_len`; 255 options | Banking77 Jev **0.870** (72) vs Laya **0.425** (77, ~3–4 tok/label); soft-acc 0.580 vs 0.471; raw ECE 0.144 vs 0.213 *theirs* (third-party Jev rows unpublished-here) |
| Where Laya leads on *their* T4 card | Latency; post-T ECE; multilingual router | Route by script before p | 1q **32.8 ms** vs Jev p50 236–276 ms (~7.8×); post-T ECE **0.081** vs 0.246; Khmer 0.000@0.952 is why Router exists |
| External openjev census (tweet, not scores) | Named list of ~18; first leaderboard promised "today" | Class-boundary + completeness watch; likes ephemeral | [@airesearch12](https://x.com/airesearch12/status/2101259522933186879) (Florian S / Benchmark Heaven). **≠** jevbench v1.1. Watch [jev-models](https://benchmarkheaven.com/jev-models); scored card is sibling. Do not copy Stripe |
| Class-boundary on a public list | GLiNER2 + routers counted as openjevs | Locate/categorize ≠ Noul; route ≠ replica ECE | GLiNER2 (Fastino); Succinct Router 14M; jev-model-router, Director, Loki. Qualify open-jev Dasein vs JoshuaSP; OpenJev razorback16 vs IamBusy |
| Incomplete census vs watch | Absence ≠ out of class | Completeness is a board watch item | Laya / localjev / kev / TypeAR / openvons / chakuho / jevinf / grande / laya-jolt / blackwood / classifier-dev |
| Harbor honesty watch (pre-score) | What the board must disclose | Calibration on/off rank; cost/latency assumptions; silent fallback; partial runs | Kinship with §67 v1.1 (cal off Main Score) and classifier-dev FALLBACK. Soft-score-as-hard-rank is a *design*. **Promoted:** answers are now Empirical as §78 |
| JevBench v1.2 geometric-mean product | Intelligence × Calibration × Speed × Cost, 25% each | Weak axis cannot be bought back; other views reorder ranks | Live [jev-models](https://benchmarkheaven.com/jev-models) scored 19 Sept 2026. Jev **75.3** / SemIf **74.6** (−0.7) *theirs*. Cal **ON** rank (delta from §67). **≠** tweet census **≠** v1.1 87.6. `notes.md` §78 |
| Weight sensitivity (same axes, not the Score) | Balanced no-cal / Emphasis Accuracy / Speed / Cost | SemIf #1 without cal; system-one-open #1 on cost; Jev #5 on cost | *Theirs*. Limits: "The weights are a choice." Do not treat geo-mean as physics |
| Option-order fragility | yes/no answer-judging 72% → 21% when A/B reversed | Small models are very sensitive to option order *theirs* | open-alternative-jev ranked on author's `A. yes, B. no`. Cousin of paraphrase-brittleness. Both runs in `results/v1.2/runs/open-alternative-jev/` |
| Instruction models in the class table | Typed decision task, not architecture purity | Luna/Gemini/DeepSeek/Qwen3.8 JSON-schema; Needle 3 tool-calling | Luna I **96.8** rank **#7**. Needle 3 C none → 0. OpenJev = razorback16 DiffusionGemma ≠ IamBusy |
| Harbor honesty (×2 / est.) | Name assumptions; ranks are configuration-specific | Self-host latency ×2 (+0.15 s) is an assumption; many costs est. | Production APIs unadjusted. Partial not ranked. Kinship classifier-dev FALLBACK |
| Laya / GLiNER2 / apps gaps | Absence ≠ quality; mapping ≠ scored | Laya absent (not named-excluded); GLiNER2 needs normalization; apps out | Completeness vs watch. Qwen3.8 27B Chutes TEE **≠** Archer |
| Apply-the-five (hourly 0842, already folded) | Wire≠logit · product+FALLBACK · packaging honesty · pointer-not-generator · leaderboard VOI | Do not re-card §73–§78; skip thin noise | `notes.md` §79. Compose, don’t dump |
| Hard-gate Noul as PR/quality (skip) | Soft sensor used as a merge seal | Soundness theater unless an exact envelope already proved the act | totally-tim/jev-gate (0★) / claude-jev-warden (1★). **≠** jev-gateway / MongLong0214/jev-gate / jev-gate-student-b. Do not copy action.yml |
| S1 keeps flying / S2 one-use (delta) | Typed flight Choice; async planner on low p | Physics/collisions; no stall; consume-mark; Local ≠ localjev | khordoo/jev-reflex-autonomy-lab. Seed = geometry. 20% still soft. No pixels. `notes.md` §80 |

On-device / Home Assistant / mobile are newly-feasible via the economics
inversion, not proven ports of every app. Named placements this hour
(`notes.md` §33): `Friedjof/jev-mobile` (USB Android, Mobile MCP task
delegation, Jev sees only prevalidated candidates); `jcpsimmons/jev-macos-loop`
(local OmniParser/OCR/AX; text-only Jev; pixels stay on the Mac; Finder
demo independently verified). HA-Jev is now a real card
(`notes.md` §68; **17★**; not for locks/heaters). Do not copy env, MCP
URLs, or install steps.

Reproduce/open heads (`rongxinzy/LightJev`, openjev family,
[`convaiinnovations/laya`](https://huggingface.co/convaiinnovations/laya),
encoder [`open-jev-deberta-v3-large`](https://huggingface.co/com-kotobalabs/open-jev-deberta-v3-large),
LoRA [`jev-gate-student-b`](https://huggingface.co/SargeDev/jev-gate-student-b),
companion packaging [`laya-typed-decisions`](https://huggingface.co/convaiinnovations/laya-typed-decisions),
GitHub/PyPI face [`NandhaKishorM/laya`](https://github.com/NandhaKishorM/laya) (**710★**; Router; not a new species; `notes.md` §76),
[`jaredpalmer/kev`](https://github.com/jaredpalmer/kev),
[`BlackwoodAI/blackwood-rlcd`](https://huggingface.co/BlackwoodAI/blackwood-rlcd))
are evidence that the *interface* (Choice/Score/Noul, or yes/no logits
as P(relevant)) is the transferable part — not a request to implement a
backbone or a second API skill. Laya: self-hostable, text-only, 512
tokens/question; vendor benches vs Jev are **claims** (this hour the
author published the vs-Jev table *and* named it third-party /
unpublished-here — `notes.md` §76). Encoder open-jev:
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
— ONNX ModernBERT; measured done 30% / shape 57% vs Jev *theirs*;
`confidence` omitted; **not** equivalence (`notes.md` §70). Distinct
from jev-local stub and jeff. **This hour's substrates (not Archer):**
[`bokuweb/grande`](https://github.com/bokuweb/grande) Rust/WebGPU
kev-shaped branches; [`jlt-commons/laya-jolt`](https://github.com/jlt-commons/laya-jolt)
Clojure byte-parity Laya; [`leesk212/JEV-CPU`](https://github.com/leesk212/JEV-CPU)
SemIf on CPU (Meanblock 404); [`Eran-BA/Jev_from_GLiNER2`](https://github.com/Eran-BA/Jev_from_GLiNER2)
spec-only GLiNER2 decide adapter. GLiNER (locate) / GLiClass (categorize) /
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
