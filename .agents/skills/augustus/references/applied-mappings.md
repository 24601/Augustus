# Applied placements: sieves, keep/drop, triage, rank, route

These cards are *where a judgment-class model sits* in running software.
They are family-agnostic: the **typed judgment provider** is TypeSafe Jev
by default (live docs / `typesafe-ai`); an open Choice/Score/Noul head
(e.g. Laya, kev) is a substitute you must self-eval (`research/notes.md` §18, §45);
GLiNER (locate) / GLiClass (categorize) / listwise rankers / vision scorers
are cousin species with different objectives (`judgment-class.md`).
Frozen-VLM logit harness: yoheinakajima/glance (`notes.md` §147) reads
answer-token probabilities from a frozen open VLM. Soft scores are for
threshold, abstain, or rank. Not a safety gate. Harness, not trained weights.
Do not copy request fields from this file.

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

**Example**: [kevinpita/winnow](https://github.com/kevinpita/winnow)
hides at relevance ≤0.22 (agent **context sieve** — always qualify
the owner; distinct from [ThinkyMiner/Winnow](https://github.com/ThinkyMiner/Winnow)
worth-your-attention VOI, `notes.md` §69); fast-jev-compaction asks two
Nouls (should the *call* stay? should the *result* stay verbatim?);
`ibrahemid/jevprune` keeps last-N + error signatures in code, then judges
the rest per line; `kevinpita/pi-jev-context` hides (does not delete)
older Pi history, always-keep user/system/todos, `/jev off` restores.
Pi compaction cousins (`tamaratran/fast-jev-compaction`,
`vava-nessa/pi-jev-compaction`) keep verbatim drop, never summarize.
**pi host port this hour (Empirical as README + their bench,
2026-09-18 ~19:48):**
[fast-jev-compaction-pi](https://github.com/zaycruz/fast-jev-compaction-pi)
— same verbatim job on pi's `session_before_compact`; fallback to
the built-in summary on any failure. Their large-session card:
compaction ~50× faster than pi's LLM summary; pure mode drops old
calls; `preserveCallInputs` restores commands/paths. Do not copy
`pi install` (`notes.md` §59).
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
**OpenCode host-port, same job, different insertion (Empirical as
README + source, 2026-09-19 ~16:39):**
[indiejoseph/opencode-jev-pruner](https://github.com/indiejoseph/opencode-jev-pruner)
— OpenCode jev-pruner context sieve.
host port of tamaratran/jev-pruner.
OpenCode `tool.execute.after` on
`bash`. Pattern: observe→score-candidates→prune.
Loop *theirs*:
bash runs → 10k-token gate → archive full output → chunk →
Jev noul per chunk vs history → rewrite with markers +
recovery footer. Default scorer jev-zen / jev-1.13-free
(Zen System One, exact id, keyless). zen-chat ≠ Noul
(`zen-chat` is an LLM approximation). fail-open original.
keepScore >0.1 floor. Archive `.opencode/fast-jev-output/`.
indiejoseph/opencode-jev-pruner ≠ nrdz-labs/fast-jev-opencode
(session compaction, §62). **≠** tamaratran/jev-pruner.
Do not copy tamaratran 24/24 / 83%. Do not copy the plugin
(`notes.md` §96).
**Decision Graph Protocol envelope, host-owned remainder
(Empirical as README + spec, 2026-09-19 ~17:40):**
[numerous-com/dgp](https://github.com/numerous-com/dgp)
— Decision Graph Protocol frame→assess→commit.
app retains permissions/effects.
Jev-first assessor-neutral.
guarded commit / receipt/next frame.
assessment batching.
Protocol around a judgment-class assessor; commit
fail-closed in the application; assessment is a
sensor. numerous-com/dgp ≠ TypeSafe official.
hard-gating DGP as safety theater.
**≠** waymode **≠** ctmx/openrouter-jev-mcp
Decision-as-Plugin **≠** petercr/jev-orchestrator
**≠** AgentGhost. Do not copy tokens / `uv`
(`notes.md` §98).
**Session-ledger cousin, same family, different job (Empirical as
README behavior, 2026-09-18 ~17:48):**
[carryforward](https://github.com/Dharundp6/jev-carryforward) —
verbatim JSONL facts (`record`); Jev Noul-scores `recall` against
the current task. Nothing summarised or deleted. Constraints and
corrections **always return in full** (Jev never votes on a rule).
Fail-open: no key → whole list. Thresholds 0.60 full / 0.30–0.60
one line are *theirs*. Nine entries × three tasks is a **hint, not
proof** (`notes.md` §55). Eval finding *theirs*: agent
called `recall` **0/4** with tools available — SessionStart
hook > hoping (`notes.md` §68). Do not copy `mcp add`.
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
**Atom then sense MCP (Empirical as README + 55 tests;
2026-09-19 ~17:49):**
[enzo-mcp](https://github.com/mahawi1992/enzo-mcp)
(MIT; **0★**) — enzo-mcp independently falsifiable claims, not
relevance-first. Deterministic evidence outranks Jev.
enzo-mcp UNKNOWN useful. Prior sensor output never sent back.
`allow_external_jev` per send. **≠** jev-sift. Do not
copy `uv` (`notes.md` §89).
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
**Framework-agnostic compact + same-pass safety (Empirical as
README + one-session bench; 2026-09-19 ~00:39; was empty
skip §61):**
[jev-compactor](https://github.com/edwardyen724-g/jev-compactor)
— **Jev judges relevance. Code decides structure.** Keep
messages byte-for-byte; never rewrite; tool pairs never
split. Regex floor in code (`rm -rf` / force-push / `DROP
TABLE` / `curl | sh`) independent of Jev. Dual fail
polarity: compaction **fails open** if Jev is down
(history unchanged) unless `failClosed`; pending-action
destructive/exfil **fails closed**. One synthetic 12.7k-
token session *theirs*: earlier vs-Sonnet card **64.5%** /
**366 ms** (`notes.md` §65); later product-arm table
**73%** (53–76%) / **350 ms** / **$0.0004** / **4 of 4**
facts vs shipped summarizers (30–250× cheaper) — two
synthetic sessions, not a survey. Foreman safety in the
same ~300 ms pass. Claude Code shorter path remains
fast-jev-compaction. OpenCode fail-open port:
fast-jev-opencode (§62 MED). Observational-memory sibling:
[pi-observational-memory-jev](https://github.com/willfish/pi-observational-memory-jev)
— keep/kind only; verbatim ledger; model-free compact
(`notes.md` §68). Do not copy npm (`notes.md` §65, §68).
**Pre-send view selection (Empirical as 500-trajectory
bench; 2026-09-19 ~03:38):**
[jev-lens](https://github.com/dizk/jev-lens) — **not**
[rashedInt32/jev-lens](https://github.com/rashedInt32/jev-lens)
(§63 human Stop filter). Code builds outline/focus/
testlog/… views from the tool result's own lines; Jev
picks the smallest view that still serves the next step;
`recall` restores dropped lines. 500 SWE-rebench
trajectories *theirs*: **79%** fewer tokens (11.6M →
2.4M); 88% command / 31% code. Compress **before** first
send — post-send prune broke cache and cost **17% more**.
Claude plugin unmeasured. Do not copy npm (`notes.md`
§68).
**Jev WHETHER / Python HOW / LLM WHAT (Empirical as README
+ offline pytest; license null; 2026-09-19 ~04:39):**
[hermes-jev-router](https://github.com/rsdkrasen/hermes-jev-router)
— compaction keeps original chunks (never rewrite);
duplicate observational tools suppressed; skip the next
main-model call when evidence is enough (**needs a Hermes
core patch**). Fail-open. Offline pytest: **2 vs 1**
main-model call pattern. Aggressive defaults. Community
plugin, not vendor. Cousin of dizk/jev-lens +
jev-compactor. Do not copy patch/plugin how-to
(`notes.md` §69).
**tools≠use / SessionStart over hoping (Empirical as
eval finding; 2026-09-19 ~03:38):**
[carryforward](https://github.com/Dharundp6/jev-carryforward)
— with tools + skill installed, the agent called
`recall` **0/4**. SessionStart hook injects rules
unconditionally; an MCP tool sitting there is not enough
(`notes.md` §68). 9×3 remains a hint.
**Empty compaction-proxy skip (2026-09-19 ~06:43 and
~07:49):**
[jev-context-pruner](https://github.com/IPECTER/jev-context-pruner)
— description-only; `contents/` 409 empty.
[jev-runway](https://github.com/IPECTER/jev-runway) —
LICENSE only; created≈pushed 1s; README 404. Sibling of
fast-jev-compaction / jev-compactor / dizk/jev-lens /
jev-pruner. Do not invent files (`notes.md` §71, §72).
**Pi verbatim summarizer replacement (Empirical as
README + latency table; 2026-09-19 ~07:49):**
[pi-jev-compact](https://github.com/dev-willbird1936/pi-jev-compact)
(MIT) — keep-windows/pins in code, then one Noul per
paired tool call; Pi stores original characters, not a
paraphrase. Fail-open to the built-in LLM summary
(off / no key / <25% saved / HTTP error). **Distinct
from**
[pi-jev-compaction](https://github.com/vava-nessa/pi-jev-compaction).
FB-Scanner *theirs*: kept 1 of 261; replay 0.6 s vs
first UI spinner 26 s (host cost, not judge cost). Pair
pi-jev-control / pi-heed. Do not copy `pi install`
(`notes.md` §72).
**Dedicated Pi port of fast-jev-compaction (Empirical as
README + bench; 2026-09-19 ~16:52):**
[fast-jev-compaction-pi](https://github.com/zaycruz/fast-jev-compaction-pi)
(MIT; npm 0.1.1; README SHA `809c0bd`) — vendored
[tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction).
Verbatim keep/drop; user/assistant text never rewritten.
Fail-open to pi's built-in LLM summary (no key / error /
timeout / `minReductionRatio`). ~50× vs LLM summary
*theirs*; `preserveCallInputs` 8/8 commands + 17/17
paths. **≠** pi-jev-compact **≠** pi-jev-compaction.
Always write **zaycruz/fast-jev-compaction-pi**. Do not
copy `pi install` (`notes.md` §87).
**Tiny local RAG prune (Empirical as README; 2026-09-19
~19:47):**
[nanoprune](https://github.com/dmdjr1409/nanoprune)
(MIT; **0★**) — local encoder prune/choice/score.
nanoprune 2.8MB ECE 2.58% *theirs*. Distill from Laya
421M. “0 hallucination guaranteed” theater. **≠**
TypeSafe Jev. Do not copy `pip` (`notes.md` §91).
**Deterministic log verify ≠ System One (Empirical as
README; 2026-09-19 ~19:47):**
[system-one-skills](https://github.com/0thernet/system-one-skills)
(MIT; **0★**) — 0thernet/system-one-skills
deterministic verify. No model call. 3/24 logs net
8,026 tok *theirs*; holdout would add 3,612. Do not
paste as a judge (`notes.md` §91).

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
log. **[choxos/jev-reviewer](https://github.com/choxos/jev-reviewer)**
(systematic-review Jev Reviewer; MIT; **12★**;
https://jevreviewer.xera.ac; **≠** egma-ai) — the model
**points at line ids**; code copies verbatim quotes with
file/page/row; *Not found* / *Unclear* are answers. Two-pass:
relative Choice (which line?) then absolute Noul (does this line
itself answer?); quotes = Noul ≥ 0.5 *theirs*. Human tick is the
product: checked answers never overwritten (`notes.md` §48, §74).
Claim/evidence Stop cousin
([clear-head](https://github.com/VladyslavHontar/clear-head), ~16:48):
the model judges claims against **keyword-retrieved session lines**,
not against another model's prose; `JEV_FIRM` below 0.6 never blocks
(`notes.md` §51). Compaction cousin
([gliner25-compaction](https://github.com/m-newhauser/gliner25-compaction),
~16:22): the model points at **character offsets** in a tool result;
code copies those bytes; a generator summary is the rejected species
(`notes.md` §50). **≠**
[gliner-native-runtime](https://github.com/shershah1024/gliner-native-runtime)
(schema→spans locate; not keep/drop of held
tool-result bytes; `notes.md` §97). Stdout-prune cousin:
[jev-pruner](https://github.com/tamaratran/jev-pruner) — the model
scores chunks of observed Bash stdout; code keeps verbatim lines and
archives the rest (`notes.md` §53). OpenCode host-port:
[indiejoseph/opencode-jev-pruner](https://github.com/indiejoseph/opencode-jev-pruner)
— same extractive job on `tool.execute.after`; jev-zen /
jev-1.13-free; zen-chat ≠ Noul (`notes.md` §96). Computer-use cousin:
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
**Meaning-as-spec (Empirical as README resolver, 2026-09-18
~19:48):**
[jevcumber](https://github.com/RubyBrewsday/jevcumber) — Cucumber
`.feature` only; no step-definition glue. Jev picks among
**observed controls** and **literals already in the step**; never
writes code or invents values. Lockfile makes replay
deterministic (`--frozen` CI, no key). Refuse below 0.6. Same
pointer family as Stagehand pick-and-copy / jev-e2e. Do not copy
the tarball install (`notes.md` §59).
**Pointer-not-generator repo walk (Empirical as README;
2026-09-19 ~16:52):**
[JevFind](https://github.com/Peu77/JevFind) (Rust MIT;
**1★**; README SHA `0588181`) — path Noul then overlapping
windows; code copies snippets. Defaults `--file-threshold
0.25` / `--threshold 0.55` still soft. Not AST; not a
patcher; not a gate. Keyword still wins exact strings.
**≠** jevex **≠** jev-semgrep **≠** jevgrep. Do not copy
cargo / `.env` (`notes.md` §87).
**NL memory → beam-search FS (Empirical as README;
2026-09-19 ~17:25):**
[findme](https://github.com/marc2332/findme) (Rust;
license null; **4★**; README SHA `f2a2ca71`) — list
entries, Jev ranks names+lightweight metadata, keep
the beam, descend. Parent fallback ≤4. gitignore /
symlink skip in code. **≠** JevFind path-then-window.
Life/knowledge retrieval, not only SWE. Do not copy
`cargo install` / `TYPESAFE_API_KEY` (`notes.md` §88).
**Decision-as-filing (Empirical as README + classify.ts;
2026-09-19 ~17:49):**
[pigeonhole](https://github.com/noripto/pigeonhole)
(MIT; **0★**) — Choice over user attributes → move.
pigeonhole OTHER skip. `OTHER` skip. Default 0.6 still soft. autoOnSave off.
**≠** jev-semgrep. Do not copy plugin marketplace
(`notes.md` §89).
**Downloads filing fail-open (Empirical as README;
2026-09-19 ~18:41):**
[tidy](https://github.com/MANISH007700/tidy)
(MIT; **0★**) — macOS Downloads. `min_confidence`
0.8 still soft. tidy none-of-folders stay. Undo.
**≠** pigeonhole **≠** downloads-sorter. Do not copy
`uv` (`notes.md` §90).
**Observe→score→act namesake (Empirical as README;
2026-09-19 ~18:41):**
[ZHUBoer/ego-jev](https://github.com/ZHUBoer/ego-jev)
(MIT; **0★**) — Ego Lite observe/act; Jev `choose`
over compact page state. ZHUBoer/ego-jev reserved
`__none__`. `selectedId` or null. No universal
cutoff. runWorkflow completed ≠ success. Exact work
local. **≠** jiangkoumo/ego-jev. Do not copy
`TYPESAFE_API_KEY` (`notes.md` §90).
**Decision-validated UI (Empirical as README; 2026-09-19
~16:52):**
[gram-render](https://github.com/wei-b0/gram-render) (MIT;
**0★**; README SHA `dd5fb44`) — derive → select → layout →
validate. Jev never authors text. Empty quotes →
`unavailable`. Telegram 4096 / 64-byte `callback_data`
prove the tree; valid ≠ good. **≠** json-render **≠**
jev2ui **≠** jev-gpt. Do not copy npm / bot token
(`notes.md` §87).
[jev2ui](https://github.com/dglazkov/jev2ui) (Apache-2.0;
**0★**; README SHA `f0d477fc`) — leftover Gemini writes;
Jev decides jobs. Jobs 11/11 vs Baseline 10/11 valid A2UI
*theirs*. Remix from the Score distribution. Skip Archer.
`notes.md` §87.
**Harness pick-and-copy (Empirical as PR-body architecture + their
local eval, 2026-09-19 ~00:48; draft stack):**
[Stagehand #2955](https://github.com/browserbase/stagehand/pull/2955)
(5/5 of [#2951](https://github.com/browserbase/stagehand/pull/2951)–#2955,
all OPEN draft) — Jev **picks** observed a11y elements; **code copies**
text. `extract` `"off"` | `"judge"` | `"pick"`. Judge replaces the
metadata LLM `completed` check (throw → LLM). Pick: schema plan
(scalars / bools-enums / lists of flat objects; else LLM); must
validate + completion gate else LLM; screenshot extract always LLM.
Their card (gemini-3.8-flash, 25×3): **37/75** no-LLM in **~0.5 s**
vs baseline **4.37 s** / two LLM calls; 69/75 vs 23/25 (**92% both**);
LLM-off **36/75** — pick is a **fast path, not a replacement**.
Same observe→score-among-candidates→code-acts *job* as jev-ultrafast /
gliner2-ultrafast / solari-reflex / cua-s1, inside a major harness.
Do not merge clocks. Do not copy `experimentalJevAct`
(`notes.md` §57).
**Closed-vote harness, no planner LLM (Empirical as README
architecture, 2026-09-18 ~21:39):**
[JevOnly](https://github.com/buluoray/JevOnly) — code builds
every option from observation / goal / fact register; **Jev
only picks**. No planner LLM, no helper LLM, no free text.
Type without generation. Verify then undo. Irreversible
`risk ≥ 0.50` never default. Worked example *theirs*: 11
steps, 43 Jev calls, ~340k tokens, ~$0.014, 17 s. Distinct
from Stagehand (LLM fallback). Do not copy `run.sh`
(`notes.md` §61).
**Host-owned product surface (Empirical as README + their
eval suite):**
[waymode](https://github.com/mossburgh/waymode) — the **app**
retains handlers, permissions, validation, and state; Jev
selects among live typed actions. `completed` is Jev's
reading — prove durable effects via server state. Default
p ≥ 0.7. Evidence *theirs*: 24/26 public suite, 34/36
completion regression — **bounded development evidence, not
proof every app is self-driving**. Not on npm. Do not copy
AI_GATEWAY how-to (`notes.md` §61).
**Hot-click CU on an indexed viewport (Empirical as README
+ n=3 medians; 2026-09-19 ~00:39):**
[ego-jev](https://github.com/jiangkoumo/ego-jev) — drive
ego-lite with Jev. Indexed element table in; one request
answers operation **and** per-op target (speculative,
compatible-only heads). Code owns observe / execute /
stale-ref / loop / `--until` exit. Text model only when
typing is needed; malformed fill → `text_model_failed`,
never guess. Jev `done` ≠ business success. Measured
*theirs*: HN **4.9 s vs 9.7 s**, wiki **5.4 s vs 10.1 s**
(~2× vs per-step `kimi-k3`; n=3; high variance; not a
benchmark). Cousin of jev-ultrafast. Distinct from JevOnly
/ waymode / Stagehand. Do not copy `install.sh`
(`notes.md` §65).
**OCR+AX desktop CU (Empirical as README; MIT **427★**;
2026-09-19 ~09:51):**
[typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use)
— macOS Vision OCR + AX → numbered items → TypeSafe
Choices (`kind` / `item` / `site` / optional
`offscreen`) → code clicks/types. **Never ships a
screenshot for the *decision*.** Writer only for
`type_text` / `site: other` / the one-shot **answer**
(the answer reader *may* receive the capture — a
writer packet, not the Choice). Overlapping options
read as doubt; keep the set exclusive. AX is a bonus,
never sole (Spotify 0 *theirs*). Post-type Noul 0.5
and `--min-confidence` 0.4 stay product copy, not
Harbor τ. $0.0002 vs Opus $0.032 (155×) *theirs* on
**one screenshot**, not a taskset. **≠** jev-ultrafast
**≠** cua-s1 **≠** jev-macos-loop **≠** camoufox. Do
not copy `uv sync` / `.env` (`notes.md` §81).
**ASR voice-browser CU (Empirical as README; MIT **103★**;
2026-09-19 ~10:01):**
[jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser)
— Web Speech partials → snapshot ≤100 → one 9–11-question
Jev request → Playwright. **Jev never generates.** Regex
spans; Jev picks; code copies. Closed-set may act on a
partial; free-text waits. Numbered overlays, spoken
digit, no second model. Spoken confirm is convenience
not auth. 27/27 fixtures *theirs*. **≠**
chris-wozniczek/jev-voice-control **≠**
nikolas-j/jev-voice-browser **≠** typesafe-computer-use.
Do not copy `npm` / `.env` / `run.sh` (`notes.md` §82).
**Adversarial browser, Playwright executes / Jev chooses
(Empirical as README; license null; 2026-09-19 ~04:39):**
[browser-jev](https://github.com/DowLucas/browser-jev) —
one Jev call per step (six oracle Nouls + severity Score
+ next-action Choice). Code-only checks first. **Sample
from the distribution, not argmax.** Fail only high conf
**and** high severity. Visual blind. Demo lesson: narrow
questions (untranslated 0.30 inside "confusing" vs 0.99
on its own Q). CI exit 1 on non-baselined findings. Do
not copy playwright / `.env` (`notes.md` §69).
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
**Pre-review typed gate (Empirical as README + own-repo
latencies; 2026-09-19 ~02:38):**
[ci-gatekeeper-bot-jev](https://github.com/NemanjaManic/ci-gatekeeper-bot-jev)
— four questions (`should_review` / `risk` / `route` /
`touches_secrets`) → `auto-approve | human-review | block`
*before* expensive LLM/human review. Operator-owned
thresholds; conservative default (`cosmetic`) escalated
trivial diffs to human-review in practice. Measured
*theirs*: Jev **504–629 ms**; secondary review ~4–5 s
only on human-review + elevated risk. Comment never
includes raw diff. `package.json` MIT / GitHub SPDX
**null**. Cousin of latch (that one is flaky-vs-real on a
*finished* red run). Distinct from egma attention ≠
correctness. Do not copy `action.yml` / secrets
(`notes.md` §67).
**Stop-hook attention redirect, not a merge blocker
(Empirical as owner-run hook smoke; 2026-09-19 ~03:38):**
[jev-preflight](https://github.com/muse0509/jev-preflight)
— eight risk axes in one request on a redacted turn
diff; `assist` = at most one reinspect then finish;
**fail-open**; default 0.85 **uncalibrated**. Not an
autofix, not a merge blocker, not a replacement for
tests/SAST. Distinct from latch / ci-gatekeeper
(authorize-or-block) and from rashedInt32/jev-lens
(human attention filter). Owner-run Claude Code 2.1.267:
no-key fail-open PASS; key-enabled exactly one
continuation *theirs*. Do not copy marketplace / key
(`notes.md` §68).
**VOI hunk prune before generative review (Empirical as
22-run cost table; 2026-09-19 ~05:46):**
[prune-review](https://github.com/shubhangi013/prune-review)
— Jev scores each hunk; only a smaller packet reaches
the generative reviewer. Safety escarpment always keeps
concurrency/auth/a11y/startup. Target ~20% cost cut.
*Theirs:* winning-only 27.9% (post hoc); all 22 incl.
305% outlier **1.18%**; excl. outlier 15.9%. Cost, not
quality. Source preview. Cousin of ci-gatekeeper (that
one auto-approve/human-review/block), not a clone. Do
not copy pnpm (`notes.md` §66, §70).
**Whole-repo intent beyond the diff (Empirical as CLI;
under construction):**
[jev-intent-review](https://github.com/yottayoshida/jev-intent-review)
— stated intent → search the repo after the change →
one small question per place →
VERIFIED/VIOLATION/UNKNOWN/NOT_APPLICABLE. Empty search
≠ proof. CLI works; GitHub Action not written. Do not
copy Cloudflare how-to (`notes.md` §70).
**Commit pre-review attention≠verdict (Empirical as 13
labelled + own-history; 2026-09-19 ~07:49):**
[commitjev](https://github.com/yodablocks/commitjev)
(MIT) — seven Nouls + one headline Choice per commit;
six regex checks never reach the model. Middle band is
**"review"**, never rounded. Nouls decide; Choice only
headlines at confidence ≥0.50. Hook **blocks only on a
warning**. Calibration *theirs*: every rule fires on its
defect; **0 false on 5 clean** (small control); own 16
commits 3 warn / 4 review / $0.0017. Same owner as
jev-orderby-bench (one commit per call; never sort
two-decimal probs). Cousin prune-review / ci-gatekeeper
/ jev-preflight. Do not copy hook install
(`notes.md` §72).
**Seed/expand/judge/verify crawlers (Empirical as
README; 2026-09-19 ~18:41):**
[jev-crawlers](https://github.com/russfranky/jev-crawlers)
(MIT; **0★**) — seed|expand|judge|verify|report.
jev-crawlers risk bands never raw boolean. Ranking ≠
calibrated bug p. n=12 fixture. Verify grounding,
not exec. Review queue is the product. rh-guard owns
the gate cousin. Do not copy `AI_GATEWAY_API_KEY`
(`notes.md` §90).
**Bulk log classify packing VOI (Empirical as README;
2026-09-19 ~19:47):**
[decide](https://github.com/alsoleg89/decide)
(license null; **0★**) — alsoleg89/decide packing VOI.
500 issues $0.0203 *theirs*. 0.8 ≠ 80% accuracy.
Classifies; never runs commands. **≠** jev-sift.
Do not invent MIT. Do not copy `uv` (`notes.md` §91).
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
**Meaning-search without embeddings (Empirical as a named
stripped-repo card, 2026-09-18 ~18:46):**
[jevgrep](https://github.com/Bentlybro/jevgrep) (`jgrep`) packed-
parallel Jev relevance; two-stage outline then zoom top 30; no
index. 228 questions on docstring-stripped Flask/httpx/Django/
AutoGPT: **79% top-5** vs BM25 40% / grep 20%. Keyword still wins
exact wording (BM25 top-10 96% vs 85%). Packed+parallel 0.9 s vs
serial ~23 min on AutoGPT 4,329 files. Distinct from kazuhideoki
(file+fzf), superagents-lab (web), and jev-sift (classify-first
MCP). Do not copy `install.sh` (`notes.md` §58).
**Meaning-grep AND/OR/NOT over line Nouls (Empirical as README
+ their LLM-as-judge test, 2026-09-18 ~21:39; dedicated
2026-09-19 ~16:30):**
[jev-semgrep](https://github.com/uehaj/jev-semgrep) — zero-dep
Node; one Noul per line × meaning; `-e`/`-a`/`-v` boolean
over *thresholded* bits; 30 lines × 8 concurrent.
Proposition ≠ embedding (cross-encoder line+question).
Contrast-set: all six “about a refund”; only customer
asking pass; angry-agent cosine ~1. Calibrated ~0.5 vs
top-k cosine. No index (vector index wins for repeated
large fixed corpora). Cross-lingual JP↔EN plus
FR/RU/DE/ES/ZH/KO; EN safer near threshold. Name collides
with [Semgrep.dev](https://semgrep.dev) SAST. **Not a
gate** (ranking fail-open; rh-guard skip). Distinct from
jevgrep (file/chunk packed search), jev-sift, jevex,
bohutang/sift, pg-jev, kazuhideoki/jev-search,
superagents-lab/jev-search, and jev-combinators
(metaphor ≠ literal AND/OR). LICENSE MIT (GitHub
NOASSERTION). **51★** this pass (ephemeral; SIGNAL ★42;
§61 0★). Their judge test: precision 0.94, recall 0.98
on 10×51 lines — not Harbor. Do not copy npm / `npx` /
`.env` / marketplace how-to (`notes.md` §61, §86).
**Calibrated meaning-grep over a live tree (Empirical as
README architecture + economics, 2026-09-19 ~17:40):**
[jegrep](https://github.com/can1357/jegrep) — describe
meaning; absolute yes/no per path + line range.
jegrep calibrated path+range Nouls.
no embeddings/index/daemon.
~$0.01–0.03 typical. agent --json.
Cascade default; `-t 0.4,0.2`; `--max-batch` ≤255.
Ranking fail-open (false drop loses the file; keyword
still wins exact strings). **No published Harbor
needle/noise table** — do **not** copy jevgrep 79%.
OpenRouter/TypeSafe auto-failover is silent FALLBACK,
not the same Noul. Pin `--endpoint`. Auto-τ-lowering
is not a 0.4 proof.
can1357/jegrep ≠ Bentlybro/jevgrep ≠ uehaj/jev-semgrep.
**≠** JevFind **≠** quarry **≠** jevex. Do not copy
`cargo install` / OpenRouter keys (`notes.md` §98).
**Pointer path-then-window (Empirical as README;
2026-09-19 ~16:52):** sibling of meaning-grep, not a
boolean composer — [JevFind](https://github.com/Peu77/JevFind)
(`notes.md` §87).
**Authorship named escape (Empirical as README;
2026-09-19 ~16:52):**
[jev-authorship-check](https://github.com/webstercharly/jev-authorship-check)
(license null; **0★**) — Choice `human` /
`ai_generated` / `uncertain`. Not courtroom evidence.
`notes.md` §87.
**n8n classify/route/score (Empirical as README;
2026-09-19 ~16:52):**
[n8n-nodes-jev](https://github.com/vibe-with-me-tools/n8n-nodes-jev)
(MIT; **1★**; npm 0.2.2) — unofficial. Route by Choice +
Low Confidence output (0.5 still soft). Arithmetic in
Code/IF. `notes.md` §87.
**Four-engine Harbor (Empirical as README + metrics.json;
2026-09-19 ~16:52):**
[job-posting-triage](https://github.com/geckguy/job-posting-triage)
— fitted tfidf wins; majority floor **0.947**; Jev on the
floor; calibration ≠ discrimination. Jev via
classifier.dev. `notes.md` §87.
**Evidence-packet explorer (Empirical as their
`docs/performance.md`, author-run):**
[jev-semantic-explorer](https://github.com/jimmyhealer/jev-semantic-explorer)
(**jevex**) — index once (chunks + BM25), Jev ranks a
shortlist, MCP returns `source_of_truth` / tests / callers /
line ranges. Read-only, not a patcher. Claude Code A/B:
6.8→2.2 files, 8.6→3.2 tools. SWE-bench Verified n=8:
**1/8 → 6/8** finish (empty output = miss); packet n=50
HitFile 0.233 vs BM25 0.159 is diagnostic, **not** the
product KPI. Distinct from jevgrep / jev-sift /
s1-graphify-indexer. Do not copy MCP how-to (`notes.md`
§61).
**Evidence-packet explorer delta (rename + n=16 SWE
card; 2026-09-19 ~07:49):**
[jevex](https://github.com/jimmyhealer/jevex) **is**
`jimmyhealer/jev-semantic-explorer` renamed (same
`created_at`; GitHub redirects). New *theirs*: SWE-bench
Verified **n=16**, 160s → **69s**, $8.74 → **$3.13**,
patch **16/16 both arms**. 90s cap 1/16 vs **11/16**
finished. Keep n=8 finish 1/8 → 6/8. Claude Code n=5
6.8 → 2.2 unchanged. (`notes.md` §72).
**Measured RAG rerank vs a generative reranker (Empirical as
one-run; Hypothesis as a transfer, ~18:46):**
[Jev-RAG](https://github.com/Max-sm-yc/Jev-RAG) — same search
~30k tokens: RAG+Jev+Spark $0.00122838 / 62.3 s vs RAG+Spark-
rerank+Spark $0.00421838 / 228.14 s vs Spark full-context $0.0032
/ **10.60 s**. ≥70% cost and 72% latency cut vs Spark *rerank*,
not vs no-RAG. Costs include embeddings. License null this pass.
Do not invent a bake-off (`notes.md` §58).
**Local rules first, then remainder Nouls; never auto-train
on the model's own hides (Empirical as README + small e2e;
2026-09-19 ~00:39):**
[x-reply-filter](https://github.com/zhuyansen/x-reply-filter)
— Chrome MV3. `rules.js` proves easy junk (zero cost);
batched Jev four Nouls on the rest (promo / bait /
off-topic / AI filler; default ≥0.75 collapses, does not
delete). Auto-hides sit in a confirm queue; only
user-confirmed examples become few-shot (10/10) plus a
"same class as marked junk" Noul. E2E *theirs*: three
samples → 0.90 / 0.93 vs 0.08 / 0.10. Cousin of
[bohutang/sift](https://github.com/bohutang/sift)
(§62 MED; ~$0.00003/post *theirs* — Substance/Humor/Chit-chat/Promo/Junk + AI-written). Cheap hold-before-show cookbook.
Do not copy wrangler (`notes.md` §65).
**Worth-your-attention VOI (Empirical as unreviewed goldens;
always qualify the owner; 2026-09-19 ~04:39):**
[ThinkyMiner/Winnow](https://github.com/ThinkyMiner/Winnow)
— Chrome extension: read / skim / save / skip from typed
answers; templates never prose. **Distinct from**
[kevinpita/winnow](https://github.com/kevinpita/winnow)
(context sieve). Feed batches ≤12; 7-day cache.
Unreviewed goldens *theirs*: **80%** verdict / **90%**
content-type. HN 30 links ~$0.0015. Not on the Chrome Web
Store. Do not copy unpacked-extension how-to
(`notes.md` §69).
**Personal-history feed without a social graph (Empirical as
README + 17 offline tests; 2026-09-19 ~06:43):**
[jevfeed](https://github.com/fengyiqicoder/jevfeed)
(MIT) — last 200 history pages stay local; outbound links
via Jina Reader; cheap LLM summarizes/filters; **one Jev
request per batch of ten** (the distribution *is* ranking).
No likes/follows/accounts. Distinct from ThinkyMiner/Winnow
(grade an existing feed) and kevinpita/winnow (sieve). Do
not copy `npm start` (`notes.md` §71).
**OpenRouter recipe atlas (Empirical as 15 small samples,
not benches; 2026-09-19 ~06:43):**
[jev-cookbook](https://github.com/nexibeo/jev-cookbook)
(MIT; 1★) — triage / PII / rerank / moderation / browser /
Gmail. Code prepares, Jev answers narrow questions. Samples
16–36 handmade; authors say **not benchmarks**. Recipes
01–13: 425 calls / $0.015; browser 5/6 *theirs*. Do not
copy OpenRouter tilde-id (`notes.md` §71).
**Decision-native inbox (Empirical as README + tests;
life/business, not SWE-only; 2026-09-19 ~07:49):**
[mailordinal](https://github.com/Milo318/mailordinal)
(MIT) — nine typed questions in one request, then a
**100-point deterministic policy** (SLA + account tier
in code). Does not ask "how urgent is this?" Humans own
ambiguity: low routing confidence never silently lowers
priority. Demo labelled `demo`; live Jev optional and
server-side. Cousin jav-email-cascade. Independent, not
affiliated with TypeSafe. Do not copy `npm run dev`
(`notes.md` §72).
**Read-only Gmail trays (Empirical as README; 2026-09-19
~17:49):**
[jevmail](https://github.com/fazlerocks/jevmail)
(MIT; **3★**) — five trays + urgency. `gmail.readonly`.
~3¢ / ~1 min per 1k *theirs*. **≠** mailordinal.
`notes.md` §89.
**macOS inbox writes after review (Empirical as README;
2026-09-19 ~17:49):**
[mailjay](https://github.com/secondfret/mailjay)
(license null; **0★**) — archive/trash proposed, not
permanent delete. **≠** jevmail readonly. `notes.md` §89.
**Metadata-only Gmail overlay (Empirical as README;
2026-09-19 ~18:41):**
[jev-mail](https://github.com/muhammedilyasy/jev-mail)
(MIT; **0★**) — overlay + dashboard. `gmail.readonly`.
muhammedilyasy/jev-mail metadata only; never bodies.
~$0.25/20k *theirs*. **≠** fazlerocks/jevmail **≠**
mailordinal **≠** mailjay **≠** Essentiel-Jev.
`notes.md` §90.
**LinkedIn hide fail-open (Empirical as README;
2026-09-19 ~18:41):**
[lkclean](https://github.com/stefw/lkclean)
(MIT; **0★**) — hide, not delete. lkclean Show
fail-open. Noise 70% / interest 35% / blocked 60%
still soft. Sponsored local. **≠** x-reply-filter
**≠** Winnow. `notes.md` §90.
**YouTube cover fail-open (Empirical as README;
2026-09-19 ~18:41):**
[jev-yt-time-saver](https://github.com/jaibhasin/jev-yt-time-saver)
(license null; **1★**) — cover + jev-yt-time-saver
Show anyway. Metadata not pixels. `notes.md` §90.
**Sort-by-meaning ranking (Empirical as README;
2026-09-19 ~18:41):**
[jsort](https://github.com/keltokhy/jsort)
(MIT; **1★**) — pairwise Jev → Bradley-Terry. jsort
scores are relative. Noul not Choice for scale.
CommonLit r=0.824 / ρ=0.841 *theirs*. Do not copy
`uv` (`notes.md` §90).
**Local prune ranking (Empirical as README; 2026-09-19
~19:47):**
[nanoprune](https://github.com/dmdjr1409/nanoprune)
— nanoprune 2.8MB ECE 2.58%. Typed-judge-kit warns
Noul rerank made R@5 worse 14/15→13/15: a gate is
not a ranker on already-good retrieval. `notes.md`
§91.
**Public classification API (Empirical as README +
eval/README; life/business; 2026-09-19 ~08:37):**
[classifier-dev](https://github.com/mrmps/classifier-dev)
(MIT; **185★**; https://classifier.dev) — the
categorization *product* those inbox apps would call.
Caller labels in, label + calibrated confidence out;
batch `{id, text}[]` ~1000. Jev primary (`src/jev.ts`);
LLM fallback only. Distinct from ask-jev-ai's
six-question wall. Do not copy wrangler / `npm i -g`
(`notes.md` §73).
**Open NAR packaging cousin (Empirical as README;
2026-09-19 ~09:07):**
[NandhaKishorM/laya](https://github.com/NandhaKishorM/laya)
(Apache-2.0; **710★**) — self-hosted Choice/Score/Noul
with a script-before-p `Router` over Hub checkpoints.
Not a classification HTTP API. Not a TypeSafe drop-in.
Do not copy `pip install laya` (`notes.md` §76).
**Questions-as-index compile (Empirical as README;
life/PKM; 2026-09-19 ~21:35):**
[byenzyme/enzyme](https://github.com/byenzyme/enzyme)
(license **null**; **63★** this pass, SIGNAL ★62) —
catalysts ≠ summaries. compile-time System One.
guidance ≠ hook. ~350×/1000× *theirs*. Do not copy
`curl | bash` (`notes.md` §94).
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
70.8% lexical (exploratory: questions revised after the first full run);
`Dicklesworthstone/skillranker` from live session context
(**VOI / abstention; 52★; hook fail-open** — see below);
LlamaIndex selectors fail closed or a declared default.
[`rajdhakad9826/routeKit`](https://github.com/rajdhakad9826/routeKit):
Jev estimates task *requirements*; code applies hard constraints and a
deterministic cost/quality/latency policy — Jev does not pick the model
(**Hypothesis** until measured on *your* catalog; `notes.md` §33).
**Session-sticky first-prompt route (Empirical as README machine,
2026-09-18 ~18:46):**
[jev-adaptive-thinking](https://github.com/jxu-dev-c/jev-adaptive-thinking)
classifies the first user prompt for `jev-auto`, then **locks**
provider/model for the process-local session; later requests never
reclassify. Timeout / missing first-round text / no stable session
ID → lock `gpt-5.6-sol` (fail-closed fallback, not passthrough).
Same family as routeKit. License null this pass. Live testing left
to the deployer. Do not copy dylib/YAML (`notes.md` §58).
**Harness plugins (brief, ~19:48):**
[dsh-jev](https://github.com/buberlo/dsh-jev) — DeepSeek Harness
decision layer; a model answer can only gate, never widen a
permission; failure never produces an allow; not on npm.
[opencode-system-one](https://github.com/emirbartu/opencode-system-one)
— OpenCode plugin; every Jev call fails open; license null.
Do not copy plugin JSON (`notes.md` §59).
**OMP/pi acceptance + route (Empirical as README fail
polarity, 2026-09-18 ~21:39):**
[omp-jev-extensions](https://github.com/luw2007/omp-jev-extensions)
— `jev_acceptance_gate` before done (Choice `{accepted,
rejected}`, not a boolean); `jev_route` subagent topology +
tier. **Fail-open** if Jev missing/timeout/malformed;
fail-open paths `confidence: 0`. Distinct from
pi-jev-approver (fail-closed without a key). Do not copy
bun / `~/.omp` (`notes.md` §61).
**OMP prompt suppression (Empirical as measured traffic +
labelled corpus, 2026-09-18 ~22:38):**
[omp-greenlight](https://github.com/SemetricLabs/omp-greenlight)
— grades gated tool calls; suppresses the approval prompt
when Jev says allow. **1,013 calls / 10 sessions / 8.95
session-hours.** Default preset **40.9%** prompts removed;
**0 of 94** unsafe auto-approvals on a 140-row labelled
corpus (live traffic has no labels). Operator owns
thresholds; the plugin **never self-tunes** the safety bar.
Not a sandbox; host `bash.patterns: deny` fires ahead.
Agent prose never sent (0→3 corpus misses). Never shadows a
built-in tool. Distinct from specpi-jev-guard (single danger
score; static fast-path miss), toolgate, interlock, and
omp-jev-extensions (fail-open *route*). Composes with
waymode. Do not copy `omp plugin` / YAML (`notes.md` §62).
**Skill-library VOI (Empirical as README architecture;
correction vs §7 fail-closed; 2026-09-19 ~01:47):**
[skillranker](https://github.com/Dicklesworthstone/skillranker)
— Jev two-pass (wide Choice then fit Nouls) from live
session context; both passes include **"none of these"**.
Advisory: the agent follows user instructions. Claude
prompt-hook maps recommendation failures to **quiet
exit-zero** (never blocks the agent). CLI keeps meaningful
exit codes. Libraries >254: Quill lexical prefilter admits
≤254 + none. Explicit requests resolve locally first.
Local feedback / replay without a new Jev call. **Hunch:**
pay to load a skill iff it changes the next step.
Compose with decision-combinators (control plane, not chat).
Distinct from skill-broker (grants). Do not copy cargo
(`notes.md` §66).
**Hermes pre-agent skill intervention (Hypothesis / outline
only — not a production recipe):**
[skill-broker](https://github.com/adamjralph/skill-broker)
— `PROJECT-OUTLINE.md` is authoritative. Deterministic code
owns catalog, profile policy, limits, and **grants**. Jev
scores relevance/confidence over authorised candidates and
**never grants access**. Candidates ≠ grants. Jev down →
foundation-only; never broaden access. Replayable route
evidence. Distinct from jev-hermes (route ≠ memory) and
from shipped routers on this card. Language/license null
this pass. Do not copy an install (`notes.md` §62).
**Sibling contrast this hour (delta, not a re-fold;
2026-09-19 ~02:38):** README now restates the outline;
still project-definition (`docs/adr` appeared; no
runtime). Same evidence≠authority doctrine as
[turnstile](https://github.com/zyphr-labs/turnstile)
(runtime authorize after policy; missing Jev → Review)
and opposite polarity from
[skillranker](https://github.com/Dicklesworthstone/skillranker)
(advisory VOI; hook fail-open). skill-broker **grants**
live in code. `notes.md` §67.
**Codex MCP host adapter (Empirical as README
architecture; ranking unbenchmarked; 2026-09-19
~02:38):**
[jev-in-codex](https://github.com/teempai/jev-in-codex)
— `jev_select_capability` / `jev_search` / `jev_triage`.
Caller supplies the catalog; server never executes
capabilities or sees Codex internals. Independent Nouls,
batched four; rec ≥ 0.5 is a **provisional heuristic**.
Absent key / errors → **lexical fallback** (local scores
are not model probabilities). Experimental MVP; MIT.
Distinct from jev-routing (Go host adapter, **not MCP**)
and jev-sift (topology A classify-first). Do not copy
npm / `config.toml` (`notes.md` §67).
**Harbor roster-size harness + Pi strip-roster (Empirical
as README architecture; no live Jev numbers this pass;
2026-09-19 ~04:39):**
[pi-jev-skill-bench](https://github.com/iamdin/pi-jev-skill-bench)
— BM25 vs Jev at roster **50 / 100 / 200 / 500**; 43 gold;
token/USD = chars/4; experiment harness not a production
claim. Cite only after `out/results-*.md` exists.
[pi-jev-skill-suggestion](https://github.com/iamdin/pi-jev-skill-suggestion)
— strip `<available_skills>`; two-stage (mean Noul 0.30 →
chunked Choice ≤254+none → shortlist 3 → fits 0.40);
fail-open; **no key → no-op**. Tool mode is a tools≠use
cousin (hopes the agent calls `skill_suggest`); auto mode
runs every prompt. Contrast skillranker (advisory VOI) /
skill-broker (grants) / jev-in-codex (caller catalog).
Do not copy `pi install` (`notes.md` §69).
**Constrained optimizer + S1 features (Empirical as live
analysis *shape*; 2026-09-18 ~23:40):**
[slo-router](https://github.com/zeeshan8281/slo-router)
— Jev supplies bounded task / exactness / external-evidence
features; a constrained controller picks the cheapest
backend meeting quality + latency SLO floors. Fail-open to
deterministic local features on timeout/invalid. Exactness
raises the quality floor; **never overrides** context or
capability. On their fixture, Jev preserved the same
routes/accuracy as the local path and raised p95 E2E
**77.93 → 490.38 ms** (~6.3×). 3/8 task-label disagreements
did not change routes. Eight-row demo is **not** a model
benchmark. License null this pass. **Hunch:** System One
belongs on the feature side of a constrained optimizer,
never as the sole hard gate on the hot path. Distinct from
routeKit (unmeasured) and bitrate-advisor (soft affinity
inside a cap). Do not copy uvicorn / OpenRouter
(`notes.md` §63).
[`trietphan/jev-claw`](https://github.com/trietphan/jev-claw) is the
same split for OpenClaw (classify axes; `decide()` maps the route; path
regex floors risk). [`nekowasabi/jev-routing`](https://github.com/nekowasabi/jev-routing)
is a host adapter, not an MCP plugin: compact, then one Choice + done,
then one schema (`notes.md` §44).
**Host-adapter surface delta (2026-09-19 ~07:49):**
same [jev-routing](https://github.com/nekowasabi/jev-routing)
binary now lists **Cursor Agent CLI** and **Devin CLI**
beside Claude Code / Codex / Grok Build. Still not MCP.
Do not re-card; do not copy ports (`notes.md` §72).
**Hermes plugin branded as Jev is Agnes (identity lock;
2026-09-19 ~07:49):**
[hermes-plugin-jev](https://github.com/Mrmimee/hermes-plugin-jev)
(README MIT / GitHub SPDX null) — Choice/Noul/Score
*shape* over **Agnes 3.0 Flash** chat-completions.
Distinct from hermes-jev-router (TypeSafe
WHETHER/HOW/WHAT). Do not copy `~/.hermes`
(`notes.md` §72).
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
**Pi System-One control plane (Empirical as README + npm
tests, no live quality numbers; 2026-09-19 ~06:43):**
[pi-jev-control](https://github.com/goodruizhan/pi-jev-control)
— task/model router, skill/memory/context gates, review
gate, GUI action router in one Pi extension. License null;
v0.3.0 private. Compaction never modifies the on-disk
session; GUI < threshold → unknown, never force-click.
Distinct from omp-jev-extensions / jevons / pi-heed / pi-om.
Do not copy `pi install` (`notes.md` §71).
**Competing NAR agent-routing (Empirical as README_EN;
audit, not endorsement; 2026-09-19 ~16:52):**
[Cerebellum-2B](https://github.com/mkeco/Cerebellum-2B)
(Apache LICENSE / GitHub SPDX other; **1★**; Hub
`mkzero/Cerebellum-2B-*`) — pointer over caller-supplied
candidates on `POST /v1/decide`. **Not** TypeSafe
`/v1/systemone`; do not paste a Cerebellum URL into
typesafe-sdk `base_url`. Wire-compat and agent-routing
are **separate** Harbor axes. Claimed 94.92% vs Jev
81.1% *theirs* is **unverified** — same discipline as
openJev-verdict-2.0. `ActEscalate` ≥0.50 still soft.
mkeco GitHub ≠ mkzero Hub. Skip Archer. `notes.md` §87.
**Jev-first bounded agent (Empirical as README;
2026-09-19 ~17:25):**
[stanley-code](https://github.com/devagrawal09/stanley-code)
(MIT; **20★**) — NL → one workflow; deterministic
gather + fixed-choice Jev; **code owns decisions**.
Empty findings ≠ approval. Router 0.6/0.55/0.15 still
soft. Pi fallback unverified. Human
`--promote-candidate` only. `jev-code` 0.0.1 does
nothing; 0.1.0 not on npm. Soft Noul ≠ hard safety.
Do not copy `npm ci` / `TYPESAFE_API_KEY`
(`notes.md` §88).
**Price workers, not the conversation (Empirical as
README; 2026-09-19 ~17:25):**
[jevsubrouter](https://github.com/leftspace89/jevsubrouter)
(MIT; **4★**) — bind the sub-agent model at
`PreToolUse`; keep the orchestrator's cached prefix.
Turn hook is advice. Fail-open. Low conf → balanced,
never silent down. Stats are counts, not dollars.
**≠** jev-gateway **≠** slo-router. Do not copy
marketplace / `~/.jevsub.env` (`notes.md` §88).
**Cheap decision layer / skill honor (Empirical as
README; 2026-09-19 ~17:49):**
[grok-bot-jev](https://github.com/Bodila51/grok-bot-jev)
(MIT; **1★**) — classify before browser/retry/research.
Shadow then honor. Skill cannot force a bot that
ignores it. A/B proxies ≠ tokens. **≠** jevsubrouter.
Do not copy skill paste (`notes.md` §89).
**APA harness cousin (Empirical as README; 2026-09-19
~17:49):**
[apa-agent-harness](https://github.com/AiPersonacademy/apa-agent-harness)
(MIT; **0★**) — policy verbs + 0.85 gate + shadow.
“Mathematically fulfilled” overclaim. Unpublished npm
`@aipersona/agent-harness`. **≠** AntonioCoppe/jev-harness.
Do not copy npm (`notes.md` §89).
**Offload classify/screen/score/verify (Empirical as
README; 2026-09-19 ~18:41):**
[yuyang2230/jev-agent-skill](https://github.com/yuyang2230/jev-agent-skill)
(MIT; **0★**) — leftover writer vs cheap decide via
OpenCode Zen. yuyang2230/jev-agent-skill
jev-1.13-free, not `jev-latest`. $0 is a Zen-tier
claim. **≠** GodsBoy/jev-agent-skill-router. Do not
copy `ZEN_API_KEY` (`notes.md` §90).
**Classifier not generator (Empirical as README;
2026-09-19 ~18:41):**
[jev-techstack-classifier](https://github.com/swap-mitra/jev-techstack-classifier)
(license null; **0★**) — plain English → ranked
stack. jev-techstack-classifier stack_config.json
only. Worker has no key. Do not copy wrangler
(`notes.md` §90).
**Pointer shell (Empirical as README; 2026-09-19
~18:41):**
[tpellet/hunch](https://github.com/tpellet/hunch)
(MIT; **0★**) — pick/why/is/run over stdin/PATH/man.
tpellet/hunch exit 3. never-execute list. Pin
`jev-1.13.0`. **≠** carldaws/hunch. Do not copy
`cargo install` (`notes.md` §90).
**Judge harness as control API (Empirical as README;
2026-09-19 ~19:47):**
[judgekit](https://github.com/lexingtonhibiki/judgekit)
(MIT; **0★**) — judgekit YAML classify/score/route/verify.
n=130 97.7% *theirs*. **≠** JudgeBench. Do not copy
`.env` (`notes.md` §91).
**Verdict-in-code (Empirical as README; 2026-09-19
~19:47):**
[typed-judge-kit](https://github.com/Ascurse/typed-judge-kit)
(MIT; **0★**) — typed-judge-kit verdict-in-code.
Thresholds from labels. MIN_LABELS=20. `notes.md` §91.
**Policy-constrained skill select (Empirical as README;
2026-09-19 ~19:47):**
[hermes-switchyard](https://github.com/bgrablin/hermes-switchyard)
(MIT; **0★**; v0.4.1) — hermes-switchyard ≠
hermes-jev-router ≠ hermes-plugin-jev. Advisory; never
loads skills; hosted routing not claimed. Do not copy
plugin install (`notes.md` §91).
**Decision-as-Plugin (Empirical as README; 2026-09-19
~19:47):**
[openrouter-jev-mcp](https://github.com/ctmx/openrouter-jev-mcp)
+ [typesafe-mcp](https://github.com/cyrusasco/typesafe-mcp)
+ [FrancoisChastel/jev-code](https://github.com/FrancoisChastel/jev-code)
(**1★**) + [claudecode-jev-marketplace](https://github.com/skylence-org/claudecode-jev-marketplace)
+ [mcp_jev](https://github.com/pedroknigge/mcp_jev)
+ [jev-skill](https://github.com/codaaiteam/jev-skill).
ctmx/openrouter-jev-mcp Decision-as-Plugin.
FrancoisChastel/jev-code ≠ npm jev-code.
claudecode-jev-marketplace fail-open not hot path.
pedroknigge/mcp_jev packs not ask_jev.
cyrusasco/typesafe-mcp noul deadband 0.35–0.65.
codaaiteam/jev-skill jevtypesafeai.com ≠ TypeSafe.
Do not copy `npx` / keys (`notes.md` §91).
**Self-hosted econ / retrieval / enterprise / CU / hybrid / Laya / demos (Empirical as README; 2026-09-19 ~20:41):**
Foq ~25ms/2.2GB local. rev prefill-only + HF jev-0.5b.
robfrase/jev planning memo. typesafe_agent_gates 27/27 / 31/31.
EpicEric/safe-sh static remainder. pastepilot Confirm before act.
Jev-Reranker live Jev not yet measured. sessionwise opt-in relevance.
jev-search pointer sieve. 400ms Salesforce WebMCP.
Always **savka777/jev-search**. **≠** kazuhideoki/jev-search
**≠** superagents-lab/jev-search.
typesafe-scheduler-diagnostics advisory. droidjev screenshot-free.
Tewoto1 jevcu planner still writes. ha-conversation-jev Jev→Grok.
dsh-jev can only gate. jev-classification-benchmark specified not run.
jev-luna-pagerduty p≥0.50. meldltd/meldecision laya-go ONNX.
laya-doom never pixels. logixism/laya-api empty README.
akpsahan/laya ≠ Archer. choxos/jevchess engine owns truth.
jev-drive sim not AV. story-arc Jev never authors.
jev-hs-assistant HS6. golergka/jev-plays-starcraft-2 UI-verified ≠ API Victory.
awesome-jev-use-cases catalog. Nibir1/typesafe-go ≠ official.
rh-guard owns the gate cousins (`notes.md` §92).
**Decision ledger / GEPA HITL (Empirical as README; 2026-09-19 ~21:23):**
fingerprint after redact. recall vs decide.
publish fingerprints+answers. CI replay as Harbor cousin.
Cache hit ≠ correctness. hyperspaceai/jevcache ≠ kushals256/jevcache.
human labels only. score never auto-accepts.
production capture flywheel. sutro-sh/jev-align ≠ caiovicentino/jev-align.
rh-guard owns HIT-as-truth and training-score auto-accept
(`notes.md` §93).
**Compile-time System One / JA replica / NAR cluster
(Empirical as README + HF card + X; 2026-09-19 ~21:35):**
guidance ≠ hook. catalysts ≠ summaries.
compile-time System One. unofficial ≠ TypeSafe.
format_version modernbert-jev/1.
Argos1111/jev_local ≠ us/jev-local ≠ kunchenguid/local-jev.
LFM default ≠ ModernBERT backend.
Nemotron ≠ TypeSafe Jev. not a calibrated replacement.
djev-dev complements djev-spark. images as Choice options.
Laya essay numbers *theirs*. Router/OOD confidence.
hosted bootstrap ≠ silent TypeSafe.
rh-guard owns guidance-as-hook / unofficial-local-as-Jev /
hosted-bootstrap silent FALLBACK / LFM-default-as-JA-softmax /
Nemotron “not calibrated replacement” / Laya
confidence-without-competence (`notes.md` §94).

**Decision-as-plugin / evidence / integrity / physical / replica (Empirical as README; 2026-09-19 ~21:41):**
difficulty + policy thresholds + JSONL trace.
jev-codex-pilot model + reasoning depth.
keep/shadow/hybrid/reject.
quarry evidence projection.
Frank-ZY-Dou/awesome-jev robotics/3D/control.
one-dollar-tahoe TypeSafe Jev defense eval.
jevguard calibrator/cache/escape.
jev-ci-selector CI shadow mode.
llama-jev llama.cpp replica.
petercr/jev-orchestrator ≠ FleeexCorp/jev-orchestrator.
seb4ez/jevguard ≠ AseemPrasad/JevGuard ≠ pablozr/JevGuard.
webNeat/llama-jev ≠ WiktorB2004/llama-index-jev.
rh-guard owns injection-firewall / CI-gate cousins
(`notes.md` §95).
**Decision Graph Protocol / calibrated meaning-grep /
Archer-arch family gap (Empirical as README + spec;
2026-09-19 ~17:40):**
Decision Graph Protocol frame→assess→commit.
app retains permissions/effects.
Jev-first assessor-neutral.
guarded commit / receipt/next frame.
assessment batching.
hard-gating DGP as safety theater.
numerous-com/dgp ≠ TypeSafe official.
jegrep calibrated path+range Nouls.
no embeddings/index/daemon.
~$0.01–0.03 typical. agent --json.
can1357/jegrep ≠ Bentlybro/jevgrep ≠ uehaj/jev-semgrep.
Archer-arch fidelity.
kev family OOD 0.76–0.77 vs Jev 0.86.
block-causal isolation.
pointer/readout CE-trained.
/v1/systemone drop-in.
replica honesty.
rh-guard owns the silent-FALLBACK cousin; rh-guard
**does not own** protocol envelope / ranking fail-open /
replica honesty (`notes.md` §98).
**Cost-derived / typed-callback overlays (Empirical as
README target design; 2026-09-19 ~18:43):**
[Kungie/gut](https://github.com/Kungie/gut)
(GitHub Apache-2.0 / LICENSE MIT / pyproject Apache-2.0
*theirs*; **0★**; pre-alpha) — cost-sensitive
decision theory × System One probabilities → control
flow. thresholds derived from costs not hard-coded.
YES / NO / UNSURE from cost_false_yes / cost_false_no /
cost_human. auto-batching same-object questions.
Default `on_unsure="raise"` is app policy, not a
System One hard gate. Kungie/gut ≠ tpellet/hunch
≠ carldaws/hunch.
[Illusion47586/judge](https://github.com/Illusion47586/judge)
(TypeScript MIT; **0★**; `@brkn-labs/judge` 0.1.0) —
judgment vs generation. deterministic execution after
probabilistic judgment. exactly one app-owned callback.
explicit uncertain branch. Illusion47586/judge ≠
lexingtonhibiki/judgekit ≠ Ascurse/typed-judge-kit.
Overlays, not species. Soft Noul ≠ hard safety
(`notes.md` §99).
**Hourly 1943 overlays (`notes.md` §100):**
[southpolesteve/probably](https://github.com/southpolesteve/probably)
(TypeScript MIT; **3★**) — Jev IS the if-statement.
judgments/probabilities drive branches. text model only
writes prose. interpreter owns variables/loops/budgets/replay.
otherwise maybe / confidence gate. chaos samples after the
gate. southpolesteve/probably ≠ carldaws/hunch ≠ feelings ≠
Kungie/gut ≠ Illusion47586/judge ≠ tidymodels/probably.
[samdotmak/jev-recall](https://github.com/samdotmak/jev-recall)
(MIT; **6★**) — retrieve by relevance not resemblance.
one calibrated yes/no per memory in one request. pointer
mode 17/18 19/20 *theirs*. embedding resemblance misses the
allergy. samdotmak/jev-recall ≠ jev-search ≠ jev-sift ≠
carryforward ≠ chopratejas/invalidate.
[chopratejas/invalidate](https://github.com/chopratejas/invalidate)
(Apache-2.0; **11★**) — memory leases ended by new evidence.
six Nouls then fixed rules in code. 0 of 157 false
invalidations. questions/plans/directives are not evidence.
unsure → review queue. host keeps the store.
[mizchi/jev-lint](https://github.com/mizchi/jev-lint)
(TypeScript MIT; **13★**) — name↔body / comment truth /
test-claims. mizchi/jev-lint is mizchi/jevlint rename. no
shipped rule has severity error. ~1 in 5 findings wrong
*theirs*. Soft Noul ≠ hard safety (`notes.md` §100).

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

## 7. Capability kernel / human-confirmed gate

**Method**: change the *trust boundary*, not the after-the-fact
"is this dangerous?" question. Two named shapes this hour
(`notes.md` §59):

1. **Capability kernel.** The LLM is ring 3; a kernel it cannot
   talk to is ring 0. Secrets never enter the agent (canaries and
   placeholders only). The action space is closed. A judgment-class
   model is a **sensor**; ordinary policy code decides BLOCK / ASK
   / ALLOW. Type-safe ≠ correct; irreversible stays behind a
   threshold **and** a human.
2. **Human-confirmed kill.** The model recommends; the operator is
   the only actuator. Re-check identity immediately before the
   irreversible signal. Shields override the judge. Displayed
   explanations are app-owned mapped text, not raw model prose.

**Transfers**: Leveson sensor ≠ constraint (`mappings.md` §8);
structural prove ∩ remainder (`mappings.md` §18); fail-closed on
the irreversible act (`mixed-architecture.md`). **Does not
transfer**: a launch-week firewall that asks "dangerous?" after
the LLM already decided with **real secrets in scope**; treating
toolgate (pre-exec of a *proposed* call) as the same product as a
kernel that never showed the secret; letting mapped UI copy be
the model's free-form reason.

```text
stunt_double = canaries + placeholders + allowlisted actions   # code
sensor       = parallel Nouls / Choice on the proposed act     # model
policy       = BLOCK | ASK(human) | ALLOW + placeholder swap   # code
kill         = human confirm after identity re-check           # not the model
```

**Example (Empirical as README architecture, 2026-09-18 ~19:48):**
[interlock](https://github.com/somoore/interlock) — twelve-hazard
Noul battery ~100 ms; `policy.py` is the product; 38-case
regression set tunes the local judge, **not a blind paper**.
Distinct from [toolgate](https://github.com/fdemir/toolgate)
(allow/block/review on a proposed tool; Jev is not authorization;
real args may already be in scope). rh-guard crossover: eval-
integrity is a different hole from a ring-0 kernel; do not merge
products. Do not copy pip / `INTERLOCK_ARMED` how-to.
**Protocol envelope cousin (Empirical as README + spec,
2026-09-19 ~17:40):**
[dgp](https://github.com/numerous-com/dgp) —
Decision Graph Protocol frame→assess→commit.
app retains permissions/effects.
Jev-first assessor-neutral.
guarded commit / receipt/next frame.
assessment batching.
The application owns state, permissions, guards, and
execution. A model is neither a security boundary nor
the source of execution authority (*theirs*).
hard-gating DGP as safety theater.
numerous-com/dgp ≠ TypeSafe official.
**≠** waymode **≠** AgentGhost **≠** actiongate.
Soft Noul ≠ hard safety (`notes.md` §98).
**Human-confirmed cousin (Empirical as README safety model):**
[port-cleanup](https://github.com/epiphany-dynamics/port-cleanup)
— Jev Stop/Keep/Your-decision; kill recs need conf ≥ 0.8;
identity re-check before SIGTERM; shields override; TCP only;
tiny final race (no pidfd). Gate UX for Augustus + rh-guard.
Do not copy Keychain how-to.
**Permission vs probability (Empirical as measured
suppression, not a kernel; 2026-09-18 ~22:38):**
[omp-greenlight](https://github.com/SemetricLabs/omp-greenlight)
— Jev is still the sensor; the **operator** owns the
auto-approve bar; the plugin never self-tunes it. Host deny
rules remain the constraint and fire first. Default 40.9% /
0 of 94 *theirs* on the labelled corpus. Not a sandbox; not
interlock (secrets may already be in the agent's world).
Do not copy YAML (`notes.md` §62).
**Spoken confirm ≠ auth (Empirical as README; voice;
2026-09-19 ~10:01):**
[jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser)
— `destructive ≥ 0.5` → say "confirm". README *theirs*:
convenience, not a guarantee. Anyone who can reach the
control port drives the browser. Sensor, not an
interlock. rh-guard owns the gate cousin. Do not copy
`npm` (`notes.md` §82).
**Wrap-as-execution ALLOW/ASK/DENY (Empirical as
README; 2026-09-19 ~10:20):**
[AgentGhost](https://github.com/reddpy/AgentGhost)
— the wrap *is* the tool's execution function;
rules first; ASK/DENY throw; `failMode: closed`.
Judge swappable. Provider-hosted tools out of
reach. **≠** actiongate **≠** toolgate **≠**
jev-use. rh-guard owns the gate cousin. Do not
copy `npm` (`notes.md` §83).
**Privilege ≠ verdict / effect-based shell gate
(Empirical as certification; 2026-09-18 ~23:40):**
[construct-auto-classifier](https://github.com/godspede/construct-auto-classifier)
— fast-allow/deny <1 ms, then Jev Choice allow/deny + nine
independent risk Nouls. Allow only if Choice allow at
operator-owned `minConfidence` (0.6) **and** every risk
below `riskThreshold` (0.7). Missing/low-conf/high-risk/
failed call = deny (fail-closed). `sudo status` can be a
safe read. Jev: **0** dangerous allowed / 975 decisions;
every chat model leaked (16–104). Pair with dinostomp
(audit the instrument) and omp-greenlight (operator-owned
dial). Distinct from toolgate / greenlight / jevgate /
interlock. **Hunch:** contracts on effects, not surface
tokens. **Landed-script trust** (byte-identical to the
remote default branch; default on; trusts whoever
controls that remote). **Headless ≠ auto-approve:**
escalation becomes deny-and-report, not a pending prompt
and not an allow (`notes.md` §68). Do not copy bun / agy
(`notes.md` §63).
**Typed escalate/continue/abort baton (Empirical as README
+ 40 tests; 2026-09-19 ~04:39):**
[jev-handoff](https://github.com/shitianfang/jev-handoff)
— MCP two-way handoff. Escalation reasons:
needs_generation / not_typeable / low_confidence /
backend_error. Gate `allow` **never grants**. Fail-open
(Jev down → typed escalate). Inverted loop: executor
enumerates, Jev picks, LLM woken only on escalate.
Vercel drops confidence (margin fallback not calibrated).
No independent quality bench. Same author as wakegate.
Do not copy npx / mcp.json (`notes.md` §69).
**Toolbelt sensors, not policy (notes only; 2026-09-19
~04:39):**
[jev-security-scan](https://github.com/win4r/jev-security-scan)
(MIT; stdlib; local rules then nine Nouls; dual p≥0.85 +
locate; four synthetic samples; not a cert; cousin
is-malicious).
[jev-decisions](https://github.com/bojansandhaus/jev-decisions)
(MIT; 1★; 25 prepared reviews; **advice, never stop
commands**; auto hooks off).
[jev-vs-llm-guardrails-intent-router](https://github.com/TeoMastro/jev-vs-llm-guardrails-intent-router)
(license null; 218 labelled items; `summary.md` **404
this pass** — do not invent numbers; README block ≥0.70).
**rh-guard owns the reward-hack angle.**
**Jev supplies evidence, code owns authority (Empirical as
README slogan; 2026-09-19 ~00:39):**
[actiongate-jev](https://github.com/omkarghugarkar007/actiongate-jev)
— deterministic policy / RBAC / schemas / limits own
ALLOW | REVIEW | BLOCK. Jev (via OpenRouter) is semantic
evidence only. A positive model score **never overrides** a
deterministic security failure. Six narrow questions, never
one vague "is this safe?" Financial / destructive /
credential **fail closed** if Jev is down. 500-case eval is
label-baseline integrity, **not** model accuracy. Early MVP.
Distinct from toolgate / interlock / construct / greenlight.
**Hunch:** canonical sensor≠constraint slogan for the
class. Do not copy pnpm (`notes.md` §64).
**Persist constraints across compaction (Empirical as
79-session bench; 2026-09-19 ~05:46):**
[pi-heed](https://github.com/Nyarlathoteppppp/pi-heed)
— conversational policy as structured state; replayed
after compaction without calling Jev again. Jev
classifies KEEP/LIFT/…; **never writes policy**.
Side-effecting calls checked before they run. Fail-open.
Shadow default. *Theirs:* v0.8.0+Jev recall 98.5% /
false block 0.0% / $0.000058; mid-session rule change
8/13 off vs 0/13 on. Distinct from actiongate
(RBAC/schema). Do not copy `pi install` (`notes.md` §70).
**Pi control-plane tool/GUI gates (Empirical as README;
license null; 2026-09-19 ~06:43):**
[pi-jev-control](https://github.com/goodruizhan/pi-jev-control)
— deterministic fast-path then Jev on uncertain tools;
GUI confidence below threshold → `unknown`, **never
force-click**. Distinct from pi-heed (constraint ledger)
(`notes.md` §71).
**jev-use PreToolUse gate (Empirical as 12/12 + Vercel
margin; 2026-09-19 ~06:43):**
[jev-use](https://github.com/shitianfang/jev-use)
— deny/ask only; **fail-open**; 12/12 *theirs*; Vercel
drops confidence so margin default 0.4. Same author as
jev-handoff. Gate never grants (`notes.md` §71).
**Commit-msg hook: fail-open on instrument failure
(Empirical as 13 labelled; 2026-09-19 ~07:49):**
[commitjev](https://github.com/yodablocks/commitjev)
— hook **blocks only on a warning**; a failed check is
not a reason to refuse. Middle band is review, never a
verdict. Credential regex cannot tell a fixture from a
key (correct failure direction). Do not copy hook
install (`notes.md` §72).
**Turnstile clone (Empirical as README architecture;
2026-09-19 ~01:47):**
[turnstile](https://github.com/zyphr-labs/turnstile)
— deterministic policy first; Jev semantic remainder
only after permit; allow/review/deny; receipts +
threshold replay with no new model calls. Jev **never
grants** authority policy denied. Missing Jev / timeout
→ **Review**. Starting 0.85 deny / 0.35 review are **not
calibrated**. Experimental alpha; no npm; Claude adapter
defaults observe + Jev off. Demo uses fixed judgments
(enforcement, not accuracy). Same doctrine as actiongate;
different product. Do not copy bun (`notes.md` §66).
**Advance/coverage ledger (Empirical as README +
BEYOND-JEV.md; 2026-09-19 ~02:38):**
[seal](https://github.com/Reasonofmoon/seal)
— **No seal, no advance.** Jev answers questions; SEAL
answers whether the world may change and **shows the
exception queue**. Every seal stamps `coverage.path` ∈
`{auto | escalate | human | code}`. Mint ≠ product
brain. Deterministic first (`provider: code:…`). Effects
stay locked while escalations are open. MIT; zero runtime
deps. Do not copy `scripts/demo.sh` (`notes.md` §67).
**Never-confidently-wrong kernel (Empirical as TLA+ +
1,080 golden chaos table; 2026-09-19 ~02:38):**
[jev-labs](https://github.com/copyleftdev/jev-labs)
— TLA+ owns the protocol (quorum 3 of 5; stability gate
above identity noise floor 0.042; TLC 1,049,750 states /
0 errors). Jev is the noisy oracle. Golden pharmacy
rounds *theirs*: **0** wrong across none/realistic/severe
(severe: 314 correct / 46 escalated). Escalate is
allowed; a confident wrong is not. Synthetic, **not**
clinical. Inverse of soundness theater: do not hard-gate
a soft judgment without that path. Do not copy
`verify.sh` (`notes.md` §67).
**Counterexample**: post-decision "is this dangerous?" with AWS
keys still in the prompt. **Test**: delete the sensor — the
constraint and the closed action space still hold; a canary use
is a catch; a human still confirms the irreversible act.
**Human every action (Empirical as README; 2026-09-19
~17:49):**
[Essentiel-Jev](https://github.com/JacquesGariepy/Essentiel-Jev)
(license null; **0★**) — Jev SENSOR; LLM drafts; human
approves every write; read-back. Essentiel-Jev never authority. 0.75
provisional. **≠** jevmail **≠** mailjay. Do not copy
`.env` (`notes.md` §89).
**Pointer-shell never-execute (Empirical as README;
2026-09-19 ~18:41):**
[tpellet/hunch](https://github.com/tpellet/hunch)
(MIT; **0★**) — `run` proposes from PATH/man; never-execute
list (`rm` refused even with `--yes`). tpellet/hunch
exit 3 abstains. **≠** carldaws/hunch. `notes.md` §90.
**Tab close fail-open (Empirical as README; 2026-09-19
~18:41):**
[tab-bouncer](https://github.com/MANISH007700/tab-bouncer)
(MIT; **0★**) — one call ≤120 tabs. tab-bouncer
pinned/audio/current never closed. Reopen.
chrome:// never touched. `notes.md` §90.
**Pause-if-no-Jev civ sim (Empirical as README;
2026-09-19 ~18:41):**
[ORIGIN-CIVILIZATION](https://github.com/JacquesGariepy/ORIGIN-CIVILIZATION)
(LICENSE MIT / SPDX NOASSERTION; **1★**) — Jev every
voluntary action; LLMs plan never decide. ORIGIN
pause-if-no-Jev. validResponse sums-to-1. **≠**
Essentiel-Jev. `notes.md` §90.
**Soft-score vs hard-argmax (Empirical as README;
cross-ref rh-guard; 2026-09-19 ~19:47):**
[typed-gate](https://github.com/harshpuri84/typed-gate)
(MIT; **0★**) — typed-gate band [0.40,0.60] is refusal.
0.51 is not a yes. 0 wrong/0 omit/117 review *theirs*.
rh-guard owns the gate cousin.
[pi-jev-gate](https://github.com/fivethirty/pi-jev-gate)
(MIT; **0★**) — pi-jev-gate fail-closed; choice is the verdict.
Ask band removed. **≠** pi-jev-approver. `notes.md` §91.
**Confirm-before-act / static remainder (Empirical as README;
cross-ref rh-guard; 2026-09-19 ~20:41):**
[jev-pastepilot](https://github.com/buberlo/jev-pastepilot)
(MIT; **0★**) — pastepilot Confirm before act. Fail-open
missing key. [safe-sh](https://github.com/EpicEric/safe-sh)
(AGPL-3.0; **1★**) — EpicEric/safe-sh static remainder.
[typesafe_agent_gates](https://github.com/ThiagaoBR/typesafe_agent_gates)
(Apache-2.0; **0★**) — typesafe_agent_gates 27/27 / 31/31.
rh-guard owns. `notes.md` §92.
**HIT-as-truth / training-score auto-accept (Empirical as README;
cross-ref rh-guard; 2026-09-19 ~21:23):**
[hyperspaceai/jevcache](https://github.com/hyperspaceai/jevcache)
— Cache hit ≠ correctness. A HIT is a sensor, not a
proof. Sharing foreign fingerprints as calibrated truth
is trust theater.
[sutro-sh/jev-align](https://github.com/sutro-sh/jev-align)
— human labels only; score never auto-accepts;
production capture flywheel. A training score is a
sensor, not an accept. **≠** caiovicentino/jev-align.
rh-guard owns HIT-as-truth and training-score
auto-accept as gate cousins; Augustus owns placement.
Soft Noul ≠ hard safety. `notes.md` §93.
**Guidance ≠ hook / unofficial-local-as-Jev /
hosted-bootstrap silent FALLBACK / LFM dual-backend /
Nemotron not-calibrated (Empirical as README;
cross-ref rh-guard; 2026-09-19 ~21:35):**
[byenzyme/enzyme](https://github.com/byenzyme/enzyme)
— guidance ≠ hook. Compiled `when asked` is
attention, not PreToolUse deny. Catalyst similarity
is a sensor, not a gate. hosted bootstrap ≠ silent
TypeSafe. Name which backend answered.
[argos1111/modernbert-ja-310m-jev](https://huggingface.co/argos1111/modernbert-ja-310m-jev)
+ [Argos1111/jev_local](https://github.com/Argos1111/jev_local)
— unofficial ≠ TypeSafe. Local p is not TypeSafe
calibration. LFM default ≠ ModernBERT backend.
Do not collapse the runtime into the Hub card.
[pst2154/Nemotron_Jev](https://github.com/pst2154/Nemotron_Jev)
— Nemotron ≠ TypeSafe Jev. not a calibrated
replacement. Laya Router/OOD confidence:
Khmer 0.000 @ 0.952 *theirs* is
confidence-without-competence. rh-guard owns
these as gate cousins; Augustus owns placement.
Soft Noul ≠ hard safety. `notes.md` §94.

**Soft judgment integrity / injection-firewall (Empirical as README;
cross-ref rh-guard; 2026-09-19 ~21:41):**
[seb4ez/jevguard](https://github.com/seb4ez/jevguard)
(MIT; **0★**) — jevguard calibrator/cache/escape.
`UNRESOLVED_OR_OTHER`; `AMBIGUOUS_STATE` top p&lt;0.40
or margin&lt;0.15. **≠** hyperspaceai/jevcache.
[guilhem/jev-ci-selector](https://github.com/guilhem/jev-ci-selector)
(license null; **0★**) — jev-ci-selector CI shadow mode.
Shadow default; enforce opt-in; skip_below 0.05 is an
experiment. Timeout/no-key → keep all.
[PavitarSinghArneja/one-dollar-tahoe](https://github.com/PavitarSinghArneja/one-dollar-tahoe)
(MIT; **0★**) — one-dollar-tahoe TypeSafe Jev defense eval.
~74 demo; README has no ASR/FPR. Do not copy attacks.
rh-guard owns. `notes.md` §95.

## 8. Decide → policy → LLM leftover cascade

**Method**: one typed decide contract, ordinary code as the
router, a generator only where leftover *text* must be written.
Three Harbor-shaped compare arms share the contract so the
policy never knows the backend: native-probability decide (one
call), verbalized JSON confidence (one call), constrained
single-token logprobs (one call per question). **Transfers**:
Noul 0.5 is cannot-tell and is **never rounded** into auto;
Score confidence 0.0 is a flat distribution and is **never
acted on**; hard flags (injection) always review even with an
LLM configured. LLM hook optional — unset degrades to human
review, the run still completes. **Does not transfer**: treating
self-reported `"confidence"` as a Noul; multiplying eight
parallel answers into a joint; hosted Jev as a default for
real customer mail (compliance first; the `DecisionBackend`
seam is the local-head answer). Distinct from dual-process-ai
(S1/S2 metaphor; routing accuracy unmeasured).

```text
prepare = strip quoted history / signature / cap          # code
decide  = 8 typed questions, one shared Answer schema     # model (any backend)
policy  = auto | review | llm                             # code, thresholds
leftover = draft category/priority/summary JSON           # LLM only if policy says so
```

**Example (Empirical as README architecture + mock compare,
2026-09-18 ~20:43):**
[jav-email-cascade](https://github.com/skiingfalcon/jav-email-cascade)
— 74 labelled synthetic emails; jev / gen-json / gen-logprob
arms; ~$0.034/1k emails *theirs*. Mock finding: gen-json
confidence essentially flat → almost none cleared the acting
threshold; gen-logprob works at 8× calls. A live jev vs
generative comparison is the point of running it, not a table
to invent here. License null this pass. Do not copy uv /
`.env`. `notes.md` §60.
**Counterexample**: rounding Noul 0.49/0.51 into auto-act;
asking a chat model the eight questions and treating the
JSON `"confidence"` as calibrated. **Test**: the same emails
through all three backends; report raw accuracy, acted
accuracy, and mean confidence on wrong answers; injection
fixtures never auto.
**Inbox cousin without leftover LLM (Empirical as README;
2026-09-19 ~07:49):**
[mailordinal](https://github.com/Milo318/mailordinal)
— same sandwich, no generator required: nine typed
signals → 100-point policy → ranked queue. Humans own
the review lane. Life/business. Independent of TypeSafe
(`notes.md` §72).
**Read-only Gmail trays (Empirical as README; 2026-09-19
~17:49):**
[jevmail](https://github.com/fazlerocks/jevmail)
(MIT; **3★**) — tray + urgency + human-wrote via
Gateway. `gmail.readonly`. ~3¢ / ~1 min per 1k
*theirs*. **≠** mailordinal **≠** mailjay. Independent.
`notes.md` §89.
**macOS proposed writes (Empirical as README;
2026-09-19 ~17:49):**
[mailjay](https://github.com/secondfret/mailjay)
(license null; **0★**) — reviews proposed actions;
archive/trash, not permanent delete. **≠** jevmail
readonly. `notes.md` §89.
**Civ leftover planner (Empirical as README;
2026-09-19 ~18:41):**
[ORIGIN-CIVILIZATION](https://github.com/JacquesGariepy/ORIGIN-CIVILIZATION)
— typed decide is Jev; leftover text is an LLM plan
that never decides. ORIGIN pause-if-no-Jev.
validResponse sums-to-1. **≠** Essentiel-Jev.
`notes.md` §90.
**Independent `/v1/decide` leftover (Empirical as
README; 2026-09-19 ~19:47):**
[codaaiteam/jev-skill](https://github.com/codaaiteam/jev-skill)
— leftover writer vs hosted decide.
codaaiteam/jev-skill jevtypesafeai.com ≠ TypeSafe.
Do not copy `JEV_API_KEY` (`notes.md` §91).
**Decision-as-plugin leftover (Empirical as README;
2026-09-19 ~21:41):**
[petercr/jev-orchestrator](https://github.com/petercr/jev-orchestrator)
(MIT; **0★**) — next-act Choice; code owns policy.
difficulty + policy thresholds + JSONL trace.
GitHub “difficulty” is not a live Score.
[Charlyhno-eng/jev-codex-pilot](https://github.com/Charlyhno-eng/jev-codex-pilot)
(MIT; **0★**) — jev-codex-pilot model + reasoning depth.
Thin overlay; leftover execution is Codex.
[SunnyKikiHK/jev-replacement](https://github.com/SunnyKikiHK/jev-replacement)
(license null; **0★**) — keep/shadow/hybrid/reject.
20-case *theirs* failed the cost gate; LLM remains
fallback. `notes.md` §95.
**Public decide-backend cousin (Empirical as README;
2026-09-19 ~08:37):**
[classifier-dev](https://github.com/mrmps/classifier-dev)
— spam/inbox/feedback over HTTP; leftover LLM is
*fallback when Jev is down*, not the product. Policy
(hold / route / act) still lives in the caller.
`notes.md` §73.
**Open NAR cousin (Empirical as README;
2026-09-19 ~09:07):**
[NandhaKishorM/laya](https://github.com/NandhaKishorM/laya)
— same sandwich without a hosted Jev: Router picks
the checkpoint, policy stays in the caller, 0.85 is
still soft. `notes.md` §76.
**Compile leftover (Empirical as README;
2026-09-19 ~21:35):**
[byenzyme/enzyme](https://github.com/byenzyme/enzyme)
— Decisions uses Jev (`ENZYME_JEV_MODEL`); catalyst
*generation* uses a separate LLM (`OPENAI_MODEL`).
compile-time System One. guidance ≠ hook. Policy
(when asked) is compiled guidance, not leftover
prose that decides. `notes.md` §94.

## 9. Closed-vote computer-use

**Method**: drive a task with nothing but closed votes. Code
constructs every available option from the environment's
state, the goal, and an explicit fact register. A
judgment-class model assigns probabilities and picks. Code
acts, verifies the effect, undoes what did not work, and
keeps values read off the environment. **Transfers**: type
without generation (values from goal / facts / page only);
irreversible risk votes never default; inspectable rejected
alternatives. **Does not transfer**: a planner LLM that
proposes free text; inventing fill values; treating Jev's
`completed` / done vote as verified success when the host
has server state to check. Distinct from Stagehand (LLM
fallback when pick abstains) and Cua-S1 (not TypeSafe Jev).

```text
observe = numbered controls / typed actions the host already owns
options = code builds from observation ∪ goal ∪ fact register
vote    = Choice / Noul: done? off-path? which action?
act     = existing handler or Chromium; never generated selectors
verify  = before/after vs intended effect; undo reversible misses
```

**Example — harness (Empirical as README architecture,
2026-09-18 ~21:39):**
[JevOnly](https://github.com/buluoray/JevOnly) (Apache-2.0) —
no planner LLM. Chromium first env; core is
environment-agnostic. Worked Wikipedia compare: 11 steps, 43
Jev calls, ~$0.014, 17 s *theirs*. `risk ≥ 0.50` never
default. Do not copy `run.sh` (`notes.md` §61).
**Example — product (Empirical as README + eval suite):**
[waymode](https://github.com/mossburgh/waymode) (MIT) — the
**app** keeps handlers, permissions, validation, and state.
Jev selects among live typed actions; a new control enters
the next snapshot without a matching model tool. Default
p ≥ 0.7; 8 steps. Evidence 24/26 and 34/36 *theirs* —
bounded development evidence, not a self-driving proof. Jev
selects the field; it does not generate fill text. Not on
npm. Do not copy AI_GATEWAY (`notes.md` §61).
**Hot-click cousin (not closed-vote; same observe→score→act
hole; 2026-09-19 ~00:39):**
[ego-jev](https://github.com/jiangkoumo/ego-jev) — indexed
viewport table; Jev picks operation+target; code owns the
loop; optional text model only for type. `--until` in code
beats Jev `done`. n=3 medians ~2×, not a bench. Distinct
from this card's no-planner extreme (`notes.md` §65).
**Observe→score→act namesake (Empirical as README;
2026-09-19 ~18:41):**
[ZHUBoer/ego-jev](https://github.com/ZHUBoer/ego-jev)
— Ego Lite observe/act; Jev `choose` over compact page
state. ZHUBoer/ego-jev reserved `__none__`.
runWorkflow completed ≠ success. Exact work local.
Agent still plans (not closed-vote).
**≠** jiangkoumo/ego-jev. `notes.md` §90.
**Observe→score→act cousins (not closed-vote; Empirical as
README; 2026-09-19 ~19:47):**
[jev-browser-agent](https://github.com/smartdio/jev-browser-agent)
— smartdio/jev-browser-agent ≠ ZHUBoer/ego-jev.
conf&lt;0.6 escalates to the outer LLM (not closed-vote).
280–740 ms *theirs*.
[omp-jev-web](https://github.com/Dakai/omp-jev-web)
— Dakai/omp-jev-web DONE ≠ proof. Overlay 5.9 s / 0
refusals *theirs*. OMP agent still plans (not closed-vote).
**≠** omp-greenlight.
[hari007sh/jev](https://github.com/hari007sh/jev)
— hari007sh/jev ≠ dannote/jev. Local cross-encoder
+ voice CU. Local encoder still plans (not closed-vote).
Teacher is `systemone generate`. License null. `notes.md` §91.
**Observe→score→act cousins (not closed-vote; Empirical as
README; 2026-09-19 ~20:41):**
[droidjev](https://github.com/mkruglikov/droidjev)
(MIT; **0★**) — droidjev screenshot-free. AX → typed
pick → adb. find ~0.6 s/iter *theirs*. **≠**
jev-ultrafast **≠** typesafe-computer-use.
[jevcu](https://github.com/Tewoto1/Computer-use-and-control-with-Jev)
(license null; **0★**) — Tewoto1 jevcu planner still writes.
Jev picks op+target. Preview default. Not closed-vote.
`notes.md` §92.
**Physical/control atlas (not closed-vote; Empirical as README;
2026-09-19 ~21:41):**
[Frank-ZY-Dou/awesome-jev](https://github.com/Frank-ZY-Dou/awesome-jev)
(license null; **0★**) — Frank-ZY-Dou/awesome-jev robotics/3D/control.
Text-state, not pixels. One seed-0 ≠ a rate.
Do not re-card jev-drone / khordoo / HA-Jev.
`notes.md` §95.
**Adversarial cousin (Playwright executes, Jev chooses;
license null; 2026-09-19 ~04:39):**
[browser-jev](https://github.com/DowLucas/browser-jev) —
code-only checks first; sample from the distribution not
argmax; fail only high conf **and** high severity. Visual
blind. Same inverted-loop family as jev-handoff
(`notes.md` §69).
**Decider≠executor cousin (Empirical as README; 2026-09-19
~05:46):**
[jeffrey](https://github.com/thomasbrueggemann/jeffrey)
(MIT) — Jev owns next-tool / progress / risk / done; the
LLM **only fills args**. Loop `Jev → tool → Jev`. Risk
Score ≥ 0.5 pauses mutating tools. Stuck ladder withholds
the looping tool (2 Jev / 0 steps). Distinct from this
card's no-LLM extreme and from jev-handoff (host baton).
Do not copy npm (`notes.md` §70).
**Hand no-text steps (Empirical as 95-call card; 2026-09-19
~06:43):**
[jev-use](https://github.com/shitianfang/jev-use)
(MIT v0.4.1) — plugin hands did-it-work / which-next /
severity / safe to Jev; writing stays with the LLM. p50
220 ms; batched 186 vs 2,672 ms; gate 12/12 *theirs*.
**≠** jev-ultrafast. Do not copy `npx` (`notes.md` §71).
**Never free-generates (Empirical as README demo;
2026-09-19 ~06:43):**
[jev-gpt](https://github.com/florian-hoenicke/jev-gpt)
(license null) — one typed question per word over a
WordNet / jina tree, then rank texts. ~400 calls / 75 s /
2¢ *theirs*. Architecture demo, not a product. Distinct
from jeffrey (pick next-tool). Do not copy API-key how-to
(`notes.md` §71).
**Continuous-control cousin (Empirical as README delta;
2026-09-19 ~09:50):**
[khordoo/jev-reflex-autonomy-lab](https://github.com/khordoo/jev-reflex-autonomy-lab)
— code owns physics/collisions; Jev only picks the next
typed flight action; optional S2 never flies and never
grants. Escalate without stalling. Local controller
**≠** githubnext/localjev. Experimental viz, not this
card's no-LLM extreme. Do not copy npm (`notes.md` §80).
**OCR+AX productized cousin (Empirical as README; MIT
**427★**; 2026-09-19 ~09:51):**
[typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use)
— hosted Jev picks among numbered OCR+AX items; code
acts. Writer is leftover generation, not a planner.
`done` is loop termination, not verified success.
Exclusive action set; split questions. 155× *theirs*
one screenshot. Distinct from this card's no-planner
browser extreme and from ego-jev hot-click. Do not
copy `uv` (`notes.md` §81).
**ASR voice-browser cousin (Empirical as README; MIT
**103★**; 2026-09-19 ~10:01):**
[jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser)
— Playwright executes; Jev only picks among snapshot
ids and regex spans. Partial-speech wait policy.
Spoken confirm ≠ auth. Distinct from this card's
no-planner extreme and from OCR desktop §81. Do not
copy `npm` (`notes.md` §82).
**Counterexample**: Stagehand extract `"pick"` with LLM
fallback sold as "no LLM" — pick is a fast path, not this
card. **Test**: every typed character exists in goal, facts,
or observed text; every irreversible act had a separate
risk vote; durable writes proved from host state, not from
Jev `completed`.
**CU source-study pointer (Empirical as README;
2026-09-19 ~17:49):**
[dairui1/jev-lab](https://github.com/dairui1/jev-lab)
— ultrafast speculative fan-out vs Cline flattened
`CLICK:3`. jev-desktop already MED — do not re-card.
0.65/0.70 still soft. **≠** BrendanH18/jev-lab.
`notes.md` §89.

**Hourly 2041 HIGH (`notes.md` §101).** Context-sieve
cousin: [cvsgireesh/jevusher](https://github.com/cvsgireesh/jevusher)
context-window admission control; VOI gate which tokens
are worth the expensive model; fail polarity per lens;
on small inputs lenses lose money; ≠ jev-sift ≠ winnow.
Skill/tool routing cousin:
[cannacre8ive/switchboard-ai](https://github.com/cannacre8ive/switchboard-ai)
cost-aware multi-model routing/escalation; decide vs do;
successful-task cost; ≠ ha-switchboard ≠ hermes-switchyard.
Capability-kernel cousin:
[MokiMeow/jev-fabric](https://github.com/MokiMeow/jev-fabric)
typed decision control plane; receipt ≠ authorization;
historical-v0 zero retained cases; ≠ jev-forge ≠ dgp.
Do not copy keys / `npm`. Soft Noul ≠ hard safety.

**Hourly 2145 HIGH (`notes.md` §102).** Question-lint
cousin: [yodablocks/jevq](https://github.com/yodablocks/jevq)
question-linting of Jev questions themselves; nine
jaggedness rules, no API key, no labelled data; static
lint ≠ measured separation; ≠ tenbin ≠ JevLint ≠
commitjev. Evidence cousin:
[WaynezProg/jev-kit](https://github.com/WaynezProg/jev-kit)
source-bound evidence checks; local quote mismatch
needs no API; exit 0 ≠ claim truth; ≠ jonathanavis96/jev-kit
(Airlock) ≠ jev-use ≠
jev-mcp. On-chain/edge cousin:
[humandebri/IC-Laya](https://github.com/humandebri/IC-Laya)
parity_verified stays false; model output never grants
Tx. Dual-judge cousin:
[copyleftdev/ember](https://github.com/copyleftdev/ember)
comparative framing is the usable judgment; prior
injection crowds out evidence; ≠ ember.js. Do not copy
keys / `mix` / `curl | sh`. Soft Noul ≠ hard safety.

**Hourly 2246 HIGH (`notes.md` §103).** Evidence-catalog
cousin: [reachjalil/system-one-bench](https://github.com/reachjalil/system-one-bench)
independent System One evidence catalog; 19 reviewed records; scores not one
leaderboard; no external record currently reproduced;
TokenTrim no-Jev matched hybrid 62.4%; ≠ mallahyari.
Eval cousin: [SivletLabs/jev-eval](https://github.com/SivletLabs/jev-eval)
21 tasks · 134 items · 208 questions; scenes from public
GitHub contracts, not production logs; ≠ willkelly ≠ 4esv.
Knowledge-work cousin:
[LYchoon/paper-radar-jev](https://github.com/LYchoon/paper-radar-jev)
arXiv paper radar with Jev relevance scoring; ranking ≠
calibration / 0.5 still soft; fail-open failed evals not
marked seen. Anti-pattern:
[erik-dunteman/ChatJev](https://github.com/erik-dunteman/ChatJev)
Jev classifier as autoregressive next-token predictor;
ChatJev-style soundness theater; ≠ dannote/jev ≠ jev-gpt.
Algorithmic cousin: [zzzzzec/jevsort](https://github.com/zzzzzec/jevsort)
parallel rank-prediction vs serial selection; independent
questions can conflict; ≠ jsort. Formal cousin:
[wufuju2023-cell/jev-alpha-proof-analysis](https://github.com/wufuju2023-cell/jev-alpha-proof-analysis)
calibrated decision head × AlphaProof value head;
implementation-layer isomorphism, semantic difference;
timeout = censoring; do not launder Noul as proof.
Do not copy keys / `npm` / `uv` / `.env`. Soft Noul ≠ hard
safety.

**Hourly 2340 HIGH (`notes.md` §104).** From-scratch cousin:
[hyusi2003/MiniSystemOne](https://github.com/hyusi2003/MiniSystemOne)
train calibrated ~27M from scratch; typed Q→prob dist / one forward pass / no LLM decode;
hyusi2003/MiniSystemOne ≠ Colvin0315/MiniSystemOne; description-only stub / size 5.
ORDER BY upgrade: [yodablocks/jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench)
ESCI hard probe fails four of six; jev_bool ECE 0.242 inversion 0.255;
do not re-fold §60 six-gates as new.
Workflow cousin: [karanb192/jev-architect](https://github.com/karanb192/jev-architect)
find/design/evaluate TypeSafe Jev decision loops; ≠ samtay32/jev-system-architect.
Anti-pattern: [Jairik/jev-distiller](https://github.com/Jairik/jev-distiller)
Jairik/jev-distiller size 1; distill-Jev UI stub / do not distill Jev as teacher of record.
Opportunity map: [licensedsaucer9-web/jev-opportunities](https://github.com/licensedsaucer9-web/jev-opportunities)
post-launch scored use-case map / Jev self-scores then human curation.
Scaffold cousin: [gavinHuang/jevinize](https://github.com/gavinHuang/jevinize)
Jev-inize a use case into classifier/router; gavinHuang/jevinize → simple-jev not TypeSafe.
Regression cousin: [VihaanAgarwal/jev-diff](https://github.com/VihaanAgarwal/jev-diff)
compare saved decisions / same label can still change the branch; not tested with a live Jev API key.
Constrained-AR anti-pattern: [zhangcy122/OpenJevPro](https://github.com/zhangcy122/OpenJevPro)
constrained logprob + temp/Platt ≠ Noul; OpenJevPro pastes openjev-sglang JevBench as own.
NAR cousin: [patelvishwa112/jev-system-one-rlcd](https://github.com/patelvishwa112/jev-system-one-rlcd)
SmolLM-135M / sub-70ms / 0 output tokens; demo P(True) 0.5052 / Choice conf 0.2872 / Score conf 0.0055.
Radar: [logicrw/awesome-jev-projects](https://github.com/logicrw/awesome-jev-projects)
source-backed Awesome Jev radar / 306+ commit-pinned; auto GitHub sync / Issue-only submissions.
Rival-aware scorer: [olanotolu/jevbetter](https://github.com/olanotolu/jevbetter)
hashed n-gram encoder / rival-aware attention; olanotolu/jevbetter vs jevlike starter.
Do not copy keys / `npx` / `pip` / `.env`. Soft Noul ≠ hard safety.

**Hourly 0042 HIGH (`notes.md` §105).** Judgment-surface
cousin: [Arohtea/jev-readout](https://github.com/Arohtea/jev-readout)
structured probability readouts; distribution > argmax;
Noul 0.5 midpoint; score is expectation not integer; bare
HTTP not SDK. Adapter cousin:
[gulagala001/jevify](https://github.com/gulagala001/jevify)
Jev-style Choice/Score/Noul from ordinary models; optional
DSH plugin; schema-valid ≠ calibrated; ≠ Mintzs/jevify.
Open-weight measurement:
[mourad-ghafiri/laya-rlcd-benchmark](https://github.com/mourad-ghafiri/laya-rlcd-benchmark)
Laya RLCD benchmark; 40.3% below constant-answer; ≠
yibie/laya-jev-lab. Edge cousin:
[SupremeDreamZ/jev-fastloop](https://github.com/SupremeDreamZ/jev-fastloop)
cheap fail-open semantic edge; second signal not sole;
FastLoopError catch; ≠ jev-ultrafast. Fan-out measurement:
[TheWebDevel/jev-fanout](https://github.com/TheWebDevel/jev-fanout)
asking more questions in one call; 0.980 at every N;
nearly not fully deterministic. RL teacher:
[harneet2512/reflexrl](https://github.com/harneet2512/reflexrl)
Qwen3-VL perception + Jev decisions train RL; 0 model
calls at deployment; VLM alone 1.7 vs +Jev 4.4; ≠
khordoo/jev-reflex-autonomy-lab. Independent cascade:
[yibie/laya-jev-lab](https://github.com/yibie/laya-jev-lab)
independent Jev API vs Laya; cascade 0.60 matches 78% at
1.8×; noul facts not judgements; ≠ dairui1/jev-lab ≠
BrendanH18/jev-lab. Locate vs decide:
[umstek/zero-shot-ie-bench](https://github.com/umstek/zero-shot-ie-bench)
GLiNER vs GLiFormer vs Laya vs Jev; extractors ≠ decision
engines; Laya dict-instructions collapse 58.3%. Throughput
arena: [angelgalvisc/snake-arena-jev-vs-llms](https://github.com/angelgalvisc/snake-arena-jev-vs-llms)
decisions-per-minute & cost; 204 moves vs 73; throughput
not intelligence; ≠ vtrivedy/jev-plays-games. Contract
cousin: [sathariels/jevcheck](https://github.com/sathariels/jevcheck)
behavioral contracts; pin expectations eval upgrades; raw
0.94 is not a release; ≠ jevals ≠ SivletLabs/jev-eval.
Evidence-linked SWE cousin:
[GaneshVG18/upgrade-radar](https://github.com/GaneshVG18/upgrade-radar)
evidence-linked dependency upgrade; Jev never generates
filenames; no_direct_evidence ≠ safe to merge; ≠
LYchoon/paper-radar-jev. Knowledge-work cousin:
[lirantal/discoprint](https://github.com/lirantal/discoprint)
discography theme/mood/complexity; five atomic questions
one call. Do not copy keys / `npm` / `npx` / `uv` / `.env`.
Soft Noul ≠ hard safety.



**Hourly 0145 HIGH (`notes.md` §106).** Architecture-probe cousin:
[uspraveen/Jevify](https://github.com/uspraveen/Jevify)
Turn any open LLM into System-One Jev; uspraveen/Jevify ≠ Mintzs/jevify ≠ gulagala001/jevify;
Jevify-any-LLM architecture probe; description-only stub / size 0.
Encoder-only: [Ruivalim/exu-base](https://github.com/Ruivalim/exu-base)
Train encoder-only calibrated decision models from a task sentence;
Exu is a toolkit, not a method; strictly proper scoring rule; Pre-alpha.
Recipe upgrade: [Colvin0315/MiniSystemOne](https://github.com/Colvin0315/MiniSystemOne)
scratch-trained calibrated decision model; typed Q → probability dists;
no published weights download URL; 90.5 seconds / 29.2% pipeline evidence.
Small-model recipe: [scienthoon/luce](https://github.com/scienthoon/luce)
Recipe for calibrated decision models — small model out; init → synth → train → eval → serve;
91.1 % / ECE 0.022 *theirs*; Jev zero-shot 75.1.
Trial: [RichardoMrMu/jev-mini](https://github.com/RichardoMrMu/jev-mini)
Put Jev's three headline claims on trial; 46x speedup / accuracy identical;
ECE 0.624 sentiment catastrophe; bigger model worse calibration.
Local JSON: [tapsin/jev-local](https://github.com/tapsin/jev-local)
JSON parse of generated text ≠ Noul; TypefAI JEV / Journal Entry Voucher.
Measurement: [goya4140/jev-reward-model-evaluation](https://github.com/goya4140/jev-reward-model-evaluation)
Jev 1.13 reward-model eval across 8 benchmark tracks; RewardBench v1 92.58%; Precise IF 50.63%.
[fstandhartinger/jevbench](https://github.com/fstandhartinger/jevbench)
classifier.dev fast tier 84.8 is Jev behind its own API; do not re-fold §78 v1.2 board as new;
Laya (421M) 70.1 now on board.
Formal compose: [AIGNLAI/ReflexRoute](https://github.com/AIGNLAI/ReflexRoute)
hard budget filter before Jev; Jev never asked to perform budget arithmetic.
[priyankark/jev-state](https://github.com/priyankark/jev-state)
Jev judges the next state, XState enforces transitions; simulation uses synthetic keyword fixtures.
Catalog: [v-modal/awesome-jev-tools](https://github.com/v-modal/awesome-jev-tools)
catalog gravity; ★339 live REST; curation is not endorsement.
[RadRebelSam/awesome-jev](https://github.com/RadRebelSam/awesome-jev)
crawler-maintained directory; Daily GitHub + npm sweep, human-merged.
HF ports: rdxtremity/jev-reranking query-side encoders, not a Jev replica;
onnx-community/system-one-qwen3.5-4b-scorer-ONNX CC-BY-NC-4.0; temperature 1.75;
transformers.js AutoModel cannot load this graph.
Consistency: This Space contains no benchmark result yet; 12-case plumbing fixture.
do not reopen or amend PR #23.
Do not copy keys / `npx` / `pip` / `.env`. Soft Noul ≠ hard safety.




**Hourly 0243 HIGH (`notes.md` §107).** Measurement-densify cousin:
[erendikmenn/jev-llm-router-benchmark](https://github.com/erendikmenn/jev-llm-router-benchmark)
Benchmark-driven Jev router and judge; cheap alone is not success;
Jev does not write, sum prices, or claim accuracy %;
Sol 94.2 / Luna 83.9 / Jev path 89.7;
19.2% Sol / 62.3% cost save / 4.5pp miss of 2pp non-inferiority;
p50 latency worse than Sol due to routing overhead.
erendikmenn/jev-llm-router-benchmark ≠ jev-rag-benchmark ≠ ryantsai/jev-llm-router.
Ticket: [aesaganda/jev-ticket-router](https://github.com/aesaganda/jev-ticket-router)
Express + node:sqlite; mock and Jev decision engines;
previous_ticket_count >= 3 is code; MIN_CONFIDENCE 0.6 still soft;
substring false positives;
aesaganda/jev-ticket-router ≠ SarathChandraBellam/jev-vs-llm-ticket-router.
Figure: [hoangngochuong24947-gif/jev-figure-router](https://github.com/hoangngochuong24947-gif/jev-figure-router)
Universal Figure & Diagram Router; confidence ≥ 0.85 hard-gate is theater;
generative AI banned from scientific plots; six visual branches.
Feedstock: hfdataset:Praveenrajus/jev-bench
human-labeled (state, question, label); 166,054 rows / 22 configs;
soft_label for human uncertainty; Praveenrajus/jev-bench ≠ fstandhartinger/jevbench.
Open ports: hf:NicolaiMTLassen/open-bonzi-jev
ternary bonsai System One GGUF; openjev's mechanism, Bonsai's weights;
Hub does not ship weights; 100/100 easy T/F is not Harbor;
label_mass ≠ correctness; stock llama.cpp Q2_0 silently gibberish;
NicolaiMTLassen/open-bonzi-jev ≠ NicolaiLassen.
hf:onnx-community/open-jev-deberta-v3-large-ONNX
transformers.js DeBERTa ONNX; source:com-kotobalabs/open-jev-deberta-v3-large;
temperature 1.05; AutoModel from_pretrained works;
onnx-community/open-jev-deberta-v3-large-ONNX ≠ system-one-qwen3.5-4b-scorer-ONNX.
Densify: [Heman10x-NGU/openJev-verdict-2.0](https://github.com/Heman10x-NGU/openJev-verdict-2.0)
107★ densify; GH 151M vs README 149.6M; PR #1 now closed unmerged;
do not re-fold §71 claim-audit as a beat.
Study: [wjdjdakf17/jev-study](https://github.com/wjdjdakf17/jev-study)
typed decisions, RLCD, confidence-gated routing; structured ≠ correct;
mock not live API; 26 tests; wjdjdakf17/jev-study ≠ baekenough/jev-study.
do not reopen or amend PR #23 or #24.
Do not copy keys / `npx` / `pip` / `uv` / `.env` / `OPENROUTER_API_KEY`. Soft Noul ≠ hard safety.





**Hourly 0345 HIGH (`notes.md` §108).** Open-reproduction + measurement-densify cousin:
Family cards: hf:NicolaiMTLassen/bonzi-27b-v2-jev
bonzi-27b-v2 / ternary-8b / 27b-v1 GGUF family densify;
WANLI-256 74.6% / 65.2% / 71.1% *theirs*;
Bonsai 1 27B Q1_0 runs on stock llama.cpp;
ternary still needs PrismML fork.
Ports: hf:mizchi/laya-multilingual-onnx
Laya multilingual ONNX WebGPU typed-decisions port;
63/63 selected answers / 5.1e-4 CPU / 1.2e-2 WebGPU.
hf:IamBusy/OpenJev-Vision
OpenJev Vision image classification + uncertainty;
CLEVR-4 held-out joint 0%.
hf:heman10x/openJev-verdict-2.0 twin tokenizer-only.
hfdataset:IamBusy/OpenJev-Vision-Research-v0.1 12,832;
294,912 derived targets not independent samples.
[UpHash-Network/mini-jev](https://github.com/UpHash-Network/mini-jev)
UpHash-Network/mini-jev is yuki-oshio transfer;
residual-head 9,222-param decreased 73/96→67/96.
Measurement PRIMARY: [ASEVlad/jev-injection-bench](https://github.com/ASEVlad/jev-injection-bench)
jev-injection-bench 11,900 labelled prompts;
Jev best ranking / Haiku better ECE 0.021 vs 0.058;
0.5–0.9 band is where Jev's numbers do not mean what they say;
Prompt wording moves panic 28%.
[manojlds/jev-dspy-bench](https://github.com/manojlds/jev-dspy-bench)
manojlds/jev-dspy-bench ≠ dspachos/jev-dspy ≠ jmanhype/jev-dspy-lab;
Jev agreement is similarity, never ground truth;
no aggregate quality grade or merge gate.
[sshariqali/jev-abstentionbench](https://github.com/sshariqali/jev-abstentionbench)
AbstentionBench-on-Jev rank 1 of 20 vs 2025 field;
question-asymmetry; forward-looking 0.465 never extreme.
[misakaikato/openkev](https://github.com/misakaikato/openkev)
openkev calibration layer not a runtime;
ECE vs coverage independent; select_threshold returns inf;
escalation catches uncertainty not ignorance;
misakaikato/openkev ≠ jaredpalmer/kev.
[goodrahstar/pdf-race](https://github.com/goodrahstar/pdf-race)
pdf-race Docling→Jev vs Gemini; parser owns the wall clock;
12/12 tie is a tie; titles selected not generated.
[ZeroX-01/jev-atlas](https://github.com/ZeroX-01/jev-atlas)
ZeroX-01/jev-atlas ≠ Zaious/jev-capability-atlas ≠ gorock007/jev-atlas;
catalog not endorsement.
[samyakjain0606/jev-is-here](https://github.com/samyakjain0606/jev-is-here)
flopcheck 16 calibrated tweet judgments; mechanical tells in code.
hfspace:BunsDev/laya-calibration-lab
Laya calibration lab Gradio MCP; T never changes argmax;
confidence ≠ top-label p; easy probe set refused;
40–48 rows too small to ship T.
do not reopen or amend PR #23 or #24 or #25.
Do not copy keys / `npx` / `pip` / `uv` / `.env` / `TYPESAFE_API_KEY` / `ANTHROPIC_API_KEY` / `HF_TOKEN` / `GEMINI_API_KEY`. Soft Noul ≠ hard safety.

**Hourly 0439 HIGH (`notes.md` §109).** Open-reproduction + measurement PRIMARY + applied class placements:
Hub jevify: hf:kushalpatil/jevify-gemma4-26b-a4b
Gemma-4 26B-A4B jevify classification+calibration;
Hub jevify merged LoRA ships weights;
PAWS 0.580/ece 0.288 is the weak cell;
kushalpatil/jevify-gemma4 ≠ Mintzs/jevify ≠ gulagala001/jevify ≠ uspraveen/Jevify;
GH kushalpatil07/jevify 404.
hf:kushalpatil/jevify-gemma4-26b-a4b-lora LoRA adapter twin not independent eval.
hf:kushalpatil/jevify-gemma4-e4b Gemma-4 E4B jevify;
smaller E4B slightly better OOD ECE than 26B-A4B.
hf:kushalpatil/jevify-gemma4-e4b-lora E4B LoRA stub card.
Family fill: hf:NicolaiMTLassen/bonzi-8b-v1-jev
bonzi Bonsai-8B v1 GGUF densify;
Bonsai-1.7B v1; Bonsai-4B v1;
WANLI-256 64.5% / 60.2% / 52.0% *theirs*;
rank #4 / #5 / #6 of 6.
Fork: [roadius2/ultra_laya](https://github.com/roadius2/ultra_laya)
roadus2 watch misspelling; lock roadius2/ultra_laya;
ultra_laya REVIEW defects;
default branch claude/laya-jev-review-gg5ppo.
Measurement PRIMARY: [AHTOOOXA/jev-cyrillic-audit](https://github.com/AHTOOOXA/jev-cyrillic-audit)
XNLI EN 88.3% ECE 0.032 → RU 77.3% ECE 0.096;
Δ −11.0 pp [−14.2,−7.8]; ECE +0.063;
MASSIVE no detectable difference at n=600;
confidence is function of p_max (r=1.000).
[JulesHuisman/jev-eval](https://github.com/JulesHuisman/jev-eval)
JulesHuisman/jev-eval scaffolding / README SHA c356a584 (was empty e69de29b);
JulesHuisman/jev-eval ≠ SivletLabs/jev-eval ≠ willkelly/jev-evaluation ≠ 4esv ≠ xxkuboxx ≠ onlyoneaman ≠ dayhaysoos/jevals.
[tunahansahin897/what-is-jev](https://github.com/tunahansahin897/what-is-jev)
947 repos scored; A 273 / B 302 / C 372; LLM rubric ≠ benches.
[Mishkun/judge-jev](https://github.com/Mishkun/judge-jev)
judge-jev 0.5 still soft.
Applied: [LiuHao-1443/jev-table-tennis](https://github.com/LiuHao-1443/jev-table-tennis)
7 bands 6/10 vs 40 bands 0/10.
[laguagu/jev-evidence-lab](https://github.com/laguagu/jev-evidence-lab)
source receipts + confidence slider re-policy without re-inference;
32/32 synthetic is smoke not production.
[hemanth/hfjev](https://github.com/hemanth/hfjev)
classify HF datasets across typed semantic dimensions.
[akash-kamat/jev-llm](https://github.com/akash-kamat/jev-llm)
pointer-not-generator 400 human-authored responses.
[chenmingtang830/jevgraph](https://github.com/chenmingtang830/jevgraph)
proposed ≠ authorized;
FewRel 160: Jev 85.0% vs lexical 13.125%;
gated 100% (95/95) coverage 59.375%.
[Towow-ai/jpp](https://github.com/Towow-ai/jpp)
J++ composable semantic computation language.
[whyashthakker/awesome-jev-use-cases](https://github.com/whyashthakker/awesome-jev-use-cases)
No benchmark winner is claimed.
[dog-last/awesome-jev](https://github.com/dog-last/awesome-jev)
phishing: naive 62.6% vs regex 91.8%; 5-atomic + LR 95.0% *theirs*.
[shinshin86/jev-aituber-tension-sample](https://github.com/shinshin86/jev-aituber-tension-sample)
AITuber tension ±15.
[shinpr/jev-reranker](https://github.com/shinpr/jev-reranker)
README npm global; repo is Rust.
[AHTOOOXA/git-confess](https://github.com/AHTOOOXA/git-confess)
git-confess code owns counting/blame/ratio;
httpx exhibit 11% (13/119) *theirs*.
[waterme7on/jev-paper-trader](https://github.com/waterme7on/jev-paper-trader)
90d trend +12.40% vs random +12.75% vs BH +41.71%;
5m win rate 25%.
Awesomejev 656 entries / 38,160 stars;
tracker likes 64 (+4) lastModified UNCHANGED;
Laya present; Blackwood ABSENT; Archer still promised_not_landed.
do not reopen or amend PR #23 or #24 or #25 or #26.
do not reopen or amend PR #23/#24/#25/#26.
Do not copy keys / `npx` / `pip` / `uv` / `.env` / `TYPESAFE_API_KEY` / `ANTHROPIC_API_KEY` / `HF_TOKEN` / `OPENAI_API_KEY` / `OPENROUTER_API_KEY`. Soft Noul ≠ hard safety.


**Hourly 0541 HIGH (`notes.md` §110).** Open-weight / RLCD / Blackwood watch + measurement PRIMARY + applied/theory placements:
Census densify: hf:BlackwoodAI/blackwood-rlcd
Blackwood tracker ABSENT; likes 2 gated manual.
hf:anthonym21/qwen3-0.6b-rlcd-decision r = c - p_a;
ECE 0.021; acc 0.807 vs warmup 0.746;
calibration beyond ~500 tokens unmeasured.
hf:larkooo/gemma-e2b-rlcd Independent primitive;
11.57s vs 54.10s · 4.67× · 120/128 *theirs*;
default path is pretrained Gemma probs not trained RLCD head.
hf:Meanblock/JEV-CPU GH Meanblock 404; lock leesk212/JEV-CPU;
softmax over letter slots ≠ Noul.
hf:impacte/mimir-lfm-openjev WANLI 0.741 vs openjev v2 0.77 *theirs*;
3-way NLI ≠ Noul.
hf:shreyanbr/system-one-distilled / gold / zeroshot
priority 0.464 = majority floor; banking77 contaminated;
raw margins not probabilities;
do not distill Jev as teacher of record (they distilled Haiku).

Hourly 0541 uniqueness lock: GH jev-haiku-benchmarking 404.
Measurement PRIMARY: [Running-Dolphins/jev-bench](https://github.com/Running-Dolphins/jev-bench)
“0.9 is not one number”; ranking ≠ calibration;
banking77 0.8–0.9 stated 0.86 actual 0.73 over-confident *theirs*;
≠ Praveenrajus/jev-bench ≠ fstandhartinger/jevbench.
[WallerChen/jev-measured](https://github.com/WallerChen/jev-measured)
$0.0000153–$0.0000226 vs circulating $0.0004 (~20×);
Score is 0..n-1 expectation not 0–1;
Noul has no confidence field;
TCP floor 198.8 ms;
type reliability is not a reason to choose Jev (json_schema 5/5);
gateway tax not one number.
[RadRebelSam/jev-decision-lab](https://github.com/RadRebelSam/jev-decision-lab)
Function-only 5/8 vs hybrid 8/8; 4/8 without Jev;
8 designed cases not conversion lift; ≠ RadRebelSam/awesome-jev.
[jackojacko05/compare-jev-bigquery-ai-functions](https://github.com/jackojacko05/compare-jev-bigquery-ai-functions)
200-row pilot Jev 86.5% 173/200 vs Gemini Flash-Lite 86.0% 172/200 vs Pro 87.0% 174/200 *theirs*;
not a ranking.
[Trecto34/openjev-fighting-ring](https://github.com/Trecto34/openjev-fighting-ring)
NLI Tetris argmax P(entail)−P(contradict).
[joshhu/jevtest](https://github.com/joshhu/jevtest)
情緒測謊器; 1q 396ms / 30q 567ms; ±0.03;
33q $0.000045 vs Gemini ~5× slower ~60× cost *theirs*;
≠ realZachi/jevtest.
hfspace:aahf/JevBenchmark
8-example Jev vs GPT-5.6 Sol ~64× cost 5.4× latency *theirs*;
synthetic; no inference; ≠ JevBench v1.2 §78.
[rhc98/awesome-jev](https://github.com/rhc98/awesome-jev)
Judged 3317 / listed 2560; Jev judges, code applies policy;
catalog ≠ endorsement.
[AiPersonacademy/Awesome-jev-use](https://github.com/AiPersonacademy/Awesome-jev-use)
APA “microsecond policy / zero hallucination” overclaim.
Applied: [erseco/questionator](https://github.com/erseco/questionator)
Client-side quiz; pointer from held docs; scanned-PDF warn;
CSP only api.typesafe.ai.
[grgy078033/grill-jev](https://github.com/grgy078033/grill-jev)
Jev judges / agent reasons / user decides;
selecting an option is not permission to implement;
degraded fallback.
[makefunstuff/jev-lsp](https://github.com/makefunstuff/jev-lsp)
pattern exact, judgement must clear floor;
no matching pattern → no model call;
not a correctness oracle;
$0.00022 vs chat $0.00306 *theirs*.
[nozomi-koborinai/jev-spec](https://github.com/nozomi-koborinai/jev-spec)
Spec vs artifact remainder;
treating 0.85 as 85% / minProbability hard-gate as Harbor.
[202620325-spec/Jev-LLM](https://github.com/202620325-spec/Jev-LLM)
VERIFY acquires discriminating evidence, never same-pool confidence-only rescoring;
fast/full/max are ceilings not sizes;
Solar writes, Jev chooses NEXT ACTION.
SemIf 2186★ (+20 vs §109 2166);
jevlike 1038★ (+7 vs 1031);
TypeAR 14★ flat;
AnotiaWang 96★ (+1 vs 95);
yibie/awesome-jev 490★;
Laya likes 802 (was 783);
tracker likes 64 flat, lastModified UNCHANGED;
Blackwood tracker ABSENT; Archer still promised_not_landed.
do not reopen or amend PR #23/#24/#25/#26/#27.
Do not copy keys / `npx` / `pip` / `uv` / `cargo` / `.env` / `TYPESAFE_API_KEY` / `ANTHROPIC_API_KEY` / `HF_TOKEN` / `OPENAI_API_KEY` / `OPENROUTER_API_KEY`. Soft Noul ≠ hard safety.



**Hourly 0743 HIGH (`notes.md` §113).** Measurement PRIMARY + open-weight/RLCD + skills/DecisionOps:
[ywchiu/jev_benchmark](https://github.com/ywchiu/jev_benchmark)
ywchiu/jev_benchmark ≠ Running-Dolphins/jev-bench ≠ Praveenrajus/jev-bench;
Gemma 4 31B 77.0% / Jev 1.13.0 61.4% / Laya 322M 0.0%;
restriction state 95.0% against 84.4%; None of the systems are particularly good at knowing when to stop and ask;
They skip the question and call a tool directly; 100% schema pass; six-field joint 48.8% vs 72.8%.
[siren2345/jev-single-decode-transformers](https://github.com/siren2345/jev-single-decode-transformers)
siren2345/jev-single-decode-transformers ≠ siren2345/jev-single-decode;
Split Transformers experiment from llama.cpp runtime.
[tanayvasishtha/jev-lab](https://github.com/tanayvasishtha/jev-lab)
tanayvasishtha/jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab ≠ yibie/laya-jev-lab;
Four experiments stress-testing TypeSafe's Jev: calibration, bundle bias, label bias, and ensembling;
second pass must be $0.00 from cache; The pages never call Jev.
[Heman10x-NGU/Verdict-open-jev](https://github.com/Heman10x-NGU/Verdict-open-jev)
Heman10x-NGU/Verdict-open-jev ≠ Heman10x-NGU/openJev-verdict-2.0;
TF-IDF + LogReg ECE 0.0207 vs Jev 0.1440; Verdict-open-jev 48.07% vs Jev 90.80%;
abstention combined recall 10.00%; p50 35.58 ms; K=25 (maximum capacity) 72.00%;
0.85 coverage 84.60% selective risk 1.18%.
26.1× faster than standard Qwen JSON generation; Jevify 90.0% / 167 ms CUDA graphs disabled.
Finding 1: Brier on stated confidence alone is a trap; grpo_rlcr 0.78 / ECE 0.084;
reliability 0.007 but resolution 0.000.
27 900 schema-driven decisions; 13 600 / 13 600 questions; candidate mass min 0.99999624.
22 configs · 166,054 rows · 4 calibration-gold; sha a39eba3f.
Student B MAE 0.148 / Pearson 0.836 / 86.0%.
pngwn/open-jev-laya-bench README 404; sha 9f69c742 likes 2.
HDFS 0.9933 (745/750) / retain 0.0084; BGL ERROR/FATAL protection 1.0000;
2,479 / 2,500 HDFS uncertain; cache hit 0.9648 (2412/2500); $0.153936 estimated;
E2 recomputes from saved probabilities.
Space sha eda59e0a; MASSIVE English 0.783 / Khmer 0.033 / Hindi 0.133;
40–48 rows too small to ship T; T never changes argmax.
[erayyilmmaz/jev-decisionops](https://github.com/erayyilmmaz/jev-decisionops)
ACT / REVIEW / FALLBACK; A provider failure, timeout, malformed output, or missing answer is **not** a policy outcome;
confidence is descriptive provider output, not a substitute for probability;
Quality denominators include only valid scored answers;
an exact halfway tie chooses the lower level.
[aiwithenoch/Jev-Skill](https://github.com/aiwithenoch/Jev-Skill)
aiwithenoch/Jev-Skill ≠ simplosophy/jev-skill ≠ laguagu/jev-skills;
The local path does not claim to turn a smaller checkpoint into Jev;
Low support becomes decision: "review"; MIT-0 SPDX NOASSERTION.
current-llm; 结构兼容，不是 Jev 模型能力.
[altryne/jevify](https://github.com/altryne/jevify)
altryne/jevify ≠ Mintzs/jevify ≠ gulagala001/jevify ≠ uspraveen/Jevify;
Find where Jev belongs. Design the questions. Measure the difference.
TypeAR-AI/TypeAR 301 → TypeLLM/TypeLLM; TypeLLM/TypeLLM 16★;
SemIf 2241★ (+34 vs §111 2207); jevlike 1051★ (+8 vs 1043);
AnotiaWang 98★ (+1 vs 97); yibie/awesome-jev 525★ (+19 vs 506);
Laya likes 864 (was 822); tracker likes 67 (+3 vs 64);
lastModified UNCHANGED `2026-09-20T04:29:16.000Z`;
do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#32/#33.
Do not copy keys / `npx` / `pip` / `uv` / `.env` / `TYPESAFE_API_KEY`. Soft Noul ≠ hard safety.


### 0920 jcr capability resolver (`notes.md` §116)

Place JCR as retrieve-wide → decide → evidence-set on a nested capability tree. Skills stay workflow+judgment; capabilities are individual operations. The resolver returns documentation; the harness owns execution, credentials, and checks. Soft scores ≠ hard gates. routing ≠ permission. docs ≠ authority to run. NiazMorshed2007/jcr ≠ skill-broker ≠ skillranker ≠ jev-sift ≠ jev-lens ≠ jevusher ≠ jev_select_capability.

Hourly 0743 uniqueness lock: Heman10x-NGU/Verdict-open-jev ≠ Heman10x-NGU/openJev-verdict-2.0; TF-IDF + LogReg ECE 0.0207 vs Jev 0.1440; Verdict-open-jev 48.07% vs Jev 90.80%; abstention combined recall 10.00%; p50 35.58 ms; K=25 (maximum capacity) 72.00%; 0.85 coverage 84.60% selective risk 1.18%; 26.1× faster than standard Qwen JSON generation; Jevify 90.0% / 167 ms CUDA graphs disabled; Finding 1: Brier on stated confidence alone is a trap; grpo_rlcr 0.78 / ECE 0.084; reliability 0.007 but resolution 0.000; 27 900 schema-driven decisions; 13 600 / 13 600 questions; candidate mass min 0.99999624; 22 configs · 166,054 rows · 4 calibration-gold; sha a39eba3f; Student B MAE 0.148 / Pearson 0.836 / 86.0%; pngwn/open-jev-laya-bench README 404; sha 9f69c742 likes 2; HDFS 0.9933 (745/750) / retain 0.0084; BGL ERROR/FATAL protection 1.0000; 2,479 / 2,500 HDFS uncertain; cache hit 0.9648 (2412/2500); $0.153936 estimated; E2 recomputes from saved probabilities; Space sha eda59e0a; MASSIVE English 0.783 / Khmer 0.033 / Hindi 0.133; 40–48 rows too small to ship T; T never changes argmax; siren2345/jev-single-decode-transformers ≠ siren2345/jev-single-decode; Split Transformers experiment from llama.cpp runtime; tanayvasishtha/jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab ≠ yibie/laya-jev-lab; Four experiments stress-testing TypeSafe's Jev: calibration, bundle bias, label bias, and ensembling; second pass must be $0.00 from cache; The pages never call Jev; Gemma 4 31B 77.0% / Jev 1.13.0 61.4% / Laya 322M 0.0%; restriction state 95.0% against 84.4%; None of the systems are particularly good at knowing when to stop and ask; They skip the question and call a tool directly; 100% schema pass; six-field joint 48.8% vs 72.8%; ywchiu/jev_benchmark ≠ Running-Dolphins/jev-bench ≠ Praveenrajus/jev-bench; ACT / REVIEW / FALLBACK; A provider failure, timeout, malformed output, or missing answer is **not** a policy outcome; confidence is descriptive provider output, not a substitute for probability; Quality denominators include only valid scored answers; an exact halfway tie chooses the lower level; aiwithenoch/Jev-Skill ≠ simplosophy/jev-skill ≠ laguagu/jev-skills; The local path does not claim to turn a smaller checkpoint into Jev; Low support becomes decision: "review"; MIT-0 SPDX NOASSERTION; current-llm; 结构兼容，不是 Jev 模型能力; altryne/jevify ≠ Mintzs/jevify ≠ gulagala001/jevify ≠ uspraveen/Jevify; Find where Jev belongs. Design the questions. Measure the difference; TypeAR-AI/TypeAR 301 → TypeLLM/TypeLLM; TypeLLM/TypeLLM 16★; SemIf 2241★ (+34 vs §111 2207); jevlike 1051★ (+8 vs 1043); AnotiaWang 98★ (+1 vs 97); yibie/awesome-jev 525★ (+19 vs 506); Laya likes 864 (was 822); tracker likes 67 (+3 vs 64); lastModified UNCHANGED `2026-09-20T04:29:16.000Z`; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#32/#33; notes.md §113

**Hourly 0646 HIGH (`notes.md` §111).** Measurement PRIMARY + datasets/Spaces + applied/skills/economics:
Calibration is not alpha. NO CURRENT ALPHA CANDIDATE.
ΔR² approximately +0.00084. Brier 0.2131387. ECE 0.0421875.
Adding Jev probability to deterministic volatility improved Brier by only 1.4058e-05.
[OrMizL/jev-compaction-bench](https://github.com/OrMizL/jev-compaction-bench)
default 0.5 keeps zero non pinned; keepResult median 0.14 to 0.17;
keepCall median 0.28 to 0.35; usable range is about 0.10 to 0.25;
7.8% to 57.9%; judges results it never sees; task-finish eval not built yet;
$0.002 per compaction.
[slavadubrov/sgr-judge-bench](https://github.com/slavadubrov/sgr-judge-bench)
slavadubrov/sgr-judge-bench ≠ slavadubrov/jev-judge-bench;
Jev 108/120 $0.083 0.34 s; Luna SGR 114/120;
paired Jev accuracy-difference intervals include zero; not evidence of equivalence;
GLM SGR 26/120 93 format failures; Terra-planned Jev hybrid 55/120.
[elyashium/atlas-replay-lab](https://github.com/elyashium/atlas-replay-lab)
rule-based by default, optionally Jev-backed; empty README;
missing key cannot break the experience.
[siren2345/jev-single-decode](https://github.com/siren2345/jev-single-decode)
prefill plus exactly one decode; softmax over A/B/C ≠ Noul;
BBQ 9,053/10,000 (90.53%); ECE 0.0890; Mean confidence 0.9943; overconfident;
score and noul not implemented.
DGUI 12 rows (was 6); INSTRUCT 119 rows likes 2.
hfspace:pngwn/open-jev encode the state once, decide everything in parallel;
0.740 accuracy against a 0.508 majority; ECE 0.047;
fine-tune's advantage ends where its 384-token training data does.
jasonkneen/open-jev ≠ pngwn/open-jev; same sha d41dc3cd.
Space does not call Jev; recomputes routing from saved probabilities.
200-case Jev 97.0% / 100.0% / 95.0% / MAE 9.22; synthetic repository benchmark.
Jev evaluations are advisory.
YehuiTang0316/jev-nlgrep ≠ Bentlybro/jevgrep ≠ can1357/jegrep ≠ uehaj/jev-semgrep;
default threshold 0.8 still soft; 40-line windows cannot prove whole function.
token-native sequential start/end Choice; Gemini/Haiku stubs not configured yet.
handful of hand-written examples, not a benchmark; Jev judged exactly what it was given.
laguagu/jev-skills ≠ laguagu/jev-evidence-lab ≠ Pleo2/awesome-jev-agent-skills.
contract_passed is not a claim of guaranteed factual truth;
Wilson lower bound 0.85 floor; fixture mode no savings claim.
SemIf 2207★ (+21 vs §110 2186); jevlike 1043★ (+5 vs 1038); TypeAR 15★ (+1 vs 14);
AnotiaWang 97★ (+1 vs 96); yibie/awesome-jev 506★ (+16 vs 490);
Laya likes 822 (was 802); tracker likes 64 flat, lastModified UNCHANGED;
do not reopen or amend PR #23/#24/#25/#26/#27/#28.
Do not copy keys / `npx` / `pip` / `uv` / `.env` / `TYPESAFE_API_KEY` / `JEV_KEY`. Soft Noul ≠ hard safety.

Hourly 0646 uniqueness lock: Calibration is not alpha; NO CURRENT ALPHA CANDIDATE; ΔR² approximately +0.00084; Brier 0.2131387; ECE 0.0421875; Adding Jev probability to deterministic volatility improved Brier by only 1.4058e-05; default 0.5 keeps zero non pinned; keepResult median 0.14 to 0.17; keepCall median 0.28 to 0.35; usable range is about 0.10 to 0.25; 7.8% to 57.9%; judges results it never sees; task-finish eval not built yet; $0.002 per compaction; slavadubrov/sgr-judge-bench ≠ slavadubrov/jev-judge-bench; Jev 108/120 $0.083 0.34 s; Luna SGR 114/120; paired Jev accuracy-difference intervals include zero; not evidence of equivalence; GLM SGR 26/120 93 format failures; Terra-planned Jev hybrid 55/120; rule-based by default, optionally Jev-backed; empty README; missing key cannot break the experience; prefill plus exactly one decode; softmax over A/B/C ≠ Noul; BBQ 9,053/10,000 (90.53%); ECE 0.0890; Mean confidence 0.9943; overconfident; score and noul not implemented; DGUI 12 rows (was 6); INSTRUCT 119 rows likes 2; encode the state once, decide everything in parallel; 0.740 accuracy against a 0.508 majority; ECE 0.047; fine-tune's advantage ends where its 384-token training data does; jasonkneen/open-jev ≠ pngwn/open-jev; same sha d41dc3cd; Space does not call Jev; recomputes routing from saved probabilities; 200-case Jev 97.0% / 100.0% / 95.0% / MAE 9.22; synthetic repository benchmark; Jev evaluations are advisory; YehuiTang0316/jev-nlgrep ≠ Bentlybro/jevgrep ≠ can1357/jegrep ≠ uehaj/jev-semgrep; default threshold 0.8 still soft; 40-line windows cannot prove whole function; token-native sequential start/end Choice; Gemini/Haiku stubs not configured yet; handful of hand-written examples, not a benchmark; Jev judged exactly what it was given; laguagu/jev-skills ≠ laguagu/jev-evidence-lab ≠ Pleo2/awesome-jev-agent-skills; contract_passed is not a claim of guaranteed factual truth; Wilson lower bound 0.85 floor; fixture mode no savings claim; SemIf 2207★ (+21 vs §110 2186); jevlike 1043★ (+5 vs 1038); TypeAR 15★ (+1 vs 14); AnotiaWang 97★ (+1 vs 96); yibie/awesome-jev 506★ (+16 vs 490); Laya likes 822 (was 802); tracker likes 64 flat, lastModified UNCHANGED; do not reopen or amend PR #23/#24/#25/#26/#27/#28.

**User-provided 0806 HIGH (`notes.md` §112).** Institutional HF voice / encoder ZS lineage:
people who compare Jev against GPT-5.6 has never fine-tuned BERTForXYZ for living and it shows; zero shot classifiers; scale them as much as decoder only models; many problems solved with LLMs could have been solved with them, it was a skill issue; opt for DeBERTa and ModernBERT ones; BERTForXYZ → DeBERTa → ModernBERT; Jev vs GPT-5.6 bakeoffs are a category error; encoder / ZS classifiers; institutional HF voice; quote *theirs*; do not invent accuracy numbers; softmax/ZS scores still ≠ calibrated Noul; soft scores ≠ hard gates; @mervenoyann; likes 421 / 189; impressions 35498 / 9613; multimodal image<>text ZS as perception front-end; hf:MoritzLaurer/deberta-v3-large-zeroshot-v2.0 likes 139; hf:MoritzLaurer/ModernBERT-large-zeroshot-v2.0 likes 72; Bart, bert, deberta, modernbert, these are all LLMs; Maziyar quoted; Jev is exemplar not the mandate; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29
people who compare Jev against GPT-5.6 has never fine-tuned BERTForXYZ for living and it shows. Jev vs GPT-5.6 bakeoffs are a category error. encoder / ZS classifiers. opt for DeBERTa and ModernBERT ones. multimodal image<>text ZS as perception front-end. softmax/ZS scores still ≠ calibrated Noul. soft scores ≠ hard gates. Do not copy `pipeline()` / `pip`.


**User-provided 0940 HIGH (`notes.md` §118).** Migration / question-design on-ramp:
Turn decision-shaped LLM prompts into proposed Jev primitives.
This is a conversion assistant, not an automatic guarantee of equivalent behavior.
Partial convertibility: Writing new text stays with an LLM.
Place only bounded Choice/Score/Noul; keep generation with the writer.
Heuristic conversion ≠ calibrated Noul. Soft proposal ≠ production gate.
alexwestco/llm-to-jev ≠ altryne/jevify ≠ Mintzs/jevify.
Do not copy `npm` / `TYPESAFE_API_KEY`. Soft Noul ≠ hard safety.

**Hourly 0843 HIGH (`notes.md` §114).** Measurement PRIMARY + hysteresis/policy + catalogs-as-lenses:
A hunch is a probability with a policy attached; { enter: 0.8, exit: 0.6 } is hysteresis; replay a policy change without inference; Decision models are providers, not the product; huncho ≠ Kungie/gut ≠ carldaws/hunch ≠ tpellet/hunch.
pretrained Qwen2.5 base ECE 0.030 (0.5B) / 0.040 (7B); instruct 0.302 / 0.269; ranking ≠ calibration.
calibration does not compose; Deferred Crispification; TCE / AMS; 25–60× headline withdrawn.
pd.cut bins by equal width while jeval bins by quantile; ECE 0.113 and ECE 0.076; jeval drift is not implemented yet.
g0runmezadam/what-is-jev IS tunahansahin897/what-is-jev (same GitHub id 1378007307); 947 repos scored; A 273 · B 302 · C 372; LLM rubric ≠ benches; catalog ≠ endorsement.
omni-/ask-jev ≠ pedroknigge/mcp_jev; Probabilities are advisory, not calibrated guarantees.
light_cutoff_applied_to_combination 0; recorded run, kinematic animation; Bring your own API key.
AND: product (independence assumed and recorded in the trace); circuit-vl-4b ≠ Archer.
vamsikrishna2421/jev-usecases ≠ whyashthakker/awesome-jev-use-cases.
xiaohuaxi/jev-study ≠ wjdjdakf17/jev-study ≠ baekenough/jev-study; 不是 benchmark; 概率没做 calibration.
Qwen2.5 ≠ Archer; Qwen 3.8 sparring ≠ Archer; Qwen/Qwen3.8-27B ≠ Archer; Archer still promised_not_landed.
SemIf 2237★ (+30 vs §111 2207); jevlike 1049★ (+6 vs 1043); TypeLLM/TypeLLM 16★; AnotiaWang 98★; yibie/awesome-jev 520★ (+14 vs 506); Laya likes 861 (was 822); tracker likes 66 (+2 vs 64) lastModified UNCHANGED; Blackwood likes 2 gated manual; Hub archerhume/4rcherhume HTTP 401.
do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35.
Do not copy keys / `npm` / `pip` / `uv` / `powershell` / `.env` / `TYPESAFE_API_KEY`. Soft Noul ≠ hard safety.

User-provided 0806 uniqueness lock: people who compare Jev against GPT-5.6 has never fine-tuned BERTForXYZ for living and it shows; zero shot classifiers; scale them as much as decoder only models; many problems solved with LLMs could have been solved with them, it was a skill issue; opt for DeBERTa and ModernBERT ones; BERTForXYZ → DeBERTa → ModernBERT; Jev vs GPT-5.6 bakeoffs are a category error; encoder / ZS classifiers; institutional HF voice; quote *theirs*; do not invent accuracy numbers; softmax/ZS scores still ≠ calibrated Noul; soft scores ≠ hard gates; @mervenoyann; likes 421 / 189; impressions 35498 / 9613; multimodal image<>text ZS as perception front-end; hf:MoritzLaurer/deberta-v3-large-zeroshot-v2.0 likes 139; hf:MoritzLaurer/ModernBERT-large-zeroshot-v2.0 likes 72; Bart, bert, deberta, modernbert, these are all LLMs; Maziyar quoted; Jev is exemplar not the mandate; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29.

Hourly 0843 uniqueness lock: A hunch is a probability with a policy attached; { enter: 0.8, exit: 0.6 } is hysteresis; replay a policy change without inference; Decision models are providers, not the product; huncho ≠ Kungie/gut ≠ carldaws/hunch ≠ tpellet/hunch; pretrained Qwen2.5 base ECE 0.030 (0.5B) / 0.040 (7B); instruct 0.302 / 0.269; 70.9% → 70.0% mean conf 74.1% → 96.7%; temperature scaling still matches it in-distribution; No Jev API was called; Qwen2.5 ≠ Archer; Qwen/Qwen3.8-27B ≠ Archer; 学習済みモデル v0.1 は準備中です; bool AUROC 0.523; 先頭だと0件、末尾だと250件; 温度を渡さない場合、確率は較正されていません; このリポジトリには Jev を呼ぶコードが存在しません; g0runmezadam/what-is-jev IS tunahansahin897/what-is-jev (same GitHub id 1378007307); 947 repos scored; A 273 · B 302 · C 372; LLM rubric ≠ benches; Data as of 2026-09-20; HEAD 895b9498; README SHA 3ae98c56; 13 focused checks and one mutually exclusive outcome; Probabilities are advisory, not calibrated guarantees; omni-/ask-jev ≠ pedroknigge/mcp_jev; pd.cut bins by equal width while jeval bins by quantile; ECE 0.113 and ECE 0.076; jeval drift is not implemented yet; rlaope/jeval ≠ dayhaysoos/jevals; calibration does not compose; ECE has exactly zero statistical power to detect the failure mode that kills trajectories; 25–60× headline withdrawn; P(all-correct): 0.0071 vs 0.0001; TCE / AMS; Qwen 3.8 sparring ≠ Archer; Deferred Crispification; light_cutoff_applied_to_combination 0; recorded run, kinematic animation; BANKING77 Accuracy BERT-Base 93.02 Jev 79.90; Analyse jev calibration (NLL, ECE) backlog; BERT figures are published supervised references, not zero-shot; 档位措辞效应 分数极差中位 0.50、最大 1.32; 修好后对照组是 0.01; 不是 benchmark; 概率没做 calibration; ~1,430 API calls, about $0.15; xiaohuaxi/jev-study ≠ wjdjdakf17/jev-study ≠ baekenough/jev-study; AND: product (independence assumed and recorded in the trace); chat model's stated confidence is not calibrated; circuit-vl-4b ≠ Archer; Bring your own API key; vamsikrishna2421/jev-usecases ≠ whyashthakker/awesome-jev-use-cases; catalog ≠ endorsement; SemIf 2237★ (+30 vs §111 2207); jevlike 1049★ (+6 vs 1043); TypeLLM/TypeLLM 16★; AnotiaWang 98★; yibie/awesome-jev 520★ (+14 vs 506); Laya likes 861 (was 822); tracker likes 66 (+2 vs 64) lastModified UNCHANGED; Blackwood likes 2 gated manual; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35; notes.md §114
**User-provided 0915 HIGH (`notes.md` §115).** NanoJev unified-games-v1 densify:
A 0.6B parallel decision model: states and questions in, complete probability distributions out. Zero output-token decoding.
One model, four games. ViZDoom Basic 128/128 vs Jev 56/128. held-out Maze 4/10 Snake 8/8 Basic 128/128 Predict 27/128.
not TypeSafe Jev; open replica / specialist gameplay S1. Game success ≠ calibrated Noul. local type boolean ≠ TypeSafe noul.
caijinchun/nanojev-arena ≠ liao96312/jev-arena-nanojev ≠ zwliJay/jev-forge ≠ NanoJev.
Do not copy `pip` / `snapshot_download` / `serve_decisions`.
User-provided 0915 uniqueness lock: TianyuCodings/NanoJev unified-games-v1 densify; A 0.6B parallel decision model: states and questions in, complete probability distributions out. Zero output-token decoding.; One model, four games; ViZDoom Basic 128/128 vs Jev 56/128; Predict Position 27/128 vs Jev 11/128; Maze 225 attempts vs Jev 2738; Snake 30 food / 256 steps; held-out Maze 4/10 Snake 8/8 Basic 128/128 Predict 27/128; Untuned Qwen3-0.6B baseline; 18,760 questions per variant; 16,333 ViZDoom; 896 Predict Position expert episodes; hard_lr1e5; mix weights 1/3, 1/3, 1/6, 1/6; Hub C-Tianyu/NanoJev revision unified-games-v1 likes 58; dataset C-Tianyu/NanoJev-Data likes 5; HEAD 618cea6d906d54e128360786d12f703fff2b1245; 1289★ / 158 forks / size 64035; README SHA 4190093c64ee75b26e9726daa3b00cbcf6d3157a; MIT; caijinchun/nanojev-arena ≠ liao96312/jev-arena-nanojev ≠ zwliJay/jev-forge ≠ NanoJev; not TypeSafe Jev; open replica / specialist gameplay S1; soft scores ≠ hard gates; Game success ≠ calibrated Noul; local type boolean ≠ TypeSafe noul; invented_signal false; do not reopen or amend PR #31/#32/#33/#35; notes.md §115


User-provided 0920 jcr uniqueness lock: NiazMorshed2007/jcr MIT; site https://jcr.niazmorshed.dev; topics ai-agents,jev,mcp; **4★**; HEAD `138b3832`; README SHA `2a49dbc1`; LICENSE SHA `46231303`; size **14850**; Jev Capability Resolver; one tool to find documented deterministic commands in a nested capability tree; returns context; **does not execute**; skills = workflow+judgment; capabilities = individual operations; format independent of Jev; proposed open standard exploration; classify (Jev) → optional OpenAI decompose compound → beam search geometric mean of routing probs; keep up to 3 paths ≥60% of best (JCR_BAND_RATIO 0.6); ambiguity / no-match / depth-limit explicit; soft scores ≠ hard gates; 0.6 band is application policy; routing ≠ permission; docs ≠ authority to run; sol-vs-opus5-20 *theirs*: 20 scenarios × 4 variants = 80 runs; lookup+explain only, no execution; Claude Opus 5: agent input 108,585→15,819 (−85%), cost $0.3700→$0.1222 (−67%), wall 105.5s→77.7s; Codex GPT-5.6-Sol: 61,952→47,669 (−23%), $0.1377→$0.1151 (−16%), wall 25.3s→62.4s (Sol slower with JCR in 19/20); One Sol outlier 372.6s / 193 Jev calls; n=1 per cell; Not Harbor task-execution; Claude/Codex harnesses; compare mode; 50 scenarios bundled; 11 groups, 960 nodes, 11,360 items; 16 routing rounds per step; NiazMorshed2007/jcr ≠ skill-broker ≠ skillranker ≠ jev-sift ≠ jev-lens ≠ jevusher ≠ jev_select_capability; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34; notes.md §116

User-provided 0922 (`notes.md` §117 / items 330–336 / batch #100). SemIf was formerly OpenJev; MLX backend; 5.21× systems≠semantic; Softmax over options ≠ calibrated Noul; live REST 2282★. Do not reopen #23–#36/#38; do not push onto open #39/#40.
User-provided 0922 uniqueness lock: SemIf was formerly OpenJev; independent; not affiliated with Jev or TypeSafe; homepage openjev.com; default master; MIT; HEAD ca3ba65f1429; Tolerate float roundoff in MLX evidence verification; pushed 2026-09-19; live REST 2282★ / 140 forks; size 9177; README SHA 74ab7f7f; LICENSE SHA ca562883; interface pattern reproduction with open models; does not reproduce Jev undisclosed model/training; Direct option logits; 0 output tokens; shared-state parallel; MLX backend for Apple Silicon (`--backend mlx`); Qwen3.5-4B 3090 direct 1.023s vs AR JSON 5.332s (**5.21×**); argmax agree 18/21; systems comparison ≠ semantic equivalence; Parallel suffixes 20.03 dec/s on 777 decisions; Browser ladder Qwen3.5-4B authored BA 0.813, pert 0.766, TypeSafe subset agreement 0.845 vs Published Jev 0.883 (102 across 20 cases); Softmax over options ≠ calibrated Noul; typed output does not guarantee semantic correctness; wire/agreement ≠ replica of TypeSafe; SemIf ≠ kw2828/OpenJev playground ≠ zhihz/openjev ≠ apiplant/semif-rs port ≠ dddanielliu/semif-serve; rename is densify not a second census; JevBench 74.6 is §78 not this ladder; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#38; do not push onto open #39/#40; notes.md §117
User-provided 0940 uniqueness lock: Turn decision-shaped LLM prompts into proposed Jev primitives; This is a conversion assistant, not an automatic guarantee of equivalent behavior; The compiler uses deterministic heuristics, not an LLM or evaluation model; It understands a deliberately small set of common prompt patterns; Generated instructions and criteria must be reviewed before production use; Score ranges such as 0 to 1 are translated into ordered Jev criteria; Prompts requiring open-ended prose are not a fit; suitability strong/partial/not_a_fit; compatibility full/partial/none; Writing new text stays with an LLM; Review the generated Score rubric; Jev scores ordered criteria, not an arbitrary 0-to-1 range; Everything runs locally in the browser; There is no framework, database, account, API, or server-side prompt processing; The key is read from the process environment and is never stored or printed; connect-src 'none'; alexwestco/llm-to-jev ≠ altryne/jevify ≠ ryana/jevify ≠ fidecastro/jevify ≠ Mintzs/jevify ≠ gulagala001/jevify ≠ uspraveen/Jevify; HEAD 234058ab372d; README SHA 43cd94fb; LICENSE SHA 5f334006; compiler SHA fdf235d0; 2★; MIT; JavaScript; size 29; Pages https://alexwestco.github.io/llm-to-jev/; invented_signal false; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35; notes.md §118
Hourly 0947 uniqueness lock: Fast and cheap agent evals. jev as judge.; 18,041 skills from the 200 most-starred repos; Not a security scanner; 最简 Jev 调用演示器; confidence 不是正确率; q93304989-bit/jev-lab ≠ tanayvasishtha/jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab ≠ yibie/laya-jev-lab; 75% cheaper and 18% faster withdrawn; jev @0.15 100% recall 87% savings; 33Audits/jev-auto ≠ gargpratyush/jev-router; no Typesafe key, no PI_API_BASE, zero deps; tool-emitted Score/Noul ≠ calibrated Noul; semantic_compatibility: false; candidate_mass; Qwen3.5-2B ≠ Archer; Jev evaluates decisions; it cannot run a coding-agent session; Status: no model yet; S1LV3RJ1NX/openjev ≠ TheoLeeCJ/openjev; 28 accepted decisions; 3 targets; score 800; health 100; arcade game not a flight trainer; A successful live TypeSafe call has not been verified for v0.1.0; abhibansal60/tidy ≠ MANISH007700/tidy; No model, Jev included, predicted which channels its owner keeps; seed 1 selected on a held-out 400-item validation split; Brier 0.342 → 0.378; more accurate and more overconfident; Qwen3.5-4B ≠ Archer; static quants of kushalpatil/jevify-gemma4-26b-a4b; The labels were corrected, and one earlier result was retracted; zero of 23,869 eligible rows; Do not compare cost without checking task success; Exit 1 is not a proof; kisshan13/typesafe-ai-go ≠ Nibir1/typesafe-go ≠ official; 38 tests that cannot fail in a 356-model warehouse; if a parser can answer it, Jev is never asked; 359 of them; Games & Simulation 82; Education & Learning 1; Ratings are heuristics; syedabbasshaheer-art/jev-atlas ≠ ZeroX-01/jev-atlas ≠ Zaious/jev-capability-atlas ≠ gorock007/jev-atlas; anandi1989/awesome-jev-usecases ≠ whyashthakker/awesome-jev-use-cases ≠ walidboulanouar/awesome-jev-use-cases ≠ vamsikrishna2421/jev-usecases; Every headline result above is self-reported; Archer Hume 84.6% MMLU-Pro is a third-party probe not landed Archer; catalog ≠ endorsement; judge ≠ actuator; softmax over A–H ≠ Noul; SemIf 2270★; jevlike 1054★; TypeLLM/TypeLLM 16★; AnotiaWang 98★; yibie/awesome-jev 538★; Laya likes 889; tracker likes 68 lastModified UNCHANGED; Blackwood likes 2 gated manual; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#35/#36/#37/#38/#40; do not push onto open #39; notes.md §119


**Hourly 1049 HIGH (`notes.md` §120).** ggmlc GGUF is not llama.cpp. serving substrate ≠ calibrated replica. Qwen3.5-9B ≠ Archer. planner writes JEV selects. pick_by_id vs pick_second. soft scores ≠ hard gates. catalog ≠ endorsement. Do not reopen or amend PR #23–#42. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
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
**Hourly 1643 HIGH (`notes.md` §127).** openjev release 0.3.0 densify. re-pin vLLM PR #57250 restructured head. restructured vLLM head ≠ logit-equiv. MODEL_VERSION stays openjev-0.1. dual serving is not generate. Hosted Codiv ≠ TypeSafe. typed judgments not opinions. Thresholds are policy not model. Jev never generates prose JSX or code. game success ≠ calibrated Noul. catalog ≠ endorsement. SHA move is not a replica. Do not reopen or amend PR #23–#49. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1643 uniqueness lock: razorback16/openjev densify HEAD febf02e88989 README SHA 242a737dba01; release 0.3.0; re-pin vLLM PR #57250 restructured head; VLLM_COMMIT baa8338; pyproject and __init__ agree 0.3.0; MODEL_VERSION stays openjev-0.1; uv.lock hygiene; dual serving is not generate; Hosted Codiv ≠ TypeSafe; restructured vLLM head ≠ logit-equiv; wire-compat ≠ logit-equiv; SHA move is not a replica; Error contract is not a Noul; frostney/clean-code-review 7★ typed judgments not opinions; documentation is read not judged; Luna writes from Jev findings; morcoan/JMP Joint Model Participation; Models participate. Real tools execute.; Jev routes actions generators supply arguments; not a swarm; zkjoie/jevbus Thresholds are policy not model; Drop < Review < Deliver; FanOut or Exclusive; Kelbie/hunch ≠ carldaws/hunch ≠ tpellet/hunch ≠ huncho; Agent Skills semantic review; SupratikB23/JevCanvas Jev never generates prose JSX or code; Diffusion never decides structure; json-render is the only renderer; skcache/jevtrafficsim Fixed Adaptive Jev; game success ≠ calibrated Noul; Shalimov04/open-jev ≠ razorback16/openjev ≠ TheoLeeCJ/openjev ≠ Zefan-Cai/Open-Jev; MstyAI/laya-onnx empty repo ≠ tozp/laya-onnx ≠ Mattepiu/laya-onnx ≠ gqgs/laya-onnx; SherifAshraf2003/jev-use ≠ shitianfang/jev-use; aniruddh-krovvidi/switchboard ≠ cannacre8ive/switchboard-ai; Visorian/TidyUp ≠ abhibansal60/tidy; isiomaC/jevkit ≠ WaynezProg/jev-kit; lee-lou2/jev-tree ≠ reachjalil/jev-tree; Royhu1/jev-poker-trainer empty repo; JoacoMarc/jev-harness-router ≠ jackbarunz/jev-tool-router; rh-guard owns primary gates; hf:Praveenrajus/jev-bench HTTP 200 was 401; hf:ZefanCai/Open-Jev densify dataset; LoRA ≠ RLCD replica; hf:emretheus/jev-rag-benchmark ≠ erendikmenn/jev-rag-benchmark; hf:ctaxnagomi/DGUI_HYPERMEM-JEV densify sha ab3d3529; hf:hugging-apps/open-jev-deberta-v3-large-demo encoder class member not Jev replica; serving substrate ≠ calibrated replica; catalog ≠ endorsement; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49; notes.md §127

**Hourly 1746 HIGH (`notes.md` §128).** TypeLLM truncated thinking densify. 0.8B thinking On 0/18 *theirs*. forced closure 20/20 type-valid *theirs*. Constrained AR ≠ calibrated Noul. Kev-0.8B completes family. 4B new-source 0.794/0.832 *theirs*. 9B new-source 0.812/0.837 *theirs*. transfer-v9 5%/9%/26% *theirs*. Facts go to code. Judgments go to Jev. Only facts can block. Jev never blocks. five-lines threshold 0.80 still soft. 155/155 argmax *theirs*. Qwen3.5 ≠ Archer. catalog ≠ endorsement. SHA move is not a replica. Do not reopen or amend PR #23–#50. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1746 uniqueness lock: TypeLLM/TypeLLM densify HEAD 702e6a287f3c README SHA 08180db0450b; truncated thinking then constrained decode; typellm_runtime.py typellm_sglang.py; evals/qwen35_small; 0.8B thinking On 0/18 *theirs*; forced closure 20/20 type-valid *theirs*; Constrained AR ≠ calibrated Noul; type safety does not guarantee factual accuracy; Qwen/Qwen3.8-27B ≠ Archer; jaredpalmer/kev densify live HEAD 8465c4c4c294 watch 38087aa0301d README SHA 19664b9ae546; Kev-0.8B completes family; Kev-0.8B 4B 9B Qwen3.5; 4B new-source 0.794/0.832 *theirs*; 9B new-source 0.812/0.837 *theirs*; transfer-v9 Kev-9B 5% Jev 9% Kev-8B 26% *theirs*; SemIf Kev-9B 0.917 Jev 0.965 *theirs*; scienthoon 0.952/0.911 vs 0.897/0.914 *theirs*; transformers >= 5.17; Qwen3.5 ≠ Archer; wire-compat ≠ logit-equiv; SHA move is not a replica; notque/vexjoy-agent 421★ /d routes /do fallback; tamaratran/jev-pruner densify HEAD 47d017c34eab; qkal/Canny Facts go to code. Judgments go to Jev. Only facts can block.; Jev never blocks; jqueryscript/awesome-jev 231 entries catalog ≠ endorsement; jqueryscript/awesome-jev ≠ MrJev/awesome-jev ≠ yibie/awesome-jev; jamescazzetta/five-lines threshold 0.80 still soft; eugeniughelbur/jev-engineering 371ms $0.0000189 300-call *theirs*; tpellet/jevify ≠ altryne/jevify; seb4ez/jevguard-mcp ≠ seb4ez/jevguard; resumocast/jev-mcp ≠ jkudish/jev-mcp; dtduc-git/jev-table first sighting; Adrian-Ernesto/jevsort ≠ zzzzzec/jevsort; MidasMulli/kev-ane 155/155 argmax *theirs*; MidasMulli/kev-ane ≠ jaredpalmer/kev; serving substrate ≠ calibrated replica; empty repo skip-thin; loktar00/llm-lan-party empty repo; rh-guard owns primary gates; catalog ≠ endorsement; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50; notes.md §128
**Hourly 1843 HIGH (`notes.md` §129).** kev own-data JSONL densify. --init_from warm-start LoRA/head PR #9. from-scratch ≠ warm-start. JSONL labels ≠ Harbor. 4B new-source 0.794/0.832 *theirs*. 9B new-source 0.812/0.837 *theirs*. 0.33 vs 0.84 vs 0.83/0.88 *theirs*. reconstruction ≠ replica. assay-001 split verdict. catalog ≠ endorsement. SHA move is not a replica. Do not reopen or amend PR #23–#51. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1843 uniqueness lock: jaredpalmer/kev densify HEAD bd058057ad0a README SHA 84b872488915; Fine-tuning on your own data; --data JSONL; --init_from warm-start LoRA/head PR #9; Kev-0.8B 4B 9B Qwen3.5 family; 4B new-source 0.794/0.832 *theirs*; 9B new-source 0.812/0.837 *theirs*; 0.33 vs 0.84 vs 0.83/0.88 *theirs*; from-scratch ≠ warm-start; JSONL labels ≠ Harbor; Kev-0.5B card Qwen3.5 family pointer; No Jev outputs were used for training; option order can change an answer; 8.2% ≥0.9 on wrong *theirs*; Kev-9B 7.5% ≥0.9 on wrong *theirs*; dabit3/jev-experiments densify 340★; simota/tenbin densify neighbor skill; Promethe-us/awesome-jev ≠ MrJev/awesome-jev ≠ yibie/awesome-jev; kyegomez/open-jev reconstruction ≠ replica; unofficial research implementation with random weights; kyegomez/open-jev ≠ razorback16/openjev ≠ TheoLeeCJ/openjev ≠ Zefan-Cai/Open-Jev ≠ Shalimov04/open-jev; jourdanlabs/assay-001 split verdict; CLINC150 ECE 0.0204 *theirs*; Banking77 ECE 0.0936 *theirs*; 8,576 responses zero type errors *theirs*; brnyxx/jev-ra 3-5x / ~300 ms *theirs*; 8.50× Wikipedia *theirs*; ThePFMind/jev-mcp ≠ jkudish/jev-mcp ≠ burnigtm/jev-mcp; namenu/pi-jev-effort ≠ TheoOliveira/pi-jev; samatv256/mini-Jev ≠ r-ms/mini-jev; comoc/jev-minesweeper ≠ EnesYilmazcode/JevMinesweeper; game success ≠ calibrated Noul; Nutlope/jev-fraud Kimi K3; jeffloo886/jev-notion; hf:akhilaaa3/openjev-v1-allmix-r512-merged ≠ hf:akhilaaa3/openjev-r512-handoff-demo; serving substrate ≠ calibrated replica; catalog ≠ endorsement; SHA move is not a replica; wire-compat ≠ logit-equiv; Qwen3.5 ≠ Archer; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51; notes.md §129

**User-provided 1936 HIGH (`notes.md` §130).** sgoedecke/system-one first-sighting. SystemOne.from_pretrained. TypeSafe-compatible ≠ TypeSafe replica. mithalouni/system-one-open first-sighting. 76.7% vs Jev 86.9% *theirs*. replica ≠ TypeSafe. kotoba-lang/typed-decisions first-sighting. DeBERTa-v3-large 0.855 / 42 ms *theirs*. kotoba-lang/typed-decisions ≠ convaiinnovations/laya-typed-decisions. aisearchio 15-link census catalog ≠ endorsement. soft scores ≠ hard gates. SHA move is not a replica. Do not reopen or amend PR #23–#52. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
User-provided 1936 uniqueness lock: sgoedecke/system-one 20★ HEAD ebde2a2db706 README SHA d331b567e2c3; SystemOne.from_pretrained; Batched single-token choice inference; TypeSafe-compatible; cache_prefix=True; LICENSE absent; sgoedecke/system-one ≠ mithalouni/system-one-open ≠ KathanModh259/system-one ≠ babybear-labs/system-one; TypeSafe-compatible ≠ TypeSafe replica; mithalouni/system-one-open 18★ MIT HEAD 77f1f7cccf8a README SHA 535f33028a68 LICENSE SHA 2f6f2cf1064e; Gemma 4 E2B / Gemma 3 270M Modal; 76.7% vs Jev 86.9% strict common subset *theirs*; 97 ms H100 *theirs*; 74.8% held-out *theirs*; replica ≠ TypeSafe; HF upload pending; kotoba-lang/typed-decisions 1★ Apache-2.0 HEAD 10d7834d3b99 README SHA 4d6bbf4c4e44 LICENSE SHA 513bb5e3cb4c; ModernBERT / DeBERTa / LLaDA-MoE; DeBERTa-v3-large 0.855 / 42 ms *theirs*; ModernBERT-base 0.717 / 68 ms *theirs*; LLaDA-MoE 0.835 / 676 ms *theirs*; kotoba-lang/typed-decisions ≠ convaiinnovations/laya-typed-decisions; encoder class member not Jev replica; aisearchio 15-link census catalog ≠ endorsement; 12 already carded 3 gaps this fold; soft scores ≠ hard gates; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52; notes.md §130

**Open-Jev densify (`notes.md` §125).** DENSIFY the original 1441 card, not a sibling first sighting. HEAD 4933ee84951f README SHA ce1a587219e4. LoRA + scalar head + calibration temperature. not merged base models. customer-service P50 85.03 vs Jev 295.26 *theirs*. 1024/32 slower 1015.90 vs 301.37 *theirs*. systems latency ≠ semantic equivalence. Open-Jev TREC pending. hard acc ≠ calibrated Noul. type-valid ≠ exact. LoRA ≠ RLCD replica. Qwen/Qwen3.8-27B ≠ Archer. SHA move is not a replica. Do not reopen or amend PR #23–#52. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
User-provided Open-Jev densify uniqueness lock: Zefan-Cai/Open-Jev densify HEAD 4933ee84951f README SHA ce1a587219e4; pushed 2026-09-21T01:34Z; Astra TREC commit 1dd56990be7e pushed 2026-09-21T01:17Z; live 3★ (was 0★; star-noise is not the fold); LoRA adapters plus trained scalar decision head and calibration temperature; not merged base models; dataset ZefanCai/Open-Jev rev c67699e13d0a; Open-Jev-2B rev 0c7aa498b162; Open-Jev-9B rev 47e966881e48; 27B still in progress; Independent of TypeSafe; no RLCD/parity claims; LoRA ≠ RLCD replica; customer-service P50 local HTTP 85.03 ms vs Jev HTTPS 295.26 ms *theirs*; 1024 tokens/32 candidates Open-Jev slower 1015.90 vs 301.37 *theirs*; prefix caching experimental/off by default; CUDA prefix caching exceeded tolerance on 9/11 workloads; systems latency ≠ semantic equivalence; GPT Luna P50 918.13 ms Astra 1938.39 ms *theirs*; TREC-DL Jev/Luna/Astra completed; Open-Jev TREC pending; 80,816 training rows; 2B 94.71% / OOD 86.02%; 9B 97.54% / 91.97% *theirs* not Harbor; hard acc ≠ calibrated Noul; type-valid ≠ exact; Qwen/Qwen3.8-27B ≠ Archer; website https://zefan-cai.github.io/open-jev/; launch X thread https://x.com/Zefan_Cai/status/2101782158658695388 https://x.com/Zefan_Cai/status/2101786019607740436 https://x.com/Zefan_Cai/status/2101789698947793231; densify §125 not a sibling first sighting; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52; notes.md §125
**Hourly 1946 HIGH (`notes.md` §131).** X-sentiment does not execute trades. heyjunpenn/awesome-jev 485 catalog ≠ endorsement. jev-arena 62.69% vs 67.26% *theirs* not gold. 203.2s $0.84 vs 823.5s $1.50 *theirs*. one seed-0 trial *theirs*. Jev $0.018825 vs Astra $5.93 *theirs*. 10.59× *theirs*. 6 class flips. agreement ≠ accuracy. probabilities uncalibrated. Qwen3.8 ≠ Archer. Spanish −6.4 pp XNLI *theirs*. ECE 0.057→0.101 *theirs*. 72.2% vs 63.4% p_max≥0.9 coverage *theirs*. llm-to-jev description rewrite Convert LLM prompts to Jev prompts. SHA unchanged 234058ab372d. 3★. heuristic conversion ≠ calibrated Noul. skip Zefan-Cai/Open-Jev densify open #53. skip #54 three. catalog ≠ endorsement. *theirs* not Harbor. SHA move is not a replica. Do not reopen or amend PR #23–#52. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1946 uniqueness lock: brainstormity/Jev-X-Sentiment-Analysis 136★ HEAD 5c932f941a92 README SHA bf4134b44cda; platform does not execute trades; heyjunpenn/awesome-jev 485 catalog ≠ endorsement; heyjunpenn/awesome-jev ≠ yibie/awesome-jev ≠ MrJev/awesome-jev ≠ Promethe-us/awesome-jev ≠ ckaraca/awesome-jev ≠ yzfly/awesome-jev-zh ≠ shirenchuang/awsomejev ≠ andyrewlee/awesome-system-one; NanmiCoder/jev-arena 10k comments 62.69% vs 67.26% *theirs* not gold; 203.2s $0.84 vs 823.5s $1.50 *theirs*; AI-reviewed labels ≠ gold; openroboto-ai/jev-robot-control one seed-0 trial *theirs*; Jev $0.018825 vs Astra $5.93 *theirs*; one-trial robot ≠ Harbor; endman100/research-Qwen3.8-JevLike 10.59× *theirs*; 6 class flips; agreement ≠ accuracy; probabilities uncalibrated; Qwen3.8 ≠ Archer; 10.59× systems ≠ ECE; marcosmartinez/jev-acento Spanish −6.4 pp XNLI *theirs*; ECE 0.057→0.101 *theirs*; 72.2% vs 63.4% p_max≥0.9 coverage *theirs*; alexwestco/llm-to-jev description rewrite Convert LLM prompts to Jev prompts; SHA unchanged 234058ab372d; 3★; heuristic conversion ≠ calibrated Noul; desc rewrite ≠ SHA/behavior change; skip Zefan-Cai/Open-Jev densify open #53; skip sgoedecke/system-one mithalouni/system-one-open kotoba-lang/typed-decisions open #54; ikermoel/open-alternative-jev already §49; nrdz-labs/fast-jev-opencode already §62; mallahyari/system-one-benchmark already §61; does not execute; catalog ≠ endorsement; *theirs* not Harbor; SHA move is not a replica; local_only ≠ Jev; rule-table ≠ model; replica ≠ TypeSafe; arunav25/jev-mcp ≠ jkudish/jev-mcp ≠ ThePFMind/jev-mcp ≠ burnigtm/jev-mcp; luckberonne/mini-jev ≠ r-ms/mini-jev ≠ samatv256/mini-Jev; Kwwwww74/OpenJev ≠ razorback16/openjev ≠ kyegomez/open-jev ≠ Zefan-Cai/Open-Jev; peach-zhang/typesafe-go ≠ kisshan13/typesafe-ai-go ≠ Nibir1/typesafe-go; laidick/system-one-benchmark ≠ mallahyari/system-one-benchmark; sahasrarjn/system-one ≠ sgoedecke/system-one; aboisvert/jevvy ≠ PanAchy/jevvy; andrest04/jev-lab ≠ javsanesq/jevlab; twilwa/pi-typesafe ≠ TheoOliveira/pi-jev; RuipuCui/jev-harness ≠ ismaelsoilet/jev-harness ≠ AntonioCoppe/jev-harness; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52; notes.md §131
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

**Hourly 1019 GEPA / catalog / routing (`notes.md` §145).** schema-valid is not the same as correct. API confidence is not P(correct). GEPA revises Choice instructions/criteria with weights fixed. review-queue policy is not F1. Soft is not gate. Not an 18th scoring-table species. routing ≠ permission. catalog ≠ endorsement.

**Hourly 1019 HIGH (`notes.md` §145).** praneeth16 GEPA ADE Corpus V2. schema-valid is not the same as correct. API confidence is not P(correct). GEPA revises Choice instructions/criteria with weights fixed. jev-1.13.0 weights fixed. Brier 0.1357→0.0747 *theirs*. F1 69.1%→79.7% *theirs*. FN 4→6. review-queue policy is not F1. Soft is not gate. Not an 18th scoring-table species. Every claim is labeled and sourced. catalog ≠ endorsement. 发送永远手动. About 180 ms. routing ≠ permission. $0.00241 *theirs*. Not a screenshot agent. game success ≠ calibrated Noul. pi-follow-through threshold 0.8 still soft. wire-compat ≠ logit-equiv. densify §144 not a sibling first sighting. pi-jev-context densify §134 not a sibling first sighting. *theirs* not Harbor. SHA move is not a replica. Do not reopen or amend PR #23–#69. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1019 uniqueness lock: praneeth16/adapting-jev-with-gepa ADE Corpus V2 GEPA; schema-valid is not the same as correct; API confidence is not P(correct); GEPA revises Choice instructions/criteria with weights fixed; jev-1.13.0 weights fixed; Brier 0.1357→0.0747 *theirs*; F1 69.1%→79.7% *theirs*; FN 4→6; review-queue policy is not F1; Soft is not gate; Not an 18th scoring-table species; aliaihub/awesome-jev-usecases 15★ NOASSERTION HEAD 6cbde6bd3569 README SHA 7ea135c6345d; Every claim is labeled and sourced; catalog ≠ endorsement; aliaihub/awesome-jev-usecases ≠ anandi1989/awesome-jev-usecases ≠ whyashthakker/awesome-jev-use-cases; rezoch340/jev-chat-JARVIS-windows 6★ MIT Py HEAD 26b686301437 README SHA 0714736b68c3; 发送永远手动; rezoch340/jev-chat-JARVIS-windows ≠ Finderchangchang/jev-chat-JARVIS; iamvatsalpatel/tiershift 3★ MIT TS HEAD 16a0826b9f62 README SHA 46fcb1cb191b; About 180 ms; routing ≠ permission; Bring-AI/jev-rl 2★ MIT Py HEAD 36f89cec85a2 README SHA 6283da6011b7; $0.00241 *theirs*; daniel4x/JevEmon 2★ GPL-3.0 HEAD 572454c69bf7 README SHA 8fc00d12848d; Not a screenshot agent; game success ≠ calibrated Noul; spoonnotfound/soupbase 2★ MIT TS HEAD 3e874e83e710 README SHA 3106bc96d6ab; Nabsku/pi-follow-through 1★ MIT TS HEAD c62ef28ff4ac README SHA 64000451b79e; pi-follow-through threshold 0.8 still soft; dashbi1/jev-sim 1★ MIT Py HEAD 753c7397d73c README SHA 05fd960799d2; wire-compat ≠ logit-equiv; jev-jarvis/jev-jarvis densify 8★ MIT Py HEAD a94e3b967ef5 README SHA e441335b1df0 was be68dd7993f0 / efe7e47a6fe8; densify §144 not a sibling first sighting; Nyarlathoteppppp/pi-jev-context densify 5★ MIT TS HEAD 96371e2bf144 README SHA d4276222a436 was f0128a86478f; pi-jev-context densify §134 not a sibling first sighting; Nyarlathoteppppp/pi-jev-context ≠ kevinpita/pi-jev-context; fly88oj/jebii 0★ MIT JS HEAD 5cbe527ed791 README SHA b4a76b8aba9d; generallymatthew/factlabel 0★ Apache-2.0 Py HEAD b3d3bceee044 README SHA b1cda6c4646e; aakgna/jevcal ≠ abhixhek/jevcal; 007M7/jev-chat ≠ w3cj/jev-chat ≠ Manta-Boardgame/jev-chat; fstandhartinger/jev-router ≠ gargpratyush/jev-router; prakash7474/Jev_guard ≠ leepokai/jev-guard; rdutra/laya-mcp ≠ PerryLink/laya-mcp ≠ wsargent/laya-mcp; Kourin1996/jev-playground ≠ wustep/jev-playground; ai-ecoverse/cua-s1.js Cua-S1 ≠ TypeSafe; skip-thin Unnati-23/jev-typesafe-guide antoniofaical/digital-twin-classifier-jev leonezhu/agent-kits empty README; skip-thin wjw66/deepseek-harness-jev-pre-compaction ziwon/jev-actor empty SHA HTTP 409; hf:chanoian/openjev-mlx-demo HTTP 401 *theirs*; hf:clduab11/jev-calibration-statistics HTTP 401 *theirs*; hf:yasserrmd/laya-lab HTTP 401 *theirs*; catalog ≠ endorsement; game success ≠ calibrated Noul; does not execute; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62/#63/#64/#65/#66/#67/#68/#69; notes.md §145

**Hourly 1110 HIGH (`notes.md` §146).** hf:thaitea/laya-vision SmolVLM typed vision decisions. same-species serving not an 18th scoring row. A-OKVQA 63.1% ECE 0.266 to 0.094 *theirs*. act head untrained do not gate on it. codearia-sieve page to typed fields. 11 of 11 *theirs* not Harbor. gemma-jev JSON chat ≠ calibrated Noul. local-decision-model independent from the public post. musubi-jev README is a kev tree copy. copied kev numbers are not a musubi bench. vllm2jev wire-compat ≠ logit-equiv. pg-laya serving substrate ≠ calibrated replica. jev-rerank ranking ≠ calibration. typesafe-mcp decision is code. act_above 0.8 still soft. densify §142 not a sibling first sighting. densify §145 not a sibling first sighting. densify §143 not a sibling first sighting. densify §139 not a sibling first sighting. catalog ≠ endorsement. *theirs* not Harbor. SHA move is not a replica. Do not reopen or amend PR #23-#70. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1110 uniqueness lock: hf:thaitea/laya-vision 13 likes sha a2653db2831b cc-by-nc-sa-4.0; SmolVLM-256M vision typed choice/score/noul; same-species serving not an 18th scoring row; independent not affiliated; A-OKVQA 63.1% ECE 0.266 to 0.094 *theirs*; ScienceQA 89.0% ECE 0.080 to 0.034 *theirs*; VQAv2 noul 73.2% ECE 0.085 to 0.042 *theirs*; All n=8235 75.9% ECE 0.035 *theirs* not Harbor; VQAv2 re-split not comparable to published VQAv2; about 71 ms *theirs*; option order varies 1.2 points *theirs*; act head untrained do not gate on it; not a drop-in replacement for Laya text checkpoint; usage loads thaitea/laya-vision-smolvlm-256m already §87; hf:thaitea/laya-vision ≠ thaitea/laya-vision-smolvlm-256m card id; AntonG87/codearia-sieve 1★ MIT TS HEAD 64ecd4151726 README SHA b03a3d29ab22; page to typed fields; 6 of 6 *theirs*; 11 of 11 *theirs* not Harbor; robots-disallowed did not fetch; no model required for the parse; 7Zenox/gemma-jev 0★ NOASSERTION Py HEAD 2eed119e03ff README SHA c3b58d6a15a9; generation-free letter slots; 144 authored decisions *theirs*; Gemma 3 270M 0.293 below chance 0.333 *theirs*; Gemma 4 E2B-it JSON chat 0.807 *theirs*; Qwen3.5-4B JSON chat 0.813 *theirs*; JSON chat ≠ calibrated Noul; softmax over letter slots ≠ calibrated Noul; bf16 vs fp32 argmax-agreement check not run; Gemma ≠ Archer; Qwen3.5 ≠ Archer; Pdbz199/local-decision-model 0★ MIT Py HEAD ddceb5829849 README SHA 80659ec966f5; independent project built only from the public post; one pass no generation; schema-valid is not the same as correct; musubi-labs/musubi-jev 0★ Apache-2.0 HEAD e943f21e4057 README SHA 8ffd43564204; README is a kev tree copy; copied kev numbers are not a musubi bench; musubi-labs/musubi-jev ≠ jaredpalmer/kev; quaeast/vllm2jev 0★ NOASSERTION Py HEAD 8a51f94961ea README SHA be92356f1176; does not reproduce Jev calibration; wire-compat ≠ logit-equiv; IAmJSD/pg-laya 0★ Apache-2.0 Rust HEAD 1bc66a4d6a7f README SHA 03476be41744; SQL choice score noul; serving substrate ≠ calibrated replica; IAmJSD/pg-laya ≠ realZachi/pg-jev ≠ giuliosmall/pg_typesafe; gbesse/jev-rerank-server 0★ MIT JS HEAD b28cef5e34a6 README SHA 91167c66c29c; SciFact n=25 nDCG@10 0.616377 to 0.718260 *theirs*; Recall@10 0.84 unchanged *theirs*; ranking ≠ calibration; MarkChu-git/typesafe-mcp 0★ MIT HEAD a064b14207c0 README SHA ae27210cc5af; decision act/review/abstain is code; act_above 0.8 still soft; MarkChu-git/typesafe-mcp ≠ itsmostafa/typesafe-mcp ≠ cyrusasco/typesafe-mcp ≠ Renwang-Huang/typesafe-mcp; pythongiant/laya-drift densify 4★ TS HEAD d33db6736ed8 README SHA 7af1781c28c5 was 334953e5cb8f / 6662121ba0f3; monitor agent drift; densify §142 not a sibling first sighting; Adkid-Zephyr/chinese-workflow-decision-bench densify 1★ MIT Py HEAD b694dc6dbcba README SHA 9ef2b7d76a37 was 6d0a7c2af303 / 4ed71a36cd51; 64/64 and 63/64 *theirs* not Harbor; synthetic not a group-chat dump; densify §145 not a sibling first sighting; turenlabs/jast densify 1★ MIT Rust HEAD c6588285208f README SHA d9214ca31f92 unchanged; star 0 to 1 is star-noise; densify §145 not a sibling first sighting; JabbaKadabra/SystemOneDotNet densify MIT C# HEAD 5120ffb84cc5 README SHA 0809f98d4c93 was 5bff3394281c / 76a9188c180a; unofficial .NET client; wire-compat ≠ logit-equiv; densify §143 not a sibling first sighting; arnavm-codes/JevFence densify HEAD 7e277474ff5e README SHA 2bbb684757de was 6fe62ca7b10c / 5441aaeaace0; soft scores ≠ hard gates; densify §145 not a sibling first sighting; cloudbtl/JevRAG 0★ Apache-2.0 Py HEAD 307ab19ee9cf README SHA 9b814bb6624b; first card revisit tag no prior notes card; cloudbtl/JevRAG ≠ emretheus/jev-rag-benchmark ≠ erendikmenn/jev-rag-benchmark; gbesse/decision-workbench densify MIT JS HEAD 877d1a9add5b README SHA 24cce8900d67 was 8889cf3750a3 / 14a3bf79da7a; human review separate from model output; demo scores are not accuracy measurements; densify §139 not a sibling first sighting; 0xagentlabs/jev-xiangqi ≠ Zafer-Liu/jev-xiangqi; RyanNg1403/jev-cli ≠ gnapse/jev-cli ≠ sunchojack/jev-cli; KennethAshley/awesome-jev ≠ heyjunpenn/awesome-jev ≠ yibie/awesome-jev; malevrigns/agent-jev ≠ hf:aimeigaoshou/agent-jev; 79.25% 1585/2000 ECE 0.1687 *theirs* not Harbor; kidzik/jiffy probabilities are uncalibrated; s3rli/jevips name collision not a decision model; skip-thin Alpha-Harper-Franklin/astra-jev jonas050210/Laya_Playground pietrushka/jev-youtube-filter empty SHA HTTP 409; skip-thin THANK-YOU-FOR-YOUR-ORDER-ASDF123/repo-laya4qxd Ylr9933/JevForAgent empty README; hf:marcmagn1/jev-alt-systemone-eval dataset sha 95f679e8455b README 404 models HTTP 401 *theirs*; catalog ≠ endorsement; game success ≠ calibrated Noul; does not execute; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62/#63/#64/#65/#66/#67/#68/#69/#70; notes.md §146

User-provided glance uniqueness lock: yoheinakajima/glance Apache-2.0 Py HEAD 8f36e063bffb README SHA b57280394bc1 LICENSE SHA d645695673349e; 3★; size 51490; pushed 2026-09-21T17:37:40Z; created 2026-09-21T06:51:38Z; PyPI glance-vlm 0.3.1; tag v0.3.1; site https://glance.yohei.me; topics calibration, image-classification, vision-language-model, vlm, zero-shot; Ask an open vision-language model typed questions about an image and get probabilities back, on your own machine; frozen open VLM default Qwen3-VL-4B Apache-2.0; answer-token logit readout in one forward pass; Glance is a calibration and measurement harness around that readout. It is not a model; trains no weights; images never leave the machine; local server binds 127.0.0.1; noul yes/no choice pick-one score ordered rating; POST /v1/decide; glance fit --unlabeled; yes/no 0.939 pick-one 0.933 rating exact 0.669 *theirs*; Gemini 3.1 Flash-Lite yes/no 0.961 pick-one 0.933 rating 0.763 *theirs*; unlabeled image-quality 0.67 to 0.76 exact *theirs*; about 32 labeled images 0.86 exact ECE about 0.03 *theirs*; non-image-quality rubrics 0.55 exact with 300 labels *theirs*; tilt 0.33 *theirs*; geometric probes diagonals 0.30 largest of four shapes 0.52 eight objects 0.56 *theirs*; stripe direction hidden-state linear probe 0.99 *theirs*; raw yes/no ECE 0.111 and 0.179 overconfident *theirs*; explicit other held-out breeds 7.7% *theirs*; claims ledger: faster or cheaper than Jev do not claim; shares inference object with featherless-ai/simple-jev hr98w/jev-visual zhengxuyu/litjev; request and response shapes follow TypeSafe Jev hosted text; yoheinakajima/glance ≠ TypeSafe Jev; POST /v1/decide ≠ TypeSafe /v1/systemone ≠ IamBusy/OpenJev /v1/decide; trains no weights unlike YOFO and unlike hf:thaitea/laya-vision §146 and unlike Zefan-Cai/Open-Jev; harness not weights; soft probs for threshold abstain rank; soft scores ≠ hard gates; logits are not calibrated probabilities of correctness; *theirs* not Harbor; catalog ≠ endorsement; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62/#63/#64/#65/#66/#67/#68/#69/#70/#71/#72; notes.md §147
