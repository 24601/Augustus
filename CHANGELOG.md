# Changelog

All notable changes to Augustus are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versioning
follows [SemVer](https://semver.org/spec/v2.0.0.html).

Each release notes the [`typesafe-ai/skills`](https://github.com/typesafe-ai/skills)
revision it was written against. That skill owns integration contracts;
Augustus owns design judgment. Re-read live TypeSafe docs before treating a
pin as current API behavior.

## [0.3.0] - 2026-09-18

Pegged against [`typesafe-ai/skills` v0.5.7](https://github.com/typesafe-ai/skills/tree/v0.5.7)
(`65a39f3`, 2026-09-12).

### Added

- Hourly 0743 HIGH (`research/notes.md` §113): **Skip
  Archer rewrite.** Docs-only on a **fresh PR off main**.
  **HARD RULE:** do not reopen or amend PR #23 or #24 or #25
  or #26 or #27 or #28 or #29 or #30 (do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30.
  merged #23 owns `notes.md` §105 / items 149–160 /
  batch #88; merged #24 owns `notes.md` §106 / items 161–177 /
  batch #89; merged #25 owns `notes.md` §107 / items 178–185 /
  batch #90; merged #26 owns `notes.md` §108 / items 186–201 /
  batch #91; merged #27 owns `notes.md` §109 / items 202–225 /
  batch #92; merged #28 owns `notes.md` §110 / items 226–247 /
  batch #93; merged #29 owns `notes.md` §111 / items 248–267 /
  batch #94 — leave them alone; merged #30 owns
  `notes.md` §112 / items 268–272 / batch #95 — leave them
  alone. This fold is `notes.md` §113 / items 273–288 /
  batch #96). Never reopen merged
  #7–**#30**. Do **not** re-fold 0646 / §111 / merged #30 / §112 / 0541 / §110 / 0439 / §109 / 0345 / §108 / 0243 / §107 /
  0145 / §106 / 0042 / §105 / 2340 / §104 / 2246 / §103 /
  2145 / §102 / 2041 / §101 / 1943 / §100 / 1843 / §99 /
  1740 / §98 / 1639 / §96 / gliner-native-runtime / §97 /
  1541 / §95 / jev-align *mechanism* / §93 /
  jev-orderby-bench *six-gates* / §60 / JevBench v1.2
  *board* / §78 / openJev-verdict *claim-audit* / §71 /
  pngwn RESULTS / §46 / yuki-oshio/mini-jev *93.25%* / §103.
  How-to-apply / mental models / architecture /
  Harbor-jevals / toolbelt — not a thin Jev skill dump.
  Backend-agnostic categorization/scoring/decision class.
  Formal methods compose with scoring; a Noul is a SENSOR;
  treating 77.0% as Harbor, 100% schema as correctness,
  0.85 as 85%, TF-IDF ECE as beating Jev, softmax A/B/C
  as a Noul, or ACT as a provider proof is soundness
  theater. Ranking ≠ calibration theater is the
  anti-pattern. Sixteen HIGH clusters / three themes:
  **Measurement / benches / calibration PRIMARY**
  ([ywchiu/jev_benchmark](https://github.com/ywchiu/jev_benchmark)
  ywchiu/jev_benchmark ≠ Running-Dolphins/jev-bench ≠ Praveenrajus/jev-bench;
  Gemma 4 31B 77.0% / Jev 1.13.0 61.4% / Laya 322M 0.0%;
  restriction state 95.0% against 84.4%; None of the systems are particularly good at knowing when to stop and ask;
  They skip the question and call a tool directly; 100% schema pass; six-field joint 48.8% vs 72.8%;
  GitHub license null; **0★**; HEAD `4322c350`; README SHA `75e6a338`; size **0** WITH CONTENTS);
  ([siren2345/jev-single-decode-transformers](https://github.com/siren2345/jev-single-decode-transformers)
  siren2345/jev-single-decode-transformers ≠ siren2345/jev-single-decode;
  Split Transformers experiment from llama.cpp runtime;
  Python MIT LICENSE SHA `3551844d`; **0★**; HEAD `2aa5fea7`; README SHA `65ba3335`; size **0** WITH CONTENTS);
  ([tanayvasishtha/jev-lab](https://github.com/tanayvasishtha/jev-lab)
  tanayvasishtha/jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab ≠ yibie/laya-jev-lab;
  Four experiments stress-testing TypeSafe's Jev: calibration, bundle bias, label bias, and ensembling;
  second pass must be $0.00 from cache; The pages never call Jev;
  **0★**; HEAD `7bfd37c1`; README SHA `33bc46e3`; size **43**);
  (hfdataset:Praveenrajus/jev-bench 22 configs · 166,054 rows · 4 calibration-gold; sha a39eba3f);
  (hfdataset:pngwn/open-jev-laya-bench pngwn/open-jev-laya-bench README 404; sha 9f69c742 likes 2);
  (hfdataset:reachjalil/jevlogs-log-triage-benchmark
  HDFS 0.9933 (745/750) / retain 0.0084; BGL ERROR/FATAL protection 1.0000;
  2,479 / 2,500 HDFS uncertain; cache hit 0.9648 (2412/2500); $0.153936 estimated;
  E2 recomputes from saved probabilities; sha `4c80b79c`);
  (hfspace:BunsDev/laya-calibration-lab Space sha eda59e0a;
  MASSIVE English 0.783 / Khmer 0.033 / Hindi 0.133; 40–48 rows too small to ship T;
  T never changes argmax);
  (hfdataset:Mikhail/mini-jev-runs 27 900 schema-driven decisions;
  13 600 / 13 600 questions; candidate mass min 0.99999624; sha `8f84bb1a`);
  **open-weight / theory / RLCD / replicas**
  ([Heman10x-NGU/Verdict-open-jev](https://github.com/Heman10x-NGU/Verdict-open-jev)
  Heman10x-NGU/Verdict-open-jev ≠ Heman10x-NGU/openJev-verdict-2.0;
  TF-IDF + LogReg ECE 0.0207 vs Jev 0.1440; Verdict-open-jev 48.07% vs Jev 90.80%;
  abstention combined recall 10.00%; p50 35.58 ms; K=25 (maximum capacity) 72.00%;
  0.85 coverage 84.60% selective risk 1.18%;
  Python SPDX NOASSERTION LICENSE SHA `84d35485`; **33★**; HEAD `465d542f`; README SHA `e2932455`; size **6709**);
  ([Mintzs/jevify](https://github.com/Mintzs/jevify)
  26.1× faster than standard Qwen JSON generation;
  Jevify 90.0% / 167 ms CUDA graphs disabled;
  **3★**; HEAD `20c112e3`; README SHA `77126815`; size **3086**);
  ([arnabgho/rlcd-lite](https://github.com/arnabgho/rlcd-lite)
  Finding 1: Brier on stated confidence alone is a trap;
  grpo_rlcr 0.78 / ECE 0.084; reliability 0.007 but resolution 0.000;
  Python Apache-2.0 LICENSE SHA `d6456956`; **1★**; HEAD `b0f981fa`; README SHA `560f24e5`; size **602**);
  (hfdataset:SargeDev/jev-distill-corpus Student B MAE 0.148 / Pearson 0.836 / 86.0%; sha `ebb133f0`);
  ([altryne/jevify](https://github.com/altryne/jevify)
  altryne/jevify ≠ Mintzs/jevify ≠ gulagala001/jevify ≠ uspraveen/Jevify;
  Find where Jev belongs. Design the questions. Measure the difference;
  TypeScript MIT LICENSE SHA `d66fef3a`; **13★**; HEAD `9b50ba13`; README SHA `9a4ec045`; size **48**);
  **skills / DecisionOps / applied**
  ([erayyilmmaz/jev-decisionops](https://github.com/erayyilmmaz/jev-decisionops)
  ACT / REVIEW / FALLBACK; A provider failure, timeout, malformed output, or missing answer is **not** a policy outcome;
  confidence is descriptive provider output, not a substitute for probability;
  Quality denominators include only valid scored answers;
  an exact halfway tie chooses the lower level;
  **0★**; HEAD `fe4e7aff`; README SHA `4688009e`; size **67**);
  ([aiwithenoch/Jev-Skill](https://github.com/aiwithenoch/Jev-Skill)
  aiwithenoch/Jev-Skill ≠ simplosophy/jev-skill ≠ laguagu/jev-skills;
  The local path does not claim to turn a smaller checkpoint into Jev;
  Low support becomes decision: "review"; MIT-0 SPDX NOASSERTION LICENSE SHA `f6bbe085`;
  **0★**; HEAD `f0cf6d6e`; README SHA `2aae6d3c`; size **42**);
  ([simplosophy/jev-skill](https://github.com/simplosophy/jev-skill)
  current-llm; 结构兼容，不是 Jev 模型能力;
  Python MIT LICENSE SHA `036a757d`; **0★**; HEAD `5cba50e7`; README SHA `5fa4f079`; size **0** WITH CONTENTS).
  TypeAR-AI/TypeAR 301 → TypeLLM/TypeLLM; TypeLLM/TypeLLM 16★;
  SemIf 2225★ (+18 vs §111 2207);
  jevlike 1046★ (+3 vs 1043);
  AnotiaWang 98★ (+1 vs 97);
  yibie/awesome-jev 516★ (+10 vs 506);
  Laya likes 852 (was 822);
  tracker likes 66 (+2 vs 64);
  lastModified UNCHANGED `2026-09-20T04:29:16.000Z`;
  Laya present; Blackwood ABSENT; Archer still promised_not_landed.
  0★ HIGH still got a real card. Soft Noul ≠ hard safety.
  `invented_signal: false`.
  Hourly 0743 uniqueness lock: Heman10x-NGU/Verdict-open-jev ≠ Heman10x-NGU/openJev-verdict-2.0; TF-IDF + LogReg ECE 0.0207 vs Jev 0.1440; Verdict-open-jev 48.07% vs Jev 90.80%; abstention combined recall 10.00%; p50 35.58 ms; K=25 (maximum capacity) 72.00%; 0.85 coverage 84.60% selective risk 1.18%; 26.1× faster than standard Qwen JSON generation; Jevify 90.0% / 167 ms CUDA graphs disabled; Finding 1: Brier on stated confidence alone is a trap; grpo_rlcr 0.78 / ECE 0.084; reliability 0.007 but resolution 0.000; 27 900 schema-driven decisions; 13 600 / 13 600 questions; candidate mass min 0.99999624; 22 configs · 166,054 rows · 4 calibration-gold; sha a39eba3f; Student B MAE 0.148 / Pearson 0.836 / 86.0%; pngwn/open-jev-laya-bench README 404; sha 9f69c742 likes 2; HDFS 0.9933 (745/750) / retain 0.0084; BGL ERROR/FATAL protection 1.0000; 2,479 / 2,500 HDFS uncertain; cache hit 0.9648 (2412/2500); $0.153936 estimated; E2 recomputes from saved probabilities; Space sha eda59e0a; MASSIVE English 0.783 / Khmer 0.033 / Hindi 0.133; 40–48 rows too small to ship T; T never changes argmax; siren2345/jev-single-decode-transformers ≠ siren2345/jev-single-decode; Split Transformers experiment from llama.cpp runtime; tanayvasishtha/jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab ≠ yibie/laya-jev-lab; Four experiments stress-testing TypeSafe's Jev: calibration, bundle bias, label bias, and ensembling; second pass must be $0.00 from cache; The pages never call Jev; Gemma 4 31B 77.0% / Jev 1.13.0 61.4% / Laya 322M 0.0%; restriction state 95.0% against 84.4%; None of the systems are particularly good at knowing when to stop and ask; They skip the question and call a tool directly; 100% schema pass; six-field joint 48.8% vs 72.8%; ywchiu/jev_benchmark ≠ Running-Dolphins/jev-bench ≠ Praveenrajus/jev-bench; ACT / REVIEW / FALLBACK; A provider failure, timeout, malformed output, or missing answer is **not** a policy outcome; confidence is descriptive provider output, not a substitute for probability; Quality denominators include only valid scored answers; an exact halfway tie chooses the lower level; aiwithenoch/Jev-Skill ≠ simplosophy/jev-skill ≠ laguagu/jev-skills; The local path does not claim to turn a smaller checkpoint into Jev; Low support becomes decision: "review"; MIT-0 SPDX NOASSERTION; current-llm; 结构兼容，不是 Jev 模型能力; altryne/jevify ≠ Mintzs/jevify ≠ gulagala001/jevify ≠ uspraveen/Jevify; Find where Jev belongs. Design the questions. Measure the difference; TypeAR-AI/TypeAR 301 → TypeLLM/TypeLLM; TypeLLM/TypeLLM 16★; SemIf 2225★ (+18 vs §111 2207); jevlike 1046★ (+3 vs 1043); AnotiaWang 98★ (+1 vs 97); yibie/awesome-jev 516★ (+10 vs 506); Laya likes 852 (was 822); tracker likes 66 (+2 vs 64); lastModified UNCHANGED `2026-09-20T04:29:16.000Z`; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30; notes.md §113

- User-provided HIGH Merve Noyan ZS classifier lineage
  (`research/notes.md` §112): **Skip Archer rewrite.**
  Docs-only on a **fresh PR off main**.
  **HARD RULE:** do not reopen or amend PR #23 or #24 or
  #25 or #26 or #27 or #28 or #29 (merged #29 owns
  `notes.md` §111 / items 248–267 / batch #94 — leave it
  alone). Institutional HF voice (@mervenoyann). Quote
  *theirs*. Do not invent accuracy numbers. Jev vs
  GPT-5.6 bakeoffs are a category error. encoder / ZS
  classifiers (BERTForXYZ → DeBERTa → ModernBERT). many
  problems solved with LLMs could have been solved with
  them, it was a skill issue. opt for DeBERTa and
  ModernBERT ones. multimodal image<>text ZS as
  perception front-end. softmax/ZS scores still ≠
  calibrated Noul. soft scores ≠ hard gates. Live X this
  pass: likes 421 / 189; impressions 35498 / 9613.
  Hub likes 139 / 72 cited. X MCP used.
  `invented_signal: false`. Composition items 268–272 /
  batch #95. Uniqueness lock: people who compare Jev against GPT-5.6 has never fine-tuned BERTForXYZ for living and it shows; zero shot classifiers; scale them as much as decoder only models; many problems solved with LLMs could have been solved with them, it was a skill issue; opt for DeBERTa and ModernBERT ones; BERTForXYZ → DeBERTa → ModernBERT; Jev vs GPT-5.6 bakeoffs are a category error; encoder / ZS classifiers; institutional HF voice; quote *theirs*; do not invent accuracy numbers; softmax/ZS scores still ≠ calibrated Noul; soft scores ≠ hard gates; @mervenoyann; likes 421 / 189; impressions 35498 / 9613; multimodal image<>text ZS as perception front-end; hf:MoritzLaurer/deberta-v3-large-zeroshot-v2.0 likes 139; hf:MoritzLaurer/ModernBERT-large-zeroshot-v2.0 likes 72; Bart, bert, deberta, modernbert, these are all LLMs; Maziyar quoted; Jev is exemplar not the mandate; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29.

- Hourly 0646 HIGH (`research/notes.md` §111): **Skip
  Archer rewrite.** Docs-only on a **fresh PR off main**.
  **HARD RULE:** do not reopen or amend PR #23 or #24 or #25
  or #26 or #27 or #28 (do not reopen or amend PR #23/#24/#25/#26/#27/#28.
  merged #23 owns `notes.md` §105 / items 149–160 /
  batch #88; merged #24 owns `notes.md` §106 / items 161–177 /
  batch #89; merged #25 owns `notes.md` §107 / items 178–185 /
  batch #90; merged #26 owns `notes.md` §108 / items 186–201 /
  batch #91; merged #27 owns `notes.md` §109 / items 202–225 /
  batch #92; merged #28 owns `notes.md` §110 / items 226–247 /
  batch #93 — leave them alone). Never reopen merged
  #7–**#28**. Do **not** re-fold 0541 / §110 / 0439 / §109 / 0345 / §108 / 0243 / §107 /
  0145 / §106 / 0042 / §105 / 2340 / §104 / 2246 / §103 /
  2145 / §102 / 2041 / §101 / 1943 / §100 / 1843 / §99 /
  1740 / §98 / 1639 / §96 / gliner-native-runtime / §97 /
  1541 / §95 / jev-align *mechanism* / §93 /
  jev-orderby-bench *six-gates* / §60 / JevBench v1.2
  *board* / §78 / openJev-verdict *claim-audit* / §71 /
  jev-judge-bench SLA-150 *contract* / §71 /
  yuki-oshio/mini-jev *93.25%* / §103. How-to-apply / mental
  models / architecture / Harbor-jevals / toolbelt — not a
  thin Jev skill dump. Backend-agnostic
  categorization/scoring/decision class. Formal methods
  compose with scoring; a Noul is a SENSOR; treating
  ECE as alpha, 0.5 compaction as safety, 0.8 nlgrep as
  80% correctness, contract_passed as truth, Wilson 0.85
  as a proof, 90.53% BBQ as calibrated, softmax over
  A/B/C as a Noul, 0.740 as TypeSafe vs Laya, 97.0% as
  Harbor, or intervals-including-zero as equivalence is
  soundness theater. Calibration is not alpha and ranking ≠
  calibration theater are the anti-patterns. Twenty HIGH
  clusters / three themes:
  **Measurement / benches / calibration PRIMARY**
  ([alakise/calibration-is-not-alpha](https://github.com/alakise/calibration-is-not-alpha)
  Calibration is not alpha; NO CURRENT ALPHA CANDIDATE;
  ΔR² approximately +0.00084; Brier 0.2131387; ECE 0.0421875;
  Adding Jev probability to deterministic volatility improved Brier by only 1.4058e-05;
  Python MIT LICENSE SHA `cbfc2daf`; **0★**; HEAD `064b75f5`; README SHA `874ea57b`; size **268**);
  ([OrMizL/jev-compaction-bench](https://github.com/OrMizL/jev-compaction-bench)
  default 0.5 keeps zero non pinned;
  keepResult median 0.14 to 0.17; keepCall median 0.28 to 0.35;
  usable range is about 0.10 to 0.25; 7.8% to 57.9%;
  judges results it never sees; task-finish eval not built yet;
  $0.002 per compaction;
  JavaScript MIT LICENSE SHA `3f4e7f2b`; **0★**; HEAD `92fd33e6`; README SHA `c7cd8b6e`; size **35**);
  ([slavadubrov/sgr-judge-bench](https://github.com/slavadubrov/sgr-judge-bench)
  slavadubrov/sgr-judge-bench ≠ slavadubrov/jev-judge-bench;
  Jev 108/120 $0.083 0.34 s; Luna SGR 114/120;
  paired Jev accuracy-difference intervals include zero;
  not evidence of equivalence;
  GLM SGR 26/120 93 format failures; Terra-planned Jev hybrid 55/120;
  Python; SPDX NOASSERTION LICENSE SHA `690cf6b9`; **0★**; HEAD `5e142707`; README SHA `8026cafa`; size **0** WITH CONTENTS);
  ([elyashium/atlas-replay-lab](https://github.com/elyashium/atlas-replay-lab)
  rule-based by default, optionally Jev-backed; empty README;
  missing key cannot break the experience;
  JavaScript; GitHub license null; **0★**; HEAD `9856ab9b`; size **197**);
  ([siren2345/jev-single-decode](https://github.com/siren2345/jev-single-decode)
  prefill plus exactly one decode; softmax over A/B/C ≠ Noul;
  BBQ 9,053/10,000 (90.53%); ECE 0.0890; Mean confidence 0.9943;
  overconfident; score and noul not implemented;
  Python MIT LICENSE SHA `3551844d`; **0★**; HEAD `65df86a3`; README SHA `51817d8c`; size **432**);
  **datasets / Spaces**
  (hfdataset:ctaxnagomi/DGUI_HYPERMEM-JEV
  DGUI 12 rows (was 6); sha `ab3d3529`);
  (hfdataset:ctaxnagomi/INSTRUCT_JEV
  INSTRUCT 119 rows likes 2; sha `b0a09278`);
  (hfspace:pngwn/open-jev
  encode the state once, decide everything in parallel;
  0.740 accuracy against a 0.508 majority; ECE 0.047;
  fine-tune's advantage ends where its 384-token training data does;
  likes **25**; sha `d41dc3cd`);
  (hfspace:jasonkneen/open-jev
  jasonkneen/open-jev ≠ pngwn/open-jev; same sha d41dc3cd; likes **0**);
  (hfspace:IkerMoel/open-alternative-jev densify sha `19b104c6`);
  (hfspace:mobarmg/jev-schema-scorer densify sha `14d35d7e`; peaked ranking ≠ calibration);
  (hfspace:reachjalil/jevlogs-triage-explorer
  Space does not call Jev; recomputes routing from saved probabilities;
  sha `dcb785ed`);
  **applied / skills / economics**
  ([IslamBaraka90/jev-typesafe-real-financial-use-cases](https://github.com/IslamBaraka90/jev-typesafe-real-financial-use-cases)
  fifty recorded demos; recorded ≠ alpha;
  JavaScript MIT LICENSE SHA `caaa17a8`; **0★**; HEAD `9d2eb48c`; README SHA `5329b92e`; size **6168**);
  ([Milo318/mailordinal](https://github.com/Milo318/mailordinal)
  200-case Jev 97.0% / 100.0% / 95.0% / MAE 9.22;
  synthetic repository benchmark;
  TypeScript MIT LICENSE SHA `66faa16d`; **0★**; HEAD `19ea819d`; README SHA `a8df45fe`; size **109**);
  ([Pleo2/awesome-jev-agent-skills](https://github.com/Pleo2/awesome-jev-agent-skills)
  Jev evaluations are advisory; catalog ≠ endorsement;
  Python MIT LICENSE SHA `25d9aa30`; **0★**; HEAD `42e3d179`; README SHA `efbe7ccf`; size **18**);
  ([YehuiTang0316/jev-nlgrep](https://github.com/YehuiTang0316/jev-nlgrep)
  YehuiTang0316/jev-nlgrep ≠ Bentlybro/jevgrep ≠ can1357/jegrep ≠ uehaj/jev-semgrep;
  default threshold 0.8 still soft; 40-line windows cannot prove whole function;
  TypeScript MIT LICENSE SHA `17cdbc7e`; **1★**; HEAD `ceec0d92`; README SHA `49e98f18`; size **6734**);
  ([dangquan1402/jev-extract](https://github.com/dangquan1402/jev-extract)
  token-native sequential start/end Choice; Gemini/Haiku stubs not configured yet;
  Python MIT LICENSE SHA `d66f9c7a`; **0★**; HEAD `20c2f19f`; README SHA `9561e53d`; size **105**);
  ([jyje/pilot-typesafeai-jev](https://github.com/jyje/pilot-typesafeai-jev)
  handful of hand-written examples, not a benchmark;
  Jev judged exactly what it was given;
  Python MIT LICENSE SHA `08b2a315`; **0★**; HEAD `cabd4778`; README SHA `8d472372`; size **245**);
  ([laguagu/jev-skills](https://github.com/laguagu/jev-skills)
  laguagu/jev-skills ≠ laguagu/jev-evidence-lab ≠ Pleo2/awesome-jev-agent-skills;
  MIT LICENSE SHA `e5ede121`; **0★**; HEAD `871ec586`; README SHA `a315944d`; size **72**);
  ([lorensation/llm-cost-optimizer-jev](https://github.com/lorensation/llm-cost-optimizer-jev)
  contract_passed is not a claim of guaranteed factual truth;
  Wilson lower bound 0.85 floor; fixture mode no savings claim;
  Python Apache-2.0 LICENSE SHA `261eeb9e`; **0★**; HEAD `db200b7e`; README SHA `6f2a595a`; size **227**).
  SemIf 2207★ (+21 vs §110 2186);
  jevlike 1043★ (+5 vs 1038);
  TypeAR 15★ (+1 vs 14);
  AnotiaWang 97★ (+1 vs 96);
  yibie/awesome-jev 506★ (+16 vs 490);
  Laya likes 822 (was 802);
  tracker likes 64 flat, lastModified UNCHANGED;
  Laya present; Blackwood ABSENT; Archer still promised_not_landed.
  0★ HIGH still got a real card. Soft Noul ≠ hard safety.
  `invented_signal: false`.
  Hourly 0646 uniqueness lock: Calibration is not alpha; NO CURRENT ALPHA CANDIDATE; ΔR² approximately +0.00084; Brier 0.2131387; ECE 0.0421875; Adding Jev probability to deterministic volatility improved Brier by only 1.4058e-05; default 0.5 keeps zero non pinned; keepResult median 0.14 to 0.17; keepCall median 0.28 to 0.35; usable range is about 0.10 to 0.25; 7.8% to 57.9%; judges results it never sees; task-finish eval not built yet; $0.002 per compaction; slavadubrov/sgr-judge-bench ≠ slavadubrov/jev-judge-bench; Jev 108/120 $0.083 0.34 s; Luna SGR 114/120; paired Jev accuracy-difference intervals include zero; not evidence of equivalence; GLM SGR 26/120 93 format failures; Terra-planned Jev hybrid 55/120; rule-based by default, optionally Jev-backed; empty README; missing key cannot break the experience; prefill plus exactly one decode; softmax over A/B/C ≠ Noul; BBQ 9,053/10,000 (90.53%); ECE 0.0890; Mean confidence 0.9943; overconfident; score and noul not implemented; DGUI 12 rows (was 6); INSTRUCT 119 rows likes 2; encode the state once, decide everything in parallel; 0.740 accuracy against a 0.508 majority; ECE 0.047; fine-tune's advantage ends where its 384-token training data does; jasonkneen/open-jev ≠ pngwn/open-jev; same sha d41dc3cd; Space does not call Jev; recomputes routing from saved probabilities; 200-case Jev 97.0% / 100.0% / 95.0% / MAE 9.22; synthetic repository benchmark; Jev evaluations are advisory; YehuiTang0316/jev-nlgrep ≠ Bentlybro/jevgrep ≠ can1357/jegrep ≠ uehaj/jev-semgrep; default threshold 0.8 still soft; 40-line windows cannot prove whole function; token-native sequential start/end Choice; Gemini/Haiku stubs not configured yet; handful of hand-written examples, not a benchmark; Jev judged exactly what it was given; laguagu/jev-skills ≠ laguagu/jev-evidence-lab ≠ Pleo2/awesome-jev-agent-skills; contract_passed is not a claim of guaranteed factual truth; Wilson lower bound 0.85 floor; fixture mode no savings claim; SemIf 2207★ (+21 vs §110 2186); jevlike 1043★ (+5 vs 1038); TypeAR 15★ (+1 vs 14); AnotiaWang 97★ (+1 vs 96); yibie/awesome-jev 506★ (+16 vs 490); Laya likes 822 (was 802); tracker likes 64 flat, lastModified UNCHANGED; do not reopen or amend PR #23/#24/#25/#26/#27/#28.

- Hourly 0541 HIGH (`research/notes.md` §110): **Skip
  Archer rewrite.** Live-REST relock after adversarial
  review (HEAD/README/size/stars/likes; Brier/Independent
  design claims unchanged). Docs-only on a **fresh PR off main**.
  **HARD RULE:** do not reopen or amend PR #23 or #24 or #25
  or #26 or #27 (do not reopen or amend PR #23/#24/#25/#26/#27.
  merged #23 owns `notes.md` §105 / items 149–160 /
  batch #88; merged #24 owns `notes.md` §106 / items 161–177 /
  batch #89; merged #25 owns `notes.md` §107 / items 178–185 /
  batch #90; merged #26 owns `notes.md` §108 / items 186–201 /
  batch #91; merged #27 owns `notes.md` §109 / items 202–225 /
  batch #92 — leave them alone). Never reopen merged
  #7–**#27**. Do **not** re-fold 0439 / §109 / 0345 / §108 / 0243 / §107 /
  0145 / §106 / 0042 / §105 / 2340 / §104 / 2246 / §103 /
  2145 / §102 / 2041 / §101 / 1943 / §100 / 1843 / §99 /
  1740 / §98 / 1639 / §96 / gliner-native-runtime / §97 /
  1541 / §95 / jev-align *mechanism* / §93 /
  jev-orderby-bench *six-gates* / §60 / JevBench v1.2
  *board* / §78 / openJev-verdict *claim-audit* / §71 /
  yuki-oshio/mini-jev *93.25%* / §103. How-to-apply / mental
  models / architecture / Harbor-jevals / toolbelt — not a
  thin Jev skill dump. Backend-agnostic
  categorization/scoring/decision class. Formal methods
  compose with scoring; a Noul is a SENSOR; treating
  Blackwood tracker-absent as landed, 0.9 as one number,
  8/8 as conversion lift, 200-row as ranking, 0.85 as 85%,
  Hub Meanblock as a new species vs leesk212, circulating
  $0.0004 as measured, Score as 0–1, Noul.confidence as
  existing, json_schema gap as typed-model win, 64× Space
  as Harbor, awesome listed counts as eval, WANLI 0.741 as
  beating openjev, ECE 0.021 as a hard gate, Independent
  `{cat,dog}` as Choice, softmax over letter slots as a
  Noul, minProbability 0.85 as Harbor, or :max as a
  mandatory search size is soundness theater. treating
  0.85 as 85% / minProbability hard-gate as Harbor, 0.9
  as one number, and 8/8 as conversion lift are the
  anti-patterns. Twenty-two HIGH clusters / three themes:
  **Open-weight / RLCD / Blackwood watch**
  (hf:BlackwoodAI/blackwood-rlcd
  Blackwood tracker ABSENT; likes 2 gated manual;
  sha `3b9e29df`);
  (hf:anthonym21/qwen3-0.6b-rlcd-decision
  r = c - p_a; ECE 0.021; acc 0.807 vs warmup 0.746;
  calibration beyond ~500 tokens unmeasured;
  apache-2.0; likes **2**; sha `b327ec5e`);
  (hf:larkooo/gemma-e2b-rlcd
  Independent primitive;
  11.57s vs 54.10s · 4.67× · 120/128 *theirs*;
  default path is pretrained Gemma probs not trained RLCD head;
  apache-2.0; likes **1**; sha `e099c730`);
  (hf:Meanblock/JEV-CPU
  GH Meanblock 404; lock leesk212/JEV-CPU;
  softmax over letter slots ≠ Noul;
  mit; likes **7**; sha `759fa606`);
  (hf:impacte/mimir-lfm-openjev
  WANLI 0.741 vs openjev v2 0.77 *theirs*;
  3-way NLI ≠ Noul; likes **0**; sha `5f9173bb`);
  (hf:shreyanbr/system-one-distilled | gold | zeroshot
  priority 0.464 = majority floor;
  banking77 contaminated;
  raw margins not probabilities;
  GH jev-haiku-benchmarking 404;
  do not distill Jev as teacher of record (they distilled Haiku);
  shas `56c9dba8` / `93e22fcf` / `4b6659d5`);
  **measurement densifies PRIMARY**
  ([Running-Dolphins/jev-bench](https://github.com/Running-Dolphins/jev-bench)
  “0.9 is not one number”; ranking ≠ calibration;
  banking77 0.8–0.9 stated 0.86 actual 0.73 over-confident *theirs*;
  ≠ Praveenrajus/jev-bench ≠ fstandhartinger/jevbench;
  Python MIT LICENSE SHA `891c70c6`; **0★**; HEAD `67d2ee42`; README SHA `ae2c5003`; size **1070**);
  ([WallerChen/jev-measured](https://github.com/WallerChen/jev-measured)
  $0.0000153–$0.0000226 vs circulating $0.0004 (~20×);
  Score is 0..n-1 expectation not 0–1;
  Noul has no confidence field;
  TCP floor 198.8 ms;
  type reliability is not a reason to choose Jev (json_schema 5/5);
  gateway tax not one number;
  Python MIT LICENSE SHA `0c563e25`; **0★**; HEAD `4a12dfb3`; README SHA `1c2c38ac`; size **37**);
  ([RadRebelSam/jev-decision-lab](https://github.com/RadRebelSam/jev-decision-lab)
  Function-only 5/8 vs hybrid 8/8; 4/8 without Jev;
  8 designed cases not conversion lift;
  ≠ RadRebelSam/awesome-jev;
  TS MIT LICENSE SHA `ae6f994c`; **0★**; HEAD `e6d6d42d`; README SHA `52a0071d`; size **128**);
  ([jackojacko05/compare-jev-bigquery-ai-functions](https://github.com/jackojacko05/compare-jev-bigquery-ai-functions)
  200-row pilot Jev 86.5% 173/200 vs Gemini Flash-Lite 86.0% 172/200 vs Pro 87.0% 174/200 *theirs*;
  not a ranking;
  Jupyter MIT LICENSE SHA `0248c4b0`; **0★**; HEAD `cb9ef56b`; README SHA `d3db5d6c`; size **307**);
  ([Trecto34/openjev-fighting-ring](https://github.com/Trecto34/openjev-fighting-ring)
  NLI Tetris argmax P(entail)−P(contradict);
  Python; license null; **0★**; HEAD `ac544f1e`; README SHA `b3fe2907`; size **1159**);
  ([joshhu/jevtest](https://github.com/joshhu/jevtest)
  情緒測謊器; 1q 396ms / 30q 567ms; ±0.03;
  33q $0.000045 vs Gemini ~5× slower ~60× cost *theirs*;
  ≠ realZachi/jevtest;
  HTML; license null; **0★**; HEAD `6a4df41d`; README SHA `57d99325`; size **34**);
  (hfspace:aahf/JevBenchmark
  8-example Jev vs GPT-5.6 Sol ~64× cost 5.4× latency *theirs*;
  synthetic; no inference; ≠ JevBench v1.2 §78;
  likes **1**; sha `36c28088`);
  ([rhc98/awesome-jev](https://github.com/rhc98/awesome-jev)
  Judged 3317 / listed 2560; Jev judges, code applies policy;
  catalog ≠ endorsement;
  TS; SPDX NOASSERTION LICENSE SHA `d491d714`; **1★**; HEAD `82898f25`; README SHA `e1f12080`; size **2529**);
  ([AiPersonacademy/Awesome-jev-use](https://github.com/AiPersonacademy/Awesome-jev-use)
  APA “microsecond policy / zero hallucination” overclaim;
  CC0-1.0 LICENSE SHA `7ba0a23e`; **2★**; HEAD `29246f12`; README SHA `d506c11f`; size **124**);
  **applied / theory placements**
  ([erseco/questionator](https://github.com/erseco/questionator)
  Client-side quiz; pointer from held docs; scanned-PDF warn;
  CSP only api.typesafe.ai;
  JS MIT LICENSE SHA `3ebdd11d`; **0★**; HEAD `b498f10b`; README SHA `4334c847`; size **1267**);
  ([grgy078033/grill-jev](https://github.com/grgy078033/grill-jev)
  Jev judges / agent reasons / user decides;
  selecting an option is not permission to implement;
  degraded fallback;
  Python MIT LICENSE SHA `7c0e962d`; **1★**; HEAD `5ce6cbe8`; README SHA `da80efcc`; size **85**);
  ([makefunstuff/jev-lsp](https://github.com/makefunstuff/jev-lsp)
  pattern exact, judgement must clear floor;
  no matching pattern → no model call;
  not a correctness oracle;
  $0.00022 vs chat $0.00306 *theirs*;
  Rust MIT LICENSE SHA `fb5bc4a5`; **0★**; HEAD `bce3d8ed`; README SHA `c7ecbf8f`; size **1696**);
  ([nozomi-koborinai/jev-spec](https://github.com/nozomi-koborinai/jev-spec)
  Spec vs artifact remainder;
  treating 0.85 as 85% / minProbability hard-gate as Harbor;
  TS MIT LICENSE SHA `e43f732a`; **1★**; HEAD `86f14198`; README SHA `c0f29baa`; size **73**);
  ([202620325-spec/Jev-LLM](https://github.com/202620325-spec/Jev-LLM)
  VERIFY acquires discriminating evidence, never same-pool confidence-only rescoring;
  fast/full/max are ceilings not sizes;
  Solar writes, Jev chooses NEXT ACTION;
  Python MIT LICENSE SHA `5d699c97`; **0★**; HEAD `da06b6d1`; README SHA `f371ba83`; size **150**).
  SemIf 2186★ (+20 vs §109 2166);
  jevlike 1038★ (+7 vs 1031);
  TypeAR 14★ flat;
  AnotiaWang 96★ (+1 vs 95);
  yibie/awesome-jev 490★;
  Laya likes 802 (was 783);
  tracker likes 64 flat, lastModified UNCHANGED;
  Laya present; Blackwood ABSENT; Archer still promised_not_landed.
  0★ HIGH still got a real card. Soft Noul ≠ hard safety.
  `invented_signal: false`.

- Hourly 0439 HIGH (`research/notes.md` §109): **Skip
  Archer rewrite.** Docs-only on a **fresh PR off main**.
  **HARD RULE:** do not reopen or amend PR #23 or #24 or #25
  or #26 (do not reopen or amend PR #23/#24/#25/#26.
  merged #23 owns `notes.md` §105 / items 149–160 /
  batch #88; merged #24 owns `notes.md` §106 / items 161–177 /
  batch #89; merged #25 owns `notes.md` §107 / items 178–185 /
  batch #90; merged #26 owns `notes.md` §108 / items 186–201 /
  batch #91 — leave them alone). Never reopen merged
  #7–**#26**. Do **not** re-fold 0345 / §108 / 0243 / §107 /
  0145 / §106 / 0042 / §105 / 2340 / §104 / 2246 / §103 /
  2145 / §102 / 2041 / §101 / 1943 / §100 / 1843 / §99 /
  1740 / §98 / 1639 / §96 / gliner-native-runtime / §97 /
  1541 / §95 / jev-align *mechanism* / §93 /
  jev-orderby-bench *six-gates* / §60 / JevBench v1.2
  *board* / §78 / openJev-verdict *claim-audit* / §71 /
  yuki-oshio/mini-jev *93.25%* / §103. How-to-apply / mental
  models / architecture / Harbor-jevals / toolbelt — not a
  thin Jev skill dump. Backend-agnostic
  categorization/scoring/decision class. Formal methods
  compose with scoring; a Noul is a SENSOR; treating
  WANLI-256 64.5/60.2/52.0 as Harbor, label_mass as
  correctness, Hub v1 family cards as shipping GGUF,
  re-folding §108 27B/ternary as new, treating LoRA stub
  cards as independent eval, hard-gating jevify n=307 ECE
  0.061 as “honest probabilities”, collapsing kushalpatil
  into Mintzs/gulagala001/uspraveen, treating GH
  kushalpatil07/jevify as an existing repo, collapsing
  JulesHuisman into SivletLabs/4esv, quoting 32/32 synthetic
  as production, hard-gating 0.8 evidence as proof, quoting
  40-band 0/10 without 7-band, treating /judge 0.5 as truth,
  treating git-confess 11% as a person verdict, treating
  paper-trader +12.40% as edge, treating Awesomejev
  656/38160 as eval, treating tracker likes as Archer
  landing, using roadus2 spelling, pasting ultra_laya vs-Jev
  as this-fork win, or treating jevgraph 100% gated as
  production is soundness theater. jevify ECE 0.061 as a
  hard gate, 0.8 evidence as proof, and paper-trader fills
  as edge are the anti-patterns. Twenty-four HIGH clusters /
  three themes:
  **open reproduction densifies**
  (hf:kushalpatil/jevify-gemma4-26b-a4b
  Gemma-4 26B-A4B jevify classification+calibration;
  Hub jevify merged LoRA ships weights;
  PAWS 0.580/ece 0.288 is the weak cell;
  kushalpatil/jevify-gemma4 ≠ Mintzs/jevify ≠ gulagala001/jevify ≠ uspraveen/Jevify;
  GH kushalpatil07/jevify 404;
  license gemma; likes **0**; sha `d4c0d1d4`);
  (hf:kushalpatil/jevify-gemma4-26b-a4b-lora
  LoRA adapter twin not independent eval;
  license null; likes **0**; sha `ec4a3d22`);
  (hf:kushalpatil/jevify-gemma4-e4b
  Gemma-4 E4B jevify;
  smaller E4B slightly better OOD ECE than 26B-A4B;
  license gemma; likes **0**; sha `a6b5a716`);
  (hf:kushalpatil/jevify-gemma4-e4b-lora
  E4B LoRA stub card; license null; likes **0**; sha `cca1f55e`);
  (hf:NicolaiMTLassen/bonzi-8b-v1-jev
  bonzi Bonsai-8B v1 GGUF densify; WANLI-256 64.5% *theirs*;
  rank #4 of 6; MIT; likes **0**; sha `588bc44e`);
  (hf:NicolaiMTLassen/bonzi-1.7b-v1-jev
  Bonsai-1.7B v1; WANLI-256 52.0% *theirs*; rank #6 of 6;
  MIT; likes **0**; sha `48148bf9`);
  (hf:NicolaiMTLassen/bonzi-4b-v1-jev
  Bonsai-4B v1; WANLI-256 60.2% *theirs*; rank #5 of 6;
  MIT; likes **0**; sha `d5545084`);
  ([roadius2/ultra_laya](https://github.com/roadius2/ultra_laya)
  roadus2 watch misspelling; lock roadius2/ultra_laya;
  ultra_laya REVIEW defects;
  default branch claude/laya-jev-review-gg5ppo;
  Python Apache-2.0 LICENSE SHA `d9a10c0d`; **0★**; HEAD `0dff5bd2`; README SHA `da95bc05`; size **0** WITH CONTENTS);
  **measurement densifies PRIMARY**
  ([AHTOOOXA/jev-cyrillic-audit](https://github.com/AHTOOOXA/jev-cyrillic-audit)
  XNLI EN 88.3% ECE 0.032 → RU 77.3% ECE 0.096;
  Δ −11.0 pp [−14.2,−7.8]; ECE +0.063;
  MASSIVE no detectable difference at n=600;
  confidence is function of p_max (r=1.000);
  Python MIT LICENSE SHA `f9b9193e`; **0★**; HEAD `7167894a`; README SHA `d36a36f5`; size **1302**);
  ([JulesHuisman/jev-eval](https://github.com/JulesHuisman/jev-eval)
  JulesHuisman/jev-eval scaffolding / README SHA c356a584 (was empty e69de29b);
  JulesHuisman/jev-eval ≠ SivletLabs/jev-eval ≠ willkelly/jev-evaluation ≠ 4esv ≠ xxkuboxx ≠ onlyoneaman ≠ dayhaysoos/jevals;
  Python; license null; **0★**; HEAD `96c2a110`; size **0** WITH CONTENTS);
  ([tunahansahin897/what-is-jev](https://github.com/tunahansahin897/what-is-jev)
  947 repos scored; A 273 / B 302 / C 372; LLM rubric ≠ benches;
  Python; SPDX NOASSERTION LICENSE SHA `790f3358`; **0★**; HEAD `71d53be2`; README SHA `3ae98c56`; size **6277**);
  ([Mishkun/judge-jev](https://github.com/Mishkun/judge-jev)
  judge-jev 0.5 still soft;
  TS; license null; **0★**; HEAD `1bf495d3`; README SHA `3788ab6e`; size **65**);
  **applied class placements**
  ([LiuHao-1443/jev-table-tennis](https://github.com/LiuHao-1443/jev-table-tennis)
  7 bands 6/10 vs 40 bands 0/10;
  Python MIT LICENSE SHA `777dc3d6`; **1★**; HEAD `0224c21c`; README SHA `3a54bc93`; size **0** WITH CONTENTS);
  ([laguagu/jev-evidence-lab](https://github.com/laguagu/jev-evidence-lab)
  source receipts + confidence slider re-policy without re-inference;
  32/32 synthetic is smoke not production;
  Python MIT LICENSE SHA `e5ede121`; **0★**; HEAD `a9669e94`; README SHA `1be53f55`; size **0** WITH CONTENTS);
  ([hemanth/hfjev](https://github.com/hemanth/hfjev)
  classify HF datasets across typed semantic dimensions;
  Python MIT LICENSE SHA `0ac06d77`; **1★**; HEAD `6f2aa501`; README SHA `20651a25`; size **48**);
  ([akash-kamat/jev-llm](https://github.com/akash-kamat/jev-llm)
  pointer-not-generator 400 human-authored responses;
  JS; license null; **0★**; HEAD `194db1a6`; README SHA `c42907a6`; size **54**);
  ([chenmingtang830/jevgraph](https://github.com/chenmingtang830/jevgraph)
  proposed ≠ authorized; FewRel 160: Jev 85.0% vs lexical 13.125%;
  gated 100% (95/95) coverage 59.375%;
  Python Apache-2.0 LICENSE SHA `57bc88a1`; **0★**; HEAD `7a6f7d05`; README SHA `bda2ed37`; size **125**);
  ([Towow-ai/jpp](https://github.com/Towow-ai/jpp)
  J++ composable semantic computation language;
  Python MIT LICENSE SHA `b1a46fbc`; **3★**; HEAD `14d77789`; README SHA `0a82d97f`; size **1071**);
  ([whyashthakker/awesome-jev-use-cases](https://github.com/whyashthakker/awesome-jev-use-cases)
  No benchmark winner is claimed;
  HTML MIT LICENSE SHA `13b5a2a6`; **3★**; HEAD `74583663`; README SHA `a6d96b87`; size **426**);
  ([dog-last/awesome-jev](https://github.com/dog-last/awesome-jev)
  phishing: naive 62.6% vs regex 91.8%; 5-atomic + LR 95.0% *theirs*;
  Python MIT LICENSE SHA `cd31b9aa`; **1★**; HEAD `206fdcab`; README SHA `1ca65f69`; size **85**);
  ([shinshin86/jev-aituber-tension-sample](https://github.com/shinshin86/jev-aituber-tension-sample)
  AITuber tension ±15;
  TS MIT LICENSE SHA `8b20d89e`; **0★**; HEAD `8c0a8ffb`; README SHA `06536d19`; size **105**);
  ([shinpr/jev-reranker](https://github.com/shinpr/jev-reranker)
  README npm global; repo is Rust;
  Rust MIT LICENSE SHA `4306a712`; **1★**; HEAD `731deba3`; README SHA `e2818c0e`; size **163**);
  ([AHTOOOXA/git-confess](https://github.com/AHTOOOXA/git-confess)
  git-confess code owns counting/blame/ratio;
  httpx exhibit 11% (13/119) *theirs*;
  Python MIT LICENSE SHA `f9b9193e`; **0★**; HEAD `54cd2849`; README SHA `764076a6`; size **3**);
  ([waterme7on/jev-paper-trader](https://github.com/waterme7on/jev-paper-trader)
  90d trend +12.40% vs random +12.75% vs BH +41.71%;
  5m win rate 25%;
  JS; license null; **0★**; HEAD `73662f79`; README SHA `4eded35a`; size **145**).
  Awesomejev 656 entries / 38,160 stars;
  WANLI-256 64.5% / 60.2% / 52.0% *theirs*;
  rank #4 / #5 / #6 of 6;
  tracker likes 64 (+4) lastModified UNCHANGED;
  Laya present; Blackwood ABSENT; Archer still promised_not_landed.
  0★ HIGH still got a real card. Soft Noul ≠ hard safety.
  `invented_signal: false`.

- Hourly 0345 HIGH (`research/notes.md` §108): **Skip
  Archer rewrite.** Docs-only on a **fresh PR off main**.
  **HARD RULE:** do not reopen or amend PR #23 or #24 or #25 (merged
  #23 owns `notes.md` §105 / items 149–160 / batch #88;
  merged #24 owns `notes.md` §106 / items 161–177 / batch #89;
  merged #25 owns `notes.md` §107 / items 178–185 / batch #90 —
  leave them alone). Never reopen merged
  #7–**#25**. Do **not** re-fold 0243 / §107 / 0145 / §106 / 0042 / §105 / 2340 / §104 / 2246 /
  §103 / 2145 / §102 / 2041 / §101 / 1943 / §100 / 1843
  / §99 / 1740 / §98 / 1639 / §96 / gliner-native-runtime
  / §97 / 1541 / §95 / jev-align *mechanism* / §93 /
  jev-orderby-bench *six-gates* / §60 / JevBench v1.2
  *board* / §78 / openJev-verdict *claim-audit* / §71 /
  yuki-oshio/mini-jev *93.25%* / §103. How-to-apply / mental models /
  architecture / Harbor-jevals / toolbelt — not a thin
  Jev skill dump. Backend-agnostic
  categorization/scoring/decision class. Formal methods
  compose with scoring; a Noul is a SENSOR; treating
  WANLI-256 as Harbor, label_mass as correctness, Hub
  family cards as shipping weights, collapsing stock Q1_0
  into §107 Q2_0 gibberish, treating the HF twin as a
  weights drop, quoting 93.25% as family-disjoint,
  hard-gating injection ECE 0.058 as “Jev is calibrated”,
  quoting AbstentionBench rank 1 without question-asymmetry /
  2025 field, treating dspy-bench as a quality claim,
  hard-gating pdf-race 12/12 as pipeline equality, treating
  atlas listed counts as eval, hard-gating flopcheck
  composite as truth, treating calibration-lab 40-row T as
  production, treating CLEVR joint 0% as “vision Jev works”,
  treating ONNX 63/63 as ECE, treating openkev T as
  transferable, or treating select_threshold inf as a bug
  is soundness theater. Injection ECE 0.058 as a hard gate
  and 40-row T as production are the anti-patterns. Sixteen
  HIGH clusters / two themes:
  **open reproduction densifies**
  (hf:NicolaiMTLassen/bonzi-27b-v2-jev
  ternary Bonsai 27B v2 open-bonzi GGUF family densify;
  Hub still does not ship weights; WANLI-256 74.6% *theirs*;
  ternary still needs PrismML fork; MIT; likes **0**; sha `c4d21b74`);
  (hf:NicolaiMTLassen/bonzi-8b-ternary-v1-jev
  ternary Bonsai 8B open-bonzi GGUF; WANLI-256 65.2% *theirs*;
  MIT; likes **0**; sha `47b66187`);
  (hf:NicolaiMTLassen/bonzi-27b-v1-jev
  Bonsai 27B v1 open-bonzi GGUF; Bonsai 1 27B Q1_0 runs on stock llama.cpp;
  WANLI-256 71.1% *theirs*; MIT; likes **0**; sha `2fb8061a`);
  (hf:mizchi/laya-multilingual-onnx
  Laya multilingual ONNX WebGPU typed-decisions port;
  63/63 selected answers / 5.1e-4 CPU / 1.2e-2 WebGPU;
  ships model.onnx 646.9MB; apache-2.0; likes **0**; sha `b6314ec9`);
  (hf:IamBusy/OpenJev-Vision
  OpenJev Vision image classification + uncertainty;
  CLEVR-4 held-out joint 0%; license other; likes **0**; sha `8cf6cbd3`);
  (hf:heman10x/openJev-verdict-2.0
  twin tokenizer-only; no 149.6M weights; likes **5** ≠ GH **107★**;
  apache-2.0; sha `794d5e0d`);
  (hfdataset:IamBusy/OpenJev-Vision-Research-v0.1
  12,832 images; 294,912 derived targets not independent samples;
  license other; likes **0**; sha `43e49184`);
  ([UpHash-Network/mini-jev](https://github.com/UpHash-Network/mini-jev)
  UpHash-Network/mini-jev is yuki-oshio transfer;
  residual-head 9,222-param decreased 73/96→67/96;
  Python MIT LICENSE SHA `79e2cff7`; **0★**; HEAD `52fbae12`; README SHA `363441b6`; size **38388**);
  **measurement densifies PRIMARY**
  ([ASEVlad/jev-injection-bench](https://github.com/ASEVlad/jev-injection-bench)
  jev-injection-bench 11,900 labelled prompts;
  Jev best ranking / Haiku better ECE 0.021 vs 0.058;
  0.5–0.9 band is where Jev's numbers do not mean what they say;
  Prompt wording moves panic 28%;
  Python MIT LICENSE SHA `0dab34c6`; **0★**; HEAD `c0d0f25d`; README SHA `1b28498c`; size **107**);
  ([manojlds/jev-dspy-bench](https://github.com/manojlds/jev-dspy-bench)
  Jev agreement is similarity, never ground truth;
  no aggregate quality grade or merge gate;
  manojlds/jev-dspy-bench ≠ dspachos/jev-dspy ≠ jmanhype/jev-dspy-lab;
  Python Apache-2.0 LICENSE SHA `261eeb9e`; **0★**; HEAD `d8c68d72`; README SHA `16100deb`; size **0** WITH CONTENTS);
  ([sshariqali/jev-abstentionbench](https://github.com/sshariqali/jev-abstentionbench)
  AbstentionBench-on-Jev rank 1 of 20 vs 2025 field;
  question-asymmetry; forward-looking 0.465 never extreme;
  Python; README MIT / GitHub SPDX NOASSERTION LICENSE SHA `7f6fb3ba`; **0★**; HEAD `f5c0c068`; README SHA `26393f0f`; size **0** WITH CONTENTS);
  ([misakaikato/openkev](https://github.com/misakaikato/openkev)
  openkev calibration layer not a runtime;
  ECE vs coverage independent; select_threshold returns inf;
  escalation catches uncertainty not ignorance;
  misakaikato/openkev ≠ jaredpalmer/kev;
  Python MIT LICENSE SHA `8c3231cb`; **0★**; HEAD `babcab1c`; README SHA `974d97f9`; size **484**);
  ([goodrahstar/pdf-race](https://github.com/goodrahstar/pdf-race)
  pdf-race Docling→Jev vs Gemini; parser owns the wall clock;
  12/12 tie is a tie; titles selected not generated;
  JS MIT LICENSE SHA `182ac1d5`; **0★**; HEAD `1c687fc6`; README SHA `05730787`; size **0** WITH CONTENTS);
  ([ZeroX-01/jev-atlas](https://github.com/ZeroX-01/jev-atlas)
  ZeroX-01/jev-atlas ≠ Zaious/jev-capability-atlas ≠ gorock007/jev-atlas;
  catalog not endorsement;
  JS; license null; **0★**; HEAD `bc94bf50`; README SHA `8dd3d308`; size **0** WITH CONTENTS);
  ([samyakjain0606/jev-is-here](https://github.com/samyakjain0606/jev-is-here)
  flopcheck 16 calibrated tweet judgments; mechanical tells in code;
  TS; license null; **0★**; HEAD `eb0de0ba`; README SHA `cefb8f96`; size **0** WITH CONTENTS);
  (hfspace:BunsDev/laya-calibration-lab
  Laya calibration lab Gradio MCP; T never changes argmax;
  confidence ≠ top-label p; easy probe set refused;
  40–48 rows too small to ship T; apache-2.0; likes **0**; sha `a3fc13ba`).
  0★ HIGH still got a real card. Soft Noul ≠ hard safety.
  `invented_signal: false`.

- Hourly 0243 HIGH (`research/notes.md` §107): **Skip
  Archer rewrite.** Docs-only on a **fresh PR off main**.
  **HARD RULE:** do not reopen or amend PR #23 or #24 (merged
  #23 owns `notes.md` §105 / items 149–160 / batch #88;
  merged #24 owns `notes.md` §106 / items 161–177 / batch #89 —
  leave them alone). Never reopen merged
  #7–**#24**. Do **not** re-fold 0145 / §106 / 0042 / §105 / 2340 / §104 / 2246 /
  §103 / 2145 / §102 / 2041 / §101 / 1943 / §100 / 1843
  / §99 / 1740 / §98 / 1639 / §96 / gliner-native-runtime
  / §97 / 1541 / §95 / jev-align *mechanism* / §93 /
  jev-orderby-bench *six-gates* / §60 / JevBench v1.2
  *board* / §78 / openJev-verdict *claim-audit* / §71. How-to-apply / mental models /
  architecture / Harbor-jevals / toolbelt — not a thin
  Jev skill dump. Backend-agnostic
  categorization/scoring/decision class. Formal methods
  compose with scoring; a Noul is a SENSOR; treating a
  0.85 figure FAST_PATH as a proof, 100/100 easy T/F as
  Harbor, label_mass as correctness, 77.10% as beating
  Jev, collapsing ticket-router into Sarath, collapsing
  jev-bench into jevbench, collapsing DeBERTa ONNX into
  the Qwen scorer ONNX, collapsing Hub/GH Nicolai
  spellings, treating 151M vs 149.6M as two models,
  quoting 62.3% cost save without the 4.5pp miss,
  treating mock keyword as production, hard-gating
  ticket 0.6 as safety, treating a study mock as a live
  API, treating stock llama.cpp Q2_0 as working, or
  re-folding §71 as a beat is soundness theater.
  Figure-router 0.85 hard-gate and 100/100 easy T/F as
  Harbor are the anti-patterns. Eight HIGH clusters /
  three themes:
  **measurement densifies PRIMARY**
  ([erendikmenn/jev-llm-router-benchmark](https://github.com/erendikmenn/jev-llm-router-benchmark)
  Benchmark-driven Jev router and judge; cheap alone is not success;
  Jev does not write, sum prices, or claim accuracy %;
  Sol 94.2 / Luna 83.9 / Jev path 89.7;
  19.2% Sol / 62.3% cost save / 4.5pp miss of 2pp non-inferiority;
  p50 latency worse than Sol due to routing overhead;
  erendikmenn/jev-llm-router-benchmark ≠ jev-rag-benchmark ≠ ryantsai/jev-llm-router;
  Python MIT LICENSE SHA `99916677`; **0★**; HEAD `f44ef450`; README SHA `df3687e5`; size **0** with contents);
  ([aesaganda/jev-ticket-router](https://github.com/aesaganda/jev-ticket-router)
  Express + node:sqlite; mock and Jev decision engines;
  previous_ticket_count >= 3 is code; MIN_CONFIDENCE 0.6 still soft;
  substring false positives;
  aesaganda/jev-ticket-router ≠ SarathChandraBellam/jev-vs-llm-ticket-router;
  JS; license null; **0★**; HEAD `ecf00046`; README SHA `41c0b50f`; size **0** with contents);
  ([hoangngochuong24947-gif/jev-figure-router](https://github.com/hoangngochuong24947-gif/jev-figure-router)
  Universal Figure & Diagram Router; confidence ≥ 0.85 hard-gate is theater;
  generative AI banned from scientific plots; six visual branches;
  Python MIT LICENSE SHA `62120c23`; **1★**; HEAD `4c51b1af`; README SHA `11d5302b`; size **340**);
  (hfdataset:Praveenrajus/jev-bench
  human-labeled (state, question, label); 166,054 rows / 22 configs;
  soft_label for human uncertainty;
  Praveenrajus/jev-bench ≠ fstandhartinger/jevbench;
  license other; likes **0**; sha `c9c3032c`);
  **open reproduction class ports**
  (hf:NicolaiMTLassen/open-bonzi-jev
  ternary bonsai System One GGUF; openjev's mechanism, Bonsai's weights;
  Hub does not ship weights; 100/100 easy T/F is not Harbor;
  label_mass ≠ correctness; stock llama.cpp Q2_0 silently gibberish;
  NicolaiMTLassen/open-bonzi-jev ≠ NicolaiLassen;
  MIT; likes **0**; sha `09240156`;
  GH companion NicolaiLassen/open-bonzi-jev Python MIT; **0★**; HEAD `1c2508fd`; LICENSE SHA `46d740e4`; size **0** with contents);
  (hf:onnx-community/open-jev-deberta-v3-large-ONNX
  transformers.js DeBERTa ONNX; source:com-kotobalabs/open-jev-deberta-v3-large;
  temperature 1.05; AutoModel from_pretrained works;
  onnx-community/open-jev-deberta-v3-large-ONNX ≠ system-one-qwen3.5-4b-scorer-ONNX;
  apache-2.0; likes **0**; sha `3bc2553b`);
  ([Heman10x-NGU/openJev-verdict-2.0](https://github.com/Heman10x-NGU/openJev-verdict-2.0)
  107★ densify; GH 151M vs README 149.6M; PR #1 now closed unmerged;
  do not re-fold §71 claim-audit as a beat;
  Python; README Apache-2.0 / GitHub SPDX NOASSERTION; **107★**; HEAD `a458733c`; README SHA `05ca75af`; size **14728**);
  **study densification**
  ([wjdjdakf17/jev-study](https://github.com/wjdjdakf17/jev-study)
  typed decisions, RLCD, confidence-gated routing; structured ≠ correct;
  mock not live API; 26 tests; wjdjdakf17/jev-study ≠ baekenough/jev-study;
  TypeScript MIT LICENSE SHA `00bbf5f9`; **0★**; HEAD `24b5d7d7`; README SHA `4ca30c93`; size **34**; default **master**).
  0★ HIGH still got a real card. Soft Noul ≠ hard safety.
  `invented_signal: false`.

- Hourly 0145 HIGH (`research/notes.md` §106): **Skip
  Archer rewrite.** Docs-only on a **fresh PR off main**.
  **HARD RULE:** do not reopen or amend PR #23 (merged
  #23 owns `notes.md` §105 / items 149–160 / batch #88 —
  leave it alone). Never reopen merged
  #7–**#23**. Do **not** re-fold 0042 / §105 / 2340 / §104 / 2246 /
  §103 / 2145 / §102 / 2041 / §101 / 1943 / §100 / 1843
  / §99 / 1740 / §98 / 1639 / §96 / gliner-native-runtime
  / §97 / 1541 / §95 / jev-align *mechanism* / §93 /
  jev-orderby-bench *six-gates* / §60 / JevBench v1.2
  *board* / §78. How-to-apply / mental models /
  architecture / Harbor-jevals / toolbelt — not a thin
  Jev skill dump. Backend-agnostic
  categorization/scoring/decision class. Formal methods
  compose with scoring; a Noul is a SENSOR; treating a
  Jevify two-liner as a checkpoint, collapsing Jevify
  into Mintzs or gulagala001, pasting Colvin as hyusi,
  treating JSON parse as a Noul, quoting 46x / 91.1% /
  92.58% / 84.8 as class ceilings, treating
  classifier.dev #1 as a better model, re-folding §78
  as new, letting Jev do budget arithmetic, treating
  XState as Jev, pasting catalog ★ as eval, treating
  SPLADE as TypeSafe Jev, or treating an empty
  consistency Space as a win is soundness theater.
  Jevify stub and JSON-parse-as-Noul are the
  anti-patterns. Seventeen HIGH clusters / four themes:
  **architecture probes PRIMARY**
  ([uspraveen/Jevify](https://github.com/uspraveen/Jevify)
  Turn any open LLM into System-One Jev;
  uspraveen/Jevify ≠ Mintzs/jevify ≠ gulagala001/jevify;
  Jevify-any-LLM architecture probe; description-only stub / size 0;
  license null; **0★**; HEAD `0f29d783`; README SHA `32608473`);
  ([Ruivalim/exu-base](https://github.com/Ruivalim/exu-base)
  Train encoder-only calibrated decision models from a task sentence;
  Exu is a toolkit, not a method; strictly proper scoring rule; Pre-alpha;
  Python MIT LICENSE SHA `336cde4c`; **1★**; HEAD `7288cdca`; README SHA `45244838`; size **180**);
  ([Colvin0315/MiniSystemOne](https://github.com/Colvin0315/MiniSystemOne)
  scratch-trained calibrated decision model; typed Q → probability dists;
  Colvin0315/MiniSystemOne ≠ hyusi2003/MiniSystemOne;
  no published weights download URL; 90.5 seconds / 29.2% pipeline evidence;
  p_i/p_j independent of other candidates;
  Apache-2.0 LICENSE SHA `261eeb9e`; **0★**; HEAD `d7f9f803`; README SHA `a5b0d2fd`; size **814**);
  ([scienthoon/luce](https://github.com/scienthoon/luce)
  Recipe for calibrated decision models — small model out;
  init → synth → train → eval → serve; 91.1 % / ECE 0.022 *theirs*;
  Jev zero-shot 75.1; Apache-2.0 LICENSE SHA `d6456956`; **1★**; HEAD `8072b97d`; README SHA `5fbe226d`; size **10833**);
  ([RichardoMrMu/jev-mini](https://github.com/RichardoMrMu/jev-mini)
  Put Jev's three headline claims on trial; 0.5B local GPU;
  46x speedup / accuracy identical; ECE 0.624 sentiment catastrophe;
  bigger model worse calibration;
  RichardoMrMu/jev-mini ≠ yuki-oshio/mini-jev ≠ r-ms/mini-jev;
  Python MIT LICENSE SHA `cbdf24bb`; **0★**; HEAD `5adef5dc`; README SHA `154ae8b0`; size **0** with contents);
  ([tapsin/jev-local](https://github.com/tapsin/jev-local)
  System-1 decision engine for local LLMs; structured choices only;
  JSON parse of generated text ≠ Noul; TypefAI JEV / Journal Entry Voucher;
  tapsin/jev-local ≠ us/jev-local ≠ Argos1111/jev_local;
  Python; license null; **0★**; HEAD `96aac2a1`; README SHA `4d728cbf`; default **master**; size **0** with contents);
  **measurement densifies**
  ([goya4140/jev-reward-model-evaluation](https://github.com/goya4140/jev-reward-model-evaluation)
  Jev 1.13 reward-model eval across 8 benchmark tracks;
  40,940 examples / 0 API errors; RewardBench v1 92.58%; Precise IF 50.63%;
  Python MIT LICENSE SHA `4588ffe5`; **0★**; HEAD `f16a06d1`; README SHA `603587fd`; size **0** with contents);
  ([SarathChandraBellam/jev-vs-llm-ticket-router](https://github.com/SarathChandraBellam/jev-vs-llm-ticket-router)
  Jev vs LLM support-ticket routing; Scaffolding in progress;
  license null; **0★**; HEAD `0318ad72`; README SHA `8223dd6f`; default **master**; size **0**);
  ([Shilin237/jev-vs-llm-cost](https://github.com/Shilin237/jev-vs-llm-cost)
  static + live decision bench; TypeSafe's own published benchmark;
  illustrative simulations, not live API calls;
  HTML; license null; **0★**; HEAD `2d4bd6a9`; README SHA `f4e98bbf`; default **master**; size **0**);
  ([fstandhartinger/jevbench](https://github.com/fstandhartinger/jevbench)
  JevBench v1 — smart/cheap/fast/reliable; I/C/S/K 25% geometric mean;
  classifier.dev fast tier 84.8 is Jev behind its own API;
  do not re-fold §78 v1.2 board as new; Laya (421M) 70.1 now on board;
  Python MIT LICENSE SHA `ebdd5738`; **6★**; HEAD `c7ab99f5`; README SHA `8fe07c41`; size **8907**);
  ([AIGNLAI/ReflexRoute](https://github.com/AIGNLAI/ReflexRoute)
  Zero-shot/few-shot LLM routing; hard budget filter before Jev;
  Jev never asked to perform budget arithmetic;
  Python MIT LICENSE SHA `1be8631e`; **1★**; HEAD `5f475d80`; README SHA `6a1ae694`; size **0** with contents);
  ([priyankark/jev-state](https://github.com/priyankark/jev-state)
  Jev judges the next state, XState enforces transitions;
  simulation uses synthetic keyword fixtures;
  TypeScript MIT LICENSE SHA `78745387`; **0★**; HEAD `c73aef65`; README SHA `15410dbe`; size **0** with contents);
  (hfspace:mjyoke1111/jev-consistency-benchmark
  Consistency benchmark Space; This Space contains no benchmark result yet;
  12-case plumbing fixture; apache-2.0; likes **0**; lastModified `2026-09-20T05:29:45Z`);
  **catalog gravity**
  ([v-modal/awesome-jev-tools](https://github.com/v-modal/awesome-jev-tools)
  catalog gravity; ★339 live REST; curation is not endorsement;
  license null; **339★**; HEAD `f117e0c3`; README SHA `8ea9a669`; size **83**);
  ([RadRebelSam/awesome-jev](https://github.com/RadRebelSam/awesome-jev)
  crawler-maintained directory; Daily GitHub + npm sweep, human-merged;
  RadRebelSam/awesome-jev ≠ AnotiaWang ≠ yibie ≠ cobanov ≠ logicrw ≠ v-modal;
  SPDX NOASSERTION LICENSE SHA `2aa7fe23`; **0★**; HEAD `27629954`; README SHA `21ec8d51`; size **919**);
  **HF class ports**
  (hf:rdxtremity/jev-reranking
  HF peft SPLADE/BGE reranker; rdxtremity/jev-reranking ≠ carlaiau/jev-reranking;
  query-side encoders, not a Jev replica; apache-2.0; likes **0**; sha `cae796ea`);
  (hf:onnx-community/system-one-qwen3.5-4b-scorer-ONNX
  ONNX System One Qwen3.5-4B scorer; source:pngwn/system-one-qwen3.5-4b-scorer;
  CC-BY-NC-4.0; temperature 1.75; transformers.js AutoModel cannot load this graph;
  likes **0**; sha `fa0bed22`).
  0★ HIGH still got a real card. Soft Noul ≠ hard safety.
  `invented_signal: false`.

- Hourly 0042 HIGH (`research/notes.md` §105): **Skip
  Archer rewrite.** Docs-only on a **fresh PR off main**.
  Never reopen merged #7–**#22**. Do **not** merge from
  merged **#22** (hourly 2340 / §104). Do **not** re-fold 2340
  / §104 / 2246 / §103 / 2145 / §102 / 2041 / §101 / 1943 / §100 /
  1843 / §99 / 1740 / §98 / 1639 / §96 /
  gliner-native-runtime / §97 / 1541 / §95 / jev-align
  *mechanism* / §93. How-to-apply / mental models /
  architecture / Harbor-jevals / toolbelt — not a thin
  Jev skill dump. Backend-agnostic
  categorization/scoring/decision class. Formal methods
  compose with scoring; a Noul is a SENSOR; treating
  displayed p as proof, schema-valid ordinary-model JSON
  as a calibrated Noul, collapsing gulagala001/jevify into
  Mintzs/jevify, quoting 40.3% without the constant-answer
  baseline, hard-gating fastloop confidence as safety,
  treating fan-out 0.0000 sd as universal determinism,
  treating 2.95× RL as Harbor, hard-gating Laya cascade
  0.60, collapsing locate into decide, treating snake
  points as intelligence, treating jevcheck as a
  correctness proof, treating `no_direct_evidence` as
  merge-safe, or treating a theme Choice as a music-theory
  certificate is soundness theater. Hard-gating a soft
  Noul as safety is the anti-pattern. Unique consecutive fragments: structured probability readouts; distribution > argmax; Noul 0.5 midpoint; score is expectation not integer; bare HTTP not SDK; Arohtea/jev-readout; Jev-style Choice/Score/Noul from ordinary models; optional DSH plugin; schema-valid ≠ calibrated; gulagala001/jevify ≠ Mintzs/jevify; Laya RLCD benchmark; 40.3% below constant-answer; open-weight measurement; mourad-ghafiri/laya-rlcd-benchmark ≠ yibie/laya-jev-lab; cheap fail-open semantic edge; second signal not sole; FastLoopError catch; SupremeDreamZ/jev-fastloop ≠ jev-ultrafast; asking more questions in one call; 0.980 at every N; nearly not fully deterministic; TheWebDevel/jev-fanout; Qwen3-VL perception + Jev decisions train RL; 0 model calls at deployment; VLM alone 1.7 vs +Jev 4.4; harneet2512/reflexrl ≠ khordoo/jev-reflex-autonomy-lab; independent Jev API vs Laya; cascade 0.60 matches 78% at 1.8×; noul facts not judgements; yibie/laya-jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab; GLiNER vs GLiFormer vs Laya vs Jev; extractors ≠ decision engines; Laya dict-instructions collapse 58.3%; umstek/zero-shot-ie-bench; decisions-per-minute & cost; 204 moves vs 73; throughput not intelligence; angelgalvisc/snake-arena-jev-vs-llms ≠ vtrivedy/jev-plays-games; behavioral contracts; pin expectations eval upgrades; raw 0.94 is not a release; sathariels/jevcheck ≠ dayhaysoos/jevals ≠ SivletLabs/jev-eval; evidence-linked dependency upgrade; Jev never generates filenames; no_direct_evidence ≠ safe to merge; GaneshVG18/upgrade-radar ≠ LYchoon/paper-radar-jev; discography theme/mood/complexity; five atomic questions one call; lirantal/discoprint. Twelve HIGH
  clusters: **structured probability readouts**
  ([Arohtea/jev-readout](https://github.com/Arohtea/jev-readout)
  PRIMARY; structured probability readouts; distribution >
  argmax; Noul 0.5 midpoint; score is expectation not
  integer; bare HTTP not SDK; JavaScript; license null;
  **0★**; HEAD `6f1e5900`; README SHA `67ee1e96`);
  **ordinary-model Jev-shape**
  ([gulagala001/jevify](https://github.com/gulagala001/jevify)
  Jev-style Choice/Score/Noul from ordinary models;
  optional DSH plugin; schema-valid ≠ calibrated;
  gulagala001/jevify ≠ Mintzs/jevify; JavaScript MIT;
  **0★**; HEAD `3d3e904a`; README SHA `0e2f8536`);
  **open-weight Laya measurement**
  ([mourad-ghafiri/laya-rlcd-benchmark](https://github.com/mourad-ghafiri/laya-rlcd-benchmark)
  Laya RLCD benchmark; 40.3% below constant-answer;
  open-weight measurement;
  mourad-ghafiri/laya-rlcd-benchmark ≠ yibie/laya-jev-lab;
  Python; license null; **0★**; HEAD `3401ff26`; README SHA
  `d8d4859e`);
  **cheap fail-open semantic edge**
  ([SupremeDreamZ/jev-fastloop](https://github.com/SupremeDreamZ/jev-fastloop)
  cheap fail-open semantic edge; second signal not sole;
  FastLoopError catch; SupremeDreamZ/jev-fastloop ≠
  jev-ultrafast; Python MIT; **0★**; HEAD `1157841a`;
  README SHA `053a0885`; GitHub size **12** (relock; was
  **0** with contents));
  **fan-out measurement**
  ([TheWebDevel/jev-fanout](https://github.com/TheWebDevel/jev-fanout)
  asking more questions in one call; 0.980 at every N;
  nearly not fully deterministic; Python MIT; **0★**; HEAD
  `b30aaadc`; README SHA `394b2e1e`; GitHub size **206**
  (relock; was **0** with contents));
  **VLM+Jev RL teacher**
  ([harneet2512/reflexrl](https://github.com/harneet2512/reflexrl)
  Qwen3-VL perception + Jev decisions train RL; 0 model
  calls at deployment; VLM alone 1.7 vs +Jev 4.4;
  harneet2512/reflexrl ≠ khordoo/jev-reflex-autonomy-lab;
  Python MIT; **0★**; HEAD `aa36be84`; README SHA
  `e6ff13cd`; default master; GitHub size **749** (relock;
  was **0** with contents));
  **independent Jev API vs Laya**
  ([yibie/laya-jev-lab](https://github.com/yibie/laya-jev-lab)
  independent Jev API vs Laya; cascade 0.60 matches 78% at
  1.8×; noul facts not judgements; yibie/laya-jev-lab ≠
  dairui1/jev-lab ≠ BrendanH18/jev-lab; Python MIT; **0★**;
  HEAD `30ba64dc`; README SHA `57bd1832`);
  **locate vs decide**
  ([umstek/zero-shot-ie-bench](https://github.com/umstek/zero-shot-ie-bench)
  GLiNER vs GLiFormer vs Laya vs Jev; extractors ≠
  decision engines; Laya dict-instructions collapse 58.3%;
  Python MIT; **0★**; HEAD `8770b16b`; README SHA
  `d69dc96a`);
  **throughput arena**
  ([angelgalvisc/snake-arena-jev-vs-llms](https://github.com/angelgalvisc/snake-arena-jev-vs-llms)
  decisions-per-minute & cost; 204 moves vs 73; throughput
  not intelligence; angelgalvisc/snake-arena-jev-vs-llms ≠
  vtrivedy/jev-plays-games; Python MIT; **0★**; HEAD
  `985a1c70`; README SHA `0db6f528`);
  **behavioral contracts**
  ([sathariels/jevcheck](https://github.com/sathariels/jevcheck)
  behavioral contracts; pin expectations eval upgrades;
  raw 0.94 is not a release; sathariels/jevcheck ≠
  dayhaysoos/jevals ≠ SivletLabs/jev-eval; Python MIT;
  **0★**; HEAD `fc49c795`; README SHA `5c832f81`);
  **evidence-linked upgrade review**
  ([GaneshVG18/upgrade-radar](https://github.com/GaneshVG18/upgrade-radar)
  evidence-linked dependency upgrade; Jev never generates
  filenames; no_direct_evidence ≠ safe to merge;
  GaneshVG18/upgrade-radar ≠ LYchoon/paper-radar-jev;
  TypeScript MIT; **0★**; HEAD `e438f9bd`; README SHA
  `c32f7d18`);
  **knowledge-work discography**
  ([lirantal/discoprint](https://github.com/lirantal/discoprint)
  discography theme/mood/complexity; five atomic questions
  one call; TypeScript Apache-2.0; **0★**; HEAD
  `a9d3294f`; README SHA `9a64f473`). Soft Noul ≠ hard
  safety. 0★ HIGH still got a real card (all twelve
  **0★**). Census **live REST pulse** (independent review
  relock after `0558f7d`): SemIf **2069★** (+22 vs §104 **2047**); jevlike
  **1022★** (+4 vs §104 **1018**); TypeAR **12★** **flat**.
  Tracker likes **59** (+3 vs §104 **56**); lastModified
  `2026-09-20T04:29:16Z` **UNCHANGED** vs §104. Hub
  `archerhume/4rcherhume` HTTP **401**. Archer still NOT
  landed. Laya Hub likes **705**. Blackwood Hub likes **2**
  gated manual — user census absent from tracker. Awesomejev
  561/27007 user-provided (≠ AnotiaWang/awesome-jev
  **92★** ≠ yibie/awesome-jev **450★**). Qwen3.8-27B ≠ Archer (likes **15796**).
  `invented_signal: false`. Do not copy keys / `npm` /
  `pip` / `npx` / `uv` / `.env`. No wrapper. No invented
  metrics. Relock: Arohtea HEAD `03734993`→`6f1e5900` /
  README `76a99fe5`→`67ee1e96`; upgrade-radar HEAD
  `1e91eb03`→`e438f9bd` / README `b7603c01`→`c32f7d18`;
  discoprint HEAD `c2a3d47e`→`a9d3294f` / README
  `392efd29`→`9a64f473`; yibie/laya-jev-lab size **49**
  (was **0** with contents); umstek size **50** (was
  **33**); jev-fastloop size **12** (was **0** with
  contents); jev-fanout size **206** (was **0** with
  contents); reflexrl size **749** (was **0** with
  contents); upgrade-radar size **908** (was **0** with
  contents); gulagala001/jevify size **145** (was **0**
  with contents); mourad size **164** (was **0** with
  contents); discoprint size **239** (was **0** with
  contents); Arohtea size **44** (was **0** with
  contents). Design claims unchanged.
- Hourly 2041 HIGH (`research/notes.md` §101): **Skip
  Archer rewrite.** Docs-only on a **fresh PR off main**.
  Never reopen merged #7–**#18**. Do **not** re-fold 1943
  / §100 / 1843 / §99 / 1740 / §98 / 1639 / §96 /
  gliner-native-runtime / §97 / 1541 / §95 / jev-align
  *mechanism* / §93. How-to-apply / mental models /
  architecture / Harbor-jevals / toolbelt — not a thin
  Jev skill dump. Backend-agnostic
  categorization/scoring/decision class. Formal methods
  compose with scoring; a Noul is a SENSOR; treating a
  zero binary name gap as a fairness certificate, letting
  Jev emit the verdict string, pasting PrismNLI's lead
  without the contamination caveat, treating J7 pass as
  safe to obey, treating a receipt as authorization, or
  hard-gating confidence ≥0.95 is soundness theater. Nine
  HIGH clusters: **resume-screening bias audit**
  ([natemoo-re/bias-bench](https://github.com/natemoo-re/bias-bench)
  PRIMARY; name×resume factorial independent Nouls;
  callback determined by resume quality; mean-probability
  name gaps operationally negligible; natemoo-re/bias-bench
  ≠ BBQ; JavaScript; license null; **0★**; HEAD
  `fe2f2535`; README SHA `a1c3e604`); **MCDA panel
  code-owned verdict**
  ([austindixson/planalyzer](https://github.com/austindixson/planalyzer)
  Plan/PRD panel → code-owned pass|review|block;
  cheerleading out of scope; Python MIT; **0★**; HEAD
  `39fc161f`; README SHA `6e4d8da3`); **EU cost-aware
  routing**
  ([cannacre8ive/switchboard-ai](https://github.com/cannacre8ive/switchboard-ai)
  cost-aware multi-model routing/escalation; decide vs do;
  successful-task cost; JavaScript MIT; **1★**; HEAD
  `5cae9d1c`; README SHA `872de837`; package **0.4.0**);
  **frozen-protocol class bake-off**
  ([elcronos/jev-vs-open-decision-models](https://github.com/elcronos/jev-vs-open-decision-models)
  TypeSafe Jev vs PrismNLI vs Laya; contamination caveat;
  Python; license null; **0★**; HEAD `b61e6cfc`; README
  SHA `b7256888`); **VOI admission**
  ([cvsgireesh/jevusher](https://github.com/cvsgireesh/jevusher)
  context-window admission control; fail polarity per
  lens; on small inputs lenses lose money; TypeScript MIT;
  **0★**; HEAD `d830d344`; README SHA `428a4a59`);
  **Leveson control plane**
  ([MokiMeow/jev-fabric](https://github.com/MokiMeow/jev-fabric)
  typed decision control plane; receipt ≠ authorization;
  historical-v0 zero retained cases; Apache-2.0; **0★**;
  HEAD `95b9a4f3`; README SHA `f485dbdd`); **scoring
  economics**
  ([jose-troche/live-rubric](https://github.com/jose-troche/live-rubric)
  live 15-dim typed rubric re-score per pause; OpenJev/Codiv
  ≠ TypeSafe hosted; ~$0.000004 desc / ~$0.000006 README;
  TypeScript; license null; **0★**; HEAD `db8da8db`;
  README SHA `4a0be084`); **pre-registered calibration
  science**
  ([willkelly/jev-evaluation](https://github.com/willkelly/jev-evaluation)
  28 predictions before data; 123,805 requests; confidence
  does not track ignorance; polite injection 65% / crude
  0%; Python MIT; **0★**; HEAD `c168c093`; README SHA
  `2d66ac22`; rh-guard owns injection); **class
  infrastructure SDK**
  ([nshkrdotcom/system_one_sdk](https://github.com/nshkrdotcom/system_one_sdk)
  provider-neutral Elixir/BEAM Noul/Choice/Score SDK;
  GitHub desc provider-neutral / README TypeSafe-first;
  Elixir MIT; **0★**; HEAD `c2a522ee`; README SHA
  `c117b4c4`; mix **0.5.0**). Soft Noul ≠ hard safety.
  0★ HIGH still got a real card (switchboard now **1★**
  live REST). Census **live REST pulse**: SemIf **1984★**;
  jevlike **1002★**; TypeAR **11★** flat. Tracker likes
  **54** (+3 vs §100 pin **51**); lastModified **CHANGED**
  2026-09-20T02:59:13Z; Hub `archerhume/4rcherhume` HTTP
  **401** (not re-fetched as a rewrite). Archer still NOT
  landed. Awesomejev 561/27007 user-provided (≠
  AnotiaWang/awesome-jev 84★).
  `invented_signal: false`. Do not copy keys / `npm` /
  `pip` / `npx` / `uv` / `mix`. No wrapper. No invented
  metrics.
- Hourly 1943 HIGH (`research/notes.md` §100): **Skip
  Archer rewrite.** Docs-only on a **fresh PR off main**.
  Never reopen merged #7–**#17**. Do **not** re-fold 1843
  / §99 / 1740 / §98 / 1639 / §96 / gliner-native-runtime
  / §97 / 1541 / §95 / jev-align *mechanism* / §93.
  How-to-apply / mental models / architecture /
  Harbor-jevals / toolbelt — not a thin Jev skill dump.
  Backend-agnostic categorization/scoring/decision class.
  Formal methods compose with scoring; a Noul is a SENSOR;
  hard-gating `feels` 80%, pasting 17/18 as Harbor,
  hard-gating 0 of 157, treating boolean @ 0.5 as a proof,
  claiming 10×, treating softmax as a Noul, or treating 62
  tests as quality is soundness theater. Six HIGH clusters:
  **Jev IS the if-statement**
  ([southpolesteve/probably](https://github.com/southpolesteve/probably)
  PRIMARY; judgments/probabilities drive branches; text
  model only writes prose; interpreter owns
  variables/loops/budgets/replay; otherwise maybe /
  confidence gate; chaos samples after the gate;
  southpolesteve/probably ≠ carldaws/hunch ≠ feelings ≠
  Kungie/gut ≠ Illusion47586/judge ≠ tidymodels/probably;
  TypeScript MIT; **3★**; HEAD `6bf671a4`; README SHA
  `c28570a9`); **GEPA live delta**
  ([sutro-sh/jev-align](https://github.com/sutro-sh/jev-align)
  133★ / forks 10 live; build calibrated classifiers from
  human feedback; HEAD `49753df9` / README SHA `363fccb7`
  unchanged vs §93); **retrieve by relevance not
  resemblance**
  ([samdotmak/jev-recall](https://github.com/samdotmak/jev-recall)
  one calibrated yes/no per memory in one request; pointer
  mode 17/18 19/20 *theirs*; embedding resemblance misses
  the allergy; MIT; **6★**; HEAD `d3e4acfb`; README SHA
  `ea774519`); **memory leases ended by new evidence**
  ([chopratejas/invalidate](https://github.com/chopratejas/invalidate)
  HIGH upgrade; six Nouls then fixed rules in code; 0 of
  157 false invalidations; questions/plans/directives are
  not evidence; unsure → review queue; host keeps the
  store; Apache-2.0; **11★**; HEAD `d6ade601`; README SHA
  `8cccad5f`); **contract-of-artifact lint rename**
  ([mizchi/jev-lint](https://github.com/mizchi/jev-lint)
  is mizchi/jevlint rename; name↔body / comment truth /
  test-claims; no shipped rule has severity error; ~1 in 5
  findings wrong *theirs*; TypeScript MIT; **13★**; HEAD
  `62d73f8e`; README SHA `4c0e37cd`); **JSON Schema
  question compiler**
  ([Kiln-AI/jev_jsonschema](https://github.com/Kiln-AI/jev_jsonschema)
  HIGH upgrade; JSON Schema → typed JSON via Jev;
  noul_threshold 0.5 decoder not a proof;
  IncompatibleSchemaError lists every bad property; MIT;
  **5★**; HEAD `fccea8c2` unchanged); **local System One
  economics**
  ([mizorewww/laya-coreml](https://github.com/mizorewww/laya-coreml)
  on-device Laya CoreML ANE; ~5 ms P50 short decisions;
  189/189 FP16 checkpoint parity; 10× not achieved;
  Apache-2.0; **0★**; HEAD `47f4baf0`; README SHA
  `2068c661`) +
  ([Micha0827/snapjudge](https://github.com/Micha0827/snapjudge)
  softmax over allowed tokens ≠ Noul; question-first
  cache; Python MIT; **3★**; HEAD `2df5ce27`; README SHA
  `64a91458`) +
  ([direwolfiy/JevPi](https://github.com/direwolfiy/JevPi)
  Jev-first Pi agent loop; slow-LLM fallback; explicit
  action menu / CandidateSource unimplemented; 62 tests
  wiring not quality; license null; **0★**; HEAD
  `980f8895`; README SHA `88ec1a55`). Soft Noul ≠ hard
  safety. 0★ HIGH still got a real card. Census **live
  REST pulse**: SemIf **1954★**; jevlike **989★**; TypeAR
  **11★** flat. Tracker likes **51** flat; lastModified
  UNCHANGED 2026-09-19T18:37:18Z; Hub
  `archerhume/4rcherhume` HTTP **401** (not re-fetched as
  a rewrite). Archer still NOT landed. Awesomejev
  561/27007 user-provided (≠ AnotiaWang/awesome-jev 83★).
  `invented_signal: false`. Do not copy keys / `bun` /
  `pip` / `npx` / `uv` / HF download. No wrapper. No
  invented metrics.
- Hourly 1843 HIGH (`research/notes.md` §99): **Skip
  Archer rewrite.** Docs-only on a **fresh PR off main**.
  Never reopen merged #7–**#16**. Do **not** re-fold 1740
  / §98 / 1639 / §96 / gliner-native-runtime / §97 /
  1541 / §95. How-to-apply / mental models /
  architecture / Harbor-jevals / toolbelt — not a thin
  Jev skill dump. Backend-agnostic
  categorization/scoring/decision class. Formal methods
  compose with scoring; a Noul is a SENSOR; hard-gating
  cost-derived 0.038 as a proof, merging von Needle
  52.6% with n=78 93%, “guaranteeing” calibration, or
  pasting “Jev wins guardrailing” is soundness theater.
  Five HIGH clusters: **cost-derived YES/NO/UNSURE
  control flow**
  ([Kungie/gut](https://github.com/Kungie/gut)
  PRIMARY; cost-sensitive decision theory × System One
  probabilities → control flow; thresholds derived from
  costs not hard-coded; YES / NO / UNSURE from
  cost_false_yes / cost_false_no / cost_human;
  auto-batching same-object questions; Kungie/gut ≠
  tpellet/hunch ≠ carldaws/hunch; GitHub Apache-2.0 /
  LICENSE MIT / pyproject Apache-2.0 *theirs*; **0★**;
  HEAD `cb56c875`; README SHA `630474f6`; pre-alpha);
  **typed-callback twin**
  ([Illusion47586/judge](https://github.com/Illusion47586/judge)
  judgment vs generation; deterministic execution after
  probabilistic judgment; exactly one app-owned
  callback; explicit uncertain branch;
  Illusion47586/judge ≠ lexingtonhibiki/judgekit ≠
  Ascurse/typed-judge-kit; TypeScript MIT; **0★**; HEAD
  `e69f65a1`; README SHA `08554c6f`; `@brkn-labs/judge`
  0.1.0); **variable-N option scoring as the trainable
  object**
  ([zwliJay/jev-forge](https://github.com/zwliJay/jev-forge)
  dynamic candidate bags not fixed label sets;
  zwliJay/jev-forge ≠ NanoJev; class-architecture note,
  not a sixth species; GitHub NOASSERTION / LICENSE MIT;
  **1★**; HEAD `eb3e4a2d`; README SHA `359f3f57`; do not
  clone Hub weights); **open NAR replica economics**
  ([wfzyx/von](https://github.com/wfzyx/von) late-catch
  HIGH of the same repo; NAR local drop-in; open replica
  economics / latency vs closed Jev; competing NAR
  claims / replica honesty; Apache-2.0; **43★**; HEAD
  `b9e42b26`; README SHA `574aa628`; do not merge Needle
  52.6% with n=78 93.0%); **typed vs chat judges on
  guardrailing**
  ([ishaannk/llm-vs-jev](https://github.com/ishaannk/llm-vs-jev)
  cross-note only; nothing wins outright; can be argued
  out of guarding; deeper integrity fold is rh-guard;
  Apache-2.0; **0★**; HEAD `182e0864`; README SHA
  `d9ebd40f`). gut/judge are **control-flow /
  decision-theory overlays, not new class-table
  species**. Soft Noul ≠ hard safety. 0★ HIGH still got
  a real card. Census **live REST quoted**: SemIf
  **1936★**; jevlike **983★** (watch claimed 984);
  TypeAR **11★** flat. Tracker likes **51** flat;
  lastModified UNCHANGED 2026-09-19T18:37:18Z; Hub
  `archerhume/4rcherhume` HTTP **401**. Archer still NOT
  landed. Awesomejev 561/27007 user-provided (≠
  AnotiaWang/awesome-jev 83★). X MCP `since_id` held;
  pages_archived 0; no invented tweets.
  `invented_signal: false`. Do not copy keys / `pip` /
  `npm` / `uv` / Hub download. No wrapper. No invented
  metrics.
- Effect-oriented loops (`notes.md` §28, `mappings.md` §19): Ward's
  ZIO client keeps Jev as the outer Choice and the handler as the
  effect. Not Effect.ts. GLiNER author: GLiNER2 "like jev" is GLiGuard
  schema-conditioned categorize, not a Noul.
- Boundary-audit stop conditions for TOCTOU-of-Noul and vacuous specs;
  FAQ rows for Alloy vs Apalache and PufferLib-as-DST-trio
- Research pointer to [dayhaysoos/jevals](https://github.com/dayhaysoos/jevals):
  local MIT workbench for Jev questions vs labeled Noul/Choice/Score cases
  (compare runs, WebMCP + agent skill). Empirical acceptance-test surface
  for Hypothesis mapping cards; complements `evaluate_decisions.py`. Not a
  jevals how-to (`research/notes.md` §24; one sentence in `validation.md`)
- Mental-models card: Augustus is design judgment across AI, SWE,
  business, knowledge work, and life — not SWE-only. Pillars: expected
  utility / selective classification, calibration and cost-sensitive
  thresholds, VOI, MCDA, search/control substitutions, signal detection,
  Leveson org/safety, NATM/snap-fit/Norman/Kent/Shirky as general
  intuition. Domain gallery labeled Hypothesis except launch-week
  Empirical SWE rows.
- Archer Hume architecture reconstruction (17 Sep 2026 essay, ~10k
  probes of `jev-1.13.0`): direct readout vs generated confidence,
  isolated questions, listwise IIA and order sensitivity, confidence as
  arithmetic on the distribution. Independent envelope probe; does not
  override live TypeSafe docs. Announced open-weight drop is **WATCH**
  (27B dense, AU healthcare residency, prefers "decision models"; still
  no Hub weights). `research/notes.md` §31, §33; `judgment-class.md`
  when-to-use table; FAQ confidence / surfaces questions.
- Entropy as allocator (**Hypothesis**, `judgment-class.md`): Atallah's
  low / medium / high buckets place System One on typed decisions and a
  frontier decoder on high-entropy synthesis — same axis as marginals
  vs joint and as VOI. "Review this PR" as medium is still partly
  generative; "first model ever" is a claim. `research/notes.md` §38
- Marginals, not a probabilistic program (`judgment-class.md`, FAQ):
  Erik Meijer — Jev is a cool API and not a PPL; Kleisli qualifications
  exaggerate; "Jev gives you the marginals; a decoder gives you the
  joint." Joints and invariants stay with TLA+ / Alloy / contracts.
  `research/notes.md` §34
- Bespoke Nimble: open contrastive recipe, not a Jev distill. Model
  card Apache-2.0 LoRA on Qwen3.5-9B (repo license absent). Their
  324-example holdout is a named receipt (Nimble 90.12%, Jev 1.13.0
  93.21%), not a ranking. 9B-vs-Jev on your labels stays Hypothesis.
  `research/notes.md` §35; one sentence in `validation.md`
- djev-spark: third compute graph (diffusion structured reads,
  Jev-shaped I/O, image-in). Empirical as the public interface;
  Hypothesis that it beats a decision head on your task. Archer's
  multimodal drop stays WATCH. `research/notes.md` §36
- Perception specialist then judgment specialist vs shared multimodal
  System One (**Hypothesis**): SAM 3.1 (masks and tracks) or an ASR
  transcript, then typed decisions on that state, is an application
  pattern, not native omni. Information dies at the interface. Prefer
  a shared multimodal decision model when the joint matters (Archer
  Watch, not Empirical; djev-spark images; future audio). Basit ask,
  primary post not retrieved. `research/notes.md` §39
- Perception→decision pipeline, measure, and hill-climb
  (**Hypothesis**, `validation.md`): stages with a versioned state
  contract; stage metrics plus a frozen taskset; HoH changes one stage
  or one interface. DSPy/Ax only on LM-program knobs; jevals and
  calibration for the decision slice; Harbor names product
  end-to-end, not a tutorial. `research/notes.md` §41
- Eval & hill-climb (`validation.md`): jevals decision-stage hygiene
  (independent keys, correctness is not confidence, held-out, immutable
  runs) and Harbor as the product taskset substrate; one composition
  table. `research/notes.md` §40

### Changed

- Skill description rewritten as trigger conditions (mixed architecture,
  prefilter, routing, preference lint, classification skepticism, family
  choice including GLiNER/GLiClass/listwise/vision) plus an explicit `not_for`
  against the official `typesafe-ai` skill
- Identity lock vs neighbor skills (`typesafe-ai`, `tenbin`, `decision-first`)
  so Augustus stays the design-judgment layer — class-wide, not TypeSafe-only
- Design cards name hole, family, and typed judgment provider (Jev default;
  other family only with self-eval)
- Protocol fan-out step is family-aware (Jev batch, GLiClass one-pass,
  dual-encoder prompt scoring); ranking vs decision fail policy is a
  non-negotiable
- Protocol and FAQ branch for "formally verify with Jev"; methods-catalog
  and composition-algebra verifier position point at the ownership split
- Skill mission and description are domain-general (AI / SWE / business /
  knowledge work / life); FAQ "is this only for software?"; mappings.md
  beyond-SWE examples labeled Hypothesis; boundary-audit red flags for
  TOCTOU-of-Noul and vacuous specs; formal-methods expanded with Alloy vs
  Apalache and the DST trio including PufferLib; GLiNER promoted from
  cousin footnote to species-map peer

### Fixed

Adversarial review of the whole skill against its own non-negotiables
(findings in `research/notes.md` §27).

- Gate fail policy is per action, not universally open
  (`composition-algebra.md` position 3, `agent-self-assessment.md`):
  advisory guards fail open *because* an interlock sits underneath;
  selection and authorization gates fail closed
- Dual-orchestration topology A selects from a closed catalog instead of
  "planning" MCP calls, which contradicted the standing planner rejection
- Species map applied to the skill's own advice: GLiClass (categorize) is
  the large-catalog substitute for a 255-option Choice; GLiNER spans are
  not (`SKILL.md`, `judgment-class.md`, `applied-mappings.md`)
- Han Xiao trolley relabeled an Empirical **rejection** (one tweet, no
  repo), not a recipe
- openjev-lm caveat moved to the figure it belongs to: 92.9% is against 70
  hand-labelled gold, 98.1% is teacher *agreement*
- Contract surface removed from design cards: the Ax constructor call and
  the `instructions` key enumeration point at live docs instead
  (`optimizer-integration.md`, `question-design.md`)
- `mappings.md` preamble no longer claims uniform Hypothesis where card
  bodies say Contract/Empirical; §17 forbids reusing jevgate's ≤0.18 as a
  constant; all Hypothesis-range references aligned to §6–§19
- Ownership split labeled Contract in `toolbox-mapping.md`, matching
  `mappings.md` §8; done-check splits structure from the Noul

Second pass on `7b3a0c3` (`research/notes.md` §43). Zero blockers.
Dropped the unpublished `npx jevals` line; SAM and ASR are upstream
producers, not the perceive species; removed two call shapes from
`optimizer-integration.md`; tagged the $0.042/MTok cell as a vendor
figure; marked GodsBoy 94.4% exploratory.
- Skill description gained trigger terms for boundary audit, question
  diagnosis, agent self-supervision, and optimizer placement

## [0.2.0] - 2026-09-18

Pegged against [`typesafe-ai/skills` v0.5.7](https://github.com/typesafe-ai/skills/tree/v0.5.7)
(`65a39f3`, 2026-09-12).

### Added

- Boundary-audit card for existing systems: three-way split (exact /
  bounded judgment / generation), code-smell catalog, fit test, opportunity
  map, smallest-viable-boundary rule, Jev-around-LLM sandwich, centralized
  policy + raw-judgment retention, red flags, completion questions
- Protocol branch: audit a codebase/PR before inventing mappings; per-action
  risk gates; keep questions/thresholds in one reviewable module
- Skill description trigger terms for brittle parsers, prompt-to-JSON
  classifiers, and agent loops that are really bounded decisions

## [0.1.0] - 2026-09-18

Pegged against [`typesafe-ai/skills` v0.5.7](https://github.com/typesafe-ai/skills/tree/v0.5.7)
(`65a39f3`, 2026-09-12) — the only tagged revision of the official skill at
Augustus launch.

### Added

- Skill protocol, decision-design card, and evidence labels (Contract /
  Empirical recipe / Hypothesis)
- Classical-method mappings: features/utility, selective decisions, decision
  circuits, bounded rerank, hierarchy/beam search
- Agent self-assessment, optimizer coupling (Ax, DSPy, ProgramAsWeights)
- Toolbox sweep, named-methods catalog, 11-position composition algebra,
  question-design diagnosis
- Validation gates and `scripts/evaluate_decisions.py`
- Launch-week evidence archive (187 repos) and public ecosystem index
- Claude Code marketplace manifest; public GitHub mirror at
  [`24601/Augustus`](https://github.com/24601/Augustus)

### Research log (pre-tag)

The dated passes below are how 0.1.0 was assembled.

### 2026-09-18 (refresh pass 2)
- Research: Gemini Deep Research report retrieved and archived (interaction ID
  saved in jev-archive/state); GitHub census doubled to ~60 Jev repos +
  framework integrations (LiteLLM, LangChain, Vercel AI, Mastra, Eliza, Ax,
  Composio); all 87 repos cloned to /home/user/workspace/jev-archive for
  hourly refresh.
- New measured recipes added to notes.md: foreman supervision loop, pi-jev
  gate thresholds, pi-warden 6→0 paired-run result, winnow relevance sieve,
  fast-jev-compaction two-noul rule, skill-router gates (0.30/0.40, shortlist
  3, 94.4% vs 70.8%), calibration ECE 0.0313 vs 32% OOD collapse (Archer
  Hume), Every 777-judgment eval, Near Here moderation numbers.
- Skill: added references/agent-self-assessment.md (agent self-supervision
  lifecycle, grounding/citation checks, skill callability testing) and two
  mapping-index rows; validation.md dogfooding section still canonical.

### 2026-09-17/18 (initial)
- Baseline research archive (sources.json, notes.md), augustus skill with
  mappings + validation references, evaluator script, hourly refresh script,
  Claude plugin marketplace manifest.

### 2026-09-18 (topic-index pass 3)
- Fixed census method: exact GitHub search paginated (700 repos created since
  09-14 captured; 700-result cap noted) + topics/jev crawl → ~80 additional
  repos; archive now 184 clones. Miss-cause documented: earlier star-sorted
  limit-40 search cut the low-star tail (incl. both MCTS repos).
- Skill: MCTS mapping promoted experimental → empirical recipe (grounded vs
  speculative fidelity in types; probes-only concession; measured 24/24 vs
  1/24 greedy); agent-self-assessment.md gains the judge-variance recipe
  (Jev judge 224-279x more consistent than LLM judge over 100 reps).

### 2026-09-18 (pass 4 — optimizers + official skills + clone audit)
- ax Jev support documented from source (native adapter details, trueThreshold
  semantics, fail-closed mapping validation); new reference
  optimizer-integration.md covering Ax + DSPy typesafeify + jev-dspy-lab.
- typesafeainate/dspy-typesafeify cloned; official typesafe-ai/skills already
  archived and layered-on (never duplicated).
- Clone audit: repos.txt deduped (185 unique), 0 missing on disk, no failures.

### 2026-09-18 (pass 5 — toolbox sweep meta-method)
- New references/toolbox-mapping.md: the how-to-find-approaches-and-
  applications procedure (judgment-shaped-hole substitution, newly-feasible
  classification via economics inversion, standing rejections list); wired
  into SKILL.md central model + index row.

### 2026-09-18 (pass 6 — named-methods + operators/theorems tier)
- references/methods-catalog.md: ~20 named algorithms (CatBoost row is
  Empirical via autoresearch cookbook) + operators/theorems tier with
  precondition-carrying rule; wired into SKILL.md index and toolbox sweep.

### 2026-09-18 (pass 7 — composition algebra as application generator)
- references/composition-algebra.md: 11-position grammar of Jev-vs-construct
  relations, logical-operator combination rules, and the position×construct
  traversal as the systematic application generator; wired into SKILL.md
  index + toolbox sweep.
- Hourly 2340 HIGH (`research/notes.md` §104): **Skip
  Archer rewrite.** Docs-only on a **fresh PR off main**.
  Never reopen merged #7–**#21**. Do **not** re-fold 2246
  / §103 / 2145 / §102 / 2041 / §101 / 1943 / §100 / 1843
  / §99 / 1740 / §98 / 1639 / §96 / gliner-native-runtime
  / §97 / 1541 / §95 / jev-align *mechanism* / §93 /
  jev-orderby-bench *six-gates* / §60. How-to-apply /
  mental models / architecture / Harbor-jevals / toolbelt
  — not a thin Jev skill dump. Backend-agnostic
  categorization/scoring/decision class. Formal methods
  compose with scoring; a Noul is a SENSOR; treating a
  description-only stub as a checkpoint, re-folding
  six-gates as new, distilling Jev as teacher of record,
  pasting openjev-sglang as OpenJevPro, treating
  constrained logprob as a Noul, quoting an
  untrained-looking demo as Jev identity, pasting a
  radar's listed numbers, or quoting 0.916 as a class
  ceiling is soundness theater. Distill-Jev UI stub and
  constrained-logprob-as-Noul are the anti-patterns.
  Eleven HIGH clusters: **from-scratch calibrated
  decision model**
  ([hyusi2003/MiniSystemOne](https://github.com/hyusi2003/MiniSystemOne)
  PRIMARY; train calibrated ~27M from scratch; typed Q→prob dist / one forward pass / no LLM decode;
  hyusi2003/MiniSystemOne ≠ Colvin0315/MiniSystemOne; description-only stub / size 5;
  Apache-2.0; **0★**; HEAD `4385335b`; README SHA `83016bf8`);
  **ORDER BY ranking upgrade**
  ([yodablocks/jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench)
  ESCI hard probe fails four of six; jev_bool ECE 0.242 inversion 0.255;
  do not re-fold §60 six-gates as new; jobbyjev one-request-per-company from batch-size result;
  Python MIT; **0★**; HEAD `52397954`;
  README SHA `7bd075c3`; size **309**);
  **find/design/evaluate decision loops**
  ([karanb192/jev-architect](https://github.com/karanb192/jev-architect)
  find/design/evaluate TypeSafe Jev decision loops; karanb192/jev-architect ≠ samtay32/jev-system-architect;
  HTML MIT; **0★**; HEAD `35ea6d93`; README SHA `68c2b5f9`; size **5199**);
  **distill-Jev UI stub**
  ([Jairik/jev-distiller](https://github.com/Jairik/jev-distiller)
  Jairik/jev-distiller size 1; distill-Jev UI stub / do not distill Jev as teacher of record;
  MIT; **0★**; HEAD `0589d44c`; README SHA `aa408c5e`);
  **post-launch scored opportunity map**
  ([licensedsaucer9-web/jev-opportunities](https://github.com/licensedsaucer9-web/jev-opportunities)
  post-launch scored use-case map / Jev self-scores then human curation;
  license null; **0★**; HEAD `a47fa414`; README SHA `aa33f901`; size **27**);
  **Jev-inize a use case**
  ([gavinHuang/jevinize](https://github.com/gavinHuang/jevinize)
  Jev-inize a use case into classifier/router; gavinHuang/jevinize → simple-jev not TypeSafe;
  featherless-ai/simple-jev;
  MIT; **0★**; HEAD `6d080632`; README SHA `5f48e622`; size **6**);
  **saved-decision regression**
  ([VihaanAgarwal/jev-diff](https://github.com/VihaanAgarwal/jev-diff)
  compare saved decisions / same label can still change the branch;
  VihaanAgarwal/jev-diff ≠ Saik0s/diffusiongemma-jev-macos;
  not tested with a live Jev API key; Python MIT; **0★**; HEAD `a3c98807`;
  README SHA `3b0ce75c`; size **120**);
  **constrained-logprob API**
  ([zhangcy122/OpenJevPro](https://github.com/zhangcy122/OpenJevPro)
  constrained logprob + temp/Platt ≠ Noul; OpenJevPro pastes openjev-sglang JevBench as own;
  zhangcy122/OpenJevPro ≠ IamBusy/OpenJev ≠ ekzhang/openjev-sglang;
  PolyForm Noncommercial; HTML; SPDX NOASSERTION; **0★**; HEAD `94d77bcb`;
  README SHA `50c77ace`; size **64** (relock; was **62**));
  **SmolLM RLCD reproduction**
  ([patelvishwa112/jev-system-one-rlcd](https://github.com/patelvishwa112/jev-system-one-rlcd)
  SmolLM-135M / sub-70ms / 0 output tokens; demo P(True) 0.5052 / Choice conf 0.2872 / Score conf 0.0055;
  README claims MIT / GitHub license null / no LICENSE file;
  patelvishwa112/jev-system-one-rlcd ≠ arnabgho/rlcd-lite ≠ blackwood-rlcd;
  Python; **0★**;
  HEAD `62b103b3`; README SHA `55994d69`);
  **source-backed Awesome radar**
  ([logicrw/awesome-jev-projects](https://github.com/logicrw/awesome-jev-projects)
  source-backed Awesome Jev radar / 306+ commit-pinned; auto GitHub sync / Issue-only submissions;
  logicrw/awesome-jev-projects ≠ AnotiaWang/awesome-jev ≠ yibie/awesome-jev ≠ cobanov/awesome-jev ≠ rupeshpoojary9/awesome-open-system-one;
  JavaScript MIT; **136★**; HEAD `97057cc1`; README SHA `25a19b31`; size **7677** (relock; was **7136**));
  **rival-aware one-pass scorer**
  ([olanotolu/jevbetter](https://github.com/olanotolu/jevbetter)
  hashed n-gram encoder / rival-aware attention; olanotolu/jevbetter vs jevlike starter;
  synthetic hard menus top-1 0.916 vs 0.873 / ECE 0.0182 vs 0.0367 / 40 vs 4608 menus/sec;
  shuffled-context control 0.335; Python MIT; **12★**; HEAD `bb0ebc82`;
  README SHA `5cbe01d4`; size **324**).
  Soft Noul ≠ hard safety. 0★ HIGH still got a real card
  (awesome-jev-projects **136★**; jevbetter **12★**). Census
  **live REST pulse**: SemIf **2047★** (+28 vs §103 **2019**);
  jevlike **1018★** (+12 vs §103 **1006**); TypeAR **12★**
  **flat**. Tracker `multimodalart/jev-reproductions-tracker`
  likes **56**; lastModified
  `2026-09-20T04:29:16.000Z`; Hub `archerhume/4rcherhume`
  HTTP **401** (not re-fetched as a rewrite). Archer
  still NOT landed. Awesomejev 561/27007 user-provided
  (≠ AnotiaWang/awesome-jev **91★** ≠ logicrw **136★**).
  Qwen3.8-27B ≠ Archer (likes **15787**).
  Independent adversarial review relock (PR #22
  after `babb111`): HIGH HEAD/README unchanged;
  star/size lag locked (awesome **136★**; SemIf
  **2047★**; jevlike **1018★**; AnotiaWang **91★**;
  OpenJevPro size **64**; simple-jev **318★**;
  openjev-sglang **205★**; RLCD size **1513**;
  Colvin size **814**; yibie **430★**; cobanov **224★**).
  `invented_signal: false`. Do not
  copy keys / `npm` / `pip` / `npx` / `uv` /
  `.env`. No wrapper. No invented metrics.
- Mixed-architecture card: default placement is judgment-class model +
  generator + code, not stack replacement. Covers cost-sensitive prefilter
  (fail-open vs fail-closed per action), tool/skill routing, AGENTS.md
  preference lint, a placement gallery from the 2026-09-18 X+GH hour, and
  an explicit answer to "Jev is just classification"
- Protocol branch and mapping-index rows for those four placements
- Non-negotiable: classification is not the product; typed judgment is a
  software primitive placed beside generation
- Hourly research archive for this pass (X theme digest + `topic:jev` movers)
  under `research/archive/hourly/2026-09-18T14/`
- Research note on Laya (`convaiinnovations/laya`): open Choice/Score/Noul
  head as a self-hosted *typed judgment provider*; vendor benches labeled
  claims; TypeSafe remains the default path
- Applied-mapping cards: context sieve, exact-text keep/drop, env/harness
  triage, moderation/ranking, skill/tool routing (`applied-mappings.md`)
- FAQ card for "it's just classification", stack replacement, Jev vs open
  head, and Augustus vs neighbor how-to skills
- Judgment-class card: Augustus covers the whole class of fast/cheap
  categorization-classification-scoring models (Jev is exemplar, not
  monopoly). Families: closed decision API, open System-1 heads (Laya),
  GLiNER/GLiClass encoder family (locate vs categorize vs local
  multi-head), listwise/pairwise rankers, vision scorers.
  Species map in `judgment-class.md`; GLiNER is a peer, not a footnote.
  Fork of listwise discriminative vs decision/proper-scoring objectives;
  four vision scoring patterns; seven portents for agent architecture.
  FAQ rows for family choice, GLiNER vs GLiClass vs Jev vs cross-encoder, and
  CLIP/SigLIP gating. No invented APIs.
- Formal-methods card: judgment vs proof ownership (sensor / constraint /
  searchlight); Alloy Analyzer vs Apalache (model finder ≠ SMT BMC ≠
  inductiveness); TLA+/Quint/P/NuSMV/PRISM/Event-B; Dafny/JML/
  Frama-C/SPARK; DST trio (Antithesis hypervisor, Resonate Lean+oracle+
  SDK, PufferLib env+seed / Ocean trainer contracts); harms
  (TOCTOU-of-Noul, soundness theater, AI×FM / Hillel vibing specs);
  crossover metaphors (NATM, snap-fit, Norman gulfs, Leveson STAMP/STPA).
  Curriculum archived at `research/archive/curriculum/FORMAL-METHODS-SYSTEM-ONE.md`;
  named rows folded here. One-screen alias: `formal-semi-formal.md`.
  Non-negotiable: never launder a Noul as a proof.
- One-screen `references/formal-semi-formal.md` (curriculum 1-pager)
- Hypothesis mapping cards (do not promote without an acceptance test):
  VOI / gather; SDT/ROC; Leveson sensor≠constraint; search/control
  outside SWE; spec property pipeline; Alloy instance loop; runtime
  assurance sandwich; DST multiverse triage; durable agent control;
  assignment hybrid; situated density (`mappings.md` §6–§16)
- Input-brittleness and structural-prove ∩ remainder cards
  (`mappings.md` §17–§18): paraphrase pairs → Chow abstain; allowlist /
  text-layer first, judge leftovers (jevgate / doc-router *shapes*
  Empirical; domain-general reading Hypothesis). FAQ: GLiNER vs Jev,
  LLM-as-judge (Langfuse framing), allowlist-then-judge
- GLiGuard as an Empirical encoder peer (`judgment-class.md`,
  `notes.md` §30): one-pass safety-schema classify on GLiNER2, not a
  Jev weight clone; FAQ "is GLiGuard Jev?"; README OR/refusal
  aggregation left as existing policy-in-code. LLM I/O safety is not
  a coding-agent tool gate
- Hourly 10:07 Boise fold (`research/notes.md` §25–§26): GLiNER2.5 local
  peer; openjev-lm 92.9% / 6 vCPU teacher-distill; jevgate; doc-router
  1.74× $; pi-jev-context; jevscope next to jevals; Han Xiao trolley
  (listwise ≠ decide); James Ward dual orchestration; JevLint
- Constrained-AR surface, not a sixth species (`judgment-class.md`):
  TypeAR puts a typed interface on a pretrained generator (next-token
  constraint ≠ proper-scoring head). Archer Hume's open-weight drop
  stays **Watch** (`research/notes.md` §31, §32)
- Hourly ~11:02 Boise fold (`research/notes.md` §33): Archer
  clarifications still Watch (27B dense one-forward-pass, multimodal
  generalization report, AU healthcare residency not anti-TypeSafe,
  prefers "decision models"); when-to-use table (proprietary Jev vs
  Archer vs TypeAR vs encoder DeBERTa vs LoRA distill); HF novel
  (jev-gate-student-b 148k corpus, jp-sns-jev7 ONNX, open-jev-deberta,
  mini-jev-runs 27.9k logits, jev-tree-choice-cap); device/harness
  (jev-mobile MCP, jev-macos-loop, jev-harness, routeKit); HacksonClark
  SREGym-Lite 20/50→24/50 — rank tests, do not diagnose
- Hourly ~11:59 Boise fold (`research/notes.md` §42): Archer still
  Watch. Three open paths (encoder / AR constrained decode / trained
  decision-only). Native constrained serving
  ([pcdServer](https://github.com/stephanj/pcdServer), TypeAR-class,
  2–256 enums, Apple+Linux GGUF). Meta-VOI hook
  (typesafe-jev-tools 149-row: Haiku more accurate, Jev confidence
  monotonic). jev-mode latency-class split (token ratio durable;
  accuracy is parity). OpenSmoke env-break vs policy-break +
  pre-mortem. jevql store-as-decision-surface. jot topology B with a
  closed catalog. openevals online full-traffic. hermes north-star
  two-layer finish gate. pi-jev (not pi-jev-context). jev-plays-games
  option-order probe. joxide jump-by-description. laya-typed-decisions
  companion packaging. No wrapper.
- Hourly ~12:58 Boise fold (`research/notes.md` §44): Archer still
  Watch (no architecture rewrite). Store-index fork: in-engine
  ([sqlite-jev](https://github.com/mgaitan/sqlite-jev), pg-jev cousin)
  vs CLI rewrite (jevql). Soft judgment inside a hard envelope
  ([bitrate-advisor](https://github.com/affirmitv/bitrate-advisor);
  mmalisper JOB planner +12% geomean, author-reported; join-order
  Choice alone was 2× slower). Distill-to-device as a *memory* gate
  (jev-gate, already §33). Encoder vs decoder open-replica receipts
  (openjev-lm $0/call overnight CPU). jev-harness as Harbor-adjacent
  practice (assert on action). Host adapter
  ([jev-routing](https://github.com/nekowasabi/jev-routing), not MCP);
  OpenClaw typed routing ([jev-claw](https://github.com/trietphan/jev-claw)).
  Voice-control and JevML are README stubs. Higgsfield auto-routing is
  a claim. No wrapper.
- kev (`jaredpalmer/kev`, `research/notes.md` §45): runnable Archer
  reconstruction on the trained decision-only open path next to Laya /
  Nimble / Watch. Qwen2.5-0.5B LoRA + pointer, Apache-2.0, `POST
  /v1/systemone` drop-in. Isolation exact (packed vs separate max Δ
  3.7e-6; secret-in-sibling p=0.03 vs in-state 0.99). Held-out ECE
  0.065 (0.031 after temp scale); acc 0.799 on 1,350 ID questions.
  Permute argmax flips 7.4%; IIA log-odds shift mean 0.13; boundary
  forgery held. Laptop-local System One for development/eval; not a
  knowledge/frontier substitute; not a Jev teacher-copy. Contrast vs
  TypeAR, encoder DeBERTa, proprietary Jev. jevals/Harbor bake-off
  candidate. No serve how-to.
- Hourly ~14:03 Boise fold (`research/notes.md` §46): Archer still
  Watch. Open multimodal RLCD
  ([blackwood-rlcd](https://huggingface.co/BlackwoodAI/blackwood-rlcd),
  CC BY-NC): screenshot + marked candidates → Choice; web acc 0.907 vs
  Jev 1.13 text-only 0.480; letter-shuffle 0.133 vs 0.587; ECE 0.037;
  ~200 ms H100; Jev still leads general text 0.850 vs 0.786. Shared
  bake-off ([open-jev-laya-bench](https://huggingface.co/datasets/pngwn/open-jev-laya-bench)):
  26+9 tasks, 11959 items; ECE/NLL/Brier; macro acc Δ +0.023
  neutral / +0.229 home; LLM-as-judge is not the score. Decision-token
  QLoRA
  ([Foodoo1/Qwen3-14B-RLCD-Decision-LoRA](https://huggingface.co/Foodoo1/Qwen3-14B-RLCD-Decision-LoRA)):
  fraud_risk 64→95%, overall 85.2→98.8% at ~234 ms/4-field broadcast;
  synthetic. jevgate frame: allowlist *proves*, Jev judges only
  unlisted, fail-open. wellposed: missing `other` → confidence 1.00
  wrong; gating cannot catch it (`tenbin` owns the lint skill).
  S1 reflex keeps control (jev-reflex-autonomy-lab). MED:
  jev-decision-layer, jev-e2e, jevpandas. No wrapper.
- Abide (`coldteadotai/abide`, `research/notes.md` §47): productized
  Jev preference lint for Claude Code / Codex / OpenCode. Soft
  AGENTS.md / CLAUDE.md rules → one Score per rule on the diff (never
  the conversation); hard rules stay with the linter (same layering
  family as jevgate). Edit- vs turn-phase observation window; banded
  confidence (≥0.8 repair / 0.5–0.8 note / <0.5 silence — their
  operating point) + fail-open hooks; rubric.json quotes source
  lines; calibrate/tune fix false positives in the question. Replay
  of 93 sessions (1,256 edits / 147 turns) with independent review:
  edit precision ~26%, turn ~73% (author-reported, before tune).
  Fuller productized path of the jev-pref contract. Complementary to
  rh-guard (eval-integrity vs project soft rules). Text/diff only —
  not multimodal. No hook how-to.
- kev delta (`research/notes.md` §45): Hub weights
  [`jaredpalmer/kev-0.5b`](https://huggingface.co/jaredpalmer/kev-0.5b);
  `--run` accepts Hub ids; PEFT `task_type=FEATURE_EXTRACTION` (publish
  patches legacy adapters). HIGH question-design: confront Choice
  `"other"` / none-of-the-above as a wrong alternative too, vary
  wording, dedicated `none_of_the_above` eval (no published rates).
  Cross-link wellposed request-shape lint. No species change. No
  wrapper.
- Hourly ~14:52 Boise fold (`research/notes.md` §48): Archer still
  Watch. Extractive selection + offline `redecide`
  ([testimonial-miner](https://github.com/AppitStudio/testimonial-miner));
  pointer-not-generator
  ([jev-reviewer](https://github.com/choxos/jev-reviewer)). Local
  `/v1/systemone` drop-in ([jev-local](https://github.com/us/jev-local);
  default scorer is a stub until `hf`). Observe→decide→verified-act,
  no screenshots ([solari-reflex](https://github.com/hitakshiA/solari-reflex);
  60.2/194.9, 66/460, 24.2/98.4 s vs Codex on Solari). Dataframe
  accessor sibling ([jevframe](https://github.com/ktaletsk/jevframe);
  note jevpandas). Route ≠ memory (jev-hermes). Advisory sidecar
  (agent-workflow-typesafe-ai). Structure induction (dag-jev experiment).
  Decision-for-control / generator-for-content (jev-agentworld-web-simulator).
  Collab arms + Wilson/McNemar (jev-testbench). AST ∩ semantic (jevscan;
  `tenbin` owns lint). Light Pi gate (pi-jev-approver). Laya ONNX port
  ([laya-onnx](https://huggingface.co/Mattepiu/laya-onnx); do not copy
  vs-Jev table). Spotcheck: SemIf 1551★; jevlike 866★; tracker
  20:12:57Z still lists Laya, not Blackwood. No wrapper.
- Hourly ~15:52 Boise fold (`research/notes.md` §49): Archer still
  Watch. X discourse blocked. Boundary map / extractable-from-state
  ([jev-capability-atlas](https://github.com/Zaious/jev-capability-atlas);
  history suite A wrong@0.90 / B 0.07 / C right@0.97; component node;
  dangerous-high ECE; DOM-as-text + fan-out). Harbor-style bake-off vs
  constrained LLMs
  ([DMB](https://github.com/nibzard/decision-model-benchmark) v2: jev
  banking 76.3% / spam 93.0% / 256+ cap; p50 264–276 ms; $0.07/1k; no
  class wins on quality). Feedstock
  ([jevals-data](https://github.com/Jevals/jevals-data) CC-BY-4.0;
  recompute-from-logs; 2026-09-18 board). Dual-process S1 decide / S2
  generate ([dual-process-ai](https://github.com/taro1985/dual-process-ai);
  routing accuracy unmeasured). Combinatorial ≠ extractive (ARC-AGI
  Direct Jev 4/400). Packed one-forward open LLM
  ([open-alternative-jev](https://github.com/ikermoel/open-alternative-jev)
  RACE-H 92.9% @ 4.55 q/s; not a Jev reproduction). Tiny SAN local
  surface ([von](https://github.com/wfzyx/von) 14 MB; not a replica).
  kev light delta **100★**. Do not merge Banking77 87% / 76.3% /
  79.67%. No wrapper.
- GLiNER2.5 extractive compaction (`research/notes.md` §50,
  [gliner25-compaction](https://github.com/m-newhauser/gliner25-compaction),
  Apache-2.0): architecture notes, not a plugin how-to. Pointer
  keep-drop (character-offset copies) vs generator summarizers;
  family with testimonial-miner / jev-reviewer. Soft retention Choice
  under a hard mutation envelope (mutating tools / shell operators →
  `keep_full`); low-confidence / invalid evidence fail closed to
  `keep_full` — contrast many fail-open Jev gates. Same compaction
  *job* as fast-jev-compaction / pi-jev-compaction; GLiNER encoder
  backend; Fastino/GLiGuard sibling class. `shadowMode` default true.
  Not Jev. Not multimodal. No invented metrics.
- CI merge-gate / fail-open wake VOI / S1 indexer / claim-evidence
  (`research/notes.md` §51): architecture notes, not a plugin how-to.
  [latch](https://github.com/CaseReed/latch) cluster-then-policy
  PASS/BLOCK (pair Harbor + rh-guard).
  [wakegate](https://github.com/shitianfang/wakegate) skip only if
  p(wake)<0.2 (21/21 smoke). s1-graphify-indexer GLiNER extract +
  escalate-S2 (10–50× unfilled).
  [clear-head](https://github.com/VladyslavHontar/clear-head)
  claims vs session evidence.
  reification-labs/foreman description-only Phoenix scaffold (not the
  super-jev loop).
  [jev-gateway-bench](https://github.com/vinilana/jev-gateway-bench)
  Harbor on/off one-run signal.
  jev-marshal Watch/empty; jevons bounded Pi supervisor (shadow
  recovery). MED: if-ai, omp-auto-mode, downloads-sorter, label-desk,
  herdr-jev. Archer still Watch. No invented metrics. No wrapper.
- GLiNER2 Ultrafast observe→score→act (`research/notes.md` §52,
  [gliner2-ultrafast](https://github.com/sahibzada-allahyar/gliner2-ultrafast),
  MIT): architecture notes, not a browser-agent how-to. Same
  observe→score-among-candidates→code-acts *job* as jev-ultrafast /
  solari-reflex; local GLiNER2 (`fastino/gliner2-multi-v1`) backend,
  not GLiNER2.5. No screenshots; no generated selectors; code owns
  actuators. Hybrid local decide + remote fill (Mercury 2.5 default
  for TYPE). `DONE` ≠ verified success. Contrast blackwood-rlcd
  screenshot multimodal; laya-mind2web is DOM-index Laya (same
  observed-candidate family). Fastino sibling class with
  gliner25-compaction (different hole) and GLiGuard (safety schema).
  Demo (theirs, not re-run): Flights 12.20 s / 13.785 s / ~$0.0001
  API — demonstration, not a bake-off. No invented metrics.
- jev-pruner evidence-preserving Bash stdout prune (`research/notes.md`
  §53, [jev-pruner](https://github.com/tamaratran/jev-pruner), MIT):
  architecture notes, not a plugin how-to. After Bash, Jev Noul-prunes
  stdout chunks before the main LLM sees them — no summary. Hard
  envelope (≤10k estimated tokens / JSON-diff-whole-doc untouched)
  then soft Noul; fail-safe keep original; full archive. Marketplace
  id still `fast-jev-output`. Codex is opt-in wrapper, not automatic
  interception. Same evidence-preserving *family* as
  fast-jev-compaction and gliner25-compaction; different *job*
  (command output vs session memory) and Jev backend vs GLiNER2.5.
  Manual sweep (theirs): needles 24/24; mean reduction 83% on trim
  scenarios. Harbor plugin-eval cannot reach Jev. Terminal-Bench
  paired pilot is integration, not a full bench. No invented metrics.
- Cua-S1 specialist System One computer-use (`research/notes.md` §54,
  [cua-s1](https://github.com/trycua/cua/tree/main/libs/cua-s1),
  parent MIT, ~23.3k★ this pass): architecture notes, not a Driver /
  MCP / `uv` how-to. Form-oriented profile `cua-s1-form-v0`. Byte
  encoder + option-attention head chooses fill/check/click/skip per
  observed element; does not generate values or selectors. Plan ≠
  execute; dry-run default; `execute`/`submit` independent opt-ins;
  fail-closed on unknown checkbox / fill without advertised token
  `set_value`. **Not TypeSafe Jev** — parallel "System One" naming in
  CUA research. Same observe→score-among-candidates→code-acts *job*
  as jev-ultrafast / gliner2-ultrafast / solari-reflex / laya-mind2web;
  specialist form contract, source-only this pass (no weights, no
  checkpoint scores). Offline metric *names* only (accuracy,
  abstention, coverage, wrong actions/targets, unsafe when should
  abstain). Tests exercise implementation, not checkpoint quality.
  Watch for a `cua-s1-form-v0` artifact drop. No invented metrics.
- Hourly ~17:48 Boise fold (`research/notes.md` §55): Archer still
  Watch. X MCP flap; `since_id` not advanced. Architecture notes, not
  a how-to. Local CUDA/PyTorch Choice/Score/Noul replica
  ([jevify](https://github.com/Mintzs/jevify); uncalibrated
  likelihoods ≠ Noul; no LICENSE this pass; independent of
  Distillation). Decision-native RAG
  ([decision-native-rag-skills](https://github.com/emergency-lee/decision-native-rag-skills);
  retrieve wide → decide → evidence set; no bundled harness; no
  universal benchmark). Verbatim session ledger + scored recall
  ([carryforward](https://github.com/Dharundp6/jev-carryforward);
  rules never judged; fail-open dump; 9×3 hint). Judgment as a
  Ruby language primitive ([hunch](https://github.com/carldaws/hunch);
  English-as-config; `rescue nil` fail-open at save). Healthcare
  Harbor-shaped S1+S2
  ([explore-typesafe-ai](https://github.com/si618/explore-typesafe-ai);
  synthetic FHIR; not clinically validated). Pre-registered
  independent eval
  ([jev-baselines-eval](https://github.com/ickma2311/jev-baselines-eval);
  **both AMBIGUOUS**; cascade sign-flip at exact parity;
  confidence=1.0 theater; encoder-with-labels wins; serving-path ≠
  model-speed; same-day errata ×3). Student-b light delta only (HF
  card unchanged). MED: toolgate (pre-exec allow/block/review; Jev
  not authorization), typesafe-screening-mcp (PubMed screening aid),
  databricks-jev-pdf-lab (**honest negative**; no OSS license),
  yannip1234/codex-jev (extractive compression family; equal
  accuracy/lower cost not established), kazuhideoki/jev-search
  (recursive *file* search + fzf; **not** superagents-lab web
  search). No wrapper. No invented metrics.
- Hourly ~18:38 Boise 2026-09-18 / 00:38 UTC 2026-09-19 fold
  (`research/notes.md` §56): Archer still Watch. Architecture
  notes, not a plugin / showcase catalog. Classify-first MCP
  ([jev-sift](https://github.com/kbhuw/jev-sift); batch path/url/text
  → Jev without entering main agent context first; 50 / 60k / 2MB /
  public-IP envelope; mocks ≠ accuracy; no LICENSE this pass;
  topology A MCP, not jev-routing). Living applied-mappings atlas
  ([jevable.com](https://jevable.com/); claimed 342 vs JSON-LD first
  page 36; class patterns — intent columns, score-among-observed,
  VOI gates, generative UI decide, robotics text-state, draft-gate
  silence ≠ safer — not a 342-title hit list). Maker clocks stay
  claims unless already a named receipt. No wrapper. No invented
  metrics.
- Stagehand experimental Jev stack (`research/notes.md` §57,
  [#2955](https://github.com/browserbase/stagehand/pull/2955) 5/5 of
  #2951–#2955, all OPEN draft): architecture notes, not an SDK
  how-to. Major harness productization of
  observe→score-among-candidates→code-acts (cousins jev-ultrafast /
  gliner2-ultrafast / cua-s1 / solari). Jev picks a11y elements;
  code copies text. extract `"off"` | `"judge"` | `"pick"`. Their
  card (gemini-3.8-flash, 25×3): **37/75** no-LLM ~0.5 s vs baseline
  **4.37 s**; 69/75 vs 23/25 (92% both); LLM-off **36/75** — pick is
  a fast path, not a replacement. Screenshot extract always LLM.
  Cache-check errors never block replay. Do not merge clocks. No
  invented metrics.
- Hourly ~18:46 Boise 2026-09-18 / 00:46 UTC 2026-09-19 fold
  (`research/notes.md` §58): Archer still Watch. Architecture
  notes, not a Convex / uv / pnpm catalog. Public judgment wall
  ([ask-jev-ai](https://github.com/waynesutton/ask-jev-ai); 6
  parallel questions; policy-in-code; cost-to-1M from tokens;
  license null). Meaning-search without embeddings
  ([jevgrep](https://github.com/Bentlybro/jevgrep); 79% top-5 vs
  BM25 40% / grep 20% on stripped repos; keyword still wins exact
  strings). PR attention ≠ correctness
  ([egma-ai/jev-reviewer](https://github.com/egma-ai/jev-reviewer);
  **not** choxos pointer-not-generator). Skills→oxlint
  ([jev-oxlint](https://github.com/cephalization/jev-oxlint);
  AST prove ∩ remainder; Phoenix fixtures; not a hard gate;
  `tenbin` owns lint). Session-sticky first-prompt routing
  ([jev-adaptive-thinking](https://github.com/jxu-dev-c/jev-adaptive-thinking);
  fail-closed fallback). Measured RAG rerank
  ([Jev-RAG](https://github.com/Max-sm-yc/Jev-RAG); one-run ≥70%
  cost / 72% latency vs Spark *rerank*; full-context Spark still
  faster). MED: safe-sh, jev-loan-triage, TurboGuo arenas, jevbox;
  hermes/mcp packs not found this pass. No wrapper. No invented
  metrics.
- Hourly ~19:48 Boise 2026-09-18 / 01:48 UTC 2026-09-19 fold
  (`research/notes.md` §59): Archer still Watch. Architecture
  notes, not a pip / venv / Cloudflare catalog. Capability kernel
  ([interlock](https://github.com/somoore/interlock); LLM ring 3 /
  kernel ring 0; secrets never in the agent; Jev SENSOR;
  `policy.py` BLOCK/ASK/ALLOW; type-safe ≠ correct; distinct from
  toolgate). Typed control plane around DSPy
  ([jev-dspy-control-plane](https://github.com/manikanda-kumar/jev-dspy-control-plane);
  DSPy drafts AFTER route+action; OpenJEV / DSPy / JSON Schema
  share ontology; offline heuristic ≠ quality). Native-probability
  calibration arena
  ([jev-arena](https://github.com/meetr1912/jev-arena); live 145
  noul Brier 0.0059 / ECE 0.0620 *theirs*; overconfident in low
  bins; 2-request fan-out) plus sonar (heatmap-as-policy) /
  vickrey (Jev never bids) / bracket (Brier vs Elo; live trailed
  Elo). Engine owns truth / Jev owns judgment
  ([game-coach](https://github.com/JoelLewis/game-coach); Wave 0
  PRD; Stockfish WASM; GPL-3.0; anti-soundness-theater with egma).
  Human-confirmed port cleanup
  ([port-cleanup](https://github.com/epiphany-dynamics/port-cleanup);
  Jev recommends; human is the only kill trigger; identity
  re-check; shields; mapped explanations). MED toolbelt:
  jev-pr-labeler, jevcumber, typedecide, jevon, dsh-jev,
  fast-jev-compaction-pi, jev-tetris-benchmark, modelsystem,
  opencode-system-one, browser-ai, semantic-bookmark. Skip
  jef-mcp (parody) and jevregist (account farming). Star spike:
  SemIf 1491→1606 (this pass 1607); jevlike 851→896 (this pass
  897). No wrapper. No invented metrics.
- Hourly ~20:43 Boise 2026-09-18 / 02:43 UTC 2026-09-19 fold
  (`research/notes.md` §60): Archer still Watch. Architecture
  notes, not a uv / bun / Modal catalog. Domain LoRA specialist
  vs few-shot hosted
  ([Domain-jev-maker](https://github.com/help-er/Domain-jev-maker);
  independent CLINC gold, not a Jev teacher-copy;
  matched-precision KL 0.168 vs 0.580 banking; few-shot
  determinate McNemar n.s.; train when downstream reads p).
  Decide→policy→LLM leftover cascade
  ([jav-email-cascade](https://github.com/skiingfalcon/jav-email-cascade);
  jev vs gen-json vs gen-logprob; Noul 0.5 never rounded;
  license null; mock gen-json flat-confidence is *their mock*).
  ORDER BY ranking family
  ([jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench);
  six gates pass; Score ordinal 0.143 weak link; 53-way 0.99
  tie; calibration ≠ sortable; recodelabs batch-40 fails
  ranking). Wire-compat GLiFormer backend
  ([jeff](https://github.com/logan-markewich/jeff); typesafe-sdk
  drop-in; ~$2.6 vs $15.6 L4 HTTP ~6×; A10G direct ~$0.65 ~24×;
  AG News 75.5% vs 90.5%; CPU more expensive; license null; not
  a Jev replica). MED: loopback gateway
  ([sysone](https://github.com/hraness/sysone); hosted + local
  OpenJev/NanoJev/Mini-Jev; no weights; credential from env).
  No wrapper. No invented metrics.
- Hourly ~21:39 Boise 2026-09-18 / 03:39 UTC 2026-09-19 fold
  (`research/notes.md` §61): Archer still Watch. Architecture
  notes, not a pip / npm / bun catalog. Active-learning triage
  ([jev-triage](https://github.com/ThyFriendlyFox/jev-triage);
  accept / expensive teacher / human; log full distributions;
  **do not distill Jev as teacher of record**, ~68% ceiling).
  Evidence-packet explorer
  ([jev-semantic-explorer](https://github.com/jimmyhealer/jev-semantic-explorer)
  / jevex; index-once ask-many; 1/8→6/8 SWE-bench Verified
  finish n=8 *theirs*; packet HitFile 0.233 diagnostic).
  Meaning-grep
  ([jev-semgrep](https://github.com/uehaj/jev-semgrep); AND/OR/NOT
  line Nouls; JP↔EN; MIT LICENSE / GitHub NOASSERTION; 0.94/0.98
  *theirs*). Closed-vote CU
  ([JevOnly](https://github.com/buluoray/JevOnly); no planner LLM;
  11 steps / 43 calls / ~$0.014 / 17 s *theirs*). Harbor Jev vs
  local MLX PCD vs AR JSON
  ([system-one-benchmark](https://github.com/mallahyari/system-one-benchmark);
  toxic-chat n=50; Jev 84.0% / Brier 0.1096 vs PCD 52% / 0.3884;
  O(1) ≠ calibrated Noul; license null). Host-owned product
  ([waymode](https://github.com/mossburgh/waymode); app retains
  handlers/permissions; 24/26 + 34/36 *theirs*; not a
  self-driving proof). OMP/pi fail-open gates
  ([omp-jev-extensions](https://github.com/luw2007/omp-jev-extensions);
  `jev_acceptance_gate` + `jev_route`; contrast pi-jev-approver
  fail-closed). Skip empty jev-compactor / laya-jolt. No wrapper.
  No invented metrics.
- Hourly ~22:38 Boise 2026-09-18 / 04:38 UTC 2026-09-19 fold
  (`research/notes.md` §62): Archer still Watch. Architecture
  notes, not an `omp plugin` / pip catalog. Watch archive path
  missing on this VM; receipts from live GitHub. Permission vs
  probability
  ([omp-greenlight](https://github.com/SemetricLabs/omp-greenlight);
  1,013 calls / 10 sessions; default **40.9%** prompts removed /
  **0 of 94** unsafe auto-approvals on labelled corpus; operator
  owns thresholds; plugin never self-tunes; not a sandbox; host
  deny stays above). Judgment ≠ permission
  ([skill-broker](https://github.com/adamjralph/skill-broker);
  Hermes pre-agent outline; code owns grants; Jev never grants
  access; **not a production recipe**). Eval integrity /
  instrument-not-score
  ([dinostomp](https://github.com/collapseindex/dinostomp);
  FINDINGS 189 / 99 against itself; `dinostomp jev` if-statement
  hygiene; ECE 0.062 *theirs* on 24 examples; beside jevals, not
  a Harbor taskset). MED: fast-jev-opencode, jev-desktop,
  jev-agent-integration, sift, JevExplore. Census: Awesomejev
  488/21644; SemIf 1641 (+13); jevlike 905 (+4); tracker likes
  41 (+1); Laya yes; Blackwood ABSENT; X MCP flapping
  (`pages_archived` 0). No wrapper. No invented metrics.
- Hourly ~23:40 Boise 2026-09-18 / 05:40 UTC 2026-09-19 fold
  (`research/notes.md` §63): Archer still Watch. Architecture
  notes, not a uvicorn / bun / marketplace catalog. Watch
  archive path missing on this VM; receipts from live GitHub +
  HF. Hunches labeled. Constrained optimizer + S1 features
  ([slo-router](https://github.com/zeeshan8281/slo-router);
  license null; Jev task/exactness/evidence as features, never
  the sole hot-path gate; fail-open local features; same
  routes/accuracy; p95 **77.93 → 490.38 ms** *theirs*; eight-row
  demo is not a benchmark). Privilege ≠ verdict
  ([construct-auto-classifier](https://github.com/godspede/construct-auto-classifier);
  Apache-2.0; effect-based shell gate; fast-allow/deny then Jev
  Choice + independent risk Nouls; fail-closed; Jev **0**
  dangerous / 975; every chat model leaked 16–104; operator-owned
  dials). Attention filter / VOI for human review
  ([jev-lens](https://github.com/rashedInt32/jev-lens) +
  [jev-lens.nvim](https://github.com/rashedInt32/jev-lens.nvim);
  never blocks the agent; never edits; never green unless sure).
  MED: [sysone-help/sysone](https://github.com/sysone-help/sysone)
  (evaluation-model-first TS SDK; **not** hraness/sysone gateway);
  [INSTRUCT_JEV](https://huggingface.co/datasets/ctaxnagomi/INSTRUCT_JEV)
  (119 rows; 47/51/21; jevals seed);
  [swift-jev](https://github.com/ckaik/swift-jev) (LICENSE-only
  this pass; not a CLI product). Census: Awesomejev 488/21644;
  SemIf **1652** (+11); tracker likes **42** (+1); lastModified
  unchanged; Laya yes; Blackwood ABSENT; X MCP flapping. No
  wrapper. No invented metrics.
- Hourly ~00:39 Boise 2026-09-19 / 06:39 UTC fold
  (`research/notes.md` §64): Archer still Watch. Architecture
  notes, not a uvx / pnpm / marketplace catalog. Watch
  archive path missing on this VM; receipts from live GitHub.
  Hunches labeled. Measurement owns endorsement
  ([jev-packs](https://github.com/dtduc-git/jev-packs);
  CC0; nine packs `verified` *theirs* on pinned
  `jev-1.13.0`; accuracy/ECE/cost/latency; `unknown`
  mandatory; named runner jevassert **not released** / 404;
  packs without evidence stay `provisional`). Jev supplies
  evidence, code owns authority
  ([actiongate-jev](https://github.com/omkarghugarkar007/actiongate-jev);
  Apache-2.0; deterministic policy owns ALLOW|REVIEW|BLOCK;
  positive score never overrides a hard security fail;
  fail-closed financial/destructive/credential if Jev is
  down; 500-case is label-baseline, not accuracy). Ranking ≠
  calibration
  ([does-jev-confidence-mean-anything](https://github.com/Adilmp/does-jev-confidence-mean-anything)
  + [jevcal](https://github.com/Adilmp/jevcal); 8,000
  human-annotated judgments; AUC **~0.91**; stated **~75%**
  vs human **~10%**; two-parameter recalibration removes
  **~96% ECE** without changing rank; never hard-threshold
  raw p as a frequency; vendor "calibrated" often means
  rank-correlation). MED:
  [gqgs/laya-onnx](https://github.com/gqgs/laya-onnx)
  (complete Laya→browser int8; distinct from Mattepiu);
  [kunchenguid/local-jev](https://github.com/kunchenguid/local-jev)
  (ModernBERT local approximation — not equivalence). Do
  not re-fold sysone-help/sysone. Census: Awesomejev
  488/21644; SemIf **1660** (+8); jevlike **910** (+5);
  TypeAR 9; tracker likes 42; lastModified unchanged; Laya
  yes; Blackwood ABSENT; X MCP flapping. No wrapper. No
  invented metrics.
- Same-hour remainder ~00:39 Boise 2026-09-19 (`research/notes.md`
  §65): Archer still Watch. Do not re-fold actiongate / jev-packs
  / sysone-help. Hot-click CU
  ([ego-jev](https://github.com/jiangkoumo/ego-jev); MIT; indexed
  viewport table → operation+target; code owns observe/execute/
  `--until`; text model only for type; HN 4.9 s vs 9.7 s / wiki
  5.4 s vs 10.1 s *theirs* n=3, high variance, not a bench).
  Jev judges relevance, code decides structure
  ([jev-compactor](https://github.com/edwardyen724-g/jev-compactor);
  MIT; was empty skip §61; never rewrite; regex floor; compaction
  fail-open if Jev down, safety fail-closed; 64.5% / 366 ms /
  $0.0004 / 0 invented paths / 4 of 4 facts vs Sonnet summary
  96.2% / 1 invented path, one session). Local rules first,
  never auto-train on the model's own hides
  ([x-reply-filter](https://github.com/zhuyansen/x-reply-filter);
  MIT; `rules.js` then batched Nouls; confirm-queue). OpenCode
  port already §62: fast-jev-opencode. Census as §64. No wrapper.
  No invented metrics.
- Hourly ~01:47 Boise 2026-09-19 (`research/notes.md` §66): Archer
  still Watch. Three clusters: **control-plane combinators**
  ([decision-combinators](https://github.com/voidning/decision-combinators);
  Then/Gate/Vote/Cascade/Weighted; not literal AND/OR; not chat
  turns) + **skill VOI**
  ([skillranker](https://github.com/Dicklesworthstone/skillranker);
  52★; two-pass + none-of-these; hook **fail-open** — corrects
  §7 fail-closed); **eval integrity without leaderboard theater**
  ([jev-capability-atlas](https://github.com/Zaious/jev-capability-atlas)
  10★ receipts, type-safe ≠ correct, axis already §49;
  [jev-frontier-100](https://github.com/softpudding/jev-frontier-100)
  Jev 77.0% vs Qwen3.5 4B/2048 96.7% / 4B off 56.0%, exploratory;
  [jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration)
  900 tickets ECE 0.107 = 4.4× floor, Choice/Score T~3.3 vs
  boolean T 0.66, unknowable priority mean p 0.74); **gate
  doctrine clone**
  ([turnstile](https://github.com/zyphr-labs/turnstile); Apache-2.0;
  policy first, Jev remainder, replay; missing Jev → Review);
  **MLX one-pass replica economics**
  ([jevmlx](https://github.com/bnsd55/jevmlx); 28★; softmax ≠
  Noul; no local leaderboard yet). MED: invalidate (0 of 157
  false invalidations), jev-intent-review (under construction),
  prune-review (22-run cost 1.18% with 305% outlier). Census not
  re-derived. No wrapper. No invented metrics.
- Hourly ~02:38 Boise 2026-09-19 (`research/notes.md` §67): Archer
  still Watch. Do not re-fold the 01:47 list except sibling
  contrast. **TLA+ compose with judgment**
  ([jev-labs](https://github.com/copyleftdev/jev-labs); MIT;
  never confidently wrong; 1,080 golden 0 wrong *theirs* under
  chaos, escalate 5%→18% severe; TLC 1,049,750 states / 0
  errors; synthetic, not clinical). **Advance/coverage ledger**
  ([seal](https://github.com/Reasonofmoon/seal); MIT; no seal,
  no advance; coverage.path auto|code|human|escalate; mint ≠
  product brain). **skill-broker sibling** (outline already
  §62; grants in code vs turnstile runtime vs skillranker
  advisory). **Sureness**
  ([how-sure-is-jev](https://github.com/adarc8/how-sure-is-jev);
  MIT; Choice confidence = max_prob; 75/25 → 0.5 vs entropy
  0.19). **JevBench v1.1**
  ([jevbench](https://github.com/fstandhartinger/jevbench);
  MIT; unofficial; Main Score 0.6/0.2/0.2; Jev 1.13.0 **87.6**;
  calibration reported not scored). **CI typed gate**
  ([ci-gatekeeper-bot-jev](https://github.com/NemanjaManic/ci-gatekeeper-bot-jev);
  package.json MIT / GitHub SPDX null; 504–629 ms *theirs*).
  **Codex MCP adapter**
  ([jev-in-codex](https://github.com/teempai/jev-in-codex);
  MIT; ranking unbenchmarked; lexical fallback). Census:
  SemIf **1683** (+11); jevlike **923** (+5); tracker likes
  **43** (+1); Awesomejev 488/21644 unchanged. No wrapper. No
  invented metrics.
- Hourly ~03:38 Boise 2026-09-19 (`research/notes.md` §68): Archer
  still Watch. Do not re-fold the 02:38 list except sibling
  contrast. **Judgment as attention redirect, not a merge
  blocker**
  ([jev-preflight](https://github.com/muse0509/jev-preflight);
  Go MIT; eight risk axes; assist=one reinspect; fail-open;
  uncalibrated 0.85; owner-run Claude Code 2.1.267: no-key
  fail-open PASS, key-enabled exactly one continuation).
  **Landed-script trust / headless≠auto-approve**
  ([construct-auto-classifier](https://github.com/godspede/construct-auto-classifier)
  delta; cert still Jev **0** dangerous / 975; $0.047/1k).
  **Jev judges relevance; code decides structure**
  ([jev-compactor](https://github.com/edwardyen724-g/jev-compactor)
  product-arm **73%** / 350 ms / 4 of 4 *theirs*; 30–250×
  cheaper than shipped summarizers; §65 64.5% is vs-Sonnet).
  **Compress-before-first-send**
  ([dizk/jev-lens](https://github.com/dizk/jev-lens); MIT;
  79% fewer tokens / 500 SWE-rebench; post-send prune +17%
  cost; distinct from rashedInt32/jev-lens). **tools≠use**
  ([jev-carryforward](https://github.com/Dharundp6/jev-carryforward)
  0/4 recall; SessionStart > hoping). **Observational
  memory**
  ([pi-observational-memory-jev](https://github.com/willfish/pi-observational-memory-jev);
  keep/kind verbatim; model-free compact). **Independent
  open-Jev class**
  ([openvons](https://github.com/genai-craft/openvons);
  Apache-2.0 LICENSE / GitHub SPDX NOASSERTION; 7★; JevPick
  3.2–4.8×; `/v1/systemone` wire-compat ≠ replica).
  **Physical-world S1**
  ([HA-Jev](https://github.com/AboveColin/HA-Jev); MIT;
  **17★**; sensors from typed answers; not for
  locks/heaters). **Judgment outside the store**
  ([jevql](https://github.com/kylemclaren/jevql); CLI
  judges; vanilla Postgres never sees `jev()`). Short
  consumer bullet: [sift](https://github.com/bohutang/sift)
  ~$0.00003/post. Census: Awesomejev **561** (+73, agent
  tooling 87→107); SemIf **1704**. No wrapper. No invented
  metrics.
- Hourly ~04:39 Boise 2026-09-19 (`research/notes.md` §69): Archer
  still Watch. Do not re-fold the 03:38 list except sibling
  contrast / combinators rename. **Digital-design combinators**
  ([jev-combinators](https://github.com/voidning/jev-combinators)
  is the rename of decision-combinators; extended Router /
  Loop / Retry / Fallback / Memory; metaphor ≠ literal AND/OR).
  **VOI cache admission**
  ([jevcache](https://github.com/kushals256/jevcache); MIT;
  same-intent skip LLM; n=100 *theirs* 0 FP / precision 1 /
  recall 0.38 / fpr 0 vs Jaccard@0.35 fpr 0.48; fail-open).
  **Harbor skill-routing harness**
  ([pi-jev-skill-bench](https://github.com/iamdin/pi-jev-skill-bench)
  + [pi-jev-skill-suggestion](https://github.com/iamdin/pi-jev-skill-suggestion);
  BM25 vs Jev at roster 50–500; 43 gold; no live numbers this
  pass; no-key no-op; tool mode is tools≠use cousin).
  **Zeroshot vs BERT displacement**
  ([jev-zeroshot-vs-bert](https://github.com/zhuyansen/jev-zeroshot-vs-bert);
  +0.05–+0.13 vs DeBERTa-c; contamination 0.901 vs `-c` 0.763;
  ≈230 / >2048 labels; DiD 0.035 vs 0.112 *theirs*).
  **Typed escalate/continue/abort baton**
  ([jev-handoff](https://github.com/shitianfang/jev-handoff);
  MIT; inverted loop; gate never grants; fail-open; Vercel
  drops confidence). **Worth-your-attention VOI**
  ([ThinkyMiner/Winnow](https://github.com/ThinkyMiner/Winnow);
  MIT; 80%/90% *theirs*; **≠** kevinpita/winnow).
  **Jev WHETHER / Python HOW / LLM WHAT**
  ([hermes-jev-router](https://github.com/rsdkrasen/hermes-jev-router);
  license null; community plugin; skip-next needs core patch).
  **Conflict ≠ ignorance**
  ([jev-typed-evaluation-collapse](https://github.com/mleyvaz/jev-typed-evaluation-collapse);
  Noul collapses; named Choice p=1.0; binary red 0.67–0.85
  *theirs*). **Playwright executes, Jev chooses**
  ([browser-jev](https://github.com/DowLucas/browser-jev);
  license null; sample-from-distribution). **Local class**
  ([OpenJev](https://github.com/IamBusy/OpenJev) Apache-2.0
  `/v1/decide` 45/60 *theirs*, not TypeSafe drop-in, ≠
  hraness/sysone runners;
  [semif-serve](https://github.com/dddanielliu/semif-serve)
  1164 vs 178 ms; runoff ≠ softmax; wire-compat ≠ replica).
  Toolbelt notes: jev-security-scan / jev-decisions / TeoMastro
  (summary.md 404 this pass); **rh-guard owns reward-hack**.
  Flywheel:
  [DGUI_HYPERMEM-JEV](https://huggingface.co/datasets/ctaxnagomi/DGUI_HYPERMEM-JEV)
  6-row schema. Census: Awesomejev **flat 561/27007**; tracker
  likes **43→45**; SemIf **1714** (+10); jevlike **926** (+3).
  No wrapper. No invented metrics.
- Hourly ~05:46 Boise 2026-09-19 (`research/notes.md` §70): Archer
  still Watch. Do not re-fold §50–§69 HIGH except sibling
  contrast / jevassert landing / prune-review, intent-review,
  laya-jolt, local-jev deltas. **Record/replay CI LANDED**
  ([jevassert](https://github.com/dtduc-git/jevassert);
  Apache-2.0; accuracy/ECE/Brier/cost/latency offline from
  recordings; exit 0/1/2; McNemar; Action `@v0`).
  **Evidence-gated packs now have a runner**
  ([jev-packs](https://github.com/dtduc-git/jev-packs);
  size 0→458; 2,990-case matrix *theirs*: Jev/Sonnet 5
  accuracy tie Δ≤0.018, Jev better calibrated 7/9, ~250×
  cheaper; sms-spam this-pass 0.953/ECE 0.040).
  **Failure-finding arena**
  ([jevarena](https://github.com/chenmingtang830/jevarena);
  Apache-2.0; **≠** meetr1912/jev-arena; harness not findings).
  **BBQ stereotype/uncertainty/cost**
  ([jev-bbq-experiment](https://github.com/simonmesmith/jev-bbq-experiment);
  license null; 58,492; 97.28%; bias 0.04/0.34; $0.3429 /
  7.75 min *theirs*; not a general bias cert).
  **Decider ≠ executor**
  ([jeffrey](https://github.com/thomasbrueggemann/jeffrey);
  MIT; Jev next-tool/progress/risk/done; LLM fills args;
  pick ≠ fill). **Sentence-as-rule lint**
  ([jevlint](https://github.com/mizchi/jevlint); MIT;
  ast-grep × `ask:`; 13/15 1.00/1.00 *theirs*; **≠**
  huntedman/JevLint). **VOI hunk prune**
  ([prune-review](https://github.com/shubhangi013/prune-review);
  22-run 1.18% with 305% outlier; ~20% target; cost not
  quality). **Whole-repo intent**
  ([jev-intent-review](https://github.com/yottayoshida/jev-intent-review);
  VERIFIED/VIOLATION/UNKNOWN; empty search ≠ proof).
  **GLiNER2 System One spec**
  ([Jev_from_GLiNER2](https://github.com/Eran-BA/Jev_from_GLiNER2);
  spec-only; ≠ jeff). **Open replica substrates**
  ([grande](https://github.com/bokuweb/grande) JGLUE 0.614/
  0.853 + 270M 0.710/0.710 *theirs*;
  [laya-jolt](https://github.com/jlt-commons/laya-jolt)
  byte parity; [JEV-CPU](https://github.com/leesk212/JEV-CPU)
  PoC, Meanblock 404; [local-jev](https://github.com/kunchenguid/local-jev)
  done 30%/shape 57%). **Persist constraints**
  ([pi-heed](https://github.com/Nyarlathoteppppp/pi-heed);
  98.5%/0 false block *theirs*). Toolbelt note:
  actiongate slogan already §64. MED:
  [system-one-responsible-ai](https://github.com/david-j-lustig/system-one-responsible-ai)
  size-0 framing stub. Census not re-derived. No wrapper.
  No invented metrics.
- Hourly ~06:43 Boise 2026-09-19 (`research/notes.md` §71): Archer
  still Watch. Do not re-fold §50–§70 HIGH except sibling
  contrast. **Harbor SGR-judge contract**
  ([jev-judge-bench](https://github.com/slavadubrov/jev-judge-bench);
  README MIT / GitHub SPDX NOASSERTION; frozen SLA-150; Jev vs
  Luna / DeepSeek-flash / glm-5.3-flash; invalid = FN;
  21 offline tests; canaries ≠ quality; **no quality headline
  yet**; **≠** jevarena / jevbench). **Empty skip**
  ([jev-context-pruner](https://github.com/IPECTER/jev-context-pruner);
  409 empty). **Hand no-text steps**
  ([jev-use](https://github.com/shitianfang/jev-use); MIT
  v0.4.1; p50 220 ms; 186 vs 2,672 ms; gate 12/12; Vercel
  drops confidence → margin 0.4; first loop 17/20 then 0/20
  *theirs*; **≠** jev-ultrafast). **Pi System-One control
  plane** ([pi-jev-control](https://github.com/goodruizhan/pi-jev-control);
  license null; v0.3.0 private; GUI never force-click;
  compaction never writes session). **Never free-generates**
  ([jev-gpt](https://github.com/florian-hoenicke/jev-gpt);
  license null; ~400 calls / 75 s / 2¢ *theirs*).
  **OpenRouter recipe atlas**
  ([jev-cookbook](https://github.com/nexibeo/jev-cookbook);
  MIT; 1★; 16–36 samples not benches; 425 calls / $0.015;
  browser 5/6 *theirs*). **Personal-history feed**
  ([jevfeed](https://github.com/fengyiqicoder/jevfeed); MIT;
  no social graph; one request per batch of ten).
  **Competing NAR claim-audit, not endorsement**
  ([openJev-verdict-2.0](https://github.com/Heman10x-NGU/openJev-verdict-2.0);
  README Apache-2.0 / GitHub SPDX NOASSERTION; 77.10%/0.0636/
  0.0144 *theirs* unverified; **open PR #1**: throughput≠
  latency, Laya parity, like-for-like ECE; **≠**
  IamBusy/OpenJev). Census not re-derived. No wrapper. No
  invented metrics.
- Hourly ~07:49 Boise 2026-09-19 (`research/notes.md` §72): Archer
  still Watch. Do not re-fold §50–§71 HIGH except sibling
  contrast. **1-token logprob endpoint ≠ Noul**
  ([chakuho](https://github.com/taku-me/chakuho); MIT;
  coverage ≠ correctness; GUI 336 *theirs* 27B 95%/92%
  vs Jev 89%/82%; `__none__` 97% vs 8B 10%). **Open
  replica engine** ([jevinf](https://github.com/zerodegress/jevinf);
  MIT; 2.57×/2.27× 100% argmax; MPS only). **Unofficial
  Elixir SDK ≠ OTP peer**
  ([typesafe-elixir-sdk](https://github.com/phiat/typesafe-elixir-sdk);
  MIT; 1★; ≠ dannote/jev). **jevex rename + n=16 VOI**
  ([jevex](https://github.com/jimmyhealer/jevex); 160s→69s
  / $8.74→$3.13 / 16/16 *theirs*; keep n=8 1/8→6/8).
  **Commit attention≠verdict**
  ([commitjev](https://github.com/yodablocks/commitjev);
  MIT; middle band never rounded; 0 false on 5 clean
  *theirs*). **Hermes plugin is Agnes not TypeSafe**
  ([hermes-plugin-jev](https://github.com/Mrmimee/hermes-plugin-jev)).
  **Pi compact ≠ compaction**
  ([pi-jev-compact](https://github.com/dev-willbird1936/pi-jev-compact);
  MIT). **Empty skip**
  ([jev-runway](https://github.com/IPECTER/jev-runway);
  LICENSE-only). **Decision-native inbox**
  ([mailordinal](https://github.com/Milo318/mailordinal);
  MIT). **Unofficial jev-cli not ready**
  ([jev-cli](https://github.com/shaharia-lab/jev-cli);
  0.0.0; ≠ jevql). **Laya multilingual**
  ([laya-multilingual](https://huggingface.co/convaiinnovations/laya-multilingual);
  MASSIVE 0.366/0.387; Khmer 0.000@0.952; ships
  uncalibrated). **Schema-scorer Hub** (GitHub 404; v2
  Choice 0.841; peaked ranking). HF 401 this pass on
  open-jev-laya-bench / jev-tree-choice-cap /
  INSTRUCT_JEV; jevlogs 404+401. Census not re-derived.
  No wrapper. No invented metrics.
- User-provided signal ~08:37 Boise 2026-09-19
  (`research/notes.md` §73): **Skip Archer.**
  **Productized System One HTTP**
  ([classifier-dev](https://github.com/mrmps/classifier-dev);
  MIT; **185★**; https://classifier.dev). Label +
  calibrated confidence as the public contract; batch
  `{id,text}[]` ~1000; Jev primary, LLM fallback only.
  400 headlines **650 ms** *theirs*. **Escalate-under-
  threshold:** smart re-asks single-label <0.7;
  multi-label ignores (re-judge worse, 23 s). Emotion
  ≥0.9 → 82% / <0.5 → 29%; gemini-3.8-flash 87.5→90.0 /
  61.8→63.7 *theirs*. Multi-label F1 **0.887** / **230 ms**
  vs cascade **0.799** / 1.5 s (eval 232 ms; AG News
  **87.7%** vs 82.0%). **Measurement-first:** `/benchmark`
  from tracked JSON; read eval/README (n=7 train-on-test;
  ~0.03 coin flip). **Silent FALLBACK:** granite F1
  **0.546** vs advertised ~**0.800** *theirs*; rh-guard
  owns the gate. Life/business (spam/inbox/feedback),
  not SWE-only. Distinct from ask-jev-ai wall. No wrapper.
  No invented metrics.
- User-provided signal ~08:48 Boise 2026-09-19
  (`research/notes.md` §74): **Skip Archer.** **Delta of
  §48.** Pointer-not-generator at evidence-synthesis
  scale
  ([choxos/jev-reviewer](https://github.com/choxos/jev-reviewer);
  MIT; **12★**; https://jevreviewer.xera.ac). **≠**
  [egma-ai/jev-reviewer](https://github.com/egma-ai/jev-reviewer).
  Two-pass Choice (which line) + Noul (does this line
  itself answer); quotes = Noul ≥ 0.5 *theirs*. *Not
  found* / *Unclear* first-class. Human tick is the
  product (checked never overwritten). 18-q template
  **4.6 s / $0.0101** *theirs* (spot check, not a
  validation study). Cochrane / PRISMA / RoB, not
  SWE-only. No wrapper. No invented metrics.
- User-provided signal ~08:56 Boise 2026-09-19
  (`research/notes.md` §75): **Skip Archer.**
  **Wire-compat ≠ logit-equiv**
  ([githubnext/localjev](https://github.com/githubnext/localjev);
  MIT; **261★**; GitHub Next). **≠**
  [kunchenguid/local-jev](https://github.com/kunchenguid/local-jev).
  Bun `POST /v1/systemone` on DiffusionGemma via Chat
  Completions; TypeSafe SDK drop-in. Prompted JSON →
  validate/retry → normalize + entropy confidence — not
  razorback16 structured-read logits. Harbor-shaped
  bake-off *theirs*: 1,200 req; Qwen3.6 short macro
  **76.7%**; Gemma 4 26B-A4B **75.0%**; DiffusionGemma
  **74.2%**; no definitive winner (2/120); do not treat
  as calibrated. LM Studio still cannot load
  DiffusionGemma. Do not copy bun / `.env`. No wrapper.
  No invented metrics.
- User-provided signal ~09:07 Boise 2026-09-19
  (`research/notes.md` §76): **Skip Archer.** **Laya
  packaging, not a new species**
  ([NandhaKishorM/laya](https://github.com/NandhaKishorM/laya);
  Apache-2.0; **710★**). PyPI + `Router` over Hub
  [`laya`](https://huggingface.co/convaiinnovations/laya) /
  [`laya-multilingual`](https://huggingface.co/convaiinnovations/laya-multilingual) /
  [`laya-typed-decisions`](https://huggingface.co/convaiinnovations/laya-typed-decisions).
  **≠** TypeSafe `/v1/systemone`. **≠** githubnext/localjev.
  T4 *theirs*: 1q **32.8 ms** (~7.8× vs Jev p50
  236–276 ms). Post-T ECE **0.081** vs Jev **0.246**;
  raw ECE still trails (0.213 vs 0.144). Banking77
  **0.425** vs Jev **0.870** (77 vs 72; ~3–4 tok/label).
  typed-decisions **0.766** is a fine-tune (base
  0.362/0.342 vs majority 0.461). Soft-acc 0.471 vs
  0.580. Khmer **0.000@0.952** — Router because gating
  cannot catch. 0.85 still soft. Jev rows third-party
  unpublished-here. Do not copy pip / preload. No
  wrapper. No invented metrics.
- User-provided signal ~09:14 Boise 2026-09-19
  (`research/notes.md` §77): **Skip Archer.** **External
  openjev census ≠ scored bake-off**
  ([@airesearch12](https://x.com/airesearch12/status/2101259522933186879);
  Florian S / Benchmark Heaven). Named ~18 (system-one-open,
  openjev-sglang, DeBERTa open-jev, Needle 3,
  open-alternative-jev, Nimble 9B, SemIf, open-jev Dasein /
  JoshuaSP, OpenJev razorback16, mini-jev, system-one,
  system-one-gemma, jevlike, AlexWortega/openjev, GLiNER2,
  Succinct Router 14M, jev-model-router/Director/Loki).
  GLiNER2 + routers are **class-boundary**. Incomplete vs
  Laya / localjev / kev / TypeAR / openvons. Engagement
  **ephemeral** (SIGNAL ~417/9/3; this pass 564/15/5). **≠**
  jevbench v1.1. Watch
  [jev-models](https://benchmarkheaven.com/jev-models); do
  not paste live ranks. Do not copy Stripe. No wrapper. No
  invented metrics.
- User-provided signal ~09:24 Boise 2026-09-19
  (`research/notes.md` §78): **Skip Archer.** **JevBench v1.2
  scored board**
  ([benchmarkheaven.com/jev-models](https://benchmarkheaven.com/jev-models);
  harness [fstandhartinger/jevbench](https://github.com/fstandhartinger/jevbench)
  MIT; 0★; HEAD `27ed3d6c`). Protocol `jevbench::v1.2`; scored
  19 Sept 2026; 534 decisions (hard 220 = 30% of Intelligence).
  Official Score = geometric mean of I/C/S/K at 25% each. Jev
  1.13.0 **75.3**; SemIf (Qwen3.5-4B) **74.6** (−0.7); OpenJev
  DiffusionGemma (razorback16) 67.6 *theirs*. Luna Intelligence
  **96.8** rank **#7** on cost. Calibration **on** the rank
  (delta from v1.1). Weighting is a product design. Option-order
  72%→21%. Self-host latency ×2 is an assumption; many costs
  est. Laya absent (gap, not named-excluded). GLiNER2 mapping
  issues; apps out. Qwen3.8 27B Chutes TEE **≠** Archer. **≠**
  tweet census §77 **≠** v1.1 87.6. Do not copy Stripe / CLI.
  No wrapper. No invented metrics.
- Hourly System One watch ~08:42 Boise 2026-09-19
  (`research/notes.md` §79): **Skip Archer.** Named HIGHs
  **already folded** (§73–§78) — extract **how-to-apply**,
  not a hit list: wire-compat ≠ logit-equiv (prompted JSON
  ≠ structured logit); productize label+p and mark
  `FALLBACK`; packaging ≠ new species / script-before-p /
  0.85 still soft; pointer-not-generator (two-pass; *Not
  found*; human tick); external census ≠ scored bake-off /
  geo-mean weights are a design. **Skip thin noise**
  (JEValuate / jevspeak / fable-jev; jev-semgrep already
  §61). Hard-gating a Noul as a PR/quality gate is
  soundness theater
  ([totally-tim/jev-gate](https://github.com/totally-tim/jev-gate)
  0★ ≠ jev-gateway; [claude-jev-warden](https://github.com/connectedGraph/claude-jev-warden)
  1★).   Qwen3.8 27B ≠ Archer. No wrapper. No invented
  metrics.
- User-provided HIGH ~09:50 Boise 2026-09-19
  (`research/notes.md` §80): **Skip Archer.** Delta of
  §46, not a new species.
  [khordoo/jev-reflex-autonomy-lab](https://github.com/khordoo/jev-reflex-autonomy-lab)
  (TypeScript; **7★**; license null; README SHA
  `130987c9`; ARCHITECTURE SHA `48da0769`; HEAD
  `e3297ebe`). S1 never stalls waiting; S2 is one-use
  advisory and never flies. Purple confidence =
  **consumed** S2 (purple bar = arrival; red = fail).
  Local controller is rule-based **≠**
  githubnext/localjev **≠** kunchenguid/local-jev.
  Live API `POST /v1/systemone` `jev-latest`; 20%
  starting gate *theirs* still soft and does not start
  a mission. Seed = geometry ≠ async replay. No pixels
  to either provider; confidence ≠ selected
  probability; S2 never grants. README GLM 5.3 vs
  ARCHITECTURE muse-spark-1.3-contributor — quote both
  *theirs*. Experimental viz, not a flight controller.
  Do not copy npm / `.dev.vars`. No wrapper. No
  invented metrics.
- User-provided HIGH ~09:51 Boise 2026-09-19
  (`research/notes.md` §81): **Skip Archer.** Productized
  observe→score-among-candidates→code-acts on a Mac,
  not a new species.
  [awlevin/typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use)
  (Python; MIT; **427★**; README SHA `369f4a6a`; HEAD
  `cc7b5066`). OCR+AX → numbered items → TypeSafe
  Choices (`kind`/`item`/`site`/`offscreen`) →
  deterministic click/type. **Never ships a screenshot
  to frontier for the *decision***; the one-shot
  **answer** writer may receive the capture (reader
  packet, not the Choice). Writer only for free text.
  Overlapping options = false low confidence. AX bonus
  never sole (Spotify 0 *theirs*). Post-type Noul 0.5
  and `--min-confidence` 0.4 still soft. $0.0002 vs
  Opus $0.032 (155×) *theirs* on **one screenshot**,
  not a Harbor taskset. Honest caveat: dates.py rebuilds
  pixel-free reasoning. **≠** jev-ultrafast **≠**
  cua-s1 **≠** jev-macos-loop **≠** camoufox. Do not
  copy `uv sync` / `.env`. No wrapper. No invented
  metrics.
- User-provided HIGH ~10:01 Boise 2026-09-19
  (`research/notes.md` §82): **Skip Archer.** Productized
  ASR observe→score-among-candidates→code-acts in
  headed Chromium, not a new species and not omni.
  [moritzkremb/jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser)
  (JavaScript; MIT; **103★**; README SHA `fa033303`;
  HEAD `054db0f3`). Web Speech partials → one 9–11-
  question Jev request (~250–350 ms *theirs*) →
  policy. Pointer-not-generator for spans. Closed-set
  may act on a partial; free-text waits. Spoken
  confirm is convenience, not auth. Numbered overlay,
  no second model. Integration 27/27 / ~$0.0002/call
  *theirs* fixtures, not a Harbor taskset. 0.5 / 0.55
  / 0.6 still soft. **≠** jev-voice-control **≠**
  nikolas-j **≠** Aj1905 **≠** typesafe-computer-use
  OCR. Do not copy `npm` / `.env` / `run.sh`. No
  wrapper. No invented metrics. Expand the §39 tweet;
  do not re-card it.
- User-provided HIGH ~10:20 Boise 2026-09-19
  (`research/notes.md` §83–§84): **Skip Archer.** Two
  signals, one fold.
  [reddpy/AgentGhost](https://github.com/reddpy/AgentGhost)
  (TypeScript; MIT; **2★**; README SHA `44145fa9`;
  HEAD `ac04e4fb`). Intent-aware ALLOW/ASK/DENY
  wrap-as-execution: the wrap *is* the tool function;
  rules first; ASK throws; `failMode: closed`. Judge
  is a slot. Provider-hosted tools out of reach.
  **≠** jwen5419807/agentghost **≠** vventirozos
  **≠** actiongate **≠** toolgate **≠** jev-use.
  rh-guard owns the gate cousin. Do not copy `npm` /
  `.env` / `AUTO_APPROVE`. [@studio_yebisu JP genre
  atlas](https://x.com/studio_yebisu/status/2101065176069886152)
  (2026-09-18T21:45:48Z). Apps by hole, not a scored
  bake-off. Stars research-time (typesafe-computer-use
  203→**427**; jev-voice-browser 40→**103**). Not
  verified evals. Engagement ephemeral (this pass
  131,234 / 1,934 / 192). SAM 3.1 already §39.
  OpenRouter Jev no-waitlist is WATCH, not a recipe.
  **≠** @airesearch12 class census **≠** v1.2 board.
  Do not dump the 30 repos. No wrapper. No invented
  metrics.
- User-provided HIGH ~10:25 Boise 2026-09-19
  (`research/notes.md` §85): **Skip Archer.** External
  pedagogy / how-to-apply, not a new species.
  [@akshay_pachaar “Jev Clearly Explained”](https://x.com/akshay_pachaar/status/2101037514945597645)
  (article https://x.com/i/article/2100940576741093376;
  2026-09-18T19:55:53Z). LLM hammer for bounded
  decisions; code owns branches; parallel questions;
  thresholds in code; **schema-safe ≠ correct**;
  placements = routing / tool-risk / verify with LLM;
  shadow-mode; questions-as-code. **200× / 400×** and
  70–500 ms / $0.042/MTok are TypeSafe **ceiling**
  claims *theirs*, not Harbor. Text-only; not looking
  at the screen. **≠** official docs **≠** Flavio
  Copes **≠** LangChain harness **≠** AgentGhost.
  Engagement ephemeral (this pass 233,495 / 2,280 /
  235). Do not copy the Python samples. No wrapper.
  No invented metrics.
- User-provided HIGH ~10:30 Boise 2026-09-19
  (`research/notes.md` §86): **Skip Archer.** Dedicated
  fold of [uehaj/jev-semgrep](https://github.com/uehaj/jev-semgrep)
  (light-noted §61). Grep by meaning via Jev Noul;
  proposition ≠ embedding; contrast-set (all six
  about a refund; only customer-*asking* pass);
  AND/OR/NOT are boolean ops on *thresholded* bits
  (do not multiply p; ≠ jev-combinators metaphor).
  Cross-lingual; no index; EN safer near threshold.
  Semgrep.dev SAST name collision. **Not a gate**
  (ranking fail-open; rh-guard skip). LICENSE MIT /
  GitHub NOASSERTION. HEAD `21120e9`; README SHA
  `923e6a5`. Stars ephemeral (0 → SIGNAL ★42 → **51**
  this pass). 0.94/0.98 LLM-as-judge 10×51 *theirs*,
  not Harbor. **≠** jevgrep **≠** jev-sift **≠**
  jevex **≠** semgrep.dev. Do not copy npm / `npx` /
  `.env` / marketplace. No wrapper. No invented
  metrics.
- Hourly 1047 HIGH + deferred 0945 backlog
  (`research/notes.md` §87): **Skip Archer.** Docs-only
  off main (PR #2 merged). How-to-apply / mental
  models / architecture / Harbor-jevals — not
  SWE-only. Formal methods compose with scoring; a
  Noul is a SENSOR; hard-gating as test/PR/HA
  write/authorship is soundness theater. Ten
  clusters: decision-validated UI
  ([gram-render](https://github.com/wei-b0/gram-render)
  never authors text;
  [jev2ui](https://github.com/dglazkov/jev2ui) Jev
  decides / Gemini writes);
  decision-as-assert
  ([jevtest](https://github.com/realZachi/jevtest)
  ambiguous band 0.15–0.85; 0.85 still soft);
  hybrid S1
  ([anima3](https://github.com/hulryung-uo/anima3)
  Qwen logprob default; jeff confidently flat; do
  **not** invent Laya);
  pointer search
  ([JevFind](https://github.com/Peu77/JevFind));
  Harbor trio
  ([jev-frontier-bench](https://github.com/manjunathshiva/jev-frontier-bench)
  72.5%/ECE 0.161 vs Fable 84%/0.064 *theirs*;
  ChaosNLI JS worse than uniform; **≠**
  frontier-100;
  [jev-gliclass-bench](https://github.com/JoeSlain/jev-gliclass-bench)
  product bakeoff 78/40/49;
  [job-posting-triage](https://github.com/geckguy/job-posting-triage)
  majority floor 0.947 / tfidf wins / calibration ≠
  discrimination);
  authorship named escape (not evidence);
  non-SWE
  ([ha-switchboard](https://github.com/grayslawson/ha-switchboard)
  HA remains execution **≠** HA-Jev;
  [n8n-nodes-jev](https://github.com/vibe-with-me-tools/n8n-nodes-jev)
  unofficial Low Confidence);
  compaction delta
  ([fast-jev-compaction-pi](https://github.com/zaycruz/fast-jev-compaction-pi)
  **≠** pi-jev-compact **≠** pi-jev-compaction;
  ~50× *theirs*);
  full-distribution optimizer
  ([jevloop](https://huggingface.co/spaces/async-dime/jevloop)
  UCB1+CEM; no LLM in the loop; mock default);
  deferred class
  ([laya-vision](https://huggingface.co/thaitea/laya-vision-smolvlm-256m)
  SmolVLM; `score` untrained; **≠** blackwood **≠**
  Archer;
  [Cerebellum-2B](https://github.com/mkeco/Cerebellum-2B)
  `/v1/decide` ≠ TypeSafe; wire-compat vs
  agent-routing as separate Harbor axes; competing
  NAR **not endorsement**;
  [laya-grounded](https://huggingface.co/Luni/laya-grounded)
  not drop-in; phishing 0.611→0.512; Platt not
  temperature). 0★ HIGHs still get real cards. Do
  not copy npm / `pi install` / n8n / HA add-on /
  `TYPESAFE_API_KEY`. No wrapper. No invented
  metrics.
- Queued user SIGNALs + remaining deferred 0945 HIGH
  (`research/notes.md` §88): **Skip Archer.** Docs-only
  on PR #3. Mental models: open LoRA replica
  ([GestaltLabs/Jeff-1](https://huggingface.co/GestaltLabs/Jeff-1)
  acc **0.8183** ECE **0.0807** vs Jev **0.8283** /
  **0.0932** n=9730 *theirs*; set reused; **≠**
  [logan-markewich/jeff](https://github.com/logan-markewich/jeff));
  Jev-first bounded agent
  ([stanley-code](https://github.com/devagrawal09/stanley-code)
  empty findings ≠ approval; human promote; 0.6/0.55/0.15
  still soft);
  NL memory → beam-search FS
  ([findme](https://github.com/marc2332/findme) **≠**
  JevFind);
  price workers not the conversation
  ([jevsubrouter](https://github.com/leftspace89/jevsubrouter)
  fail-open; counts ≠ dollars). laya-vision +
  Cerebellum already §87 — not re-carded. Soft Noul ≠
  hard safety. Do not copy `uv` / npm / cargo /
  marketplace / `TYPESAFE_API_KEY` / `JEVSUB_API_KEY`.
  No wrapper. No invented metrics.
- Hourly 1144 HIGH (`research/notes.md` §89): **Skip
  Archer.** Docs-only on PR #3. Do **not** re-fold
  1047 / §87 / §88. How-to-apply / mental models /
  architecture / Harbor-jevals — not a thin Jev skill
  dump. Backend-agnostic categorization/scoring/
  decision class. Formal methods compose with scoring;
  a Noul is a SENSOR; hard-gating a default 0.5 bool,
  quoting apa “mathematically fulfilled,” treating A/B
  proxies as token savings, letting Jev send mail, or
  pasting jev-test bars as results is soundness theater.
  Seven clusters: **Typed if**
  ([feelings](https://github.com/BoundaryML/feelings)
  `.feels()` default 0.5 is Noul-0.5-never-rounded;
  exhaustive BAML `match`; **≠** hunch **≠** Probably;
  license null; **0★**);
  **Shadow then honor**
  ([apa-agent-harness](https://github.com/AiPersonacademy/apa-agent-harness)
  **≠** AntonioCoppe/jev-harness; unpublished npm;
  0.85 still soft;
  [apa-persona-engine](https://github.com/AiPersonacademy/apa-persona-engine)
  SM then leftover LLM; <250 ms ≠ microsecond;
  [grok-bot-jev](https://github.com/Bodila51/grok-bot-jev)
  skill honor; A/B proxies ≠ tokens; 13.0× is a
  top-five cap);
  **Human every action**
  ([Essentiel-Jev](https://github.com/JacquesGariepy/Essentiel-Jev)
  never authority; 0.75 provisional; license null);
  **Atom then sense**
  ([enzo-mcp](https://github.com/mahawi1992/enzo-mcp)
  independently falsifiable claims; UNKNOWN useful;
  **≠** jev-sift);
  **File by Choice**
  ([pigeonhole](https://github.com/noripto/pigeonhole)
  OTHER skip; 0.6 still soft; **≠** jev-semgrep;
  client-side playground
  [jev-agent-decision-playground](https://huggingface.co/spaces/bojansandhaus/jev-agent-decision-playground)
  static no-network; **≠** classifier.dev; sibling
  jev-decisions pointer only);
  **Question preflight**
  ([jev-reliability](https://github.com/vcjdeboer/jev-reliability)
  Nothing about accuracy; noul-gate 0.0%/12.5%/3.6%
  *theirs*; **≠** dinostomp;
  [clduab11/jev-test](https://github.com/clduab11/jev-test)
  bars ≠ scores; **≠** realZachi/jevtest;
  [jev-rag-benchmark](https://github.com/erendikmenn/jev-rag-benchmark)
  “Jev wins” is not an assumption; **≠** Jev-RAG;
  [dairui1/jev-lab](https://github.com/dairui1/jev-lab)
  urgent 91% vs Haiku 79% *theirs* synthetic; **≠**
  BrendanH18/jev-lab; do not re-card jev-desktop);
  **Inbox read-only vs write**
  ([jevmail](https://github.com/fazlerocks/jevmail)
  `gmail.readonly` ~3¢/1k *theirs*; **3★**;
  [mailjay](https://github.com/secondfret/mailjay)
  archive/trash after review; license null; **≠**
  mailordinal). Soft Noul ≠ hard safety. 0★ HIGHs
  still get real cards. Do not copy unpublished npm
  `@aipersona/…` / `uv` / `baml toolchain` / Gateway
  keys / `TYPESAFE_API_KEY`. No wrapper. No invented
  metrics.
- Hourly 1241 HIGH (`research/notes.md` §90): **Skip
  Archer.** Docs-only on a **fresh PR off main**. Never
  reopen merged #3 / #4 / #5. Do **not** re-fold 1144 /
  §89. How-to-apply / mental models / architecture /
  Harbor-jevals / toolbelt — not a thin Jev skill dump.
  Backend-agnostic categorization/scoring/decision class
  (Jev-like speed/econ). Formal methods compose with
  scoring; a Noul is a SENSOR; hard-gating AUTO_ACT,
  treating ranking logits as frequencies, pasting
  95.2% / 83% plumbing / 36/120 NL2Bash as class
  ceilings, or letting Jev send/delete/close pinned
  tabs is soundness theater. Twelve clusters:
  **Observe→score→act namesake**
  ([ZHUBoer/ego-jev](https://github.com/ZHUBoer/ego-jev)
  reserved `__none__`; runWorkflow completed ≠ success;
  **≠** jiangkoumo/ego-jev; **0★**);
  **Decision-as-ranking**
  ([jsort](https://github.com/keltokhy/jsort) scores are
  relative; Noul not Choice for scale; CommonLit
  r=0.824 / ρ=0.841 *theirs*; **1★**);
  **Native vs schema-guided Harbor**
  ([groundedness-judge-bench](https://github.com/slavadubrov/groundedness-judge-bench)
  native vs schema-guided; implicit_true included
  in yes; Jev 0.6667 vs GLM 0.7661 *theirs*;
  LICENSE MIT / SPDX NOASSERTION; **0★**; **≠**
  jev-judge-bench);
  **0 promotions / authored vs real**
  ([jev_playground](https://github.com/JYeswak/jev_playground)
  0 promotions; routing-backtest 0.0447%; **0★**; **≠**
  HF playground);
  **Offload + classifier-not-generator**
  ([yuyang2230/jev-agent-skill](https://github.com/yuyang2230/jev-agent-skill)
  jev-1.13-free; **≠** GodsBoy; **0★**;
  [jev-techstack-classifier](https://github.com/swap-mitra/jev-techstack-classifier)
  stack_config.json only; license null; **0★**);
  **Collapse late**
  ([s1_ruby](https://github.com/innocentdiaz/s1_ruby)
  collapse late; `undecided?` abstain; **≠** hunch **≠**
  feelings; **1★**);
  **Unofficial toolbelt**
  ([2389-research/judgement](https://github.com/2389-research/judgement)
  license null; confidence ≠ winner p; **0★**;
  [typesafeai-sdk-rust-community](https://github.com/community-ports/typesafeai-sdk-rust-community)
  typesafeai-sdk-community not a new species; **0★**);
  **Pointer shell**
  ([tpellet/hunch](https://github.com/tpellet/hunch)
  exit 3; never-execute list; **≠** carldaws/hunch;
  **0★**);
  **Preview-first VOI / rubric rewrite**
  ([jev-file-search](https://github.com/emilwagman/jev-file-search)
  scores not calibrated accuracy; **0★**;
  [jev-linkmap](https://github.com/stas4000/jev-linkmap)
  Jev never sees S2 prose; LICENSE MIT / SPDX
  NOASSERTION; **0★**);
  **Life fail-open covers**
  ([jev-mail](https://github.com/muhammedilyasy/jev-mail)
  metadata only; [tidy](https://github.com/MANISH007700/tidy)
  none-of-folders stay; [tab-bouncer](https://github.com/MANISH007700/tab-bouncer)
  pinned/audio/current never closed;
  [lkclean](https://github.com/stefw/lkclean) Show
  fail-open; [jev-yt-time-saver](https://github.com/jaibhasin/jev-yt-time-saver)
  Show anyway);
  **S1 decide / S2 plan**
  ([ORIGIN-CIVILIZATION](https://github.com/JacquesGariepy/ORIGIN-CIVILIZATION)
  pause-if-no-Jev; validResponse sums-to-1; **≠**
  Essentiel-Jev; **1★**);
  **Seed/expand/judge/verify + local daemon ≠ Jev**
  ([jev-crawlers](https://github.com/russfranky/jev-crawlers)
  risk bands never raw boolean; **0★**;
  [jevbrain](https://github.com/Synxneuos/jevbrain)
  AUTO_ACT is not a Noul; license null; **9★**). Soft
  Noul ≠ hard safety. 0★ HIGHs still get real cards.
  Census (user-provided; not re-derived): Archer still
  NOT landed (HF empty; tracker likes 49 lastModified
  2026-09-19T18:37:18Z still promised); Laya yes;
  Blackwood ABSENT; SemIf 1846 (+17); jevlike 962 (+3);
  TypeAR-AI/TypeAR 10 (+1); Awesomejev flat 561/27007.
  Do not copy `TYPESAFE_API_KEY` / `ZEN_API_KEY` /
  `AI_GATEWAY` / `uv` / `cargo` / wrangler / chrome
  unpacked / OAuth client ids / shop URLs / `.env`.
  No wrapper. No invented metrics.
- Hourly 1347 HIGH (`research/notes.md` §91): **Skip
  Archer.** Docs-only on a **fresh PR off main**. Never
  reopen merged #3 / #4 / #5 / #7. Do **not** re-fold
  1241 / §90. How-to-apply / mental models /
  architecture / Harbor-jevals / toolbelt — not a thin
  Jev skill dump. Backend-agnostic
  categorization/scoring/decision class (Jev-like
  speed/econ). Formal methods compose with scoring; a
  Noul is a SENSOR; hard-gating argmax as safety,
  pasting 97.7% n=130 / 0 hallucination / 8,026 tokens
  as class ceilings, or treating a skill named System
  One as a judge is soundness theater. Nine clusters:
  **Judge harness as control API**
  ([judgekit](https://github.com/lexingtonhibiki/judgekit)
  YAML classify/score/route/verify; 97.7% n=130
  *theirs*; **0★**;
  [typed-judge-kit](https://github.com/Ascurse/typed-judge-kit)
  verdict-in-code; MIN_LABELS=20; **0★**);
  **Batch packing VOI**
  ([decide](https://github.com/alsoleg89/decide)
  packing VOI; 0.8 ≠ 80% accuracy; license null;
  **0★**; **≠** jev-sift);
  **Calibration as product**
  ([Jev-Calibration](https://github.com/AnthusAI/Jev-Calibration)
  Platt ECE 0.117→0.052; license null; **0★**;
  [jev-calibration-arena](https://github.com/pmcclelland/jev-calibration-arena)
  never acts; size 0; **0★**; **≠** jev-arena);
  **Decision-as-Plugin**
  ([openrouter-jev-mcp](https://github.com/ctmx/openrouter-jev-mcp);
  [typesafe-mcp](https://github.com/cyrusasco/typesafe-mcp)
  noul deadband 0.35–0.65;
  [FrancoisChastel/jev-code](https://github.com/FrancoisChastel/jev-code)
  ≠ npm jev-code; **1★**;
  [claudecode-jev-marketplace](https://github.com/skylence-org/claudecode-jev-marketplace)
  fail-open not hot path;
  [mcp_jev](https://github.com/pedroknigge/mcp_jev)
  packs not ask_jev;
  [jev-skill](https://github.com/codaaiteam/jev-skill)
  jevtypesafeai.com ≠ TypeSafe);
  **Policy-constrained skill select**
  ([hermes-switchyard](https://github.com/bgrablin/hermes-switchyard)
  ≠ hermes-jev-router ≠ hermes-plugin-jev; **0★**);
  **Tiny local econ pruner**
  ([nanoprune](https://github.com/dmdjr1409/nanoprune)
  2.8MB ECE 2.58%; 0 hallucination theater; **0★**);
  **Observe→score→act cousins**
  ([jev-browser-agent](https://github.com/smartdio/jev-browser-agent)
  ≠ ZHUBoer/ego-jev;
  [omp-jev-web](https://github.com/Dakai/omp-jev-web)
  DONE ≠ proof;
  [hari007sh/jev](https://github.com/hari007sh/jev)
  ≠ dannote/jev; license null);
  **Deterministic verify ≠ System One**
  ([system-one-skills](https://github.com/0thernet/system-one-skills)
  deterministic verify; **0★**);
  **Soft-score vs hard-argmax**
  ([typed-gate](https://github.com/harshpuri84/typed-gate)
  band [0.40,0.60] is refusal;
  [pi-jev-gate](https://github.com/fivethirty/pi-jev-gate)
  fail-closed; choice is the verdict; rh-guard owns). Soft
  Noul ≠ hard safety. 0★ HIGHs still get real cards.
  Census (user-provided; not re-derived): Archer still
  NOT landed. Do not copy `TYPESAFE_API_KEY` /
  `OPENROUTER_API_KEY` / `JEV_API_KEY` / `uv` / `npx`
  / plugin-marketplace install / `.env`. No wrapper.
  No invented metrics.
- Hourly 1441 HIGH (`research/notes.md` §92): **Skip
  Archer.** Docs-only on a **fresh PR off main**. Never
  reopen merged #3 / #4 / #5 / #7 / **#8**. Do **not**
  re-fold 1347 / §91. How-to-apply / mental models /
  architecture / Harbor-jevals / toolbelt — not a thin
  Jev skill dump. Backend-agnostic
  categorization/scoring/decision class (Jev-like
  speed/econ). rh-guard owns the gate cousins;
  Augustus owns placement. Formal methods compose with
  scoring; a Noul is a SENSOR; pasting Foq 100%/ECE
  0.2% / Reranker 0.1667 / 400 ms / akpsahan vs-Jev as
  class ceilings, or treating Qwen3.8-27B as Archer, is
  soundness theater. Nine clusters:
  **Self-hosted econ**
  ([Foq](https://github.com/yohanargentina-oss/Foq)
  ~25ms/2.2GB local; **1★**;
  [rev](https://github.com/jaswanthsanjay88/rev)
  prefill-only + HF jev-0.5b; **0★**;
  [robfrase/jev](https://github.com/robfrase/jev)
  planning memo);
  **Soft-judgment gate integrity**
  ([typesafe_agent_gates](https://github.com/ThiagaoBR/typesafe_agent_gates)
  27/27 / 31/31; [safe-sh](https://github.com/EpicEric/safe-sh)
  static remainder; **1★**;
  [jev-pastepilot](https://github.com/buberlo/jev-pastepilot)
  Confirm before act; rh-guard owns);
  **Retrieval as calibrated decision space**
  ([Jev-Reranker](https://github.com/uspraveen/Jev-Reranker)
  live Jev not yet measured;
  [sessionwise](https://github.com/Nasrallah-AL/sessionwise)
  opt-in relevance;
  [jev-search](https://github.com/savka777/jev-search)
  pointer sieve; **≠** kazuhideoki/jev-search
  **≠** superagents-lab/jev-search);
  **Enterprise reflexes**
  ([400ms-agentic-sf](https://github.com/furuCRM-Inc/400ms-agentic-sf)
  Salesforce WebMCP;
  [typesafe-scheduler-diagnostics](https://github.com/thevilledev/typesafe-scheduler-diagnostics)
  advisory);
  **Screenshot-free / CU**
  ([droidjev](https://github.com/mkruglikov/droidjev)
  screenshot-free;
  [jevcu](https://github.com/Tewoto1/Computer-use-and-control-with-Jev)
  planner still writes);
  **Hybrid S1/S2**
  ([ha-conversation-jev](https://github.com/luxus/ha-conversation-jev)
  Jev→Grok; **1★**;
  [dsh-jev](https://github.com/buberlo/dsh-jev)
  can only gate; **2★**);
  **Harbor-jevals / SRE**
  ([jev-classification-benchmark](https://github.com/rachit-srivastava-devx/jev-classification-benchmark)
  specified not run;
  [jev-luna-pagerduty-trigger](https://huggingface.co/datasets/reachjalil/jev-luna-pagerduty-trigger)
  p≥0.50);
  **Laya densifies**
  ([meldecision](https://github.com/meldltd/meldecision)
  laya-go ONNX;
  [laya-doom](https://github.com/shantanugoel/laya-doom)
  never pixels;
  [laya-api](https://github.com/logixism/laya-api)
  empty README;
  [akpsahan/laya](https://huggingface.co/akpsahan/laya)
  ≠ Archer);
  **Demos / unofficial toolbelt**
  ([jevchess](https://github.com/choxos/jevchess)
  engine owns truth; **1★**;
  [jev-drive](https://github.com/vedssharma/jev-drive)
  sim not AV;
  [story-arc](https://github.com/amali-s/story-arc)
  Jev never authors;
  [jev-hs-assistant](https://github.com/newbie1668/jev-hs-assistant)
  HS6;
  [jev-plays-starcraft-2](https://github.com/golergka/jev-plays-starcraft-2)
  UI-verified ≠ API Victory; **1★**;
  [awesome-jev-use-cases](https://github.com/walidboulanouar/awesome-jev-use-cases)
  catalog; **2★**;
  [typesafe-go](https://github.com/Nibir1/typesafe-go)
  ≠ official). Soft Noul ≠ hard safety. 0★ HIGHs
  still get real cards. Census (user-provided; not
  re-derived): Archer still NOT landed; tracker likes
  **50** lastModified UNCHANGED
  2026-09-19T18:37:18Z; SemIf 1873 (+7); jevlike 969
  (+2); TypeAR 10 flat; Awesomejev 561/27007 flat.
  Do not copy `TYPESAFE_API_KEY` / OAuth `client_id` /
  `uv` / `npx` / `.env`. No wrapper. No invented
  metrics.
- SIGNAL fold jevcache + jev-align (`research/notes.md`
  §93): **Skip Archer.** Docs-only on a **fresh PR
  off main** after #9 merge `059f3670`. **Never
  reopen** merged #3 / #4 / #5 / #7 / #8 / **#9**.
  Do **not** re-fold 1441 / §92. How-to-apply /
  mental models / architecture / Harbor-jevals /
  toolbelt — not a thin Jev skill dump.
  Backend-agnostic categorization/scoring/decision
  class (Jev-like speed/econ). rh-guard owns
  HIT-as-truth and training-score auto-accept as
  gate cousins; Augustus owns placement. Formal
  methods compose with scoring; a HIT and a
  training score are SENSOR. Two clusters:
  **Decision ledger / memoization**
  ([hyperspaceai/jevcache](https://github.com/hyperspaceai/jevcache);
  license **null**; **8★** this pass, SIGNAL ★6;
  HEAD `a211d13`; README SHA `7c2abe99`;
  fingerprint after redact; recall vs decide;
  publish fingerprints+answers; CI replay as Harbor
  cousin; Cache hit ≠ correctness;
  hyperspaceai/jevcache ≠ kushals256/jevcache;
  memoize typed decisions; VOI of cache hit);
  **GEPA alignment loop**
  ([sutro-sh/jev-align](https://github.com/sutro-sh/jev-align);
  Apache-2.0; **60★** this pass, SIGNAL ★56; forks
  **7**; HEAD `49753df`; README SHA `363fccb7`;
  human labels only; score never auto-accepts;
  production capture flywheel; sutro-sh/jev-align ≠
  caiovicentino/jev-align; GEPA + System One). Soft
  Noul ≠ hard safety. Census (user-provided; not
  re-derived): Archer still NOT landed. Do not copy
  `TYPESAFE_API_KEY` / `uv` / `npx` / `curl | sh` /
  `.env`. No wrapper. No invented metrics.
- SIGNAL fold enzyme + JA ModernBERT + Gemma/Nemotron/djev-dev/Laya
  essay (`research/notes.md` §94): **Skip Archer.** Docs-only
  on a **fresh PR off main** after #10 merge `30438eff`.
  **Never reopen** merged #3 / #4 / #5 / #7 / #8 / #9 /
  **#10**. Do **not** re-fold jevcache/jev-align / §93.
  How-to-apply / mental models / architecture /
  Harbor-jevals / toolbelt — not a thin Jev skill dump.
  Backend-agnostic categorization/scoring/decision
  class (Jev-like speed/econ). rh-guard owns
  guidance-as-hook, unofficial-local-as-Jev,
  hosted-bootstrap silent FALLBACK,
  LFM-default-as-JA-softmax, Nemotron
  “not calibrated replacement”, and Laya
  confidence-without-competence as gate cousins;
  Augustus owns placement. Formal methods compose
  with scoring; `when asked`, unofficial local p,
  Nemotron p, and Laya 0.85 are SENSOR. Three
  clusters: **Compile-time System One /
  questions-as-index**
  ([byenzyme/enzyme](https://github.com/byenzyme/enzyme);
  license **null**; **63★** this pass, SIGNAL ★62;
  HEAD `c91d6b5`; README SHA `9af7c570`;
  guidance ≠ hook; catalysts ≠ summaries;
  compile-time System One; hosted bootstrap ≠
  silent TypeSafe; ~350×/1000× *theirs*
  (GitHub description); **≠** enzymejs/enzyme);
  **Unofficial JA ModernBERT cross-encoder**
  ([argos1111/modernbert-ja-310m-jev](https://huggingface.co/argos1111/modernbert-ja-310m-jev);
  CC-BY-SA-4.0; **2 likes**; sha `07cda235`;
  unofficial ≠ TypeSafe; format_version
  modernbert-jev/1; Argos1111/jev_local ≠
  us/jev-local ≠ kunchenguid/local-jev; LFM
  default ≠ ModernBERT backend; JGLUE JNLI
  92.62% / JComQA 92.40% *theirs*);
  **NAR class legitimacy / multimodal /
  Router-OOD**
  ([@googlegemma](https://x.com/googlegemma/status/2101069861598482817)
  ~0.2s *theirs*;
  [pst2154/Nemotron_Jev](https://github.com/pst2154/Nemotron_Jev)
  **6★**; README SHA `f2f3d052`; HEAD `983cc29` on
  `feat/nemotron-decision-lab`; Nemotron ≠ TypeSafe
  Jev; not a calibrated replacement;
  [Davipar/djev-dev](https://github.com/Davipar/djev-dev)
  Apache-2.0; **2★**; README SHA `6d59d020`;
  djev-dev complements djev-spark; images as Choice
  options;
  [Laya essay](https://laya.convaiinnovations.com/);
  Laya essay numbers *theirs*; Router/OOD
  confidence). Soft Noul ≠ hard safety. Census
  (user-provided; not re-derived): Archer still NOT
  landed. Do not copy `TYPESAFE_API_KEY` /
  `ENZYME_JEV_MODEL` / `curl | bash` / docker /
  `pip install laya`. No wrapper. No invented
  metrics.
- Hourly 1541 HIGH (`research/notes.md` §95): **Skip
  Archer.** Docs-only on a **fresh PR off main**. Never
  reopen merged #7 / **#8** / **#9** / **#10** /
  **#12**. Do **not** push onto §93 / §94. Do **not** re-fold
  1441 / §92. How-to-apply / mental models /
  architecture / Harbor-jevals / toolbelt — not a thin
  Jev skill dump. Backend-agnostic
  categorization/scoring/decision class (Jev-like
  speed/econ). rh-guard owns the injection-firewall /
  CI-gate cousins; Augustus owns placement. Formal
  methods compose with scoring; a Noul is a SENSOR;
  pasting orchestrator 0.95 / skip_below 0.05 /
  OpenRoboto $ as class ceilings, inventing
  one-dollar-tahoe ASR/FPR, or treating numbered-choice
  softmax as a Noul is soundness theater. Six clusters:
  **Decision-as-plugin for SWE**
  ([petercr/jev-orchestrator](https://github.com/petercr/jev-orchestrator)
  difficulty + policy thresholds + JSONL trace; **0★**;
  [Charlyhno-eng/jev-codex-pilot](https://github.com/Charlyhno-eng/jev-codex-pilot)
  model + reasoning depth; **0★**;
  [SunnyKikiHK/jev-replacement](https://github.com/SunnyKikiHK/jev-replacement)
  keep/shadow/hybrid/reject; license null; **0★**);
  **Evidence projection**
  ([jackboykin/quarry](https://github.com/jackboykin/quarry)
  quarry evidence projection; Go MIT; **0★**; **master**);
  **Soft judgment integrity**
  ([seb4ez/jevguard](https://github.com/seb4ez/jevguard)
  calibrator/cache/escape; **0★**;
  [guilhem/jev-ci-selector](https://github.com/guilhem/jev-ci-selector)
  CI shadow mode; license null; **0★**; rh-guard owns);
  **Physical/control first-class domain**
  ([Frank-ZY-Dou/awesome-jev](https://github.com/Frank-ZY-Dou/awesome-jev)
  Frank-ZY-Dou/awesome-jev robotics/3D/control; license
  null; **0★**; text-state, not pixels);
  **Harbor-jevals / injection-firewall**
  ([PavitarSinghArneja/one-dollar-tahoe](https://github.com/PavitarSinghArneja/one-dollar-tahoe)
  TypeSafe Jev defense eval; **0★**; ~74 demo; README
  has no ASR/FPR; rh-guard owns);
  **llama.cpp replica**
  ([webNeat/llama-jev](https://github.com/webNeat/llama-jev)
  llama.cpp replica; license null; **0★**; softmax ≠
  Noul). Soft Noul ≠ hard safety. 0★ HIGHs still get
  real cards. Census **not provided this hour** (not
  re-derived). Archer still NOT landed. Do not copy
  `TYPESAFE_API_KEY` / `AI_GATEWAY_API_KEY` /
  `EXA_API_KEY` / `GROQ_API_KEY` / `uv` / `npx` /
  `go install` / `.env` / `attacks.json`. No wrapper.
  No invented metrics.
- Hourly 1639 HIGH (`research/notes.md` §96): **Skip
  Archer.** Docs-only on a **fresh PR off main**. Never
  reopen merged #7–**#13**. Do **not** re-fold 1541 /
  §95. How-to-apply / mental models / architecture /
  Harbor-jevals / toolbelt — not a thin Jev skill dump.
  Backend-agnostic categorization/scoring/decision
  class. Formal methods compose with scoring; a Noul
  is a SENSOR; treating zen-chat as calibrated Jev,
  pasting tamaratran 24/24 onto this host, or
  hard-gating keepThreshold 0.5 as proof of
  irrelevance is soundness theater. One HIGH cluster:
  **OpenCode host-port of evidence-preserving stdout
  prune**
  ([indiejoseph/opencode-jev-pruner](https://github.com/indiejoseph/opencode-jev-pruner)
  OpenCode jev-pruner context sieve;
  observe→score-candidates→prune; jev-zen /
  jev-1.13-free; zen-chat ≠ Noul; fail-open original;
  keepScore >0.1 floor; GitHub license **null**;
  `package.json` MIT; **0★**; HEAD `764169c`
  **master**). MEDIUM watch (do not over-weight):
  [jongyunhur/jev-webagent-bench](https://github.com/jongyunhur/jev-webagent-bench)
  empty stub; [Kiln-AI/jev_jsonschema](https://github.com/Kiln-AI/jev_jsonschema)
  noul_threshold 0.5 (**5★**); [NSStudent/JevSwiftSDK](https://github.com/NSStudent/JevSwiftSDK)
  unofficial (**5★**). Soft Noul ≠ hard safety. Census
  **not provided this hour** (not re-derived). Archer
  still NOT landed. Do not copy `TYPESAFE_API_KEY` /
  `OPENCODE_API_KEY` / `npx` / plugin marketplace.
  No wrapper. No invented metrics.
- SIGNAL gliner-native-runtime (`research/notes.md` §97):
  **Skip Archer.** Docs-only on a **fresh PR off main**.
  Never reopen merged #7–**#14**. Do **not** re-fold 1639
  / §96. How-to-apply / mental models / architecture /
  Harbor-jevals / toolbelt — not a thin Jev skill dump.
  Backend-agnostic categorization/scoring/decision class.
  User-linked SIGNAL (pushed 2026-08-26). Formal methods
  compose with scoring; span confidence is a SENSOR;
  treating this as TypeSafe Choice/Score/Noul, collapsing
  it into Fastino official, or hard-gating default 0.1 as
  NER quality is soundness theater. One HIGH cluster:
  **GLiNER2 native Apple path**
  ([shershah1024/gliner-native-runtime](https://github.com/shershah1024/gliner-native-runtime)
  unofficial Swift/Core ML GLiNER 2.5-small; entity spans
  + confidence; not Choice/Score/Noul; not TypeSafe;
  label descriptions as schema; on-device ANE economics;
  honesty locks; Apache-2.0; **4★**; HEAD `b44f661`;
  README SHA `901eb063`). Soft Noul ≠ hard safety.
  default threshold 0.1 still soft. Census **not provided
  this hour** (not re-derived). Archer still NOT landed.
  Do not copy `swift build` / Git LFS / Hub weights.
  No wrapper. No invented metrics.
- Hourly 1740 HIGH (`research/notes.md` §98): **Skip
  Archer rewrite.** Docs-only on a **fresh PR off main**.
  Never reopen merged #7–**#15**. Do **not** re-fold 1639
  / §96 / gliner-native-runtime / §97 / 1541 / §95. How-to-apply
  / mental models / architecture / Harbor-jevals / toolbelt —
  not a thin Jev skill dump. Backend-agnostic
  categorization/scoring/decision class. Formal methods
  compose with scoring; a Noul is a SENSOR; hard-gating DGP
  as safety theater, hard-gating 0.4/0.2 as “concept absent,”
  treating OpenRouter/TypeSafe auto-failover as one Noul
  (silent FALLBACK), or pasting kev OOD 0.76 as
  Jev-equivalent is soundness theater. Three HIGH clusters: **Decision Graph Protocol
  envelope**
  ([numerous-com/dgp](https://github.com/numerous-com/dgp)
  Decision Graph Protocol frame→assess→commit; app retains
  permissions/effects; Jev-first assessor-neutral; guarded
  commit / receipt/next frame; assessment batching;
  numerous-com/dgp ≠ TypeSafe official; Python MIT; **0★**;
  HEAD `a9cb3c4`; README SHA `655fc638`); **calibrated
  meaning-grep over a live tree**
  ([can1357/jegrep](https://github.com/can1357/jegrep)
  jegrep calibrated path+range Nouls; no
  embeddings/index/daemon; ~$0.01–0.03 typical; agent --json;
  can1357/jegrep ≠ Bentlybro/jevgrep ≠ uehaj/jev-semgrep;
  Rust MIT; **13★**; HEAD `a280f14`; README SHA `6f241390`);
  **Archer-arch fidelity + measured calibration gap**
  ([jaredpalmer/kev](https://github.com/jaredpalmer/kev)
  Archer-arch fidelity; kev family OOD 0.76–0.77 vs Jev 0.86;
  block-causal isolation; pointer/readout CE-trained;
  /v1/systemone drop-in; replica honesty; Apache-2.0; **507★**;
  do not rewrite §45; Jev-omni owns the replica fold). Soft
  Noul ≠ hard safety. 0★ HIGH still got a real card. Census
  **not provided this hour** except Archer tracker likes
  **51** (+1); lastModified UNCHANGED 2026-09-19T18:37:18Z;
  Hub `archerhume/4rcherhume` HTTP **401**. Archer still NOT
  landed. Do not copy keys / `uv` / `cargo` / `.env`. No
  wrapper. No invented metrics.
- Hourly 2145 HIGH (`research/notes.md` §102): **Skip
  Archer rewrite.** Docs-only on a **fresh PR off main**.
  Never reopen merged #7–**#19**. Do **not** re-fold 2041
  / §101 / 1943 / §100 / 1843 / §99 / 1740 / §98 / 1639
  / §96 / gliner-native-runtime / §97 / 1541 / §95 /
  jev-align *mechanism* / §93. How-to-apply / mental
  models / architecture / Harbor-jevals / toolbelt — not
  a thin Jev skill dump. Backend-agnostic
  categorization/scoring/decision class. Formal methods
  compose with scoring; a Noul is a SENSOR; treating a
  clean jevq run as measured separation, treating 62
  IC-Laya tests as Laya parity, letting a Score grant Tx,
  pasting “Jev48 beats Jev on phishing” from AUROC,
  injecting class priors as “help”, treating v4 as a
  pharmacy controller, distilling Jev as teacher of
  record, pasting maze 1.00 as a general System One, or
  treating jev-kit exit 0 as claim truth is soundness
  theater. Nine HIGH clusters: **question-linting of Jev
  questions themselves**
  ([yodablocks/jevq](https://github.com/yodablocks/jevq)
  PRIMARY; nine jaggedness rules, no API key, no labelled
  data; static lint ≠ measured separation;
  yodablocks/jevq ≠ tenbin ≠ JevLint ≠ commitjev; Python
  MIT; **0★**; HEAD `40b2dd90`; README SHA `3198dde0`);
  **open-weights Laya as class exemplar (binding)**
  ([ChristianAlexander/laya_ex](https://github.com/ChristianAlexander/laya_ex)
  Nx/Bumblebee runtime; host chooses backend; Elixir
  Apache-2.0; **0★**; HEAD `99f9ce73`; README SHA
  `6361c920`; mix **0.1.0**);
  **on-chain/edge Laya deploy**
  ([humandebri/IC-Laya](https://github.com/humandebri/IC-Laya)
  parity_verified stays false; model output never grants
  Tx; Rust MIT; **0★**; HEAD `055ef42f`; README SHA
  `85431606`); **auditable weekend replica**
  ([agilabs-ai/jev48](https://github.com/agilabs-ai/jev48)
  Jev outputs never used for training; unpaired 0.577 vs
  0.727; Python MIT; **0★**; HEAD `aa697005`; README SHA
  `3f667dd4`); **adversarial dual-judge / framing**
  ([copyleftdev/ember](https://github.com/copyleftdev/ember)
  comparative framing is the usable judgment; prior
  injection crowds out evidence; TypeScript MIT; **0★**;
  HEAD `c02f622b`; README SHA `6db00b56`); **Laya
  specialist + Hub replica**
  ([PIXELZX0/XERON](https://github.com/PIXELZX0/XERON)
  training still GPU-pending; license null; **0★**; HEAD
  `5e870a4d`) +
  ([daliborsb/laya](https://huggingface.co/daliborsb/laya)
  Hub Laya replica drop; ≠ convaiinnovations/laya);
  **distillation economics**
  ([MagaBitmex/jev-4b-distill-data](https://huggingface.co/datasets/MagaBitmex/jev-4b-distill-data)
  gold is programmatic; teacher is closed-API clone; do
  not distill Jev as teacher of record; student checkpoint
  missing); **non-LLM VIN System One**
  ([lewislululu/jevon](https://huggingface.co/lewislululu/jevon)
  planning depth not chat; maze 1.0000 n=141 *theirs*;
  AGPL; likes **3**; ≠ douglance/jevon); **source-bound
  evidence**
  ([WaynezProg/jev-kit](https://github.com/WaynezProg/jev-kit)
  local quote mismatch needs no API; exit 0 ≠ claim
  truth; MIT; **0★**; HEAD `4558554f`; README SHA
  `a7f14838`; ≠ jonathanavis96/jev-kit Airlock). Soft
  Noul ≠ hard safety. 0★ HIGH still
  got a real card. Census **live REST pulse** (review
  relock): SemIf **2000★** (+16 vs §101 **1984**);
  jevlike **1002★** **flat**; TypeAR **12★** (+1 vs
  §101 **11**). Tracker likes **54**;
  lastModified `2026-09-20T02:59:13Z`; Hub
  `archerhume/4rcherhume` HTTP **401** (not re-fetched as
  a rewrite). Archer still NOT landed. Awesomejev
  561/27007 user-provided (≠ AnotiaWang/awesome-jev
  **86★**). Qwen3.8-27B ≠ Archer.
  `invented_signal: false`. Do not copy keys / `npm` /
  `pip` / `npx` / `uv` / `mix` / `curl | sh`. No wrapper.
  No invented metrics.
- Hourly 2246 HIGH (`research/notes.md` §103): **Skip
  Archer rewrite.** Docs-only on a **fresh PR off main**.
  Never reopen merged #7–**#20**. Do **not** re-fold 2145
  / §102 / 2041 / §101 / 1943 / §100 / 1843 / §99 / 1740
  / §98 / 1639 / §96 / gliner-native-runtime / §97 / 1541
  / §95 / jev-align *mechanism* / §93. How-to-apply /
  mental models / architecture / Harbor-jevals / toolbelt
  — not a thin Jev skill dump. Backend-agnostic
  categorization/scoring/decision class. Formal methods
  compose with scoring; a Noul is a SENSOR; treating a
  catalog row as a bake-off win, treating constructed
  scenes as production logs, pasting Hev 80.00% as Jev
  identity, quoting mini-jev 93.25% as family-disjoint,
  putting Jev in an AR next-token loop, laundering a Noul
  as a Lean step, treating parallel rank-k as a sort
  proof, pasting a curated list’s von sub-15ms as an
  Augustus fact, or hard-thresholding paper-radar 0.5 as
  frequency is soundness theater. ChatJev-style soundness
  theater is the anti-pattern. Nine HIGH clusters:
  **independent System One evidence catalog**
  ([reachjalil/system-one-bench](https://github.com/reachjalil/system-one-bench)
  PRIMARY; 19 reviewed records; scores not one leaderboard; no external record
  currently reproduced; TokenTrim no-Jev matched hybrid
  62.4%; JavaScript MIT; **0★**; HEAD `ceb17269`; README
  SHA `d9e0c7b7`; ≠ mallahyari/system-one-benchmark);
  **typed eval freeze**
  ([SivletLabs/jev-eval](https://github.com/SivletLabs/jev-eval)
  21 tasks · 134 items · 208 questions; scenes from public
  GitHub contracts, not production logs; Python MIT;
  **0★**; HEAD `3f9d976f`; README SHA `df16766c`; ≠
  willkelly/jev-evaluation ≠ 4esv/jev-eval);
  **option-isolated tiny replica**
  ([nafisazizir/hev](https://github.com/nafisazizir/hev)
  option isolation (sibling-blind); permutation-equivariant;
  Hub OWNER not published; Apache-2.0; **0★**; HEAD
  `79a486f9`; README SHA `b995dce3`; ≠ jaredpalmer/kev);
  **frozen-LLM typed decisions**
  ([yuki-oshio/mini-jev](https://github.com/yuki-oshio/mini-jev)
  frozen local LLM logits, no trained decision head;
  residual-head 9,222-param decreased 73/96→67/96;
  confidence = 1−normalized entropy, not P(correct);
  Python MIT; **0★**; HEAD `dff5b323`; README SHA
  `363441b6`; ≠ r-ms/mini-jev);
  **AR next-token anti-pattern**
  ([erik-dunteman/ChatJev](https://github.com/erik-dunteman/ChatJev)
  Jev classifier as autoregressive next-token predictor;
  ChatJev-style soundness theater; license null; **1★**;
  HEAD `ea33ab8d`; README SHA `c763be19`; ≠ dannote/jev ≠
  jev-gpt);
  **formal compose with scoring**
  ([wufuju2023-cell/jev-alpha-proof-analysis](https://github.com/wufuju2023-cell/jev-alpha-proof-analysis)
  calibrated decision head × AlphaProof value head;
  implementation-layer isomorphism, semantic difference;
  timeout = censoring; do not launder Noul as proof;
  license null; **0★**; HEAD `afd9bb6f`; README SHA
  `1810d7f6`);
  **parallel rank vs serial selection**
  ([zzzzzec/jevsort](https://github.com/zzzzzec/jevsort)
  parallel rank-prediction vs serial selection;
  independent questions can conflict; HTML; license null;
  **1★**; HEAD `57067b90`; README SHA `85044740`; ≠
  keltokhy/jsort);
  **open-side ecosystem catalog**
  ([rupeshpoojary9/awesome-open-system-one](https://github.com/rupeshpoojary9/awesome-open-system-one)
  curated open System One ecosystem catalog; CC0 1.0;
  SPDX NOASSERTION; **0★**; HEAD `637ee3d3`; README SHA
  `0007e343`; ≠ AnotiaWang/awesome-jev);
  **knowledge-work paper radar**
  ([LYchoon/paper-radar-jev](https://github.com/LYchoon/paper-radar-jev)
  arXiv paper radar with Jev relevance scoring; ranking ≠
  calibration / 0.5 still soft; fail-open failed evals
  not marked seen; Python MIT; **0★**; HEAD `fbadf01c`;
  README SHA `1cb8a9c3`; size **73**; default master).
  Soft Noul ≠ hard safety. 0★ HIGH still got a real card
  (jevsort **1★**). Census **live REST pulse** (review
  relock): SemIf **2019★** (+19 vs §102 **2000**);
  jevlike **1006★** (+4 vs §102 **1002**); TypeAR **12★**
  **flat**. Tracker likes **54**; lastModified
  `2026-09-20T02:59:13Z`; Hub `archerhume/4rcherhume`
  HTTP **401** (not re-fetched as a rewrite). Archer
  still NOT landed. Awesomejev 561/27007 user-provided
  (≠ AnotiaWang/awesome-jev **87★**). Qwen3.8-27B ≠
  Archer. `invented_signal: false`. Do not copy keys /
  `npm` / `pip` / `npx` / `uv` / `.env`. No wrapper.
  No invented metrics.
- Hourly 2041 HIGH (`research/notes.md` §101): **Skip
  Archer rewrite.** Docs-only on a **fresh PR off main**.
  Never reopen merged #7–**#18**. Do **not** re-fold 1943
  / §100 / 1843 / §99 / 1740 / §98 / 1639 / §96 /
  gliner-native-runtime / §97 / 1541 / §95 / jev-align
  *mechanism* / §93. How-to-apply / mental models /
  architecture / Harbor-jevals / toolbelt — not a thin
  Jev skill dump. Backend-agnostic
  categorization/scoring/decision class. Formal methods
  compose with scoring; a Noul is a SENSOR; treating a
  zero binary name gap as a fairness certificate, letting
  Jev emit the verdict string, pasting PrismNLI's lead
  without the contamination caveat, treating J7 pass as
  safe to obey, treating a receipt as authorization, or
  hard-gating confidence ≥0.95 is soundness theater. Nine
  HIGH clusters: **resume-screening bias audit**
  ([natemoo-re/bias-bench](https://github.com/natemoo-re/bias-bench)
  PRIMARY; name×resume factorial independent Nouls;
  callback determined by resume quality; mean-probability
  name gaps operationally negligible; natemoo-re/bias-bench
  ≠ BBQ; JavaScript; license null; **0★**; HEAD
  `fe2f2535`; README SHA `a1c3e604`); **MCDA panel
  code-owned verdict**
  ([austindixson/planalyzer](https://github.com/austindixson/planalyzer)
  Plan/PRD panel → code-owned pass|review|block;
  cheerleading out of scope; Python MIT; **0★**; HEAD
  `39fc161f`; README SHA `6e4d8da3`); **EU cost-aware
  routing**
  ([cannacre8ive/switchboard-ai](https://github.com/cannacre8ive/switchboard-ai)
  cost-aware multi-model routing/escalation; decide vs do;
  successful-task cost; JavaScript MIT; **1★**; HEAD
  `5cae9d1c`; README SHA `872de837`; package **0.4.0**);
  **frozen-protocol class bake-off**
  ([elcronos/jev-vs-open-decision-models](https://github.com/elcronos/jev-vs-open-decision-models)
  TypeSafe Jev vs PrismNLI vs Laya; contamination caveat;
  Python; license null; **0★**; HEAD `b61e6cfc`; README
  SHA `b7256888`); **VOI admission**
  ([cvsgireesh/jevusher](https://github.com/cvsgireesh/jevusher)
  context-window admission control; fail polarity per
  lens; on small inputs lenses lose money; TypeScript MIT;
  **0★**; HEAD `d830d344`; README SHA `428a4a59`);
  **Leveson control plane**
  ([MokiMeow/jev-fabric](https://github.com/MokiMeow/jev-fabric)
  typed decision control plane; receipt ≠ authorization;
  historical-v0 zero retained cases; Apache-2.0; **0★**;
  HEAD `95b9a4f3`; README SHA `f485dbdd`); **scoring
  economics**
  ([jose-troche/live-rubric](https://github.com/jose-troche/live-rubric)
  live 15-dim typed rubric re-score per pause; OpenJev/Codiv
  ≠ TypeSafe hosted; ~$0.000004 desc / ~$0.000006 README;
  TypeScript; license null; **0★**; HEAD `db8da8db`;
  README SHA `4a0be084`); **pre-registered calibration
  science**
  ([willkelly/jev-evaluation](https://github.com/willkelly/jev-evaluation)
  28 predictions before data; 123,805 requests; confidence
  does not track ignorance; polite injection 65% / crude
  0%; Python MIT; **0★**; HEAD `c168c093`; README SHA
  `2d66ac22`; rh-guard owns injection); **class
  infrastructure SDK**
  ([nshkrdotcom/system_one_sdk](https://github.com/nshkrdotcom/system_one_sdk)
  provider-neutral Elixir/BEAM Noul/Choice/Score SDK;
  GitHub desc provider-neutral / README TypeSafe-first;
  Elixir MIT; **0★**; HEAD `c2a522ee`; README SHA
  `c117b4c4`; mix **0.5.0**). Soft Noul ≠ hard safety.
  0★ HIGH still got a real card (switchboard now **1★**
  live REST). Census **live REST pulse**: SemIf **1984★**;
  jevlike **1002★**; TypeAR **11★** flat. Tracker likes
  **54** (+3 vs §100 pin **51**); lastModified **CHANGED**
  2026-09-20T02:59:13Z; Hub `archerhume/4rcherhume` HTTP
  **401** (not re-fetched as a rewrite). Archer still NOT
  landed. Awesomejev 561/27007 user-provided (≠
  AnotiaWang/awesome-jev 84★).
  `invented_signal: false`. Do not copy keys / `npm` /
  `pip` / `npx` / `uv` / `mix`. No wrapper. No invented
  metrics.
- Hourly 1943 HIGH (`research/notes.md` §100): **Skip
  Archer rewrite.** Docs-only on a **fresh PR off main**.
  Never reopen merged #7–**#17**. Do **not** re-fold 1843
  / §99 / 1740 / §98 / 1639 / §96 / gliner-native-runtime
  / §97 / 1541 / §95 / jev-align *mechanism* / §93.
  How-to-apply / mental models / architecture /
  Harbor-jevals / toolbelt — not a thin Jev skill dump.
  Backend-agnostic categorization/scoring/decision class.
  Formal methods compose with scoring; a Noul is a SENSOR;
  hard-gating `feels` 80%, pasting 17/18 as Harbor,
  hard-gating 0 of 157, treating boolean @ 0.5 as a proof,
  claiming 10×, treating softmax as a Noul, or treating 62
  tests as quality is soundness theater. Six HIGH clusters:
  **Jev IS the if-statement**
  ([southpolesteve/probably](https://github.com/southpolesteve/probably)
  PRIMARY; judgments/probabilities drive branches; text
  model only writes prose; interpreter owns
  variables/loops/budgets/replay; otherwise maybe /
  confidence gate; chaos samples after the gate;
  southpolesteve/probably ≠ carldaws/hunch ≠ feelings ≠
  Kungie/gut ≠ Illusion47586/judge ≠ tidymodels/probably;
  TypeScript MIT; **3★**; HEAD `6bf671a4`; README SHA
  `c28570a9`); **GEPA live delta**
  ([sutro-sh/jev-align](https://github.com/sutro-sh/jev-align)
  133★ / forks 10 live; build calibrated classifiers from
  human feedback; HEAD `49753df9` / README SHA `363fccb7`
  unchanged vs §93); **retrieve by relevance not
  resemblance**
  ([samdotmak/jev-recall](https://github.com/samdotmak/jev-recall)
  one calibrated yes/no per memory in one request; pointer
  mode 17/18 19/20 *theirs*; embedding resemblance misses
  the allergy; MIT; **6★**; HEAD `d3e4acfb`; README SHA
  `ea774519`); **memory leases ended by new evidence**
  ([chopratejas/invalidate](https://github.com/chopratejas/invalidate)
  HIGH upgrade; six Nouls then fixed rules in code; 0 of
  157 false invalidations; questions/plans/directives are
  not evidence; unsure → review queue; host keeps the
  store; Apache-2.0; **11★**; HEAD `d6ade601`; README SHA
  `8cccad5f`); **contract-of-artifact lint rename**
  ([mizchi/jev-lint](https://github.com/mizchi/jev-lint)
  is mizchi/jevlint rename; name↔body / comment truth /
  test-claims; no shipped rule has severity error; ~1 in 5
  findings wrong *theirs*; TypeScript MIT; **13★**; HEAD
  `62d73f8e`; README SHA `4c0e37cd`); **JSON Schema
  question compiler**
  ([Kiln-AI/jev_jsonschema](https://github.com/Kiln-AI/jev_jsonschema)
  HIGH upgrade; JSON Schema → typed JSON via Jev;
  noul_threshold 0.5 decoder not a proof;
  IncompatibleSchemaError lists every bad property; MIT;
  **5★**; HEAD `fccea8c2` unchanged); **local System One
  economics**
  ([mizorewww/laya-coreml](https://github.com/mizorewww/laya-coreml)
  on-device Laya CoreML ANE; ~5 ms P50 short decisions;
  189/189 FP16 checkpoint parity; 10× not achieved;
  Apache-2.0; **0★**; HEAD `47f4baf0`; README SHA
  `2068c661`) +
  ([Micha0827/snapjudge](https://github.com/Micha0827/snapjudge)
  softmax over allowed tokens ≠ Noul; question-first
  cache; Python MIT; **3★**; HEAD `2df5ce27`; README SHA
  `64a91458`) +
  ([direwolfiy/JevPi](https://github.com/direwolfiy/JevPi)
  Jev-first Pi agent loop; slow-LLM fallback; explicit
  action menu / CandidateSource unimplemented; 62 tests
  wiring not quality; license null; **0★**; HEAD
  `980f8895`; README SHA `88ec1a55`). Soft Noul ≠ hard
  safety. 0★ HIGH still got a real card. Census **live
  REST pulse**: SemIf **1954★**; jevlike **989★**; TypeAR
  **11★** flat. Tracker likes **51** flat; lastModified
  UNCHANGED 2026-09-19T18:37:18Z; Hub
  `archerhume/4rcherhume` HTTP **401** (not re-fetched as
  a rewrite). Archer still NOT landed. Awesomejev
  561/27007 user-provided (≠ AnotiaWang/awesome-jev 83★).
  `invented_signal: false`. Do not copy keys / `bun` /
  `pip` / `npx` / `uv` / HF download. No wrapper. No
  invented metrics.
- Hourly 1843 HIGH (`research/notes.md` §99): **Skip
  Archer rewrite.** Docs-only on a **fresh PR off main**.
  Never reopen merged #7–**#16**. Do **not** re-fold 1740
  / §98 / 1639 / §96 / gliner-native-runtime / §97 /
  1541 / §95. How-to-apply / mental models /
  architecture / Harbor-jevals / toolbelt — not a thin
  Jev skill dump. Backend-agnostic
  categorization/scoring/decision class. Formal methods
  compose with scoring; a Noul is a SENSOR; hard-gating
  cost-derived 0.038 as a proof, merging von Needle
  52.6% with n=78 93%, “guaranteeing” calibration, or
  pasting “Jev wins guardrailing” is soundness theater.
  Five HIGH clusters: **cost-derived YES/NO/UNSURE
  control flow**
  ([Kungie/gut](https://github.com/Kungie/gut)
  PRIMARY; cost-sensitive decision theory × System One
  probabilities → control flow; thresholds derived from
  costs not hard-coded; YES / NO / UNSURE from
  cost_false_yes / cost_false_no / cost_human;
  auto-batching same-object questions; Kungie/gut ≠
  tpellet/hunch ≠ carldaws/hunch; GitHub Apache-2.0 /
  LICENSE MIT / pyproject Apache-2.0 *theirs*; **0★**;
  HEAD `cb56c875`; README SHA `630474f6`; pre-alpha);
  **typed-callback twin**
  ([Illusion47586/judge](https://github.com/Illusion47586/judge)
  judgment vs generation; deterministic execution after
  probabilistic judgment; exactly one app-owned
  callback; explicit uncertain branch;
  Illusion47586/judge ≠ lexingtonhibiki/judgekit ≠
  Ascurse/typed-judge-kit; TypeScript MIT; **0★**; HEAD
  `e69f65a1`; README SHA `08554c6f`; `@brkn-labs/judge`
  0.1.0); **variable-N option scoring as the trainable
  object**
  ([zwliJay/jev-forge](https://github.com/zwliJay/jev-forge)
  dynamic candidate bags not fixed label sets;
  zwliJay/jev-forge ≠ NanoJev; class-architecture note,
  not a sixth species; GitHub NOASSERTION / LICENSE MIT;
  **1★**; HEAD `eb3e4a2d`; README SHA `359f3f57`; do not
  clone Hub weights); **open NAR replica economics**
  ([wfzyx/von](https://github.com/wfzyx/von) late-catch
  HIGH of the same repo; NAR local drop-in; open replica
  economics / latency vs closed Jev; competing NAR
  claims / replica honesty; Apache-2.0; **43★**; HEAD
  `b9e42b26`; README SHA `574aa628`; do not merge Needle
  52.6% with n=78 93.0%); **typed vs chat judges on
  guardrailing**
  ([ishaannk/llm-vs-jev](https://github.com/ishaannk/llm-vs-jev)
  cross-note only; nothing wins outright; can be argued
  out of guarding; deeper integrity fold is rh-guard;
  Apache-2.0; **0★**; HEAD `182e0864`; README SHA
  `d9ebd40f`). gut/judge are **control-flow /
  decision-theory overlays, not new class-table
  species**. Soft Noul ≠ hard safety. 0★ HIGH still got
  a real card. Census **live REST quoted**: SemIf
  **1936★**; jevlike **983★** (watch claimed 984);
  TypeAR **11★** flat. Tracker likes **51** flat;
  lastModified UNCHANGED 2026-09-19T18:37:18Z; Hub
  `archerhume/4rcherhume` HTTP **401**. Archer still NOT
  landed. Awesomejev 561/27007 user-provided (≠
  AnotiaWang/awesome-jev 83★). X MCP `since_id` held;
  pages_archived 0; no invented tweets.
  `invented_signal: false`. Do not copy keys / `pip` /
  `npm` / `uv` / Hub download. No wrapper. No invented
  metrics.
- Effect-oriented loops (`notes.md` §28, `mappings.md` §19): Ward's
  ZIO client keeps Jev as the outer Choice and the handler as the
  effect. Not Effect.ts. GLiNER author: GLiNER2 "like jev" is GLiGuard
  schema-conditioned categorize, not a Noul.
- Boundary-audit stop conditions for TOCTOU-of-Noul and vacuous specs;
  FAQ rows for Alloy vs Apalache and PufferLib-as-DST-trio
- Research pointer to [dayhaysoos/jevals](https://github.com/dayhaysoos/jevals):
  local MIT workbench for Jev questions vs labeled Noul/Choice/Score cases
  (compare runs, WebMCP + agent skill). Empirical acceptance-test surface
  for Hypothesis mapping cards; complements `evaluate_decisions.py`. Not a
  jevals how-to (`research/notes.md` §24; one sentence in `validation.md`)
- Mental-models card: Augustus is design judgment across AI, SWE,
  business, knowledge work, and life — not SWE-only. Pillars: expected
  utility / selective classification, calibration and cost-sensitive
  thresholds, VOI, MCDA, search/control substitutions, signal detection,
  Leveson org/safety, NATM/snap-fit/Norman/Kent/Shirky as general
  intuition. Domain gallery labeled Hypothesis except launch-week
  Empirical SWE rows.
- Archer Hume architecture reconstruction (17 Sep 2026 essay, ~10k
  probes of `jev-1.13.0`): direct readout vs generated confidence,
  isolated questions, listwise IIA and order sensitivity, confidence as
  arithmetic on the distribution. Independent envelope probe; does not
  override live TypeSafe docs. Announced open-weight drop is **WATCH**
  (27B dense, AU healthcare residency, prefers "decision models"; still
  no Hub weights). `research/notes.md` §31, §33; `judgment-class.md`
  when-to-use table; FAQ confidence / surfaces questions.
- Entropy as allocator (**Hypothesis**, `judgment-class.md`): Atallah's
  low / medium / high buckets place System One on typed decisions and a
  frontier decoder on high-entropy synthesis — same axis as marginals
  vs joint and as VOI. "Review this PR" as medium is still partly
  generative; "first model ever" is a claim. `research/notes.md` §38
- Marginals, not a probabilistic program (`judgment-class.md`, FAQ):
  Erik Meijer — Jev is a cool API and not a PPL; Kleisli qualifications
  exaggerate; "Jev gives you the marginals; a decoder gives you the
  joint." Joints and invariants stay with TLA+ / Alloy / contracts.
  `research/notes.md` §34
- Bespoke Nimble: open contrastive recipe, not a Jev distill. Model
  card Apache-2.0 LoRA on Qwen3.5-9B (repo license absent). Their
  324-example holdout is a named receipt (Nimble 90.12%, Jev 1.13.0
  93.21%), not a ranking. 9B-vs-Jev on your labels stays Hypothesis.
  `research/notes.md` §35; one sentence in `validation.md`
- djev-spark: third compute graph (diffusion structured reads,
  Jev-shaped I/O, image-in). Empirical as the public interface;
  Hypothesis that it beats a decision head on your task. Archer's
  multimodal drop stays WATCH. `research/notes.md` §36
- Perception specialist then judgment specialist vs shared multimodal
  System One (**Hypothesis**): SAM 3.1 (masks and tracks) or an ASR
  transcript, then typed decisions on that state, is an application
  pattern, not native omni. Information dies at the interface. Prefer
  a shared multimodal decision model when the joint matters (Archer
  Watch, not Empirical; djev-spark images; future audio). Basit ask,
  primary post not retrieved. `research/notes.md` §39
- Perception→decision pipeline, measure, and hill-climb
  (**Hypothesis**, `validation.md`): stages with a versioned state
  contract; stage metrics plus a frozen taskset; HoH changes one stage
  or one interface. DSPy/Ax only on LM-program knobs; jevals and
  calibration for the decision slice; Harbor names product
  end-to-end, not a tutorial. `research/notes.md` §41
- Eval & hill-climb (`validation.md`): jevals decision-stage hygiene
  (independent keys, correctness is not confidence, held-out, immutable
  runs) and Harbor as the product taskset substrate; one composition
  table. `research/notes.md` §40

### Changed

- Skill description rewritten as trigger conditions (mixed architecture,
  prefilter, routing, preference lint, classification skepticism, family
  choice including GLiNER/GLiClass/listwise/vision) plus an explicit `not_for`
  against the official `typesafe-ai` skill
- Identity lock vs neighbor skills (`typesafe-ai`, `tenbin`, `decision-first`)
  so Augustus stays the design-judgment layer — class-wide, not TypeSafe-only
- Design cards name hole, family, and typed judgment provider (Jev default;
  other family only with self-eval)
- Protocol fan-out step is family-aware (Jev batch, GLiClass one-pass,
  dual-encoder prompt scoring); ranking vs decision fail policy is a
  non-negotiable
- Protocol and FAQ branch for "formally verify with Jev"; methods-catalog
  and composition-algebra verifier position point at the ownership split
- Skill mission and description are domain-general (AI / SWE / business /
  knowledge work / life); FAQ "is this only for software?"; mappings.md
  beyond-SWE examples labeled Hypothesis; boundary-audit red flags for
  TOCTOU-of-Noul and vacuous specs; formal-methods expanded with Alloy vs
  Apalache and the DST trio including PufferLib; GLiNER promoted from
  cousin footnote to species-map peer

### Fixed

Adversarial review of the whole skill against its own non-negotiables
(findings in `research/notes.md` §27).

- Gate fail policy is per action, not universally open
  (`composition-algebra.md` position 3, `agent-self-assessment.md`):
  advisory guards fail open *because* an interlock sits underneath;
  selection and authorization gates fail closed
- Dual-orchestration topology A selects from a closed catalog instead of
  "planning" MCP calls, which contradicted the standing planner rejection
- Species map applied to the skill's own advice: GLiClass (categorize) is
  the large-catalog substitute for a 255-option Choice; GLiNER spans are
  not (`SKILL.md`, `judgment-class.md`, `applied-mappings.md`)
- Han Xiao trolley relabeled an Empirical **rejection** (one tweet, no
  repo), not a recipe
- openjev-lm caveat moved to the figure it belongs to: 92.9% is against 70
  hand-labelled gold, 98.1% is teacher *agreement*
- Contract surface removed from design cards: the Ax constructor call and
  the `instructions` key enumeration point at live docs instead
  (`optimizer-integration.md`, `question-design.md`)
- `mappings.md` preamble no longer claims uniform Hypothesis where card
  bodies say Contract/Empirical; §17 forbids reusing jevgate's ≤0.18 as a
  constant; all Hypothesis-range references aligned to §6–§19
- Ownership split labeled Contract in `toolbox-mapping.md`, matching
  `mappings.md` §8; done-check splits structure from the Noul

Second pass on `7b3a0c3` (`research/notes.md` §43). Zero blockers.
Dropped the unpublished `npx jevals` line; SAM and ASR are upstream
producers, not the perceive species; removed two call shapes from
`optimizer-integration.md`; tagged the $0.042/MTok cell as a vendor
figure; marked GodsBoy 94.4% exploratory.
- Skill description gained trigger terms for boundary audit, question
  diagnosis, agent self-supervision, and optimizer placement

## [0.2.0] - 2026-09-18

Pegged against [`typesafe-ai/skills` v0.5.7](https://github.com/typesafe-ai/skills/tree/v0.5.7)
(`65a39f3`, 2026-09-12).

### Added

- Boundary-audit card for existing systems: three-way split (exact /
  bounded judgment / generation), code-smell catalog, fit test, opportunity
  map, smallest-viable-boundary rule, Jev-around-LLM sandwich, centralized
  policy + raw-judgment retention, red flags, completion questions
- Protocol branch: audit a codebase/PR before inventing mappings; per-action
  risk gates; keep questions/thresholds in one reviewable module
- Skill description trigger terms for brittle parsers, prompt-to-JSON
  classifiers, and agent loops that are really bounded decisions

## [0.1.0] - 2026-09-18

Pegged against [`typesafe-ai/skills` v0.5.7](https://github.com/typesafe-ai/skills/tree/v0.5.7)
(`65a39f3`, 2026-09-12) — the only tagged revision of the official skill at
Augustus launch.

### Added

- Skill protocol, decision-design card, and evidence labels (Contract /
  Empirical recipe / Hypothesis)
- Classical-method mappings: features/utility, selective decisions, decision
  circuits, bounded rerank, hierarchy/beam search
- Agent self-assessment, optimizer coupling (Ax, DSPy, ProgramAsWeights)
- Toolbox sweep, named-methods catalog, 11-position composition algebra,
  question-design diagnosis
- Validation gates and `scripts/evaluate_decisions.py`
- Launch-week evidence archive (187 repos) and public ecosystem index
- Claude Code marketplace manifest; public GitHub mirror at
  [`24601/Augustus`](https://github.com/24601/Augustus)

### Research log (pre-tag)

The dated passes below are how 0.1.0 was assembled.

### 2026-09-18 (refresh pass 2)
- Research: Gemini Deep Research report retrieved and archived (interaction ID
  saved in jev-archive/state); GitHub census doubled to ~60 Jev repos +
  framework integrations (LiteLLM, LangChain, Vercel AI, Mastra, Eliza, Ax,
  Composio); all 87 repos cloned to /home/user/workspace/jev-archive for
  hourly refresh.
- New measured recipes added to notes.md: foreman supervision loop, pi-jev
  gate thresholds, pi-warden 6→0 paired-run result, winnow relevance sieve,
  fast-jev-compaction two-noul rule, skill-router gates (0.30/0.40, shortlist
  3, 94.4% vs 70.8%), calibration ECE 0.0313 vs 32% OOD collapse (Archer
  Hume), Every 777-judgment eval, Near Here moderation numbers.
- Skill: added references/agent-self-assessment.md (agent self-supervision
  lifecycle, grounding/citation checks, skill callability testing) and two
  mapping-index rows; validation.md dogfooding section still canonical.

### 2026-09-17/18 (initial)
- Baseline research archive (sources.json, notes.md), augustus skill with
  mappings + validation references, evaluator script, hourly refresh script,
  Claude plugin marketplace manifest.

### 2026-09-18 (topic-index pass 3)
- Fixed census method: exact GitHub search paginated (700 repos created since
  09-14 captured; 700-result cap noted) + topics/jev crawl → ~80 additional
  repos; archive now 184 clones. Miss-cause documented: earlier star-sorted
  limit-40 search cut the low-star tail (incl. both MCTS repos).
- Skill: MCTS mapping promoted experimental → empirical recipe (grounded vs
  speculative fidelity in types; probes-only concession; measured 24/24 vs
  1/24 greedy); agent-self-assessment.md gains the judge-variance recipe
  (Jev judge 224-279x more consistent than LLM judge over 100 reps).

### 2026-09-18 (pass 4 — optimizers + official skills + clone audit)
- ax Jev support documented from source (native adapter details, trueThreshold
  semantics, fail-closed mapping validation); new reference
  optimizer-integration.md covering Ax + DSPy typesafeify + jev-dspy-lab.
- typesafeainate/dspy-typesafeify cloned; official typesafe-ai/skills already
  archived and layered-on (never duplicated).
- Clone audit: repos.txt deduped (185 unique), 0 missing on disk, no failures.

### 2026-09-18 (pass 5 — toolbox sweep meta-method)
- New references/toolbox-mapping.md: the how-to-find-approaches-and-
  applications procedure (judgment-shaped-hole substitution, newly-feasible
  classification via economics inversion, standing rejections list); wired
  into SKILL.md central model + index row.

### 2026-09-18 (pass 6 — named-methods + operators/theorems tier)
- references/methods-catalog.md: ~20 named algorithms (CatBoost row is
  Empirical via autoresearch cookbook) + operators/theorems tier with
  precondition-carrying rule; wired into SKILL.md index and toolbox sweep.

### 2026-09-18 (pass 7 — composition algebra as application generator)
- references/composition-algebra.md: 11-position grammar of Jev-vs-construct
  relations, logical-operator combination rules, and the position×construct
  traversal as the systematic application generator; wired into SKILL.md
  index + toolbox sweep.
