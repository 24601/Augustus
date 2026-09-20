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
