# The judgment-model class, analyzed (Jev is exemplar)

Snapshot of **187 repositories** built on TypeSafe Jev (jev-1.13) during launch
week (Sep 15–18, 2026), all cloned and indexed with per-repo evidence, plus
class-level neighbors (open heads, GLiClass-adjacent, listwise rankers,
vision scorers). Maintained by the Augustus skill; refreshed hourly on
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

### Agent harnesses & self-supervision
- **Kevthetech143/super-jev** — domain-independent loop: observe → questions → decide → **permit (independent of confidence)** → execute (idempotency key) → verify → JSONL replay.
- **AntonioCoppe/jev-harness** — policy + confidence gate + shadow mode + offline eval CLI; 24-row filter 48.9s (Claude CLI) vs 1.3s Jev.
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

### Skills & tooling
- **typesafe-ai/skills** — official skill (contracts/patterns).
- **dbreunig/building-with-jev-skill** — doc-grounded question design + symptom→cause→fix diagnosis table (distilled into our `question-design.md`).
- **ax-llm/ax** — native `typesafe` provider; **typesafeainate/dspy-typesafeify** — DSPy decorator PoC.
- **riff (scale-venture-partners)** — hybrid static+semantic linter with ruff-style JEV codes and per-finding calibrated p; 14 calls ≈ $0.0004.
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
Hypothesis cards: `references/mappings.md` §6–§16.

## The skill that owns this analysis

[GitHub](https://github.com/24601/Augustus) — `SKILL.md` + reference cards
covering mental models across domains (not SWE-only), the judgment-model
class (Jev exemplar, not monopoly), mixed architecture, formal/semi-formal
placement, applied placements, method substitution, composition algebra,
question-design, validation, and optimizer coupling.
