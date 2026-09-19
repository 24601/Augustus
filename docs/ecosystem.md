# The judgment-model class, analyzed (Jev is exemplar)

Snapshot of **187 repositories** built on TypeSafe Jev (jev-1.13) during launch
week (Sep 15–18, 2026), all cloned and indexed with per-repo evidence, plus
class-level neighbors (open heads, GLiNER/GLiClass encoder family,
listwise rankers, vision scorers). Maintained by the Augustus skill; refreshed hourly on
weekdays. Jev is the densest public corpus, not the class monopoly.

- `archive/evidence.csv` — 169-row per-repo table: README size, languages, primitive usage (Noul/Choice/Score/API), tests, threshold histograms.
- `archive/findings.md` — deep-read distillation with status labels (Contract / Empirical / Hypothesis).
- `archive/repos.txt` — every clone.

## Categories

### Decision engines & search
- **paulobueno164/jev-mcts** — MCTS with typed fidelity (grounded depth 24, speculative capped at 2), "only probes concede," calibrated thresholds, seeded debias. 24/24 vs greedy 1/24.
- **lhemerly/mcts-agent** — batched Noul prune + Choice PUCT priors + Score/10 leaf value (no random rollouts).
- **carlaiau/jev-reranking** — independent TREC DL2019 benchmark: zero-shot Jev best MAP 0.4748, nDCG@10 0.683 vs monoBERT 0.718; $0.76 per 41k pairs.
- **superagents-lab/jev-search** — federated web search: Jev understands intent (query/sources/time-range), lanes fan out concurrently, Jev ranks results; merge by URL + engine agreement + rank.
- **kazuhideoki/jev-search** — recursive *file* search + fzf. Not the federated web product. `notes.md` §55.
- **kbhuw/jev-sift** — classify-first MCP: batch path/url/text → Jev before the main agent reads. Topology A, not a host adapter. `notes.md` §56.
- **Bentlybro/jevgrep** — meaning-search CLI+MCP without embeddings (`jgrep`). Packed parallel relevance; 79% top-5 vs BM25 40% / grep 20% on docstring-stripped repos. Keyword still wins exact strings. `notes.md` §58.
- **Max-sm-yc/Jev-RAG** — one-run RAG+Jev rerank vs Muse Spark rerank (≥70% cost / 72% latency); full-context Spark still faster. `notes.md` §58.

### Languages & runtimes
- **probably-lang (southpolesteve)** — a programming language whose **loop conditions are Jev feelings**: `while draft feels "like a LinkedIn influencer post" { … }`. Judgment-state recordings give deterministic replay.
- **carldaws/hunch** — Ruby library, not a new language: `almost_certain?` / `pick` / `rate` as chance/Choice/Score. English-as-config. Validations `rescue nil` fail-open at save. `notes.md` §55.
- **dannote/jev** — Elixir/OTP: Jev as a peer process; answers are messages; "clause order is the routing, thresholds are guards"; network-free tests.
- **jamesward/zio-typesafe-ai** — Effect-oriented (ZIO) client: Jev is the outer Choice; the handler runs the effect. Not Effect.ts and not the Jev HTTP contract. Hypothesis: `mappings.md` §19 (`notes.md` §28).

### Agent harnesses & self-supervision
- **Kevthetech143/super-jev** — domain-independent loop: observe → questions → decide → **permit (independent of confidence)** → execute (idempotency key) → verify → JSONL replay.
- **AntonioCoppe/jev-harness** — policy + confidence gate + shadow mode + offline eval CLI asserting on the **action**; 24-row filter 48.9s (Claude CLI) vs 1.3s Jev. Harbor/jevals-adjacent practice. `notes.md` §33, §44.
- **khordoo/jev-reflex-autonomy-lab** — S1 Jev reflex keeps control; optional S2 planner is one-use advice on low confidence. Experimental viz, not a flight controller. `notes.md` §46.
- **perixtar/jev-e2e** — NL cases; Jev selects observed controls; Playwright independently checks. PASS/FAIL/BLOCKED. Alpha. `notes.md` §46.
- **Wany-i/jev-decision-layer** — business decision tool; caller names the judgment; `gate` is part of the result. Unofficial. `notes.md` §46.
- **yalindogusahin/jevpandas** — pandas semantic index; noul/choice/score; LICENSE absent this pass. `notes.md` §46. Accessor sibling: **ktaletsk/jevframe** (PyPI; pandas and Polars `.jev`; full `p__`). `notes.md` §48.
- **Friedjof/jev-mobile** — durable Android worker + Mobile MCP; Jev sees prevalidated candidates only. `notes.md` §33.
- **jcpsimmons/jev-macos-loop** — Apple-silicon computer-use; local OmniParser/OCR/AX; text-only Jev. Finder demo independently verified.
- **rajdhakad9826/routeKit** — Jev estimates task requirements; policy engine selects the LLM. Jev does not pick the model.
- **jxu-dev-c/jev-adaptive-thinking** — session-sticky first-prompt Jev classification; fail-closed lock to `gpt-5.6-sol`. License null. `notes.md` §58.
- **Dicklesworthstone/skillranker** — hook ranks the skill catalog from live context with a calibration loop.
- **GodsBoy/jev-agent-skill-router** — 94.4% vs 70.8% lexical routing on 72 requests.
- **matthewdonsemail-lab/open-typesafe-camoufox** — browser agent at ~$0.0002/step: 11-way action Choice, free text only when needed.
- **gamesonrblx/Jevbridge** — ACP adapter putting Jev's typed decisions alongside Codex/Claude/Grok.

### Latency-first applications (dabit3/jev-experiments, 21 demos)
Per-keystroke launchers (104ms median, sequence-tagged staleness), firehose moderation at 300 msg/s with **judge-once/re-policy-in-code**, pre-execution guards (shell/commit/send), 32-agent swarm at 65 decisions/s ≈ $10/h, voice turn-taking, meeting minutes 150ms after each utterance, JUDGE/SCORE/CHOOSE spreadsheet formulas, accessibility-tree computer use, BM25→Jev re-rank (50%→100% top-1).

