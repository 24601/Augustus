#!/usr/bin/env python3
"""Uniqueness gate for merged 0843 (§114), merged 0915 NanoJev (§115),
merged 0920 jcr (§116), merged 0922 SemIf (§117), merged 0940
llm-to-jev (§118), hourly 0947 HIGH (§119), hourly 1049 HIGH (§120),
hourly 1143 HIGH (§121), hourly 1248 HIGH (§123), hourly 1340 HIGH (§124), hourly 1441 HIGH (§125), hourly 1542 HIGH (§126), hourly 1643 HIGH (§127), hourly 1746 HIGH (§128), hourly 1843 HIGH (§129), user-provided 1936 HIGH (§130), Open-Jev densify (§125), hourly 1946 HIGH (§131), hourly 2049 HIGH (§132), hourly 2146 HIGH (§133), hourly 2246 HIGH (§134), hourly 2347 HIGH (§135), hourly 0049 HIGH (§136), hourly 0151 HIGH (§137), hourly 0248 HIGH (§138), hourly 0348 HIGH (§139), and hourly 0445 HIGH (§140), and hourly 0551 HIGH (§141), and hourly 0707 HIGH (§142), and hourly 0823 HIGH (§143), and hourly 0923 HIGH (§144), and hourly 1019 HIGH (§145).

Each lock must appear as one consecutive substring in every listed overlay.
Fragments scattered across files do not count.

Revisit / since-last-look protocol (`notes.md` §122) is a consecutive
substring in the skill + research files (not a 21-overlay dump wall).
Hourly must treat revisit HIGH like novel HIGH. Star-noise is not a fold.

Also: YAML-parse SKILL.md frontmatter; notes.md owns §114–§145;
composition items 289–316, 322–329, 330–336, 337–352, 353–368, 369–384, 385–400, 401–416, 417–432, 433–448, 449–464, 465–480, 481–496, 497–504, 505–520, 521–536, 537–552, 553–568, 569–584, 585–600, 601–616, 617–632, 633–648, 649–664, 665–680, and 681–696, and 697–712, and 713–728, and 729–744 exist;
findings batches #97–#126 exist. Items 317–321 stay unused.
The 1843 archive run_digest must claim §129 / 481–496 / #111.
The 1946 archive run_digest must claim §131 / 505–520 / #113
(not the 1746 IDs §128 / 465–480 / #110).
The 2049 archive run_digest must claim §132 / 521–536 / #114.
The 2146 archive run_digest must claim §133 / 537–552 / #115.
The 2246 archive run_digest must claim §134 / 553–568 / #116.
The 2347 archive run_digest must claim §135 / 569–584 / #117.
The 0049 archive run_digest must claim §136 / 585–600 / #118.
The 0151 archive run_digest must claim §137 / 601–616 / #119.
The 0248 archive run_digest must claim §138 / 617–632 / #120.
The 0348 archive run_digest must claim §139 / 633–648 / #121.
The 0445 archive run_digest must claim §140 / 649–664 / #122.
The 0551 archive run_digest must claim §141 / 665–680 / #123.
The 0707 archive run_digest must claim §142 / 681–696 / #124.
The 0823 archive run_digest must claim §143 / 697–712 / #125.
The 0923 archive run_digest must claim §144 / 713–728 / #126.
The 1019 archive run_digest must claim §145 / 729–744 / #127.
CHANGELOG.md must not hold uniqueness dump walls (dumps live in
changelog-hourly.md). README.md is not a uniqueness overlay: the
human-facing README stops at License and must not hold uniqueness
locks or hourly HIGH digests.
Pages greps stay in docs/index.md and docs/_layouts/default.html.
The 0843 ecosystem blurb cites notes.md §114. Does not fetch the
network. Does not treat a lock as a Harbor score.
"""

from pathlib import Path
import json
import re
import subprocess
import sys
import yaml

ROOT = Path(__file__).resolve().parents[4]

UNIQ_0843 = (
    "Hourly 0843 uniqueness lock: A hunch is a probability with a policy attached; "
    "{ enter: 0.8, exit: 0.6 } is hysteresis; replay a policy change without inference; "
    "Decision models are providers, not the product; huncho ≠ Kungie/gut ≠ carldaws/hunch ≠ tpellet/hunch; "
    "pretrained Qwen2.5 base ECE 0.030 (0.5B) / 0.040 (7B); instruct 0.302 / 0.269; "
    "70.9% → 70.0% mean conf 74.1% → 96.7%; temperature scaling still matches it in-distribution; "
    "No Jev API was called; Qwen2.5 ≠ Archer; Qwen/Qwen3.8-27B ≠ Archer; "
    "学習済みモデル v0.1 は準備中です; bool AUROC 0.523; 先頭だと0件、末尾だと250件; "
    "温度を渡さない場合、確率は較正されていません; このリポジトリには Jev を呼ぶコードが存在しません; "
    "g0runmezadam/what-is-jev IS tunahansahin897/what-is-jev (same GitHub id 1378007307); "
    "947 repos scored; A 273 · B 302 · C 372; LLM rubric ≠ benches; Data as of 2026-09-20; "
    "HEAD 895b9498; README SHA 3ae98c56; 13 focused checks and one mutually exclusive outcome; "
    "Probabilities are advisory, not calibrated guarantees; omni-/ask-jev ≠ pedroknigge/mcp_jev; "
    "pd.cut bins by equal width while jeval bins by quantile; ECE 0.113 and ECE 0.076; "
    "jeval drift is not implemented yet; rlaope/jeval ≠ dayhaysoos/jevals; "
    "calibration does not compose; ECE has exactly zero statistical power to detect the failure mode that kills trajectories; "
    "25–60× headline withdrawn; P(all-correct): 0.0071 vs 0.0001; TCE / AMS; "
    "Qwen 3.8 sparring ≠ Archer; Deferred Crispification; light_cutoff_applied_to_combination 0; "
    "recorded run, kinematic animation; BANKING77 Accuracy BERT-Base 93.02 Jev 79.90; "
    "Analyse jev calibration (NLL, ECE) backlog; BERT figures are published supervised references, not zero-shot; "
    "档位措辞效应 分数极差中位 0.50、最大 1.32; 修好后对照组是 0.01; 不是 benchmark; 概率没做 calibration; "
    "~1,430 API calls, about $0.15; xiaohuaxi/jev-study ≠ wjdjdakf17/jev-study ≠ baekenough/jev-study; "
    "AND: product (independence assumed and recorded in the trace); "
    "chat model's stated confidence is not calibrated; circuit-vl-4b ≠ Archer; "
    "Bring your own API key; vamsikrishna2421/jev-usecases ≠ whyashthakker/awesome-jev-use-cases; "
    "catalog ≠ endorsement; SemIf 2237★ (+30 vs §111 2207); jevlike 1049★ (+6 vs 1043); "
    "TypeLLM/TypeLLM 16★; AnotiaWang 98★; yibie/awesome-jev 520★ (+14 vs 506); "
    "Laya likes 861 (was 822); tracker likes 66 (+2 vs 64) lastModified UNCHANGED; "
    "Blackwood likes 2 gated manual; Archer still promised_not_landed; "
    "Hub archerhume/4rcherhume HTTP 401; "
    "do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35; notes.md §114"
)

UNIQ_0915 = (
    "User-provided 0915 uniqueness lock: TianyuCodings/NanoJev unified-games-v1 densify; "
    "A 0.6B parallel decision model: states and questions in, complete probability distributions out. Zero output-token decoding.; "
    "One model, four games; ViZDoom Basic 128/128 vs Jev 56/128; Predict Position 27/128 vs Jev 11/128; "
    "Maze 225 attempts vs Jev 2738; Snake 30 food / 256 steps; "
    "held-out Maze 4/10 Snake 8/8 Basic 128/128 Predict 27/128; Untuned Qwen3-0.6B baseline; "
    "18,760 questions per variant; 16,333 ViZDoom; 896 Predict Position expert episodes; "
    "hard_lr1e5; mix weights 1/3, 1/3, 1/6, 1/6; Hub C-Tianyu/NanoJev revision unified-games-v1 likes 58; "
    "dataset C-Tianyu/NanoJev-Data likes 5; HEAD 618cea6d906d54e128360786d12f703fff2b1245; "
    "1289★ / 158 forks / size 64035; README SHA 4190093c64ee75b26e9726daa3b00cbcf6d3157a; MIT; "
    "caijinchun/nanojev-arena ≠ liao96312/jev-arena-nanojev ≠ zwliJay/jev-forge ≠ NanoJev; "
    "not TypeSafe Jev; open replica / specialist gameplay S1; soft scores ≠ hard gates; "
    "Game success ≠ calibrated Noul; local type boolean ≠ TypeSafe noul; invented_signal false; "
    "do not reopen or amend PR #31/#32/#33/#35; notes.md §115"
)

UNIQ_JCR = (
    "User-provided 0920 jcr uniqueness lock: NiazMorshed2007/jcr MIT; site https://jcr.niazmorshed.dev; "
    "topics ai-agents,jev,mcp; **4★**; HEAD `138b3832`; README SHA `2a49dbc1`; LICENSE SHA `46231303`; "
    "size **14850**; Jev Capability Resolver; one tool to find documented deterministic commands in a nested capability tree; "
    "returns context; **does not execute**; skills = workflow+judgment; capabilities = individual operations; "
    "format independent of Jev; proposed open standard exploration; classify (Jev) → optional OpenAI decompose compound → "
    "beam search geometric mean of routing probs; keep up to 3 paths ≥60% of best (JCR_BAND_RATIO 0.6); "
    "ambiguity / no-match / depth-limit explicit; soft scores ≠ hard gates; 0.6 band is application policy; "
    "routing ≠ permission; docs ≠ authority to run; sol-vs-opus5-20 *theirs*: 20 scenarios × 4 variants = 80 runs; "
    "lookup+explain only, no execution; Claude Opus 5: agent input 108,585→15,819 (−85%), cost $0.3700→$0.1222 (−67%), "
    "wall 105.5s→77.7s; Codex GPT-5.6-Sol: 61,952→47,669 (−23%), $0.1377→$0.1151 (−16%), wall 25.3s→62.4s "
    "(Sol slower with JCR in 19/20); One Sol outlier 372.6s / 193 Jev calls; n=1 per cell; Not Harbor task-execution; "
    "Claude/Codex harnesses; compare mode; 50 scenarios bundled; 11 groups, 960 nodes, 11,360 items; "
    "16 routing rounds per step; NiazMorshed2007/jcr ≠ skill-broker ≠ skillranker ≠ jev-sift ≠ jev-lens ≠ jevusher ≠ "
    "jev_select_capability; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34; notes.md §116"
)

UNIQ_0940 = (
    "User-provided 0940 uniqueness lock: Turn decision-shaped LLM prompts into proposed Jev primitives; "
    "This is a conversion assistant, not an automatic guarantee of equivalent behavior; "
    "The compiler uses deterministic heuristics, not an LLM or evaluation model; "
    "It understands a deliberately small set of common prompt patterns; "
    "Generated instructions and criteria must be reviewed before production use; "
    "Score ranges such as 0 to 1 are translated into ordered Jev criteria; "
    "Prompts requiring open-ended prose are not a fit; "
    "suitability strong/partial/not_a_fit; compatibility full/partial/none; "
    "Writing new text stays with an LLM; "
    "Review the generated Score rubric; Jev scores ordered criteria, not an arbitrary 0-to-1 range; "
    "Everything runs locally in the browser; "
    "There is no framework, database, account, API, or server-side prompt processing; "
    "The key is read from the process environment and is never stored or printed; "
    "connect-src 'none'; "
    "alexwestco/llm-to-jev ≠ altryne/jevify ≠ ryana/jevify ≠ fidecastro/jevify ≠ Mintzs/jevify ≠ gulagala001/jevify ≠ uspraveen/Jevify; "
    "HEAD 234058ab372d; README SHA 43cd94fb; LICENSE SHA 5f334006; compiler SHA fdf235d0; "
    "2★; MIT; JavaScript; size 29; Pages https://alexwestco.github.io/llm-to-jev/; "
    "invented_signal false; "
    "do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35; notes.md §118"
)


UNIQ_0922 = (
'User-provided 0922 uniqueness lock: SemIf was formerly OpenJev; independent; not affiliated with Jev or TypeSafe; homepage openjev.com; default master; MIT; HEAD ca3ba65f1429; Tolerate float roundoff in MLX evidence verification; pushed 2026-09-19; live REST 2282★ / 140 forks; size 9177; README SHA 74ab7f7f; LICENSE SHA ca562883; interface pattern reproduction with open models; does not reproduce Jev undisclosed model/training; Direct option logits; 0 output tokens; shared-state parallel; MLX backend for Apple Silicon (`--backend mlx`); Qwen3.5-4B 3090 direct 1.023s vs AR JSON 5.332s (**5.21×**); argmax agree 18/21; systems comparison ≠ semantic equivalence; Parallel suffixes 20.03 dec/s on 777 decisions; Browser ladder Qwen3.5-4B authored BA 0.813, pert 0.766, TypeSafe subset agreement 0.845 vs Published Jev 0.883 (102 across 20 cases); Softmax over options ≠ calibrated Noul; typed output does not guarantee semantic correctness; wire/agreement ≠ replica of TypeSafe; SemIf ≠ kw2828/OpenJev playground ≠ zhihz/openjev ≠ apiplant/semif-rs port ≠ dddanielliu/semif-serve; rename is densify not a second census; JevBench 74.6 is §78 not this ladder; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#38; do not push onto open #39/#40; notes.md §117'
)

UNIQ_0947 = (
    'Hourly 0947 uniqueness lock: Fast and cheap agent evals. jev as judge.; 18,041 skills from the 200 most-starred repos; Not a security scanner; 最简 Jev 调用演示器; confidence 不是正确率; q93304989-bit/jev-lab ≠ tanayvasishtha/jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab ≠ yibie/laya-jev-lab; 75% cheaper and 18% faster withdrawn; jev @0.15 100% recall 87% savings; 33Audits/jev-auto ≠ gargpratyush/jev-router; no Typesafe key, no PI_API_BASE, zero deps; tool-emitted Score/Noul ≠ calibrated Noul; semantic_compatibility: false; candidate_mass; Qwen3.5-2B ≠ Archer; Jev evaluates decisions; it cannot run a coding-agent session; Status: no model yet; S1LV3RJ1NX/openjev ≠ TheoLeeCJ/openjev; 28 accepted decisions; 3 targets; score 800; health 100; arcade game not a flight trainer; A successful live TypeSafe call has not been verified for v0.1.0; abhibansal60/tidy ≠ MANISH007700/tidy; No model, Jev included, predicted which channels its owner keeps; seed 1 selected on a held-out 400-item validation split; Brier 0.342 → 0.378; more accurate and more overconfident; Qwen3.5-4B ≠ Archer; static quants of kushalpatil/jevify-gemma4-26b-a4b; The labels were corrected, and one earlier result was retracted; zero of 23,869 eligible rows; Do not compare cost without checking task success; Exit 1 is not a proof; kisshan13/typesafe-ai-go ≠ Nibir1/typesafe-go ≠ official; 38 tests that cannot fail in a 356-model warehouse; if a parser can answer it, Jev is never asked; 359 of them; Games & Simulation 82; Education & Learning 1; Ratings are heuristics; syedabbasshaheer-art/jev-atlas ≠ ZeroX-01/jev-atlas ≠ Zaious/jev-capability-atlas ≠ gorock007/jev-atlas; anandi1989/awesome-jev-usecases ≠ whyashthakker/awesome-jev-use-cases ≠ walidboulanouar/awesome-jev-use-cases ≠ vamsikrishna2421/jev-usecases; Every headline result above is self-reported; Archer Hume 84.6% MMLU-Pro is a third-party probe not landed Archer; catalog ≠ endorsement; judge ≠ actuator; softmax over A–H ≠ Noul; SemIf 2270★; jevlike 1054★; TypeLLM/TypeLLM 16★; AnotiaWang 98★; yibie/awesome-jev 538★; Laya likes 889; tracker likes 68 lastModified UNCHANGED; Blackwood likes 2 gated manual; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#35/#36/#37/#38/#40; do not push onto open #39; notes.md §119'
)


UNIQ_1049 = (
    'Hourly 1049 uniqueness lock: ggmlc GGUF is not llama.cpp; Loading them in llama.cpp will fail; one encoder pass; hf:mys/laya-GGUF sha 713ae6f6e39f likes 0 apache-2.0; hf:mys/laya-multilingual-GGUF sha 3b645ae54281; hf:mys/laya-typed-decisions-GGUF sha 1e9e8ba1f527; hf:tozp/laya-onnx sha 0862aeba1e65 Opset 14 FP32 and INT8; tozp/laya-onnx ≠ Mattepiu/laya-onnx ≠ gqgs/laya-onnx; docker-laya MIT HEAD 1b8239a51ddd README SHA 9cb7bdc3; laya.cpp RTX ggml CUDA HEAD 8590937c79a2 README SHA cdd429b9; serving substrate ≠ calibrated replica; Softmax over options ≠ calibrated Noul; Qwen3.5-4B ≠ Archer; Qwen3.5-9B ≠ Archer; jev-position-test n=6 HEAD 7a56ca1c2698 README SHA 23f194c9; jevmlx slots 5 of 6; hosted Jev 0 of 6; prior_correction made it worse; jevSweeper mean Spearman ρ −0.274; picked exact-optimal 1/25 (4%); 31 of 36 still logically decidable; 86% of the time we should not have been asking; game success ≠ calibrated Noul; LLM2Jev 64★ Apache-2.0 HEAD 924618721277 README SHA da35fe61; not affiliated with or endorsed by Jev or TypeSafe; No answer tokens are generated; OpenSourceJev llama.cpp Qwen3-1.7B HEAD 3c41fba3681d; JEV-MLX Qwen3.5-9B HEAD dec24cd929ea; decision-head-rlcd Qwen3.5-4B 4.9M LoRA; AUTO_ACT is not a Noul; closed-set fail-open stdlib-only; verified=False; soft scores ≠ hard gates; 22 to 40% cheaper *theirs*; first version 70% more expensive; 111-case benchmark *theirs*; CDC 5,000 Jev 72.2% AUC 0.7725 *theirs*; accuracy is a trap; 9.0% base rate always-no 91.0%; catalog ≠ endorsement; jev-skill 109★ 90 scenarios HEAD 4f6e899a24d4; awesome-jev-live 673 entries 4★; minecraft-agent 214★ 131 JEV decisions 35 Astra calls; nether-final-08 8 minutes 43.300 seconds; planner writes JEV selects; RoboJEV structured simulator state not images; ashare-trader 策略未通过自己的回测门槛; 36 组参数全部净期望为负; no positive expectation under real costs; typed_evals NOT an official TypeSafe AI product; jev-as-judge is a sensor; third-person-audit 40% & 60% watermarks still soft; The included experience uses a handwritten demo provider; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42; notes.md §120'
)

UNIQ_1143 = (
    'Hourly 1143 uniqueness lock: open recreation ≠ calibrated replica; Qwen3.5-4B ≠ Archer; It is an open re-creation of Jev; less calibrated; perch 164★ MIT HEAD ba775a9940b6 README SHA 7ad0403b; semantic lint is a sensor not a proof; oxlint-plugin-jev cutoff 0.8 still soft; nassim-arifette/jevgrep ≠ Bentlybro/jevgrep ≠ can1357/jegrep ≠ uehaj/jev-semgrep; patdown fuzzy linter; PanAchy/jevvy ≠ Atominac/jevvy; No orders, no advice; SmartMoney-Cub 25★ HEAD d93cf493853d; paired bootstrap CIs *theirs*; emretheus/jev-rag-benchmark ≠ erendikmenn/jev-rag-benchmark; +0.82 pts XQuAD-EN 95% CI +0.35 to +1.31; +7.62 pts SciFact CI +4.88 to +10.38; Same accuracy, 35x faster *theirs*; systems comparison ≠ semantic equivalence; BANKING77 500 Jev 81.0% GPT-OSS 82.8% Mercury 73.2% Gemini 85.4% *theirs*; frozen cascade missed its evaluation accuracy target 430/500 vs GPT-5 432/500; This is not demonstrated equal-quality savings; 24 invented tickets; Routing errors caught by the gate 0 of 3; sample too small to establish calibration; This is not TypeSafe Jev; No real API requests were made; wire-compat ≠ replica; KonghaYao/laya-jev 按官方接口写的客户端只改一个 base URL; gqgs/laya-onnx densify 496.8 MiB; tozp/laya-onnx ≠ Mattepiu/laya-onnx ≠ gqgs/laya-onnx; serving substrate ≠ calibrated replica; BeatAPI/awesome-jev ≠ 99hansling/awesome-jev ≠ Vishnurr2k01/awesome-jev ≠ robokrunch/awesome-jev ≠ rudy2steiner/awesome-jev-hub; All 125 projects; catalog ≠ endorsement; Pasblinn/jev-lab ≠ tanayvasishtha/jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab ≠ yibie/laya-jev-lab ≠ q93304989-bit/jev-lab; Independent project. Not affiliated with TypeSafe; Kevthetech143/super-jev densify experimental V0.2.0; permission ≠ confidence; allay-team/openjev ≠ piyush-infocusp/openjev ≠ TheoLeeCJ/openjev; 2022 Mineflayer Jevalent collision; kushalpatil/jevify-gemma4-e4b GGUF densify; static quants; This dataset and model are independent research artifacts, not reproductions of Jev or RLCD; pngwn demo accuracy 0.705 ECE 0.046 ~112 ms *theirs*; cutoff 0.8 still soft; soft scores ≠ hard gates; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43; notes.md §121'
)

UNIQ_1248 = (
    'Hourly 1248 uniqueness lock: decide is not generate; tryDecide returns typed calibrated judgments not a token stream; juspay/neurolink 133★ MIT HEAD 268b0fe83130 README SHA e709cadfa6b6 tag v12.19.0; GLiNER/GLiClass ports are class members not Jev replicas; MacPaw/Gliner2Swift ≠ Knowledgator/GLiClass.c ≠ fbilhaut/gliclass-rs ≠ Knowledgator/GLiClass.js ≠ gravitee-io/GLiNER4j ≠ apiplant/gliner-rs ≠ codesoda/gliner2-rs; 8.7x faster 4.4x fewer prompts *theirs*; 153 was a reporting error; corrected 156-case 9.8x faster 4.2x fewer prompts *theirs*; independent v0.2.1 1.24x vs Mini *theirs*; Approvals only; anpicasso/hermes-jev-approvals ≠ hermes-switchyard; scx-router GLiClass ranks candidate LLMs in one non-generative pass; typesafeai-dotnet-sdk Not affiliated with TypeSafe AI; hyperspaceai/jevcache ≠ kushals256/jevcache; ST-jeved measures each reply; 400 plain-text for unaskable question; razorback16/openjev:0.2.1 Docker densify HEAD 794a81b87131; wire-compat ≠ logit-equiv; Option-Marker joint attention 93.5% macro *theirs*; 93.6% micro *theirs*; n=78; T = 1.0367 vs T = 1.1692 two temperatures; guaranteeing is soundness theater; wfzyx/von densify HEAD bed7e7337791; Benchmark Heaven leaderboard #2 74.9 *theirs*; NLL calibration assets; 77.10% still §71 claim-audit; do not re-fold as a beat; Heman10x-NGU/openJev-verdict-2.0 densify HEAD bff28567cff4; kev-family weight tarballs; PLAN_Qwen35 proposal for review; deadline 0.53→0.82 at 9B *theirs*; Qwen3.5-9B ≠ Archer; isolation would fail by construction on DeltaNet; jaredpalmer/kev densify; JevBench v1.2.2 jeff 66.9 (#9) jev 75.3 (#2) *theirs*; logan-markewich/jeff densify HEAD 34b32f99a727; thinking=True/False per-field budget; type safety does not guarantee factual accuracy; TypeLLM/TypeLLM densify HEAD c4b03ba9e792; us/jev-local stub until hf; Eran-BA/Jev_from_GLiNER2 spec ≠ replica; lsu-ub-uu/systemone ≠ TypeSafe System One; Layan/Laya HF spaces name-match; catalog ≠ endorsement; decide ≠ generate ≠ stream; 93.5% *theirs* not Harbor; 74.9 *theirs* not Harbor; 8.7x *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45; notes.md §123'
)

UNIQ_1340 = (
    'Hourly 1340 uniqueness lock: typesafe-sdk 0.7 Pydantic response models; msgspec dropped; The server\'s output is unchanged and was never wrong; MLX backend 400 plain-text error contract; SchemaError is 400 plain-string detail not 422 list; razorback16/openjev densify HEAD 6e91dfc031bc README SHA cbdcc8de0304; Pydantic response models ≠ logit-equiv; msgspec dropped is not a replica; Error contract is not a Noul; wire-compat ≠ logit-equiv; PLAN_Qwen35 densify; corrected Qwen3.5 LoRA target names verified; in_proj_qkv in_proj_z in_proj_a in_proj_b out_proj; peft 0.21 existence proof; OOD-calibration study; coverage-at-error-budget metric in Phase 0; PLAN_Qwen35 still proposal for review; deadline 0.53→0.82 at 9B *theirs*; isolation would fail by construction on DeltaNet; Qwen3.5-9B ≠ Archer; jaredpalmer/kev densify HEAD 75cc15ddb8e2 PLAN SHA eca543246f50; GLiNER locate ports are class members not Jev replicas; urchade/GLiNER ≠ fbilhaut/gline-rs ≠ lmoe/gliner-onnx.js ≠ shershah1024/gliner-native-runtime; Locate ≠ decide; Jev-Vision skip 0.936 effect 0.967 done 0.896 157 ms *theirs*; ~160 ms *theirs* not Harbor; 0.971 F1 *theirs* not Harbor; coverage-at-error-budget *theirs* not Harbor; hf:fr0stbit3/laya-gguf serving substrate ≠ calibrated replica; jkcdarunday/SystemOne-Next ≠ TypeSafe System One; catalog ≠ endorsement; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46; notes.md §124'
)

