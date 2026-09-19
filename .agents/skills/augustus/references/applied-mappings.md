# Applied placements: sieves, keep/drop, triage, rank, route

These cards are *where a judgment-class model sits* in running software.
They are family-agnostic: the **typed judgment provider** is TypeSafe Jev
by default (live docs / `typesafe-ai`); an open Choice/Score/Noul head
(e.g. Laya, kev) is a substitute you must self-eval (`research/notes.md` §18, §45);
GLiNER (locate) / GLiClass (categorize) / listwise rankers / vision scorers
are cousin species with different objectives (`judgment-class.md`). Do not
copy request fields from this file.

Same card grammar as `mappings.md`: what transfers, what does not, sketch,
example, counterexample, test. Status words: **Contract**, **Empirical
recipe**, **Hypothesis**.

Umbrella placement: `mixed-architecture.md`. Classification skepticism:
`faq.md`. Family / objective / vision / agent-architecture portents:
`judgment-class.md`. Cross-domain (not SWE-only): `mental-models.md`.
Proof vs judgment: `formal-methods.md`.

## 1. Context sieve

**Method**: admit / stub / drop artifacts before they consume context.
**Transfers**: one relevance Noul (or a small Score rubric) per block,
span, or tool result, batched over the same state; code hides confident-no
behind a stub + recall key. An always-keep set lives in **code** (current
instruction, recent turns, errors, signatures, last-N lines). **Does not
transfer**: asking the provider to rewrite or summarize the artifact (that
is generation); hiding errors because they scored "irrelevant"; treating
timeout as drop.

```text
candidates = split(tool_result)          # code owns the unit
always_keep = errors ∪ last_N ∪ instruction
judge = Noul(relevant_to_task) per remaining unit
code: hide if p ≤ t and not always_keep; stub + recall key
fail open on missing verdict → keep
```

