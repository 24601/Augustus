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
**Meaning-as-spec (Empirical as README resolver, 2026-09-18
~19:48):**
[jevcumber](https://github.com/RubyBrewsday/jevcumber) — Cucumber
`.feature` only; no step-definition glue. Jev picks among
**observed controls** and **literals already in the step**; never
writes code or invents values. Lockfile makes replay
deterministic (`--frozen` CI, no key). Refuse below 0.6. Same
pointer family as Stagehand pick-and-copy / jev-e2e. Do not copy
the tarball install (`notes.md` §59).
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
+ their LLM-as-judge test, 2026-09-18 ~21:39):**
[jev-semgrep](https://github.com/uehaj/jev-semgrep) — zero-dep
Node; one Noul per line × meaning; `-e`/`-a`/`-v` boolean
over those bits; 30 lines × 8 concurrent. Cross-lingual
JP↔EN, no translation step. Name collides with Semgrep
static analysis. Distinct from jevgrep (file/chunk packed
search). LICENSE MIT (GitHub NOASSERTION). Their judge test:
precision 0.94, recall 0.98. Do not copy npm / key how-to
(`notes.md` §61).
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