### Measurement & calibration
- **FirasSX914/calibre** — thresholds don't transfer across datasets: Banking77 routing win (80.2%@$0.103) became a 46%-more-cost tie on Web of Science.
- **arnabgho/rlcd-lite** — GRPO + Brier proper-scoring-rule reward → calibrated decisions; binary reward doesn't calibrate.
- **stephanj/parallelConstraintDecoding** — whole JSON schema of booleans/enums in two forward passes (prefill → parallel masked fields).
- **Foadsf/jev-for-engineers**, **AbdelStark/jev-benchmarks**, **BrendanH18/jev-lab** — measurement discipline and cost/latency visibility.
- **dayhaysoos/jevals** — local MIT workbench: labeled cases (Noul / Choice / Score), compare runs, WebMCP + agent skill. Empirical acceptance-test surface for Hypothesis mapping cards; complements `evaluate_decisions.py`. Not affiliated with TypeSafe. Pointer: `research/notes.md` §24. Hygiene and the Harbor substrate: `validation.md` Eval & hill-climb (`notes.md` §40). Shared bake-off exemplar: [`pngwn/open-jev-laya-bench`](https://huggingface.co/datasets/pngwn/open-jev-laya-bench) (ECE/NLL/Brier; LLM-as-judge is not the score; `notes.md` §46). Harbor-style frozen protocol vs constrained LLMs: [`nibzard/decision-model-benchmark`](https://github.com/nibzard/decision-model-benchmark) (DMB v2; jev banking 76.3% / spam 93.0% / 256+ cap; p50 264–276 ms; $0.07/1k; `notes.md` §49). Feedstock: [`Jevals/jevals-data`](https://github.com/Jevals/jevals-data) (CC-BY-4.0 boards + JSONL; recompute-from-logs; 2026-09-18 board). Boundary map (not a leaderboard): [`Zaious/jev-capability-atlas`](https://github.com/Zaious/jev-capability-atlas). Combinatorial negative: [`simonmesmith/jev-arc-agi-v1-experiment`](https://github.com/simonmesmith/jev-arc-agi-v1-experiment) (Direct Jev 4/400). Pre-registered independent eval (honest negative): [`ickma2311/jev-baselines-eval`](https://github.com/ickma2311/jev-baselines-eval) (both AMBIGUOUS; cascade sign-flip; `notes.md` §55). Healthcare Harbor-shaped: [`si618/explore-typesafe-ai`](https://github.com/si618/explore-typesafe-ai) (synthetic FHIR; not clinically validated).
- **jeiel85/jevscope** — local-first visual debugger + JSONL regression for Choice/Score/Noul; compare two definitions; policy buckets are JevScope-derived. Sits next to jevals. Pointer: `research/notes.md` §25.

### Local / open heads & GLi\* species
- **GLiNER / GLiNER2.5 / GLiClass** — species map: locate spans vs categorize the sequence vs local multi-head (fastino-ai GLiNER2.5 CPU-first). Peer of Jev, not a footnote. `references/judgment-class.md`. Author primary source: GLiNER2 "like jev" is schema-conditioned categorize (GLiGuard), not a Noul (`notes.md` §28). 36× Browser Use claim is a tweet (`notes.md` §25). Named jobs: [gliner25-compaction](https://github.com/m-newhauser/gliner25-compaction) — extractive retention Choice + char-offset copies; not a summarizer; not Jev (`notes.md` §50). [gliner2-ultrafast](https://github.com/sahibzada-allahyar/gliner2-ultrafast) — GLiNER2 `fastino/gliner2-multi-v1` scores observed a11y/DOM controls; not GLiNER2.5; not multimodal (`notes.md` §52).
- **GLiGuard** (fastino-ai) — 0.3B GLiNER2 encoder, checkpoint `fastino/gliguard-LLMGuardrails-300M`. One bidirectional pass over a safety schema. Same interface shape as batched questions; different objective. Not a Jev weight clone. `judgment-class.md`; `notes.md` §30.
- **DECRUX9812/openjev-lm** — Qwen2.5-0.5B+LoRA distilled from hosted Jev answers; 65/70 = 92.9% on 70 hand-labelled rows (one annotator, one domain, one seed) overnight on 6 vCPU, $0/call. Its 98.1% on fresh rows is teacher *agreement*, not gold. Receipts pattern: `notes.md` §25, §44.
- **convaiinnovations/laya** — open Choice/Score/Noul head, text-only, 512 tok. Companion packaging this hour: [`laya-typed-decisions`](https://huggingface.co/convaiinnovations/laya-typed-decisions) (421.3M, acc 0.766 / Brier 0.066 unverified). Shared bake-off: [`pngwn/open-jev-laya-bench`](https://huggingface.co/datasets/pngwn/open-jev-laya-bench) (26+9 tasks, 11959 items; ECE/NLL/Brier; not TypeSafe Jev vs Laya). ONNX replica: [`Mattepiu/laya-onnx`](https://huggingface.co/Mattepiu/laya-onnx) (~15 ms CPU; do not copy vs-Jev table). `notes.md` §18, §42, §46, §48.
- **jaredpalmer/kev** — Qwen2.5-0.5B LoRA + pointer readout; Apache-2.0; Hub [`jaredpalmer/kev-0.5b`](https://huggingface.co/jaredpalmer/kev-0.5b) plus GitHub release tarball. Runnable Archer reconstruction (`POST /v1/systemone`). Public gold, not a Jev teacher. Isolation exact; ID ECE 0.065 (0.031 after T); acc 0.799 / 1,350. NOTA training must confront `"other"` as a wrong alternative (`notes.md` §45 delta). **100★** this pass (light activity delta; `notes.md` §49). Not a knowledge/frontier substitute.
- **ikermoel/open-alternative-jev** — packed one-forward logprob System One on open LLMs (HF + vLLM). Apache-2.0. **Not a Jev reproduction.** RACE-H 92.9% @ 4.55 q/s on Qwen3.6-27B 8-bit; interference 6–9%. Space demo. `notes.md` §49.
- **wfzyx/von** — 14 MB Needle SAN; local `POST /v1/systemone`; sub-15 ms CPU claim / ~38 ms embed. authored144 needle 52.6% — **not a calibrated Jev replica**. Distinguish from jev-local stub and kev pointer. Do not copy vs-Jev table. `notes.md` §49.
- **Mintzs/jevify** — CUDA/PyTorch packed-logprob cousin on Qwen2.5-1.5B (`ora_decision_engine`). Uncalibrated likelihoods ≠ Noul. Independent of Distillation. No LICENSE this pass. `notes.md` §55.
- **BlackwoodAI/blackwood-rlcd** — open multimodal RLCD (image-text-to-text), Jev-compatible shim, CC BY-NC 4.0. Screenshot + marked candidates → Choice. Card: web acc 0.907 vs Jev 1.13 text-only 0.480; letter-shuffle 0.133 vs 0.587; ECE 0.037; ~200 ms H100. Jev still leads general text 0.850 vs 0.786. Not Archer Watch. `notes.md` §46.
- **Foodoo1/Qwen3-14B-RLCD-Decision-LoRA** — decision-token QLoRA on Qwen3-14B under parallel constrained decoding. Held-out 200-case / 4-field: fraud_risk 64→95%, overall 85.2→98.8% at ~234 ms. Synthetic; not a financial product. `notes.md` §46.
- **zmtomorrow/TypeAR** — constrained autoregressive decoding surface: typed fields on a pretrained open model, no retraining. Not a proper-scoring decision head. `research/notes.md` §32.
- **stephanj/pcdServer** — native Parallel Constrained Decoder (C++20, llama.cpp GGUF, Apple+Linux). TypeAR-class serving: 2–256 enums, 1–63 parallel fields; softmax over allowed values is not a Noul. `notes.md` §42.
- **com-kotobalabs/open-jev-deberta-v3-large** — encoder open-jev, DeBERTa-v3-large 434M, apache-2.0, public gold (not a Jev teacher). In-domain ECE 0.022; OOD acc 0.854→0.690. `notes.md` §33.
- **Mikhail/mini-jev-runs** — 27.9k schema-driven decisions; one forward pass; answer from next-token logits; no token generated. Calibration / constrained-decoding gold. `notes.md` §33.
- **kokuren/jp-sns-jev7-estimator** — JP SNS seven-axis ONNX distill; teacher scores, not calibrated probabilities; `threat` F1@0.5 = 0. Domain-local categorize.
- **Archer Hume open decision-model** — **Watch.** Qwen3.8 27B dense, 265k, multimodal no audio; one forward pass locally once AR is removed. Driver: AU healthcare data-residency. No Hub weights this pass. `notes.md` §31–§33. Runnable *architecture* productization (0.5B, not that drop): **jaredpalmer/kev**. `notes.md` §45.
- **bespokelabsai/nimble** — open recipe: contrastive hard labels, not a Jev distill. Model card Apache-2.0 LoRA `bespokelabs/Bespoke-Nimble-9B` on Qwen3.5-9B (repo license absent). Their 324-row holdout is a named receipt, not a ranking. `research/notes.md` §35.
- **mmastrac/djev-spark** — DiffusionGemma 26B-A4B NVFP4, Jev-shaped decisions, images as an extension. Third compute graph. Interface claim, not a win over a decision head. `research/notes.md` §36.
- **Perception then judgment** — SAM 3.1 (masks and tracks) or ASR (a transcript) are upstream producers, not the perceive species. System One on that state is decide. Composition, not native omni. Information dies at the interface. Open multimodal *decide* that ships now: blackwood-rlcd (not Archer). `research/notes.md` §39, §46.

### Structural prove ∩ remainder
- **thevibeworks/jevgate** — Proven / Refused / Unknown; cannot block; 0/59 unsafe unasked held-out. Allowlist **proves** read-only verbs; Jev judges only unlisted. Allowlist ∩ System One.
- **coldteadotai/abide** — same family, different remainder: linter proves lintable rules; Jev Scores residual soft AGENTS.md rules; fail-open, banded. `notes.md` §47.
- **suraj-phanindra/wellposed** — lint the Jev request before it comes back confidently wrong. Missing `other` → confidence 1.00 on a wrong Choice; gating cannot catch it. `tenbin` owns the lint skill. `notes.md` §46.
- **misbahsy/doc-router** — page OCR router: 155→87 billed, 1.74× $ on 19 docs / 155 pages. Same sandwich.

### Agent harnesses extras (this hour)
- **kevinpita/pi-jev-context** — reversible Pi context sieve: hide, do not delete; `/jev off` restores. Cousin of winnow/jevprune.
- **vava-nessa/pi-jev-compaction** (and `tamaratran/fast-jev-compaction`) — verbatim drop, never summarize. Pair with jev-gate-student-b for local memory-gating. Same *job* as [gliner25-compaction](https://github.com/m-newhauser/gliner25-compaction) (GLiNER2.5 encoder backend; `notes.md` §50). Stdout cousin [jev-pruner](https://github.com/tamaratran/jev-pruner) — same family, prune Bash before the LLM, not session memory (`notes.md` §53).
- **reachjalil/jev-tree** — authored taxonomy so each Choice stays under 255; truncate silently drops the tail (`jev-tree-choice-cap`).
- **HacksonClark / SREGym-Lite** — Jev ranks next tests/evidence; does not diagnose; 20/50→24/50 with 2 regressions. `notes.md` §33.
- **ddfeyes/jev-mode** — bulk triage/tag/route off frontier context; synthetic 1,000: −77.8% tokens; accuracy is parity. `notes.md` §42.
- **runta-dev/jot** — closed-catalog System One shell (topology B). "First general-purpose" is a claim.
- **wotai-dev/typesafe-jev-tools** — meta-VOI: does this decision need a model? 149-row Jev vs Haiku 4.5.
- **memovai/openevals** — online every-step eval into Langfuse; code graders first. Beside Harbor, not instead of it.
- **poponline63/hermes-jev-north-star** — deterministic checks then Jev finish gate; empty evidence refuses.
- **TheoOliveira/pi-jev** — Pi semantic tool/skill routing. Not kevinpita/pi-jev-context.
- **vtrivedy/jev-plays-games** — Choice over legal moves; probabilities ≠ win odds.
- **ant4g0nist/joxide** — zoxide index, Jev shortlist, local paths only.
- **mgaitan/sqlite-jev** — batched NL judgments as a SQLite loadable extension (`jev_rows`). In-engine sibling of jevql's CLI rewrite; inspired by pg-jev. Semantic full scan, not an index. `notes.md` §44.
- **affirmitv/bitrate-advisor** — live ABR: Jev proposes, deterministic policy clamps (never bolder). Missing the model returns policy. `notes.md` §44.
- **nekowasabi/jev-routing** — Go host adapter for Claude Code / Codex / Grok Build. Not MCP, not npx. `notes.md` §44.
- **trietphan/jev-claw** — OpenClaw typed routing: Jev classifies, `decide()` in code. `notes.md` §44.
- **chris-wozniczek/jev-voice-control** — Speech → Jev → macOS actions. README-only this pass. Hypothesis. `notes.md` §44.
- **gamesonrblx/JevML** — claimed PCA/MCMC/diffusion/NCA primitives + a picker. README-only. Hypothesis. `notes.md` §44.

### Skills & tooling
- **typesafe-ai/skills** — official skill (contracts/patterns).
- **dbreunig/building-with-jev-skill** — doc-grounded question design + symptom→cause→fix diagnosis table (distilled into our `question-design.md`).
- **ax-llm/ax** — native `typesafe` provider; **typesafeainate/dspy-typesafeify** — DSPy decorator PoC.
- **riff (scale-venture-partners)** — hybrid static+semantic linter with ruff-style JEV codes and per-finding calibrated p; 14 calls ≈ $0.0004.
- **huntedman/JevLint** — file-level convention Nouls (magic-strings, descriptive-names); write→check→fix; no line-level/auto-fix. Sibling of jev-pref. Independent. Pointer: `notes.md` §26.
- **coldteadotai/abide** — productized Jev preference lint (Claude Code / Codex / OpenCode). Soft instruction-file rules as one Score per rule on the diff; linter owns hard rules; bands + fail-open; compile/calibrate/tune/replay. Replay 93 sessions: edit precision ~26% / turn ~73% (independent review, before tune). Fuller path of jev-pref; complementary to rh-guard. Text/diff only. `notes.md` §47.
- **super-jev / probably / jev-search** above — see their cards in `archive/findings.md`.

### Mixed architecture (2026-09-18T14 discourse + topic:jev)

Default placement, not a new product class: Jev judges, an LLM writes, code
owns control. Movers that sharpened the card: `git-jev-stage` (exact hunk
Choice), `jevprune` (per-line relevance with an always-keep set),
`llama-index-jev` (rerank fails open / select fails closed), `jev-pref`
(AGENTS.md as criteria; Abide is the productized path, `notes.md` §47), `lizard-agent` (no LLM when nothing needs writing),
`jevql` (judgment as SQL `WHERE`; CLI so Postgres never sees `jev()`),
`sqlite-jev` (in-engine SQLite extension; same hole), OpenSmoke (Jev over every step, LLM only
on flags). Neighbor skills `tenbin` and `decision-first` are *not* Augustus
clones — they own lint/eval and try-Jev-first habit. Entropy allocator
(**Hypothesis**): cheap typed scorers for low- and medium-entropy
decisions; a frontier write only for high-entropy synthesis
(`judgment-class.md`; `research/notes.md` §38).

### Hourly ~14:52 Boise (extractive / local surface / speed layer)

Patterns, not a catalog. `notes.md` §48. TypeSafe Jev is the exemplar in
the READMEs, not a monopoly.

- **AppitStudio/testimonial-miner** — extractive selection + multi-question broadcast + offline `redecide`. Model never writes the quote.
- **choxos/jev-reviewer** — pointer-not-generator: line ids; verbatim copy with place; *not found* is an answer.
- **egma-ai/jev-reviewer** — Jev assigns PR **attention** P0/P1/P2; OpenAI writes behavior deltas. Attention ≠ correctness. Not the choxos pointer product. `notes.md` §58.
- **us/jev-local** — contract-compatible `POST /v1/systemone`. Default scorer is a **stub** until `JEVLOCAL_SCORER=hf`.
- **hitakshiA/solari-reflex** — observe → decide → verified act; no screenshots. Author table vs Codex on Solari ~3–7× wall. Encoder-backend cousin: gliner2-ultrafast (`notes.md` §52). Specialist-form cousin: cua-s1 (`notes.md` §54). Harness cousin: Stagehand experimental Jev stack (`notes.md` §57).
- **ktaletsk/jevframe** — pandas/Polars `.jev` accessor; full `p__`; sibling of jevpandas.
- **de-niji/jev-hermes** — route ≠ memory: cheap intent gate skips memory tours.
- **ngallodev-software/agent-workflow-typesafe-ai** — advisory sidecar receipts; never changes host routing (Apache-2.0).
- **Joymfl/dag-jev** — structure induction over a bag (experiment; empty README; no metrics).
- **knowlet/jev-agentworld-web-simulator** — decision for control, generator for content; SQLite world.
- **ufx7/jev-testbench** — collab arms (`llm_autonomous` / `scripted_plus_jev` / `llm_plus_jev`); Wilson / McNemar.
- **alexykn/jevscan** — Tree-sitter ∩ typed questions. `tenbin` owns the lint skill.
- **cephalization/jev-oxlint** — skills→oxlint remainder after AST/precheck; Phoenix fixtures; experiment; not a hard gate. `notes.md` §58.
- **phin-tech/pi-jev-approver** — Pi shell gate; fail-closed without a key. Light rh-guard-adjacent note.
- **Mattepiu/laya-onnx** — Laya ONNX port (~15 ms CPU). Do not copy the vs-Jev table. Distinct later replica: [`gqgs/laya-onnx`](https://github.com/gqgs/laya-onnx) (complete Laya→browser int8; conversion smoke; `notes.md` §64).
- **kunchenguid/local-jev** — ModernBERT `/v1/systemone` approximation; **not** behavioral equivalence. Distinct from jev-local stub and jeff. `notes.md` §64.

Spotcheck this pass (not a fold): SemIf **1551★** (+60 vs awesome claim 1491); jevlike **866★**. Awesomejev 488/21644 not re-derived (public snapshot still 410 / 10,093). Tracker lastModified **2026-09-18T20:12:57Z**; Laya listed; Blackwood not. Archer still Watch.

### Hourly ~15:52 Boise (boundary map / Harbor bake-off / dual-process)

Patterns, not a catalog. `notes.md` §49. TypeSafe Jev is the exemplar, not a monopoly. Archer still Watch. X discourse blocked this hour.

- **Zaious/jev-capability-atlas** — when-it-holds map with API receipts. Axis: extractable from fed state vs needs outside knowledge. History suite table (A wrong@0.90 / B near-flat 0.07 / C right@0.97). Component node ≠ internals-as-FSM. Dangerous-high ECE (DAIR Emotion). Browser-use = DOM-as-text + fan-out, not vision.
- **nibzard/decision-model-benchmark (DMB)** — frozen protocol: jev vs 8 constrained LLMs vs baselines. v2 report of record. jev banking 76.3% / spam 93.0% / 256+ cap; p50 264–276 ms; $0.07/1k. No class wins on quality.
- **Jevals/jevals-data** — CC-BY-4.0 boards + JSONL. Recompute-from-logs. 2026-09-18 board (do not merge Banking77 with DMB/atlas).
- **taro1985/dual-process-ai** — Kahneman S1 decide / S2 generate. Routing accuracy unmeasured. Keyword fallback ≠ S1.
- **simonmesmith/jev-arc-agi-v1-experiment** — Direct Jev 4/400 (1%). Combinatorial ≠ extractive.
- **ikermoel/open-alternative-jev** — packed one-forward; RACE-H 92.9% @ 4.55 q/s. Not a Jev reproduction.
- **wfzyx/von** — 14 MB SAN local drop-in. Distinguishes from jev-local stub / kev pointer. Do not copy vs-Jev table.
- **jaredpalmer/kev** — light delta: **100★** this pass. No species rewrite.

### Hourly ~16:22 Boise (GLiNER2.5 extractive compaction)

Architecture notes, not a plugin catalog. `notes.md` §50. TypeSafe Jev is the exemplar, not a monopoly. **Not Jev. Not multimodal.** Archer still Watch.

- **m-newhauser/gliner25-compaction** — local GLiNER2.5 (`fastino/gliner2.5-base-v1`) retention Choice (`keep_full` / `keep_evidence` / `keep_call_only` / `drop`) + exact character-offset copies. Pointer family with testimonial-miner / jev-reviewer. Mutating tools / shell operators → `keep_full` in code. Fail-closed to `keep_full` (contrast many fail-open Jev gates). Same compaction *job* as fast-jev-compaction / pi-jev-compaction; encoder backend; Fastino/GLiGuard sibling class. `shadowMode` default true. Experimental; characters not tokens; no published retention-quality rates. Apache-2.0.

### Hourly ~16:48 Boise (CI merge-gate / fail-open wake / S1 indexer / claim-evidence)

Architecture notes, not a plugin catalog. `notes.md` §51. TypeSafe Jev is the exemplar, not a monopoly. Archer still Watch.

- **CaseReed/latch** — merge-gate: cluster in code, Jev labels cause, policy owns Gate PASS (infra) vs BLOCK (real). Judge never says ignore alone. Playwright reporter fail-open; `--gate` is a separate step. Pair Harbor + rh-guard. MIT.
- **shitianfang/wakegate** — fail-open VOI wake/resume (Horvitz). Skip only if Jev answers and p(wake)<0.2. 21/21 smoke (same author wrote scenarios+question). Contrast pi-jev-approver fail-closed / jevgate cannot-block. MIT.
- **GreyssonEnterprises/s1-graphify-indexer** (+ `s1-indexer`) — GLiNER default code-graph; escalate LLM only if backend loaded and low conf. 10–50× **unfilled**. Query does not invent edges. License not on GitHub this pass.
- **VladyslavHontar/clear-head** — Stop hook: claims vs session evidence. Keyword retriever; `JEV_FIRM` 0.6 never blocks below. MIT. 1★.
- **reification-labs/foreman** — description-only Phoenix scaffold (S1 specialists + S2 coordinator). Not the super-jev "foreman" loop. No Jev dep. Do not invent an Elixir API.
- **vinilana/jev-gateway-bench** — Harbor on/off routing; hidden chess perft; one-run signal (36/36 both; 4 vs 6 LLM req). Product sibling `jev-gateway` fail-open if Jev down. MIT.
- **LightningK0ala/jev-marshal** — Watch / empty repo. Policy-as-judgment PR cousin of Abide / if-ai.
- **LilDojd/jevons** — bounded Pi supervisor; shadow recovery; never generates commands. MIT.
- MED: if-ai (plain-English PR checks, fail-closed on error); omp-auto-mode (safe/unsafe/ask); jev-downloads-sorter (device-loop Choice); jev-label-desk (description-only); herdr-jev (~260 ms triage + triad; no-key heuristic).

### Hourly ~16:56 Boise (GLiNER2 Ultrafast observe→score→act)

Architecture notes, not a browser-agent catalog. `notes.md` §52. TypeSafe Jev is the exemplar, not a monopoly. **Not Jev. Not GLiNER2.5. Not multimodal.** Archer still Watch.

- **sahibzada-allahyar/gliner2-ultrafast** — local GLiNER2 (`fastino/gliner2-multi-v1`) scores observed a11y/DOM controls. Adaptation of jev-ultrafast. No screenshots; no generated selectors; code owns actuators. Hybrid local decide + remote Mercury 2.5 fill. `DONE` ≠ verified success. Same *job* as jev-ultrafast / solari-reflex; encoder backend. Contrast blackwood-rlcd (screenshot + marked letters). Cousin: ShaunSpark/laya-mind2web-browser-agent (Laya over DOM indices). Fastino sibling class with gliner25-compaction (different hole) and GLiGuard (safety schema). Demo (theirs, not re-run): Flights 12.20 s visible / 13.785 s loop / ~$0.0001 API — demonstration, not a bake-off. MIT.

### Hourly ~17:15 Boise (jev-pruner evidence-preserving Bash stdout prune)

Architecture notes, not a plugin catalog. `notes.md` §53. TypeSafe Jev is the exemplar, not the monopoly. **Not a summarizer. Not session compaction. Not GLiNER.** Archer still Watch.

- **tamaratran/jev-pruner** — after Bash, Jev Noul-prunes stdout chunks before the main LLM sees them. No summary. Hard envelope (≤10k estimated tokens; JSON/XML/YAML/diff/binary; whole-document commands) then soft Noul. Fail-safe keep original; full archive. Marketplace id still `fast-jev-output`. Codex is opt-in wrapper, not automatic interception. Same evidence-preserving *family* as fast-jev-compaction / gliner25-compaction; different *job* (command output vs session memory). Manual sweep (theirs): needles 24/24; mean reduction 83% on trim scenarios. Harbor plugin-eval cannot reach Jev. Terminal-Bench paired pilot is integration, not a full bench. MIT.

### Hourly ~17:21 Boise (Cua-S1 specialist form System One, source-only)

Architecture notes, not a Driver / MCP catalog. `notes.md` §54. TypeSafe Jev is the exemplar, not the monopoly. **Not TypeSafe Jev. Not GLiNER. Not a general CUA. Not multimodal pixels-in.** Archer still Watch. Weights Watch.

- **trycua/cua `libs/cua-s1`** — specialist System One computer-use research. Profile `cua-s1-form-v0` (form-oriented UI). Parent MIT; ~23.3k★ this pass. Byte-level `tinyx` encoder + option-attention head: per observed element fill (from extracted `Label: value`) / check / click / skip. Does not generate values or selectors. Code owns execution order. Plan ≠ execute; dry-run default; `execute` and `submit` independent opt-ins; submit at most one high-confidence Button labeled exactly `Submit` / `Submit Form`; fail-closed on missing checkbox state; fill execution fails closed unless the runtime advertises token-based `set_value`. Source-only: no weights, no checkpoint scores. Offline metric *names* only (accuracy, abstention, coverage, wrong actions/targets, unsafe when should abstain). Tests exercise implementation, not checkpoint quality. Same observe→score-among-candidates→code-acts *job* as jev-ultrafast / gliner2-ultrafast / solari-reflex / laya-mind2web; parallel "System One" name in CUA, not a TypeSafe contract. Watch for a `cua-s1-form-v0` artifact drop.

### Hourly ~17:48 Boise (CUDA replica, decision-native RAG, verbatim recall, Ruby primitive, FHIR Harbor, AMBIGUOUS baselines)

Architecture notes, not a CUDA/venv / gem / mcp / uv catalog. `notes.md` §55. TypeSafe Jev is the exemplar, not the monopoly. Archer still Watch. X MCP flap; `since_id` not advanced.

- **Mintzs/jevify** — CUDA/PyTorch parallel Choice/Score/Noul *shape* on Qwen2.5-1.5B (`ora_decision_engine`). CUDA graphs, branch kernels, literal-label scoring. **Uncalibrated likelihoods ≠ Noul.** Independent of Distillation. Default refund workflow is not a validated policy. No LICENSE this pass.
- **emergency-lee/decision-native-rag-skills** — MIT. Retrieve wide → decide → evidence set → conflict resolve → reason only over kept evidence. Provider-agnostic. No bundled harness. No universal benchmark. Core Augustus RAG mental model. Classify-first MCP cousin: **kbhuw/jev-sift** (`notes.md` §56).
- **Dharundp6/jev-carryforward** — MIT, 1★, npm `carryforward`. Verbatim session ledger; Jev scores recall; rules never judged; fail-open dump. 9×3 hint, not proof.
- **carldaws/hunch** — MIT. Ruby `chance`/`pick`/`rate`; English-as-config; `rescue nil` fail-open at save. Cousin of probably-lang (library, not a new language).
- **si618/explore-typesafe-ai** — FHIR S1 (Jev) + Claude S2 on 100 synthetic Synthea patients. Labels first. 60 requests / 403 judgments. **Not clinically validated.** License not in API this pass.
- **ickma2311/jev-baselines-eval** — MIT. Pre-registered vs nano/frontier/encoder. **Both AMBIGUOUS.** Cascade sign-flip at exact parity; confidence=1.0 theater; encoder 0.933/9ms with labels; serving-path ≠ model-speed; same-day errata ×3. jevals/Harbor practice exemplar.
- **SargeDev/jev-gate-student-b** — light delta only; HF card unchanged (MAE 0.187 / Pearson 0.791 / 90% n=60; fail-open; teacher-copy).
- MED: **fdemir/toolgate** (pre-exec allow/block/review; Jev not authorization; 72-case synthetic); **masa-med-ai/typesafe-screening-mcp** (PubMed include/maybe/exclude; 326 hits ~17s ~$0.014; screening aid); **laurentfabre/databricks-jev-pdf-lab** (honest negative; no OSS license); **yannip1234/codex-jev** (extractive Codex compression; 185→44 estimated tokens is an integration demo; equal accuracy/lower cost not established); **kazuhideoki/jev-search** (recursive *file* search + fzf; **not** superagents-lab federated web search).

### Hourly ~18:38 Boise 2026-09-18 / 00:38 UTC 2026-09-19 (classify-first MCP + living applied-mappings atlas)

Architecture notes, not a plugin / showcase catalog. `notes.md` §56. TypeSafe Jev is the exemplar, not the monopoly. Archer still Watch. No invented metrics. No 342-title dump.

- **kbhuw/jev-sift** — classify first, read selectively. Batch path / public URL / inline text → Jev relevance or 1–8 typed questions. Content to Jev without entering main agent context first. Envelope (theirs): 50 items, 60k char, 2 MB / 20 s, public-IP only, no JS/cookies/login, PDFs unsupported. Uncertain/errors/truncation ≠ irrelevant. Transport tests (mocks) ≠ accuracy. No LICENSE this pass. Same retrieve-wide → decide → evidence-set family as decision-native-rag-skills. Topology A MCP; **not** nekowasabi/jev-routing (host adapter).
- **jevable.com** — living applied-mappings atlas. Claimed **342** curated projects; JSON-LD first page **36**. Categories: Agents, Browser extensions, Creative tools, Data & research, Developer tools, Experiments, Finance, Games, Marketing, Productivity, Robotics. No public API this pass. Class patterns: intent columns, score-among-observed, VOI gates, generative UI decide, robotics text-state, draft-gate silence ≠ safer. Maker clocks stay claims unless already a named receipt.

### Hourly ~18:48 Boise 2026-09-18 / 00:48 UTC 2026-09-19 (Stagehand experimental Jev pick-and-copy)

Architecture notes, not an SDK catalog. `notes.md` §57. TypeSafe Jev is the exemplar, not the monopoly. Archer still Watch. Draft stack. No invented metrics.

- **browserbase/stagehand #2951–#2955** (MIT parent; all OPEN draft; author miguelg719). 5/5 user link: [#2955](https://github.com/browserbase/stagehand/pull/2955) extract completion **judge** + **pick-and-copy**. Jev picks a11y elements; code copies text. `extract` `"off"` | `"judge"` | `"pick"`. Both modes send page/extracted content to TypeSafe. Schema/gate/screenshot-always-LLM in code; LLM fallback. Their card (gemini-3.8-flash, Browserbase, local, 25×3): 69/75 vs 23/25 (92% both); **37/75** no-LLM ~0.5 s vs baseline **4.37 s** / two LLM calls; LLM-off **36/75** — pick is a fast path, not a replacement. Stack: #2951 editable ids (outline byte-for-byte unchanged); #2952 client + pick library (`best`+`strict`); #2953 act tree; #2954 observe + cache-check (errors never block replay). Same observe→score-among-candidates→code-acts *job* as jev-ultrafast / gliner2-ultrafast / cua-s1 / solari, inside a major harness. Do not merge clocks. Do not copy `experimentalJevAct`.

### Hourly ~18:46 Boise 2026-09-18 / 00:46 UTC 2026-09-19 (public wall, meaning-search, attention≠correctness, skills→oxlint, session-sticky route, measured RAG rerank)

Architecture notes, not a Convex / uv / pnpm / dylib catalog. `notes.md` §58. TypeSafe Jev is the exemplar, not the monopoly. Archer still Watch. No invented metrics. Do not re-fold §50–§57.

- **waynesutton/ask-jev-ai** — public realtime judgment wall; 6 parallel questions/ask; policy-in-code (`convex/questions.ts`); safety p≥0.6 blocked; no-key allowlist (UI says Jev offline). Cost $0.000032–$0.000041/ask from TypeSafe token counts → $32–$41/1M. Live askjev.ai. License null this pass. Productized System One primitive surface.
- **Bentlybro/jevgrep** — MIT. Meaning-search CLI+MCP (`jgrep`) without embeddings. Packed parallel Jev relevance; two-stage outline→zoom. 228 questions on docstring-stripped repos: **79% top-5** vs BM25 40% / grep 20%. Keyword still wins exact strings (BM25 top-10 96% vs 85%). Packed+parallel 0.9 s vs serial ~23 min AutoGPT 4,329 files. Distinct from kazuhideoki / superagents-lab / jev-sift.
- **egma-ai/jev-reviewer** — MIT. Jev assigns PR attention P0/P1/P2; OpenAI writes behavior deltas. Attention ≠ correctness (anti-soundness-theater). **Not** choxos/jev-reviewer. Local CLI; does not publish PR comments. Incomplete never P2. Demo: real Jev + labeled prepared explanation copy; live OpenAI pending funded API.
- **cephalization/jev-oxlint** — experiment; nothing published; license null. Skills→oxlint: AST/precheck in code; guidance whole-file in state; survey/calibrate/propose. Phoenix: answer-key agree on every fixture; found flush-only-on-success (noul 0.07); routing sharp; coarse hint not. Not a hard gate. `tenbin` owns the lint skill.
- **jxu-dev-c/jev-adaptive-thinking** — Go CLIProxyAPI plugin; license null. Session-sticky first-prompt classification; later turns never reclassify; fail-closed lock to `gpt-5.6-sol`. Same family as routeKit. Live testing left to the deployer.
- **Max-sm-yc/Jev-RAG** — license null. One-run: ≥70% cost / 72% latency vs Muse Spark *rerank*; full-context Spark still faster (10.60 s). Costs include embeddings.
- MED: **EpicEric/safe-sh** (AGPL-3.0; static shell analysis, not pre-exec auth); **ravikadam/jev-loan-triage** (17 typed questions; policy in `loan.js`); **TurboGuo/jev-fedspeech** + **jev-dating** (Jev vs chat arenas; prior empty search was a query miss); **g-h-miles/jevbox** (MIT; drum grooves). hermes/mcp packs: **no new pack this pass** (hermes-jev-north-star / jev-hermes already folded).

### Hourly ~19:48 Boise 2026-09-18 / 01:48 UTC 2026-09-19 (capability kernel, typed DSPy control plane, calibration arena, engine-owns-truth, human-confirmed kill)

Architecture notes, not a pip / venv / Cloudflare catalog. `notes.md` §59. TypeSafe Jev is the exemplar, not the monopoly. Archer still Watch. No invented metrics. Skip parody (`SPFreedom/jef-mcp`) and account farming (`rayelzz/jevregist`). Star spike this day: SemIf 1491→1606 (this pass 1607★); vinnylarouge/jevlike 851→896 (this pass 897★).

- **somoore/interlock** — MIT, Python. Capability kernel: LLM ring 3 / Interlock ring 0. Secrets never enter the agent (canaries/placeholders). Closed action space. Jev is SENSOR; `policy.py` decides BLOCK/ASK/ALLOW. Anti-pattern: launch-week firewalls that ask "dangerous?" after the LLM already decided with real secrets in scope. Type-safe ≠ correct; irreversible behind threshold AND human. Distinct from toolgate. 38-case local-judge set, not a blind paper.
- **manikanda-kumar/jev-dspy-control-plane** — MIT, Python. Benchmark-first: constrained classifier as typed control plane around DSPy. Classifier → ontology → security override → confidence → state machine → tool allow-list; DSPy drafts AFTER route+action. OpenJEV / DSPy / JSON Schema share ontology. Offline heuristic ≠ quality. Accuracy alone is not enough.
- **meetr1912/jev-arena** (+ **jev-sonar** / **jev-vickrey** / **jev-bracket**) — MIT, Python. Native-probability calibration on analytic worlds (not verbalized confidence). Live *theirs*: 145 noul, Brier 0.0059, ECE 0.0620, 2 requests / 710 ms; overconfident in low bins. Sonar: heatmap-as-policy. Vickrey: Jev never bids; code monotonizes CDF. Bracket: Brier vs Elo; live trailed Elo (honest).
- **JoelLewis/game-coach** — GPL-3.0, TypeScript. Wave 0 PRD: Stockfish owns truth; Jev owns judgment; templates + capped writing model own words. Anti-soundness-theater with egma attention≠correctness. ~$0.012/chess game (theirs).
- **epiphany-dynamics/port-cleanup** — MIT, Swift. Jev recommends; human is the only kill trigger; identity re-check; shields override; mapped explanations not raw model prose. conf ≥ 0.8 for kill recs. Gate UX + rh-guard cousin.
- MED toolbelt: **1jehuang/jev-pr-labeler** (conceptual scope, not line counts); **RubyBrewsday/jevcumber** (.feature only; pointer among observed controls); **shkumbinhasani/typedecide** (class SDK; not on npm); **douglance/jevon** (CLI+MCP; key not in agent config); **buberlo/dsh-jev** (DSH plugin; can only gate, never widen); **zaycruz/fast-jev-compaction-pi** (pi port of fast-jev-compaction); **planstack-ai/jev-tetris-benchmark** (legal set in code; not a rigorous eval); **fabricioctelles/modelsystem** (modelsystem.one catalog; 1★; not affiliated); **emirbartu/opencode-system-one** (fail-open plugin; license null; 1★); **phanngoc/browser-ai** (Go CDP; design done, implementation tracked); **acorn181/semantic-bookmark** (user-authored semantic rules).

### Hourly ~20:43 Boise 2026-09-18 / 02:43 UTC 2026-09-19 (domain specialist vs few-shot hosted, decide→policy leftover cascade, ORDER BY calibration≠sortable, GLiFormer wire-compat backend)

Architecture notes, not a uv / bun / Modal catalog. `notes.md` §60. TypeSafe Jev is the exemplar, not the monopoly. Archer still Watch. No invented metrics. Do not re-fold §50–§59.

- **help-er/Domain-jev-maker** — MIT, Python. Domain LoRA on independent CLINC-150 gold (not a Jev teacher-copy). Matched-precision KL: local 0.168 vs hosted zero-shot 0.580 banking; r +0.933 vs +0.343. Few-shot hosted determinate McNemar n.s. Train specialist when downstream reads p; hosted+examples when only argmax.
- **skiingfalcon/jav-email-cascade** — Python; license null. Decide→policy→LLM leftover. jev vs gen-json vs gen-logprob on one Answer schema. Noul 0.5 never rounded. Mock gen-json confidence flat is *their mock*. Distinct from dual-process-ai (routing unmeasured).
- **yodablocks/jev-orderby-bench** — MIT, Python. Independent ORDER BY measurement. Six gates pass. Score ordinal 0.143 weak link; 53-way 0.99 tie; calibration ≠ sortable. recodelabs batch-40 fails ranking. Not a fourth DuckDB extension.
- **logan-markewich/jeff** — Python; license null. GLiFormer-400M `/v1/systemone` typesafe-sdk drop-in. ~$2.6 vs $15.6 L4 HTTP (~6×); A10G direct ~$0.65 (~24×); AG News 75.5% vs 90.5%. CPU more expensive. Encoder ≠ Jev replica.
- MED: **hraness/sysone** — MIT, TypeScript. Loopback gateway; routes hosted Jev + local OpenJev/NanoJev/Mini-Jev; does not run weights; credential from env never config.

### Hourly ~21:39 Boise 2026-09-18 / 03:39 UTC 2026-09-19 (active-learning triage / don't distill Jev as teacher, evidence-packet explorer, meaning-grep, closed-vote CU, Jev vs MLX PCD Harbor, host-owned waymode, OMP/pi fail-open gates)

Architecture notes, not a pip / npm / bun catalog. `notes.md` §61. TypeSafe Jev is the exemplar, not the monopoly. Archer still Watch. No invented metrics. Do not re-fold §50–§60. Skip empty `edwardyen724-g/jev-compactor` and `jlt-commons/laya-jolt`.

- **ThyFriendlyFox/jev-triage** — MIT, Python. Active-learning: high conf accept / middling expensive teacher / low-or-boundary human. Logs full distributions. **Do not distill Jev as teacher of record** (~68% ceiling). Real outcomes stay the targets. Distinguish Domain-jev-maker (independent gold) vs openjev-lm (teacher-copy).
- **jimmyhealer/jev-semantic-explorer** — MIT, Python (jevex). Index-once ask-many; citable evidence packets. Claude Code 6.8→2.2 files. SWE-bench Verified n=8: **1/8 → 6/8** finish (empty = miss, author-run). Packet n=50 HitFile 0.233 vs BM25 0.159 is diagnostic, not the product KPI.
- **uehaj/jev-semgrep** — JavaScript; LICENSE MIT (GitHub NOASSERTION). Zero-dep Node; AND/OR/NOT over line Nouls; JP↔EN. Distinct from jevgrep. Precision 0.94 / recall 0.98 *theirs*. Name collides with Semgrep SAST.
- **buluoray/JevOnly** — Apache-2.0, Python. Closed-vote-only: code builds options, Jev only picks; **no planner LLM**. Fact register + verify/undo. 11 steps / 43 calls / ~$0.014 / 17 s *theirs*. Distinct from Stagehand LLM fallback.
- **mallahyari/system-one-benchmark** — Python; license null. Harbor-shaped Jev vs local MLX PCD (Qwen2.5-1.5B) vs AR JSON on LMSYS toxic-chat n=50. Jev **84.0%** / Brier **0.1096**; PCD 52% / 0.3884 / O(1). PCD speed ≠ calibrated Noul. Small n.
- **mossburgh/waymode** — MIT, TypeScript. App retains handlers/permissions/validation/state; Jev over live typed actions. 24/26 + 34/36 *theirs* — bounded development evidence, not a self-driving proof. Not on npm.
- **luw2007/omp-jev-extensions** — MIT, TypeScript. OMP/pi `jev_acceptance_gate` + `jev_route`. **Fail-open** if Jev missing (`confidence: 0`). Contrast pi-jev-approver fail-closed.

### Hourly ~22:38 Boise 2026-09-18 / 04:38 UTC 2026-09-19 (permission vs probability, judgment ≠ permission outline, eval instrument-not-score)

Architecture notes, not an `omp plugin` / pip catalog. `notes.md` §62. TypeSafe Jev is the exemplar, not the monopoly. Archer still Watch. No invented metrics. Do not re-fold §50–§61. Watch archive path missing this VM; receipts from live GitHub.

- **SemetricLabs/omp-greenlight** — MIT, Python. OMP plugin grades gated tool calls and suppresses the approval prompt when Jev says allow. **1,013 calls / 10 sessions / 8.95 h.** Default **40.9%** prompts removed; **0 of 94** unsafe auto-approvals on a 140-row labelled corpus (live traffic unlabelled). Operator owns thresholds; plugin never self-tunes the safety bar. Not a sandbox; host `bash.patterns: deny` fires first. Agent prose withheld (0→3 corpus misses). Never shadows a built-in tool. Composes with waymode / omp-jev-extensions. Distinct from specpi-jev-guard / toolgate / interlock.
- **adamjralph/skill-broker** — language/license null. **Project-outline only** (`PROJECT-OUTLINE.md`). Hermes pre-agent: code owns catalog/policy/grants; Jev scores relevance/confidence and **never grants access**. Jev down → foundation-only; never broaden access. Replayable route evidence. **Not a production recipe.** Distinct from jev-hermes and shipped §5 routers.
- **collapseindex/dinostomp** — Python; README Apache-2.0 (GitHub NOASSERTION); 5★. Eval verification layer: checks the instrument, not just the score. FINDINGS.md 189 (F 52 / D 99 / N 38); **99 against itself**. `dinostomp jev` tests a Jev question like an if-statement (accuracy / p(yes) cut / ECE / blank lean / rewording). Demo *theirs* 24 examples: 100% / ECE **0.062**. Beside jevals, not a Harbor taskset. Anti-soundness-theater cousin of rh-guard / egma / game-coach.
- MED: **nrdz-labs/fast-jev-opencode** (MIT, TypeScript; OpenCode V2 context-hook port of fast-jev-compaction; fail-open; 1★); **yikangy873-gif/jev-desktop** (MIT, JS; Codex Computer Use action selection); **MrDiamondBallz/jev-agent-integration** (MIT, Python; provider-neutral Hermes skill/plugin); **bohutang/sift** (MIT, JS; X feed semantic labels/hide); **CorieW/JevExplore** (TypeScript; license null; bounded web action-space discovery).

### Hourly ~23:40 Boise 2026-09-18 / 05:40 UTC 2026-09-19 (constrained optimizer + S1 features, privilege ≠ verdict, attention/VOI never-block)

Architecture notes, not a uvicorn / bun / marketplace catalog. `notes.md` §63. TypeSafe Jev is the exemplar, not the monopoly. Archer still Watch. No invented metrics. Do not re-fold §50–§62. Watch archive path missing this VM; receipts from live GitHub + HF. Hunches labeled.

- **zeeshan8281/slo-router** — Python; license null. Jev supplies bounded task / exactness / external-evidence features; a constrained controller picks the cheapest backend meeting quality + latency SLO floors. Fail-open to local deterministic features. Exactness raises the quality floor; never overrides capability. Measured *theirs*: same routes/accuracy as the local path; p95 E2E **77.93 → 490.38 ms** (~6.3×). 3/8 task-label disagreements did not change routes. Eight-row demo is not a benchmark. **Hunch:** System One on the feature side of a constrained optimizer, never the sole hot-path gate. Harbor-style latency measurement is mandatory before claiming “Jev routing.”
- **godspede/construct-auto-classifier** — Apache-2.0, TypeScript. Effect-based shell safety gate (OpenCode / Antigravity). Fast-allow/deny <1 ms, then Jev Choice + nine independent risk Nouls. Operator-owned `minConfidence` / `riskThreshold`. Fail-closed. **Privilege ≠ verdict** (`sudo status` can be safe). Certification *theirs*: **975** decisions/model; Jev **0** dangerous allowed; every chat model leaked 16–104. Pair with dinostomp (instrument) and omp-greenlight (operator-owned dial). **Hunch:** contracts on effects, not surface tokens.
- **rashedInt32/jev-lens** (+ **jev-lens.nvim**) — MIT, JavaScript / Lua. Claude Code stop-hook: calibrated “do I need to look / which files / strip debris?” **Never blocks** the agent, never edits files, never says green unless sure. nvim popup is display-only (no API key). Distinct from jev-gates (stops writes). **Hunch:** attention filter / VOI for human review, not a permission gate. Complements skill-broker and omp-greenlight.
- MED: **sysone-help/sysone** (MIT TS; evaluation-model-first SDK; cancellable; never auto-retry; first adapter Jev via Vercel AI Gateway; **not** hraness/sysone loopback gateway); **ctaxnagomi/INSTRUCT_JEV** (HF; MIT; 119 rows, 47/51/21 choice/noul/score; jevals seed); **ckaik/swift-jev** (MIT; LICENSE-only this pass; not a CLI product).

### Hourly ~00:39 Boise 2026-09-19 / 06:39 UTC (measurement owns endorsement, Jev supplies evidence / code owns authority, ranking ≠ calibration)

Architecture notes, not a uvx / pnpm / marketplace catalog. `notes.md` §64. TypeSafe Jev is the exemplar, not the monopoly. Archer still Watch. No invented metrics. Do not re-fold §50–§63. Watch archive path missing this VM; receipts from live GitHub. Hunches labeled. Do not re-fold sysone-help/sysone.

- **dtduc-git/jev-packs** — Python; CC0-1.0. Evidence-gated registry: `pack.yaml` + `cases.jsonl` + `evidence.md`. A pack is only `verified` after accuracy / ECE / cost / latency on pinned `jev-1.13.0`. `unknown` mandatory on every Choice/Score. Backend-neutral. Named suite jevassert → jev-packs → jev-table; **jevassert and jev-table 404 this pass** (runner not released; packs structurally validated by CI). Nine packs `verified` *theirs* (single-run): citation-support 800 / 0.919 / 0.022; rag-answerability 840 / 0.908 / 0.021; moderation 1350 / 0.906 / 0.027; rag-passage-relevance 800 / 0.899 / 0.035; entity-merge 840 / 0.857 / 0.017; support-triage 1350 / 0.887 / 0.059; sms-spam 150 / 0.967 / 0.053; boolq-yes-no 150 / 0.887 / 0.063; banking-intent 150 / 0.840 / 0.090. Dataset-derived keep upstream licenses. Distinct from INSTRUCT_JEV (no evidence gate) and dinostomp (instrument). **Hunch:** Harbor/jevals pattern — measurement owns endorsement; packs without evidence stay `provisional`.
- **omkarghugarkar007/actiongate-jev** — TypeScript Apache-2.0. Runtime authorization: deterministic policy / RBAC / schemas own ALLOW | REVIEW | BLOCK; TypeSafe Jev via OpenRouter is semantic evidence only. Slogan: **"Jev supplies evidence. Code owns authority."** A positive model score never overrides a deterministic security failure. Six narrow questions, never one "is this safe?" Financial / destructive / credential fail-closed if Jev is down. 500-case eval is **label-baseline integrity, not accuracy**. Early MVP. Distinct from toolgate / interlock / construct / greenlight. **Hunch:** canonical anti-soundness-theater counterexample — decision models as sensors, not sole hard gates.
- **Adilmp/does-jev-confidence-mean-anything** (+ **Adilmp/jevcal**) — Python; license null / MIT. Calibration audit: **8,000** judgments vs `civil_comments` humans on `jev-1.13.0`; $0.05. Ranking strong (AUC **~0.91**; rank corr 0.96) but probabilities systematically shifted toward "yes": when Jev said **~75%**, humans flagged **~10%**. Two-parameter recalibration removes **~96% of ECE** without changing rank (`natural`/tightened ECE 0.156 → 0.006). Accuracy is a trap (`insult`@0.5 61.0% vs always-no 67.8% while AUC 0.83). Vendor "calibrated" is rank-correlation, not frequency units. Companion jevcal: ~100 labelled rows (94% of error at 100). ECE gameable (constant base-rate ECE 0) — they decide on **Brier**. One domain; do not cite `threat` (n=1). **Hunch:** never hard-threshold raw decision-model p as a frequency without domain recalibration.
- MED: **gqgs/laya-onnx** (complete Laya→browser ONNX int8 496.8 MiB; conversion smoke; distinct from Mattepiu/laya-onnx); **kunchenguid/local-jev** (ModernBERT local `/v1/systemone` approximation — not behavioral equivalence; distinct from jev-local stub and jeff).

### Hourly ~00:39 Boise 2026-09-19 remainder (hot-click CU, verbatim compact+gate, local-rules-then-remainder)

Architecture notes, not an install.sh / pnpm / wrangler catalog. `notes.md` §65. Same hour as §64. TypeSafe Jev is the exemplar, not the monopoly. Archer still Watch. No invented metrics. Do not re-fold actiongate / jev-packs / sysone-help.

- **jiangkoumo/ego-jev** — JavaScript MIT. Drive ego-lite with Jev: indexed viewport table → operation+target in one request. Code owns observe/execute/stale-ref/loop/`--until`. Text model only when typing is needed; never guess a fill. Jev `done` ≠ business success. Measured *theirs*: HN **4.9 s vs 9.7 s**, wiki **5.4 s vs 10.1 s** (~2× vs per-step `kimi-k3`; n=3; high variance; not a benchmark). Cousin of jev-ultrafast. Distinct from JevOnly / waymode / Stagehand.
- **edwardyen724-g/jev-compactor** — TypeScript MIT; **1★**. Was empty skip §61. **"Jev judges relevance. Code decides structure."** Never rewrite. Regex floor in code. Compaction fail-open if Jev down; safety fail-closed on pending destructive/exfil. One synthetic 12.7k-token session *theirs*: **64.5%** / **366 ms** / **$0.0004** / **0** hallucinated paths / **4 of 4** facts vs truncate 53%/1 of 4 vs Sonnet summary 96.2%/6.1 s/1 invented path. Claude Code shorter path: fast-jev-compaction. OpenCode fail-open port already §62: fast-jev-opencode.
- **zhuyansen/x-reply-filter** — JavaScript MIT. Chrome MV3. Local `rules.js` first, then batched four Nouls. Collapse not delete. Auto-hides sit in a confirm queue — **never auto-train on the model's own hides**. E2E *theirs*: 3 samples → 0.90/0.93 vs 0.08/0.10. Cousin of bohutang/sift. Cheap hold-before-show cookbook.

### Hourly ~01:47 Boise 2026-09-19 / 07:47 UTC (control-plane combinators, receipts-not-leaderboard, skill VOI, OOD/AUC≠ECE, frontier-100, turnstile, jevmlx)

Architecture notes, not an npm / cargo / pip / bun catalog. `notes.md` §66. TypeSafe Jev is the exemplar, not the monopoly. Archer still Watch. No invented metrics. Do not re-fold §50–§65 HIGH except one-line. Atlas axis already §49; skillranker existence already §7; jevmlx reconstruction already §1. Hunches labeled.

- **voidning/decision-combinators** — TypeScript; README MIT / GitHub license null. Then / Gate / Vote / Cascade / Weighted over Choice/Score/Noul. Analogized as logic gates; **not** literal AND/OR (those stay in code). No measurements. **Hunch:** System One as a control plane, not chat turns.
- **Zaious/jev-capability-atlas** — **10★** this pass. Receipts-not-leaderboard hold/break map. Type-safe ≠ correct (schema-valid ≠ picked-right). Extractable-from-state axis already §49 — do not rehash the history suite. Unofficial.
- **Dicklesworthstone/skillranker** — Rust; **52★**. Two-pass + none-of-these. Claude hook **fail-open** (quiet exit 0) — corrects §7 fail-closed. VOI over a skill library. Distinct from skill-broker (grants).
- **scienthoon/jev-ood-calibration** — MIT. 900 synthetic tickets + 3 public benches; ~$0.06. Public OpenBookQA ECE 0.024 / T 0.96. Synthetic ECE **0.107 = 4.4×** floor; priority (unknowable org rule) 44.7% / mean p **0.74** / T **3.40**; boolean T **0.66**. Sign flips by type. Do not threshold `confidence`. Complements does-jev-confidence.
- **softpudding/jev-frontier-100** — MIT. 100×3. Jev **77.0%**; Qwen3.5 4B off **56.0%** / 512 **78.3%** / 2048 **96.7%**. Exploratory, not preregistered. Attach the thinking budget. Not a ceiling.
- **zyphr-labs/turnstile** — Apache-2.0; experimental alpha; no npm. Deterministic policy first; Jev remainder; receipts + replay. Missing Jev → Review. Jev never grants what policy denied. Actiongate-class clone.
- **bnsd55/jevmlx** — MIT; **28★**. MLX one-pass schema→JSON+probs. Softmax ≠ Noul. No local leaderboard yet. Distinct from system-one-benchmark Harbor table.
- MED: **chopratejas/invalidate** (Apache-2.0; 5★; 157 cases 89.2%/97.5%/0 false invalidations; memory leases); **yottayoshida/jev-intent-review** (under construction; empty search ≠ proof); **shubhangi013/prune-review** (source preview; 22-run cost 1.18% with 305% outlier).

### Hourly ~02:38 Boise 2026-09-19 / 08:38 UTC (TLA+ compose, SEAL coverage ledger, skill-broker sibling, sureness, JevBench v1.1, CI typed gate, Codex MCP)

Architecture notes, not a cargo / pip / npm / action.yml catalog. `notes.md` §67. TypeSafe Jev is the exemplar, not the monopoly. Archer still Watch. No invented metrics. Do not re-fold the 01:47 list except sibling contrast. Hunches labeled.

- **copyleftdev/jev-labs** — Python MIT. TLA+ consensus kernel around live Jev. **Never confidently wrong.** 1,080 golden: 0 wrong under none/realistic/severe *theirs* (severe 314 correct / 46 escalate). Rule of three <0.28% — not a proof of zero. TLC 1,049,750 states / 0 errors. Synthetic pharmacy, not clinical. Inverse of soundness theater: escalate instead of hard-gate.
- **Reasonofmoon/seal** — Python MIT. **No seal, no advance.** Jev answers questions; SEAL answers whether the world may change. coverage.path ∈ {auto|code|human|escalate} visible. Mint ≠ product brain. Zero runtime deps.
- **adamjralph/skill-broker** — outline already §62. Sibling this hour: grants in code vs turnstile runtime authorize vs skillranker advisory VOI. Still not a production recipe. Language/license null.
- **adarc8/how-sure-is-jev** — Python MIT; zero-dep. max_prob/margin/entropy/gini/perplexity → CERTAIN|…|CLUELESS. Choice confidence = max_prob (most generous). Pair with ood-calibration.
- **fstandhartinger/jevbench** — Python MIT; unofficial. v1.1 Capability/Speed/Cost → Main Score. Jev 1.13.0 **87.6** *theirs*. Calibration **reported, not scored**. Native vs verbalized. Partial runs not ranked. Harbor/jevals practice, not a vendor eval.
- **NemanjaManic/ci-gatekeeper-bot-jev** — package.json MIT / GitHub SPDX null. Four typed questions → auto-approve|human-review|block before expensive review. Own-repo Jev **504–629 ms**. Conservative default escalated trivial diffs. Cousin of latch, not flaky-vs-real.
- **teempai/jev-in-codex** — TypeScript MIT. Codex MCP: jev_select_capability / jev_search / jev_triage. Ranking unbenchmarked. Lexical fallback. Distinct from jev-routing (not MCP).

### Hourly ~03:38 Boise 2026-09-19 / 09:38 UTC (attention redirect, pre-send views, tools≠use, observational memory, open-Jev class, physical-world S1)

Architecture notes, not a cargo / pip / npm / plugin catalog. `notes.md` §68. TypeSafe Jev is the exemplar, not the monopoly. Archer still Watch. No invented metrics. Do not re-fold the 02:38 list except sibling contrast. Hunches labeled.

- **muse0509/jev-preflight** — Go MIT; 1★; v0.1.0 Public Beta. Claude Code Stop-hook: eight risk axes in one request; assist = one reinspect then finish; **fail-open**; uncalibrated 0.85. Not a merge blocker (contrast latch / ci-gatekeeper / construct). Owner-run Claude Code 2.1.267: no-key fail-open PASS; key-enabled exactly one continuation *theirs*. Distinct from rashedInt32/jev-lens (human Stop filter).
- **godspede/construct-auto-classifier** — delta. Cert unchanged: Jev **0** dangerous / 975; $0.047/1k; chat leaked. **Landed-script trust** (byte-identical to remote default branch; trusts whoever controls that remote). **Headless ≠ auto-approve** (deny-and-report, not pending/auto-approve). Two gates cannot share one OpenCode prompt.
- **edwardyen724-g/jev-compactor** — product-arm bench *theirs*: **73%** (53–76%) / **350 ms** / $0.0004 / **4 of 4** vs Anthropic 86%/16.8s/3 of 4, Codex 85%, OpenCode 85%, Gemini 61%/4 of 4. 30–250× cheaper. Foreman safety in the same ~300 ms pass. §65 64.5%/366ms is vs-Sonnet on the same session. "Jev judges relevance. Code decides structure."
- **dizk/jev-lens** — TypeScript MIT. Pre-send view selection (outline/focus/testlog/…). 500 SWE-rebench trajectories: **79%** fewer tokens (11.6M → 2.4M). Compress **before** first send — post-send prune +17% cost (cache). **Not** rashedInt32/jev-lens. Claude plugin unmeasured.
- **Dharundp6/jev-carryforward** — delta. Plugin eval: `recall` **0/4** with tools+skill. **tools≠use.** SessionStart hook > hoping the model reaches for memory. 9×3 remains a hint.
- **willfish/pi-observational-memory-jev** — TypeScript MIT. Pi `/om`: Jev keep/kind only; verbatim ledger; model-free compact; kind-keyed durable topics. Failed Jev does not drain the buffer. Same anti-summary thesis as fast-jev-compaction / jev-compactor. Do not install beside amosblomqvist `/om`.
- **genai-craft/openvons** — Python; Apache-2.0 LICENSE / GitHub SPDX NOASSERTION; **7★**. Independent open-Jev class (LM/vision/voice finite-choice+prob; NOTA; execute/confirm/reject). Unrelated to TypeSafe. `/v1/systemone` **wire-compat, not a replica**. JevPick 3.2–4.8× byte-identical *theirs*. Flutter on-device.
- **AboveColin/HA-Jev** — Python MIT; **17★**. First real card (was a gallery stub). Sensors from typed answers; confidence gating; Jev-gates-LLM examples. **Not for locks/heaters/smoke.** `background:` triples laundry separation *theirs*. Confidence uncalibrated. Physical-world System One.
- **kylemclaren/jevql** — architecture note. CLI judges; vanilla Postgres never sees `jev()`. **Judgment outside the store** vs pg-jev / sqlite-jev in-engine.
- **bohutang/sift** — short use-case only. ~$0.00003/post *theirs*. Substance/Humor/Chit-chat/Promo/Junk + AI-written. Minimal consumer categorization surface.

### Hourly ~04:39 Boise 2026-09-19 / 10:39 UTC (digital-design combinators, VOI cache, skill-routing Harbor harness, zeroshot displacement, typed handoff)

Architecture notes, not an npm / npx / bun / plugin catalog. `notes.md` §69. TypeSafe Jev is the exemplar, not the monopoly. Archer still Watch. No invented metrics. Do not re-fold the 03:38 list except sibling contrast / combinators rename. Hunches labeled.

- **voidning/jev-combinators** — TypeScript; package MIT / GitHub SPDX null. **Rename** of decision-combinators (same `created_at`). Core five + **extended** Router / Loop / Retry / Fallback / Memory. Digital-design slogan (transistors / logic gates / chip) is a *metaphor* for soft classifiers; **not** literal AND/OR. npm `jev-combinators` 0.1.0. No measurements. Works with TypeSafe + any `/v1/systemone`.
- **kushals256/jevcache** — TypeScript MIT. OpenAI-compatible proxy: Jev admits same-intent cache hits; skip the expensive LLM. Fail-open. Live eval n=100 *theirs*: Jev **0 FP / precision 1 / recall 0.38 / fpr 0** vs Jaccard@0.35 fpr 0.48; $0.00174. Not in v0: streaming HITs.
- **iamdin/pi-jev-skill-bench** + **pi-jev-skill-suggestion** — TypeScript MIT. Harbor/jevals comparative harness: BM25 vs Jev at roster 50–500; 43 gold. **No live Jev numbers this pass.** Suggestion: strip roster; two-stage 0.30 / 0.40; no-key no-op; tool mode is tools≠use cousin.
- **zhuyansen/jev-zeroshot-vs-bert** — Python MIT. Jev beats clean DeBERTa-c on 7 sets (+0.05–+0.13; PAWS AUC +0.03; arXiv 2026 +0.30) *theirs*. Contaminated 0.901 vs `-c` 0.763. Label-equivalence ~230 / >2048. Banking77 512+ feature hurts. DiD 0.035 vs 0.112.
- **shitianfang/jev-handoff** — TypeScript MIT; alpha v0.1. MCP baton: typed escalate/continue/abort. Gate `allow` never grants. Fail-open. Inverted loop. Vercel drops confidence. Same author as wakegate.
- **ThinkyMiner/Winnow** — TypeScript MIT. Chrome worth-your-attention VOI. **Distinct from kevinpita/winnow.** read/skim/save/skip from typed answers; 80%/90% *theirs*. Not on Chrome Web Store.
- **rsdkrasen/hermes-jev-router** — Python; license null. **Jev WHETHER / Python HOW / LLM WHAT.** Compact original chunks; skip next main-model (needs core patch). Fail-open. Community plugin, not vendor.
- **mleyvaz/jev-typed-evaluation-collapse** — Python; license null. NCML field note v0.3 *theirs*: Noul collapses conflict vs ignorance; named Choice separates p=1.0; binary Choice lexically biased.
- **DowLucas/browser-jev** — TypeScript; license null. Playwright executes, Jev chooses. Sample from the distribution not argmax. Fail only high conf **and** high severity.
- **IamBusy/OpenJev** — Python Apache-2.0. Local 0.6B LoRA+scalar head. `/v1/decide` **not** TypeSafe drop-in. 45/60 *theirs*. Distinct from hraness/sysone OpenJev runners. **dddanielliu/semif-serve** — SemIf behind `/v1/systemone`; 1164 vs 178 ms *theirs*; wire-compat ≠ replica.
- Toolbelt notes: **win4r/jev-security-scan** (MIT; not a cert), **bojansandhaus/jev-decisions** (MIT; 1★; reviews never stop commands), **TeoMastro/jev-vs-llm-guardrails-intent-router** (license null; summary.md 404 this pass). **rh-guard owns reward-hack.**
- **ctaxnagomi/DGUI_HYPERMEM-JEV** — HF MIT; 6-row flywheel (analyze 4 / rerank 2 / supersede 0). Sibling INSTRUCT_JEV.

Census this hour (user-provided): Awesomejev **flat 561/27007**; tracker likes **43→45**, lastModified unchanged; SemIf **1714** (+10); jevlike **926** (+3). Archer still NOT landed.

### Hourly ~05:46 Boise 2026-09-19 / 11:55 UTC (record/replay CI, BBQ, decider≠executor, sentence-as-rule lint, open replica substrates)

Architecture notes, not an npm / uvx / cargo / plugin catalog. `notes.md` §70. TypeSafe Jev is the exemplar, not the monopoly. Archer still Watch. No invented metrics. Do not re-fold §50–§69 HIGH except sibling contrast / jevassert landing / prune-review, intent-review, laya-jolt, local-jev deltas. Hunches labeled. Calibration+cost as first-class gates. Open replicas diversify substrates under one contract — not TypeSafe clones.

- **dtduc-git/jevassert** — Python Apache-2.0. **LANDED** (was 404 §64). Record/replay CI: accuracy + ECE/Brier + cost/latency **offline from recordings**. PyPI `jevassert`; GH Action `@v0`. Pack SPEC v0 with jev-packs. `unknown` mandatory. Backend-neutral. Exit 0/1/2. McNemar. Do not copy `uvx`.
- **dtduc-git/jev-packs** — **delta**. CC0-1.0; size 0→458. Now pairs with the landed runner. First full matrix *theirs* (2,990 cases): Jev and Sonnet 5 statistical tie on accuracy (Δ≤0.018); Jev better calibrated 7/9; ~250× cheaper ($0.000014–0.000031 vs ~$0.0036). sms-spam this-pass **0.953 / ECE 0.040**.
- **chenmingtang830/jevarena** — TypeScript Apache-2.0. Open BYOK arena; preview jevarena-lab.vercel.app. **Failure-finding, not crowning winners.** Python harness remains JevJudge-Bench. Runnable harness, **not measured findings**. **≠** meetr1912/jev-arena. Always qualify the owner.
- **simonmesmith/jev-bbq-experiment** — R; license null. Full BBQ 58,492; Jev 1.13.0 **56,900 / 97.28%**; amb 99.96% / inf 94.60%; bias **0.04 / 0.34**; **$0.3429 / 7.75 min** *theirs*. 12 of 13 amb errors stereotype-aligned; inf errors mostly unknown (1,487/1,579). Order diagnostic 1/484. **Not a general bias cert.** Dataset CC BY 4.0 BBQ.
- **thomasbrueggemann/jeffrey** — TypeScript MIT. **Decider ≠ executor:** Jev next-tool/progress/risk/done; LLM only fills args. Loop Jev→tool→Jev. Risk≥0.5 pause. Stuck ladder (2 Jev / 0 steps). Pick ≠ fill. Mapping §9 still rejects the fused planner-writer.
- **mizchi/jevlint** — TypeScript MIT. **ast-grep subjects × sentence `ask:` scored by Jev.** Matcher silent-fail vs Jev loud. 13/15 naming/comment rules **1.00/1.00** *theirs*. Review mode 4-fn diff 2 req / $0.00013. Fail-open no-verdict. **≠** huntedman/JevLint. Always qualify the owner.
- **shubhangi013/prune-review** — **delta**. 22-run numbers unchanged: winning 27.9% post hoc; all 22 incl. 305% outlier **1.18%**; excl. outlier 15.9%. Target ~20%. Cost not quality. Safety escarpment always keeps concurrency/auth/a11y/startup.
- **yottayoshida/jev-intent-review** — **delta**. Dual MIT/Apache-2.0. Whole-repo intent VERIFIED/VIOLATION/UNKNOWN/NOT_APPLICABLE. CLI works; GH Action not written. Empty search ≠ proof.
- **Eran-BA/Jev_from_GLiNER2** — spec-only; license null; size 0. GLiNER2-base-v1 → Choice/Score/Noul `/v1/systemone`. **No service, no training, no measurements.** Interface ≠ replica. Distinct from jeff GLiFormer.
- **bokuweb/grande** — Rust; license null. Rust/WebGPU System One; Archer/kev-shaped shared-state branches. JGLUE *theirs*: E2B zshot JNLI **0.614** ECE 0.252→**0.088** T=2.81; JCQA **0.853**. 270M **0.710/0.710**. Packed Δmax 7e-5. Isolation sibling 0.098 / state 0.996. Softmax ≠ Noul until calibrated.
- **jlt-commons/laya-jolt** — **delta** (empty skip §61). Clojure Apache-2.0. Byte-for-byte vs Python `system_one` on README quickstart. ~1e-7 last-digit drift. ~1.7 GB f32.
- **leesk212/JEV-CPU** — Python MIT. SemIf CPU semantic-if + web UI. **Meanblock/JEV-CPU 404** — only leesk212 exists. Cross-ref semif-serve §69. Demo GIF is PoC not a bench.
- **kunchenguid/local-jev** — **delta**. ONNX ModernBERT-large-zeroshot-v2.0. Measured vs jev-1.13.0 *theirs* (136 checkpoints): done **30%** / shape **57%** / r −0.06; gold done 26% vs Jev 87%; 112 min vs 21 s. Confidence omitted. Not equivalence.
- Toolbelt notes: **omkarghugarkar007/actiongate-jev** slogan already §64 (single-use ALLOW/REVIEW/BLOCK). **Nyarlathoteppppp/pi-heed** — TypeScript MIT; 3★. Persist user constraints across compaction; check side-effecting calls. Jev never writes policy. Fail-open. Shadow default. Bench *theirs* v0.8.0+Jev: recall **98.5%** / false block **0.0%** / $0.000058. Live: rule changed mid-session 8/13 off vs 0/13 on.
- MED: **david-j-lustig/system-one-responsible-ai** — MIT; size 0; README+LICENSE only. Framing stub. Pair with BBQ, not a substitute.

Census **not re-derived** this hour (last §69). Archer still NOT landed.

### Hourly ~06:43 Boise 2026-09-19 / 12:50 UTC (SGR-judge Harbor contract, control-plane productization, never-generates, recipes+life feed, NAR claim-audit)

Architecture notes, not an npm / uvx / plugin catalog. `notes.md` §71. TypeSafe Jev is the exemplar, not the monopoly. Archer still Watch. No invented metrics. Do not re-fold §50–§70 HIGH except sibling contrast. Hunches labeled. Harbor-shaped **contract** before a quality headline. Control plane productization. Generation as a tree of Choices. Competing NAR claims are an **audit object**, not an endorsement.

- **slavadubrov/jev-judge-bench** — Python; README MIT / GitHub SPDX NOASSERTION. Frozen SLA-150: Jev vs cheap schema-guided LLM judges (Luna / DeepSeek-flash / glm-5.3-flash). Human labels; invalid = FN; cost/latency first-class. **No quality headline yet.** 21 offline tests. Canaries *theirs* not quality: Jev OpenRouter 5/5; Luna 10/10; DeepSeek GA 10/10; DeepSeek beta 8/10; GLM 5.3 10/10; GLM 4.7 4/10 overload. $10 Berlin live in progress. Direct TypeSafe untested. Five-field/H5 untested. **≠** chenmingtang830/jevarena **≠** fstandhartinger/jevbench. Always qualify the owner.
- **IPECTER/jev-context-pruner** — **EMPTY SKIP.** Description-only Codex compression-proxy slogan; contents 409 empty. Sibling of fast-jev-compaction / jev-compactor / dizk/jev-lens. Do not invent files.
- **shitianfang/jev-use** — TypeScript MIT v0.4.1. Claude/Codex/pi plugin: hand no-text steps to Jev; writing stays with the LLM. Same author as jev-handoff. Vercel `typesafe-ai/jev` 95 calls *theirs*: p50 **220 ms** / p95 423; 12q **186 vs 2,672 ms**; 20-step 4.3 s / 0 escalated; gate **12/12** / p50 199 ms. Vercel drops confidence → margin default **0.4**; first loop 17/20 then 0/20. Fail-open gate. **≠** jev-ultrafast. Do not copy `npx`.
- **goodruizhan/pi-jev-control** — TypeScript; license null; v0.3.0 private. Pi System-One control plane (router/gate/retry/sieve/review/GUI). Compaction never modifies on-disk session. GUI < threshold → unknown, never force-click. No live quality numbers. Distinct from omp-jev-extensions / jevons / pi-heed / pi-om. Do not copy `pi install`.
- **florian-hoenicke/jev-gpt** — Python; license null. Extreme decider≠executor: never free-generates; one typed question per WordNet/jina tree choice, then rank texts. ~**400** calls / **75 s** / **2 cents** *theirs*. Architecture demo, not a product. Distinct from jeffrey.
- **nexibeo/jev-cookbook** — JavaScript MIT; 1★. 15 OpenRouter recipes. Samples 16–36, **not benchmarks**. Recipes 01–13: **425** calls / **$0.015**; median 0.34–0.45 s; browser **5/6**. Pattern: code prepares, Jev answers. Do not copy OpenRouter tilde-id.
- **fengyiqicoder/jevfeed** — JavaScript MIT. Personal browser-history feed. No likes/follows/accounts. Last 200 pages local; one Jev request per batch of ten (distribution *is* ranking). 17 tests, no network. Distinct from ThinkyMiner/Winnow and kevinpita/winnow.
- **Heman10x-NGU/openJev-verdict-2.0** — **claim-verification, not endorsement.** Python; README Apache-2.0 / GitHub SPDX NOASSERTION. Hub heman10x/openJev-verdict-2.0 HTTP 200. README *theirs* N=2000: acc **77.10%** / Brier **0.0636** / ECE corr **0.0144**. Jev table row is a Laya-catalogued vendor baseline, not independent. **Open PR #1** audits: throughput 24.7/s misread as 25 ms (actual 40.5 ms; 3.5× not 28×); Laya 76.60% inside 95% CI (parity); like-for-like dist ECE 15.13% vs 21.40%, Jev 14.40% slightly lower. **≠** IamBusy/OpenJev `/v1/decide`.

Census **not re-derived** this hour (last §69). Archer still NOT landed.

See `references/mixed-architecture.md` in the skill. Class-level family
choice: `references/judgment-class.md`. Proof vs judgment (Alloy vs
Apalache; DST trio Antithesis / Resonate HQ / PufferLib):
`references/formal-methods.md` (one-screen: `formal-semi-formal.md`).
Cross-domain frames (not SWE-only): `references/mental-models.md`.
Hypothesis cards: `references/mappings.md` §6–§19.

## The skill that owns this analysis

[GitHub](https://github.com/24601/Augustus) — `SKILL.md` + reference cards
covering mental models across domains (not SWE-only), the judgment-model
class (Jev exemplar, not monopoly), mixed architecture, formal/semi-formal
placement, applied placements, method substitution, composition algebra,
question-design, validation, and optimizer coupling.