**Example**: winnow hides at relevance ≤0.22; fast-jev-compaction asks two
Nouls (should the *call* stay? should the *result* stay verbatim?);
`ibrahemid/jevprune` keeps last-N + error signatures in code, then judges
the rest per line; `kevinpita/pi-jev-context` hides (does not delete)
older Pi history, always-keep user/system/todos, `/jev off` restores.
Pi compaction cousins (`tamaratran/fast-jev-compaction`,
`vava-nessa/pi-jev-compaction`) keep verbatim drop, never summarize.
**Encoder backend, same job (Empirical as README behavior, 2026-09-18
~16:22):**
[gliner25-compaction](https://github.com/m-newhauser/gliner25-compaction)
— GLiNER2.5 (`fastino/gliner2.5-base-v1`) chooses
`keep_full` / `keep_evidence` / `keep_call_only` / `drop` and copies
exact character-offset spans. Not a summarizer. Mutating tools / unknown
shell / control operators → `keep_full`. Low-confidence or invalid
evidence **fails closed to `keep_full`** (the reduction is the
irreversible act; from the evidence side this *looks* like keep-on-error).
`shadowMode` defaults true. Characters, not tokens; no published
retention-quality rates (`notes.md` §50). Family:
`judgment-class.md`. Do not copy the plugin.
**Stdout prune, same family, different job (Empirical as README /
evals README, 2026-09-18 ~17:15):**
[jev-pruner](https://github.com/tamaratran/jev-pruner) — after Bash
runs, Jev Noul-prunes stdout chunks **before** the main LLM sees
them; no summary. Hard envelope first (≤10k estimated tokens;
JSON/XML/YAML/diff/binary; whole-document commands untouched), then
soft Noul. Fail-safe keep original on any failure; full archive for
recovery. Marketplace id still `fast-jev-output`. Codex is opt-in
wrapper, not automatic interception. Same author as
fast-jev-compaction; complementary, not a duplicate. Do not copy
the plugin (`notes.md` §53).
**Session-ledger cousin, same family, different job (Empirical as
README behavior, 2026-09-18 ~17:48):**
[carryforward](https://github.com/Dharundp6/jev-carryforward) —
verbatim JSONL facts (`record`); Jev Noul-scores `recall` against
the current task. Nothing summarised or deleted. Constraints and
corrections **always return in full** (Jev never votes on a rule).
Fail-open: no key → whole list. Thresholds 0.60 full / 0.30–0.60
one line are *theirs*. Nine entries × three tasks is a **hint, not
proof** (`notes.md` §55). Do not copy `mcp add`.
**Classify-first MCP, same family, different job (Empirical as
README / schema, 2026-09-19 ~00:38):**
[jev-sift](https://github.com/kbhuw/jev-sift) — batch path / public
URL / inline text (or a tool description) → Jev relevance or 1–8
typed questions **before** the main agent reads. Content goes to
the judge without entering main agent context first (paths/URLs).
Uncertain → closer look; errors and truncation ≠ irrelevant. Hard
envelope (theirs): 50 items, 60k char, 2 MB / 20 s, public-IP only,
no JS/cookies/login, PDFs unsupported. Transport tests ≠ accuracy.
No LICENSE this pass. Same retrieve-wide → decide → evidence-set
family as decision-native-rag-skills. Cousins: typesafe-screening-mcp,
kazuhideoki/jev-search, jev-pruner (after Bash), carryforward (ledger
you already hold). Not jev-routing (host adapter). Topology A MCP
(LLM outer loop). Do not copy plugin / `mcpServers` / key-file
how-to (`notes.md` §56).
Local teacher-copy for the same hole:
[`SargeDev/jev-gate-student-b`](https://huggingface.co/SargeDev/jev-gate-student-b)
(Qwen2.5-0.5B LoRA; P(relevant) from yes/no logits; 148,160-row
[`jev-distill-corpus`](https://huggingface.co/datasets/SargeDev/jev-distill-corpus);
card: fail-open on errors; HF card **unchanged** this pass vs
`notes.md` §33). That is System One as a **memory/context
gate**, not an action permit: vector recall → local yes/no → inject or
stub (`notes.md` §33, §44, §55). Agreement with Jev labels is not independent
gold (`notes.md` §33). Official cousin: classifying RAG passages cookbook
(**Contract**). **Counterexample**: one Noul "is this log useful?" over
3k lines — that is nine judgments pretending to be one. **Test**: recall
of must-keep lines (failures, the current instruction); tokens saved;
timeout leaves the artifact in context. Fail-open: a false drop loses
evidence.

## 2. Exact-text keep / drop

**Method**: select among candidates the program already holds (hunks,
lines, spans, DOM nodes). The provider never invents bytes.
**Transfers**: one Choice per candidate (`include` / `exclude` / `mixed`,
or a Noul per line) with the user's sentence or task as criteria; `mixed`
and low-confidence stay out; code applies an **exact** subset (patch,
filter, click). **Does not transfer**: splitting a hunk, generating a
commit message, rewriting the span, or recovering a candidate you never
parsed.

```text
candidates = git_diff | parse_lines | visible_elements   # code
questions  = Choice{include, exclude, mixed} per candidate
code: include iff winner=include AND confidence ≥ t
      mixed → human or leave unstaged; never auto-split
apply exact bytes; working tree / source text unchanged except by
the subset operation you already had
```

**Example**: `ibrahemid/git-jev-stage` — candidates from `git diff`; mixed
hunks unstaged; lines never split; atomic apply after confirm. Line-by-line
search cookbook (**Contract**): score existing line ids, do not generate
ids. lizard-agent: pick among visible elements; answers are *located*.
Omni cousin this hour: [blackwood-rlcd](https://huggingface.co/BlackwoodAI/blackwood-rlcd)
picks among **letters drawn on the screenshot**; code still clicks
(`notes.md` §46). Text-only cousin: [jev-e2e](https://github.com/perixtar/jev-e2e)
— Jev selects observed controls; Playwright independently checks;
a confident model cannot substitute for checked expectations.
**Extractive quotes (Empirical as named receipts, 2026-09-18 ~14:52):**
[testimonial-miner](https://github.com/AppitStudio/testimonial-miner) —
code numbers sentences; one broadcast (Choice/Noul/Score + per-sentence
Nouls); the model never writes; `redecide` retunes thresholds on the
log. [jev-reviewer](https://github.com/choxos/jev-reviewer) — the model
**points at line ids**; code copies verbatim quotes with place; *not
found* is an answer. Claim/evidence Stop cousin
([clear-head](https://github.com/VladyslavHontar/clear-head), ~16:48):
the model judges claims against **keyword-retrieved session lines**,
not against another model's prose; `JEV_FIRM` below 0.6 never blocks
(`notes.md` §51). Compaction cousin
([gliner25-compaction](https://github.com/m-newhauser/gliner25-compaction),
~16:22): the model points at **character offsets** in a tool result;
code copies those bytes; a generator summary is the rejected species
(`notes.md` §50). Stdout-prune cousin:
[jev-pruner](https://github.com/tamaratran/jev-pruner) — the model
scores chunks of observed Bash stdout; code keeps verbatim lines and
archives the rest (`notes.md` §53). Computer-use cousin:
[solari-reflex](https://github.com/hitakshiA/solari-reflex) — structured
observation → typed decision → verified act; **no screenshots**; model
output never becomes a selector (`notes.md` §48). Encoder-backend
cousin of the same hole:
[gliner2-ultrafast](https://github.com/sahibzada-allahyar/gliner2-ultrafast)
— local GLiNER2 (`fastino/gliner2-multi-v1`) scores observed a11y/DOM
controls; code clicks; remote text helper only for TYPE; `DONE` ≠
verified success (`notes.md` §52). Open-head cousin:
[laya-mind2web](https://huggingface.co/ShaunSpark/laya-mind2web-browser-agent)
— Laya operation + target index over interactive DOM elements (not
screenshot multimodal). Contrast blackwood-rlcd (letters on a
screenshot). Specialist-form cousin, **not TypeSafe Jev:**
[Cua-S1](https://github.com/trycua/cua/tree/main/libs/cua-s1) —
option-attention among observed elements (fill/check/click/skip);
code owns execution order; dry-run default; source-only
(`notes.md` §54).
**Score-among-observed atlas (Empirical as public showcase class
pattern, 2026-09-19 ~00:38):**
[jevable.com](https://jevable.com/) — candidates already on the
page (a11y/DOM, ads, on-screen posts); the model scores; **code**
clicks / filters. Not a 342-title dump. Cross-link: jev-ultrafast /
gliner2-ultrafast / solari-reflex / cua-s1 / laya-mind2web. Your
Signal: score posts already on screen, apply rules locally — same
judge-once / re-policy family as Near Here. Do not merge Flights
7 s / $0.0039 with gliner2-ultrafast 12.20 s; computer-use "100×"
is a **claim** (`notes.md` §56).
**DOM-as-text + fan-out (Empirical as atlas browser-use *shape*):** a
screenshot task translated into a structured DOM snapshot as `state`,
then speculative questions over numbered candidates — not vision
(`notes.md` §49; `mental-models.md` §boundary).
**Axis check:** if the kept byte / cited fact / click target is not
already in the candidates you numbered, this card does not apply —
retrieve or parse first; do not ask recall.
**Counterexample**: "write the patch that matches this sentence" — that is
generation. **Test**: every kept byte occurs in the input; mixed never
auto-included; snapshot stale → abort, don't guess.

## 3. Environment / harness triage

**Method**: separate *environment* failures (missing keys, tools, files,
network, truncated output, unloaded prefs) from *agent* failures, cheaply
enough to scan every step instead of sampling.
**Transfers**: a small battery of Nouls/Choices over each trace step
(silent workaround? disclosed? recovered? missing-secret? broken-tool?);
code groups repeats into incidents; an LLM writes root-cause **only on
flagged runs**. **Does not transfer**: one Noul "was this a good run?";
treating a high p as proof the sandbox is healthy; letting the provider
author the fix.

```text
for step in trace:                         # code iterates
  flags = {silent_workaround, disclosed, missing_key, truncated, …}
code: cluster flagged runs by missing thing
LLM: root-cause prose on the cluster, not on every step
```

**Example**: `aaravriyer193/OpenSmoke` — Jev over every step; LLM autopsy
on flags; the motivating failure is an agent that hit `KeyError` and said
"Done." **SREGym-Lite (Empirical as a *shape*, 2026-09-18):**
[@HacksonClark](https://x.com/HacksonClark/status/2100993319878721665)
/ [blog](https://sregym.com/blog/jev-sregym-lite) — Jev as a *tool* that
ranks proposed diagnostic tests and reviews evidence (20/50 → 24/50;
4 improved, **2 regressed**). It did not diagnose; it cannot recover a
hypothesis the agent never offered. Placement (same thread,
[@Antoniocoppe](https://x.com/Antoniocoppe/status/2100993869680615552)):
rank next tests/evidence; keep tests closed; inspect regressions as
calibration failures (was confidence high on the wrong Choice?); low
confidence goes back to the agent, not into silent mitigation.
`notes.md` §33. The named cut this hour (`notes.md` §42): Noul
`env_broken` *as opposed to* the agent's own bug; Choice category;
Noul workaround; run status silent / disclosed / recovered / clean.
Heuristic fixture 12 traces: P=R=0.86; Jev on that fixture not yet
measured. Pre-mortem: scan a new sandbox *before* users meet it, fail
the build on *silent* env-breaks — a shape, not a CLI.
**Merge-gate cousin (Empirical as README behavior / offline demo,
2026-09-18 ~16:48):**
[latch](https://github.com/CaseReed/latch) — cluster a finished red
run (Playwright / Jest / pytest / JUnit) **in code**; Jev labels each
cause (≤8 calls; cached free); **policy** returns Gate: PASS (infra
noise) vs Gate: BLOCK (real failure). The judge never says "ignore"
alone; `ignore_as_infra` needs `env_cascade` + an infra fingerprint.
Reporter never fails Playwright (missing key → `needs_human`);
`--gate` is a separate CI step. Demo: 8 connection errors → PASS; 5
assertions → BLOCK. Message-based grouping fragments logic
regressions (`pallets/click`: 13 failures → 10 clusters). Pair with
Harbor (frozen CI artifacts × PASS/BLOCK) and rh-guard
(eval-integrity). Their policy thresholds are not class constants
(`notes.md` §51). Do not copy the reporter.
**Counterexample**: sampling 2% of production with an LLM judge —
the economics inversion is the point. **Test**: planted harness bugs
recovered; false-flag rate on known-clean runs; LLM never runs on the
clean majority. High-stakes cousin: `luantak/is-malicious` is a *pre-run*
gate (fail closed + sandbox), not triage of a finished trace.

## 4. Moderation and ranking

**Method**: hold-before-publish (moderation) and graded relevance (ranking)
are the same cost-sensitive cascade with different fail policies.
**Transfers**: hazard Nouls + harm Score for moderation; a shared Score
rubric (or per-pair Noul) for rerank of a **retrieved shortlist**; store
raw probabilities and re-policy in code (judge once). **Does not
transfer**: ranking as selection (wrong tool is an action); exhaustive
pointwise scoring as an index; a universal 0.8; Choice probabilities
compared across different candidate pools; treating a listwise or
CLIP/GLiClass affinity as a fail-closed authorize (`judgment-class.md`).

```text
moderation: Nouls(jailbreak, hate, …) + Score(harm)
            → code: pass / review / hold / block
            fail closed on publish; fail open on "keep in review"
ranking:    retrieve K → Score/Noul per candidate → sort in code
            fail open: keep retrieval order on error
            select (which engine/tool): fail closed
```

**Example**: Near Here / jev-experiments firehose (judge-once, slider
re-filters); LlamaIndex Jev rerank **Empirical** BEIR nfcorpus MiniLM
0.340 → 0.396 nDCG@5, rerank fails open, select fails closed; TREC DL2019
zero-shot MAP 0.4748 / nDCG@10 0.683 vs monoBERT 0.718 (`mappings.md` §4).
Realtime ~200ms chat claims remain **Hypothesis** as a number. **Counterexample**:
using top-1 Choice as a relevance score across queries; dropping RAG
chunks fail-closed so a timeout empties the context.
**Decision-native RAG (Empirical as architecture; Hypothesis as a
universal win, 2026-09-18 ~17:48):**
[decision-native-rag-skills](https://github.com/emergency-lee/decision-native-rag-skills)
— retrieve wide → decide explicitly → evidence set → conflict
resolve → reason only over kept evidence. Embeddings stay candidate
generators. Provider-agnostic; no bundled Python harness; **no
universal benchmark**. Default migration gates are starting
targets. Offline replay → shadow → canary → A/B (`notes.md` §55).
Do not ship because an LLM judge prefers it.
**Classify-first agent I/O of the same sandwich (Empirical as
README, 2026-09-19 ~00:38):**
[jev-sift](https://github.com/kbhuw/jev-sift) — file lists and
public URLs stay candidate generators; the judge sees content; the
main LLM opens only items worth a closer look. Inline text the
agent already read cannot recover that cost. Uncertain/errors/
truncation ≠ irrelevant. Mocks ≠ accuracy (`notes.md` §56).
**Living applied-mappings atlas (Empirical as showcase; 342 is
*their* count):**
[jevable.com](https://jevable.com/) — class patterns (intent
columns, score-among-observed, VOI gates, generative UI decide,
robotics text-state, draft-gate fail modes), not a hit list.
JSON-LD first page is 36; `pageSize` 36. No public API this pass.
Maker clocks stay claims unless already a named receipt
(`notes.md` §56).
**Recursive file search (MED; distinguish from federated web):**
[kazuhideoki/jev-search](https://github.com/kazuhideoki/jev-search)
scores local files then fzf — **not**
[superagents-lab/jev-search](https://github.com/superagents-lab/jev-search)
(web lanes). Max-over-chunks is not a calibrated whole-file
probability. No LICENSE this pass.
**Test**: moderation
cost/coverage + false-hold vs false-publish; ranking recall *separate*
from nDCG; select misroute rate; required-evidence recall vs Top-K.

## 5. Skill / tool routing

**Method**: selector over a **closed catalog** (skills, tools, query
engines, models), not "the model chooses its next tool in a loop."
**Transfers**: Choice over the offered set + a whether-anything-fits Noul
(reject-all is first-class); rank-then-verify (cheap pass over
descriptions, second request over a shortlist with full bodies); suggest
at most one skill per turn. Large or changing catalogs may prefer a
GLiClass one-pass (categorize over all catalog labels at once) over a
255-option Choice — that limit is Jev's, not the class's
(`judgment-class.md`). GLiNER spans are the wrong species for this hole:
picking a catalog member locates nothing. **Does not transfer**: an
open-ended "what should I do?"; dispatch, auth, or argument validation
delegated to the provider; routing ROI copied from another dataset.

```text
catalog = skills | tools | engines          # code owns membership
q1: Choice(which) + Noul(anything_fits)     # one request
q2: rerank top-k with full bodies, fits-Nouls may reject all
code: dispatch | refuse | ask_human
fail closed on side effects; no-match option when coverage is open
```

**Example**: skill_suggestion cookbook (**Contract**); GodsBoy 94.4% vs
70.8% lexical (exploratory: questions revised after the first full run); `Dicklesworthstone/skillranker` from live session context;
LlamaIndex selectors fail closed or a declared default.
[`rajdhakad9826/routeKit`](https://github.com/rajdhakad9826/routeKit):
Jev estimates task *requirements*; code applies hard constraints and a
deterministic cost/quality/latency policy — Jev does not pick the model
(**Hypothesis** until measured on *your* catalog; `notes.md` §33).
[`trietphan/jev-claw`](https://github.com/trietphan/jev-claw) is the
same split for OpenClaw (classify axes; `decide()` maps the route; path
regex floors risk). [`nekowasabi/jev-routing`](https://github.com/nekowasabi/jev-routing)
is a host adapter, not an MCP plugin: compact, then one Choice + done,
then one schema (`notes.md` §44).
[`TheoOliveira/pi-jev`](https://github.com/TheoOliveira/pi-jev) is the
same selector hole inside Pi (tools + skills); fail-open to a keyword
shortlist; **not** `kevinpita/pi-jev-context` (sieve).
[`ddfeyes/jev-mode`](https://github.com/ddfeyes/jev-mode) is the
latency-class split: bulk triage/tag/route off the frontier context
(synthetic 1,000: −77.8% tokens; accuracy claim is **parity**).
**Route ≠ memory** ([jev-hermes](https://github.com/de-niji/jev-hermes)):
a cheap intent Choice skips memory/tool *tours* on `calendar` / `mail` /
`status`; `complex` keeps memory. Savings are skipped tours, not
turning memory off (`notes.md` §48).
Toolrouter / open JevRouter: **Hypothesis** until measured on *your*
catalog. **Counterexample**:
the agent looping "pick a tool, call it, pick again" with the provider as
the planner. **Test**: callability (literal / paraphrase / near-miss
neighbor); reject-all when nothing fits; calibre reminder — thresholds
do not transfer (`validation.md`).

## 6. Expensive observation router

**Method**: do not buy a costly observation (OCR, lab test, LLM autopsy,
full PDF) when structure already has the answer. **Transfers**:
structural prove ∩ remainder judge (`mappings.md` §18). pdf-inspector
(or a text layer, a recipe, a law) first; Noul only on leftovers; merge
in code. **Does not:** OCR-every-page because the model is cheap enough;
copying 1.74×; skipping pages the structure said needed OCR.

```text
for page in document:
  if text_layer usable → extract locally
  else Noul(needs_OCR) → send only those pages
merge in page order; never drop a page
```

**Example (Empirical, this corpus):** `misbahsy/doc-router` — 19 docs /
155 pages, 155→87 billed, 1.72× wall, **1.74× $**; judge is **2.5% of
the OCR bill it authorises**; 9 false-skips vs 28 for rules-only
(heuristic cheaper, misses 3× more). **Counterexample:** Jev as the first
OCR, so a watermark talks a scan into "has text." **Test**: planted scans
are sent; planted born-digital pages are not billed; page order preserved.
Re-measure on *your* documents. Same sandwich as jevgate (Proven / Refused /
Unknown). Same VOI as retrieve-then-state: if the answer is not in the
cheap text layer, **pay for the passage / OCR**, then judge
(`mental-models.md` §boundary; atlas history suite).
