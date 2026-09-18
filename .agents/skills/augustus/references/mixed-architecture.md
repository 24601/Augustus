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
judgment: `formal-methods.md`.

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
| Route to a tool / start a side effect | **Fail closed** (don't call) | A wrong tool is an action |
| Rerank a retrieved list | Fail open: keep retrieval order (`WiktorB2004/llama-index-jev`, **Empirical recipe** on BEIR nfcorpus: MiniLM 0.340 nDCG@5 → MiniLM+Jev 0.396; rerank fails open, *select* fails closed). Listwise/cross-encoder scores belong here, not on the row above. | Ranking errors are quality; selection errors are control-flow |

Worked placements (2026-09-18 topic:jev hour + prior archive):

- **Chunks before the LLM** — discourse dominant theme (48 tagged samples).
  Official cousin: classifying RAG passages cookbook (**Contract**).
- **Command output before context** — `ibrahemid/jevprune`: per-line
  relevance against the task; last-N lines and error signatures kept in
  *code* before Jev sees anything; full output recoverable by id. Same
  shape as winnow/fast-jev-compaction (`agent-self-assessment.md`).
- **Diff hunks before `git add`** — `ibrahemid/git-jev-stage`: one Choice
  per hunk (`include` / `exclude` / `mixed`); mixed and low-confidence stay
  unstaged; lines never split; staging is an exact patch after confirm.
  Candidates come from `git diff`, not from Jev.
- **Every agent-step before an LLM autopsy** — `aaravriyer193/OpenSmoke`:
  Jev over all steps (cheap enough to skip sampling); LLM only on flagged
  runs for root cause. Prefilter of *analyst attention*.
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
- Function-calling cookbook (**Contract**): function *names* and closed-set
  args as questions; code still validates the call.

Routing ROI does not transfer across datasets (`validation.md`, calibre).
`FirasSX914/Janus` exists to *measure* when Jev vs another model wins on
your data, then route — that measurement loop is the design, not a
universal gate.

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

Related placements:

- **AGENTS.md / project prefs as criteria** — jev-pref; pi-warden rule
  breaks 6→0 on 150 paired runs (`agent-self-assessment.md`).
- **Confidence gates + shadow mode** — `AntonioCoppe/jev-harness` (48.9s
  Claude CLI vs 1.3s Jev on a 24-row filter). Log would-do until evals pass.
- **Hybrid countable + judgment rules** — `DanRWilloughby/snifftest`:
  deterministic tells score 1.00; judgment rules flag only outside the
  unsure band. Explicit: a reading near 0.5 is *no judgment*, never a pass.
  That is the Noul-0.5-is-uncertainty non-negotiable, implemented.
- **Rubric-then-prose review** — `frostney/clean-code-review`: Jev against a
  named rubric (Clean Code), then an LLM writes the review. Mixed
  architecture, not "Jev is the reviewer."
- **Semantic smell gates** — `Eliran-Turgeman/repear` (silent failures,
  weakened tests, scope creep); `scale-venture-partners/riff` (static codes
  + per-finding p). Decompose the opaque "quality" score into named Nouls.
- **Malicious-before-run** — `luantak/is-malicious`. High-stakes gate:
  fail closed, shadow first, never treat a Jev yes as authorization to
  execute untrusted code. Code still sandboxes.

Permit is independent of confidence (`Kevthetech143/super-jev`): domain
rules veto regardless of model certainty.

## Placement gallery (2026-09-18 movers)

Use these as *existence proofs of a position*, then write your own
decision-design card. Do not clone APIs from READMEs.

| Placement | Judgment | Stays in code | Artifact |
|---|---|---|---|
| Hold-before-publish moderation | Hazard Nouls + harm Score | Block/review/pass policy | Near Here / firehose family |
| Tool / engine / skill select | Choice + fits-Noul | Dispatch, auth, reject-all | skillranker, LlamaIndex selectors, Toolrouter |
| Preference lint | Per-rule Noul/Choice on a diff | Rule text, outcome map | jev-pref |
| Context / log prune | Per-line or per-block relevance | Always-keep set, recall keys | jevprune, winnow |
| Exact hunk staging | Per-hunk include/exclude/mixed | `git diff`, atomic apply | git-jev-stage |
| Semantic `WHERE` | Noul/`jev_prob` over a row | SQL, indexes, LIMIT | `kylemclaren/jevql` (CLI rewrites; DB sees ordinary SQL) |
| Home automation read | Choice/Score/Noul as an entity | Automations, device I/O | `AboveColin/HA-Jev` |
| Browser loop without generation | Action Choice over visible elements | Perception, constraints, click | lizard-agent |
| Analyst attention cascade | Step-level silent-failure Nouls | Grouping, LLM autopsy | OpenSmoke |
| Formula / query embedding | JUDGE as a function | Spreadsheet/SQL engine | judge-sheets, jevql |

On-device / Home Assistant / mobile remain **thin evidence** this hour (2 X
samples; `Friedjof/jev-mobile`, HA-Jev). Treat as newly-feasible candidates
via the economics inversion, not as proven ports.

Reproduce/open heads (`rongxinzy/LightJev`, openjev family,
[`convaiinnovations/laya`](https://huggingface.co/convaiinnovations/laya))
are evidence that the *interface* (Choice/Score/Noul, no generation) is the
transferable part — not a request to implement a backbone or a second API
skill. Laya: self-hostable, text-only, 512 tokens/question; vendor benches
vs Jev are **claims**. Closed calibrated API vs open weights is a
self-eval tradeoff (`research/notes.md` §18). TypeSafe remains the
documented *exemplar*, not the class monopoly. GLiNER (locate) /
GLiClass (categorize) / GLiNER2.5 (local multi-head), listwise, and
vision families: `judgment-class.md`.

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