UNIQ_1441 = (
    'Hourly 1441 uniqueness lock: vLLM NVIDIA + MLX Apple Silicon; Codiv hosted free endpoint; dual /v1/systemone + /v1/chat/completions; razorback16/openjev densify HEAD cddbd962c88a README SHA a5943415cb92; STE README rewrite; serving-port densify; chat 501 on MLX; dual serving is not generate; Hosted Codiv ≠ TypeSafe; wire-compat ≠ logit-equiv; SHA move is not a replica; Error contract is not a Noul; hr98w/jev-visual 167★ Apple Silicon visual candidate scoring; 37.30s → 2.40s at 64 decisions *theirs*; Breakout 9 bricks 6 returns 2 lives *theirs*; candidate probabilities are relative not correctness; jkudish/jev-mcp 156★ ten MCP tools; recommendation is advisory; the server never blocks on its own; TypeSafe CLERC 5% to 18% *theirs*; jkudish/jev-mcp ≠ burnigtm/jev-mcp; zhengxuyu/litjev off-the-shelf Qwen decision layer; Probabilities are not calibrated by default; Qwen/Qwen3.8-27B ≠ Archer; zhengxuyu/litjev ≠ alexwestco/llm-to-jev; Zefan-Cai/Open-Jev LoRA + scalar head; 2B 94.71% 9B 97.54% hard test *theirs*; 2B OOD 86.02% 9B OOD 91.97% *theirs*; 80,816 training rows; 27B still in progress; LoRA ≠ RLCD replica; Zefan-Cai/Open-Jev ≠ TheoLeeCJ/openjev ≠ razorback16/openjev; cristianoliveira/jeq intelligence you can pipe; pass-min 0.8 still soft; JEQ does not own actions; AndyInQtr/laya-coreai CoreML serving substrate ≠ calibrated replica; AndyInQtr/laya-coreai ≠ mizorewww/laya-coreml; catalog ≠ endorsement; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47; notes.md §125'
)

UNIQ_1542 = (
    'Hourly 1542 uniqueness lock: TypeLLM/TypeLLM densify HEAD 6a48f9f1e623 README SHA dbdc1f193537; README densify 3k→12k B; thinking=True/False per-field budget; type safety does not guarantee factual accuracy; Batch 5.8x *theirs*; Constrained AR ≠ calibrated Noul; Qwen/Qwen3.8-27B ≠ Archer; jaredpalmer/kev densify HEAD b339f446a0ef README SHA 86b0a19909f3; Kev-0.6B 4B 8B family; 4B new-source 0.790/0.806 *theirs*; 8B new-source 0.796/0.780 *theirs*; Jev hosted 0.857 *theirs*; Questions share the input text but cannot read each other; No Jev outputs were used for training; 8.2% ≥0.9 on wrong *theirs*; option order can change an answer; Qwen3 ≠ Archer; wire-compat ≠ logit-equiv; SHA move is not a replica; TheoOliveira/pi-jev 21★ fail-closed routing; JEV_THRESHOLD 0.65 still soft; routing ≠ permission; harshwasan/jev-sentinel fail closed never auto-allows; harshwasan/jev-sentinel ≠ leepokai/jev-guard; jackbarunz/jev-tool-router ≠ esinocchi/jev-tool-router; threshold 0.90 still soft; 76/81 vs 77/81 *theirs*; 0.419s vs 2.459s *theirs*; $0.00486 vs $0.03673 *theirs*; does not execute; not a security boundary; baronunread/leanest fail-open uncertainty means RUN; classifier.dev default Jev/Laya pluggable; openlayer-ai/jevals ≠ dayhaysoos/jevals; estimates not Harbor; classifier ≠ authorizer; MrJev/awesome-jev 118 entries catalog ≠ endorsement; MrJev/awesome-jev ≠ yibie/awesome-jev; Koushik890/jev-firewall fail closed ask_below 0.7 still soft; CompleteTech-LLC-AI-Research/jev-codex-approval experimental native not compiled; confidence is not a measured probability; rh-guard owns primary gates; hf:rAVEUK/open-jev-deberta-v3-large encoder class member not Jev replica; hf:p-yan/laya-quanto serving substrate ≠ calibrated replica; hf:Gtrkrsk/laya serving substrate ≠ calibrated replica; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48; notes.md §126'
)

UNIQ_1643 = (
    "Hourly 1643 uniqueness lock: razorback16/openjev densify HEAD febf02e88989 README SHA 242a737dba01; release 0.3.0; re-pin vLLM PR #57250 restructured head; VLLM_COMMIT baa8338; pyproject and __init__ agree 0.3.0; MODEL_VERSION stays openjev-0.1; uv.lock hygiene; dual serving is not generate; Hosted Codiv ≠ TypeSafe; restructured vLLM head ≠ logit-equiv; wire-compat ≠ logit-equiv; SHA move is not a replica; Error contract is not a Noul; frostney/clean-code-review 7★ typed judgments not opinions; documentation is read not judged; Luna writes from Jev findings; morcoan/JMP Joint Model Participation; Models participate. Real tools execute.; Jev routes actions generators supply arguments; not a swarm; zkjoie/jevbus Thresholds are policy not model; Drop < Review < Deliver; FanOut or Exclusive; Kelbie/hunch ≠ carldaws/hunch ≠ tpellet/hunch ≠ huncho; Agent Skills semantic review; SupratikB23/JevCanvas Jev never generates prose JSX or code; Diffusion never decides structure; json-render is the only renderer; skcache/jevtrafficsim Fixed Adaptive Jev; game success ≠ calibrated Noul; Shalimov04/open-jev ≠ razorback16/openjev ≠ TheoLeeCJ/openjev ≠ Zefan-Cai/Open-Jev; MstyAI/laya-onnx empty repo ≠ tozp/laya-onnx ≠ Mattepiu/laya-onnx ≠ gqgs/laya-onnx; SherifAshraf2003/jev-use ≠ shitianfang/jev-use; aniruddh-krovvidi/switchboard ≠ cannacre8ive/switchboard-ai; Visorian/TidyUp ≠ abhibansal60/tidy; isiomaC/jevkit ≠ WaynezProg/jev-kit; lee-lou2/jev-tree ≠ reachjalil/jev-tree; Royhu1/jev-poker-trainer empty repo; JoacoMarc/jev-harness-router ≠ jackbarunz/jev-tool-router; rh-guard owns primary gates; hf:Praveenrajus/jev-bench HTTP 200 was 401; hf:ZefanCai/Open-Jev densify dataset; LoRA ≠ RLCD replica; hf:emretheus/jev-rag-benchmark ≠ erendikmenn/jev-rag-benchmark; hf:ctaxnagomi/DGUI_HYPERMEM-JEV densify sha ab3d3529; hf:hugging-apps/open-jev-deberta-v3-large-demo encoder class member not Jev replica; serving substrate ≠ calibrated replica; catalog ≠ endorsement; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49; notes.md §127"
)

UNIQ_1746 = (
    'Hourly 1746 uniqueness lock: TypeLLM/TypeLLM densify HEAD 702e6a287f3c README SHA 08180db0450b; truncated thinking then constrained decode; typellm_runtime.py typellm_sglang.py; evals/qwen35_small; 0.8B thinking On 0/18 *theirs*; forced closure 20/20 type-valid *theirs*; Constrained AR ≠ calibrated Noul; type safety does not guarantee factual accuracy; Qwen/Qwen3.8-27B ≠ Archer; jaredpalmer/kev densify live HEAD 8465c4c4c294 watch 38087aa0301d README SHA 19664b9ae546; Kev-0.8B completes family; Kev-0.8B 4B 9B Qwen3.5; 4B new-source 0.794/0.832 *theirs*; 9B new-source 0.812/0.837 *theirs*; transfer-v9 Kev-9B 5% Jev 9% Kev-8B 26% *theirs*; SemIf Kev-9B 0.917 Jev 0.965 *theirs*; scienthoon 0.952/0.911 vs 0.897/0.914 *theirs*; transformers >= 5.17; Qwen3.5 ≠ Archer; wire-compat ≠ logit-equiv; SHA move is not a replica; notque/vexjoy-agent 421★ /d routes /do fallback; tamaratran/jev-pruner densify HEAD 47d017c34eab; qkal/Canny Facts go to code. Judgments go to Jev. Only facts can block.; Jev never blocks; jqueryscript/awesome-jev 231 entries catalog ≠ endorsement; jqueryscript/awesome-jev ≠ MrJev/awesome-jev ≠ yibie/awesome-jev; jamescazzetta/five-lines threshold 0.80 still soft; eugeniughelbur/jev-engineering 371ms $0.0000189 300-call *theirs*; tpellet/jevify ≠ altryne/jevify; seb4ez/jevguard-mcp ≠ seb4ez/jevguard; resumocast/jev-mcp ≠ jkudish/jev-mcp; dtduc-git/jev-table first sighting; Adrian-Ernesto/jevsort ≠ zzzzzec/jevsort; MidasMulli/kev-ane 155/155 argmax *theirs*; MidasMulli/kev-ane ≠ jaredpalmer/kev; serving substrate ≠ calibrated replica; empty repo skip-thin; loktar00/llm-lan-party empty repo; rh-guard owns primary gates; catalog ≠ endorsement; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50; notes.md §128'
)

UNIQ_1936 = (
    "User-provided 1936 uniqueness lock: sgoedecke/system-one 20★ HEAD ebde2a2db706 README SHA d331b567e2c3; SystemOne.from_pretrained; Batched single-token choice inference; TypeSafe-compatible; cache_prefix=True; LICENSE absent; sgoedecke/system-one ≠ mithalouni/system-one-open ≠ KathanModh259/system-one ≠ babybear-labs/system-one; TypeSafe-compatible ≠ TypeSafe replica; mithalouni/system-one-open 18★ MIT HEAD 77f1f7cccf8a README SHA 535f33028a68 LICENSE SHA 2f6f2cf1064e; Gemma 4 E2B / Gemma 3 270M Modal; 76.7% vs Jev 86.9% strict common subset *theirs*; 97 ms H100 *theirs*; 74.8% held-out *theirs*; replica ≠ TypeSafe; HF upload pending; kotoba-lang/typed-decisions 1★ Apache-2.0 HEAD 10d7834d3b99 README SHA 4d6bbf4c4e44 LICENSE SHA 513bb5e3cb4c; ModernBERT / DeBERTa / LLaDA-MoE; DeBERTa-v3-large 0.855 / 42 ms *theirs*; ModernBERT-base 0.717 / 68 ms *theirs*; LLaDA-MoE 0.835 / 676 ms *theirs*; kotoba-lang/typed-decisions ≠ convaiinnovations/laya-typed-decisions; encoder class member not Jev replica; aisearchio 15-link census catalog ≠ endorsement; 12 already carded 3 gaps this fold; soft scores ≠ hard gates; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52; notes.md §130"
)

UNIQ_1843 = (
    "Hourly 1843 uniqueness lock: jaredpalmer/kev densify HEAD bd058057ad0a README SHA 84b872488915; Fine-tuning on your own data; --data JSONL; --init_from warm-start LoRA/head PR #9; Kev-0.8B 4B 9B Qwen3.5 family; 4B new-source 0.794/0.832 *theirs*; 9B new-source 0.812/0.837 *theirs*; 0.33 vs 0.84 vs 0.83/0.88 *theirs*; from-scratch ≠ warm-start; JSONL labels ≠ Harbor; Kev-0.5B card Qwen3.5 family pointer; No Jev outputs were used for training; option order can change an answer; 8.2% ≥0.9 on wrong *theirs*; Kev-9B 7.5% ≥0.9 on wrong *theirs*; dabit3/jev-experiments densify 340★; simota/tenbin densify neighbor skill; Promethe-us/awesome-jev ≠ MrJev/awesome-jev ≠ yibie/awesome-jev; kyegomez/open-jev reconstruction ≠ replica; unofficial research implementation with random weights; kyegomez/open-jev ≠ razorback16/openjev ≠ TheoLeeCJ/openjev ≠ Zefan-Cai/Open-Jev ≠ Shalimov04/open-jev; jourdanlabs/assay-001 split verdict; CLINC150 ECE 0.0204 *theirs*; Banking77 ECE 0.0936 *theirs*; 8,576 responses zero type errors *theirs*; brnyxx/jev-ra 3-5x / ~300 ms *theirs*; 8.50× Wikipedia *theirs*; ThePFMind/jev-mcp ≠ jkudish/jev-mcp ≠ burnigtm/jev-mcp; namenu/pi-jev-effort ≠ TheoOliveira/pi-jev; samatv256/mini-Jev ≠ r-ms/mini-jev; comoc/jev-minesweeper ≠ EnesYilmazcode/JevMinesweeper; game success ≠ calibrated Noul; Nutlope/jev-fraud Kimi K3; jeffloo886/jev-notion; hf:akhilaaa3/openjev-v1-allmix-r512-merged ≠ hf:akhilaaa3/openjev-r512-handoff-demo; serving substrate ≠ calibrated replica; catalog ≠ endorsement; SHA move is not a replica; wire-compat ≠ logit-equiv; Qwen3.5 ≠ Archer; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51; notes.md §129"
)

UNIQ_OPENJEV = (
    'User-provided Open-Jev densify uniqueness lock: Zefan-Cai/Open-Jev densify HEAD 4933ee84951f README SHA ce1a587219e4; pushed 2026-09-21T01:34Z; Astra TREC commit 1dd56990be7e pushed 2026-09-21T01:17Z; live 3★ (was 0★; star-noise is not the fold); LoRA adapters plus trained scalar decision head and calibration temperature; not merged base models; dataset ZefanCai/Open-Jev rev c67699e13d0a; Open-Jev-2B rev 0c7aa498b162; Open-Jev-9B rev 47e966881e48; 27B still in progress; Independent of TypeSafe; no RLCD/parity claims; LoRA ≠ RLCD replica; customer-service P50 local HTTP 85.03 ms vs Jev HTTPS 295.26 ms *theirs*; 1024 tokens/32 candidates Open-Jev slower 1015.90 vs 301.37 *theirs*; prefix caching experimental/off by default; CUDA prefix caching exceeded tolerance on 9/11 workloads; systems latency ≠ semantic equivalence; GPT Luna P50 918.13 ms Astra 1938.39 ms *theirs*; TREC-DL Jev/Luna/Astra completed; Open-Jev TREC pending; 80,816 training rows; 2B 94.71% / OOD 86.02%; 9B 97.54% / 91.97% *theirs* not Harbor; hard acc ≠ calibrated Noul; type-valid ≠ exact; Qwen/Qwen3.8-27B ≠ Archer; website https://zefan-cai.github.io/open-jev/; launch X thread https://x.com/Zefan_Cai/status/2101782158658695388 https://x.com/Zefan_Cai/status/2101786019607740436 https://x.com/Zefan_Cai/status/2101789698947793231; densify §125 not a sibling first sighting; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52; notes.md §125'
)

UNIQ_1946 = (
    'Hourly 1946 uniqueness lock: brainstormity/Jev-X-Sentiment-Analysis 136★ HEAD 5c932f941a92 README SHA bf4134b44cda; platform does not execute trades; heyjunpenn/awesome-jev 485 catalog ≠ endorsement; heyjunpenn/awesome-jev ≠ yibie/awesome-jev ≠ MrJev/awesome-jev ≠ Promethe-us/awesome-jev ≠ ckaraca/awesome-jev ≠ yzfly/awesome-jev-zh ≠ shirenchuang/awsomejev ≠ andyrewlee/awesome-system-one; NanmiCoder/jev-arena 10k comments 62.69% vs 67.26% *theirs* not gold; 203.2s $0.84 vs 823.5s $1.50 *theirs*; AI-reviewed labels ≠ gold; openroboto-ai/jev-robot-control one seed-0 trial *theirs*; Jev $0.018825 vs Astra $5.93 *theirs*; one-trial robot ≠ Harbor; endman100/research-Qwen3.8-JevLike 10.59× *theirs*; 6 class flips; agreement ≠ accuracy; probabilities uncalibrated; Qwen3.8 ≠ Archer; 10.59× systems ≠ ECE; marcosmartinez/jev-acento Spanish −6.4 pp XNLI *theirs*; ECE 0.057→0.101 *theirs*; 72.2% vs 63.4% p_max≥0.9 coverage *theirs*; alexwestco/llm-to-jev description rewrite Convert LLM prompts to Jev prompts; SHA unchanged 234058ab372d; 3★; heuristic conversion ≠ calibrated Noul; desc rewrite ≠ SHA/behavior change; skip Zefan-Cai/Open-Jev densify open #53; skip sgoedecke/system-one mithalouni/system-one-open kotoba-lang/typed-decisions open #54; ikermoel/open-alternative-jev already §49; nrdz-labs/fast-jev-opencode already §62; mallahyari/system-one-benchmark already §61; does not execute; catalog ≠ endorsement; *theirs* not Harbor; SHA move is not a replica; local_only ≠ Jev; rule-table ≠ model; replica ≠ TypeSafe; arunav25/jev-mcp ≠ jkudish/jev-mcp ≠ ThePFMind/jev-mcp ≠ burnigtm/jev-mcp; luckberonne/mini-jev ≠ r-ms/mini-jev ≠ samatv256/mini-Jev; Kwwwww74/OpenJev ≠ razorback16/openjev ≠ kyegomez/open-jev ≠ Zefan-Cai/Open-Jev; peach-zhang/typesafe-go ≠ kisshan13/typesafe-ai-go ≠ Nibir1/typesafe-go; laidick/system-one-benchmark ≠ mallahyari/system-one-benchmark; sahasrarjn/system-one ≠ sgoedecke/system-one; aboisvert/jevvy ≠ PanAchy/jevvy; andrest04/jev-lab ≠ javsanesq/jevlab; twilwa/pi-typesafe ≠ TheoOliveira/pi-jev; RuipuCui/jev-harness ≠ ismaelsoilet/jev-harness ≠ AntonioCoppe/jev-harness; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52; notes.md §131'
)


UNIQ_2049 = (
    'Hourly 2049 uniqueness lock: jaredpalmer/kev densify HEAD c096660c8da2 PLAN SHA 8d77dd271c66 README SHA unchanged 84b872488915; night-2 dates/unknowable/assertion; KEV_TEMPERATURE T≈2.0; Brier 0.291→0.267 ECE 0.105→0.039 *theirs*; 7.5%→3.2% *theirs*; grouped T rejected; Qwen3.6-35B-A3B smoke 0.812 *theirs*; 21M LoRA experts frozen; Hub --revision night2-du; MMLU-Pro 1000 Kev-9B 0.511 Jev 0.829 *theirs*; Qwen3.6 ≠ Archer; temperature scaling ≠ ECE unless measured; kotoba-lang/typed-decisions densify HEAD ff7f84e74d04 README SHA unchanged 4d6bbf4c4e44; feat expose trained OpenJev decision runtime; open_jev.py; tests/test_open_jev.py; generated_text: False; trained runtime ≠ TypeSafe; OpenJev.from_pretrained; decide_request kind typed-decisions/open-jev-v1; daftAI2026/awesome-jev ≠ heyjunpenn/awesome-jev ≠ yibie/awesome-jev ≠ MrJev/awesome-jev ≠ Promethe-us/awesome-jev; danielamitay/swev CoreML; serving substrate ≠ calibrated replica; smlayero/jev-debtgate CI gate cutoff still soft; Octalab-Inc/jqv stock Qwen3 decision API; franckverrot/lev ≠ jaredpalmer/kev; neko233-com/laya-go ≠ convaiinnovations/laya; tryAGI/TypeSafeAI ≠ official; abgregs/jev-experiments ≠ nak1b/jev-experiments ≠ dabit3/jev-experiments; jaanavit/gliner2-skill Locate ≠ decide; prasanthj/duckdb-jev SQL predicates; hf:Nebulaw1 legal LoRA ≠ RLCD replica; Qwen3.5 ≠ Archer; catalog ≠ endorsement; *theirs* not Harbor; SHA move is not a replica; skip-thin KadePrice123/jev-state-tracking hideri777/jev-application-sample; Hub --revision is a pin not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55; notes.md §132'
)

UNIQ_2146 = (
    'Hourly 2146 uniqueness lock: Zefan-Cai/Open-Jev densify HEAD a00559ea0ab2 README SHA unchanged ce1a587219e4; Publish prepared Open-Jev provider quality evaluation pipeline; 808 requests 1841 labelled decisions per model; Open-Jev GPU inference has not started; 48 CPU tests pass; Open-Jev TREC pending; 65/76 72/76 66/76 60/76 71/76 *theirs*; 117/140 109/140 135/140 *theirs*; JF100 232/300 227/300 300/300 *theirs*; FizzBuzz 299/300 300/300 300/300 *theirs*; mailroom 908/921 900/921 913/921 *theirs*; Jev TREC DL19/DL20 nDCG@10 0.275836/0.190667 strict *theirs*; Luna 0.729911/0.702082 *theirs*; Astra 0.736610/0.714484 *theirs*; provider pipeline ≠ completed Open-Jev quality; CPU tests ≠ GPU scores; tinmanlab/cartpole-jev densify HEAD 922cc61490a0 README SHA 0860958714f3; Active model Kev Not TypeSafe Jev; 81.25% 52/64 *theirs*; one record of 64; fine-tuned Kev ≠ TypeSafe Jev; softmax ≠ calibrated Noul; xuboboo/ashare-trader densify HEAD 26c7e95e6828 README SHA 7a860bdfa97b; premarket + intradaily; local probability model; QMT sidecar mock/dry default no orders; AUC 0.532 *theirs*; 36 组参数全部净期望为负; does not execute; gauravsaini/kevin first card Playwright + Onyx; Laya/Kev friends *theirs*; 3.69ms *theirs* not Harbor; metask-jev-4b 79.6% / 80.1% *theirs*; Bespoke Nimble-9B 74.8% / 63.5; Jev 76.0% / 75.3; lumen mixture-of-LoRA conformal; ardada2468/typedecide ≠ shkumbinhasani/typedecide; 87 of 144 order-unstable *theirs*; bonsai 192/231 ECE 0.037 *theirs*; 8GB; vercel-labs 95% Luna fallback; cutoff 95% still soft; tinmanlab/jev-qwen3.8-27b Qwen3.8 ≠ Archer; train-your-first-jev Qwen2.5-0.5B LoRA; sankaku-tech/jev-kit ≠ WaynezProg/jev-kit ≠ isiomaC/jevkit; jevfish DecisionScore 78.24 *theirs*; Typed Decision Bench 5387; reflex-gate CoT GBNF ≠ Noul; skip-thin IOCArena laya-mirror empty SHA; snsk JP 97.6 vs 36.9 *theirs*; yunhe-dev/awesomejev catalog ≠ endorsement; yunhe-dev/awesomejev ≠ heyjunpenn/awesome-jev ≠ daftAI2026/awesome-jev; wayfind/metask-jev ≠ metask-ai/metask-jev; mjyoke1111/jev-lab already §106; mizchi/jev-playground 19★; KaLM-Jev reranker ≠ Jev replica; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56; notes.md §133'
)

UNIQ_2246 = (
    'Hourly 2246 uniqueness lock: Zefan-Cai/Open-Jev densify HEAD 48346d0630f1 README SHA unchanged ce1a587219e4; Publish strict Open-Jev TREC evaluation preparation and context proof; Actual Open-Jev TREC model inference is pending; All 79 combined CPU tests pass; 97 queries 43 DL19 54 DL20; at most 873 requests per model; No GPU or model inference was used; TREC prep ≠ completed Open-Jev TREC; context proof ≠ nDCG; CPU tests ≠ GPU scores; Open-Jev TREC pending; TypeLLM/TypeLLM densify HEAD 8a8b4aefd443 README SHA 9f6dea3a4c8c; Add PyPI packaging and publish workflow; typellm 0.1.1; Drop fixed banner height so it scales on PyPI; Constrained AR ≠ calibrated Noul; PyPI packaging ≠ calibrated Noul; type safety does not guarantee factual accuracy; featherless-ai/simple-jev 408★ HEAD b02aa81c915a README SHA 4c5be59e9738; logits are not calibrated probabilities of correctness; does not reproduce TypeSafe; /v1/systemone alias of /v1/classifier; wire-compat ≠ logit-equiv; everyai-com/jev-directory 13★ 50 runnable evals 1300+ builds catalog ≠ endorsement; Jev-Mem 11.0% 6.6× 36.7% *theirs* not Harbor; Nyarlathoteppppp/pi-jev-context ≠ kevinpita/pi-jev-context; FogMoe/necro abandoned LoRA retrospective; LoRA ≠ RLCD replica; Qwen3.5-0.8B ≠ Archer; clarity-judge independent community project; hearim Jev-compatible Go gateway; yijunyu/jev-rs any LLM one prefill; alongL/openJev ≠ Zefan-Cai/Open-Jev; huaizuo2022/jev-ultrafast ≠ browser-use/jev-ultrafast; FluidInference/laya-coreml ≠ AndyInQtr/laya-coreai ≠ mizorewww/laya-coreml; serving substrate ≠ calibrated replica; wayfind/metask-jev-4b-policy-mix ≠ metask-ai/metask-jev; majiayu000/awesome-jev ≠ heyjunpenn/awesome-jev ≠ yibie/awesome-jev; rajasekharponakala/jev-mcp ≠ thedv91/jev-mcp ≠ jkudish/jev-mcp; skip-thin jev-droid 404 mach empty SHA; game success ≠ calibrated Noul; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57; notes.md §134'
)

UNIQ_2347 = (
    "Hourly 2347 uniqueness lock: razorback16/openjev densify HEAD 2050fdb8280d README SHA d5322e16e565; MLX backend steps>1/think/text gen + image Qs; dual serving is not generate; Hosted Codiv \u2260 TypeSafe; wire-compat \u2260 logit-equiv; SHA move is not a replica; TypeLLM/TypeLLM densify HEAD 8a8b4aefd443 README SHA unchanged 9f6dea3a4c8c; GitHub Release v0.1.1; Drop fixed banner height so it scales on PyPI; Constrained AR \u2260 calibrated Noul; PyPI packaging \u2260 calibrated Noul; type safety does not guarantee factual accuracy; zjunlp/JevLoop 6\u2605 independent not affiliated; NicolaiLassen/open-bonsai-jev \u2260 NicolaiMTLassen/open-bonzi-jev; WANLI-256 74.6% *theirs*; danielhirt/jev-lab \u2260 tanayvasishtha/jev-lab \u2260 dairui1/jev-lab \u2260 mjyoke1111/jev-lab; option order 0.188 or 0.542 *theirs*; novaleolin/jev-evolve; option order can change an answer; LabGuy94/jevtok 0 mismatches *theirs* not Harbor; ockev 35ms 95.8% TomatoEggBench *theirs* not Harbor; structured-decision-bench n=8 *theirs*; n=8 is not Harbor; Yang-SS-stack/jev-computer-use \u2260 Mrchen116/jev-computer-use; amoreX/jevvy \u2260 PanAchy/jevvy \u2260 aboisvert/jevvy; smile-magic/laya-mlx-ddz \u2260 smile-magic/laya-mlx-wzq; sriramkasyap/laya-api wire-compat \u2260 logit-equiv; hf:space:Yuki131/KaLM-Jev \u2260 KaLM-Embedding/KaLM-Jev; KaLM-Jev reranker \u2260 Jev replica; hf:soyelmismo/laya-multilingual-onnx serving substrate \u2260 calibrated replica; ranking before lossless condensation; llm-routing-jiv does not execute; jev-page-checker advisory does not block; 1deat0r/Jcua Cua-S1 \u2260 TypeSafe; Jev-Register-Tool catalog only; nexibeo/jev-cookbook already carded; leesk212/JEV-CPU already carded; kazuhideoki/jev-search already carded; skip-thin layacm empty SHA; game success \u2260 calibrated Noul; does not execute; catalog \u2260 endorsement; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58; notes.md \u00a7135"
)

