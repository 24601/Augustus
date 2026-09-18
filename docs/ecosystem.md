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

### Languages & runtimes
- **probably-lang (southpolesteve)** — a programming language whose **loop conditions are Jev feelings**: `while draft feels "like a LinkedIn influencer post" { … }`. Judgment-state recordings give deterministic replay.
- **dannote/jev** — Elixir/OTP: Jev as a peer process; answers are messages; "clause order is the routing, thresholds are guards"; network-free tests.
- **jamesward/zio-typesafe-ai** — Effect-oriented (ZIO) client: Jev is the outer Choice; the handler runs the effect. Not Effect.ts and not the Jev HTTP contract. Hypothesis: `mappings.md` §19 (`notes.md` §28).

### Agent harnesses & self-supervision
- **Kevthetech143/super-jev** — domain-independent loop: observe → questions → decide → **permit (independent of confidence)** → execute (idempotency key) → verify → JSONL replay.
- **AntonioCoppe/jev-harness** — policy + confidence gate + shadow mode + offline eval CLI; 24-row filter 48.9s (Claude CLI) vs 1.3s Jev. Selective abstention.
- **Friedjof/jev-mobile** — durable Android worker + Mobile MCP; Jev sees prevalidated candidates only. `notes.md` §33.
- **jcpsimmons/jev-macos-loop** — Apple-silicon computer-use; local OmniParser/OCR/AX; text-only Jev. Finder demo independently verified.
- **rajdhakad9826/routeKit** — Jev estimates task requirements; policy engine selects the LLM. Jev does not pick the model.
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
- **dayhaysoos/jevals** — local MIT workbench: labeled cases (Noul / Choice / Score), compare runs, WebMCP + agent skill. Empirical acceptance-test surface for Hypothesis mapping cards; complements `evaluate_decisions.py`. Not affiliated with TypeSafe. Pointer: `research/notes.md` §24.
- **jeiel85/jevscope** — local-first visual debugger + JSONL regression for Choice/Score/Noul; compare two definitions; policy buckets are JevScope-derived. Sits next to jevals. Pointer: `research/notes.md` §25.

### Local / open heads & GLi\* species
- **GLiNER / GLiNER2.5 / GLiClass** — species map: locate spans vs categorize the sequence vs local multi-head (fastino-ai GLiNER2.5 CPU-first). Peer of Jev, not a footnote. `references/judgment-class.md`. Author primary source: GLiNER2 "like jev" is schema-conditioned categorize (GLiGuard), not a Noul (`notes.md` §28). 36× Browser Use claim is a tweet (`notes.md` §25).
- **GLiGuard** (fastino-ai) — 0.3B GLiNER2 encoder, checkpoint `fastino/gliguard-LLMGuardrails-300M`. One bidirectional pass over a safety schema. Same interface shape as batched questions; different objective. Not a Jev weight clone. `judgment-class.md`; `notes.md` §30.
- **DECRUX9812/openjev-lm** — Qwen2.5-0.5B+LoRA distilled from hosted Jev answers; 65/70 = 92.9% on 70 hand-labelled rows (one annotator, one domain, one seed) overnight on 6 vCPU. Its 98.1% on fresh rows is teacher *agreement*, not gold.
- **zmtomorrow/TypeAR** — constrained autoregressive decoding surface: typed fields on a pretrained open model, no retraining. Not a proper-scoring decision head. `research/notes.md` §32.
- **com-kotobalabs/open-jev-deberta-v3-large** — encoder open-jev, DeBERTa-v3-large 434M, apache-2.0, public gold (not a Jev teacher). In-domain ECE 0.022; OOD acc 0.854→0.690. `notes.md` §33.
- **Mikhail/mini-jev-runs** — 27.9k schema-driven decisions; one forward pass; answer from next-token logits; no token generated. Calibration / constrained-decoding gold. `notes.md` §33.
- **kokuren/jp-sns-jev7-estimator** — JP SNS seven-axis ONNX distill; teacher scores, not calibrated probabilities; `threat` F1@0.5 = 0. Domain-local categorize.
- **Archer Hume open decision-model** — **Watch.** Qwen3.8 27B dense, 265k, multimodal no audio; one forward pass locally once AR is removed. Driver: AU healthcare data-residency. No Hub weights this pass. `notes.md` §31–§33.
- **bespokelabsai/nimble** — open recipe: contrastive hard labels, not a Jev distill. Model card Apache-2.0 LoRA `bespokelabs/Bespoke-Nimble-9B` on Qwen3.5-9B (repo license absent). Their 324-row holdout is a named receipt, not a ranking. `research/notes.md` §35.
- **mmastrac/djev-spark** — DiffusionGemma 26B-A4B NVFP4, Jev-shaped decisions, images as an extension. Third compute graph. Interface claim, not a win over a decision head. `research/notes.md` §36.

### Structural prove ∩ remainder
- **thevibeworks/jevgate** — Proven / Refused / Unknown; cannot block; 0/59 unsafe unasked held-out. Allowlist ∩ System One.
- **misbahsy/doc-router** — page OCR router: 155→87 billed, 1.74× $ on 19 docs / 155 pages. Same sandwich.

### Agent harnesses extras (this hour)
- **kevinpita/pi-jev-context** — reversible Pi context sieve: hide, do not delete; `/jev off` restores. Cousin of winnow/jevprune.
- **vava-nessa/pi-jev-compaction** (and `tamaratran/fast-jev-compaction`) — verbatim drop, never summarize. Pair with jev-gate-student-b for local memory-gating.
- **reachjalil/jev-tree** — authored taxonomy so each Choice stays under 255; truncate silently drops the tail (`jev-tree-choice-cap`).
- **HacksonClark / SREGym-Lite** — Jev ranks next tests/evidence; does not diagnose; 20/50→24/50 with 2 regressions. `notes.md` §33.

### Skills & tooling
- **typesafe-ai/skills** — official skill (contracts/patterns).
- **dbreunig/building-with-jev-skill** — doc-grounded question design + symptom→cause→fix diagnosis table (distilled into our `question-design.md`).
- **ax-llm/ax** — native `typesafe` provider; **typesafeainate/dspy-typesafeify** — DSPy decorator PoC.
- **riff (scale-venture-partners)** — hybrid static+semantic linter with ruff-style JEV codes and per-finding calibrated p; 14 calls ≈ $0.0004.
- **huntedman/JevLint** — file-level convention Nouls (magic-strings, descriptive-names); write→check→fix; no line-level/auto-fix. Sibling of jev-pref. Independent. Pointer: `notes.md` §26.
- **super-jev / probably / jev-search** above — see their cards in `archive/findings.md`.

### Mixed architecture (2026-09-18T14 discourse + topic:jev)

Default placement, not a new product class: Jev judges, an LLM writes, code
owns control. Movers that sharpened the card: `git-jev-stage` (exact hunk
Choice), `jevprune` (per-line relevance with an always-keep set),
`llama-index-jev` (rerank fails open / select fails closed), `jev-pref`
(AGENTS.md as criteria), `lizard-agent` (no LLM when nothing needs writing),
`jevql` (judgment as SQL `WHERE`), OpenSmoke (Jev over every step, LLM only
on flags). Neighbor skills `tenbin` and `decision-first` are *not* Augustus
clones — they own lint/eval and try-Jev-first habit.

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
