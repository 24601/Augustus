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

Jev-class: Jev, kev, Laya, OpenJev. Call and act, or place the judgment.

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
- `research/notes.md`: living hourly catalog (dense)
- `research/README.md`: evidence archive index (sources, refresh log, hourly dumps)
- `research/changelog-hourly.md`: hourly uniqueness dumps after v0.3.0
- User-provided 0915 uniqueness lock: TianyuCodings/NanoJev unified-games-v1 densify; A 0.6B parallel decision model: states and questions in, complete probability distributions out. Zero output-token decoding.; One model, four games; ViZDoom Basic 128/128 vs Jev 56/128; Predict Position 27/128 vs Jev 11/128; Maze 225 attempts vs Jev 2738; Snake 30 food / 256 steps; held-out Maze 4/10 Snake 8/8 Basic 128/128 Predict 27/128; Untuned Qwen3-0.6B baseline; 18,760 questions per variant; 16,333 ViZDoom; 896 Predict Position expert episodes; hard_lr1e5; mix weights 1/3, 1/3, 1/6, 1/6; Hub C-Tianyu/NanoJev revision unified-games-v1 likes 57; dataset C-Tianyu/NanoJev-Data likes 5; HEAD 618cea6d906d54e128360786d12f703fff2b1245; 1284★ / 158 forks / size 64035; README SHA 4190093c64ee75b26e9726daa3b00cbcf6d3157a; MIT; caijinchun/nanojev-arena ≠ liao96312/jev-arena-nanojev ≠ zwliJay/jev-forge ≠ NanoJev; not TypeSafe Jev; open replica / specialist gameplay S1; soft scores ≠ hard gates; Game success ≠ calibrated Noul; local type boolean ≠ TypeSafe noul; invented_signal false; do not reopen or amend PR #31/#32/#33/#35; notes.md §115
- Hourly 0743 uniqueness lock: Heman10x-NGU/Verdict-open-jev ≠ Heman10x-NGU/openJev-verdict-2.0; TF-IDF + LogReg ECE 0.0207 vs Jev 0.1440; Verdict-open-jev 48.07% vs Jev 90.80%; abstention combined recall 10.00%; p50 35.58 ms; K=25 (maximum capacity) 72.00%; 0.85 coverage 84.60% selective risk 1.18%; 26.1× faster than standard Qwen JSON generation; Jevify 90.0% / 167 ms CUDA graphs disabled; Finding 1: Brier on stated confidence alone is a trap; grpo_rlcr 0.78 / ECE 0.084; reliability 0.007 but resolution 0.000; 27 900 schema-driven decisions; 13 600 / 13 600 questions; candidate mass min 0.99999624; 22 configs · 166,054 rows · 4 calibration-gold; sha a39eba3f; Student B MAE 0.148 / Pearson 0.836 / 86.0%; pngwn/open-jev-laya-bench README 404; sha 9f69c742 likes 2; HDFS 0.9933 (745/750) / retain 0.0084; BGL ERROR/FATAL protection 1.0000; 2,479 / 2,500 HDFS uncertain; cache hit 0.9648 (2412/2500); $0.153936 estimated; E2 recomputes from saved probabilities; Space sha eda59e0a; MASSIVE English 0.783 / Khmer 0.033 / Hindi 0.133; 40–48 rows too small to ship T; T never changes argmax; siren2345/jev-single-decode-transformers ≠ siren2345/jev-single-decode; Split Transformers experiment from llama.cpp runtime; tanayvasishtha/jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab ≠ yibie/laya-jev-lab; Four experiments stress-testing TypeSafe's Jev: calibration, bundle bias, label bias, and ensembling; second pass must be $0.00 from cache; The pages never call Jev; Gemma 4 31B 77.0% / Jev 1.13.0 61.4% / Laya 322M 0.0%; restriction state 95.0% against 84.4%; None of the systems are particularly good at knowing when to stop and ask; They skip the question and call a tool directly; 100% schema pass; six-field joint 48.8% vs 72.8%; ywchiu/jev_benchmark ≠ Running-Dolphins/jev-bench ≠ Praveenrajus/jev-bench; ACT / REVIEW / FALLBACK; A provider failure, timeout, malformed output, or missing answer is **not** a policy outcome; confidence is descriptive provider output, not a substitute for probability; Quality denominators include only valid scored answers; an exact halfway tie chooses the lower level; aiwithenoch/Jev-Skill ≠ simplosophy/jev-skill ≠ laguagu/jev-skills; The local path does not claim to turn a smaller checkpoint into Jev; Low support becomes decision: "review"; MIT-0 SPDX NOASSERTION; current-llm; 结构兼容，不是 Jev 模型能力; altryne/jevify ≠ Mintzs/jevify ≠ gulagala001/jevify ≠ uspraveen/Jevify; Find where Jev belongs. Design the questions. Measure the difference; TypeAR-AI/TypeAR 301 → TypeLLM/TypeLLM; TypeLLM/TypeLLM 16★; SemIf 2241★ (+34 vs §111 2207); jevlike 1051★ (+8 vs 1043); AnotiaWang 98★ (+1 vs 97); yibie/awesome-jev 525★ (+19 vs 506); Laya likes 864 (was 822); tracker likes 67 (+3 vs 64); lastModified UNCHANGED `2026-09-20T04:29:16.000Z`; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#32/#33; notes.md §113
- Hourly 0843 uniqueness lock: A hunch is a probability with a policy attached; { enter: 0.8, exit: 0.6 } is hysteresis; replay a policy change without inference; Decision models are providers, not the product; huncho ≠ Kungie/gut ≠ carldaws/hunch ≠ tpellet/hunch; pretrained Qwen2.5 base ECE 0.030 (0.5B) / 0.040 (7B); instruct 0.302 / 0.269; 70.9% → 70.0% mean conf 74.1% → 96.7%; temperature scaling still matches it in-distribution; No Jev API was called; Qwen2.5 ≠ Archer; Qwen/Qwen3.8-27B ≠ Archer; 学習済みモデル v0.1 は準備中です; bool AUROC 0.523; 先頭だと0件、末尾だと250件; 温度を渡さない場合、確率は較正されていません; このリポジトリには Jev を呼ぶコードが存在しません; g0runmezadam/what-is-jev IS tunahansahin897/what-is-jev (same GitHub id 1378007307); 947 repos scored; A 273 · B 302 · C 372; LLM rubric ≠ benches; Data as of 2026-09-20; HEAD 895b9498; README SHA 3ae98c56; 13 focused checks and one mutually exclusive outcome; Probabilities are advisory, not calibrated guarantees; omni-/ask-jev ≠ pedroknigge/mcp_jev; pd.cut bins by equal width while jeval bins by quantile; ECE 0.113 and ECE 0.076; jeval drift is not implemented yet; rlaope/jeval ≠ dayhaysoos/jevals; calibration does not compose; ECE has exactly zero statistical power to detect the failure mode that kills trajectories; 25–60× headline withdrawn; P(all-correct): 0.0071 vs 0.0001; TCE / AMS; Qwen 3.8 sparring ≠ Archer; Deferred Crispification; light_cutoff_applied_to_combination 0; recorded run, kinematic animation; BANKING77 Accuracy BERT-Base 93.02 Jev 79.90; Analyse jev calibration (NLL, ECE) backlog; BERT figures are published supervised references, not zero-shot; 档位措辞效应 分数极差中位 0.50、最大 1.32; 修好后对照组是 0.01; 不是 benchmark; 概率没做 calibration; ~1,430 API calls, about $0.15; xiaohuaxi/jev-study ≠ wjdjdakf17/jev-study ≠ baekenough/jev-study; AND: product (independence assumed and recorded in the trace); chat model's stated confidence is not calibrated; circuit-vl-4b ≠ Archer; Bring your own API key; vamsikrishna2421/jev-usecases ≠ whyashthakker/awesome-jev-use-cases; catalog ≠ endorsement; SemIf 2237★ (+30 vs §111 2207); jevlike 1049★ (+6 vs 1043); TypeLLM/TypeLLM 16★; AnotiaWang 98★; yibie/awesome-jev 520★ (+14 vs 506); Laya likes 861 (was 822); tracker likes 66 (+2 vs 64) lastModified UNCHANGED; Blackwood likes 2 gated manual; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33; notes.md §114


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
[releases](https://github.com/24601/Augustus/releases). Current: **0.4.0**,
written against [`typesafe-ai/skills` v0.5.7](https://github.com/typesafe-ai/skills/tree/v0.5.7)
(`65a39f3`; live HEAD still this commit). Re-read live TypeSafe docs
before treating that pin as current API behavior.

## License

MIT. See [LICENSE](LICENSE). Security reports: [SECURITY.md](SECURITY.md).
Contributions: [CONTRIBUTING.md](CONTRIBUTING.md).
