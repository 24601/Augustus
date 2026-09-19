# Augustus

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/github/v/release/24601/Augustus)](https://github.com/24601/Augustus/releases)
[![Claude Code](https://img.shields.io/badge/Claude_Code-marketplace-purple.svg)](.claude-plugin/marketplace.json)
[![Skills.sh](https://img.shields.io/badge/skills.sh-compatible-green.svg)](https://www.skills.sh/)

**Augustus** — named for Augustus De Morgan (1806–1871), mentor and professor
of William Stanley Jevons — is an agent skill for **placing typed
probabilistic judgment** (the Jev-class of System One models) using
mathematical, logical, and algorithmic mental models. It applies across
**AI, software, business, knowledge work, and life** — not only SWE.
[TypeSafe](https://docs.typesafe.ai/) Jev is the documented exemplar
(Choice, Score, Noul), not the monopoly. Formal methods are one pillar.
Exact work stays in code or policy; the model owns narrow judgment;
never launder a Noul as a proof.

> Companion, not replacement, to the official
> [`typesafe-ai` skill](https://github.com/typesafe-ai/skills). That skill
> owns Jev integration contracts; Augustus owns the **design judgment**:
> which *pillar*, *family*, and classical method map, what the objective
> implies for fail-open vs fail-closed, and what experiment would prove a
> design wrong. Not a TypeSafe-only how-to.

## The skill

- `.agents/skills/augustus/SKILL.md` — working protocol + decision-design card
- `.agents/skills/augustus/references/mental-models.md` — cross-domain
  frames (EU, abstention, VOI, MCDA, SDT, search/control, Leveson,
  NATM/snap-fit/Norman); not SWE-only. Extractable-from-state boundary
  map (self-contained vs needs outside knowledge)
- `.agents/skills/augustus/references/judgment-class.md` — the class (Jev
  exemplar, not monopoly): open heads (Laya, kev, encoder DeBERTa, LoRA
  distill, domain specialist on independent gold), constrained-AR (TypeAR, pcdServer), announced decision-model (Watch),
  open multimodal RLCD (blackwood-rlcd; not Archer), Laya ONNX port,
  contract-compatible local `/v1/systemone` (stub until hf scorer; also kev pointer / von tiny SAN — not replicas; **jevify** CUDA/PyTorch packed-logprob cousin — uncalibrated likelihoods ≠ Noul; **jeff** GLiFormer-400M encoder drop-in — not a Jev replica; **sysone** loopback gateway routes hosted + local, not a model),
  GLiNER/GLiClass species (locate vs categorize vs local multi-head;
  GLiNER2.5 extractive compaction as a named job, not a new species;
  GLiNER code-graph indexer + escalate-S2, 10–50× unfilled;
  GLiNER2 observe→score-among-candidates computer-use as a *different*
  named job, not GLiNER2.5),
  **OpenJev** local `/v1/decide` (not TypeSafe drop-in; distinct from
  hraness/sysone OpenJev runners), **semif-serve** SemIf `/v1/systemone`
  runoff (wire-compat ≠ replica),
  listwise vs decision objectives, vision scoring, when-to-use axes
  (including decision-model vs constrained LLM),
  agent-architecture portents
- `.agents/skills/augustus/references/formal-methods.md` — judgment vs
  proof ownership; Alloy Analyzer vs Apalache (finder ≠ BMC ≠
  inductiveness); TLA+/Quint/P/NuSMV/PRISM/Event-B/mCRL2/KeYmaera;
  Dafny/JML/Frama-C/SPARK/ITP; DST trio (Antithesis hypervisor, Resonate
  HQ durable-async Lean+oracle+SDK, PufferLib env+seed); TOCTOU-of-Noul,
  soundness theater, AI×FM harms (Hillel, Cauli); NATM/snap-fit/Norman/
  Leveson/Kent/Shirky
- `.agents/skills/augustus/references/formal-semi-formal.md` — one-screen
  alias of the FM pillar
- `.agents/skills/augustus/references/mixed-architecture.md` — default
  placement: judgment-class model + LLM + code; preference lint; provider
  (Jev default / other family with self-eval); dual-process S1 decide / S2
  generate; component node; DOM-as-text + fan-out; shadow-mode compaction rollout;
  fail-open wake vs fail-closed merge-gate; Harbor on/off routing;
  hybrid local decide + remote fill; `DONE` ≠ verified success;
  evidence-preserving stdout prune (hard envelope then Noul);
  specialist S1 computer-use (Cua-S1 form-v0; plan ≠ execute; not TypeSafe Jev);
  judgment as a language primitive (hunch); decision-native RAG
  (retrieve wide → decide → evidence set); classify-first MCP
  (jev-sift); draft-gate heartbeat; living class-pattern atlas;
  public judgment wall; PR attention ≠ correctness; session-sticky
  first-prompt route; capability kernel (secrets never in agent;
  Jev SENSOR); typed control plane around DSPy; engine owns truth /
  Jev owns judgment; human-confirmed kill; decide→policy→LLM leftover
  cascade; wire-compat encoder backend; loopback gateway;
  closed-vote computer-use (no planner LLM); host-owned handlers ×
  System One; active-learning triage (do not distill Jev as teacher);
  evidence-packet explorer; meaning-grep AND/OR/NOT; OMP prompt
  suppression (permission vs probability; operator owns the bar);
  judgment ≠ permission (skill-broker outline, not a recipe);
  constrained optimizer + S1 features (slo-router; never sole
  hot-path gate); effect-based shell gate (privilege ≠ verdict);
  attention filter / VOI (jev-lens; never blocks; never green unless sure);
  measurement owns endorsement (jev-packs evidence-gated + jevassert record/replay CI);
  Jev supplies evidence / code owns authority (actiongate-jev);
  ranking ≠ calibration (never hard-threshold raw p as frequency);
  hot-click CU (ego-jev; indexed table; S1 on click path);
  Jev judges relevance / code decides structure (jev-compactor);
  local rules first / never auto-train on own hides (x-reply-filter);
  control-plane combinators (not chat turns); skill VOI / abstention
  (skillranker hook fail-open); receipts not leaderboard (atlas);
  OOD / AUC ≠ ECE (sign flips by type); thinking-budget bake-off
  (frontier-100); turnstile evidence≠authority + replay; MLX
  one-pass replica economics (jevmlx; softmax ≠ Noul);
  never confidently wrong / TLA+ compose (jev-labs);
  no seal no advance / coverage ledger (seal; mint ≠ product
  brain); sureness bands (how-sure-is-jev; max_prob is generous);
  JevBench Harbor practice (calibration not in Main Score);
  CI typed gate before expensive review (ci-gatekeeper);
  Codex MCP host adapter (jev-in-codex);
  judgment as attention redirect (jev-preflight; not a merge blocker);
  compress-before-first-send (dizk/jev-lens; 79% fewer tokens);
  tools≠use / SessionStart over hoping (carryforward 0/4);
  observational memory (pi-om keep/kind verbatim);
  open-Jev class (openvons; JevPick; wire-compat ≠ replica);
  physical-world S1 (HA-Jev; not for locks);
  judgment outside the store (jevql CLI);
  landed-script trust / headless≠auto-approve (construct);
  digital-design combinators (jev-combinators rename + extended five);
  VOI cache admission (jevcache 0 FP/100);
  worth-your-attention VOI (ThinkyMiner/Winnow ≠ kevinpita/winnow);
  Jev WHETHER / Python HOW / LLM WHAT (hermes-jev-router);
  typed escalate/continue/abort baton (jev-handoff; gate never grants);
  Playwright executes, Jev chooses (browser-jev);
  OpenJev `/v1/decide` ≠ drop-in + SemIf runoff wire;
  conflict ≠ ignorance (named Choice escape);
  decision-as-memory flywheel (DGUI_HYPERMEM-JEV);
  record/replay CI (jevassert LANDED);
  measurement owns endorsement now has a runner (jev-packs
  2,990-case matrix; calibration+cost first-class);
  failure-finding arena (jevarena ≠ jev-arena);
  BBQ stereotype/uncertainty/cost (not a bias cert);
  decider≠executor (jeffrey; pick ≠ fill);
  sentence-as-rule lint (mizchi/jevlint ≠ huntedman/JevLint);
  VOI hunk prune (prune-review ~20% cost target);
  whole-repo intent VERIFIED/VIOLATION/UNKNOWN;
  GLiNER2 System One spec ≠ replica;
  open replica substrates (grande / laya-jolt / JEV-CPU /
  local-jev measured not equivalent);
  persist constraints across compaction (pi-heed);
  Harbor SGR-judge contract (jev-judge-bench; canaries ≠ quality;
  no headline yet; ≠ jevarena/jevbench);
  hand no-text steps (jev-use; Vercel drops confidence);
  Pi System-One control plane (pi-jev-control; GUI never force-click);
  never free-generates (jev-gpt tree of Choices);
  OpenRouter recipe atlas (jev-cookbook; samples not benches);
  personal-history feed (jevfeed; no social graph);
  competing NAR claim-audit (openJev-verdict-2.0; PR #1; ≠ OpenJev);
  empty compaction-proxy skip (IPECTER);
  1-token logprob endpoint ≠ Noul (chakuho; coverage ≠ correctness);
  open replica engine (jevinf; argmax-parity ≠ ECE);
  unofficial Elixir SDK ≠ OTP peer;
  jevex n=16 files-to-read VOI;
  commit pre-review attention≠verdict (middle band);
  Hermes plugin is Agnes not TypeSafe;
  pi-jev-compact ≠ pi-jev-compaction;
  decision-native inbox (mailordinal);
  unofficial jev-cli not ready (≠ jevql);
  laya-multilingual English checkpoint confident-wrong OOD;
  schema-scorer peaked ranking ≠ calibration;
  productized System One HTTP (classifier.dev; label+confidence; batch ~1000);
  escalate-under-threshold (smart single-label <0.7; multi-label ignores);
  silent FALLBACK (granite 0.546 vs advertised 0.800; rh-guard owns the gate)
- `.agents/skills/augustus/references/applied-mappings.md` — context sieve,
  exact-text keep/drop (extractive / pointer-not-generator; char-offset compaction; observed a11y/DOM controls; Bash stdout prune; verbatim session ledger / carryforward 0/4 tools≠use; classify-first MCP / jev-sift; Stagehand extract pick-and-copy; jevcumber meaning-as-spec; closed-vote JevOnly; host-owned waymode; jev-compactor framework-agnostic compact+gate 73% product-arm; dizk/jev-lens pre-send views; pi-om observational keep/kind), env triage (OpenSmoke + latch merge-gate; ci-gatekeeper pre-review typed gate; jev-preflight Stop-hook attention redirect, not a merge blocker), moderation/ranking (decision-native RAG evidence set; living class-pattern atlas; meaning-search without embeddings / jevgrep; meaning-grep jev-semgrep; evidence-packet jevex; measured RAG rerank vs generative rerank; sift ~$0.00003/post; ThinkyMiner/Winnow worth-your-attention VOI ≠ kevinpita/winnow), skill routing (route ≠ memory; session-sticky first-prompt lock; OMP/pi fail-open jev_route; OMP prompt suppression / omp-greenlight; skill-broker outline — Jev never grants access; slo-router constrained optimizer + S1 features; skillranker VOI / hook fail-open; jev-in-codex Codex MCP adapter; pi-jev-skill-bench Harbor roster-size harness; pi-jev-skill-suggestion strip-roster), capability kernel / human-confirmed gate (interlock vs toolgate; port-cleanup; permission vs probability; construct-auto-classifier privilege ≠ verdict + landed-script / headless≠auto-approve; actiongate-jev — Jev supplies evidence, code owns authority; turnstile — policy first, replay; seal — no seal no advance / coverage ledger; jev-labs — never confidently wrong; jev-handoff typed baton — gate never grants), decide→policy→LLM leftover cascade (jav-email-cascade), closed-vote computer-use (applied-mappings §9; ego-jev hot-click cousin; browser-jev Playwright executes Jev chooses; jeffrey decider≠executor; jev-use hand no-text steps; jev-gpt never free-generates), VOI hunk prune / whole-repo intent (prune-review / jev-intent-review), persist constraints (pi-heed; Jev never writes policy), Pi control plane (pi-jev-control), personal-history ranking (jevfeed; ≠ Winnow), OpenRouter recipe atlas (jev-cookbook), empty compaction-proxy skip (IPECTER), Pi verbatim summarizer replacement (pi-jev-compact ≠ pi-jev-compaction), decision-native inbox (mailordinal), commit pre-review (commitjev), jevex n=16 files-to-read, productized classification API (classifier.dev; spam/inbox/feedback)
- `.agents/skills/augustus/references/faq.md` — "just classification",
  stack replacement, Jev vs open head vs encoder vs LoRA vs constrained AR vs kev vs blackwood,
  wait-for-Archer, missing-other confident-wrong, soft project rules vs linter (Abide), extractive/pointer-not-generator, compaction summarize vs pointer, encoder vs Jev compaction, fail-closed keep_full, shadow-mode rollout, fail-open vs fail-closed wake vs CI gate, observe→score→act backend-agnostic, hybrid local decide + remote fill, DONE ≠ verified success, stdout prune vs session compaction, Cua-S1 vs TypeSafe Jev, plan ≠ execute / dry-run, local drop-in vs stub scorer, route ≠ memory, when-it-holds / extractable-from-state, decision-model vs constrained LLM, dual-process S1/S2, combinatorial grid ≠ extractive, GLiNER vs GLiClass vs CLIP, LLM-as-judge, in-engine vs CLI store,
  hard envelope (bitrate / planner), not-another-how-to,
  uncalibrated local likelihoods ≠ Noul, decision-native RAG, classify-first MCP, living applied-mappings atlas / class patterns, draft-gate silence ≠ safer, robotics text-state vs pixels, Stagehand extract pick-and-copy / fast-path not replacement, public judgment wall / six parallel questions, meaning-search without embeddings, attention≠correctness PR review, skills→oxlint not a hard gate, session-sticky fail-closed routing, measured RAG rerank vs generative rerank, cascade
  sign-flip / calibration theater, Precision PDF honest negative,
  type-safe ≠ correct / Jev is SENSOR not policy, Ax/DSPy knobs vs
  typed control plane, native vs verbalized confidence, engine owns
  truth / Jev owns judgment, train specialist vs few-shot hosted,
  Noul 0.5 cannot-tell never rounded, calibration ≠ sortable,
  local `/v1/systemone` ≠ Jev (GLiFormer / gateway),
  do not distill Jev as teacher of record, PCD O(1) ≠ calibrated Noul,
  closed-vote CU vs Stagehand pick, OMP/pi fail-open vs pi-jev-approver,
  permission vs probability / operator owns the safety bar, judgment ≠
  permission / Jev never grants access, eval integrity / instrument not
  score, Jev not sole hot-path gate / constrained optimizer + S1 features,
  privilege ≠ verdict / effect contracts, attention filter not permission,
  measurement owns endorsement / evidence-gated packs, Jev supplies
  evidence / code owns authority, ranking ≠ calibration / never
  hard-threshold raw p as frequency, Jev `done` ≠ browser success,
  never auto-train on the model's own hides, pointer compact ≠
  LLM summarize, combinators not a new model, AUC ≠ ECE / sign
  by type, thinking-budget bake-off, local MLX one-pass ≠ Noul, never confidently wrong / TLA+ compose, no seal no advance, sureness vs max_prob, JevBench calibration not in Main Score, CI typed gate before expensive review, Codex MCP adapter, two jev-lens products, Stop-hook not merge blocker, tools≠use, openvons not TypeSafe, Noul not for locks/heaters, two Winnow products, OpenJev `/v1/decide` not drop-in, SemIf runoff ≠ replica, combinators rename + extended five, Noul conflict≠ignorance, jevcache fail-open, typed baton never grants, jevassert record/replay CI, jevarena≠jev-arena, BBQ not a bias cert, jeffrey pick≠fill, jevlint≠JevLint, local-jev not equivalent, constraints survive compaction (pi-heed), jev-judge-bench≠jevarena≠jevbench (no quality headline yet), jev-use≠ultrafast / Vercel drops confidence, pi-jev-control GUI never force-click, jev-gpt never generates, cookbook samples not benches, jevfeed no social graph, openJev-verdict claims ≠ OpenJev / not endorsement, 1-token logprob ≠ Noul / coverage ≠ correctness, jevinf replica ≠ TypeSafe, elixir-sdk ≠ dannote/jev, jevex n=16 rename, commitjev middle band, hermes-plugin-jev is Agnes, pi-jev-compact ≠ pi-jev-compaction, IPECTER runway empty, mailordinal inbox, jev-cli not ready ≠ jevql, laya-multilingual confident-wrong OOD, schema-scorer peaked ranking, HF 401 / GitHub 404 Hub-only, classifier.dev productized HTTP / escalate-under-threshold / silent FALLBACK / vs_jev tracked JSON

- `.agents/skills/augustus/references/mappings.md` — classical-method
  mappings with boundaries, counterexamples, acceptance tests (including
  Hypothesis cards §6–§19 — promote only with a test that ran)
- `.agents/skills/augustus/references/validation.md` — design gate, eval
  recipes, Jev-for-skills (routing, self-monitoring, testing, modularity,
  frontmatter), and Eval & hill-climb (jevals hygiene + Harbor taskset;
  open-jev-laya-bench as ECE/NLL/Brier bake-off exemplar; DMB as
  Harbor-style frozen protocol vs constrained LLMs; jevals-data as
  CC-BY-4.0 recompute-from-logs feedstock; Abide replay as
  Harbor-adjacent soft-rule measurement; solari-reflex Harbor-style
  computer-use; gliner2-ultrafast encoder-backend cousin (`DONE` ≠
  success; demo is not a bake-off); Cua-S1 specialist form source-only
  (metric names, no checkpoint scores; not TypeSafe Jev); Stagehand
  extract pick-and-copy 37/75 no-LLM ~0.5s vs 4.37s (*their* card;
  pick ≠ replacement; draft #2951–#2955); jevgrep 79% top-5 vs BM25
  / grep on stripped repos; Jev-RAG one-run vs Spark rerank
  (full-context Spark still faster); jev-oxlint Phoenix answer-key;
  native-probability calibration arena (jev-arena live Brier 0.0059 /
  ECE 0.0620 *theirs*); typed control-plane bake-off shape
  (jev-dspy-control-plane; offline stubs ≠ quality); jev-testbench collab arms; ARC-AGI Direct Jev as
  combinatorial-≠-extractive negative; jev-gateway-bench Harbor on/off
  routing one-run signal; jev-pruner Harbor needle/noise + Terminal-Bench
  integration pilot, not a full bench; jev-baselines-eval pre-registered
  **AMBIGUOUS** + cascade sign-flip; explore-typesafe-ai synthetic FHIR
  Harbor-shaped, not clinically validated; databricks-jev-pdf-lab honest
  negative; Domain-jev-maker specialist vs few-shot (KL/r/McNemar);
  jav-email-cascade compare arms; jev-orderby-bench ORDER BY gates
  (calibration ≠ sortable); jeff GLiFormer cost/accuracy;
  system-one-benchmark Jev vs MLX PCD vs AR JSON n=50 (Brier 0.1096 vs
  0.3884); jevex 1/8→6/8 SWE finish n=8; jev-semgrep 0.94/0.98;
  omp-greenlight 1,013/10 default 40.9% / 0 of 94; dinostomp jev-as-if
  ECE 0.062 *theirs* / FINDINGS 189; slo-router p95 77.93→490.38 same
  routes; construct-auto-classifier Jev 0 dangerous / 975; INSTRUCT_JEV
  119-row instruct seed; jev-packs nine verified packs on pinned
  jev-1.13 + **jevassert LANDED** (2,990-case matrix; Jev/Sonnet 5
  accuracy tie, Jev better calibrated 7/9, ~250× cheaper;
  sms-spam 0.953/0.040); BBQ 58,492 / 97.28% / $0.3429 *theirs*;
  jevlint 13/15 1.00/1.00; grande JGLUE 0.614/0.853; local-jev
  done 30%/shape 57%; pi-heed 98.5%/0 false block; does-jev-confidence 8,000 judgments
  AUC ~0.91 / stated ~75% vs human ~10% / ~96% ECE removed;
  ego-jev n=3 medians ~2× vs per-step LLM; jev-compactor 64.5%/
  366ms/0 invented paths vs Sonnet summary, one session;
  jev-frontier-100 Jev 77.0% vs Qwen3.5 4B/2048 96.7%
  (exploratory); jev-ood-calibration 900 tickets ECE 0.107 =
  4.4× floor / sign flips by type; jev-labs 1,080 golden 0
  wrong under chaos (escalate; not a proof of zero);
  jevbench v1.1 Jev 1.13.0 Main 87.6 (calibration not scored);
  how-sure-is-jev Choice confidence = max_prob; ci-gatekeeper
  504–629 ms own-repo; dizk/jev-lens 79% / 500 trajectories;
  jev-compactor product-arm 73%/350ms/4 of 4; carryforward
  0/4 recall; openvons JevPick 3.2–4.8×; HA-Jev 17★ not for
  locks; jev-preflight fail-open 8 axes; jevcache 0 FP/100;
  zeroshot-vs-bert +0.05–+0.13 / DiD; ThinkyMiner/Winnow
  80%/90%; OpenJev 45/60; semif-serve 1164 vs 178 ms;
  typed-evaluation-collapse Noul vs named Choice;
  jev-judge-bench SLA-150 contract / canaries ≠ quality / no headline
  yet; jev-use 220 ms p50 / 12/12 / Vercel 0.4 *theirs*; jev-cookbook
  425/$0.015 samples not benches; openJev-verdict-2.0 77.10%/0.0636/
  0.0144 *theirs* unverified + PR #1 claim-audit;
  chakuho GUI 336 27B 95%/92% vs Jev 89%/82% *theirs*;
  jevinf 2.57×/2.27× 100% argmax; jevex n=16 160s→69s /
  $8.74→$3.13; commitjev 0 false on 5 clean *theirs*;
  laya-multilingual MASSIVE 0.366/0.387 vs 0.227/0.733;
  schema-scorer v2 Choice 0.841; HF 401 this pass;
  classifier.dev 400/650 ms; F1 0.887 / 230 ms vs 0.799;
  AG News 87.7%; granite 0.546 vs advertised 0.800 *theirs*)
- `.agents/skills/augustus/references/boundary-audit.md` — existing-system
  insertion: fit test, opportunity map, smallest boundary, red flags
- `.agents/skills/augustus/scripts/evaluate_decisions.py` — offline evaluator
  for selective binary decisions (Brier, reliability, threshold/cost sweep)

Plus `research/` — the living evidence archive behind the skill, refreshed
hourly (see `research/README.md`).

## Install

**Claude Code** (plugin marketplace, mirrors the official TypeSafe layout):

```bash
claude plugin marketplace add 24601/Augustus
claude plugin install augustus@augustus
```

**Any skills-compatible agent** (Amp, Codex, Cursor, …):

```bash
npx skills add 24601/Augustus --skill augustus
```

**ChatGPT**: skills are not a native ChatGPT primitive — paste
`.agents/skills/augustus/SKILL.md` plus the `references/` files into a
GPT's instructions or a Project's knowledge and it will follow the protocol.

**Amp**: repo-local `.agents/skills/` are discovered automatically.

## GitHub topics

`jev` `typesafe` `typesafe-ai` `system-one` `system-one-models`
`structured-output` `calibrated-confidence` `ai-agents` `agent-skills`
`decision-systems` `reranking` `beam-search` `claude-code` `python` `llm`
`decision-theory` `semantic-search` `agent-workflows` `mixed-architecture`
`tool-routing` `skill-routing` `semantic-lint` `classification` `gliclass`
`listwise-ranking` `vision-scoring` `open-weights` `formal-methods`
`model-checking` `deterministic-simulation` `decision-theory`
`value-of-information` `signal-detection` `mcda` `calibration`
`alloy` `apalache` `pufferlib` `stamp-stpa`

## Versioning

See [CHANGELOG.md](CHANGELOG.md) and
[releases](https://github.com/24601/Augustus/releases). Current: **0.3.0**,
written against [`typesafe-ai/skills` v0.5.7](https://github.com/typesafe-ai/skills/tree/v0.5.7)
(`65a39f3`). Re-read live TypeSafe docs before treating that pin as current
API behavior.

## License

MIT — see [LICENSE](LICENSE).