UNIQ_0049 = (
    'Hourly 0049 uniqueness lock: Zefan-Cai/Open-Jev densify HEAD f46ff604f794 via afb5226982c7 README SHA e32c4bbd519c was ce1a587219e4; Publish audited JevBench public-subset baselines; community benchmark plan; diverse hard-data pipeline New model gains have not been measured; 231 public tasks 72 original 48 easy 111 hard; full 534 303 private unavailable; do not report full-534; 2B 150/231 64.94% 9B 179/231 77.49% Jev 200/231 86.58% Luna 206/231 89.18% Astra 231/231 100.00% *theirs*; Brier 0.4751 0.3219 0.1811 0.2074 0.0085 *theirs*; ECE 0.1274 0.0858 0.0318 0.0932 0.0149 *theirs*; P50 138.0 189.2 291.3 953.8 2206.4 ms *theirs*; candidate order 119 of 139 Choice; native vs verbalized; public-subset ≠ Harbor; 231 ≠ 534; Open-Jev TREC pending; 27B training not complete; LoRA ≠ RLCD replica; Qwen3.5-2B ≠ Archer; Qwen3.5-9B ≠ Archer; densify §125 not a sibling first sighting; jaredpalmer/kev densify HEAD e0bcf50153f1 README SHA unchanged 84b872488915; PLAN correct 35B MMLU-Pro (0.550); evaluate.load honour weights_dtype=bf16; Kev Qwen3.6-35B-A3B MMLU-Pro 0.550 Kev-9B 0.545 Jev 0.840 *theirs*; Not shipped; Qwen3.6 ≠ Archer; Hub --revision is a pin not a replica; wy-coliney/jev-browser-use 282★ 5-10× *theirs* not Harbor; Jev clicks Codex thinks and verifies; wy-coliney/jev-browser-use ≠ browser-use/jev-ultrafast ≠ Mrlyk/jev-browser ≠ akras14/jevbro; gargpratyush/jev-router 270★ first card fail-open routing ≠ permission; 33Audits/jev-auto ≠ gargpratyush/jev-router; BillionsBobby/JevRouter 124★ 38% 44% vs 24% *theirs* not Harbor; ordered routing ≠ end-to-end; BillionsBobby/JevRouter ≠ gargpratyush/jev-router; daseinlabs/open-jev 75★ Gemma 3 4B MLX; softmax next-token ≠ calibrated Noul; head 0.970 ECE 0.027 *theirs*; shuffled-context 0.258; daseinlabs/open-jev ≠ Zefan-Cai/Open-Jev ≠ razorback16/openjev ≠ zhlei07/openjev; skeptrunedev/jev-recruiter potential_match ≠ hiring decision; abhixhek/jevcal threshold on held-out; simulator not a Jev bench; fail-closed without fallback; AntonioCoppe/jev-harness already carded; akash-kamat/system-one-gemma 64.4% ECE 0.047 *theirs*; 200x *theirs* not Harbor; Premo-Cloud/typesafe-sdk-java unofficial; AgentBuff/awesome-jev catalog ≠ endorsement; AgentBuff/awesome-jev ≠ yibie/awesome-jev ≠ heyjunpenn/awesome-jev; Alpha-Harper-Franklin/jev-drive ≠ VennIntelligence/jev-drive; skip-thin zhlei07/openjev empty SHA khmuhtadin/n8n-nodes-jev-classification empty SHA; game success ≠ calibrated Noul; does not execute; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59; notes.md §136'
)

UNIQ_0151 = (
    'Hourly 0151 uniqueness lock: Zefan-Cai/Open-Jev densify HEAD ed45657bf726 via 748ae3024294 README SHA 12e0f581e15d was e32c4bbd519c; Publish audited v3 community data and held-out evaluation protocol; Redesign readable project site and consolidate benchmark results; 129,288 decision rows 74,921 training; frozen mixture 96,849 training; 1,280-row / 840-group comparison panel; v3 data prepared ≠ retrained released models; held-out protocol ≠ Harbor; 1,280-row panel ≠ Harbor; finite training loss ≠ quality improvement; website redesign ≠ calibration; 27B step 616 pending; Open-Jev TREC pending; LoRA ≠ RLCD replica; Qwen3.5-2B ≠ Archer; Qwen3.5-9B ≠ Archer; densify §125 not a sibling first sighting; chy4pro/jev-for-chrome 12★ community port ≠ TypeSafe; chy4pro/jev-for-chrome ≠ browser-use/jev-ultrafast; PsiACE/dohnuts 4★ small multimodal direct decisions; joint RLCD *theirs*; Dohnuts ≠ TypeSafe; catoenm/first-instinct 9B 63.3%→78.1% *theirs* not Harbor; 371,278 prepared ≠ consumed; RL did not reliably improve held-out; independent educational not a recovered Jev recipe; 123Satyajeet123/jev-wide naive throws away 83% *theirs*; 255 documented ~32,768 tokens real; two-decimal 95.8% floored *theirs*; IIA fails +0.31 ... +0.50 *theirs*; AltSlate-Labs/certo KL 0.008 acc 0.844 ECE 0.004 *theirs*; research preview independent not affiliated; endomorphosis/JevOps Jev is a gate not a generator; Lake remains admission; Jev never writes Lean; gbesse/question-forge held-out before winner; demo accuracy is synthetic not a Jev benchmark; flyryan/ai-news-aggregator 26★ does not execute; Akashdb5/jev-router ≠ gargpratyush/jev-router ≠ daviddl9/jev-router; kiuckhuang/laya-jev ≠ KonghaYao/laya-jev; tegersdorfer-collab/jevkit ≠ isiomaC/jevkit ≠ WaynezProg/jev-kit; buluoray/JevOnly already carded; yottayoshida/jev-intent-review already carded; skip-thin Iskandeur/system1-system2 zhlei07/open-system-one Hand-In/openjev-multimodal gwxcsny53/jev-watchtower empty SHA; serving substrate ≠ calibrated replica; game success ≠ calibrated Noul; does not execute; catalog ≠ endorsement; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60; notes.md §137'
)

UNIQ_0248 = (
    'Hourly 0248 uniqueness lock: hf:knowledgator/gliclass-instruct-large-v1.0 43 likes sha 825e5478c1bf apache-2.0; Efficient zero-shot and few-shot multi-task model via sequence classification; GLiClass knowledgator Hub family class-peer catalog not Jev equivalent; Knowledgator/GLiClass.c already §123; Hub models first card as class-peer entries; GLiNER/GLiClass ports are class members not Jev replicas; hf:space:mayafree/typed-decision-leaderboard 33 likes sha f4fc44077818; typed-decision-leaderboard *theirs* not Harbor; JEV 0.7350 ZTC 27B 0.7289 ZTC 397B 0.7272 *theirs* not Harbor; 2,018 items same labels; three-way tie; tacticocc/Jevbridge 33★ MIT HEAD da443ea453ac README SHA 2178333c4c3b; Jevbridge ACP and MCP adapter; does not generate text; Any LLM as System One; wire-compat ≠ logit-equiv; tshmieldev/sharp 29★ MIT HEAD 17cbd8d9cc9e README SHA 783a5cde519c; Cut the slop; Filter your X timeline; kavehmz/typesafe-playground 11★ HEAD 733991a2924a README SHA 04c0b1f6e7da; real API calls not polished benchmarks; himomohi/aside-jev 7★ MIT HEAD e570db43b0e1 README SHA 288e7c91c307; Jev picks the next action from your defined candidates; Not a Cua binding; Jev is the model Aside is the browser runtime; nico-martin/open-jev 6★ MIT HEAD 52667199e8a5 README SHA 81c0485d5833; open reproductions of the shape; Nothing is generated; nico-martin/open-jev ≠ razorback16/openjev ≠ Zefan-Cai/Open-Jev ≠ meijustory123/openjev; hf:chaoliangUNSW/Jev-Style-Qwen3.5-2B-Decision-GGUF 82.3% ECE 0.017 *theirs*; Same decision as bf16 94.4% *theirs*; Qwen3.5-2B ≠ Archer; serving substrate ≠ calibrated replica; hf:pngwn/nanodiff-350m-typed-decisions ECE 0.065 → 0.036 *theirs*; hf:litert-community/laya-LiteRT 144/144 *theirs*; gargpratyush/journey-evals A page that says Success is never accepted as proof; mpnikhil/dev-0.4b Banking77 91.33% BoolQ 85.20% *theirs*; encoder class member not Jev replica; n4ze3m/typed-decisions-synth 7,414 cases 25,859 questions; Nobody checked it; Zaious/jev-capability-atlas already carded; LocalLLaMA/typed-decisions already carded; fengyiqicoder/jevfeed already carded; Zhao-Tian-yi/awesome-jev ≠ Gerry9000/awesome-jev ≠ heyjunpenn/awesome-jev ≠ yibie/awesome-jev; kaustav1996/reflex ≠ vuckuola619/reflex; tphakala/jev-mcp ≠ jkudish/jev-mcp; ninthspace/hunch ≠ carldaws/hunch ≠ tpellet/hunch; ruban-24/switchboard ≠ cannacre8ive/switchboard-ai; hf:openjev/openjev ≠ razorback16/openjev; catalog ≠ endorsement; skip-thin Fibonaccirabbit/Jev-VLN imanshu03/jev-browser-use luca-saggese/laya.c empty SHA; game success ≠ calibrated Noul; does not execute; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61; notes.md §138'
)

UNIQ_0348 = (
    "Hourly 0348 uniqueness lock: JonathanHHenson/open-cricket MIT HEAD d75af22125ed README SHA 7d288a741089; Local structured decisions using causal language models; default Qwen/Qwen2.5-1.5B-Instruct; independent of TypeSafe; API follows Jev's general call shapes but model predictions and confidence calibration differ; wire-compat ≠ logit-equiv; Qwen2.5 ≠ Archer; replica ≠ TypeSafe; virtualman333/jev-decision-arena MIT HEAD cf6ae4ed31e8 README SHA 037f75d9610d; Greedy 0.90 vs Oracle 0.82 *theirs*; Random conf 0.00 still 20.5% *theirs*; ECE 0.180 / 0.106 / 0.205 *theirs*; confidence ≠ P(correct); game success ≠ calibrated Noul; seed 42 n=1 is not Harbor; dopeCape/typesafe-ai-test HEAD ed2adb7740d7 README SHA 183f91c36471; 8,400 calls $0.39 *theirs*; Noul 0.7 true 44% *theirs*; ≥0.9 conf 91.7% AG News *theirs*; versioned model ids rejected; *theirs* not Harbor; pCwOrM/werr 2★ MIT HEAD 2526cae98891 README SHA b29476734a09; JevBench 81.65 *theirs* not Harbor; WindTunnel 49/49 *theirs* not Harbor; 0-byte Mandelbrot is not a replica; meijustory123/OpenJev-Kit HEAD c53125982f80 README SHA a4e72c61a973; training not complete; no accuracy; Qwen3.5-0.8B ≠ Archer; meijustory123/OpenJev-Kit IS meijustory123/openjev (same GitHub id 1379187719); meijustory123/OpenJev-Kit ≠ Zefan-Cai/Open-Jev; microchipgnu/jev-hooks HEAD cbf40e64d7b2 README SHA af25fb0aaf70; Compose meaning like state; rashedInt32/jury.nvim 1★ MIT HEAD bf31e9509e7e README SHA a2b088dd0787; Code enumerates the candidates; evoke-build/evoke 1★ Apache-2.0 HEAD 310840b56f1d README SHA 02b91962cef4; Jev is the first classifier the design is bound to none; moritzkremb/jev-voice-browser densify HEAD 198a0764395a README SHA 816309fc22e6 was fa033303; context is the conversation so far; densify §82 not a sibling first sighting; luantak/is-malicious densify 18★ MIT HEAD faf6ba61d7e1 README SHA 4ae098b4b7ae; A clean report is not proof; does not sandbox; skillseedorg/ChatJEVs MIT HEAD 346e7347cf90 README SHA 6ff81d54040f; ChatJEVs ≠ erik-dunteman/ChatJev; generation from Choice is not a language model replica; chrisns/laya-mac-serve MIT HEAD f294500821b6 README SHA 00e39a7d04e2; serving substrate ≠ calibrated replica; rimusz/localjev-mlx HEAD 297836a0d95e README SHA 2d96d20e0b80; rimusz/localjev-mlx ≠ githubnext/localjev; luhayes/jev-agent-router 1★ MIT HEAD bba795a4dc4e README SHA 17a2f44993d1; does not execute; cutoff 0.8 still soft; gbesse/decision-workbench MIT HEAD 8889cf3750a3 README SHA 14a3bf79da7a; demo scores are not accuracy measurements; zhuyansen/x-reply-filter already carded; kylemclaren/jev-search ≠ kazuhideoki/jev-search; xinwang-nwpu/jev-mobile ≠ Friedjof/jev-mobile; kcd-dev/jev-skill ≠ raphael-liu/jev-skill; yanmad27/ask-jev ≠ kuhung/ask-jev; hf:s1lv3rj1nx/openjev-router-healthcare encoder class member not Jev replica; hf:akhilaaa3/openjev-v1-40705-nimble-r512-merged ≠ hf:akhilaaa3/openjev-v1-allmix-r512-merged; jevai spaces catalog ≠ endorsement; skip-thin Fibonaccirabbit/Jev-GalGame MadhavBahl/jev-guide advance-lion/dsh-jev-hooks amithgc/local-jev hiro1202/jev-review-gate-poc inlight37-design/decision-model_lab kuhung/ask-jev mmiguez314/jev-lab pomodorozhong/exp-jev vanthiet1/JevGuarAgent empty SHA; catalog ≠ endorsement; game success ≠ calibrated Noul; does not execute; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62; notes.md §139"
)

UNIQ_0445 = (
    'Hourly 0445 uniqueness lock: lucasmartins-ai/lcc 7★ MIT HEAD a7e86fb60997 README SHA 877831764be9; keeps essentially every block 0.0%/−0.5% *theirs*; mechanical −70.0% Jev −52.1% *theirs*; mock Laya = Jev −22.6% on XL withdrawn; Token reduction alone is not cost reduction; N=18 pilot not Harbor; David-Lolly/Jev-Compatible 3★ HEAD e52e963d8539 README SHA 6e5ff22d40a6; Chat 1282.3 ms vs gateway 232.1 ms ~1/5.5 *theirs*; 3/3 n=3; Softmax over candidate logprobs; Qwen3.8-27B ≠ Archer; wire-compat ≠ logit-equiv; hwfengcs/any2jev 2★ Apache-2.0 HEAD 719b0eb9eefe README SHA 27e0af212cd5; independent not affiliated; acc 0.796 ECE 0.027 *theirs*; 42 ms vs JSON 778 ms *theirs*; Snake acc 0.953 ECE 0.034 *theirs*; Qwen3-0.6B ≠ Archer; /v1/systemone wire-compat ≠ logit-equiv; TianyuCodings/NanoJev densify HEAD 76fdfc9ecdca README SHA a8f8afeb7e44 was 618cea6d / 4190093c64ee; Add JevHarness project link to READMEs; densify §115 not a sibling first sighting; SHA move is not a replica; jjd-lab/jev-synthetic-survey MIT HEAD 9ca8c4ab94bb README SHA ec1664288d50; How you ask mattered more; Noul TVD 0.1530 vs GPT 0.1789 *theirs*; ECE 0.1472 *theirs* not Harbor; missed 0.05 bar; 67.28% vs 64.78% *theirs*; $4.02 vs ~$136 *theirs*; independent work; CankatSarac/jev-arcade MIT HEAD b2e45ed3c1c6 README SHA 1f06af0f4c74; snake 70/80 *theirs*; tetris 167 vs heuristic 2333 *theirs*; 74% conf <0.5 *theirs*; Calibration is not yet measured; three seeds not Harbor; game success ≠ calibrated Noul; sszxt/rlcd HEAD 66ca01664d6b README SHA 3da08d46758d; ECE 0.490→0.423 Brier 0.487→0.409 *theirs*; Yang 2023 contrastive ≠ TypeSafe RLCD; Qwen2.5 ≠ Archer; still overconfident; hf:AXERA-TECH/Laya sha 51a586cd14e2 apache; AX650 NPU 69.991/27.722/69.990 ms *theirs*; seq 256 up to 4 options; serving substrate ≠ calibrated replica; base convaiinnovations/laya; hf:openjev/openjev-MLX-4bit sha c59bf1eed7d8 cc-by-nc-4.0; ~15 GB 4-bit affine; independent not affiliated; hf:openjev/openjev-MLX-4bit ≠ razorback16/openjev; hf:GeekyAbs/laya sha b65d05b4d9eb; GeekyAbs/laya ≠ convaiinnovations/laya; hf:alfred361/laya-web sha 33f171161da5; 100% argmax *theirs*; multilingual-int8 93.8% / worst shift 16.9 pts *theirs*; 50bbx/laya-needle Apache HEAD 01961bade52f README SHA ecaff4dfd271; threshold 0.58 still soft; local Laya ≠ hosted Jev; yunhai-dev/laya2typesafeapi HEAD 4aeb89be286b README SHA d2e5d114fcd8; TypeSafe-compatible ≠ TypeSafe replica; iamdgarcia/openJev MIT HEAD 62bbc30eece2 README SHA 55614ad8caab; independent educational; not local inference; iamdgarcia/openJev ≠ alongL/openJev ≠ Zefan-Cai/Open-Jev; chrisns/homebrew-laya-mac-serve MIT HEAD 1b3c4c0bdb70 README SHA 5e58082b7e9b; tap for chrisns/laya-mac-serve §139; serving substrate ≠ calibrated replica; nk412/judgements MIT HEAD 6624e53c86cc README SHA 86fe465f7887; pydantic wrapper; threshold 0.5 still soft; JingHao-Leon/awesome-jev-apps MIT HEAD d3ef0254c4b2 README SHA fd38a3c4ff2e; catalog ≠ endorsement; JingHao-Leon/awesome-jev-apps ≠ heyjunpenn/awesome-jev; Manta-Boardgame/jev-chat HEAD 44721bae8c2e README SHA 03272e4b9a9f; unofficial; 98% confidence *theirs*; ximing/jev-snake-game HEAD 1e80283f458e README SHA 0a54b74eb095; 用 TypeSafe Jev 驱动的自动贪吃蛇; hf:dataset:syvai/danish-dynaword-laya gated HTTP 401; size_categories 10K<n<100K; devbackend/jevgo ≠ kisshan13/typesafe-ai-go ≠ peach-zhang/typesafe-go; qiudingkai-crypto/jevai and Strernd/beer-jev share README SHA e215bc4ccf13 template collision; skip-thin Adrian-lzr/jev-spire-brain Dililianxice/jev-robotic-arm-benchmark baltzparra/jev-study lzero07/jev-laya-statement qq150078158-lab/TDM-demo empty SHA; Awesomejev 691→802 (+111) / 38194→52151 stars quote watch not re-derive; tracker likes 81 lastModified UNCHANGED; Softmax over options ≠ calibrated Noul; catalog ≠ endorsement; game success ≠ calibrated Noul; does not execute; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62/#63; notes.md §140'
)

UNIQ_0551 = (
    'Hourly 0551 uniqueness lock: jaredpalmer/kev densify HEAD 4f8110a3f862 README SHA d497d4b89427 was e0bcf50153f1 / 84b872488915; Night-2 sign-off; dates+unknowable deltas promoted for 0.8B/4B/9B; v7-base tags; PLAN SHA 5e6d2fca508e; locked OOD 0.684/0.837/0.852 *theirs*; test Kev-9B 0.837→0.852 *theirs*; Kev-4B 0.832→0.837 *theirs*; Kev-0.8B 0.668→0.684 *theirs*; T≈2.0 Brier 0.291→0.267 ECE 0.105→0.039 *theirs*; 7.5%→3.2% *theirs*; grouped T rejected; date_facts deadline 9B 0.72→0.80 raw→0.90 preprocessor; unknowable ≥0.9 → 0.00; 35B Not shipped MMLU-Pro 0.550 *theirs*; coverage@5% 0.62 from 0.66 at 9B *theirs*; not a controlled architecture comparison; Qwen3.5 ≠ Archer; Qwen3.6 ≠ Archer; temperature scaling ≠ ECE unless measured; Hub --revision is a pin not a replica; densify §45 not a sibling first sighting; SHA move is not a replica; bespokelabsai/nimble densify HEAD f136b3f75721 README SHA b3a04a310f1e; Publish original 2676 training examples and frozen 324 holdout; 90.1% vs Jev 93.2% vs base 66.4% *theirs*; did not distill from Jev; densify §35 not a sibling first sighting; AbdelStark/awesome-typesafe-jev 416★ MIT HEAD a6a68b57888a README SHA e47993484e3a github_id 1374058281; Independent community project; catalog ≠ endorsement; AbdelStark/awesome-typesafe-jev IS AbdelStark/awesome-typesafe (same GitHub id 1374058281); cookiespiggy/agentic-rl 103★ MIT HEAD 072bdd8c69de README SHA f2cc68b4e214; ch.25 Jev vs RL; RL ≠ calibrated Noul; DevMortimer/pi-typesafe 27★ MIT HEAD 8dcaa887e22c README SHA 6a11fb9df8b9; DevMortimer/pi-typesafe ≠ twilwa/pi-typesafe ≠ TheoOliveira/pi-jev; hf:gump2049/APUS-OpenJev-v1 sha e7e3cc0b9c82; APUS-OpenJev 9B 85.0% vs Jev API 82.5% *theirs* not Harbor; Frozen80 n=80; Candidate probabilities are not calibrated confidence; Qwen3.5-4B ≠ Archer; Qwen3.5-9B ≠ Archer; hf:SeanLiu/Jev-Vision sha 9b77fa5fdcd0 apache-2.0; POPE 0.907 MME 0.927 NLVR2 0.930 *theirs*; yes/no ECE 0.034 to 0.047 *theirs*; JevBench hard 52% at 91% mean confidence *theirs*; Qwen3-VL-8B ≠ Archer; LoRA ≠ RLCD replica; wire-compat ≠ logit-equiv; hf:SeanLiu/Jev-Vision ≠ sseanliu/Jev-Vision; evoke-build/evoke densify 6★ HEAD ca8a311743fe README SHA fcce876e2cab was 310840b56f1d / 02b91962cef4; Jev is the first adapter the design is bound to no engine; densify §139 not a sibling first sighting; 47thtechcorner/RayCodes_GLiNER_V1_Multi densify HEAD 485cf8045f73 README SHA 035b339c3789; Zero Hallucinations marketing; Locate ≠ decide; kylemclaren/jevsearch ≠ kylemclaren/jev-search ≠ kazuhideoki/jev-search; stacklok/typesafe-go ≠ kisshan13/typesafe-ai-go ≠ peach-zhang/typesafe-go ≠ Nibir1/typesafe-go; sontakey/awesome-jev ≠ heyjunpenn/awesome-jev ≠ yibie/awesome-jev ≠ AbdelStark/awesome-typesafe-jev; Giustino98/system-one-bench ≠ mallahyari/system-one-benchmark; skip-thin eatmoreduck/jev-jarvis githubMJ/Laya4j hawkymisc/typed-decision-bert jayanthbagare/laya_examples mohamedAtoui/Jev-project petrixh/laya-test sidhasadhak/jev-perfume-advisor wendaoheri/jev-browser zohaibtanwir/jev-samsho2 empty SHA; game success ≠ calibrated Noul; does not execute; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62/#63/#64; notes.md §141'
)

UNIQ_0707 = (
    'Hourly 0707 uniqueness lock: Sac-Y/Jev-cu 524★ HEAD e2cc92d731fa README SHA 3deeafbc870f; 只传文字，不传截图; Text only no screenshots; Codex CU executes; local policy gates; kyotofin/tax-doc-classifier 322★ Apache-2.0 HEAD 3e95a77f763c README SHA 72c4f74b542e; 100% of our tax document corpus at $0.001 per page; TaxCalcBench 0 strict errors *theirs*; blank IRS 38 strict errors 5.05% *theirs*; 34× cheaper and 6× faster *theirs*; 261 IRS forms; 100% of corpus *theirs* not Harbor; fhshaik/typesafe-mario 319★ HEAD ca22449ed187 README SHA c489f9350414; The model does not receive screenshots; game success ≠ calibrated Noul; droidrun/mobile-jev 307★ MIT HEAD 395fc222beac README SHA d257fed2c5f7; 21 seconds for 9 actions *theirs*; A completed booking is not demonstrated; droidrun/mobile-jev ≠ Friedjof/jev-mobile; realZachi/pg-jev 269★ HEAD afd11fa856d7 README SHA e8735928b57d; giuliosmall/pg_typesafe ≠ realZachi/pg-jev; kitze/skillbox 220★ MIT HEAD cda64ad3310a README SHA dedcb6be3c39; itsmostafa/typesafe-mcp 181★ MIT HEAD d4c110c7edd8 README SHA 2bd68aff4299; itsmostafa/typesafe-mcp ≠ cyrusasco/typesafe-mcp ≠ burnigtm/jev-mcp; kitze/unclutter 157★ MIT HEAD 9ef9beccc1e5 README SHA 5ad63c67fd02; standardagents/jevpilot 147★ HEAD e1beeb13b9a9 README SHA ec386a81e12c; AbdelStark/awesome-typesafe-jev densify 417★ MIT HEAD d6ea2a0d6cf4 README SHA 234ae59a0b16 was a6a68b57888a / e47993484e3a; The field guide to typed decisions; Independent community project; densify §141 not a sibling first sighting; SHA move is not a replica; hf:Praveenrajus/jev-bench HTTP 401 was 200; densify §107/§125 remainder; *theirs* not Harbor; hf:wayfind/metask-jev-4b-policy-mix densify sha 5ecdd272ab4a README SHA c534ee82b141; densify §134 not a sibling first sighting; wayfind/metask-jev-4b-policy-mix ≠ metask-ai/metask-jev; patryckalves/jev-no-enem HEAD 7f85f787e3d1 README SHA 237b308df062; ENEM 2025 *theirs* not Harbor; 56.6% (103/182) *theirs*; ECE 0.078 *theirs*; Ying-Kai-Liao/jev-browser ≠ wy-coliney/jev-browser-use; w3cj/jev-chat ≠ Manta-Boardgame/jev-chat; snellingio/system-one ≠ sgoedecke/system-one ≠ Luke458/system-one ≠ developerekene/System-One; stoleas/typesafe-computer-use ≠ awlevin/typesafe-computer-use; holotwist/laya ≠ NandhaKishorM/laya; RafalWilinski/vibecheck ≠ psyb0t/vibecheck; dannote/jev ≠ okooo5km/jev ≠ sebastianbugal/jev; skip-thin developerekene/System-One holotwist/laya wuzhiping/jev-laya empty SHA; hf:s1lv3rj1nx/openjev-healthcare-router HTTP 401 *theirs*; hf:s1lv3rj1nx/openjev-heldout HTTP 401 *theirs*; hf:s1lv3rj1nx/openjev-mixture HTTP 401 *theirs*; catalog ≠ endorsement; game success ≠ calibrated Noul; does not execute; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62/#63/#64/#65; notes.md §142'
)

