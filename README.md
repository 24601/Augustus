# Augustus

Place typed probabilistic judgment (Jev-class System One / decision
models) using classical mental models. Jev is the exemplar, not the monopoly.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/24601/Augustus)](https://github.com/24601/Augustus/releases)
[![Pages](https://img.shields.io/badge/docs-24601.github.io-blue.svg)](https://24601.github.io/Augustus/)
[![Claude Code](https://img.shields.io/badge/Claude_Code-marketplace-purple.svg)](.claude-plugin/marketplace.json)
[![Skills.sh](https://img.shields.io/badge/skills.sh-compatible-green.svg)](https://www.skills.sh/)

**Homepage:** [24601.github.io/Augustus](https://24601.github.io/Augustus/)

Agent skill for placing TypeSafe Jev Choice/Score/Noul with classical
decision methods, composition algebra, and a validation gate.

**Augustus**, named for Augustus De Morgan (1806–1871), mentor and professor
of William Stanley Jevons, is the design-judgment skill for **where** typed
probabilistic judgment belongs (the Jev-class of System One models), using
mathematical, logical, and algorithmic mental models. It applies across
**AI, software, business, knowledge work, and life**, not only SWE.
[TypeSafe](https://docs.typesafe.ai/) Jev is the documented exemplar
(Choice, Score, Noul), not the monopoly. Formal methods are one pillar.
Exact work stays in code or policy; the model owns narrow judgment;
never launder a Noul as a proof.

> **Not a TypeSafe product.** Companion, not replacement, to the official
> [`typesafe-ai` skill](https://github.com/typesafe-ai/skills). That skill
> owns Jev integration contracts; Augustus owns the **design judgment**:
> which *pillar*, *family*, and classical method map, what the objective
> implies for fail-open vs fail-closed, and what experiment would prove a
> design wrong. Not a TypeSafe-only how-to. Integrity / reward-hack
> companion: [`rh-guard`](https://github.com/24601/rh-guard).

![Jev-class models with vs without Augustus. Without: call the model, act on the score, then quiet failure modes (soft Noul treated as hard gate, GPT bakeoff framing, no falsifier, polarity unchosen). With Augustus: state, pillar and family map, question design, fail-open vs fail-closed, typed Choice Score Noul, code owns effects, named falsifying experiment.](docs/assets/with-without-augustus.svg)

Jev-class: Jev, kev, Laya, OpenJev, GLiNER, SemIf, NanoJev, Jeff-1, localjev.
Call and act, or place the judgment. Same split for any typed probabilistic
judgment tool, not Jev-only.

## Recipes

Class-wide, not a TypeSafe how-to. Full cards:
[`docs/release-notes-v0.5.0.md`](docs/release-notes-v0.5.0.md) ·
[Pages recipes](https://24601.github.io/Augustus/#recipes).

- **Encoder (GLiNER / GLiClass).** Without: treat locate/categorize as a decision head and hard-gate spans. With: species map; remainder after extractive spans. Measure span quality separately from ECE.
- **Open heads (Laya, SemIf, kev, Jeff-1).** Without: wire-compat or argmax agree as replica. With: softmax ≠ calibrated Noul; systems timing ≠ semantic equivalence. Measure ECE/Brier on held-out, not only speed.
- **NanoJev.** Without: game wins as calibration. With: specialist gameplay S1; local boolean ≠ TypeSafe noul. Measure held-out game separately from ECE.
- **llm-to-jev.** Without: ship converted prompts as equivalent behavior. With: heuristic on-ramp; review the Score rubric. heuristic conversion ≠ calibrated Noul.
- **jcr.** Without: run what the tree found. With: lookup returns context; **does not execute**. Routing ≠ permission; docs ≠ authority to run.
- **localjev / prompted JSON.** Without: parse generated JSON as a Noul. With: schema-valid ≠ picked-right.

## The skill

One line per file. The living catalog is in the reference cards and
[`research/notes.md`](research/notes.md), not this README.

- `.agents/skills/augustus/SKILL.md`: working protocol and decision-design card
- `.agents/skills/augustus/references/mental-models.md`: cross-domain frames (EU, VOI, MCDA, SDT, ...); not SWE-only
- `.agents/skills/augustus/references/judgment-class.md`: the class (Jev exemplar, not monopoly) and peer families
- `.agents/skills/augustus/references/formal-methods.md`: judgment vs proof; soundness theater; DST trio
- `.agents/skills/augustus/references/formal-semi-formal.md`: one-screen alias of the formal-methods pillar
- `.agents/skills/augustus/references/mixed-architecture.md`: where S1 judgment sits next to LLM + code
- `.agents/skills/augustus/references/composition-algebra.md`: positions a typed judgment can occupy relative to any method
- `.agents/skills/augustus/references/applied-mappings.md`: sieves, keep/drop, triage, rank, and route placements
- `.agents/skills/augustus/references/faq.md`: design-judgment FAQ (not an API how-to)
- `.agents/skills/augustus/references/mappings.md`: classical-method mappings with boundaries and tests
- `.agents/skills/augustus/references/methods-catalog.md`: named algorithms → judgment-shaped substitution
- `.agents/skills/augustus/references/toolbox-mapping.md`: how to find a substitution in a method you already trust
- `.agents/skills/augustus/references/question-design.md`: writing and diagnosing well-formed questions
- `.agents/skills/augustus/references/validation.md`: design gate, eval recipes, Harbor/jevals practice
- `.agents/skills/augustus/references/boundary-audit.md`: existing-system insertion: smallest boundary, red flags
- `.agents/skills/augustus/references/optimizer-integration.md`: Jev inside Ax/DSPy optimizer loops
- `.agents/skills/augustus/references/agent-self-assessment.md`: agent self-supervision gates (pre-action, done, stuck)
- `.agents/skills/augustus/scripts/evaluate_decisions.py`: offline Brier / reliability / cost-threshold evaluator
- `research/notes.md`: living hourly catalog (dense); §118 llm-to-jev conversion assistant (heuristic on-ramp, not a replica)
- `research/README.md`: evidence archive index (sources, refresh log, hourly dumps)
- `research/changelog-hourly.md`: hourly uniqueness dumps after v0.3.0
- Hourly 0743 uniqueness dump: [`research/changelog-hourly.md`](research/changelog-hourly.md) (`notes.md` §113 / batch #96).
- Hourly 0843 uniqueness lock: A hunch is a probability with a policy attached; { enter: 0.8, exit: 0.6 } is hysteresis; replay a policy change without inference; Decision models are providers, not the product; huncho ≠ Kungie/gut ≠ carldaws/hunch ≠ tpellet/hunch; pretrained Qwen2.5 base ECE 0.030 (0.5B) / 0.040 (7B); instruct 0.302 / 0.269; 70.9% → 70.0% mean conf 74.1% → 96.7%; temperature scaling still matches it in-distribution; No Jev API was called; Qwen2.5 ≠ Archer; Qwen/Qwen3.8-27B ≠ Archer; 学習済みモデル v0.1 は準備中です; bool AUROC 0.523; 先頭だと0件、末尾だと250件; 温度を渡さない場合、確率は較正されていません; このリポジトリには Jev を呼ぶコードが存在しません; g0runmezadam/what-is-jev IS tunahansahin897/what-is-jev (same GitHub id 1378007307); 947 repos scored; A 273 · B 302 · C 372; LLM rubric ≠ benches; Data as of 2026-09-20; HEAD 895b9498; README SHA 3ae98c56; 13 focused checks and one mutually exclusive outcome; Probabilities are advisory, not calibrated guarantees; omni-/ask-jev ≠ pedroknigge/mcp_jev; pd.cut bins by equal width while jeval bins by quantile; ECE 0.113 and ECE 0.076; jeval drift is not implemented yet; rlaope/jeval ≠ dayhaysoos/jevals; calibration does not compose; ECE has exactly zero statistical power to detect the failure mode that kills trajectories; 25–60× headline withdrawn; P(all-correct): 0.0071 vs 0.0001; TCE / AMS; Qwen 3.8 sparring ≠ Archer; Deferred Crispification; light_cutoff_applied_to_combination 0; recorded run, kinematic animation; BANKING77 Accuracy BERT-Base 93.02 Jev 79.90; Analyse jev calibration (NLL, ECE) backlog; BERT figures are published supervised references, not zero-shot; 档位措辞效应 分数极差中位 0.50、最大 1.32; 修好后对照组是 0.01; 不是 benchmark; 概率没做 calibration; ~1,430 API calls, about $0.15; xiaohuaxi/jev-study ≠ wjdjdakf17/jev-study ≠ baekenough/jev-study; AND: product (independence assumed and recorded in the trace); chat model's stated confidence is not calibrated; circuit-vl-4b ≠ Archer; Bring your own API key; vamsikrishna2421/jev-usecases ≠ whyashthakker/awesome-jev-use-cases; catalog ≠ endorsement; SemIf 2237★ (+30 vs §111 2207); jevlike 1049★ (+6 vs 1043); TypeLLM/TypeLLM 16★; AnotiaWang 98★; yibie/awesome-jev 520★ (+14 vs 506); Laya likes 861 (was 822); tracker likes 66 (+2 vs 64) lastModified UNCHANGED; Blackwood likes 2 gated manual; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35; notes.md §114
- User-provided 0915 uniqueness lock: TianyuCodings/NanoJev unified-games-v1 densify; A 0.6B parallel decision model: states and questions in, complete probability distributions out. Zero output-token decoding.; One model, four games; ViZDoom Basic 128/128 vs Jev 56/128; Predict Position 27/128 vs Jev 11/128; Maze 225 attempts vs Jev 2738; Snake 30 food / 256 steps; held-out Maze 4/10 Snake 8/8 Basic 128/128 Predict 27/128; Untuned Qwen3-0.6B baseline; 18,760 questions per variant; 16,333 ViZDoom; 896 Predict Position expert episodes; hard_lr1e5; mix weights 1/3, 1/3, 1/6, 1/6; Hub C-Tianyu/NanoJev revision unified-games-v1 likes 58; dataset C-Tianyu/NanoJev-Data likes 5; HEAD 618cea6d906d54e128360786d12f703fff2b1245; 1289★ / 158 forks / size 64035; README SHA 4190093c64ee75b26e9726daa3b00cbcf6d3157a; MIT; caijinchun/nanojev-arena ≠ liao96312/jev-arena-nanojev ≠ zwliJay/jev-forge ≠ NanoJev; not TypeSafe Jev; open replica / specialist gameplay S1; soft scores ≠ hard gates; Game success ≠ calibrated Noul; local type boolean ≠ TypeSafe noul; invented_signal false; do not reopen or amend PR #31/#32/#33/#35; notes.md §115
- User-provided HIGH NiazMorshed2007/jcr (`research/notes.md` §116 / items 309–316 / batch #99). Capability-tree lookup; **does not execute**. Merged #35 owns §114. Merged #36 owns §115. Open #37 §117.


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

**Copy the skill path** (Cursor / Amp / any agent that reads repo-local
skills):

```bash
git clone https://github.com/24601/Augustus.git
# skill lives at .agents/skills/augustus/
```

**ChatGPT**: skills are not a native ChatGPT primitive. Paste
`.agents/skills/augustus/SKILL.md` plus the `references/` files into a
GPT's instructions or a Project's knowledge and it will follow the protocol.

**Amp**: repo-local `.agents/skills/` are discovered automatically.

## GitHub topics

`jev` `typesafe` `typesafe-ai` `system-one` `system-one-models`
`structured-output` `calibrated-confidence` `ai-agents` `agent-skills`
`decision-systems` `reranking` `beam-search` `claude-code` `python` `llm`
`decision-theory` `decision-making` `semantic-search` `agent-workflows`
`mixed-architecture` `agentic-ai` `zero-shot-classification`
`tool-routing` `skill-routing` `semantic-lint` `classification` `gliclass`
`listwise-ranking` `vision-scoring` `open-weights` `formal-methods`
`model-checking` `deterministic-simulation`
`value-of-information` `signal-detection` `mcda` `calibration`
`alloy` `apalache` `pufferlib` `stamp-stpa`

## Versioning

See [CHANGELOG.md](CHANGELOG.md) and
[releases](https://github.com/24601/Augustus/releases). Current: **0.5.0**,
written against [`typesafe-ai/skills` v0.5.7](https://github.com/typesafe-ai/skills/tree/v0.5.7)
(`65a39f3`; live HEAD still this commit). Re-read live TypeSafe docs
before treating that pin as current API behavior.

## License

MIT. See [LICENSE](LICENSE). Security reports: [SECURITY.md](SECURITY.md).
Contributions: [CONTRIBUTING.md](CONTRIBUTING.md).

User-provided 0920 jcr uniqueness lock: NiazMorshed2007/jcr MIT; site https://jcr.niazmorshed.dev; topics ai-agents,jev,mcp; **4★**; HEAD `138b3832`; README SHA `2a49dbc1`; LICENSE SHA `46231303`; size **14850**; Jev Capability Resolver; one tool to find documented deterministic commands in a nested capability tree; returns context; **does not execute**; skills = workflow+judgment; capabilities = individual operations; format independent of Jev; proposed open standard exploration; classify (Jev) → optional OpenAI decompose compound → beam search geometric mean of routing probs; keep up to 3 paths ≥60% of best (JCR_BAND_RATIO 0.6); ambiguity / no-match / depth-limit explicit; soft scores ≠ hard gates; 0.6 band is application policy; routing ≠ permission; docs ≠ authority to run; sol-vs-opus5-20 *theirs*: 20 scenarios × 4 variants = 80 runs; lookup+explain only, no execution; Claude Opus 5: agent input 108,585→15,819 (−85%), cost $0.3700→$0.1222 (−67%), wall 105.5s→77.7s; Codex GPT-5.6-Sol: 61,952→47,669 (−23%), $0.1377→$0.1151 (−16%), wall 25.3s→62.4s (Sol slower with JCR in 19/20); One Sol outlier 372.6s / 193 Jev calls; n=1 per cell; Not Harbor task-execution; Claude/Codex harnesses; compare mode; 50 scenarios bundled; 11 groups, 960 nodes, 11,360 items; 16 routing rounds per step; NiazMorshed2007/jcr ≠ skill-broker ≠ skillranker ≠ jev-sift ≠ jev-lens ≠ jevusher ≠ jev_select_capability; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34; notes.md §116
User-provided 0922 uniqueness lock: SemIf was formerly OpenJev; independent; not affiliated with Jev or TypeSafe; homepage openjev.com; default master; MIT; HEAD ca3ba65f1429; Tolerate float roundoff in MLX evidence verification; pushed 2026-09-19; live REST 2282★ / 140 forks; size 9177; README SHA 74ab7f7f; LICENSE SHA ca562883; interface pattern reproduction with open models; does not reproduce Jev undisclosed model/training; Direct option logits; 0 output tokens; shared-state parallel; MLX backend for Apple Silicon (`--backend mlx`); Qwen3.5-4B 3090 direct 1.023s vs AR JSON 5.332s (**5.21×**); argmax agree 18/21; systems comparison ≠ semantic equivalence; Parallel suffixes 20.03 dec/s on 777 decisions; Browser ladder Qwen3.5-4B authored BA 0.813, pert 0.766, TypeSafe subset agreement 0.845 vs Published Jev 0.883 (102 across 20 cases); Softmax over options ≠ calibrated Noul; typed output does not guarantee semantic correctness; wire/agreement ≠ replica of TypeSafe; SemIf ≠ kw2828/OpenJev playground ≠ zhihz/openjev ≠ apiplant/semif-rs port ≠ dddanielliu/semif-serve; rename is densify not a second census; JevBench 74.6 is §78 not this ladder; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#38; do not push onto open #39/#40; notes.md §117
User-provided 0940 uniqueness lock: Turn decision-shaped LLM prompts into proposed Jev primitives; This is a conversion assistant, not an automatic guarantee of equivalent behavior; The compiler uses deterministic heuristics, not an LLM or evaluation model; It understands a deliberately small set of common prompt patterns; Generated instructions and criteria must be reviewed before production use; Score ranges such as 0 to 1 are translated into ordered Jev criteria; Prompts requiring open-ended prose are not a fit; suitability strong/partial/not_a_fit; compatibility full/partial/none; Writing new text stays with an LLM; Review the generated Score rubric; Jev scores ordered criteria, not an arbitrary 0-to-1 range; Everything runs locally in the browser; There is no framework, database, account, API, or server-side prompt processing; The key is read from the process environment and is never stored or printed; connect-src 'none'; alexwestco/llm-to-jev ≠ altryne/jevify ≠ ryana/jevify ≠ fidecastro/jevify ≠ Mintzs/jevify ≠ gulagala001/jevify ≠ uspraveen/Jevify; HEAD 234058ab372d; README SHA 43cd94fb; LICENSE SHA 5f334006; compiler SHA fdf235d0; 2★; MIT; JavaScript; size 29; Pages https://alexwestco.github.io/llm-to-jev/; invented_signal false; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35; notes.md §118
Hourly 0947 uniqueness lock: Fast and cheap agent evals. jev as judge.; 18,041 skills from the 200 most-starred repos; Not a security scanner; 最简 Jev 调用演示器; confidence 不是正确率; q93304989-bit/jev-lab ≠ tanayvasishtha/jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab ≠ yibie/laya-jev-lab; 75% cheaper and 18% faster withdrawn; jev @0.15 100% recall 87% savings; 33Audits/jev-auto ≠ gargpratyush/jev-router; no Typesafe key, no PI_API_BASE, zero deps; tool-emitted Score/Noul ≠ calibrated Noul; semantic_compatibility: false; candidate_mass; Qwen3.5-2B ≠ Archer; Jev evaluates decisions; it cannot run a coding-agent session; Status: no model yet; S1LV3RJ1NX/openjev ≠ TheoLeeCJ/openjev; 28 accepted decisions; 3 targets; score 800; health 100; arcade game not a flight trainer; A successful live TypeSafe call has not been verified for v0.1.0; abhibansal60/tidy ≠ MANISH007700/tidy; No model, Jev included, predicted which channels its owner keeps; seed 1 selected on a held-out 400-item validation split; Brier 0.342 → 0.378; more accurate and more overconfident; Qwen3.5-4B ≠ Archer; static quants of kushalpatil/jevify-gemma4-26b-a4b; The labels were corrected, and one earlier result was retracted; zero of 23,869 eligible rows; Do not compare cost without checking task success; Exit 1 is not a proof; kisshan13/typesafe-ai-go ≠ Nibir1/typesafe-go ≠ official; 38 tests that cannot fail in a 356-model warehouse; if a parser can answer it, Jev is never asked; 359 of them; Games & Simulation 82; Education & Learning 1; Ratings are heuristics; syedabbasshaheer-art/jev-atlas ≠ ZeroX-01/jev-atlas ≠ Zaious/jev-capability-atlas ≠ gorock007/jev-atlas; anandi1989/awesome-jev-usecases ≠ whyashthakker/awesome-jev-use-cases ≠ walidboulanouar/awesome-jev-use-cases ≠ vamsikrishna2421/jev-usecases; Every headline result above is self-reported; Archer Hume 84.6% MMLU-Pro is a third-party probe not landed Archer; catalog ≠ endorsement; judge ≠ actuator; softmax over A–H ≠ Noul; SemIf 2270★; jevlike 1054★; TypeLLM/TypeLLM 16★; AnotiaWang 98★; yibie/awesome-jev 538★; Laya likes 889; tracker likes 68 lastModified UNCHANGED; Blackwood likes 2 gated manual; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#35/#36/#37/#38/#40; do not push onto open #39; notes.md §119
- Hourly 1049 HIGH (`research/notes.md` §120 / items 353–368 / batch #103). ggmlc GGUF serving / option-order / exact-p Minesweeper / adapters / catalogs. uniqueness_gate 0843+0915+jcr+0922+0940+0947+1049. Does not bump 0.5.0. Merged #41 owns §119. Merged #42 is the 0.5.0 release.
- Hourly 0947 HIGH (`research/notes.md` §119 / items 337–352 / batch #102). jev-as-judge / OneForward candidate_mass / catalogs / replay / RLCD heads. uniqueness_gate 0843+0915+jcr+0922+0940+0947. Does not bump 0.5.0. Merged #42 is the 0.5.0 release. Merged #40 owns §118. Merged #39 is §114 hygiene. Merged #37 owns §117. Merged #38 owns §116.
Hourly 1049 uniqueness lock: ggmlc GGUF is not llama.cpp; Loading them in llama.cpp will fail; one encoder pass; hf:mys/laya-GGUF sha 713ae6f6e39f likes 0 apache-2.0; hf:mys/laya-multilingual-GGUF sha 3b645ae54281; hf:mys/laya-typed-decisions-GGUF sha 1e9e8ba1f527; hf:tozp/laya-onnx sha 0862aeba1e65 Opset 14 FP32 and INT8; tozp/laya-onnx ≠ Mattepiu/laya-onnx ≠ gqgs/laya-onnx; docker-laya MIT HEAD 1b8239a51ddd README SHA 9cb7bdc3; laya.cpp RTX ggml CUDA HEAD 8590937c79a2 README SHA cdd429b9; serving substrate ≠ calibrated replica; Softmax over options ≠ calibrated Noul; Qwen3.5-4B ≠ Archer; Qwen3.5-9B ≠ Archer; jev-position-test n=6 HEAD 7a56ca1c2698 README SHA 23f194c9; jevmlx slots 5 of 6; hosted Jev 0 of 6; prior_correction made it worse; jevSweeper mean Spearman ρ −0.274; picked exact-optimal 1/25 (4%); 31 of 36 still logically decidable; 86% of the time we should not have been asking; game success ≠ calibrated Noul; LLM2Jev 64★ Apache-2.0 HEAD 924618721277 README SHA da35fe61; not affiliated with or endorsed by Jev or TypeSafe; No answer tokens are generated; OpenSourceJev llama.cpp Qwen3-1.7B HEAD 3c41fba3681d; JEV-MLX Qwen3.5-9B HEAD dec24cd929ea; decision-head-rlcd Qwen3.5-4B 4.9M LoRA; AUTO_ACT is not a Noul; closed-set fail-open stdlib-only; verified=False; soft scores ≠ hard gates; 22 to 40% cheaper *theirs*; first version 70% more expensive; 111-case benchmark *theirs*; CDC 5,000 Jev 72.2% AUC 0.7725 *theirs*; accuracy is a trap; 9.0% base rate always-no 91.0%; catalog ≠ endorsement; jev-skill 109★ 90 scenarios HEAD 4f6e899a24d4; awesome-jev-live 673 entries 4★; minecraft-agent 214★ 131 JEV decisions 35 Astra calls; nether-final-08 8 minutes 43.300 seconds; planner writes JEV selects; RoboJEV structured simulator state not images; ashare-trader 策略未通过自己的回测门槛; 36 组参数全部净期望为负; no positive expectation under real costs; typed_evals NOT an official TypeSafe AI product; jev-as-judge is a sensor; third-person-audit 40% & 60% watermarks still soft; The included experience uses a handwritten demo provider; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42; notes.md §120
