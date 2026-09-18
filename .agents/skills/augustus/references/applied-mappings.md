# Applied placements: sieves, keep/drop, triage, rank, route

These cards are *where a judgment-class model sits* in running software.
They are family-agnostic: the **typed judgment provider** is TypeSafe Jev
by default (live docs / `typesafe-ai`); an open Choice/Score/Noul head
(e.g. Laya) is a substitute you must self-eval (`research/notes.md` §18);
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
Official cousin: classifying RAG passages cookbook
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
"Done." **Counterexample**: sampling 2% of production with an LLM judge —
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
chunks fail-closed so a timeout empties the context. **Test**: moderation
cost/coverage + false-hold vs false-publish; ranking recall *separate*
from nDCG; select misroute rate.

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
70.8% lexical; `Dicklesworthstone/skillranker` from live session context;
LlamaIndex selectors fail closed or a declared default. Toolrouter / open
JevRouter: **Hypothesis** until measured on *your* catalog. **Counterexample**:
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
Unknown).