UNIQ_0823 = (
    "Hourly 0823 uniqueness lock: PsiACE/dohnuts densify 11★ Apache-2.0 HEAD 253766e5fcb7 README SHA 4b5b019deba9 was a5049834489c / e1b448c440b5; MODEL_CARD + training dataset refs; JevBench 65.80% vs Jev 86.58% / Laya multi 47.62% *theirs*; 152 / 231 *theirs*; 78.21% macro accuracy *theirs*; 180,031 decisions *theirs*; Qwen3.5-0.8B; Joint RLCD *theirs*; Dohnuts ≠ TypeSafe; densify §137 not a sibling first sighting; same-species serving not an 18th scoring row; SHA move is not a replica; FluidInference/FluidUse 3★ Apache-2.0 Swift HEAD c18071d791eb README SHA f1cba4a244bb; on-device Mac form CU; Accessibility API; CUA-S1-FORMS CoreML ~706K params ~1ms Neural Engine; field→value match among supplied options not free text; Cua-S1 ≠ TypeSafe; FluidInference/FluidUse ≠ FluidInference/laya-coreml ≠ AndyInQtr/laya-coreai ≠ mizorewww/laya-coreml; serving substrate ≠ calibrated replica; shhivv/third-hand 274★ MIT Swift HEAD 430394b35dbb README SHA b615d7c3fd19; Screenshots aren't uploaded; Jev is the only model; not fully offline; typesafe-ai/system-one-adapter-python 226★ MIT HEAD adffc2eab300 README SHA d01afbf0499e; Drop-in TypeSafeClient replacement backed by LLM APIs; wire-compat ≠ logit-equiv; typesafe-ai/typesafe-sdk-js 203★ MIT HEAD 66880ccded6c README SHA 7e834076c14e; typesafe-ai/typesafe-sdk-python 175★ MIT HEAD 2ce5c65f1364 README SHA 361a3bc13e19; catalog ≠ endorsement; r-ms/mini-jev 40★ MIT HEAD ca612198bfb6 README SHA 565b70c4cf4d; read the option letter's logits instead of generating JSON; yuki-oshio/mini-jev ≠ r-ms/mini-jev; JSON 0.909 letters 0.907 *theirs*; 13 600 / 13 600 *theirs*; softmax over letters ≠ calibrated Noul; Das-rebel/a3m-router 16★ MIT HEAD 62caefe59315 README SHA c19e802d5cf2; model=jev-auto; routing ≠ permission; AbdelStark/jev-benchmarks 13★ Apache-2.0 HEAD 0d610cc53e79 README SHA 5fd3627f7de4; AG News 0.910 *theirs*; Banking77 0.870 *theirs*; DAIR Emotion 0.480 *theirs*; *theirs* not Harbor; browser-use/jev-ultrafast densify 14622★ MIT HEAD 1231850a0bf1 README SHA fa7d079f9192; Fastest and cheapest web agent *theirs*; densify description rewrite; pythongiant/laya-drift densify 4★ HEAD 334953e5cb8f README SHA 6662121ba0f3 was fc94b71cf7dd / 55ef2343ee5d; opencode plugin to calculate agentic drift over time *theirs*; densify §142 not a sibling first sighting; BlinkWrite/pii-masker densify 1★ MIT HEAD 6ad202ab4443 README SHA 27931758af6c; On-device reversible PII masking *theirs*; Locate ≠ decide; TypeSafeAI/typesafe-playground ≠ kavehmz/typesafe-playground ≠ nickthompson480/typesafe-ai-playground; siliconkernel/vllm-jev-decison 8★ MIT HEAD a9362d52b9a8; No generative fallback; Stumble/jev-go 3★ MIT HEAD a475dc925ba6; Twister915/typesafe-ai 11★ Apache-2.0 Rust HEAD d4455efb1d06; rorshopping/jev-on-a-laptop 23★ HEAD 5821d9106103; Unofficial research repo. Not affiliated with TypeSafe AI; Qwen2.5 ≠ Archer; skip-thin GokhanCalkap/LayaCode fredzhaozonghui/LAYA1 empty SHA; Abhi895/Laya ≠ convaiinnovations/laya; mjdileep/OpenJev ≠ Zefan-Cai/Open-Jev; Abhi001vj/system-one-open ≠ mithalouni/system-one-open ≠ sgoedecke/system-one; ZulfiFazhar/system-one ≠ sgoedecke/system-one; Futureppo/typesafe_register key-farming skip; soft scores ≠ hard gates; catalog ≠ endorsement; game success ≠ calibrated Noul; does not execute; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62/#63/#64/#65/#66; notes.md §143"
)


UNIQ_0923 = (
    'Hourly 0923 uniqueness lock: vericle/intellyweave 76★ BSD-3-Clause Py HEAD ff4152ce9d20 README SHA 3afa702012e8; GLiNER OSINT; Locate ≠ decide; genai-craft/openvons 13★ NOASSERTION Py HEAD c2683c4539a7 README SHA 85164d409725; finite choices + none; 4B frozen+head 0.916 vs 27B zs 0.875 *theirs*; 8 questions 22.6 ms *theirs*; softmax ≠ calibrated Noul; whyashthakker/beam-cli 11★ AGPL-3.0 TS HEAD 5162ec66179a README SHA d55847ca5681; AgentBeam local security layer; soft scores ≠ hard gates; atharvamhaske/typesafe-sdk-go 8★ MIT Go HEAD 6ea04182d356 README SHA 8d90abda1f58; unofficial not affiliated; wire-compat ≠ logit-equiv; atharvamhaske/typesafe-sdk-go ≠ kisshan13/typesafe-ai-go ≠ stacklok/typesafe-go ≠ Nibir1/typesafe-go ≠ peach-zhang/typesafe-go ≠ draganm/go-jev ≠ kataras/jev ≠ robertjndw/gosys1 ≠ Stumble/jev-go; Prophetlab/JevPokerBench 7★ MIT Py HEAD 9c9816688a3c README SHA 0fcd6807b9c3; chips virtual; game success ≠ calibrated Noul; *theirs* not Harbor; tyler-dot-earth/patdown densify 11★ NOASSERTION TS HEAD 8b2b2b591470 README SHA 1052b6da2c25 was ae0e277fdd64 / 275f4b9c; Block/steer/fuzzy lint; judge swappable; default TypeSafe/Jev; provider-neutral; densify §121 not a sibling first sighting; evoke-build/evoke densify 8★ Apache-2.0 Rust HEAD 50c9637ef11f README SHA 72ec0e65c432 was ca8a311743fe / fcce876e2cab; Jev is the first adapter; the design is bound to no engine; densify §139 not a sibling first sighting; lukstei/slop-grader 5★ MIT TS HEAD b60332684ff8 README SHA bbc1604754d3; Runs every rule against every line in parallel. No skimming; sumleo/prompt2jev densify 2★ MIT Py HEAD f3b6bc763b74 README SHA 3d58e8c10075 was bd9cd8a471a6 / afc36885861e; heuristic conversion ≠ calibrated Noul; densify §141 not a sibling first sighting; Andymulb/jev_the_philosopher 0★ MIT TeX HEAD 334e3f9b83e5 README SHA 8db05448b75f; Median 275 ms; trolley 0.99 vs 0.78; 11/11/7 match/differ/undecided of 29 *theirs*; PerryLink/layacore 0★ Apache HEAD 12afe3af5edc README SHA f78b73d21cf7; retired name reservation; the project is now PerryLink/laya-mcp; retired name reservation is not a replica; PerryLink/layacore-mcp HEAD b006cc7c3f87 README SHA 1177f286f3f8; PerryLink/laya-mcp-npm launcher not implementation HEAD 426e965b4c48 README SHA 98ed0d448b09; PerryLink/laya-mcp ≠ wsargent/laya-mcp; DreamBlooms/dohnuts.cpp ≠ PsiACE/dohnuts; ClemensSchartmueller/jev-guard ≠ leepokai/jev-guard ≠ seb4ez/jevguard; AABBAASS1/jev-router ≠ gargpratyush/jev-router ≠ Akashdb5/jev-router ≠ daviddl9/jev-router; wustep/jev-playground ≠ AbnormalPilot/jev-playground ≠ mizchi/jev-playground; Li-Evan/awesome-jev ≠ Omrigotlieb/awesome-jev ≠ youzizzz1028/Awesome-Jev ≠ heyjunpenn/awesome-jev ≠ yibie/awesome-jev; sunchojack/jev-cli ≠ gnapse/jev-cli; Alistair77/openjev ≠ Zefan-Cai/Open-Jev ≠ razorback16/openjev; jev-jarvis/jev-jarvis ≠ eatmoreduck/jev-jarvis; Renwang-Huang/typesafe-mcp ≠ itsmostafa/typesafe-mcp; inematds/laya ≠ convaiinnovations/laya ≠ NandhaKishorM/laya; kataras/jev ≠ okooo5km/jev ≠ sebastianbugal/jev ≠ dannote/jev; ai-ecoverse/kev.js ≠ jaredpalmer/kev; skip-thin gnapse/jev-cli HTTP 404 fr4j4/system-one-arena nothingmn/Jev.Sdk youniszhang/jev-local Vaibhaav-Tiwari/fly-doom-jev fengliner/jev-tank-battle ngouard5/jeveuxaider-design empty SHA; hf:Skylarcc/Laya-Online HTTP 401 *theirs*; hf:piratehack009/laya-cn-flash-triage HTTP 404 *theirs*; catalog ≠ endorsement; game success ≠ calibrated Noul; does not execute; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62/#63/#64/#65/#66/#67; notes.md §144'
)

UNIQ_1019 = (
    "Hourly 1019 uniqueness lock: praneeth16/adapting-jev-with-gepa ADE Corpus V2 GEPA; schema-valid is not the same as correct; API confidence is not P(correct); GEPA revises Choice instructions/criteria with weights fixed; jev-1.13.0 weights fixed; Brier 0.1357\u21920.0747 *theirs*; F1 69.1%\u219279.7% *theirs*; FN 4\u21926; review-queue policy is not F1; Soft is not gate; Not an 18th scoring-table species; aliaihub/awesome-jev-usecases 15\u2605 NOASSERTION HEAD 6cbde6bd3569 README SHA 7ea135c6345d; Every claim is labeled and sourced; catalog \u2260 endorsement; aliaihub/awesome-jev-usecases \u2260 anandi1989/awesome-jev-usecases \u2260 whyashthakker/awesome-jev-use-cases; rezoch340/jev-chat-JARVIS-windows 6\u2605 MIT Py HEAD 26b686301437 README SHA 0714736b68c3; \u53d1\u9001\u6c38\u8fdc\u624b\u52a8; rezoch340/jev-chat-JARVIS-windows \u2260 Finderchangchang/jev-chat-JARVIS; iamvatsalpatel/tiershift 3\u2605 MIT TS HEAD 16a0826b9f62 README SHA 46fcb1cb191b; About 180 ms; routing \u2260 permission; Bring-AI/jev-rl 2\u2605 MIT Py HEAD 36f89cec85a2 README SHA 6283da6011b7; $0.00241 *theirs*; daniel4x/JevEmon 2\u2605 GPL-3.0 HEAD 572454c69bf7 README SHA 8fc00d12848d; Not a screenshot agent; game success \u2260 calibrated Noul; spoonnotfound/soupbase 2\u2605 MIT TS HEAD 3e874e83e710 README SHA 3106bc96d6ab; Nabsku/pi-follow-through 1\u2605 MIT TS HEAD c62ef28ff4ac README SHA 64000451b79e; pi-follow-through threshold 0.8 still soft; dashbi1/jev-sim 1\u2605 MIT Py HEAD 753c7397d73c README SHA 05fd960799d2; wire-compat \u2260 logit-equiv; jev-jarvis/jev-jarvis densify 8\u2605 MIT Py HEAD a94e3b967ef5 README SHA e441335b1df0 was be68dd7993f0 / efe7e47a6fe8; densify \u00a7144 not a sibling first sighting; Nyarlathoteppppp/pi-jev-context densify 5\u2605 MIT TS HEAD 96371e2bf144 README SHA d4276222a436 was f0128a86478f; pi-jev-context densify \u00a7134 not a sibling first sighting; Nyarlathoteppppp/pi-jev-context \u2260 kevinpita/pi-jev-context; fly88oj/jebii 0\u2605 MIT JS HEAD 5cbe527ed791 README SHA b4a76b8aba9d; generallymatthew/factlabel 0\u2605 Apache-2.0 Py HEAD b3d3bceee044 README SHA b1cda6c4646e; aakgna/jevcal \u2260 abhixhek/jevcal; 007M7/jev-chat \u2260 w3cj/jev-chat \u2260 Manta-Boardgame/jev-chat; fstandhartinger/jev-router \u2260 gargpratyush/jev-router; prakash7474/Jev_guard \u2260 leepokai/jev-guard; rdutra/laya-mcp \u2260 PerryLink/laya-mcp \u2260 wsargent/laya-mcp; Kourin1996/jev-playground \u2260 wustep/jev-playground; ai-ecoverse/cua-s1.js Cua-S1 \u2260 TypeSafe; skip-thin Unnati-23/jev-typesafe-guide antoniofaical/digital-twin-classifier-jev leonezhu/agent-kits empty README; skip-thin wjw66/deepseek-harness-jev-pre-compaction ziwon/jev-actor empty SHA HTTP 409; hf:chanoian/openjev-mlx-demo HTTP 401 *theirs*; hf:clduab11/jev-calibration-statistics HTTP 401 *theirs*; hf:yasserrmd/laya-lab HTTP 401 *theirs*; catalog \u2260 endorsement; game success \u2260 calibrated Noul; does not execute; routing \u2260 permission; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62/#63/#64/#65/#66/#67/#68/#69; notes.md \u00a7145"
)



REVISIT_LOCK = (
    "Revisit / since-last-look lock: catalogued repos are not done; "
    "store fingerprints default_sha, pushed_at, description_hash, release_tag; "
    "material change is README/API/release/calibration claim/serving port/bench rewrite; "
    "star-noise is stars/likes/forks alone; densify the prior notes section, "
    "do not mint a sibling first sighting; do not invent equivalence; "
    "SHA move is not a replica; treat revisit HIGH like novel HIGH for Augustus; "
    "notes.md §122"
)

REVISIT_OVERLAYS = [
    ".agents/skills/augustus/SKILL.md",
    "research/notes.md",
    "research/README.md",
    "research/revisit-checklist.md",
    "CONTRIBUTING.md",
]

OVERLAYS = [
    "research/notes.md",
    "research/changelog-hourly.md",
    "research/refresh-log.md",
    "research/archive/findings.md",
    "docs/ecosystem.md",
    ".agents/skills/augustus/SKILL.md",
    ".agents/skills/augustus/references/applied-mappings.md",
    ".agents/skills/augustus/references/faq.md",
    ".agents/skills/augustus/references/mental-models.md",
    ".agents/skills/augustus/references/composition-algebra.md",
    ".agents/skills/augustus/references/mixed-architecture.md",
    ".agents/skills/augustus/references/validation.md",
    ".agents/skills/augustus/references/judgment-class.md",
    ".agents/skills/augustus/references/formal-methods.md",
    ".agents/skills/augustus/references/formal-semi-formal.md",
    ".agents/skills/augustus/references/methods-catalog.md",
    ".agents/skills/augustus/references/toolbox-mapping.md",
    ".agents/skills/augustus/references/mappings.md",
    ".agents/skills/augustus/references/agent-self-assessment.md",
    ".agents/skills/augustus/references/question-design.md",
]


def load_skill_frontmatter(text: str) -> dict:
    if not text.startswith("---"):
        raise AssertionError("SKILL.md missing YAML frontmatter")
    end = text.find("\n---\n", 3)
    if end < 0:
        raise AssertionError("SKILL.md frontmatter not closed")
    data = yaml.safe_load(text[3:end])
    if not isinstance(data, dict):
        raise AssertionError("SKILL.md frontmatter is not a mapping")
    return data


LICENSE_HEADING = "\n## License\n"
LICENSE_END = (
    "MIT. See [LICENSE](LICENSE). Security reports: [SECURITY.md](SECURITY.md).\n"
    "Contributions: [CONTRIBUTING.md](CONTRIBUTING.md)."
)
_HOURLY_USER_LINE = re.compile(
    r"(?im)^\s*(?:[-*]+\s+|\*\*)?(Hourly|User-provided)\b"
)
_FOLD_RESIDUE = re.compile(
    r"(?is)(uniqueness lock|Hourly\s+\d|User-provided|"
    r"notes\.md|invented_signal|does not bump|fold HIGH)"
)


def readme_after_license(readme: str):
    """Return text after the License heading, or None if missing."""
    idx = readme.find(LICENSE_HEADING)
    if idx >= 0:
        return readme[idx + len(LICENSE_HEADING) :]
    if readme.startswith("## License\n"):
        return readme[len("## License\n") :]
    return None


def readme_dump_wall_violations(readme: str) -> list[str]:
    """Fail if the package README holds uniqueness locks or fold residue.

    Human README stops at License. Locks live in notes.md / overlays /
    uniqueness_gate fixtures, not README.md.
    """
    failed = []
    if "README.md" in OVERLAYS:
        failed.append("README.md must not be a uniqueness overlay")
    if "uniqueness lock" in readme:
        failed.append(
            "README.md holds uniqueness lock "
            "(human README is not a fold overlay)"
        )
    after = readme_after_license(readme)
    if after is None:
        failed.append("README.md missing ## License heading")
        return failed
    if LICENSE_END not in after:
        failed.append(
            "README.md License block is not the MIT / SECURITY / "
            "CONTRIBUTING ending"
        )
        extra = after
    else:
        extra = after.split(LICENSE_END, 1)[1]
    extra_stripped = extra.strip()
    if extra_stripped:
        failed.append(
            "README.md continues after the License block "
            "(human README must stop at License)"
        )
        if "uniqueness lock" in extra:
            failed.append("README.md holds uniqueness lock after ## License")
        if _HOURLY_USER_LINE.search(extra):
            failed.append(
                "README.md Hourly/User-provided uniqueness-lock or HIGH "
                "prose after ## License"
            )
        for para in re.split(r"\n\s*\n", extra):
            blob = para.strip()
            if len(blob) > 200 and _FOLD_RESIDUE.search(blob):
                failed.append(
                    "README.md fold residue after ## License "
                    f"(paragraph {len(blob)} chars)"
                )
                break
    return failed


def readme_dump_wall_self_test() -> list[str]:
    """Negative fixture: a lock after License must fail the dump-wall check."""
    failed = []
    good = (
        "# Augustus\n\nDesign judgment for the decision-model class.\n"
        + LICENSE_HEADING
        + "\n"
        + LICENSE_END
        + "\n"
    )
    if readme_dump_wall_violations(good):
        failed.append(
            "readme dump-wall self-test: clean License README must pass"
        )
    bad_lock = good + "Hourly 0823 uniqueness lock: dohnuts densify;\n"
    if not any("uniqueness lock" in m for m in readme_dump_wall_violations(bad_lock)):
        failed.append(
            "readme dump-wall self-test: uniqueness lock after License must fail"
        )
    bad_high = good + "- Hourly 0823 HIGH (`research/notes.md` §143).\n"
    if not readme_dump_wall_violations(bad_high):
        failed.append(
            "readme dump-wall self-test: Hourly HIGH after License must fail"
        )
    long_para = (
        "Hourly fold residue that restates notes.md invented_signal false "
        "and does not bump 0.5.0 " * 8
    )
    bad_long = good + long_para + "\n"
    hits = readme_dump_wall_violations(bad_long)
    if not any("fold residue" in m or "continues after" in m for m in hits):
        failed.append(
            "readme dump-wall self-test: long fold residue after License must fail"
        )
    return failed


def main() -> int:
    failed = []
    failed.extend(readme_dump_wall_self_test())
    for rel in OVERLAYS:
        path = ROOT / rel
        if not path.is_file():
            failed.append(f"missing {rel}")
            continue
        body = path.read_text(encoding="utf-8")
        if UNIQ_0843 not in body:
            failed.append(f"0843 lock missing as one substring: {rel}")
        if UNIQ_0915 not in body:
            failed.append(f"0915 lock missing as one substring: {rel}")
        if UNIQ_JCR not in body:
            failed.append(f"jcr lock missing as one substring: {rel}")
        if UNIQ_0922 not in body:
            failed.append(f"0922 lock missing as one substring: {rel}")
        if UNIQ_0940 not in body:
            failed.append(f"0940 lock missing as one substring: {rel}")
        if UNIQ_0947 not in body:
            failed.append(f"0947 lock missing as one substring: {rel}")
        if UNIQ_1049 not in body:
            failed.append(f"1049 lock missing as one substring: {rel}")
        if UNIQ_1143 not in body:
            failed.append(f"1143 lock missing as one substring: {rel}")
        if UNIQ_1248 not in body:
            failed.append(f"1248 lock missing as one substring: {rel}")
        if UNIQ_1340 not in body:
            failed.append(f"1340 lock missing as one substring: {rel}")
        if UNIQ_1441 not in body:
            failed.append(f"1441 lock missing as one substring: {rel}")
        if UNIQ_1542 not in body:
            failed.append(f"1542 lock missing as one substring: {rel}")
        if UNIQ_1643 not in body:
            failed.append(f"1643 lock missing as one substring: {rel}")
        if UNIQ_1746 not in body:
            failed.append(f"1746 lock missing as one substring: {rel}")
        if UNIQ_1843 not in body:
            failed.append(f"1843 lock missing as one substring: {rel}")
        if UNIQ_1936 not in body:
            failed.append(f"1936 lock missing as one substring: {rel}")
        if UNIQ_OPENJEV not in body:
            failed.append(f"openjev densify lock missing as one substring: {rel}")
        if UNIQ_1946 not in body:
            failed.append(f"1946 lock missing as one substring: {rel}")
        if UNIQ_2049 not in body:
            failed.append(f"2049 lock missing as one substring: {rel}")
        if UNIQ_2146 not in body:
            failed.append(f"2146 lock missing as one substring: {rel}")
        if UNIQ_2246 not in body:
            failed.append(f"2246 lock missing as one substring: {rel}")
        if UNIQ_2347 not in body:
            failed.append(f"2347 lock missing as one substring: {rel}")
        if UNIQ_0049 not in body:
            failed.append(f"0049 lock missing as one substring: {rel}")
        if UNIQ_0151 not in body:
            failed.append(f"0151 lock missing as one substring: {rel}")
        if UNIQ_0248 not in body:
            failed.append(f"0248 lock missing as one substring: {rel}")
        if UNIQ_0348 not in body:
            failed.append(f"0348 lock missing as one substring: {rel}")
        if UNIQ_0445 not in body:
            failed.append(f"0445 lock missing as one substring: {rel}")
        if UNIQ_0551 not in body:
            failed.append(f"0551 lock missing as one substring: {rel}")
        if UNIQ_0707 not in body:
            failed.append(f"0707 lock missing as one substring: {rel}")
        if UNIQ_0823 not in body:
            failed.append(f"0823 lock missing as one substring: {rel}")
        if UNIQ_0923 not in body:
            failed.append(f"0923 lock missing as one substring: {rel}")
        if UNIQ_1019 not in body:
            failed.append(f"1019 lock missing as one substring: {rel}")
        if "meijustory123/OpenJev-Kit ≠ meijustory123/openjev" in body:
            failed.append(
                "0348 false namesake lock still present "
                "(OpenJev-Kit IS openjev, same GitHub id 1379187719): "
                f"{rel}"
            )
    if "meijustory123/OpenJev-Kit IS meijustory123/openjev (same GitHub id 1379187719)" not in UNIQ_0348:
        failed.append("UNIQ_0348 missing OpenJev-Kit IS openjev same-id lock")
    if "GeekyAbs/laya ≠ convaiinnovations/laya" not in UNIQ_0445:
        failed.append("UNIQ_0445 missing GeekyAbs/laya ≠ convaiinnovations/laya")
    if "densify §115 not a sibling first sighting" not in UNIQ_0445:
        failed.append("UNIQ_0445 missing NanoJev densify §115 lock")
    if "densify §45 not a sibling first sighting" not in UNIQ_0551:
        failed.append("UNIQ_0551 missing kev densify §45 lock")
    if "densify §35 not a sibling first sighting" not in UNIQ_0551:
        failed.append("UNIQ_0551 missing Nimble densify §35 lock")
    if "AbdelStark/awesome-typesafe-jev IS AbdelStark/awesome-typesafe (same GitHub id 1374058281)" not in UNIQ_0551:
        failed.append("UNIQ_0551 missing awesome-typesafe-jev same-id lock")
    if "Night-2 sign-off" not in UNIQ_0551:
        failed.append("UNIQ_0551 missing Night-2 sign-off")
    if "densify §141 not a sibling first sighting" not in UNIQ_0707:
        failed.append("UNIQ_0707 missing AbdelStark densify §141 lock")
    if "densify §107/§125 remainder" not in UNIQ_0707:
        failed.append("UNIQ_0707 missing jev-bench densify §107/§125 lock")
    if "densify §134 not a sibling first sighting" not in UNIQ_0707:
        failed.append("UNIQ_0707 missing metask densify §134 lock")
    if "只传文字，不传截图" not in UNIQ_0707:
        failed.append("UNIQ_0707 missing Jev-cu text-only lock")
    if "A completed booking is not demonstrated" not in UNIQ_0707:
        failed.append("UNIQ_0707 missing mobile-jev booking lock")
    if "ENEM 2025 *theirs* not Harbor" not in UNIQ_0707:
        failed.append("UNIQ_0707 missing ENEM *theirs* lock")
    if "#65" not in UNIQ_0707:
        failed.append("UNIQ_0707 missing HARD RULE #65")
    if "densify §137 not a sibling first sighting" not in UNIQ_0823:
        failed.append("UNIQ_0823 missing dohnuts densify §137 lock")
    if "same-species serving not an 18th scoring row" not in UNIQ_0823:
        failed.append("UNIQ_0823 missing same-species serving lock")
    if "field→value match among supplied options not free text" not in UNIQ_0823:
        failed.append("UNIQ_0823 missing FluidUse field→value lock")
    if "#66" not in UNIQ_0823:
        failed.append("UNIQ_0823 missing HARD RULE #66")
    if "densify §121 not a sibling first sighting" not in UNIQ_0923:
        failed.append("UNIQ_0923 missing patdown densify §121 lock")
    if "retired name reservation is not a replica" not in UNIQ_0923:
        failed.append("UNIQ_0923 missing retired-name lock")
    if "GLiNER OSINT" not in UNIQ_0923:
        failed.append("UNIQ_0923 missing intellyweave GLiNER OSINT lock")
    if "finite choices + none" not in UNIQ_0923:
        failed.append("UNIQ_0923 missing openvons finite-choice lock")
    if "#67" not in UNIQ_0923:
        failed.append("UNIQ_0923 missing HARD RULE #67")
    if "schema-valid is not the same as correct" not in UNIQ_1019:
        failed.append("UNIQ_1019 missing schema-valid lock")
    if "API confidence is not P(correct)" not in UNIQ_1019:
        failed.append("UNIQ_1019 missing confidence lock")
    if "review-queue policy is not F1" not in UNIQ_1019:
        failed.append("UNIQ_1019 missing review-queue lock")
    if "Not an 18th scoring-table species" not in UNIQ_1019:
        failed.append("UNIQ_1019 missing 18th scoring-table lock")
    if "densify §144 not a sibling first sighting" not in UNIQ_1019:
        failed.append("UNIQ_1019 missing jev-jarvis densify §144 lock")
    if "pi-jev-context densify §134 not a sibling first sighting" not in UNIQ_1019:
        failed.append("UNIQ_1019 missing pi-jev-context densify lock")
    if "#68" not in UNIQ_1019:
        failed.append("UNIQ_1019 missing HARD RULE #68")
    if "#69" not in UNIQ_1019:
        failed.append("UNIQ_1019 missing HARD RULE #69")
    for rel in REVISIT_OVERLAYS:
        path = ROOT / rel
        if not path.is_file():
            failed.append(f"missing revisit overlay {rel}")
            continue
        body = path.read_text(encoding="utf-8")
        if REVISIT_LOCK not in body:
            failed.append(f"revisit lock missing as one substring: {rel}")
    notes = (ROOT / "research/notes.md").read_text(encoding="utf-8")
    if "## 114. Hourly 0843 HIGH" not in notes:
        failed.append("notes.md missing §114 heading")
    if "## 115. User-provided HIGH — TianyuCodings/NanoJev" not in notes:
        failed.append("notes.md missing merged #36 §115 heading")
    if "## 116. User-provided HIGH — NiazMorshed2007/jcr" not in notes:
        failed.append("notes.md missing merged #38 §116 heading")
    if "## 117. User-provided HIGH" not in notes:
        failed.append("notes.md missing merged #37 §117 heading")
    if "## 118. User-provided HIGH — alexwestco/llm-to-jev" not in notes:
        failed.append("notes.md missing §118 heading")
    if "## 119. Hourly 0947 HIGH" not in notes:
        failed.append("notes.md missing §119 heading")
    if "## 120. Hourly 1049 HIGH" not in notes:
        failed.append("notes.md missing §120 heading")
    if "## 121. Hourly 1143 HIGH" not in notes:
        failed.append("notes.md missing §121 heading")
    if "## 122. Revisit / since-last-look" not in notes:
        failed.append("notes.md missing §122 heading")
    if "## 123. Hourly 1248 HIGH" not in notes:
        failed.append("notes.md missing §123 heading")
    if "## 124. Hourly 1340 HIGH" not in notes:
        failed.append("notes.md missing §124 heading")
    if "## 125. Hourly 1441 HIGH" not in notes:
        failed.append("notes.md missing §125 heading")
    if "## 126. Hourly 1542 HIGH" not in notes:
        failed.append("notes.md missing §126 heading")
    if "## 127. Hourly 1643 HIGH" not in notes:
        failed.append("notes.md missing §127 heading")
    if "## 128. Hourly 1746 HIGH" not in notes:
        failed.append("notes.md missing §128 heading")
    if "## 129. Hourly 1843 HIGH" not in notes:
        failed.append("notes.md missing §129 heading")
    if "## 130. User-provided HIGH" not in notes:
        failed.append("notes.md missing §130 heading")
    if "## 131. Hourly 1946 HIGH" not in notes:
        failed.append("notes.md missing §131 heading")
    if "## 132. Hourly 2049 HIGH" not in notes:
        failed.append("notes.md missing §132 heading")
    if "## 133. Hourly 2146 HIGH" not in notes:
        failed.append("notes.md missing §133 heading")
    if "## 134. Hourly 2246 HIGH" not in notes:
        failed.append("notes.md missing §134 heading")
    if "## 135. Hourly 2347 HIGH" not in notes:
        failed.append("notes.md missing §135 heading")
    if "## 136. Hourly 0049 HIGH" not in notes:
        failed.append("notes.md missing §136 heading")
    if "## 137. Hourly 0151 HIGH" not in notes:
        failed.append("notes.md missing §137 heading")
    if "## 138. Hourly 0248 HIGH" not in notes:
        failed.append("notes.md missing §138 heading")
    if "## 139. Hourly 0348 HIGH" not in notes:
        failed.append("notes.md missing §139 heading")
    if "## 140. Hourly 0445 HIGH" not in notes:
        failed.append("notes.md missing §140 heading")
    if "## 141. Hourly 0551 HIGH" not in notes:
        failed.append("notes.md missing §141 heading")
    if "## 142. Hourly 0707 HIGH" not in notes:
        failed.append("notes.md missing §142 heading")
    if "## 143. Hourly 0823 HIGH" not in notes:
        failed.append("notes.md missing §143 heading")
    if "## 144. Hourly 0923 HIGH" not in notes:
        failed.append("notes.md missing §144 heading")
    if "## 145. Hourly 1019 HIGH" not in notes:
        failed.append("notes.md missing §145 heading")

    notes140 = notes[notes.find("## 140. Hourly 0445 HIGH"):]
    for remainder_id in (
        "qingshungLI/everything-about-jev",
        "ryanzen9/XFlow",
        "Akhila14/jev-traffic-simulator",
        "ChuckNomis/linkedin-post-filtering-jev",
        "DanielJD1216/magic-computer-use",
        "Keitark/jev-cats-and-dogs",
        "OriginalByteMe/system-one-chess-arena",
        "Tsagaanbayr1/jev-tetris",
        "Zafer-Liu/jev-xiangqi",
        "agrogov/jev-system-one-study",
        "emtay-com/fastlaya",
        "fajarhide/askgrep",
        "igrejaborabora/lus222-jev-challenge",
        "kofujimura/jev-obniz-led",
        "korallis/KorWF-Pi",
        "martijnd/jev-checkers-demo",
        "neo4j-field/jev-graphrag",
        "tikeda/jev-ux-ui-reference",
        "toreleon/JevGames",
        "umgbhalla/jevx",
        "wizicer/jev_info_site",
    ):
        if remainder_id not in notes140:
            failed.append(f"notes.md §140 missing remainder card {remainder_id}")
    notes141 = notes[notes.find("## 141. Hourly 0551 HIGH"):]
    for remainder_id in (
        "Finderchangchang/jev-chat-JARVIS",
        "carlosedm10/agi-jev-containment",
        "0x7067/jev-browse",
        "sumleo/prompt2jev",
        "stacklok/typesafe-go",
        "sontakey/awesome-jev",
        "mattt/AnyDecisionModel",
        "kylemclaren/jevsearch",
        "jiawei686/jev-screen-mcp",
        "igloomatics/jev-ai-detector",
        "alperenerol/jev-1.13-mini-benchmark",
        "KranzL/Jevflake",
        "yzyialy/crush-monitor",
        "trifleen/jev-vs-luna-phishing",
        "slatinwine/jevy",
        "Giustino98/system-one-bench",
        "Autometrixai/jev-clinic-triage-eval",
        "Waxmell114514/awesome-jev-compaction",
        "PhilPentatonic/hermes-model-routing",
        "Dearest/plotveil",
        "DDnim/jev-vs-laya",
        "MudraID/mudraid-adapter-node",
    ):
        if remainder_id not in notes141:
            failed.append(f"notes.md §141 missing remainder card {remainder_id}")
    notes142 = notes[notes.find("## 142. Hourly 0707 HIGH"):]
    for remainder_id in (
        "compozy/yoshi",
        "jomatsu/pi-jev-auto-mode",
        "sorrycc/typesafe-snake",
        "rhighs/jev-code",
        "smkrv/jev-calibrate",
        "iammrduncan/typesafe-ai-benchmark",
        "SAGAR-TAMANG/sarvam-jev",
        "GhalebDweikat/winnow",
        "IAmUnbounded/save-token-jev-clean",
        "pithings/advocaat",
        "mrnugget/jev-shell-history",
        "giuliosmall/pg_typesafe",
        "trungdq88/youtube-sponsor-detection",
        "w3cj/jev-chat",
        "Ying-Kai-Liao/jev-browser",
        "realZachi/typesafe-adblock",
        "snellingio/system-one",
        "pythongiant/laya-drift",
        "seanthomasevans/typesafe-nes",
        "stoleas/typesafe-computer-use",
        "FelineStateMachine/typesafe-go",
        "patryckalves/jev-no-enem",
    ):
        if remainder_id not in notes142:
            failed.append(f"notes.md §142 missing remainder card {remainder_id}")
    notes143 = notes[notes.find("## 143. Hourly 0823 HIGH"):]
    for remainder_id in (
        "shhivv/third-hand",
        "typesafe-ai/system-one-adapter-python",
        "typesafe-ai/typesafe-sdk-js",
        "typesafe-ai/typesafe-sdk-python",
        "r-ms/mini-jev",
        "Das-rebel/a3m-router",
        "AbdelStark/jev-benchmarks",
        "FluidInference/FluidUse",
        "PsiACE/dohnuts",
        "BlinkWrite/pii-masker",
        "pythongiant/laya-drift",
        "browser-use/jev-ultrafast",
        "typesafeainate/dspy-typesafeify",
        "rorshopping/jev-on-a-laptop",
        "TypeSafeAI/typesafe-playground",
        "Twister915/typesafe-ai",
        "siliconkernel/vllm-jev-decison",
        "wmoto-ai/local-decision-playground",
        "Stumble/jev-go",
        "nickthompson480/typesafe-ai-playground",
        "arczhi/jet",
        "djhoomin/local-system-one",
        "Abhi001vj/system-one-open",
        "JabbaKadabra/SystemOneDotNet",
        "ZulfiFazhar/system-one",
        "fathiyul/system-one-exploration",
        "raaulc/jev-projects",
        "mjdileep/OpenJev",
        "hf:SargeDev/jev-distill-corpus-v3",
        "hf:aungthuhein-dev/laya-burmese-sib200",
        "Futureppo/typesafe_register",
    ):
        if remainder_id not in notes143:
            failed.append(f"notes.md §143 missing remainder card {remainder_id}")
    notes144 = notes[notes.find("## 144. Hourly 0923 HIGH"):]
    for remainder_id in (
        "vericle/intellyweave",
        "genai-craft/openvons",
        "whyashthakker/beam-cli",
        "atharvamhaske/typesafe-sdk-go",
        "Prophetlab/JevPokerBench",
        "tyler-dot-earth/patdown",
        "evoke-build/evoke",
        "lukstei/slop-grader",
        "sumleo/prompt2jev",
        "Andymulb/jev_the_philosopher",
        "PerryLink/layacore",
        "PerryLink/layacore-mcp",
        "PerryLink/laya-mcp-npm",
        "DreamBlooms/dohnuts.cpp",
        "ClemensSchartmueller/jev-guard",
        "AABBAASS1/jev-router",
        "gnapse/jev-cli",
        "hf:Skylarcc/Laya-Online",
        "hf:piratehack009/laya-cn-flash-triage",
        "kataras/jev",
        "Li-Evan/awesome-jev",
        "jev-jarvis/jev-jarvis",
        "Alistair77/openjev",
        "inematds/laya",
        "ai-ecoverse/kev.js",
        "HQarroum/laymbda",
        "hemanth/jev-chess",
        "unownone/jevsume",
        "stas4000/jev-papers",
        "lBroth/nullpii",
        "wustep/jev-playground",
        "Renwang-Huang/typesafe-mcp",
    ):
        if remainder_id not in notes144:
            failed.append(f"notes.md §144 missing remainder card {remainder_id}")
    notes145 = notes[notes.find("## 145. Hourly 1019 HIGH"):]
    for remainder_id in (
        'praneeth16/adapting-jev-with-gepa',
        'aliaihub/awesome-jev-usecases',
        'rezoch340/jev-chat-JARVIS-windows',
        'iamvatsalpatel/tiershift',
        'Bring-AI/jev-rl',
        'daniel4x/JevEmon',
        'spoonnotfound/soupbase',
        'Nabsku/pi-follow-through',
        'dashbi1/jev-sim',
        'newuser7171/jev-gamepilot',
        'sungatetop/Jev-robot',
        '007M7/jev-chat',
        'Adkid-Zephyr/chinese-workflow-decision-bench',
        'Ahmadnmic/autocorrecter',
        'Anmol-Srv/jev-video-search',
        'Anson-gzy/jev-paste',
        'AnyEvalOrg/eval-jevbench',
        'AravDharnikota/apush-debate-jev',
        'BrunoAccorsi/reflex-lab',
        'DanielTea/screenquest',
        'DeadPackets/UnitedStatesOfJev',
        'F0Rextasy/omp-marketplace',
        'FavianDT/layanan-fakultas-v1.0',
        'Kelwing/laya-candle',
        'Kourin1996/jev-playground',
        'LuisSleepy/layag-cms-auth',
        'Madikhan33/jev_codex',
        'NoNFake/job-classifier-search',
        'ShiqinGuo/jev4jobhunter',
        'TakumiNoguchi2004/jev-noul-vs-choice',
        'TerryAragorn/aliexpress-selection-first-principles',
        'Unnati-23/jev-typesafe-guide',
        'Uri-cyber/typesafe-agent',
        'XMoyas/web_attack_detection_jev',
        'YiLight0/paperfocus',
        'Yushenggg/zero-shot-classifier',
        'aakgna/jevcal',
        'aaronmeis/learn-jev',
        'adams100111/typesafe-php',
        'ai-ecoverse/cua-s1.js',
        'ak--47/ak-jev',
        'alexhawat/judge-jev',
        'alperiox/audio-jevlike',
        'antoniofaical/digital-twin-classifier-jev',
        'arnavm-codes/JevFence',
        'balazsorban44/nvim-jev-plugin',
        'cappuch/openjev.cpp',
        'chrismathew3/fast-jev-codex',
        'colbyford/jev-binder-classification',
        'cyyeh/laya-demo',
        'diluteoxygen/JevPalette',
        'fstandhartinger/decision-desk',
        'fstandhartinger/jev-router',
        'gbesse/jev-bluffcall',
        'gbesse/jev-brandsafety',
        'gbesse/jev-cardgen',
        'gbesse/jev-columns',
        'gbesse/jev-contract-graph',
        'gbesse/jev-crowdsim',
        'gbesse/jev-duelarena',
        'gbesse/jev-exposure-radar',
        'gbesse/jev-extract',
        'gbesse/jev-fingerprint',
        'gbesse/jev-label',
        'gbesse/jev-meetingpulse',
        'gbesse/jev-pairs',
        'gbesse/jev-pii',
        'gbesse/jev-proxy',
        'gbesse/jev-regwatch',
        'gbesse/jev-roast',
        'gbesse/jev-tar',
        'gbesse/jev-timemachine',
        'gbesse/jev-trace',
        'gbesse/jev-utility',
        'gexiuzhen-sketch/jev-chinese-console',
        'gradient30/typesafe-handbook',
        'heliowap/delegador',
        'hf:chanoian/openjev-mlx-demo',
        'hf:clduab11/jev-calibration-statistics',
        'hf:ldov/openjevv',
        'hf:litert-community/Laya-Multilingual-LiteRT',
        'hf:yasserrmd/laya-lab',
        'instax-dutta/sysone-bench',
        'jacopopper/jev-red',
        'leonezhu/agent-kits',
        'liudejua27-blip/jev-huamn',
        'louispaulet/jev-playground',
        'nevzataksoy/jev-trader-bybit',
        'ojusave/beat-jev',
        'patelkrish-27/layaApi',
        'pedro-pscunha/guideme-rust',
        'prakash7474/Jev_guard',
        'pstong216/jevnav-demo',
        'rdutra/laya-mcp',
        'riku1128-tong/jev_test_action',
        'roisol144/before-you-send',
        'royalpinto007/jev-msw',
        'sk123qaq/hermes-plugin-jev-approval',
        'slatejack/jev-desktop',
        'steve8708/jev-browser-benchmark',
        'taupirho/jev-test',
        'tfolkman/jev-village',
        'thehan-co/jevriel',
        'tinystruct/tinystruct-typesafe-sdk',
        'tobalo/jev-demo-sample',
        'turenlabs/jast',
        'vittoriobrehautduran/decisionmakertest',
        'who/naming-things',
        'wjw66/deepseek-harness-jev-pre-compaction',
        'xiaoMingChina/jevcn',
        'xygamer179-boop/Veylon-RLCD-Small-Conditional-Model',
        'yubol-bobo/rlcd-survey',
        'zchee/typesafe-sdk-rust',
        'ziwon/jev-actor',
        'ziwon/jev-iab-explorer',
        'jev-jarvis/jev-jarvis',
        'Nyarlathoteppppp/pi-jev-context',
        'fly88oj/jebii',
        'generallymatthew/factlabel',
    ):
        if remainder_id not in notes145:
            failed.append(f"notes.md §145 missing remainder card {remainder_id}")
    algebra = (ROOT / ".agents/skills/augustus/references/composition-algebra.md").read_text(
        encoding="utf-8"
    )
    for n in list(range(289, 317)) + list(range(322, 330)) + list(range(330, 337)) + list(range(337, 353)) + list(range(353, 369)) + list(range(369, 385)) + list(range(385, 401)) + list(range(401, 417)) + list(range(417, 433)) + list(range(433, 449)) + list(range(449, 465)) + list(range(465, 481)) + list(range(481, 497)) + list(range(497, 505)) + list(range(505, 521)) + list(range(521, 537)) + list(range(537, 553)) + list(range(553, 569)) + list(range(569, 585)) + list(range(585, 601)) + list(range(601, 617)) + list(range(617, 633)) + list(range(633, 649)) + list(range(649, 665)) + list(range(665, 681)) + list(range(681, 697)) + list(range(697, 713)) + list(range(713, 729)) + list(range(729, 745)):
        needle = f"{n}. **"
        if needle not in algebra:
            failed.append(f"composition-algebra missing item {n}")
    for n in range(317, 322):
        needle = f"{n}. **"
        if needle in algebra:
            failed.append(f"composition-algebra stole unused item {n}")
    findings = (ROOT / "research/archive/findings.md").read_text(encoding="utf-8")
    for batch in (
        "## Batch #97",
        "## Batch #98",
        "## Batch #99",
        "## Batch #100",
        "## Batch #101",
        "## Batch #102",
        "## Batch #103",
        "## Batch #104",
        "## Batch #105",
        "## Batch #106",
        "## Batch #107",
        "## Batch #108",
        "## Batch #109",
        "## Batch #110",
        "## Batch #111",
        "## Batch #112",
        "## Batch #113",
        "## Batch #114",
        "## Batch #115",
        "## Batch #116",
        "## Batch #117",
        "## Batch #118",
        "## Batch #119",
        "## Batch #120",
        "## Batch #121",
        "## Batch #122",
        "## Batch #123",
        "## Batch #124",
        "## Batch #125",
        "## Batch #126",
        "## Batch #127",
    ):
        if batch not in findings:
            failed.append(f"findings.md missing {batch}")
    digest_path_2146 = ROOT / "research/archive/hourly/2026-09-21T03/run_digest.json"
    if not digest_path_2146.is_file():
        failed.append("missing 2146 run_digest.json")
    else:
        digest2146 = json.loads(digest_path_2146.read_text(encoding="utf-8"))
        if digest2146.get("label") != "2146":
            failed.append(f"2146 run_digest label {digest2146.get('label')!r} != '2146'")
        if digest2146.get("notes_section") != "133":
            failed.append(
                f"2146 run_digest notes_section {digest2146.get('notes_section')!r} != '133'"
            )
        if digest2146.get("composition") != "537-552":
            failed.append(
                f"2146 run_digest composition {digest2146.get('composition')!r} != '537-552'"
            )
        if digest2146.get("findings_batch") != 115:
            failed.append(
                f"2146 run_digest findings_batch {digest2146.get('findings_batch')!r} != 115"
            )
        if digest2146.get("invented_signal") is not False:
            failed.append("2146 run_digest invented_signal is not false")
    digest_path_2246 = ROOT / "research/archive/hourly/2026-09-21T04/run_digest.json"
    if not digest_path_2246.is_file():
        failed.append("missing 2246 run_digest.json")
    else:
        digest2246 = json.loads(digest_path_2246.read_text(encoding="utf-8"))
        if digest2246.get("label") != "2246":
            failed.append(f"2246 run_digest label {digest2246.get('label')!r} != '2246'")
        if digest2246.get("notes_section") != "134":
            failed.append(
                f"2246 run_digest notes_section {digest2246.get('notes_section')!r} != '134'"
            )
        if digest2246.get("composition") != "553-568":
            failed.append(
                f"2246 run_digest composition {digest2246.get('composition')!r} != '553-568'"
            )
        if digest2246.get("findings_batch") != 116:
            failed.append(
                f"2246 run_digest findings_batch {digest2246.get('findings_batch')!r} != 116"
            )
        if digest2246.get("invented_signal") is not False:
            failed.append("2246 run_digest invented_signal is not false")
    digest_path_2347 = ROOT / "research/archive/hourly/2026-09-21T05/run_digest.json"
    if not digest_path_2347.is_file():
        failed.append("missing 2347 run_digest.json")
    else:
        digest2347 = json.loads(digest_path_2347.read_text(encoding="utf-8"))
        if digest2347.get("label") != "2347":
            failed.append(f"2347 run_digest label {digest2347.get('label')!r} != '2347'")
        if digest2347.get("notes_section") != "135":
            failed.append(
                f"2347 run_digest notes_section {digest2347.get('notes_section')!r} != '135'"
            )
        if digest2347.get("composition") != "569-584":
            failed.append(
                f"2347 run_digest composition {digest2347.get('composition')!r} != '569-584'"
            )
        if digest2347.get("findings_batch") != 117:
            failed.append(
                f"2347 run_digest findings_batch {digest2347.get('findings_batch')!r} != 117"
            )
        if digest2347.get("invented_signal") is not False:
            failed.append("2347 run_digest invented_signal is not false")
    digest_path_0248 = ROOT / "research/archive/hourly/2026-09-21T09/run_digest.json"
    if not digest_path_0248.is_file():
        failed.append("missing 0248 run_digest.json")
    else:
        digest0248 = json.loads(digest_path_0248.read_text(encoding="utf-8"))
        if digest0248.get("label") != "0248":
            failed.append(f"0248 run_digest label {digest0248.get('label')!r} != '0248'")
        if digest0248.get("notes_section") != "138":
            failed.append(
                f"0248 run_digest notes_section {digest0248.get('notes_section')!r} != '138'"
            )
        if digest0248.get("composition") != "617-632":
            failed.append(
                f"0248 run_digest composition {digest0248.get('composition')!r} != '617-632'"
            )
        if digest0248.get("findings_batch") != 120:
            failed.append(
                f"0248 run_digest findings_batch {digest0248.get('findings_batch')!r} != 120"
            )
        if digest0248.get("invented_signal") is not False:
            failed.append("0248 run_digest invented_signal is not false")
    digest_path_0348 = ROOT / "research/archive/hourly/2026-09-21T10/run_digest.json"
    if not digest_path_0348.is_file():
        failed.append("missing 0348 run_digest.json")
    else:
        digest0348 = json.loads(digest_path_0348.read_text(encoding="utf-8"))
        if digest0348.get("label") != "0348":
            failed.append(f"0348 run_digest label {digest0348.get('label')!r} != '0348'")
        if digest0348.get("notes_section") != "139":
            failed.append(
                f"0348 run_digest notes_section {digest0348.get('notes_section')!r} != '139'"
            )
        if digest0348.get("composition") != "633-648":
            failed.append(
                f"0348 run_digest composition {digest0348.get('composition')!r} != '633-648'"
            )
        if digest0348.get("findings_batch") != 121:
            failed.append(
                f"0348 run_digest findings_batch {digest0348.get('findings_batch')!r} != 121"
            )
        if digest0348.get("invented_signal") is not False:
            failed.append("0348 run_digest invented_signal is not false")
    digest_path_0445 = ROOT / "research/archive/hourly/2026-09-21T11/run_digest.json"
    if not digest_path_0445.is_file():
        failed.append("missing 0445 run_digest.json")
    else:
        digest0445 = json.loads(digest_path_0445.read_text(encoding="utf-8"))
        if digest0445.get("label") != "0445":
            failed.append(f"0445 run_digest label {digest0445.get('label')!r} != '0445'")
        if digest0445.get("notes_section") != "140":
            failed.append(
                f"0445 run_digest notes_section {digest0445.get('notes_section')!r} != '140'"
            )
        if digest0445.get("composition") != "649-664":
            failed.append(
                f"0445 run_digest composition {digest0445.get('composition')!r} != '649-664'"
            )
        if digest0445.get("findings_batch") != 122:
            failed.append(
                f"0445 run_digest findings_batch {digest0445.get('findings_batch')!r} != 122"
            )
        if digest0445.get("invented_signal") is not False:
            failed.append("0445 run_digest invented_signal is not false")
    digest_path_0551 = ROOT / "research/archive/hourly/2026-09-21T12/run_digest.json"
    if not digest_path_0551.is_file():
        failed.append("missing 0551 run_digest.json")
    else:
        digest0551 = json.loads(digest_path_0551.read_text(encoding="utf-8"))
        if digest0551.get("label") != "0551":
            failed.append(f"0551 run_digest label {digest0551.get('label')!r} != '0551'")
        if digest0551.get("notes_section") != "141":
            failed.append(
                f"0551 run_digest notes_section {digest0551.get('notes_section')!r} != '141'"
            )
        if digest0551.get("composition") != "665-680":
            failed.append(
                f"0551 run_digest composition {digest0551.get('composition')!r} != '665-680'"
            )
        if digest0551.get("findings_batch") != 123:
            failed.append(
                f"0551 run_digest findings_batch {digest0551.get('findings_batch')!r} != 123"
            )
        if digest0551.get("invented_signal") is not False:
            failed.append("0551 run_digest invented_signal is not false")
    digest_path_0707 = ROOT / "research/archive/hourly/2026-09-21T13/run_digest.json"
    if not digest_path_0707.is_file():
        failed.append("missing 0707 run_digest.json")
    else:
        digest0707 = json.loads(digest_path_0707.read_text(encoding="utf-8"))
        if digest0707.get("label") != "0707":
            failed.append(f"0707 run_digest label {digest0707.get('label')!r} != '0707'")
        if digest0707.get("notes_section") != "142":
            failed.append(
                f"0707 run_digest notes_section {digest0707.get('notes_section')!r} != '142'"
            )
        if digest0707.get("composition") != "681-696":
            failed.append(
                f"0707 run_digest composition {digest0707.get('composition')!r} != '681-696'"
            )
        if digest0707.get("findings_batch") != 124:
            failed.append(
                f"0707 run_digest findings_batch {digest0707.get('findings_batch')!r} != 124"
            )
        if digest0707.get("invented_signal") is not False:
            failed.append("0707 run_digest invented_signal is not false")
    digest_path_0823 = ROOT / "research/archive/hourly/2026-09-21T14/run_digest.json"
    if not digest_path_0823.is_file():
        failed.append("missing 0823 run_digest.json")
    else:
        digest0823 = json.loads(digest_path_0823.read_text(encoding="utf-8"))
        if digest0823.get("label") != "0823":
            failed.append(f"0823 run_digest label {digest0823.get('label')!r} != '0823'")
        if digest0823.get("notes_section") != "143":
            failed.append(
                f"0823 run_digest notes_section {digest0823.get('notes_section')!r} != '143'"
            )
        if digest0823.get("composition") != "697-712":
            failed.append(
                f"0823 run_digest composition {digest0823.get('composition')!r} != '697-712'"
            )
        if digest0823.get("findings_batch") != 125:
            failed.append(
                f"0823 run_digest findings_batch {digest0823.get('findings_batch')!r} != 125"
            )
        if digest0823.get("invented_signal") is not False:
            failed.append("0823 run_digest invented_signal is not false")
    digest_path_0923 = ROOT / "research/archive/hourly/2026-09-21T15/run_digest.json"
    if not digest_path_0923.is_file():
        failed.append("missing 0923 run_digest.json")
    else:
        digest0923 = json.loads(digest_path_0923.read_text(encoding="utf-8"))
        if digest0923.get("label") != "0923":
            failed.append(f"0923 run_digest label {digest0923.get('label')!r} != '0923'")
        if digest0923.get("notes_section") != "144":
            failed.append(
                f"0923 run_digest notes_section {digest0923.get('notes_section')!r} != '144'"
            )
        if digest0923.get("composition") != "713-728":
            failed.append(
                f"0923 run_digest composition {digest0923.get('composition')!r} != '713-728'"
            )
        if digest0923.get("findings_batch") != 126:
            failed.append(
                f"0923 run_digest findings_batch {digest0923.get('findings_batch')!r} != 126"
            )
        if digest0923.get("invented_signal") is not False:
            failed.append("0923 run_digest invented_signal is not false")
    digest_path_1019 = ROOT / "research/archive/hourly/2026-09-21T16/run_digest.json"
    if not digest_path_1019.is_file():
        failed.append("missing 1019 run_digest.json")
    else:
        digest1019 = json.loads(digest_path_1019.read_text(encoding="utf-8"))
        if digest1019.get("label") != "1019":
            failed.append(f"1019 run_digest label {digest1019.get('label')!r} != '1019'")
        if digest1019.get("notes_section") != "145":
            failed.append(
                f"1019 run_digest notes_section {digest1019.get('notes_section')!r} != '145'"
            )
        if digest1019.get("composition") != "729-744":
            failed.append(
                f"1019 run_digest composition {digest1019.get('composition')!r} != '729-744'"
            )
        if digest1019.get("findings_batch") != 127:
            failed.append(
                f"1019 run_digest findings_batch {digest1019.get('findings_batch')!r} != 127"
            )
        if digest1019.get("invented_signal") is not False:
            failed.append("1019 run_digest invented_signal is not false")
    digest_path_0151 = ROOT / "research/archive/hourly/2026-09-21T08/run_digest.json"
    if not digest_path_0151.is_file():
        failed.append("missing 0151 run_digest.json")
    else:
        digest0151 = json.loads(digest_path_0151.read_text(encoding="utf-8"))
        if digest0151.get("label") != "0151":
            failed.append(f"0151 run_digest label {digest0151.get('label')!r} != '0151'")
        if digest0151.get("notes_section") != "137":
            failed.append(
                f"0151 run_digest notes_section {digest0151.get('notes_section')!r} != '137'"
            )
        if digest0151.get("composition") != "601-616":
            failed.append(
                f"0151 run_digest composition {digest0151.get('composition')!r} != '601-616'"
            )
        if digest0151.get("findings_batch") != 119:
            failed.append(
                f"0151 run_digest findings_batch {digest0151.get('findings_batch')!r} != 119"
            )
        if digest0151.get("invented_signal") is not False:
            failed.append("0151 run_digest invented_signal is not false")
    digest_path_0049 = ROOT / "research/archive/hourly/2026-09-21T07/run_digest.json"
    if not digest_path_0049.is_file():
        failed.append("missing 0049 run_digest.json")
    else:
        digest0049 = json.loads(digest_path_0049.read_text(encoding="utf-8"))
        if digest0049.get("label") != "0049":
            failed.append(f"0049 run_digest label {digest0049.get('label')!r} != '0049'")
        if digest0049.get("notes_section") != "136":
            failed.append(
                f"0049 run_digest notes_section {digest0049.get('notes_section')!r} != '136'"
            )
        if digest0049.get("composition") != "585-600":
            failed.append(
                f"0049 run_digest composition {digest0049.get('composition')!r} != '585-600'"
            )
        if digest0049.get("findings_batch") != 118:
            failed.append(
                f"0049 run_digest findings_batch {digest0049.get('findings_batch')!r} != 118"
            )
        if digest0049.get("invented_signal") is not False:
            failed.append("0049 run_digest invented_signal is not false")
    digest_path_2049 = ROOT / "research/archive/hourly/2026-09-21T02/run_digest.json"
    if not digest_path_2049.is_file():
        failed.append("missing 2049 run_digest.json")
    else:
        digest2049 = json.loads(digest_path_2049.read_text(encoding="utf-8"))
        if digest2049.get("label") != "2049":
            failed.append(f"2049 run_digest label {digest2049.get('label')!r} != '2049'")
        if digest2049.get("notes_section") != "132":
            failed.append(
                f"2049 run_digest notes_section {digest2049.get('notes_section')!r} != '132'"
            )
        if digest2049.get("composition") != "521-536":
            failed.append(
                f"2049 run_digest composition {digest2049.get('composition')!r} != '521-536'"
            )
        if digest2049.get("findings_batch") != 114:
            failed.append(
                f"2049 run_digest findings_batch {digest2049.get('findings_batch')!r} != 114"
            )
        if digest2049.get("invented_signal") is not False:
            failed.append("2049 run_digest invented_signal is not false")
    digest_path = ROOT / "research/archive/hourly/2026-09-21T00/run_digest.json"
    digest_path_1946 = ROOT / "research/archive/hourly/2026-09-21T01/run_digest.json"
    if not digest_path_1946.is_file():
        failed.append("missing 1946 run_digest.json")
    else:
        digest1946 = json.loads(digest_path_1946.read_text(encoding="utf-8"))
        if digest1946.get("label") != "1946":
            failed.append(f"1946 run_digest label {digest1946.get('label')!r} != '1946'")
        if digest1946.get("notes_section") != "131":
            failed.append(
                f"1946 run_digest notes_section {digest1946.get('notes_section')!r} != '131'"
            )
        if digest1946.get("composition") != "505-520":
            failed.append(
                f"1946 run_digest composition {digest1946.get('composition')!r} != '505-520'"
            )
        if digest1946.get("findings_batch") != 113:
            failed.append(
                f"1946 run_digest findings_batch {digest1946.get('findings_batch')!r} != 113"
            )
        if digest1946.get("invented_signal") is not False:
            failed.append("1946 run_digest invented_signal is not false")
    if not digest_path.is_file():
        failed.append("missing 1843 run_digest.json")
    else:
        digest = json.loads(digest_path.read_text(encoding="utf-8"))
        if digest.get("label") != "1843":
            failed.append(f"1843 run_digest label {digest.get('label')!r} != '1843'")
        if digest.get("notes_section") != "129":
            failed.append(
                f"1843 run_digest notes_section {digest.get('notes_section')!r} != '129'"
            )
        if digest.get("composition") != "481-496":
            failed.append(
                f"1843 run_digest composition {digest.get('composition')!r} != '481-496'"
            )
        if digest.get("findings_batch") != 111:
            failed.append(
                f"1843 run_digest findings_batch {digest.get('findings_batch')!r} != 111"
            )
        if digest.get("invented_signal") is not False:
            failed.append("1843 run_digest invented_signal is not false")
    skill = (ROOT / ".agents/skills/augustus/SKILL.md").read_text(encoding="utf-8")
    try:
        fm = load_skill_frontmatter(skill)
    except Exception as e:
        failed.append(f"SKILL.md yaml.safe_load: {e}")
        fm = {}
    else:
        if fm.get("name") != "augustus":
            failed.append("SKILL.md name != augustus")
        meta = fm.get("metadata") or {}
        if meta.get("version") != "0.5.1":
            failed.append(
                f"SKILL.md metadata.version {meta.get('version')!r} != '0.5.1'"
            )
        desc = fm.get("description") or ""
        if len(desc) > 1024:
            failed.append(
                f"SKILL.md description is {len(desc)} chars "
                "(registry blurb must stay under 1024; trigger wall "
                "lives in references/activation-triggers.md)"
            )
        triggers_rel = (
            ".agents/skills/augustus/references/activation-triggers.md"
        )
        triggers_path = ROOT / triggers_rel
        if not triggers_path.is_file():
            failed.append(f"missing {triggers_rel}")
            triggers = ""
        else:
            triggers = triggers_path.read_text(encoding="utf-8")
        if "references/activation-triggers.md" not in skill:
            failed.append(
                "SKILL.md must point at references/activation-triggers.md"
            )
        haystack = desc + "\n" + skill + "\n" + triggers
        for frag in (
            "A hunch is a probability with a policy attached",
            "calibration does not compose",
            "Qwen2.5 ≠ Archer",
            "Qwen/Qwen3.8-27B ≠ Archer",
            "Deferred Crispification",
            "ranking ≠ calibration",
            "g0runmezadam/what-is-jev IS tunahansahin897/what-is-jev",
            "NiazMorshed2007/jcr",
            "does not execute",
            "JCR_BAND_RATIO 0.6",
            "routing ≠ permission",
            "docs ≠ authority to run",
            "Not Harbor task-execution",
            "TianyuCodings/NanoJev",
            "SemIf was formerly OpenJev",
            "systems comparison ≠ semantic equivalence",
            "Softmax over options ≠ calibrated Noul",
            "live REST 2282★",
            "JevBench 74.6 is §78 not this ladder",
            "Turn decision-shaped LLM prompts into proposed Jev primitives",
            "conversion assistant, not an automatic guarantee of equivalent behavior",
            "heuristic conversion ≠ calibrated Noul",
            "alexwestco/llm-to-jev ≠ altryne/jevify",
            "judge ≠ actuator",
            "softmax over A–H ≠ Noul",
            "candidate_mass",
            "Qwen3.5-2B ≠ Archer",
            "Qwen3.5-4B ≠ Archer",
            "ggmlc GGUF is not llama.cpp",
            "serving substrate ≠ calibrated replica",
            "Qwen3.5-9B ≠ Archer",
            "planner writes JEV selects",
            "pick_by_id vs pick_second",
            "open recreation ≠ calibrated replica",
            "semantic lint is a sensor not a proof",
            "cutoff 0.8 still soft",
            "paired bootstrap CIs *theirs*",
            "Same accuracy, 35x faster *theirs*",
            "This is not demonstrated equal-quality savings",
            "permission ≠ confidence",
            "wire-compat ≠ replica",
            "decide is not generate",
            "tryDecide returns typed calibrated judgments not a token stream",
            "GLiNER/GLiClass ports are class members not Jev replicas",
            "93.5% *theirs* not Harbor",
            "74.9 *theirs* not Harbor",
            "8.7x *theirs* not Harbor",
            "Option-Marker joint attention",
            "openjev:0.2.1",
            "thinking=True/False per-field budget",
            "PLAN_Qwen35",
            "hyperspaceai/jevcache ≠ kushals256/jevcache",
            "wire-compat ≠ logit-equiv",
            "SHA move is not a replica",
            'typesafe-sdk 0.7 Pydantic response models',
            'msgspec dropped',
            "The server's output is unchanged and was never wrong",
            'SchemaError is 400 plain-string detail not 422 list',
            'Pydantic response models ≠ logit-equiv',
            'msgspec dropped is not a replica',
            'Error contract is not a Noul',
            'coverage-at-error-budget *theirs* not Harbor',
            'PLAN_Qwen35 still proposal for review',
            'GLiNER locate ports are class members not Jev replicas',
            'Locate ≠ decide',
            '~160 ms *theirs* not Harbor',
            '0.971 F1 *theirs* not Harbor',
            'hf:fr0stbit3/laya-gguf serving substrate ≠ calibrated replica',
            'jkcdarunday/SystemOne-Next ≠ TypeSafe System One',
            'vLLM NVIDIA + MLX Apple Silicon',
            'Codiv hosted free endpoint',
            'dual /v1/systemone + /v1/chat/completions',
            'chat 501 on MLX',
            'dual serving is not generate',
            'Hosted Codiv ≠ TypeSafe',
            'hr98w/jev-visual 167★ Apple Silicon visual candidate scoring',
            '37.30s → 2.40s at 64 decisions *theirs*',
            'Breakout 9 bricks 6 returns 2 lives *theirs*',
            'candidate probabilities are relative not correctness',
            'jkudish/jev-mcp 156★ ten MCP tools',
            'recommendation is advisory',
            'the server never blocks on its own',
            'TypeSafe CLERC 5% to 18% *theirs*',
            'jkudish/jev-mcp ≠ burnigtm/jev-mcp',
            'zhengxuyu/litjev off-the-shelf Qwen decision layer',
            'Probabilities are not calibrated by default',
            'Qwen/Qwen3.8-27B ≠ Archer',
            'zhengxuyu/litjev ≠ alexwestco/llm-to-jev',
            'Zefan-Cai/Open-Jev LoRA + scalar head',
            '2B 94.71% 9B 97.54% hard test *theirs*',
            '2B OOD 86.02% 9B OOD 91.97% *theirs*',
            '80,816 training rows',
            '27B still in progress',
            'LoRA ≠ RLCD replica',
            'Zefan-Cai/Open-Jev ≠ TheoLeeCJ/openjev ≠ razorback16/openjev',
            'cristianoliveira/jeq intelligence you can pipe',
            'pass-min 0.8 still soft',
            'JEQ does not own actions',
            'AndyInQtr/laya-coreai CoreML serving substrate ≠ calibrated replica',
            'AndyInQtr/laya-coreai ≠ mizorewww/laya-coreml',
            'TypeLLM/TypeLLM densify HEAD 6a48f9f1e623',
            'README densify 3k→12k B',
            'Batch 5.8x *theirs*',
            'Constrained AR ≠ calibrated Noul',
            'jaredpalmer/kev densify HEAD b339f446a0ef',
            'Kev-0.6B 4B 8B family',
            '4B new-source 0.790/0.806 *theirs*',
            '8B new-source 0.796/0.780 *theirs*',
            'Jev hosted 0.857 *theirs*',
            'Questions share the input text but cannot read each other',
            'No Jev outputs were used for training',
            '8.2% ≥0.9 on wrong *theirs*',
            'option order can change an answer',
            'Qwen3 ≠ Archer',
            'TheoOliveira/pi-jev 21★ fail-closed routing',
            'JEV_THRESHOLD 0.65 still soft',
            'harshwasan/jev-sentinel fail closed never auto-allows',
            'harshwasan/jev-sentinel ≠ leepokai/jev-guard',
            'jackbarunz/jev-tool-router ≠ esinocchi/jev-tool-router',
            'threshold 0.90 still soft',
            '76/81 vs 77/81 *theirs*',
            '0.419s vs 2.459s *theirs*',
            '$0.00486 vs $0.03673 *theirs*',
            'not a security boundary',
            'baronunread/leanest fail-open uncertainty means RUN',
            'classifier.dev default Jev/Laya pluggable',
            'openlayer-ai/jevals ≠ dayhaysoos/jevals',
            'estimates not Harbor',
            'classifier ≠ authorizer',
            'MrJev/awesome-jev 118 entries catalog ≠ endorsement',
            'MrJev/awesome-jev ≠ yibie/awesome-jev',
            'Koushik890/jev-firewall fail closed ask_below 0.7 still soft',
            'CompleteTech-LLC-AI-Research/jev-codex-approval experimental native not compiled',
            'confidence is not a measured probability',
            'rh-guard owns primary gates',
            'hf:rAVEUK/open-jev-deberta-v3-large encoder class member not Jev replica',
            'hf:p-yan/laya-quanto serving substrate ≠ calibrated replica',
            'hf:Gtrkrsk/laya serving substrate ≠ calibrated replica',
            'hourly 1542 / notes.md §126',
            "razorback16/openjev densify HEAD febf02e88989",
            "release 0.3.0",
            "re-pin vLLM PR #57250 restructured head",
            "MODEL_VERSION stays openjev-0.1",
            "uv.lock hygiene",
            "restructured vLLM head ≠ logit-equiv",
            "frostney/clean-code-review 7★ typed judgments not opinions",
            "documentation is read not judged",
            "morcoan/JMP Joint Model Participation",
            "Models participate. Real tools execute.",
            "Thresholds are policy not model",
            "Kelbie/hunch ≠ carldaws/hunch ≠ tpellet/hunch ≠ huncho",
            "Jev never generates prose JSX or code",
            "json-render is the only renderer",
            "game success ≠ calibrated Noul",
            "Shalimov04/open-jev ≠ razorback16/openjev",
            "MstyAI/laya-onnx empty repo",
            "hf:Praveenrajus/jev-bench HTTP 200 was 401",
            "hourly 1643 / notes.md §127",
            'TypeLLM/TypeLLM densify HEAD 702e6a287f3c',
            'truncated thinking then constrained decode',
            '0.8B thinking On 0/18 *theirs*',
            'forced closure 20/20 type-valid *theirs*',
            'jaredpalmer/kev densify live HEAD 8465c4c4c294',
            'Kev-0.8B completes family',
            '4B new-source 0.794/0.832 *theirs*',
            '9B new-source 0.812/0.837 *theirs*',
            'transfer-v9 Kev-9B 5% Jev 9% Kev-8B 26% *theirs*',
            'SemIf Kev-9B 0.917 Jev 0.965 *theirs*',
            'scienthoon 0.952/0.911 vs 0.897/0.914 *theirs*',
            'transformers >= 5.17',
            'Qwen3.5 ≠ Archer',
            'notque/vexjoy-agent 421★ /d routes /do fallback',
            'Facts go to code. Judgments go to Jev. Only facts can block.',
            'Jev never blocks',
            'jqueryscript/awesome-jev ≠ MrJev/awesome-jev ≠ yibie/awesome-jev',
            'five-lines threshold 0.80 still soft',
            '371ms $0.0000189 300-call *theirs*',
            'tpellet/jevify ≠ altryne/jevify',
            'seb4ez/jevguard-mcp ≠ seb4ez/jevguard',
            'resumocast/jev-mcp ≠ jkudish/jev-mcp',
            'Adrian-Ernesto/jevsort ≠ zzzzzec/jevsort',
            'MidasMulli/kev-ane 155/155 argmax *theirs*',
            'hourly 1746 / notes.md §128',
            "jaredpalmer/kev densify HEAD bd058057ad0a",
            "Fine-tuning on your own data",
            "--data JSONL",
            "--init_from warm-start LoRA/head PR #9",
            "from-scratch ≠ warm-start",
            "JSONL labels ≠ Harbor",
            "Kev-0.8B 4B 9B Qwen3.5 family",
            "0.33 vs 0.84 vs 0.83/0.88 *theirs*",
            "Kev-0.5B card Qwen3.5 family pointer",
            "reconstruction ≠ replica",
            "unofficial research implementation with random weights",
            "assay-001 split verdict",
            "CLINC150 ECE 0.0204 *theirs*",
            "Banking77 ECE 0.0936 *theirs*",
            "8,576 responses zero type errors *theirs*",
            "brnyxx/jev-ra 3-5x / ~300 ms *theirs*",
            "8.50× Wikipedia *theirs*",
            "Promethe-us/awesome-jev ≠ MrJev/awesome-jev ≠ yibie/awesome-jev",
            "ThePFMind/jev-mcp ≠ jkudish/jev-mcp",
            "kyegomez/open-jev ≠ razorback16/openjev",
            "namenu/pi-jev-effort ≠ TheoOliveira/pi-jev",
            "samatv256/mini-Jev ≠ r-ms/mini-jev",
            "comoc/jev-minesweeper ≠ EnesYilmazcode/JevMinesweeper",
            "hf:akhilaaa3/openjev-v1-allmix-r512-merged ≠ hf:akhilaaa3/openjev-r512-handoff-demo",
            "dabit3/jev-experiments densify 340★",
            "simota/tenbin densify neighbor skill",
            'sgoedecke/system-one 20★ HEAD ebde2a2db706',
            'SystemOne.from_pretrained',
            'TypeSafe-compatible ≠ TypeSafe replica',
            'mithalouni/system-one-open 18★ MIT HEAD 77f1f7cccf8a',
            '76.7% vs Jev 86.9% strict common subset *theirs*',
            '97 ms H100 *theirs*',
            '74.8% held-out *theirs*',
            'replica ≠ TypeSafe',
            'kotoba-lang/typed-decisions 1★ Apache-2.0 HEAD 10d7834d3b99',
            'DeBERTa-v3-large 0.855 / 42 ms *theirs*',
            'ModernBERT-base 0.717 / 68 ms *theirs*',
            'LLaDA-MoE 0.835 / 676 ms *theirs*',
            'kotoba-lang/typed-decisions ≠ convaiinnovations/laya-typed-decisions',
            'aisearchio 15-link census catalog ≠ endorsement',
            '12 already carded 3 gaps this fold',
            'user-provided 1936 / notes.md §130',
            "hourly 1843 / notes.md §129",
            "Open-Jev densify HEAD 4933ee84951f",
            "Astra TREC commit 1dd56990be7e",
            "not merged base models",
            "customer-service P50 local HTTP 85.03 ms vs Jev HTTPS 295.26 ms *theirs*",
            "1024 tokens/32 candidates Open-Jev slower 1015.90 vs 301.37 *theirs*",
            "prefix caching experimental/off by default",
            "systems latency ≠ semantic equivalence",
            "GPT Luna P50 918.13 ms Astra 1938.39 ms *theirs*",
            "TREC-DL Jev/Luna/Astra completed",
            "Open-Jev TREC pending",
            "hard acc ≠ calibrated Noul",
            "densify §125 not a sibling first sighting",
            "Open-Jev densify / notes.md §125",
            "launch X thread https://x.com/Zefan_Cai/status/2101782158658695388",
            "2101786019607740436",
            "2101789698947793231",
            'platform does not execute trades',
            'heyjunpenn/awesome-jev 485 catalog ≠ endorsement',
            '62.69% vs 67.26% *theirs* not gold',
            '203.2s $0.84 vs 823.5s $1.50 *theirs*',
            'one seed-0 trial *theirs*',
            'Jev $0.018825 vs Astra $5.93 *theirs*',
            '10.59× *theirs*',
            '6 class flips',
            'agreement ≠ accuracy',
            'probabilities uncalibrated',
            'Qwen3.8 ≠ Archer',
            'Spanish −6.4 pp XNLI *theirs*',
            'ECE 0.057→0.101 *theirs*',
            '72.2% vs 63.4% p_max≥0.9 coverage *theirs*',
            'Convert LLM prompts to Jev prompts',
            'SHA unchanged 234058ab372d',
            'skip Zefan-Cai/Open-Jev densify open #53',
            'skip sgoedecke/system-one mithalouni/system-one-open kotoba-lang/typed-decisions open #54',
            'hourly 1946 / notes.md §131',
            'AI-reviewed labels ≠ gold',
            'one-trial robot ≠ Harbor',
            '10.59× systems ≠ ECE',
            'desc rewrite ≠ SHA/behavior change',
            'rule-table ≠ model',
            'local_only ≠ Jev',
            'jaredpalmer/kev densify HEAD c096660c8da2',
            'PLAN SHA 8d77dd271c66',
            'README SHA unchanged 84b872488915',
            'night-2 dates/unknowable/assertion',
            'KEV_TEMPERATURE T≈2.0',
            'Brier 0.291→0.267 ECE 0.105→0.039 *theirs*',
            '7.5%→3.2% *theirs*',
            'grouped T rejected',
            'Qwen3.6-35B-A3B smoke 0.812 *theirs*',
            '21M LoRA experts frozen',
            'Hub --revision night2-du',
            'MMLU-Pro 1000 Kev-9B 0.511 Jev 0.829 *theirs*',
            'Qwen3.6 ≠ Archer',
            'temperature scaling ≠ ECE unless measured',
            'Hub --revision is a pin not a replica',
            'kotoba-lang/typed-decisions densify HEAD ff7f84e74d04',
            'feat expose trained OpenJev decision runtime',
            'open_jev.py',
            'tests/test_open_jev.py',
            'generated_text: False',
            'trained runtime ≠ TypeSafe',
            'OpenJev.from_pretrained',
            'decide_request kind typed-decisions/open-jev-v1',
            'daftAI2026/awesome-jev ≠ heyjunpenn/awesome-jev',
            'franckverrot/lev ≠ jaredpalmer/kev',
            'neko233-com/laya-go ≠ convaiinnovations/laya',
            'tryAGI/TypeSafeAI ≠ official',
            'hourly 2049 / notes.md §132',
            'Open-Jev densify HEAD a00559ea0ab2',
            'README SHA unchanged ce1a587219e4',
            'Publish prepared Open-Jev provider quality evaluation pipeline',
            '808 requests 1841 labelled decisions per model',
            'Open-Jev GPU inference has not started',
            '48 CPU tests pass',
            'Open-Jev TREC pending',
            '65/76 72/76 66/76 60/76 71/76 *theirs*',
            'provider pipeline ≠ completed Open-Jev quality',
            'CPU tests ≠ GPU scores',
            'tinmanlab/cartpole-jev densify HEAD 922cc61490a0',
            'Active model Kev Not TypeSafe Jev',
            '81.25% 52/64 *theirs*',
            'one record of 64',
            'fine-tuned Kev ≠ TypeSafe Jev',
            'softmax ≠ calibrated Noul',
            'xuboboo/ashare-trader densify HEAD 26c7e95e6828',
            'QMT sidecar mock/dry default no orders',
            'AUC 0.532 *theirs*',
            'gauravsaini/kevin first card Playwright + Onyx',
            '3.69ms *theirs* not Harbor',
            'metask-jev-4b 79.6% / 80.1% *theirs*',
            'cutoff 95% still soft',
            'hourly 2146 / notes.md §133',
            'Open-Jev densify HEAD 48346d0630f1',
            'Publish strict Open-Jev TREC evaluation preparation and context proof',
            'Actual Open-Jev TREC model inference is pending',
            'All 79 combined CPU tests pass',
            'TREC prep ≠ completed Open-Jev TREC',
            'context proof ≠ nDCG',
            'TypeLLM/TypeLLM densify HEAD 8a8b4aefd443',
            'typellm 0.1.1',
            'PyPI packaging ≠ calibrated Noul',
            'featherless-ai/simple-jev 408★ HEAD b02aa81c915a',
            'logits are not calibrated probabilities of correctness',
            'hourly 2246 / notes.md §134',
            'Open-Jev densify HEAD 48346d0630f1',
            'Publish strict Open-Jev TREC evaluation preparation and context proof',
            'Actual Open-Jev TREC model inference is pending',
            'All 79 combined CPU tests pass',
            'TREC prep ≠ completed Open-Jev TREC',
            'context proof ≠ nDCG',
            'TypeLLM/TypeLLM densify HEAD 8a8b4aefd443',
            'typellm 0.1.1',
            'PyPI packaging ≠ calibrated Noul',
            'featherless-ai/simple-jev 408★ HEAD b02aa81c915a',
            'logits are not calibrated probabilities of correctness',
            'hourly 2246 / notes.md §134',
            'razorback16/openjev densify HEAD 2050fdb8280d',
            'MLX backend steps>1/think/text gen + image Qs',
            'GitHub Release v0.1.1',
            'README SHA unchanged 9f6dea3a4c8c',
            'zjunlp/JevLoop 6★ independent not affiliated',
            'option order 0.188 or 0.542 *theirs*',
            'n=8 is not Harbor',
            'ranking before lossless condensation',
            'hourly 2347 / notes.md §135',
            'Open-Jev densify HEAD f46ff604f794',
            'README SHA e32c4bbd519c',
            'Publish audited JevBench public-subset baselines',
            'public-subset ≠ Harbor',
            '231 ≠ 534',
            'jaredpalmer/kev densify HEAD e0bcf50153f1',
            'PLAN correct 35B MMLU-Pro (0.550)',
            'evaluate.load honour weights_dtype=bf16',
            'wy-coliney/jev-browser-use 282★',
            '5-10× *theirs* not Harbor',
            'fail-open routing ≠ permission',
            'ordered routing ≠ end-to-end',
            'softmax next-token ≠ calibrated Noul',
            'potential_match ≠ hiring decision',
            'hourly 0049 / notes.md §136',
            'Open-Jev densify HEAD ed45657bf726',
            'README SHA 12e0f581e15d',
            'Publish audited v3 community data and held-out evaluation protocol',
            'Redesign readable project site and consolidate benchmark results',
            'v3 data prepared ≠ retrained released models',
            'held-out protocol ≠ Harbor',
            '1,280-row panel ≠ Harbor',
            'finite training loss ≠ quality improvement',
            'website redesign ≠ calibration',
            '129,288 decision rows 74,921 training',
            'frozen mixture 96,849 training',
            '1,280-row / 840-group comparison panel',
            '27B step 616 pending',
            'naive throws away 83% *theirs*',
            'certo KL 0.008 acc 0.844 ECE 0.004 *theirs*',
            'first-instinct 63.3%→78.1% *theirs* not Harbor',
            '371,278 prepared ≠ consumed',
            'Jev is a gate not a generator',
            'Lake remains admission',
            'Jev never writes Lean',
            'community port ≠ TypeSafe',
            'chy4pro/jev-for-chrome ≠ browser-use/jev-ultrafast',
            'joint RLCD *theirs*',
            'Dohnuts ≠ TypeSafe',
            'Akashdb5/jev-router ≠ gargpratyush/jev-router ≠ daviddl9/jev-router',
            'kiuckhuang/laya-jev ≠ KonghaYao/laya-jev',
            'tegersdorfer-collab/jevkit ≠ isiomaC/jevkit ≠ WaynezProg/jev-kit',
            'buluoray/JevOnly already carded',
            'yottayoshida/jev-intent-review already carded',
            'skip-thin Iskandeur/system1-system2 zhlei07/open-system-one Hand-In/openjev-multimodal gwxcsny53/jev-watchtower empty SHA',
            'hourly 0151 / notes.md §137',
            'GLiClass knowledgator Hub family class-peer catalog not Jev equivalent',
            'typed-decision-leaderboard *theirs* not Harbor',
            'JEV 0.7350 ZTC 27B 0.7289',
            'Jevbridge ACP and MCP adapter',
            'Cut the slop',
            'Not a Cua binding',
            'open reproductions of the shape',
            '82.3% ECE 0.017 *theirs*',
            'tacticocc/Jevbridge 33★',
            'tshmieldev/sharp 29★',
            'wire-compat ≠ logit-equiv',
            'serving substrate ≠ calibrated replica',
            'Zaious/jev-capability-atlas already carded',
            'skip-thin Fibonaccirabbit/Jev-VLN imanshu03/jev-browser-use luca-saggese/laya.c empty SHA',
            'hourly 0248 / notes.md §138',
            'Greedy 0.90 vs Oracle 0.82 *theirs*',
            'Random conf 0.00 still 20.5% *theirs*',
            '8,400 calls $0.39 *theirs*',
            'Noul 0.7 true 44% *theirs*',
            'JevBench 81.65 *theirs* not Harbor',
            'WindTunnel 49/49 *theirs* not Harbor',
            '0-byte Mandelbrot is not a replica',
            'training not complete',
            'meijustory123/OpenJev-Kit IS meijustory123/openjev',
            'Compose meaning like state',
            'Code enumerates the candidates',
            'Jev is the first classifier the design is bound to none',
            'context is the conversation so far',
            'A clean report is not proof',
            'does not sandbox',
            'ChatJEVs ≠ erik-dunteman/ChatJev',
            'generation from Choice is not a language model replica',
            'demo scores are not accuracy measurements',
            'Qwen2.5 ≠ Archer',
            'confidence ≠ P(correct)',
            'seed 42 n=1 is not Harbor',
            'skip-thin Fibonaccirabbit/Jev-GalGame MadhavBahl/jev-guide advance-lion/dsh-jev-hooks amithgc/local-jev hiro1202/jev-review-gate-poc inlight37-design/decision-model_lab kuhung/ask-jev mmiguez314/jev-lab pomodorozhong/exp-jev vanthiet1/JevGuarAgent empty SHA',
            'hourly 0348 / notes.md §139',
            'keeps essentially every block 0.0%/−0.5% *theirs*',
            'Token reduction alone is not cost reduction',
            'Chat 1282.3 ms vs gateway 232.1 ms ~1/5.5 *theirs*',
            'acc 0.796 ECE 0.027 *theirs*',
            'How you ask mattered more',
            'Calibration is not yet measured',
            'Add JevHarness project link to READMEs',
            'densify §115 not a sibling first sighting',
            'Awesomejev 691→802',
            'tracker likes 81 lastModified UNCHANGED',
            'hf:AXERA-TECH/Laya',
            'hf:openjev/openjev-MLX-4bit ≠ razorback16/openjev',
            'GeekyAbs/laya ≠ convaiinnovations/laya',
            'Softmax over candidate logprobs',
            'skip-thin Adrian-lzr/jev-spire-brain Dililianxice/jev-robotic-arm-benchmark baltzparra/jev-study lzero07/jev-laya-statement qq150078158-lab/TDM-demo empty SHA',
            'hourly 0445 / notes.md §140',
            'not a digital twin',
            'Score fan-out ≠ chess engine',
            'Jev cannot waive a failing check',
            'umgbhalla/jevx ≠ hawkyre/jevx',
            'ryanzen9/XFlow ≠ hawkyre/jevx',
            'Tsagaanbayr1/jev-tetris ≠ planstack-ai/jev-tetris-benchmark',
            'wizicer/jev_info_site ≠ JingHao-Leon/awesome-jev-apps',
            'hourly 0551 / notes.md §141',
            'Night-2 sign-off',
            'densify §45 not a sibling first sighting',
            'densify §35 not a sibling first sighting',
            'did not distill from Jev',
            'Independent community project',
            'APUS-OpenJev 9B 85.0% vs Jev API 82.5% *theirs* not Harbor',
            'Frozen80 n=80',
            'Candidate probabilities are not calibrated confidence',
            'Jev is the first adapter the design is bound to no engine',
            'Zero Hallucinations marketing',
            'kylemclaren/jevsearch ≠ kylemclaren/jev-search',
            'stacklok/typesafe-go ≠ kisshan13/typesafe-ai-go',
            'DevMortimer/pi-typesafe ≠ twilwa/pi-typesafe',
            'hf:SeanLiu/Jev-Vision ≠ sseanliu/Jev-Vision',
            'sontakey/awesome-jev ≠ heyjunpenn/awesome-jev',
            'Giustino98/system-one-bench ≠ mallahyari/system-one-benchmark',
            'skip-thin eatmoreduck/jev-jarvis',
            'densify §139 not a sibling first sighting',
            'AbdelStark/awesome-typesafe-jev IS AbdelStark/awesome-typesafe',
            'hourly 0707 / notes.md §142',
            '只传文字，不传截图',
            'Text only no screenshots',
            '100% of our tax document corpus at $0.001 per page',
            'TaxCalcBench 0 strict errors *theirs*',
            'blank IRS 38 strict errors 5.05% *theirs*',
            '100% of corpus *theirs* not Harbor',
            'The model does not receive screenshots',
            '21 seconds for 9 actions *theirs*',
            'A completed booking is not demonstrated',
            'droidrun/mobile-jev ≠ Friedjof/jev-mobile',
            'giuliosmall/pg_typesafe ≠ realZachi/pg-jev',
            'itsmostafa/typesafe-mcp ≠ cyrusasco/typesafe-mcp ≠ burnigtm/jev-mcp',
            'The field guide to typed decisions',
            'densify §141 not a sibling first sighting',
            'hf:Praveenrajus/jev-bench HTTP 401 was 200',
            'densify §107/§125 remainder',
            'densify §134 not a sibling first sighting',
            'ENEM 2025 *theirs* not Harbor',
            'Ying-Kai-Liao/jev-browser ≠ wy-coliney/jev-browser-use',
            'w3cj/jev-chat ≠ Manta-Boardgame/jev-chat',
            'snellingio/system-one ≠ sgoedecke/system-one ≠ Luke458/system-one ≠ developerekene/System-One',
            'stoleas/typesafe-computer-use ≠ awlevin/typesafe-computer-use',
            'holotwist/laya ≠ NandhaKishorM/laya',
            'RafalWilinski/vibecheck ≠ psyb0t/vibecheck',
            'dannote/jev ≠ okooo5km/jev ≠ sebastianbugal/jev',
            'skip-thin developerekene/System-One holotwist/laya wuzhiping/jev-laya empty SHA',
            'hf:s1lv3rj1nx/openjev-healthcare-router HTTP 401 *theirs*',
            'hourly 0823 / notes.md §143',
            'JevBench 65.80% vs Jev 86.58%',
            'Laya multi 47.62%',
            'same-species serving not an 18th scoring row',
            'field→value match among supplied options not free text',
            "Screenshots aren't uploaded",
            'Jev is the only model',
            'not fully offline',
            'JSON 0.909 letters 0.907 *theirs*',
            '13 600 / 13 600 *theirs*',
            'softmax over letters ≠ calibrated Noul',
            'model=jev-auto',
            'AG News 0.910 *theirs*',
            'Banking77 0.870 *theirs*',
            'DAIR Emotion 0.480 *theirs*',
            'Fastest and cheapest web agent *theirs*',
            'densify §137 not a sibling first sighting',
            'densify description rewrite',
            'TypeSafeAI/typesafe-playground ≠ kavehmz/typesafe-playground ≠ nickthompson480/typesafe-ai-playground',
            'No generative fallback',
            'Unofficial research repo. Not affiliated with TypeSafe AI',
            'skip-thin GokhanCalkap/LayaCode fredzhaozonghui/LAYA1 empty SHA',
            'Abhi895/Laya ≠ convaiinnovations/laya',
            'mjdileep/OpenJev ≠ Zefan-Cai/Open-Jev',
            'Abhi001vj/system-one-open ≠ mithalouni/system-one-open ≠ sgoedecke/system-one',
            'ZulfiFazhar/system-one ≠ sgoedecke/system-one',
            'Futureppo/typesafe_register key-farming skip',
            'FluidInference/FluidUse ≠ FluidInference/laya-coreml ≠ AndyInQtr/laya-coreai ≠ mizorewww/laya-coreml',
            '78.21% macro accuracy *theirs*',
            '180,031 decisions *theirs*',
            'hourly 0923 / notes.md §144',
            'GLiNER OSINT',
            'finite choices + none',
            '4B frozen+head 0.916 vs 27B zs 0.875 *theirs*',
            '8 questions 22.6 ms *theirs*',
            'AgentBeam local security layer',
            'unofficial not affiliated',
            'chips virtual',
            'densify §121 not a sibling first sighting',
            'Runs every rule against every line in parallel. No skimming',
            'Median 275 ms',
            'trolley 0.99 vs 0.78',
            '11/11/7 match/differ/undecided of 29 *theirs*',
            'retired name reservation is not a replica',
            'PerryLink/laya-mcp ≠ wsargent/laya-mcp',
            'DreamBlooms/dohnuts.cpp ≠ PsiACE/dohnuts',
            'ClemensSchartmueller/jev-guard ≠ leepokai/jev-guard ≠ seb4ez/jevguard',
            'AABBAASS1/jev-router ≠ gargpratyush/jev-router ≠ Akashdb5/jev-router ≠ daviddl9/jev-router',
            'skip-thin gnapse/jev-cli HTTP 404',
            'hf:Skylarcc/Laya-Online HTTP 401 *theirs*',
            'hf:piratehack009/laya-cn-flash-triage HTTP 404 *theirs*',
            'atharvamhaske/typesafe-sdk-go ≠ kisshan13/typesafe-ai-go ≠ stacklok/typesafe-go ≠ Nibir1/typesafe-go ≠ peach-zhang/typesafe-go ≠ draganm/go-jev ≠ kataras/jev ≠ robertjndw/gosys1 ≠ Stumble/jev-go',
            'hourly 1019 / notes.md §145',
            'schema-valid is not the same as correct',
            'API confidence is not P(correct)',
            'GEPA revises Choice instructions/criteria with weights fixed',
            'Brier 0.1357→0.0747 *theirs*',
            'F1 69.1%→79.7% *theirs*',
            'FN 4→6',
            'review-queue policy is not F1',
            'Soft is not gate',
            'Not an 18th scoring-table species',
            '发送永远手动',
            'About 180 ms',
            '$0.00241 *theirs*',
            'Not a screenshot agent',
            'pi-follow-through threshold 0.8 still soft',
            'densify §144 not a sibling first sighting',
            'pi-jev-context densify §134 not a sibling first sighting',
            'aliaihub/awesome-jev-usecases ≠ anandi1989/awesome-jev-usecases ≠ whyashthakker/awesome-jev-use-cases',
            'rezoch340/jev-chat-JARVIS-windows ≠ Finderchangchang/jev-chat-JARVIS',
            'aakgna/jevcal ≠ abhixhek/jevcal',
            '007M7/jev-chat ≠ w3cj/jev-chat ≠ Manta-Boardgame/jev-chat',
            'fstandhartinger/jev-router ≠ gargpratyush/jev-router',
            'prakash7474/Jev_guard ≠ leepokai/jev-guard',
            'rdutra/laya-mcp ≠ PerryLink/laya-mcp ≠ wsargent/laya-mcp',
            'Kourin1996/jev-playground ≠ wustep/jev-playground',
            'ai-ecoverse/cua-s1.js Cua-S1 ≠ TypeSafe',
            'skip-thin Unnati-23/jev-typesafe-guide antoniofaical/digital-twin-classifier-jev leonezhu/agent-kits empty README',
            'skip-thin wjw66/deepseek-harness-jev-pre-compaction ziwon/jev-actor empty SHA HTTP 409',
            'hf:chanoian/openjev-mlx-demo HTTP 401 *theirs*',
            'hf:clduab11/jev-calibration-statistics HTTP 401 *theirs*',
            'hf:yasserrmd/laya-lab HTTP 401 *theirs*',
        ):
            if frag not in haystack:
                failed.append(f"SKILL.md missing fragment {frag!r}")
        proto_candidates = [
            line
            for line in list(skill.splitlines()) + list(triggers.splitlines())
            if "cascade sign-flip / calibration theater" in line
        ]
        proto_line = max(proto_candidates, key=len) if proto_candidates else ""
        if not proto_line:
            failed.append(
                "cascade sign-flip line missing from SKILL.md and "
                "references/activation-triggers.md"
            )
        else:
            for frag in (
                "llm prompt to jev primitives",
                "conversion assistant not equivalent behavior",
                "heuristic conversion ≠ calibrated Noul",
                "alexwestco/llm-to-jev ≠ altryne/jevify",
                "user-provided 0940 / notes.md §118",
                "judge ≠ actuator",
                "candidate_mass",
                "softmax over A–H ≠ Noul",
                "hourly 0947 / notes.md §119",
                "ggmlc GGUF is not llama.cpp",
                "serving substrate ≠ calibrated replica",
                "Qwen3.5-9B ≠ Archer",
                "planner writes JEV selects",
                "hourly 1049 / notes.md §120",
                "open recreation ≠ calibrated replica",
                "semantic lint is a sensor not a proof",
                "cutoff 0.8 still soft",
                "paired bootstrap CIs *theirs*",
                "Same accuracy, 35x faster *theirs*",
                "hourly 1143 / notes.md §121",
                "revisit HIGH / since-last-look",
                "catalogued repo changed",
                "star-noise vs material change",
                "densify prior notes without inventing equivalence",
                "decide is not generate",
                "tryDecide returns typed calibrated judgments not a token stream",
                "GLiNER/GLiClass ports are class members not Jev replicas",
                "93.5% *theirs* not Harbor",
                "74.9 *theirs* not Harbor",
                "8.7x *theirs* not Harbor",
                "Option-Marker joint attention",
                "openjev:0.2.1",
                "thinking=True/False per-field budget",
                "PLAN_Qwen35",
                "hyperspaceai/jevcache ≠ kushals256/jevcache",
                "wire-compat ≠ logit-equiv",
                "SHA move is not a replica",
                "hourly 1248 / notes.md §123",
                'typesafe-sdk 0.7 Pydantic response models',
                'msgspec dropped',
                "The server's output is unchanged and was never wrong",
                'SchemaError is 400 plain-string detail not 422 list',
                'Pydantic response models ≠ logit-equiv',
                'msgspec dropped is not a replica',
                'Error contract is not a Noul',
                'coverage-at-error-budget *theirs* not Harbor',
                'PLAN_Qwen35 still proposal for review',
                'GLiNER locate ports are class members not Jev replicas',
                'Locate ≠ decide',
                '~160 ms *theirs* not Harbor',
                '0.971 F1 *theirs* not Harbor',
                'hf:fr0stbit3/laya-gguf serving substrate ≠ calibrated replica',
                'jkcdarunday/SystemOne-Next ≠ TypeSafe System One',
                'hourly 1340 / notes.md §124',
                'vLLM NVIDIA + MLX Apple Silicon',
                'Codiv hosted free endpoint',
                'dual /v1/systemone + /v1/chat/completions',
                'chat 501 on MLX',
                'dual serving is not generate',
                'Hosted Codiv ≠ TypeSafe',
                'hr98w/jev-visual 167★ Apple Silicon visual candidate scoring',
                '37.30s → 2.40s at 64 decisions *theirs*',
                'Breakout 9 bricks 6 returns 2 lives *theirs*',
                'candidate probabilities are relative not correctness',
                'jkudish/jev-mcp 156★ ten MCP tools',
                'recommendation is advisory',
                'the server never blocks on its own',
                'TypeSafe CLERC 5% to 18% *theirs*',
                'jkudish/jev-mcp ≠ burnigtm/jev-mcp',
                'zhengxuyu/litjev off-the-shelf Qwen decision layer',
                'Probabilities are not calibrated by default',
                'Qwen/Qwen3.8-27B ≠ Archer',
                'zhengxuyu/litjev ≠ alexwestco/llm-to-jev',
                'Zefan-Cai/Open-Jev LoRA + scalar head',
                '2B 94.71% 9B 97.54% hard test *theirs*',
                '2B OOD 86.02% 9B OOD 91.97% *theirs*',
                '80,816 training rows',
                '27B still in progress',
                'LoRA ≠ RLCD replica',
                'Zefan-Cai/Open-Jev ≠ TheoLeeCJ/openjev ≠ razorback16/openjev',
                'cristianoliveira/jeq intelligence you can pipe',
                'pass-min 0.8 still soft',
                'JEQ does not own actions',
                'AndyInQtr/laya-coreai CoreML serving substrate ≠ calibrated replica',
                'AndyInQtr/laya-coreai ≠ mizorewww/laya-coreml',
                'hourly 1441 / notes.md §125',
                'TypeLLM/TypeLLM densify HEAD 6a48f9f1e623',
                'README densify 3k→12k B',
                'Batch 5.8x *theirs*',
                'Constrained AR ≠ calibrated Noul',
                'jaredpalmer/kev densify HEAD b339f446a0ef',
                'Kev-0.6B 4B 8B family',
                '4B new-source 0.790/0.806 *theirs*',
                '8B new-source 0.796/0.780 *theirs*',
                'Jev hosted 0.857 *theirs*',
                'Questions share the input text but cannot read each other',
                'No Jev outputs were used for training',
                '8.2% ≥0.9 on wrong *theirs*',
                'option order can change an answer',
                'Qwen3 ≠ Archer',
                'TheoOliveira/pi-jev 21★ fail-closed routing',
                'JEV_THRESHOLD 0.65 still soft',
                'harshwasan/jev-sentinel fail closed never auto-allows',
                'harshwasan/jev-sentinel ≠ leepokai/jev-guard',
                'jackbarunz/jev-tool-router ≠ esinocchi/jev-tool-router',
                'threshold 0.90 still soft',
                '76/81 vs 77/81 *theirs*',
                '0.419s vs 2.459s *theirs*',
                '$0.00486 vs $0.03673 *theirs*',
                'not a security boundary',
                'baronunread/leanest fail-open uncertainty means RUN',
                'classifier.dev default Jev/Laya pluggable',
                'openlayer-ai/jevals ≠ dayhaysoos/jevals',
                'estimates not Harbor',
                'classifier ≠ authorizer',
                'MrJev/awesome-jev 118 entries catalog ≠ endorsement',
                'MrJev/awesome-jev ≠ yibie/awesome-jev',
                'Koushik890/jev-firewall fail closed ask_below 0.7 still soft',
                'CompleteTech-LLC-AI-Research/jev-codex-approval experimental native not compiled',
                'confidence is not a measured probability',
                'rh-guard owns primary gates',
                'hf:rAVEUK/open-jev-deberta-v3-large encoder class member not Jev replica',
                'hf:p-yan/laya-quanto serving substrate ≠ calibrated replica',
                'hf:Gtrkrsk/laya serving substrate ≠ calibrated replica',
                'hourly 1542 / notes.md §126',
                "razorback16/openjev densify HEAD febf02e88989",
                "release 0.3.0",
                "re-pin vLLM PR #57250 restructured head",
                "MODEL_VERSION stays openjev-0.1",
                "uv.lock hygiene",
                "restructured vLLM head ≠ logit-equiv",
                "frostney/clean-code-review 7★ typed judgments not opinions",
                "documentation is read not judged",
                "morcoan/JMP Joint Model Participation",
                "Models participate. Real tools execute.",
                "Thresholds are policy not model",
                "Kelbie/hunch ≠ carldaws/hunch ≠ tpellet/hunch ≠ huncho",
                "Jev never generates prose JSX or code",
                "json-render is the only renderer",
                "game success ≠ calibrated Noul",
                "Shalimov04/open-jev ≠ razorback16/openjev",
                "MstyAI/laya-onnx empty repo",
                "hf:Praveenrajus/jev-bench HTTP 200 was 401",
                "hourly 1643 / notes.md §127",
                'TypeLLM/TypeLLM densify HEAD 702e6a287f3c',
                'truncated thinking then constrained decode',
                '0.8B thinking On 0/18 *theirs*',
                'forced closure 20/20 type-valid *theirs*',
                'jaredpalmer/kev densify live HEAD 8465c4c4c294',
                'Kev-0.8B completes family',
                '4B new-source 0.794/0.832 *theirs*',
                '9B new-source 0.812/0.837 *theirs*',
                'transfer-v9 Kev-9B 5% Jev 9% Kev-8B 26% *theirs*',
                'SemIf Kev-9B 0.917 Jev 0.965 *theirs*',
                'scienthoon 0.952/0.911 vs 0.897/0.914 *theirs*',
                'transformers >= 5.17',
                'Qwen3.5 ≠ Archer',
                'notque/vexjoy-agent 421★ /d routes /do fallback',
                'Facts go to code. Judgments go to Jev. Only facts can block.',
                'Jev never blocks',
                'jqueryscript/awesome-jev ≠ MrJev/awesome-jev ≠ yibie/awesome-jev',
                'five-lines threshold 0.80 still soft',
                '371ms $0.0000189 300-call *theirs*',
                'tpellet/jevify ≠ altryne/jevify',
                'seb4ez/jevguard-mcp ≠ seb4ez/jevguard',
                'resumocast/jev-mcp ≠ jkudish/jev-mcp',
                'Adrian-Ernesto/jevsort ≠ zzzzzec/jevsort',
                'MidasMulli/kev-ane 155/155 argmax *theirs*',
                'hourly 1746 / notes.md §128',
                "Fine-tuning on your own data",
                "--data JSONL",
                "--init_from warm-start LoRA/head PR #9",
                "from-scratch ≠ warm-start",
                "JSONL labels ≠ Harbor",
                "Kev-0.8B 4B 9B Qwen3.5 family",
                "0.33 vs 0.84 vs 0.83/0.88 *theirs*",
                "reconstruction ≠ replica",
                "assay-001 split verdict",
                "Promethe-us/awesome-jev ≠ MrJev/awesome-jev ≠ yibie/awesome-jev",
                "ThePFMind/jev-mcp ≠ jkudish/jev-mcp",
                "kyegomez/open-jev ≠ razorback16/openjev",
                "namenu/pi-jev-effort ≠ TheoOliveira/pi-jev",
                "samatv256/mini-Jev ≠ r-ms/mini-jev",
                'TypeSafe-compatible ≠ TypeSafe replica',
                'SystemOne.from_pretrained',
                'replica ≠ TypeSafe',
                '76.7% vs Jev 86.9% strict common subset *theirs*',
                'kotoba-lang/typed-decisions ≠ convaiinnovations/laya-typed-decisions',
                'DeBERTa-v3-large 0.855 / 42 ms *theirs*',
                'aisearchio 15-link census catalog ≠ endorsement',
                'user-provided 1936 / notes.md §130',
                "hourly 1843 / notes.md §129",
                "Open-Jev densify HEAD 4933ee84951f",
                "Astra TREC commit 1dd56990be7e",
                "not merged base models",
                "customer-service P50 local HTTP 85.03 ms vs Jev HTTPS 295.26 ms *theirs*",
                "1024 tokens/32 candidates Open-Jev slower 1015.90 vs 301.37 *theirs*",
                "prefix caching experimental/off by default",
                "systems latency ≠ semantic equivalence",
                "GPT Luna P50 918.13 ms Astra 1938.39 ms *theirs*",
                "TREC-DL Jev/Luna/Astra completed",
                "Open-Jev TREC pending",
                "hard acc ≠ calibrated Noul",
                "densify §125 not a sibling first sighting",
                "Open-Jev densify / notes.md §125",
                "launch X thread https://x.com/Zefan_Cai/status/2101782158658695388",
                "2101786019607740436",
                "2101789698947793231",
                'platform does not execute trades',
                'heyjunpenn/awesome-jev 485 catalog ≠ endorsement',
                '62.69% vs 67.26% *theirs* not gold',
                '203.2s $0.84 vs 823.5s $1.50 *theirs*',
                'one seed-0 trial *theirs*',
                'Jev $0.018825 vs Astra $5.93 *theirs*',
                '10.59× *theirs*',
                '6 class flips',
                'agreement ≠ accuracy',
                'probabilities uncalibrated',
                'Qwen3.8 ≠ Archer',
                'Spanish −6.4 pp XNLI *theirs*',
                'ECE 0.057→0.101 *theirs*',
                '72.2% vs 63.4% p_max≥0.9 coverage *theirs*',
                'Convert LLM prompts to Jev prompts',
                'SHA unchanged 234058ab372d',
                'skip Zefan-Cai/Open-Jev densify open #53',
                'skip sgoedecke/system-one mithalouni/system-one-open kotoba-lang/typed-decisions open #54',
                'hourly 1946 / notes.md §131',
                'AI-reviewed labels ≠ gold',
                'one-trial robot ≠ Harbor',
                '10.59× systems ≠ ECE',
                'desc rewrite ≠ SHA/behavior change',
                'rule-table ≠ model',
                'local_only ≠ Jev',
                'jaredpalmer/kev densify HEAD c096660c8da2',
            'PLAN SHA 8d77dd271c66',
            'README SHA unchanged 84b872488915',
            'night-2 dates/unknowable/assertion',
            'KEV_TEMPERATURE T≈2.0',
            'Brier 0.291→0.267 ECE 0.105→0.039 *theirs*',
            '7.5%→3.2% *theirs*',
            'grouped T rejected',
            'Qwen3.6-35B-A3B smoke 0.812 *theirs*',
            '21M LoRA experts frozen',
            'Hub --revision night2-du',
            'MMLU-Pro 1000 Kev-9B 0.511 Jev 0.829 *theirs*',
            'Qwen3.6 ≠ Archer',
            'temperature scaling ≠ ECE unless measured',
            'Hub --revision is a pin not a replica',
            'kotoba-lang/typed-decisions densify HEAD ff7f84e74d04',
            'feat expose trained OpenJev decision runtime',
            'open_jev.py',
            'tests/test_open_jev.py',
            'generated_text: False',
            'trained runtime ≠ TypeSafe',
            'OpenJev.from_pretrained',
            'decide_request kind typed-decisions/open-jev-v1',
            'daftAI2026/awesome-jev ≠ heyjunpenn/awesome-jev',
            'franckverrot/lev ≠ jaredpalmer/kev',
            'neko233-com/laya-go ≠ convaiinnovations/laya',
            'tryAGI/TypeSafeAI ≠ official',
            'hourly 2049 / notes.md §132',
            'Open-Jev densify HEAD a00559ea0ab2',
            'README SHA unchanged ce1a587219e4',
            'Publish prepared Open-Jev provider quality evaluation pipeline',
            '808 requests 1841 labelled decisions per model',
            'Open-Jev GPU inference has not started',
            '48 CPU tests pass',
            'Open-Jev TREC pending',
            '65/76 72/76 66/76 60/76 71/76 *theirs*',
            'provider pipeline ≠ completed Open-Jev quality',
            'CPU tests ≠ GPU scores',
            'tinmanlab/cartpole-jev densify HEAD 922cc61490a0',
            'Active model Kev Not TypeSafe Jev',
            '81.25% 52/64 *theirs*',
            'one record of 64',
            'fine-tuned Kev ≠ TypeSafe Jev',
            'softmax ≠ calibrated Noul',
            'xuboboo/ashare-trader densify HEAD 26c7e95e6828',
            'QMT sidecar mock/dry default no orders',
            'AUC 0.532 *theirs*',
            'gauravsaini/kevin first card Playwright + Onyx',
            '3.69ms *theirs* not Harbor',
            'metask-jev-4b 79.6% / 80.1% *theirs*',
            'cutoff 95% still soft',
            'hourly 2146 / notes.md §133',
            'razorback16/openjev densify HEAD 2050fdb8280d',
            'MLX backend steps>1/think/text gen + image Qs',
            'GitHub Release v0.1.1',
            'README SHA unchanged 9f6dea3a4c8c',
            'zjunlp/JevLoop 6★ independent not affiliated',
            'option order 0.188 or 0.542 *theirs*',
            'n=8 is not Harbor',
            'ranking before lossless condensation',
            'hourly 2347 / notes.md §135',
            'Open-Jev densify HEAD f46ff604f794',
            'README SHA e32c4bbd519c',
            'Publish audited JevBench public-subset baselines',
            'public-subset ≠ Harbor',
            '231 ≠ 534',
            'jaredpalmer/kev densify HEAD e0bcf50153f1',
            'PLAN correct 35B MMLU-Pro (0.550)',
            'evaluate.load honour weights_dtype=bf16',
            'wy-coliney/jev-browser-use 282★',
            '5-10× *theirs* not Harbor',
            'fail-open routing ≠ permission',
            'ordered routing ≠ end-to-end',
            'softmax next-token ≠ calibrated Noul',
            'potential_match ≠ hiring decision',
            'hourly 0049 / notes.md §136',
            'Open-Jev densify HEAD ed45657bf726',
            'README SHA 12e0f581e15d',
            'Publish audited v3 community data and held-out evaluation protocol',
            'Redesign readable project site and consolidate benchmark results',
            'v3 data prepared ≠ retrained released models',
            'held-out protocol ≠ Harbor',
            '1,280-row panel ≠ Harbor',
            'finite training loss ≠ quality improvement',
            'website redesign ≠ calibration',
            '129,288 decision rows 74,921 training',
            'frozen mixture 96,849 training',
            '1,280-row / 840-group comparison panel',
            '27B step 616 pending',
            'naive throws away 83% *theirs*',
            'certo KL 0.008 acc 0.844 ECE 0.004 *theirs*',
            'first-instinct 63.3%→78.1% *theirs* not Harbor',
            '371,278 prepared ≠ consumed',
            'Jev is a gate not a generator',
            'Lake remains admission',
            'Jev never writes Lean',
            'community port ≠ TypeSafe',
            'chy4pro/jev-for-chrome ≠ browser-use/jev-ultrafast',
            'joint RLCD *theirs*',
            'Dohnuts ≠ TypeSafe',
            'Akashdb5/jev-router ≠ gargpratyush/jev-router ≠ daviddl9/jev-router',
            'kiuckhuang/laya-jev ≠ KonghaYao/laya-jev',
            'tegersdorfer-collab/jevkit ≠ isiomaC/jevkit ≠ WaynezProg/jev-kit',
            'buluoray/JevOnly already carded',
            'yottayoshida/jev-intent-review already carded',
            'skip-thin Iskandeur/system1-system2 zhlei07/open-system-one Hand-In/openjev-multimodal gwxcsny53/jev-watchtower empty SHA',
            'hourly 0151 / notes.md §137',
            'GLiClass knowledgator Hub family class-peer catalog not Jev equivalent',
            'typed-decision-leaderboard *theirs* not Harbor',
            'JEV 0.7350 ZTC 27B 0.7289',
            'Jevbridge ACP and MCP adapter',
            'Cut the slop',
            'Not a Cua binding',
            'open reproductions of the shape',
            '82.3% ECE 0.017 *theirs*',
            'hourly 0248 / notes.md §138',
            'Greedy 0.90 vs Oracle 0.82 *theirs*',
            'Random conf 0.00 still 20.5% *theirs*',
            '8,400 calls $0.39 *theirs*',
            'Noul 0.7 true 44% *theirs*',
            'JevBench 81.65 *theirs* not Harbor',
            '0-byte Mandelbrot is not a replica',
            'training not complete',
            'meijustory123/OpenJev-Kit IS meijustory123/openjev',
            'Compose meaning like state',
            'A clean report is not proof',
            'does not sandbox',
            'hourly 0348 / notes.md §139',
            'keeps essentially every block 0.0%/−0.5% *theirs*',
            'Token reduction alone is not cost reduction',
            'Chat 1282.3 ms vs gateway 232.1 ms ~1/5.5 *theirs*',
            'acc 0.796 ECE 0.027 *theirs*',
            'How you ask mattered more',
            'Calibration is not yet measured',
            'Add JevHarness project link to READMEs',
            'densify §115 not a sibling first sighting',
            'Awesomejev 691→802',
            'tracker likes 81 lastModified UNCHANGED',
            'hf:AXERA-TECH/Laya',
            'hf:openjev/openjev-MLX-4bit ≠ razorback16/openjev',
            'GeekyAbs/laya ≠ convaiinnovations/laya',
            'Softmax over candidate logprobs',
            'skip-thin Adrian-lzr/jev-spire-brain Dililianxice/jev-robotic-arm-benchmark baltzparra/jev-study lzero07/jev-laya-statement qq150078158-lab/TDM-demo empty SHA',
            'hourly 0445 / notes.md §140',
            'not a digital twin',
            'Score fan-out ≠ chess engine',
            'Jev cannot waive a failing check',
            'umgbhalla/jevx ≠ hawkyre/jevx',
            'ryanzen9/XFlow ≠ hawkyre/jevx',
            'Tsagaanbayr1/jev-tetris ≠ planstack-ai/jev-tetris-benchmark',
            'wizicer/jev_info_site ≠ JingHao-Leon/awesome-jev-apps',
            'hourly 0551 / notes.md §141',
            'Night-2 sign-off',
            'densify §45 not a sibling first sighting',
            'densify §35 not a sibling first sighting',
            'did not distill from Jev',
            'Independent community project',
            'APUS-OpenJev 9B 85.0% vs Jev API 82.5% *theirs* not Harbor',
            'Frozen80 n=80',
            'Candidate probabilities are not calibrated confidence',
            'Jev is the first adapter the design is bound to no engine',
            'Zero Hallucinations marketing',
            'kylemclaren/jevsearch ≠ kylemclaren/jev-search',
            'stacklok/typesafe-go ≠ kisshan13/typesafe-ai-go',
            'DevMortimer/pi-typesafe ≠ twilwa/pi-typesafe',
            'hf:SeanLiu/Jev-Vision ≠ sseanliu/Jev-Vision',
            'sontakey/awesome-jev ≠ heyjunpenn/awesome-jev',
            'Giustino98/system-one-bench ≠ mallahyari/system-one-benchmark',
            'skip-thin eatmoreduck/jev-jarvis',
            'densify §139 not a sibling first sighting',
            'AbdelStark/awesome-typesafe-jev IS AbdelStark/awesome-typesafe',
            'hourly 0707 / notes.md §142',
            '只传文字，不传截图',
            'Text only no screenshots',
            '100% of our tax document corpus at $0.001 per page',
            'TaxCalcBench 0 strict errors *theirs*',
            'blank IRS 38 strict errors 5.05% *theirs*',
            '100% of corpus *theirs* not Harbor',
            'The model does not receive screenshots',
            '21 seconds for 9 actions *theirs*',
            'A completed booking is not demonstrated',
            'droidrun/mobile-jev ≠ Friedjof/jev-mobile',
            'giuliosmall/pg_typesafe ≠ realZachi/pg-jev',
            'itsmostafa/typesafe-mcp ≠ cyrusasco/typesafe-mcp ≠ burnigtm/jev-mcp',
            'The field guide to typed decisions',
            'densify §141 not a sibling first sighting',
            'hf:Praveenrajus/jev-bench HTTP 401 was 200',
            'densify §107/§125 remainder',
            'densify §134 not a sibling first sighting',
            'ENEM 2025 *theirs* not Harbor',
            'Ying-Kai-Liao/jev-browser ≠ wy-coliney/jev-browser-use',
            'w3cj/jev-chat ≠ Manta-Boardgame/jev-chat',
            'snellingio/system-one ≠ sgoedecke/system-one ≠ Luke458/system-one ≠ developerekene/System-One',
            'stoleas/typesafe-computer-use ≠ awlevin/typesafe-computer-use',
            'holotwist/laya ≠ NandhaKishorM/laya',
            'RafalWilinski/vibecheck ≠ psyb0t/vibecheck',
            'dannote/jev ≠ okooo5km/jev ≠ sebastianbugal/jev',
            'skip-thin developerekene/System-One holotwist/laya wuzhiping/jev-laya empty SHA',
            'hf:s1lv3rj1nx/openjev-healthcare-router HTTP 401 *theirs*',
            'hourly 0823 / notes.md §143',
            'JevBench 65.80% vs Jev 86.58%',
            'Laya multi 47.62%',
            'same-species serving not an 18th scoring row',
            'field→value match among supplied options not free text',
            "Screenshots aren't uploaded",
            'Jev is the only model',
            'not fully offline',
            'JSON 0.909 letters 0.907 *theirs*',
            '13 600 / 13 600 *theirs*',
            'softmax over letters ≠ calibrated Noul',
            'model=jev-auto',
            'AG News 0.910 *theirs*',
            'Banking77 0.870 *theirs*',
            'DAIR Emotion 0.480 *theirs*',
            'Fastest and cheapest web agent *theirs*',
            'densify §137 not a sibling first sighting',
            'densify description rewrite',
            'TypeSafeAI/typesafe-playground ≠ kavehmz/typesafe-playground ≠ nickthompson480/typesafe-ai-playground',
            'No generative fallback',
            'Unofficial research repo. Not affiliated with TypeSafe AI',
            'skip-thin GokhanCalkap/LayaCode fredzhaozonghui/LAYA1 empty SHA',
            'Abhi895/Laya ≠ convaiinnovations/laya',
            'mjdileep/OpenJev ≠ Zefan-Cai/Open-Jev',
            'Abhi001vj/system-one-open ≠ mithalouni/system-one-open ≠ sgoedecke/system-one',
            'ZulfiFazhar/system-one ≠ sgoedecke/system-one',
            'Futureppo/typesafe_register key-farming skip',
            'FluidInference/FluidUse ≠ FluidInference/laya-coreml ≠ AndyInQtr/laya-coreai ≠ mizorewww/laya-coreml',
            '78.21% macro accuracy *theirs*',
            '180,031 decisions *theirs*',
            'hourly 0923 / notes.md §144',
            'GLiNER OSINT',
            'finite choices + none',
            '4B frozen+head 0.916 vs 27B zs 0.875 *theirs*',
            '8 questions 22.6 ms *theirs*',
            'AgentBeam local security layer',
            'unofficial not affiliated',
            'chips virtual',
            'densify §121 not a sibling first sighting',
            'Runs every rule against every line in parallel. No skimming',
            'Median 275 ms',
            'trolley 0.99 vs 0.78',
            '11/11/7 match/differ/undecided of 29 *theirs*',
            'retired name reservation is not a replica',
            'PerryLink/laya-mcp ≠ wsargent/laya-mcp',
            'DreamBlooms/dohnuts.cpp ≠ PsiACE/dohnuts',
            'ClemensSchartmueller/jev-guard ≠ leepokai/jev-guard ≠ seb4ez/jevguard',
            'AABBAASS1/jev-router ≠ gargpratyush/jev-router ≠ Akashdb5/jev-router ≠ daviddl9/jev-router',
            'skip-thin gnapse/jev-cli HTTP 404',
            'hf:Skylarcc/Laya-Online HTTP 401 *theirs*',
            'hf:piratehack009/laya-cn-flash-triage HTTP 404 *theirs*',
            'atharvamhaske/typesafe-sdk-go ≠ kisshan13/typesafe-ai-go ≠ stacklok/typesafe-go ≠ Nibir1/typesafe-go ≠ peach-zhang/typesafe-go ≠ draganm/go-jev ≠ kataras/jev ≠ robertjndw/gosys1 ≠ Stumble/jev-go',
            'hourly 1019 / notes.md §145',
            'schema-valid is not the same as correct',
            'API confidence is not P(correct)',
            'GEPA revises Choice instructions/criteria with weights fixed',
            'Brier 0.1357→0.0747 *theirs*',
            'F1 69.1%→79.7% *theirs*',
            'FN 4→6',
            'review-queue policy is not F1',
            'Soft is not gate',
            'Not an 18th scoring-table species',
            '发送永远手动',
            'About 180 ms',
            '$0.00241 *theirs*',
            'Not a screenshot agent',
            'pi-follow-through threshold 0.8 still soft',
            'densify §144 not a sibling first sighting',
            'pi-jev-context densify §134 not a sibling first sighting',
            'aliaihub/awesome-jev-usecases ≠ anandi1989/awesome-jev-usecases ≠ whyashthakker/awesome-jev-use-cases',
            'rezoch340/jev-chat-JARVIS-windows ≠ Finderchangchang/jev-chat-JARVIS',
            'aakgna/jevcal ≠ abhixhek/jevcal',
            '007M7/jev-chat ≠ w3cj/jev-chat ≠ Manta-Boardgame/jev-chat',
            'fstandhartinger/jev-router ≠ gargpratyush/jev-router',
            'prakash7474/Jev_guard ≠ leepokai/jev-guard',
            'rdutra/laya-mcp ≠ PerryLink/laya-mcp ≠ wsargent/laya-mcp',
            'Kourin1996/jev-playground ≠ wustep/jev-playground',
            'ai-ecoverse/cua-s1.js Cua-S1 ≠ TypeSafe',
            'skip-thin Unnati-23/jev-typesafe-guide antoniofaical/digital-twin-classifier-jev leonezhu/agent-kits empty README',
            'skip-thin wjw66/deepseek-harness-jev-pre-compaction ziwon/jev-actor empty SHA HTTP 409',
            'hf:chanoian/openjev-mlx-demo HTTP 401 *theirs*',
            'hf:clduab11/jev-calibration-statistics HTTP 401 *theirs*',
            'hf:yasserrmd/laya-lab HTTP 401 *theirs*',
            ):
                if frag not in proto_line:
                    failed.append(f"SKILL.md protocol missing {frag!r}")
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    for name, lock in (
        ("0843", UNIQ_0843),
        ("0915", UNIQ_0915),
        ("jcr", UNIQ_JCR),
        ("0922", UNIQ_0922),
        ("0940", UNIQ_0940),
        ("0947", UNIQ_0947),
        ("1049", UNIQ_1049),
        ("1143", UNIQ_1143),
        ("1248", UNIQ_1248),
        ("1340", UNIQ_1340),
        ("1441", UNIQ_1441),
        ("1542", UNIQ_1542),
        ("1643", UNIQ_1643),
        ("1746", UNIQ_1746),
        ("1843", UNIQ_1843),
        ("1936", UNIQ_1936),
        ("openjev_densify", UNIQ_OPENJEV),
        ("1946", UNIQ_1946),
        ("2049", UNIQ_2049),
        ("2146", UNIQ_2146),
        ("2246", UNIQ_2246),
        ("2347", UNIQ_2347),
        ("0049", UNIQ_0049),
        ("0151", UNIQ_0151),
        ("0248", UNIQ_0248),
        ("0348", UNIQ_0348),
        ("0445", UNIQ_0445),
        ("0551", UNIQ_0551),
        ("0707", UNIQ_0707),
        ("0823", UNIQ_0823),
        ("0923", UNIQ_0923),
        ("1019", UNIQ_1019),
    ):
        if lock in changelog:
            failed.append(
                f"CHANGELOG.md holds {name} uniqueness dump "
                "(v0.4.0: dumps live in changelog-hourly.md)"
            )
    if "Hourly 0743 uniqueness lock:" in changelog:
        failed.append("CHANGELOG.md holds 0743 uniqueness dump")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    failed.extend(readme_dump_wall_violations(readme))
    index = (ROOT / "docs/index.md").read_text(encoding="utf-8")
    for s in ("TypeSafe Jev Choice/Score/Noul", "Install the skill"):
        if s not in index:
            failed.append(f"docs/index.md missing Pages gate {s!r}")
    layout = (ROOT / "docs/_layouts/default.html").read_text(encoding="utf-8")
    if "LICENSE" not in layout:
        failed.append("docs/_layouts/default.html missing LICENSE (Pages gate after #34)")
    eco = (ROOT / "docs/ecosystem.md").read_text(encoding="utf-8")
    if "decision-circuits tutorial. `notes.md` §114." not in eco:
        failed.append("docs/ecosystem.md 0843 blurb must cite notes.md §114")
    if REVISIT_LOCK in changelog:
        failed.append(
            "CHANGELOG.md holds revisit lock dump "
            "(protocol lock lives in SKILL.md + research/)"
        )
    helper = ROOT / "research/revisit_fingerprints.py"
    store = ROOT / "research/revisit_fingerprints.json"
    if not helper.is_file():
        failed.append("missing research/revisit_fingerprints.py")
    if not store.is_file():
        failed.append("missing research/revisit_fingerprints.json")
    else:
        try:
            r = subprocess.run(
                [sys.executable, str(helper), "--self-test"],
                cwd=str(ROOT),
                capture_output=True,
                text=True,
                check=False,
            )
        except OSError as e:
            failed.append(f"revisit_fingerprints.py could not run: {e}")
        else:
            if r.returncode != 0:
                failed.append(
                    "revisit_fingerprints.py --self-test failed: "
                    + (r.stdout + r.stderr).strip()
                )
    skill_headings = (ROOT / ".agents/skills/augustus/SKILL.md").read_text(
        encoding="utf-8"
    )
    if "## REVISIT / since last look" not in skill_headings:
        failed.append("SKILL.md missing REVISIT / since last look heading")
    contributing = (ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")
    if "revisit HIGH like novel HIGH" not in contributing:
        failed.append("CONTRIBUTING.md missing revisit HIGH like novel HIGH")
    if failed:
        print("uniqueness-gate FAIL")
        for line in failed:
            print(" -", line)
        return 1
    print("uniqueness-gate ok")
    print(
        f"0843 chars={len(UNIQ_0843)} 0915 chars={len(UNIQ_0915)} "
        f"jcr chars={len(UNIQ_JCR)} lock0922 chars={len(UNIQ_0922)} "
        f"0940 chars={len(UNIQ_0940)} 0947 chars={len(UNIQ_0947)} "
        f"1049 chars={len(UNIQ_1049)} "
        f"1143 chars={len(UNIQ_1143)} "
        f"1248 chars={len(UNIQ_1248)} "
        f"1340 chars={len(UNIQ_1340)} "
        f"1441 chars={len(UNIQ_1441)} "
        f"1542 chars={len(UNIQ_1542)} "
        f"1643 chars={len(UNIQ_1643)} "
        f"1746 chars={len(UNIQ_1746)} "
        f"1843 chars={len(UNIQ_1843)} "
        f"1936 chars={len(UNIQ_1936)} "
        f"openjev_densify chars={len(UNIQ_OPENJEV)} "
        f"1946 chars={len(UNIQ_1946)} "
        f"2049 chars={len(UNIQ_2049)} "
        f"2146 chars={len(UNIQ_2146)} "
        f"2246 chars={len(UNIQ_2246)} "
        f"2347 chars={len(UNIQ_2347)} "
        f"0049 chars={len(UNIQ_0049)} 0151 chars={len(UNIQ_0151)} 0248 chars={len(UNIQ_0248)} 0348 chars={len(UNIQ_0348)} 0445 chars={len(UNIQ_0445)} 0551 chars={len(UNIQ_0551)} 0707 chars={len(UNIQ_0707)} 0823 chars={len(UNIQ_0823)} 0923 chars={len(UNIQ_0923)} 1019 chars={len(UNIQ_1019)} "
        f"revisit chars={len(REVISIT_LOCK)} "
        f"overlays={len(OVERLAYS)} "
        f"revisit_overlays={len(REVISIT_OVERLAYS)}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
