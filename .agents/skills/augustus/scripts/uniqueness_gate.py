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
The user-provided ryana/jevify lock (notes.md §152) lives in notes.md
and this module only. It is not an overlay-wall dump.
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

UNIQ_1110 = (
    "Hourly 1110 uniqueness lock: hf:thaitea/laya-vision 13 likes sha a2653db2831b cc-by-nc-sa-4.0; SmolVLM-256M vision typed choice/score/noul; same-species serving not an 18th scoring row; independent not affiliated; A-OKVQA 63.1% ECE 0.266 to 0.094 *theirs*; ScienceQA 89.0% ECE 0.080 to 0.034 *theirs*; VQAv2 noul 73.2% ECE 0.085 to 0.042 *theirs*; All n=8235 75.9% ECE 0.035 *theirs* not Harbor; VQAv2 re-split not comparable to published VQAv2; about 71 ms *theirs*; option order varies 1.2 points *theirs*; act head untrained do not gate on it; not a drop-in replacement for Laya text checkpoint; usage loads thaitea/laya-vision-smolvlm-256m already \u00a787; hf:thaitea/laya-vision \u2260 thaitea/laya-vision-smolvlm-256m card id; AntonG87/codearia-sieve 1\u2605 MIT TS HEAD 64ecd4151726 README SHA b03a3d29ab22; page to typed fields; 6 of 6 *theirs*; 11 of 11 *theirs* not Harbor; robots-disallowed did not fetch; no model required for the parse; 7Zenox/gemma-jev 0\u2605 NOASSERTION Py HEAD 2eed119e03ff README SHA c3b58d6a15a9; generation-free letter slots; 144 authored decisions *theirs*; Gemma 3 270M 0.293 below chance 0.333 *theirs*; Gemma 4 E2B-it JSON chat 0.807 *theirs*; Qwen3.5-4B JSON chat 0.813 *theirs*; JSON chat \u2260 calibrated Noul; softmax over letter slots \u2260 calibrated Noul; bf16 vs fp32 argmax-agreement check not run; Gemma \u2260 Archer; Qwen3.5 \u2260 Archer; Pdbz199/local-decision-model 0\u2605 MIT Py HEAD ddceb5829849 README SHA 80659ec966f5; independent project built only from the public post; one pass no generation; schema-valid is not the same as correct; musubi-labs/musubi-jev 0\u2605 Apache-2.0 HEAD e943f21e4057 README SHA 8ffd43564204; README is a kev tree copy; copied kev numbers are not a musubi bench; musubi-labs/musubi-jev \u2260 jaredpalmer/kev; quaeast/vllm2jev 0\u2605 NOASSERTION Py HEAD 8a51f94961ea README SHA be92356f1176; does not reproduce Jev calibration; wire-compat \u2260 logit-equiv; IAmJSD/pg-laya 0\u2605 Apache-2.0 Rust HEAD 1bc66a4d6a7f README SHA 03476be41744; SQL choice score noul; serving substrate \u2260 calibrated replica; IAmJSD/pg-laya \u2260 realZachi/pg-jev \u2260 giuliosmall/pg_typesafe; gbesse/jev-rerank-server 0\u2605 MIT JS HEAD b28cef5e34a6 README SHA 91167c66c29c; SciFact n=25 nDCG@10 0.616377 to 0.718260 *theirs*; Recall@10 0.84 unchanged *theirs*; ranking \u2260 calibration; MarkChu-git/typesafe-mcp 0\u2605 MIT HEAD a064b14207c0 README SHA ae27210cc5af; decision act/review/abstain is code; act_above 0.8 still soft; MarkChu-git/typesafe-mcp \u2260 itsmostafa/typesafe-mcp \u2260 cyrusasco/typesafe-mcp \u2260 Renwang-Huang/typesafe-mcp; pythongiant/laya-drift densify 4\u2605 TS HEAD d33db6736ed8 README SHA 7af1781c28c5 was 334953e5cb8f / 6662121ba0f3; monitor agent drift; densify \u00a7142 not a sibling first sighting; Adkid-Zephyr/chinese-workflow-decision-bench densify 1\u2605 MIT Py HEAD b694dc6dbcba README SHA 9ef2b7d76a37 was 6d0a7c2af303 / 4ed71a36cd51; 64/64 and 63/64 *theirs* not Harbor; synthetic not a group-chat dump; densify \u00a7145 not a sibling first sighting; turenlabs/jast densify 1\u2605 MIT Rust HEAD c6588285208f README SHA d9214ca31f92 unchanged; star 0 to 1 is star-noise; densify \u00a7145 not a sibling first sighting; JabbaKadabra/SystemOneDotNet densify MIT C# HEAD 5120ffb84cc5 README SHA 0809f98d4c93 was 5bff3394281c / 76a9188c180a; unofficial .NET client; wire-compat \u2260 logit-equiv; densify \u00a7143 not a sibling first sighting; arnavm-codes/JevFence densify HEAD 7e277474ff5e README SHA 2bbb684757de was 6fe62ca7b10c / 5441aaeaace0; soft scores \u2260 hard gates; densify \u00a7145 not a sibling first sighting; cloudbtl/JevRAG 0\u2605 Apache-2.0 Py HEAD 307ab19ee9cf README SHA 9b814bb6624b; first card revisit tag no prior notes card; cloudbtl/JevRAG \u2260 emretheus/jev-rag-benchmark \u2260 erendikmenn/jev-rag-benchmark; gbesse/decision-workbench densify MIT JS HEAD 877d1a9add5b README SHA 24cce8900d67 was 8889cf3750a3 / 14a3bf79da7a; human review separate from model output; demo scores are not accuracy measurements; densify \u00a7139 not a sibling first sighting; 0xagentlabs/jev-xiangqi \u2260 Zafer-Liu/jev-xiangqi; RyanNg1403/jev-cli \u2260 gnapse/jev-cli \u2260 sunchojack/jev-cli; KennethAshley/awesome-jev \u2260 heyjunpenn/awesome-jev \u2260 yibie/awesome-jev; malevrigns/agent-jev \u2260 hf:aimeigaoshou/agent-jev; 79.25% 1585/2000 ECE 0.1687 *theirs* not Harbor; kidzik/jiffy probabilities are uncalibrated; s3rli/jevips name collision not a decision model; skip-thin Alpha-Harper-Franklin/astra-jev jonas050210/Laya_Playground pietrushka/jev-youtube-filter empty SHA HTTP 409; skip-thin THANK-YOU-FOR-YOUR-ORDER-ASDF123/repo-laya4qxd Ylr9933/JevForAgent empty README; hf:marcmagn1/jev-alt-systemone-eval dataset sha 95f679e8455b README 404 models HTTP 401 *theirs*; catalog \u2260 endorsement; game success \u2260 calibrated Noul; does not execute; routing \u2260 permission; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62/#63/#64/#65/#66/#67/#68/#69/#70; notes.md \u00a7146"
)



UNIQ_GLANCE = (
"User-provided glance uniqueness lock: yoheinakajima/glance Apache-2.0 Py HEAD 8f36e063bffb README SHA b57280394bc1 LICENSE SHA d645695673349e; 4★; 1 fork; star-noise is not the fold; size 51490; pushed 2026-09-21T17:37:40Z; created 2026-09-21T06:51:38Z; PyPI glance-vlm 0.3.1; tag v0.3.1; site https://glance.yohei.me; topics calibration, image-classification, vision-language-model, vlm, zero-shot; Ask an open vision-language model typed questions about an image and get probabilities back, on your own machine; frozen open VLM default Qwen3-VL-4B Apache-2.0; yes/no pick-one and default unfitted rating read from answer-token logits in one forward pass; default unfitted rating is jsondigits (1 pass, exact 0.669); labeled glance fit uses ens4d (4 passes); four-pass zero-shot rating 0.570 behind write JSON 0.672; glance fit --unlabeled uses jsondigits; fast2 (2 passes) and digits (1 pass) remain available; Glance is a calibration and measurement harness around that readout. It is not a model; trains no weights; images never leave the machine; local server binds 127.0.0.1; noul yes/no choice pick-one score ordered rating; POST /v1/decide; zero-shot table only yes/no 0.939 pick-one 0.933 rating exact 0.669 *theirs*; Gemini 3.1 Flash-Lite yes/no 0.961 pick-one 0.933 rating 0.763 *theirs*; fitted readout marked fitted do not say zero-shot or no training: unlabeled image-quality 0.67 to 0.76 exact (README; CLAIMS one-pass 0.758 at 16 unlabeled images) *theirs*; labeled about 32 images 0.86 exact ECE about 0.03 per rubric does not transfer *theirs*; Glance is not an image-quality metric; on KADID-10k it misses their own targets; do not quote interim KADID numbers; Q-SiT-mini 0.9B trained for image quality is level under the same 32-label fit; hand-built features beat it on low-level artifacts when labels are plentiful; non-image-quality rubrics 0.55 exact with 300 labels *theirs*; tilt 0.33 *theirs*; geometric probes diagonals 0.30 largest of four shapes 0.52 eight objects 0.56 *theirs*; stripe direction hidden-state linear probe 0.99 *theirs*; raw yes/no ECE 0.111 and 0.179 *theirs*; pooled two-number Platt map on those suites ECE 0.061 and 0.053 *theirs*; transfer to a new yes/no task untested; glance fit is a per-rubric rating map not that Platt map; explicit other held-out breeds 7.7% *theirs*; claims ledger: faster or cheaper than Jev do not claim; shares inference object with featherless-ai/simple-jev hr98w/jev-visual zhengxuyu/litjev; request and response shapes follow TypeSafe Jev hosted text; yoheinakajima/glance ≠ TypeSafe Jev; POST /v1/decide ≠ TypeSafe /v1/systemone ≠ IamBusy/OpenJev /v1/decide is a wire lock not OpenJev v2 identity; OpenJev v2 is Hub AlexWortega/openjev trained 4B multimodal claim scorer census §77 do not mint a sibling card; OpenJev v2 ≠ Zefan-Cai/Open-Jev ≠ razorback16/openjev ≠ IamBusy/OpenJev-Vision; Zefan-Cai/Open-Jev §125 is a separate trained-head namesake; trains no weights unlike YOFO and unlike hf:thaitea/laya-vision §146 and unlike OpenJev v2 and unlike IamBusy/OpenJev-Vision; harness not weights; soft probs for threshold abstain rank; soft scores ≠ hard gates; logits are not calibrated probabilities of correctness; *theirs* not Harbor; catalog ≠ endorsement; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62/#63/#64/#65/#66/#67/#68/#69/#70/#71/#72; notes.md §147"
)

UNIQ_1203 = (
    "Hourly 1203 uniqueness lock: peterfriese/jev-foundation-models Swift 6 bridge into Apple Foundation Models; peterfriese/jev-foundation-models 1★ Apache-2.0 Swift HEAD 27963995965d README SHA b40b836f4396; 40 to 150 ms *theirs*; zero hallucinations is a README claim *theirs*; Never embed API keys; bridge is not an on-device replica; Apple Foundation Models host the call shape; Jev remains the decision model; Alexander-Ollman/laya-ft signal detection; Alexander-Ollman/laya-ft 0★ NOASSERTION Py HEAD 41f8247c3969 README SHA e97e314c88d5; Aegis prompts F1 60.6% 81.5% 83.7% *theirs*; Aegis responses 37.4% 69.5% 77.0% *theirs*; ToxicChat 36.4% 50.5% 53.3% *theirs*; WildGuard prompts 48.7% 59.4% 65.7% *theirs*; WildGuard responses 20.8% 53.3% 51.6% *theirs*; BeaverTails 6.0% 34.1% 59.4% *theirs*; false alarms 24.8% to 65.2% to 47.2% *theirs*; XSTest 250 harmless prompts *theirs*; 67,890 decisions *theirs* not Harbor; No Jev outputs were used; not a dependable general-purpose safety filter *theirs*; detection gain is not a license to auto-block; Soft judgment never sole veto; Ejokey/lightjev $0.000851 in 23.6s *theirs*; Ejokey/lightjev 0★ MIT Py HEAD 921fffb588b9 README SHA 30fa74b9f711; six pages four hits 3/3 *theirs*; about $0.0001 per decision *theirs*; STOP always available; one crawl is not Harbor; code owns the queue; ruslanlap/jev-gate measured $0.000143 *theirs*; ruslanlap/jev-gate 0★ MIT Py HEAD 300014a1bdea README SHA 96e31d8dc5d8; exit code 2 is code; noul p=0.02 is not a merge; five typed questions; probabilities must sum to 1 within 0.02 *theirs*; ruslanlap/jev-gate ≠ hf:SargeDev/jev-gate-student-b-merged; Renwang-Huang/arbitype independent not an official TypeSafe product; Renwang-Huang/arbitype 0★ MIT Py HEAD 454cf2c4a345 README SHA ffa11f281a52; PyPI 0.6.0 pending; Renwang-Huang/arbitype ≠ Renwang-Huang/typesafe-mcp; Codercise/jev-in-practice key stays in the Node process; Codercise/jev-in-practice 0★ MIT TS HEAD 02be666a30ad README SHA 3f0c47161028; playground is not a bench; fraud sales patent presets; emlama/jev-mcp saved tool is inputs context questions docs; emlama/jev-mcp 0★ MIT Py HEAD 4c7da93a21be README SHA a258eb52829c; emlama/jev-mcp ≠ burnigtm/jev-mcp ≠ jkudish/jev-mcp ≠ resumocast/jev-mcp ≠ tphakala/jev-mcp; single SQLite volume; hf:clduab11/jev-calibration-statistics HTTP 200 was 401; hf:clduab11/jev-calibration-statistics 0 likes sha 9bbe055ee875 mit; sha 9bbe055ee875 was 13f4fa48f2f2; 0.612 against 0.740 *theirs*; missed its main pre-registered bar *theirs*; AUROC 0.899 *theirs*; 9,075 passages 349 questions *theirs*; jev-1.13.0; Gemma 4 ≠ Archer; densify §145 not a sibling first sighting; hf:aimeigaoshou/agent-jev sha 024a68eade83 was 7d433994fbde; hf:aimeigaoshou/agent-jev 0 likes sha 024a68eade83 apache-2.0; verified:false; accuracy 0.7925 ECE 0.1687 Brier 0.0448 *theirs*; same numbers as §146 not a new Harbor; Qwen3-0.6B ≠ Archer; malevrigns/agent-jev ≠ hf:aimeigaoshou/agent-jev; densify §146 not a sibling first sighting; AkashPriyadarshii/jev-seo densify HEAD f42455ac951a was f8cb7c55c356; AkashPriyadarshii/jev-seo 27★ MIT Rust HEAD f42455ac951a README SHA 677171501c8e; README SHA 677171501c8e was e3290fd15add; 27★ was 21★; densify §131 not a sibling first sighting; catalog ≠ endorsement; dtduc-git/jevnav densify HEAD b7a12d2f54ce was 96f5438bea96; dtduc-git/jevnav 1★ Apache-2.0 Py HEAD b7a12d2f54ce README SHA 61ea35cc8f32; page truth not pixels; replay exits 1 with no model call *theirs*; densify §129 not a sibling first sighting; star 0 to 1 is star-noise; dtduc-git/jevnav ≠ pstong216/jevnav-demo; SoundBlaster/SwiftDecision first card revisit tag no prior notes card; SoundBlaster/SwiftDecision 0★ Apache-2.0 Swift HEAD 7af9416e1ac4 README SHA 54ad5d8e4886; Models propose. Application keeps policy; SoundBlaster/SwiftDecision ≠ peterfriese/jev-foundation-models ≠ SoundBlaster/SwiftDecision-Examples; Tongyun1/Jev-in-the-Loop densify HEAD 039c2117f4e3 was a60444c0c268; Tongyun1/Jev-in-the-Loop 0★ MIT Py HEAD 039c2117f4e3 README SHA ffe54ee54576; README SHA ffe54ee54576 was e4ebd224d5f8; Codex prepares inputs Jev picks the next action; operating a browser is not a calibrated Noul; hfnissum-byte/jevmerge code enumerates model picks code gates; hfnissum-byte/jevmerge 1★ NOASSERTION JS HEAD 2b472ca7304b README SHA b32e85e4909c; prakash5284 n=10 is not Harbor; $0.0019 *theirs*; theglitcharchitect/muse-skills shadow mode proceeds anyway; skip-thin Elue-dev/jev_elixir Shoaib-Asghar/jev-probe lvzhaobo/-jev-assayer empty SHA HTTP 409; ravinarayanan89/JevForce HTTP 404; jevonj05/jevonj05 name collision not a decision model; sunmont/pi-jev-dsk-agi acronym expansion is not TypeSafe Jev; hf:opg13/laya about 33 ms *theirs* not Harbor; hf:marcmagn1/jev-alt-systemone-trackio ≠ hf:marcmagn1/jev-alt-systemone-eval; game success ≠ calibrated Noul; does not execute; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; wire-compat ≠ logit-equiv; serving substrate ≠ calibrated replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62/#63/#64/#65/#66/#67/#68/#69/#70/#71/#72; notes.md §148; peterfriese/jev-foundation-models 1★ Apache-2.0 Swift HEAD 27963995965d README SHA b40b836f4396; AbdelStark/abdelstark.github.io 0★ NOASSERTION HTML HEAD bd54fa76189c README SHA 8f7523bcaf57; Alexander-Ollman/laya-ft 0★ NOASSERTION Py HEAD 41f8247c3969 README SHA e97e314c88d5; AustinDKB/grass-optimizer 0★ NOASSERTION Py HEAD 6a0616ab83e1 README SHA e7ee8271da7e; BipinRajC/Jev-api-experiments 0★ NOASSERTION Py HEAD e57a266df0ea README SHA cee6481e2e5b; Codercise/jev-in-practice 0★ MIT TS HEAD 02be666a30ad README SHA 3f0c47161028; DevvGwardo/ghost-route 0★ MIT TS HEAD ca4e40fd94b4 README SHA b4be5c1f6893; Ejokey/lightjev 0★ MIT Py HEAD 921fffb588b9 README SHA 30fa74b9f711; Elue-dev/jev_elixir empty SHA HTTP 409; Georgy-hook/laya-rimworld-director 0★ GPL-3.0 Py HEAD fb82dbf34562 README SHA f25b95e16247; Jorgediamanto/jev-playground 0★ NOASSERTION Py HEAD b3b3d2d8f8db README SHA 7b9972acca45; Lavenir7/Jev2048 0★ NOASSERTION JS HEAD 9e8785ba82e1 README SHA aabbb986b729; Makia9879/pi-jev-router 0★ NOASSERTION TS HEAD 2f6aed131dc8 README SHA 81b43e3994fd; NikHeck/jev-benchmark 0★ NOASSERTION Py HEAD 4997038a2902 README SHA 9e6d3a30ef4b; Renwang-Huang/arbitype 0★ MIT Py HEAD 454cf2c4a345 README SHA ffa11f281a52; Shoaib-Asghar/jev-probe empty SHA HTTP 409; SoundBlaster/SwiftDecision-Examples 0★ MIT HEAD 378c8bc4564f README SHA 05e313ca7b00; Sy3058/jev-evaluate 0★ NOASSERTION Py HEAD 4e6424305b27 README SHA 9a4f7fc26e43; UtpalJayNadiger/find 0★ ISC TS HEAD 44247083ac90 README SHA 670a74958a92; ahtcfg24/codex-speculator 0★ MIT TS HEAD 8496757f0c86 README SHA 6caece2fcb2e; allebee/jevgrep 0★ MIT Py HEAD e7ec44aa801d README SHA 96102d2f6a22; allebee/pytest-jev 0★ MIT Py HEAD b24310cccf43 README SHA 7ab5e2e57a5a; babanomania/linkedin-bullshit-filter 0★ MIT TS HEAD 2838b3c6dc76 README SHA 408ff8140090; bangxiao0927/decidespeak 0★ Apache-2.0 Py HEAD 6558e1a9b157 README SHA d1b95ca6b74b; bitofant/laya 0★ NOASSERTION HEAD f9335cb99e9b README SHA 1a26983aef62; coreywoo27/Jev-Empowered-Qwen-mlx 0★ MIT Py HEAD a14c9b924351 README SHA 2131d40716fc; cornelflorea/jev-test 0★ NOASSERTION TS HEAD 42cadf15cc79 README SHA 35db91381f38; dannyowelch/jev-abstention-checker 0★ NOASSERTION TS HEAD fb2a0afa6220 README SHA acf5b81da07f; dante01yoon/laya-jev-arena 0★ NOASSERTION JS HEAD 4a723c55d31c README SHA a1280d76ddcd; datamonsterr/jev_auto_select_skills 0★ NOASSERTION TS HEAD ffa748ef2cab README SHA 37cd6e7ca9c4; diluteoxygen/JevName 0★ NOASSERTION JS HEAD 08f239452851 README SHA 4598ba81b321; edrache/jevworms 0★ NOASSERTION JS HEAD e79d677c7714 README SHA 098a1d2d3af3; emerson-buoy/jev-ticket-classifier 0★ NOASSERTION TS HEAD a51bd3faf388 README SHA 6a2f242d2409; emlama/jev-mcp 0★ MIT Py HEAD 4c7da93a21be README SHA a258eb52829c; fblissjr/typesafe-experiments 0★ MIT TS HEAD 0d21b21d3c0e README SHA 81d2df816c34; frahlg/laya-ems-test 0★ Apache-2.0 Py HEAD a7f72577dc0e README SHA 35993b958438; hazlema/jev-connect4 0★ MIT TS HEAD be4f9757a820 README SHA bcef5ccd0859; hf:marcmagn1/jev-alt-systemone-trackio 0 likes sha e8fe2df8f29c NOASSERTION; hf:opg13/laya 0 likes sha 99175af5d679 apache-2.0; hfnissum-byte/jevmerge 1★ NOASSERTION JS HEAD 2b472ca7304b README SHA b32e85e4909c; ishantanu/jevtraces 0★ Apache-2.0 Go HEAD 7053acccc254 README SHA f83ca85d1641; jayozer/jevzero 0★ MIT Py HEAD 601228d24a8a README SHA 1a6c376f01ef; jeonck/clinic-checklist 0★ NOASSERTION Py HEAD b693bfa56d42 README SHA e2bb49fe9f2a; jevonj05/jevonj05 0★ NOASSERTION Py HEAD eaf07387d305 README SHA 3743fe2fb819; jordilopez/pi-smart-router 0★ NOASSERTION TS HEAD 2cd38cc56af1 README SHA 89c03c160a85; karanb192/jev-skill-scout 0★ MIT JS HEAD a10b1a1fe71b README SHA 638dd7042894; ljbuturovic/jevgram 0★ NOASSERTION Py HEAD 73185b0df270 README SHA 2af501753734; luisrapalino/jev-smart-bets 0★ MIT TS HEAD a606f2b45195 README SHA 0f3714226f74; lvzhaobo/-jev-assayer empty SHA HTTP 409; lvzhaobo/jev-assayer 1★ NOASSERTION Py HEAD 795031c93e71 README SHA 7fe614bdf174; makiisthenes/JevAIExperimentation 0★ NOASSERTION Py HEAD dae1c2f867d0 README SHA e69de29bb2d1; moelahmady/shunt-jev 0★ MIT TS HEAD 47285110cf2a README SHA 2332516baf23; naiersaidane/jev-demos 0★ NOASSERTION TS HEAD dd8d6fe03da6 README SHA 6a41ac881196; olivere/systemone 0★ MIT Go HEAD fe90e12af0a0 README SHA ede6fced042e; p2kalita/Building-a-Harness-with-Jev-LangChain 0★ NOASSERTION Py HEAD 7c7318ebe703 README SHA 38bc6d9acddc; pavlealeksic/jev-hermes 0★ NOASSERTION Py HEAD ff858e957322 README SHA 2444a463e79c; perezjohn0/jevpav 0★ NOASSERTION HEAD 3185ac2bc377 README SHA ad253f8dfe83; piyushsonawane07/trueKeep 0★ NOASSERTION TS HEAD a072d99e6034 README SHA a217f090c99d; prakash5284/jev-vs-llm-resume-jd-eval 0★ NOASSERTION Py HEAD d9a80a8a00f4 README SHA 06b2104f5b63; pratik-codechef/jev-model 0★ NOASSERTION TS HEAD 5b3a8fb21b50 no README; punitarani/jeve 0★ NOASSERTION Py HEAD c12c66b809da README SHA 631ba86611e4; ravinarayanan89/JevForce HTTP 404; rishhavv/tabjev 0★ MIT JS HEAD 9b4abd1ee7d6 README SHA 15cbe787df05; ruslanlap/jev-gate 0★ MIT Py HEAD 300014a1bdea README SHA 96e31d8dc5d8; sathwikkuncham/laya-snake-arena 0★ Apache-2.0 Py HEAD e7227d789501 README SHA 6947e635bc72; shivpratapsinghpanwar/edgefront 0★ MIT Py HEAD 3b3771d69949 README SHA 7342f40028e9; singhdevhub-lovepreet/firstlight 0★ NOASSERTION TS HEAD 43378a949bce README SHA 5efe948df249; sliday/jev-chess-algo 0★ MIT TS HEAD 4462ace0895b README SHA 24e42556378c; sunmont/pi-jev-dsk-agi 0★ NOASSERTION TS HEAD 2aa1f06e5da6 README SHA b25ef30d534b; theglitcharchitect/muse-skills 0★ MIT Py HEAD f0cc9cc9cea6 README SHA a14927d3b12f; uibuckets/ai-decision-lab 0★ MIT Py HEAD bd237978608f README SHA bc88b74a1ba6; uibuckets/laya-local-service 0★ MIT Py HEAD 7b340cb7ab25 README SHA fbc8e3ca521a; wuxie888/jev-yaba-wechat 0★ MIT Py HEAD b29bd3c42cec README SHA 0744b3dd6268; AkashPriyadarshii/jev-seo 27★ MIT Rust HEAD f42455ac951a README SHA 677171501c8e; dtduc-git/jevnav 1★ Apache-2.0 Py HEAD b7a12d2f54ce README SHA 61ea35cc8f32; SoundBlaster/SwiftDecision 0★ Apache-2.0 Swift HEAD 7af9416e1ac4 README SHA 54ad5d8e4886; Tongyun1/Jev-in-the-Loop 0★ MIT Py HEAD 039c2117f4e3 README SHA ffe54ee54576; hf:aimeigaoshou/agent-jev 0 likes sha 024a68eade83 apache-2.0; hf:clduab11/jev-calibration-statistics 0 likes sha 9bbe055ee875 mit"
)

UNIQ_1256 = (
"Hourly 1256 uniqueness lock: AboveColin/jevclient 2\u2605 MIT Py HEAD a225eadd6eb0 README SHA 5e102cbaa555; typed client is not a replica; wire-compat \u2260 logit-equiv; revsmoke/promptrejectormcp 2\u2605 ISC TS HEAD 752217d26fe9 README SHA dab9c144b5f2; screen is a sensor; application must act; soft judgment is not a sole veto; GodModeAI2025/JevCoreML 0\u2605 Apache-2.0 Swift HEAD cb5c261a1412 README SHA f61f018eee8f; CoreML serving substrate \u2260 calibrated replica; kev \u2260 TypeSafe; Neoo-Blue/vibecheck 0\u2605 Kotlin HEAD cfd6c46899f8 README SHA 718ab09e0442; Jev never writes the reply; RavenValentin/TypeSafe.Jev 0\u2605 MIT C# HEAD 5868475507e5 README SHA 6a4cf10feb67; unofficial .NET client; pin jev-1.13.0; adorosario/jev-rag-claim-verification 0\u2605 MIT Py HEAD 2bdb4d9f3935 README SHA 9b6547d48a39; Jev 1.13.0 balanced acc 73.3 CI [68.5, 77.9] false-verification 23.2% *theirs*; Astra task-optimised 73.8 *theirs*; difference -0.6 points; 187\u00d7 *theirs* not Harbor; bytelabs-oss/clash-jev 1\u2605 MIT Py HEAD 04d420669966 README SHA 31f93aa3c8d7; no trained policy; fallback never logged as Jev; game success \u2260 calibrated Noul; krisitown/jev-router HEAD e2809e09f497 README SHA fa27068d3876; routing \u2260 permission; allebee/jevgrep revisit 0\u2605 MIT Py HEAD 5cebf4c046ac README SHA e30654352e5f; first card revisit tag no prior notes card; default threshold 0.5 still soft; meaning-grep is not a gate; allebee/jevgrep \u2260 Bentlybro/jevgrep \u2260 nassim-arifette/jevgrep \u2260 can1357/jegrep \u2260 uehaj/jev-semgrep; harlanljones/jev-roster-shapes densify HEAD 1d94f9e07fe8 README SHA 4653c58a6459; missing data stays missing; geometry never creates value; 8.8 ms is UI latency not a Jev bench; densify \u00a7134 not a sibling first sighting; ktaletsk/jevframe densify HEAD 16bd3eae69b7 README SHA 6e0a9ef1ba79; no result thresholded or silently renormalized; densify \u00a748 not a sibling first sighting; hfnissum-byte/Hunkpick 77% *theirs* not Harbor; code enumerates model picks code gates; breejesh/gen1 schema-valid is not the same as correct; 100% schema is not calibrated Noul; hf:Cruzex/laya-typed-decisions-smoketest smoke accuracy 0.460 *theirs* not Harbor; reference 0.727 is not comparable; hf:abidlabs/jev-typed-decisions-causal-0.6b quick_eval acc 0.6234 NLL 1.2755 n=640 *theirs*; unre-run report 0.7518 ECE 0.0154 was not re-run; hf:s1lv3rj1nx/openjev-general-lora Banking77 0.728 vs TypeSafe Jev 0.820 *theirs*; hf:libingzheren/Jev-Mem 0.777 LLM-as-a-Judge *theirs* not Harbor; LLM-as-a-Judge \u2260 gold; not the \u00a7134 11.0% figure; smartaces/jev-plays-streetfighter-2 6\u2605 text state not video; catalog \u2260 endorsement; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62/#63/#64/#65/#66/#67/#68/#69/#70/#71/#72/#73/#74; notes.md \u00a7150"
)

UNIQ_1352 = (
"Hourly 1352 uniqueness lock: benjamincanac/tia Jev decides generator writes code owns irreversible; the model never classifies and never sees a probability; dry-run default; human labels stay; Soft judgment never sole veto; MorrisZJ/AnyJev L0 is not calibration; decision.level raw L0 L1; not affiliated with TypeSafe; Qwen3-8B banking20 raw flip 0.227 to 0.077; L0 acc 0.807; L1 ECE 0.100 *theirs*; Jev 1.13.0 acc 0.727 published not rerun; laya-typed-decisions measured 0.768 ECE 0.215 *theirs*; headline 0.766 is a different author sentence; do not average 0.768 and 0.766; MorrisZJ/AnyJev \u2260 hwfengcs/any2jev; Qwen3 \u2260 Archer; Qwen2.5 \u2260 Archer; andududu/jeview answers nothing itself; key stored as plain text; a live view is not a calibration claim; satiricalguru/Fast-Jev-Agents never summarizes or rewrites text; pinned text stays; 100 ms to 1 s *theirs*; 50 to 80% *theirs*; README badge 50/50 *theirs* not Harbor; Alberto-Codes/judgevet noul carries no confidence; score is continuous; jev-latest returned jev-1.13.0; later sentence every answer carries a confidence is their tension; wire-compat \u2260 logit-equiv; Alberto-Codes/judgevet \u2260 jkudish/jev-mcp; Emlembow/jevgraph 63.9% to 81.8% *theirs*; unanswerable still returns; ranking \u2260 an answer; Ivanovskyi/typesafe-ai-gateway 0.75 still soft; MANUAL_REVIEW; routing \u2260 permission; abe17124/jev-laya-chess-bench legal UCI; no W/D/L table; do not invent scores; game success \u2260 calibrated Noul; GitHub license null README Apache-2.0 *theirs*; adelaserna82/jev-model-net-sdk unofficial simulation first; planned NuGet names are not a published contract; adelaserna82/jev-model-net-sdk \u2260 JabbaKadabra/SystemOneDotNet \u2260 saibimajdi/typesafeai-dotnet-sdk; karozi/awesome-jev-resources catalog \u2260 endorsement; karozi/awesome-jev-resources \u2260 ham-zax/awesome-jev; hf:abidlabs/jev-typed-decisions-causal-0.6b first card revisit tag no prior notes card; prior_sha null; sha 440a8931d8db; quick_eval acc 0.6234 NLL 1.2755 n=640 *theirs*; do not quote 0.7518; ECE 0.0154 not re-run here; restricted letter CE \u2260 calibrated Noul; LoRA \u2260 RLCD replica; Qwen/Qwen3-0.6B-Base \u2260 Archer; Qwen3-0.6B \u2260 Archer; hf:abidlabs/jev-typed-decisions-demo is the Gradio not the weights; devanshbatham/nyx 2,277 frozen requests *theirs*; Qwen3.5-4B \u2260 Archer; latency clocks are different operating points; harrymunro/jev-laya-benchmark 92.9% vs 65.3% *theirs* not Harbor; mbburabak/jev-safety-benchmark 12,254 live calls *theirs*; HateCheck Shieldstral cell empty; hf:Wouze/laya-ara MASSIVE intent 0.816 scenario 0.865 XNLI-ar 0.723 OSACT4-A 0.862 *theirs*; top-1 among k\u226412 not corpus nDCG@10; hf:Wouze/laya-ara-rag \u2260 hf:Wouze/laya-ara; hf:juspay/jev-trained Qwen3.6 \u2260 Archer; inference false; serving substrate \u2260 calibrated replica; MatteoGauthier/laya-onnx export parity is not Harbor; zerowidth-ai/shims-sdk example 0.86 is a README illustration; encoder class member not Jev replica; skip-thin canok07/jev-router fedorpark/jev-inbox-lab rscottstevens-byte/jev tgallice/jev-go empty SHA HTTP 409; codeJRV/openjev-hermes-plugin HTTP 404; sed-ndi/test-jev README HTTP 404; canok07/jev-router \u2260 gargpratyush/jev-router; codeJRV/openjev-hermes-plugin \u2260 Zefan-Cai/Open-Jev; does not execute; routing \u2260 permission; *theirs* not Harbor; SHA move is not a replica; Skip Archer; invented_signal: false; Parent merges only after ADV_PASS; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62/#63/#64/#65/#66/#67/#68/#69/#70/#71/#72/#73/#74/#75/#76; glance §147, hourly 1203 §148, lev §149, and hourly 1256 §150 are on main; this fold is §151 only; notes.md \u00a7151; benjamincanac/tia 3\u2605 NOASSERTION TS HEAD fb1f3fc5a08b README SHA 8e72540ed19d; MorrisZJ/AnyJev 1\u2605 Apache-2.0 Py HEAD 39612ea0dbad README SHA 13000620bb24; andududu/jeview 1\u2605 MIT JS HEAD 313fb25fdbb6 README SHA b11e9eecafc9; karozi/awesome-jev-resources 1\u2605 NOASSERTION HEAD 6fc7b2bbb484 README SHA e43f103fa149; satiricalguru/Fast-Jev-Agents 1\u2605 MIT TS HEAD d2a2cf0c27f9 README SHA aec74c017e2a; 247arjun/JevPlayground 0\u2605 MIT JS HEAD 7eb341853c14 README SHA 5771aae9f263; Alberto-Codes/judgevet 0\u2605 MIT Py HEAD 8baf10bdb9a9 README SHA 3534d0bca3bf; DanM3rcurius/po-radar 0\u2605 Apache-2.0 Py HEAD cd367c978747 README SHA 6d6f0e9423b9; Emlembow/jevgraph 0\u2605 NOASSERTION JS HEAD 9b76d0dfaa03 README SHA 5a292aa627df; Faresabdelghany/jev-browser-test 0\u2605 NOASSERTION Py HEAD 0ced4fc4d510 README SHA a892d7502e65; Ivanovskyi/typesafe-ai-gateway 0\u2605 NOASSERTION Java HEAD b7a07bab1f47 README SHA 57c4b2ea4d00; MatteoGauthier/laya-onnx 0\u2605 Apache-2.0 TS HEAD e2578f5eb4a9 README SHA 1a2d0d6ab6b5; SAITS-Swiss-AI-Tech-Services/jev-mcp 0\u2605 MIT Py HEAD b63834b57c47 README SHA 803d4028db3f; SimonKaran13/DOOMJEV 0\u2605 NOASSERTION HEAD 57335641e9dc README SHA aa909c20f1ca; TokyoHunter/jev-animal-finder 0\u2605 NOASSERTION HTML HEAD 039eebdc3d93 README SHA 0b3f142ea401; abe17124/jev-laya-chess-bench 0\u2605 NOASSERTION Py HEAD 25cb0b542c33 README SHA 6ae7b84d046c; adelaserna82/jev-model-net-sdk 0\u2605 MIT C# HEAD adfd02bff8b6 README SHA 0c134d84847a; aitofy-dev/jev-awesome-skills 0\u2605 MIT TS HEAD 544f447cc1f2 README SHA 4358da54ba3f; aleksvega/jev-skill-router 0\u2605 MIT JS HEAD e360f3ff5b13 README SHA 5a8868bfd7bb; alibowbow/jev 0\u2605 NOASSERTION JS HEAD 6865532303fe README SHA 405d7aa47ef4; anchorshell/relay 0\u2605 NOASSERTION Go HEAD fb9c68c44f10 README SHA 8abce1477026; ankurlamichhane90/mac-voice-assistant 0\u2605 MIT Py HEAD 9616c9e0d3ba README SHA 129f0a1fc6b9; canok07/jev-router empty SHA HTTP 409; codeJRV/openjev-hermes-plugin HTTP 404; d-callan/bionym 0\u2605 NOASSERTION Py HEAD 50c3f20d8903 README SHA 9f08f9b86509; deemkeen/jevgeni 0\u2605 NOASSERTION TS HEAD 45e4739961e5 README SHA a1aa02587139; devanshbatham/nyx 0\u2605 Apache-2.0 Py HEAD f54400f5b3c7 README SHA 685e5326d87e; diluteoxygen/JevMood 0\u2605 NOASSERTION JS HEAD 2f1d518c9bb7 README SHA 46dfefe14ee8; emipaz/jev 0\u2605 NOASSERTION Py HEAD 24ebc8f4aa96 README SHA 4ba7873f5fef; fedorpark/jev-inbox-lab empty SHA HTTP 409; fredp74/calibrus 0\u2605 MIT Py HEAD 99857011694c README SHA 996140762c25; gbesse/bevy-jev 0\u2605 MIT Rust HEAD 7c2d856c5a4f README SHA 6968b772a169; gbesse/figma-jev-review 0\u2605 MIT TS HEAD 5c2bd09b869e README SHA 94b9f2259e4a; gbesse/jev-premiere-markers 0\u2605 MIT JS HEAD 0b86a810aea9 README SHA 1fdbe504ca02; gbesse/jev-unreal-statetree 0\u2605 MIT C++ HEAD 7a29d778b02e README SHA 6d9a0daf14a8; ham-zax/awesome-jev 0\u2605 NOASSERTION Py HEAD 2feee30987c1 README SHA b2f54fb300b5; harrymunro/jev-laya-benchmark 0\u2605 MIT Py HEAD 0f977d20641e README SHA f8e5830655b1; hf:Wouze/laya-ara 0 likes sha e6de79f74226 other; hf:Wouze/laya-ara-rag 0 likes sha c6a917f43fee apache-2.0; hf:abidlabs/jev-typed-decisions-causal-0.6b 0 likes sha 440a8931d8db apache-2.0; hf:abidlabs/jev-typed-decisions-demo 0 likes sha c03353154801 apache-2.0; hf:akhilaaa3/openjev-train 0 likes sha 91c04ef1cf2e other; hf:juspay/jev-trained 0 likes sha fc03bb699dbd apache-2.0; hf:rarha/laya-onnx 0 likes sha b5eb4528c941 apache-2.0; htpu/mailaya 0\u2605 Apache-2.0 JS HEAD 30b97f46b419 README SHA fe273b722191; ilyaryabchinski/jevss 0\u2605 NOASSERTION Py HEAD 4fd5fec4dc9f README SHA 1ae319334fff; individual11/jev-feedbin-filter 0\u2605 NOASSERTION TS HEAD 432c89194fa2 README SHA 2f4cf5a66173; jpvajda/jev-demo 0\u2605 NOASSERTION TS HEAD 6e8d6da7c083 README SHA d891f3d4a17c; kevinaaaquil/jev-rubix 0\u2605 NOASSERTION JS HEAD 1dbab869b1b4 README SHA eca7d0acdc45; koolerkx/vibe-discord-bot-jev 0\u2605 NOASSERTION TS HEAD 65cb426d514a README SHA 4372e4cd36c3; marcelormendes/diffninja 0\u2605 MIT TS HEAD b53d5427e0ad README SHA 513dbfeaea61; mbburabak/jev-safety-benchmark 0\u2605 MIT Py HEAD 1bf1eacfc37e README SHA 8b4ae44b8b96; mwatkins03-netizen/The-Complaint-Atlas-Fable-5 0\u2605 NOASSERTION JS HEAD 296f7bfeb9be README SHA 4d5333f02168; nautahakk/jev-codex-router 0\u2605 MIT JS HEAD 49d75e9230ce README SHA f51077559a4d; pavan142/jev-experiments 0\u2605 NOASSERTION TS HEAD 92f96ac4023d README SHA 69a29f87649d; pedro-pscunha/guideme-python 0\u2605 Apache-2.0 Py HEAD 9a9d4d574de7 README SHA e2fc4d164b29; photuris/overseer-judge 0\u2605 MIT Go HEAD 9bdd94ada9b1 README SHA 30a2e39174df; qasimhammad1/applyguard 0\u2605 MIT TS HEAD 28897637e064 README SHA 8b5cdfbead1c; rscottstevens-byte/jev empty SHA HTTP 409; sed-ndi/test-jev 0\u2605 NOASSERTION HTML HEAD ccde5849b930 README HTTP 404; tgallice/jev-go empty SHA HTTP 409; vaibhavgupta5/Jev-Email-Classifier 0\u2605 NOASSERTION JS HEAD 92d9abf9f97b README SHA 66bb426ffe6e; vishalyadav28/resume-jev-match 0\u2605 NOASSERTION Py HEAD e78a1ec2d2c8 README SHA f1def63ffeb0; yangda611/omarchy-smart-paste 0\u2605 MIT Shell HEAD a55dabf2ba59 README SHA 54d4a399ca1b; zerowidth-ai/shims-sdk 0\u2605 Apache-2.0 JS HEAD ae1bf6afa440 README SHA 16f2357b158d"
)

UNIQ_RYANA = (
"User-provided ryana/jevify uniqueness lock: ryana/jevify prompt-only design-investigation aid; Prompts to jev-ify your projects; description_hash 0e539a1e865b; live REST stargazers_count 6; forks_count 0; license null; no LICENSE file; no releases; release_tag null; language null; topics empty; GitHub id 1376670432; size 3; README blob 7567 bytes; HEAD 87a9ef3674f111c74bb33cccd3bfa56bd0c4a15c; README SHA 227e2324818375e1f73d044af6a56a5b933c496b; created 2026-09-19T03:16:52Z; pushed 2026-09-19T03:18:52Z; single commit docs: add Jev project investigation prompt by Ryan Angilly (ryana); root is README-only; Paste the prompt below into your coding agent while it is working in your project; architectural deductions are not verified implementation details; Separate vendor claims, independently measured results, and your own hypotheses; Questions in one request are evaluated independently; application code combines their answers; Treat returned probabilities as signals whose calibration needs testing on our workload; Continue the analysis without inventing results; Do not assume that more questions are free; prompt is not a runtime gate; not a decision model; not a serving head; not a converter; not an agent skill package; not an Augustus skill; not a TypeSafe product; soft scores ≠ hard gates; catalog ≠ endorsement; invented_signal false; ryana/jevify ≠ altryne/jevify ≠ fidecastro/jevify ≠ Mintzs/jevify ≠ gulagala001/jevify ≠ uspraveen/Jevify ≠ apurv101/jevify ≠ arzkr/jevify-demo ≠ alexwestco/llm-to-jev; altryne/jevify is an agent skill; fidecastro/jevify serves LLMs as a Jev-like endpoint; Mintzs/jevify is an inference engine (optional CUDA graphs off by default); gulagala001/jevify is a DSH plugin; uspraveen/Jevify turns an open LLM into a System One shape; apurv101/jevify empty repo HTTP 409; arzkr/jevify-demo is a demo namesake; alexwestco/llm-to-jev stays notes.md §118 heuristic converter; first dedicated card notes.md §152; do not reclaim §147 glance §148 1203 §149 lev §150 1256 §151 1352; composition 809-820; findings batch #132; glance §147, hourly 1203 §148, lev §149, hourly 1256 §150, and hourly 1352 §151 are on main; this fold is §152 only; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62/#63/#64/#65/#66/#67/#68/#69/#70/#71/#72/#73/#74/#75/#76/#77; does not bump 0.5.0 or 0.5.1; notes.md §152"
)

UNIQ_1454 = (
"Hourly 1454 uniqueness lock: NobleSpartan6/otto Jev chooses concrete actions; model score not a guarantee; fill-a-form is exact and issues no model call; stop cannot undo an input already delivered; published typesafe-computer-use figures are not Otto benchmarks; nourhelmi/pi-jev-compaction 0.25 still soft; API error timeout or invalid answer clears nothing new; jev_read does not rerun; LiamSherline/jev-lead-scorer nothing sends itself; P near 0.5 written NULL; about $0.042 per million input tokens is a pricing illustration *theirs*; MatteoGauthier/laya-portable same answers is their claim; export parity is not Harbor; MatteoGauthier/laya-portable \u2260 MatteoGauthier/laya-onnx; strombolini/Armada Codiv OpenJev \u2260 TypeSafe; ranking \u2260 calibration; example 99% is an illustration; Yushenggg/zero-shot-classifier open recreation \u2260 calibrated replica; Qwen3-4B \u2260 Archer; densify \u00a7145 not a sibling first sighting; danielamitay/swev MLX was CoreML; densify \u00a7132 not a sibling first sighting; serving substrate \u2260 calibrated replica; GaNotchVFX/jev-benchmarks 84.0% *theirs*; kokuren333/jev-jmle-benchmark 88.58% *theirs*; hosamsh/jev-mind2web one Mind2Web shard; 79.2% *theirs* on a described element; test splits are not run; Jevals/Jevals 1/28 of the price *theirs*; piyushpawar54/system-one-bench n=40 26/40 ECE 0.3292 *theirs*; 0.94 when right 0.93 when wrong *theirs*; n=40 is not Harbor; hf:lostargon/Tiny-Jev in-distribution ECE 0.004 *theirs* is not held-out ECE 0.299 *theirs*; fitted public rows are not zero-shot; Gemma 4 \u2260 Archer; hf:rarha/laya-onnx sha b5eb4528c941 unchanged; likes 0 to 1 is star-noise; densify \u00a7151 not a sibling first sighting; TokyoHunter/jev-animal-finder SHA moved; aleksvega/jev-skill-router SHA unchanged e360f3ff5b13; routing \u2260 permission; a scan is not a grant; Soft judgment never sole veto; game success \u2260 calibrated Noul; wire-compat \u2260 logit-equiv; catalog \u2260 endorsement; *theirs* not Harbor; SHA move is not a replica; skip-thin xuan7zhang/jev-toolspace empty SHA HTTP 409; DarkWanderer/laya README HTTP 404; Skip Archer; invented_signal: false; Parent merges only after ADV_PASS; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62/#63/#64/#65/#66/#67/#68/#69/#70/#71/#72/#73/#74/#75/#76/#77/#78; ryana/jevify \u00a7152 are on main; this fold is \u00a7153 only; composition 821-836; findings batch #133; notes.md \u00a7153; B0mbxstiC/jev-chatgpt 0\u2605 NOASSERTION TypeScript HEAD ef144d737c27 README SHA 6e182e06d11d; DarkWanderer/laya 0\u2605 NOASSERTION Python HEAD 60ef215ffbf5 README HTTP 404; Emlembow/jev-graph-search 0\u2605 MIT JavaScript HEAD dc32a9514aba README SHA 18c560aac436; FYIsoft/Microsoft.Extensions.AI.Providers 0\u2605 MIT C# HEAD 82cabf61db28 README SHA c9967b714c75; GaNotchVFX/jev-benchmarks 0\u2605 NOASSERTION Python HEAD 794e8c74bec8 README SHA f56b4c010006; GreenKeewi/jev-x-scanner 0\u2605 NOASSERTION JavaScript HEAD b5c14e25e81e README SHA 7718cc27a568; HCTDIP/jevkit 0\u2605 NOASSERTION None HEAD cc1e6a5f02de README SHA 3057bd01f157; JKasteele/mail-safety-lab 0\u2605 MIT Python HEAD e57958e3429e README SHA 817bb888cecb; Jevals/Jevals 0\u2605 NOASSERTION None HEAD 15c062817b92 README SHA a65da0c19ccc; Jevals/jevals-data 0\u2605 CC-BY-4.0 None HEAD 21bb47b72814 README SHA a441666c5ad1; JohnCari/of-record 0\u2605 NOASSERTION TypeScript HEAD 17e82e08f607 README SHA 372ce6a6c637; Klikwork/feedlens 0\u2605 MIT JavaScript HEAD d6da9a797344 README SHA 336549d7020c; KushagraBharti/The-JEV-LLM 0\u2605 NOASSERTION None HEAD 46ff212a8db1 README SHA 4b9965fcc3c9; LiamSherline/jev-lead-scorer 1\u2605 MIT Python HEAD cf7be6176927 README SHA 7daec2fed256; MatteoGauthier/laya-portable 1\u2605 Apache-2.0 TypeScript HEAD c7ed6bbbc866 README SHA d74c3b52e106; Maxi91f/jev_testing 0\u2605 MIT Python HEAD c5ac469ec84e README SHA fd3ada2bac7b; MstyAI/laya-mlx-swift 0\u2605 Apache-2.0 Swift HEAD 284d426dbb68 README SHA d375c3061904; NobleSpartan6/otto 4\u2605 MIT TypeScript HEAD 80681ef1bc11 README SHA f2a0ba922276; OpenScribbler/semantic-style-lab 0\u2605 MIT HTML HEAD 5e68817a829a README SHA fb530afa79b3; PAUNYWSE34/-Your-Payment-Receipt-Details-jevans4824-aol.com--7qlmt3wo 0\u2605 NOASSERTION DIGITAL Command Language HEAD 3e9c30709d08 README HTTP 404; Postman-Devrel/JevPong 0\u2605 MIT TypeScript HEAD 1541b57cc8f9 README SHA 121ce430ac9a; RastislavDujava/jev-classification-prompting 0\u2605 MIT Python HEAD dfce3d631219 README SHA af1e23ad3b86; SebasPinto/moviejev 0\u2605 MIT Python HEAD bee3433c057d README SHA 36e9c407d16b; Sourav19o7/jev-examples 0\u2605 NOASSERTION Python HEAD d7bb723db51f README HTTP 404; Spray2/JEVangelion 0\u2605 NOASSERTION Python HEAD 90541b3c0319 README SHA deff29f31db6; SuperInstance/substrate-gan 0\u2605 NOASSERTION TypeScript HEAD 5c24df2a5766 README SHA 7aa952c738ae; TokyoHunter/jev-animal-finder 0\u2605 NOASSERTION HTML HEAD c00c3ab9b754 README SHA ed86e368bd69; Yaro60/jev-research 0\u2605 NOASSERTION JavaScript HEAD 9fe2f3ab82be README SHA c02d1bf963c2; Yushenggg/zero-shot-classifier 1\u2605 MIT Python HEAD 969d8f098423 README SHA b10879ce0c0b; ajmeese7/jev-chess 1\u2605 BSD-3-Clause TypeScript HEAD fbce02e1055b README SHA 5abd840cc46d; aleksvega/jev-skill-router 0\u2605 MIT JavaScript HEAD e360f3ff5b13 README SHA 5a8868bfd7bb; altanapps/security-sandbox-jev 0\u2605 MIT Python HEAD 3d4b20aa024c README SHA 45ba01f3191e; asynq-io/system-one 0\u2605 MIT Python HEAD 15cbeb7ccc85 README SHA 45d08b1be22e; baldpanda/jev-sandbox 0\u2605 NOASSERTION Jupyter Notebook HEAD 48427189de99 README SHA 923731c658df; cdeguet/jev-tetris 0\u2605 MIT Python HEAD 6ccc5e547352 README SHA f338a35174e4; cedrecs/jev-stories 0\u2605 MIT JavaScript HEAD 34fbe3a8478f README SHA 9bd0ff871cba; cohenom/laya-snake 0\u2605 NOASSERTION HTML HEAD b67174791011 README SHA 094ffcc612df; danielamitay/swev 1\u2605 MIT Swift HEAD 7ad6ddbfb363 README SHA 569b5506edb8; dperezcabrera/jev-chess 0\u2605 GPL-3.0 JavaScript HEAD 87073d612222 README SHA 1d73415bcad3; echohello-dev/jev-mcp-server 0\u2605 MIT TypeScript HEAD e47c20898ed5 README SHA cb287a94fa60; eriestra/blockly-jev 0\u2605 MIT TypeScript HEAD 74e412be1faa README SHA 04495887c4a2; fcjr/jev-first-search 0\u2605 MIT JavaScript HEAD d02d2f648d37 README SHA 1b146dbd8065; fullcolorcoder/reflex-jev 0\u2605 NOASSERTION TypeScript HEAD ed4461b05007 README SHA 4969bf97f9b5; gbesse/blender-jev-review 0\u2605 MIT Python HEAD 6dbc03f2fe4f README SHA 7178aaa0eb53; gbesse/jev-obs-cues 0\u2605 MIT Python HEAD 89d906685ec7 README SHA 0d9ef68d7e0e; gbesse/jev-vscode-review 0\u2605 MIT TypeScript HEAD d7f689a389bf README SHA b4b8fa5d1365; gbesse/roblox-jev-studio 0\u2605 MIT Lua HEAD 2b600272a1ca README SHA 3ec1e24e8f59; glebmish/jev-watchdog 0\u2605 MIT Python HEAD 50023b0b8c45 README SHA 9c10538d7fd3; gnapse/jev 0\u2605 MIT TypeScript HEAD a212d875135c README SHA 614f78028698; gopaljigaur/decide 0\u2605 NOASSERTION None HEAD d11f10969613 README HTTP 404; haystackeditor/stop-rules 0\u2605 MIT JavaScript HEAD 915b58aced41 README SHA 07bd38a27f7e; heyaozh/jev-rust-crate 0\u2605 NOASSERTION Rust HEAD e04bd414c838 README SHA 2cfc33cfe5ea; hf:juspay/jev-one 0 likes sha 4de0db772d71 apache-2.0; hf:lostargon/Tiny-Jev 2 likes sha 7b6792156bb6 apache-2.0; hf:marcmagn1/jev-08b-typed-r1 0 likes sha 5d5db74f33bc NOASSERTION README HTTP 404; hf:rarha/laya-onnx 1 likes sha b5eb4528c941 apache-2.0; hosamsh/jev-mind2web 0\u2605 NOASSERTION Python HEAD 0c08c9a92a38 README SHA 8f4d60c4f86a; jonkthomas/jev-shadow 0\u2605 MIT JavaScript HEAD 0544e43e029f README SHA 30ae59cc9ce4; jose-salcedo-sp/recall 0\u2605 NOASSERTION HTML HEAD 061a53b2d024 README HTTP 404; kennedy-f/hermes-jev-decision-layer 0\u2605 MIT Python HEAD f6ab8b8856c1 README SHA c8f6607df02e; kokuren333/jev-jmle-benchmark 0\u2605 MIT Python HEAD 88b6c1b1aa75 README SHA d53e6e3dc48d; koz/anti-dead-internet 0\u2605 MIT TypeScript HEAD edd38a5ac70f README SHA f76d073abc9c; layareddy10-source/layareddy10-source.github.io 0\u2605 NOASSERTION HTML HEAD f365388c355e README HTTP 404; maxvaega/gmail-jev-guard 0\u2605 NOASSERTION JavaScript HEAD ac4a07b4673f README SHA 102954def6db; mingleiw/jev-oncall 0\u2605 NOASSERTION HTML HEAD fdb068d0ac8a README SHA 6b6c77eb5f20; mraad/feln-laya 0\u2605 NOASSERTION Python HEAD e6b4ca939d47 README SHA 978e6d71e64a; nourhelmi/pi-jev-compaction 2\u2605 MIT TypeScript HEAD 103c0b006f33 README SHA 5061f0f56056; piyushpawar54/system-one-bench 0\u2605 NOASSERTION Python HEAD 539505a03704 README SHA ed776e3b8b7f; ppradyoth/jev-guard 0\u2605 MIT Python HEAD 63becd00cc57 README SHA de0582c8555c; pratikgorji/jev-guide 0\u2605 NOASSERTION HTML HEAD 5d1729cad434 README SHA 0456a9c795b6; rawwerks/one-system 0\u2605 MIT TypeScript HEAD 7a1fd8253ca6 README SHA ea10bf3eeedd; sriharsha8991/JEV-use_cases 0\u2605 NOASSERTION None HEAD 8f1ce2a8dc9b README SHA 03e0fa28cd98; strombolini/Armada 1\u2605 NOASSERTION Swift HEAD dc3056dfa327 README SHA 52aabecafa9d; sunnyspot114514/jevnet-runtime 0\u2605 Apache-2.0 Python HEAD 028e7835cb1a README SHA 2a8f9a629b99; suyash-lyzr/jev-typesafe 0\u2605 NOASSERTION TypeScript HEAD dfa949b7eab8 README SHA fcfb27b46f71; v0idhrt/lyra-n 0\u2605 MIT TypeScript HEAD ce6a49952c0a README SHA e6fdd010baec; xosi/laya 0\u2605 Apache-2.0 Python HEAD 21ee0c0b73f3 README SHA a91d4052686b; xuan7zhang/jev-toolspace empty SHA HTTP 409"
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
        if UNIQ_1110 not in body:
            failed.append(f"1110 lock missing as one substring: {rel}")
        if UNIQ_GLANCE not in body:
            failed.append(f"glance lock missing as one substring: {rel}")
        if UNIQ_1203 not in body:
            failed.append(f"1203 lock missing as one substring: {rel}")
        if UNIQ_1256 not in body:
            failed.append(f"1256 lock missing as one substring: {rel}")
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
    if "same-species serving not an 18th scoring row" not in UNIQ_1110:
        failed.append("UNIQ_1110 missing same-species lock")
    if "act head untrained do not gate on it" not in UNIQ_1110:
        failed.append("UNIQ_1110 missing act-head lock")
    if "JSON chat ≠ calibrated Noul" not in UNIQ_1110:
        failed.append("UNIQ_1110 missing JSON chat lock")
    if "copied kev numbers are not a musubi bench" not in UNIQ_1110:
        failed.append("UNIQ_1110 missing musubi copy lock")
    if "ranking ≠ calibration" not in UNIQ_1110:
        failed.append("UNIQ_1110 missing ranking lock")
    if "densify §142 not a sibling first sighting" not in UNIQ_1110:
        failed.append("UNIQ_1110 missing laya-drift densify lock")
    if "densify §139 not a sibling first sighting" not in UNIQ_1110:
        failed.append("UNIQ_1110 missing decision-workbench densify lock")
    if "densify §143 not a sibling first sighting" not in UNIQ_1110:
        failed.append("UNIQ_1110 missing SystemOneDotNet densify lock")
    if "densify §145 not a sibling first sighting" not in UNIQ_1110:
        failed.append("UNIQ_1110 missing §145 densify lock")
    if "harness not weights" not in UNIQ_GLANCE:
        failed.append("UNIQ_GLANCE missing harness lock")
    if "soft scores ≠ hard gates" not in UNIQ_GLANCE:
        failed.append("UNIQ_GLANCE missing soft-score lock")
    if "notes.md §147" not in UNIQ_GLANCE:
        failed.append("UNIQ_GLANCE missing §147")
    if "yoheinakajima/glance" not in UNIQ_GLANCE:
        failed.append("UNIQ_GLANCE missing catalog id")
    if "OpenJev v2 ≠ Zefan-Cai/Open-Jev ≠ razorback16/openjev ≠ IamBusy/OpenJev-Vision" not in UNIQ_GLANCE:
        failed.append("UNIQ_GLANCE missing four-way OpenJev namesake")
    if "AlexWortega/openjev" not in UNIQ_GLANCE:
        failed.append("UNIQ_GLANCE missing OpenJev v2 Hub id")
    if "do not mint a sibling card" not in UNIQ_GLANCE:
        failed.append("UNIQ_GLANCE missing no-sibling-card lock")
    if "wire lock not OpenJev v2 identity" not in UNIQ_GLANCE:
        failed.append("UNIQ_GLANCE missing wire-not-identity lock")
    if "jsondigits" not in UNIQ_GLANCE or "ens4d" not in UNIQ_GLANCE:
        failed.append("UNIQ_GLANCE missing jsondigits/ens4d pass lock")
    if "do not say zero-shot or no training" not in UNIQ_GLANCE:
        failed.append("UNIQ_GLANCE missing fitted-readout caveat")
    if "Platt" not in UNIQ_GLANCE:
        failed.append("UNIQ_GLANCE missing Platt map")
    if "Q-SiT-mini" not in UNIQ_GLANCE:
        failed.append("UNIQ_GLANCE missing Q-SiT-mini rating limit")
    if "do not quote interim KADID numbers" not in UNIQ_GLANCE:
        failed.append("UNIQ_GLANCE missing KADID non-quote lock")
    if "#70" not in UNIQ_1110:
        failed.append("UNIQ_1110 missing HARD RULE #70")
    if "Swift 6 bridge into Apple Foundation Models" not in UNIQ_1203:
        failed.append("UNIQ_1203 missing Swift bridge lock")
    if "Never embed API keys" not in UNIQ_1203:
        failed.append("UNIQ_1203 missing API key lock")
    if "false alarms 24.8% to 65.2% to 47.2% *theirs*" not in UNIQ_1203:
        failed.append("UNIQ_1203 missing false-alarm lock")
    if "Soft judgment never sole veto" not in UNIQ_1203:
        failed.append("UNIQ_1203 missing sole-veto lock")
    if "exit code 2 is code" not in UNIQ_1203:
        failed.append("UNIQ_1203 missing exit-code lock")
    if "0.612 against 0.740 *theirs*" not in UNIQ_1203:
        failed.append("UNIQ_1203 missing calibration lock")
    if "verified:false" not in UNIQ_1203:
        failed.append("UNIQ_1203 missing verified:false lock")
    if "densify §145 not a sibling first sighting" not in UNIQ_1203:
        failed.append("UNIQ_1203 missing §145 densify lock")
    if "densify §146 not a sibling first sighting" not in UNIQ_1203:
        failed.append("UNIQ_1203 missing §146 densify lock")
    if "densify §131 not a sibling first sighting" not in UNIQ_1203:
        failed.append("UNIQ_1203 missing §131 densify lock")
    if "densify §129 not a sibling first sighting" not in UNIQ_1203:
        failed.append("UNIQ_1203 missing §129 densify lock")
    if "#72" not in UNIQ_1203:
        failed.append("UNIQ_1203 missing HARD RULE #72")
    if "soft judgment is not a sole veto" not in UNIQ_1256:
        failed.append("UNIQ_1256 missing soft-judgment lock")
    if "wire-compat ≠ logit-equiv" not in UNIQ_1256:
        failed.append("UNIQ_1256 missing wire-compat lock")
    if "schema-valid is not the same as correct" not in UNIQ_1256:
        failed.append("UNIQ_1256 missing schema-valid lock")
    if "game success ≠ calibrated Noul" not in UNIQ_1256:
        failed.append("UNIQ_1256 missing game-success lock")
    if "routing ≠ permission" not in UNIQ_1256:
        failed.append("UNIQ_1256 missing routing lock")
    if "serving substrate ≠ calibrated replica" not in UNIQ_1256:
        failed.append("UNIQ_1256 missing serving-substrate lock")
    if "densify §134 not a sibling first sighting" not in UNIQ_1256:
        failed.append("UNIQ_1256 missing §134 densify lock")
    if "densify §48 not a sibling first sighting" not in UNIQ_1256:
        failed.append("UNIQ_1256 missing §48 densify lock")
    if "allebee/jevgrep ≠ Bentlybro/jevgrep" not in UNIQ_1256:
        failed.append("UNIQ_1256 missing jevgrep namesake")
    if "0.5 still soft" not in UNIQ_1256:
        failed.append("UNIQ_1256 missing 0.5 still soft")
    if "77% *theirs*" not in UNIQ_1256:
        failed.append("UNIQ_1256 missing 77% lock")
    if "0.460" not in UNIQ_1256 or "0.6234" not in UNIQ_1256 or "0.7518" not in UNIQ_1256:
        failed.append("UNIQ_1256 missing smoke/quick_eval numbers")
    if "0.728" not in UNIQ_1256 or "0.820" not in UNIQ_1256:
        failed.append("UNIQ_1256 missing Banking77 pair")
    if "0.777" not in UNIQ_1256 or "LLM-as-a-Judge" not in UNIQ_1256:
        failed.append("UNIQ_1256 missing Jev-Mem judge lock")
    if "23.2%" not in UNIQ_1256 or "187×" not in UNIQ_1256:
        failed.append("UNIQ_1256 missing claim-bench lock")
    if "*theirs* not Harbor" not in UNIQ_1256:
        failed.append("UNIQ_1256 missing not Harbor")
    if "#73" not in UNIQ_1256 or "#74" not in UNIQ_1256:
        failed.append("UNIQ_1256 missing HARD RULE #73/#74")
    if ("open #" + "74") in UNIQ_1256:
        failed.append("UNIQ_1256 still claims the pre-merge #74 push ban")
    if "notes.md §150" not in UNIQ_1256:
        failed.append("UNIQ_1256 missing §150")
    if "notes.md §149" in UNIQ_1256:
        failed.append("UNIQ_1256 claims lev §149")
    if "notes.md §148" in UNIQ_1256:
        failed.append("UNIQ_1256 still claims §148")

    if "Jev decides generator writes code owns irreversible" not in UNIQ_1352:
        failed.append("UNIQ_1352 missing tia irreversible lock")
    if "never classifies" not in UNIQ_1352:
        failed.append("UNIQ_1352 missing never classifies lock")
    if "L0 is not calibration" not in UNIQ_1352:
        failed.append("UNIQ_1352 missing L0 lock")
    if "0.227 to 0.077" not in UNIQ_1352:
        failed.append("UNIQ_1352 missing flip lock")
    if "L1 ECE 0.100" not in UNIQ_1352:
        failed.append("UNIQ_1352 missing L1 ECE lock")
    if "answers nothing itself" not in UNIQ_1352:
        failed.append("UNIQ_1352 missing jeview lock")
    if "never summarizes" not in UNIQ_1352:
        failed.append("UNIQ_1352 missing verbatim lock")
    if "noul carries no confidence" not in UNIQ_1352:
        failed.append("UNIQ_1352 missing noul confidence lock")
    if "63.9% to 81.8%" not in UNIQ_1352:
        failed.append("UNIQ_1352 missing recall lock")
    if "0.75 still soft" not in UNIQ_1352:
        failed.append("UNIQ_1352 missing threshold lock")
    if "legal UCI" not in UNIQ_1352:
        failed.append("UNIQ_1352 missing legal UCI lock")
    if "0.6234" not in UNIQ_1352:
        failed.append("UNIQ_1352 missing quick_eval lock")
    if "do not quote 0.7518" not in UNIQ_1352:
        failed.append("UNIQ_1352 missing 0.7518 lock")
    if "first card revisit tag no prior notes card" not in UNIQ_1352:
        failed.append("UNIQ_1352 missing first-card lock")
    if "this fold is §151 only" not in UNIQ_1352:
        failed.append("UNIQ_1352 missing §151-only occupancy")
    if "hourly 1256 §150 are on main" not in UNIQ_1352:
        failed.append("UNIQ_1352 missing merged §150 occupancy")
    if "do not push onto open #75" in UNIQ_1352 or "Open PR #75" in UNIQ_1352:
        failed.append("UNIQ_1352 still claims open #75")
    if "notes.md §151" not in UNIQ_1352:
        failed.append("UNIQ_1352 missing §151 lock")
    if "Soft judgment never sole veto" not in UNIQ_1352:
        failed.append("UNIQ_1352 missing sole-veto lock")
    if "#76" not in UNIQ_1352:
        failed.append("UNIQ_1352 missing HARD RULE #76")
    if "prompt-only design-investigation aid" not in UNIQ_RYANA:
        failed.append("UNIQ_RYANA missing species")
    if "stargazers_count 6" not in UNIQ_RYANA:
        failed.append("UNIQ_RYANA missing live stars")
    if "license null" not in UNIQ_RYANA:
        failed.append("UNIQ_RYANA missing license null")
    if "87a9ef3674f111c74bb33cccd3bfa56bd0c4a15c" not in UNIQ_RYANA:
        failed.append("UNIQ_RYANA missing HEAD")
    if "227e2324818375e1f73d044af6a56a5b933c496b" not in UNIQ_RYANA:
        failed.append("UNIQ_RYANA missing README SHA")
    if "notes.md §152" not in UNIQ_RYANA:
        failed.append("UNIQ_RYANA missing §152")
    if "composition 809-820" not in UNIQ_RYANA:
        failed.append("UNIQ_RYANA missing composition 809-820")
    if "findings batch #132" not in UNIQ_RYANA:
        failed.append("UNIQ_RYANA missing findings batch #132")
    if "does not bump 0.5.0 or 0.5.1" not in UNIQ_RYANA:
        failed.append("UNIQ_RYANA missing version freeze")
    if "this fold is §152 only" not in UNIQ_RYANA:
        failed.append("UNIQ_RYANA missing §152-only occupancy")
    if "hourly 1352 §151 are on main" not in UNIQ_RYANA:
        failed.append("UNIQ_RYANA missing merged §151 occupancy")
    if "do not push onto open #77" in UNIQ_RYANA or "open #77 owns" in UNIQ_RYANA:
        failed.append("UNIQ_RYANA still claims open #77")

    if "Jev chooses concrete actions" not in UNIQ_1454:
        failed.append("UNIQ_1454 missing otto action lock")
    if "model score not a guarantee" not in UNIQ_1454:
        failed.append("UNIQ_1454 missing model-score lock")
    if "0.25 still soft" not in UNIQ_1454:
        failed.append("UNIQ_1454 missing keep-threshold lock")
    if "nothing sends itself" not in UNIQ_1454:
        failed.append("UNIQ_1454 missing send lock")
    if "same answers is their claim" not in UNIQ_1454:
        failed.append("UNIQ_1454 missing laya claim lock")
    if "Codiv OpenJev ≠ TypeSafe" not in UNIQ_1454:
        failed.append("UNIQ_1454 missing Codiv lock")
    if "ranking ≠ calibration" not in UNIQ_1454:
        failed.append("UNIQ_1454 missing ranking lock")
    if "open recreation ≠ calibrated replica" not in UNIQ_1454:
        failed.append("UNIQ_1454 missing recreation lock")
    if "Qwen3-4B ≠ Archer" not in UNIQ_1454:
        failed.append("UNIQ_1454 missing Qwen3-4B lock")
    if "MLX was CoreML" not in UNIQ_1454:
        failed.append("UNIQ_1454 missing MLX lock")
    if "densify §132 not a sibling first sighting" not in UNIQ_1454:
        failed.append("UNIQ_1454 missing §132 densify lock")
    if "densify §145 not a sibling first sighting" not in UNIQ_1454:
        failed.append("UNIQ_1454 missing §145 densify lock")
    if "densify §151 not a sibling first sighting" not in UNIQ_1454:
        failed.append("UNIQ_1454 missing §151 densify lock")
    if "88.58% *theirs*" not in UNIQ_1454:
        failed.append("UNIQ_1454 missing JMLE lock")
    if "84.0% *theirs*" not in UNIQ_1454:
        failed.append("UNIQ_1454 missing GaNotch lock")
    if "one Mind2Web shard" not in UNIQ_1454:
        failed.append("UNIQ_1454 missing Mind2Web lock")
    if "SHA unchanged e360f3ff5b13" not in UNIQ_1454:
        failed.append("UNIQ_1454 missing skill-router SHA lock")
    if "sha b5eb4528c941 unchanged" not in UNIQ_1454:
        failed.append("UNIQ_1454 missing laya-onnx SHA lock")
    if "this fold is §153 only" not in UNIQ_1454:
        failed.append("UNIQ_1454 missing §153-only occupancy")
    if "ryana/jevify §152 are on main" not in UNIQ_1454:
        failed.append("UNIQ_1454 missing merged §152 occupancy")
    if "notes.md §153" not in UNIQ_1454:
        failed.append("UNIQ_1454 missing §153 lock")
    if "composition 821-836" not in UNIQ_1454:
        failed.append("UNIQ_1454 missing composition")
    if "findings batch #133" not in UNIQ_1454:
        failed.append("UNIQ_1454 missing findings batch")
    if "#78" not in UNIQ_1454:
        failed.append("UNIQ_1454 missing HARD RULE #78")
    if "Soft judgment never sole veto" not in UNIQ_1454:
        failed.append("UNIQ_1454 missing sole-veto lock")
    if "invented_signal: false" not in UNIQ_1454:
        failed.append("UNIQ_1454 missing invented_signal")
    if "Skip Archer" not in UNIQ_1454:
        failed.append("UNIQ_1454 missing Skip Archer")
    if "n=40 is not Harbor" not in UNIQ_1454:
        failed.append("UNIQ_1454 missing n=40 lock")
    if "held-out ECE 0.299" not in UNIQ_1454:
        failed.append("UNIQ_1454 missing Tiny-Jev held-out ECE")
    if "fitted public rows are not zero-shot" not in UNIQ_1454:
        failed.append("UNIQ_1454 missing Tiny-Jev fit-set lock")
    if "do not push onto open #77" in UNIQ_1454 or "open #77 owns" in UNIQ_1454:
        failed.append("UNIQ_1454 claims open #77")

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
    if "## 146. Hourly 1110 HIGH" not in notes:
        failed.append("notes.md missing §146 heading")
    if "## 147. User-provided glance HIGH" not in notes:
        failed.append("notes.md missing §147 heading")
    if "## 148. Hourly 1203 HIGH" not in notes:
        failed.append("notes.md missing §148 heading")
    if "## 149. User-provided lev HIGH" not in notes:
        failed.append("notes.md missing §149 heading")
    if "## 150. Hourly 1256 HIGH" not in notes:
        failed.append("notes.md missing §150 heading")
    if "## 152. User-provided ryana/jevify HIGH" not in notes:
        failed.append("notes.md missing §152 heading")
    if notes.count(UNIQ_RYANA) != 1:
        failed.append(
            f"notes.md ryana lock count {notes.count(UNIQ_RYANA)} != 1"
        )
    if (
        "ryana/jevify\n   (first dedicated card `notes.md` §152)"
        not in notes
    ):
        failed.append("notes.md §118 missing ryana §152 namesake pointer")
    if "User-provided 0940 uniqueness lock:" not in notes:
        failed.append("notes.md missing frozen 0940 lock")
    for rel in OVERLAYS:
        if rel == "research/notes.md":
            continue
        overlay = (ROOT / rel).read_text(encoding="utf-8")
        if UNIQ_RYANA in overlay:
            failed.append(f"ryana lock leaked into overlay {rel}")

    if "## 151. Hourly 1352 HIGH" not in notes:
        failed.append("notes.md missing §151 heading")
    i149 = notes.find("## 149. User-provided lev HIGH")
    i150 = notes.find("## 150. Hourly 1256 HIGH")
    i151 = notes.find("## 151. Hourly 1352 HIGH")
    if not (i149 >= 0 and i150 > i149 and i151 > i150):
        failed.append("notes.md must stay contiguous §149 then §150 then §151")
    i152 = notes.find("## 152. User-provided ryana/jevify HIGH")
    if not (i151 >= 0 and i152 > i151):
        failed.append("notes.md must stay contiguous §150 then §151 then §152")
    notes152 = notes[i152:] if i152 >= 0 else ""
    if "this fold is §152 only" not in notes152:
        failed.append("notes.md §152 missing §152-only occupancy")
    if "hourly 1352 §151 are on main" not in notes152:
        failed.append("notes.md §152 missing merged §151 occupancy")
    if "do not push onto open #77" in notes152 or "open #77 owns" in notes152:
        failed.append("notes.md §152 still claims open #77")

    if "## 153. Hourly 1454 HIGH" not in notes:
        failed.append("notes.md missing §153 heading")
    if notes.count(UNIQ_1454) != 1:
        failed.append(
            f"notes.md 1454 lock count {notes.count(UNIQ_1454)} != 1"
        )
    i153 = notes.find("## 153. Hourly 1454 HIGH")
    if not (i152 >= 0 and i153 > i152):
        failed.append("notes.md must stay contiguous §152 then §153")
    notes153 = notes[i153:] if i153 >= 0 else ""
    if "this fold is §153 only" not in notes153:
        failed.append("notes.md §153 missing §153-only occupancy")
    if "ryana/jevify §152 are on main" not in notes153:
        failed.append("notes.md §153 missing merged §152 occupancy")
    if "do not push onto open #77" in notes153 or "open #77 owns" in notes153:
        failed.append("notes.md §153 claims open #77")
    if UNIQ_1454 not in notes153:
        failed.append("1454 lock missing inside notes.md §153")
    readme_1454 = (ROOT / "README.md").read_text(encoding="utf-8")
    if UNIQ_1454 in readme_1454:
        failed.append("README.md must not hold the 1454 uniqueness lock")
    if not readme_1454.rstrip().endswith("Contributions: [CONTRIBUTING.md](CONTRIBUTING.md)."):
        failed.append("README.md must still end at the License close")
    for rel in OVERLAYS:
        if rel == "research/notes.md":
            continue
        overlay_1454 = (ROOT / rel).read_text(encoding="utf-8")
        if UNIQ_1454 in overlay_1454:
            failed.append(
                f"1454 lock must stay in notes.md and the gate fixture, not {rel}"
            )
    for remainder_id in (
        "B0mbxstiC/jev-chatgpt",
        "DarkWanderer/laya",
        "Emlembow/jev-graph-search",
        "FYIsoft/Microsoft.Extensions.AI.Providers",
        "GaNotchVFX/jev-benchmarks",
        "GreenKeewi/jev-x-scanner",
        "HCTDIP/jevkit",
        "JKasteele/mail-safety-lab",
        "Jevals/Jevals",
        "Jevals/jevals-data",
        "JohnCari/of-record",
        "Klikwork/feedlens",
        "KushagraBharti/The-JEV-LLM",
        "LiamSherline/jev-lead-scorer",
        "MatteoGauthier/laya-portable",
        "Maxi91f/jev_testing",
        "MstyAI/laya-mlx-swift",
        "NobleSpartan6/otto",
        "OpenScribbler/semantic-style-lab",
        "PAUNYWSE34/-Your-Payment-Receipt-Details-jevans4824-aol.com--7qlmt3wo",
        "Postman-Devrel/JevPong",
        "RastislavDujava/jev-classification-prompting",
        "SebasPinto/moviejev",
        "Sourav19o7/jev-examples",
        "Spray2/JEVangelion",
        "SuperInstance/substrate-gan",
        "TokyoHunter/jev-animal-finder",
        "Yaro60/jev-research",
        "Yushenggg/zero-shot-classifier",
        "ajmeese7/jev-chess",
        "aleksvega/jev-skill-router",
        "altanapps/security-sandbox-jev",
        "asynq-io/system-one",
        "baldpanda/jev-sandbox",
        "cdeguet/jev-tetris",
        "cedrecs/jev-stories",
        "cohenom/laya-snake",
        "danielamitay/swev",
        "dperezcabrera/jev-chess",
        "echohello-dev/jev-mcp-server",
        "eriestra/blockly-jev",
        "fcjr/jev-first-search",
        "fullcolorcoder/reflex-jev",
        "gbesse/blender-jev-review",
        "gbesse/jev-obs-cues",
        "gbesse/jev-vscode-review",
        "gbesse/roblox-jev-studio",
        "glebmish/jev-watchdog",
        "gnapse/jev",
        "gopaljigaur/decide",
        "haystackeditor/stop-rules",
        "heyaozh/jev-rust-crate",
        "hf:juspay/jev-one",
        "hf:lostargon/Tiny-Jev",
        "hf:marcmagn1/jev-08b-typed-r1",
        "hf:rarha/laya-onnx",
        "hosamsh/jev-mind2web",
        "jonkthomas/jev-shadow",
        "jose-salcedo-sp/recall",
        "kennedy-f/hermes-jev-decision-layer",
        "kokuren333/jev-jmle-benchmark",
        "koz/anti-dead-internet",
        "layareddy10-source/layareddy10-source.github.io",
        "maxvaega/gmail-jev-guard",
        "mingleiw/jev-oncall",
        "mraad/feln-laya",
        "nourhelmi/pi-jev-compaction",
        "piyushpawar54/system-one-bench",
        "ppradyoth/jev-guard",
        "pratikgorji/jev-guide",
        "rawwerks/one-system",
        "sriharsha8991/JEV-use_cases",
        "strombolini/Armada",
        "sunnyspot114514/jevnet-runtime",
        "suyash-lyzr/jev-typesafe",
        "v0idhrt/lyra-n",
        "xosi/laya",
        "xuan7zhang/jev-toolspace",
    ):
        if remainder_id not in notes153:
            failed.append(f"notes.md §153 missing card {remainder_id}")
    if UNIQ_1352 not in notes:
        failed.append("1352 lock missing as one substring: research/notes.md")
    notes151 = notes[notes.find("## 151. Hourly 1352 HIGH"):]
    if notes151.count(UNIQ_1352) != 1:
        failed.append("notes.md §151 must hold the 1352 lock once")
    readme_body = (ROOT / "README.md").read_text(encoding="utf-8")
    if UNIQ_1352 in readme_body:
        failed.append("README.md must not hold the 1352 uniqueness lock")
    for rel in OVERLAYS:
        if rel == "research/notes.md":
            continue
        overlay_body = (ROOT / rel).read_text(encoding="utf-8")
        if UNIQ_1352 in overlay_body:
            failed.append(
                f"1352 lock must stay in notes.md and the gate fixture, not {rel}"
            )

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
    notes146 = notes[notes.find("## 146. Hourly 1110 HIGH"):]
    for remainder_id in (
        "hf:thaitea/laya-vision",
        "AntonG87/codearia-sieve",
        "0xagentlabs/jev-xiangqi",
        "7Zenox/gemma-jev",
        "7starsseeker/dsh-fact-check",
        "Aimlessss/rust-jev-typesafe-trade-decision-engine",
        "Alpha-Harper-Franklin/astra-jev",
        "AltSlate-Labs/jev-dag",
        "AnthonyAlcaraz/aiven-agentic-graphrag-demo",
        "Anxiety471/idle-mmo-bot",
        "DjTaNg-404/Laya-2048",
        "DwainYu/laya-multilingual-playground",
        "IAmJSD/pg-laya",
        "KennethAshley/awesome-jev",
        "MarkChu-git/typesafe-mcp",
        "Obrais-cloud/ticket-rerank",
        "Obrais-cloud/typesafe-translate",
        "Pdbz199/local-decision-model",
        "RyanNg1403/jev-cli",
        "THANK-YOU-FOR-YOUR-ORDER-ASDF123/repo-laya4qxd",
        "Tom-R-Main/Footwork",
        "Tongyun1/Jev-in-the-Loop",
        "Ylr9933/JevForAgent",
        "Ylr9933/JevOS",
        "andrew-monroe/twenty-questions",
        "aninibread/jev-dino",
        "apolenkov/jev-codex-router-lab",
        "awoaCrim/pi-smart-subagents",
        "baldm0mma/JevTheDev-PortfolioPage",
        "blueOctopusAI/ai-accordion",
        "chenrui333/jev-docs",
        "chensheng43/jevtest",
        "codejunkie99/jev-engineering",
        "deesatzed/JevEdge0",
        "emerson-buoy/jev-poc",
        "erboland/jev-fund",
        "gavansmyth-arch/jev-chrome-extension",
        "gbesse/jev-rerank-server",
        "hanshs474/jevx-client",
        "hf:SargeDev/jev-gate-student-b-merged",
        "hf:aimeigaoshou/agent-jev",
        "hf:marcmagn1/jev-alt-systemone-eval",
        "hf:sivasub987/mandate-1-laya",
        "i-madhav/jevxlaya-mlx",
        "iapp-technology/openthai-systemone-doom",
        "jan-barg/jev-traffic-control",
        "jonas050210/Laya_Playground",
        "kidzik/jiffy",
        "ksalk/laya-docker-api",
        "lewisjohnvillamor/Jevfit",
        "majonation/jev-plays-games",
        "malevrigns/agent-jev",
        "marcemarin/typesafe-laravel",
        "musubi-labs/musubi-jev",
        "narulaskaran/jev-data-questions",
        "nathan1313/issue-triage-bot",
        "ninjasweb/jev-blog-filter",
        "notzSph/zjev",
        "pavlealeksic/laya-hermes",
        "pietrushka/jev-youtube-filter",
        "proshunsuke/jev-tab-order",
        "quaeast/vllm2jev",
        "rahiseko-alt/jev-test1",
        "s3rli/jevips",
        "sisodias/jev-agent-skills",
        "thundercat1/jev-clin-trial-extraction-benchmarks",
        "unirt/jev-eval-ja",
        "uzuraDev/cookie-clicker-jev",
        "walidboulanouar/jev-agent-kit",
        "pythongiant/laya-drift",
        "turenlabs/jast",
        "Adkid-Zephyr/chinese-workflow-decision-bench",
        "JabbaKadabra/SystemOneDotNet",
        "arnavm-codes/JevFence",
        "cloudbtl/JevRAG",
        "gbesse/decision-workbench",
    ):
        if remainder_id not in notes146:
            failed.append(f"notes.md §146 missing remainder card {remainder_id}")
    notes147 = notes[notes.find("## 148. Hourly 1203 HIGH"):]
    for remainder_id in (
        'peterfriese/jev-foundation-models',
        'AbdelStark/abdelstark.github.io',
        'Alexander-Ollman/laya-ft',
        'AustinDKB/grass-optimizer',
        'BipinRajC/Jev-api-experiments',
        'Codercise/jev-in-practice',
        'DevvGwardo/ghost-route',
        'Ejokey/lightjev',
        'Elue-dev/jev_elixir',
        'Georgy-hook/laya-rimworld-director',
        'Jorgediamanto/jev-playground',
        'Lavenir7/Jev2048',
        'Makia9879/pi-jev-router',
        'NikHeck/jev-benchmark',
        'Renwang-Huang/arbitype',
        'Shoaib-Asghar/jev-probe',
        'SoundBlaster/SwiftDecision-Examples',
        'Sy3058/jev-evaluate',
        'UtpalJayNadiger/find',
        'ahtcfg24/codex-speculator',
        'allebee/jevgrep',
        'allebee/pytest-jev',
        'babanomania/linkedin-bullshit-filter',
        'bangxiao0927/decidespeak',
        'bitofant/laya',
        'coreywoo27/Jev-Empowered-Qwen-mlx',
        'cornelflorea/jev-test',
        'dannyowelch/jev-abstention-checker',
        'dante01yoon/laya-jev-arena',
        'datamonsterr/jev_auto_select_skills',
        'diluteoxygen/JevName',
        'edrache/jevworms',
        'emerson-buoy/jev-ticket-classifier',
        'emlama/jev-mcp',
        'fblissjr/typesafe-experiments',
        'frahlg/laya-ems-test',
        'hazlema/jev-connect4',
        'hf:marcmagn1/jev-alt-systemone-trackio',
        'hf:opg13/laya',
        'hfnissum-byte/jevmerge',
        'ishantanu/jevtraces',
        'jayozer/jevzero',
        'jeonck/clinic-checklist',
        'jevonj05/jevonj05',
        'jordilopez/pi-smart-router',
        'karanb192/jev-skill-scout',
        'ljbuturovic/jevgram',
        'luisrapalino/jev-smart-bets',
        'lvzhaobo/-jev-assayer',
        'lvzhaobo/jev-assayer',
        'makiisthenes/JevAIExperimentation',
        'moelahmady/shunt-jev',
        'naiersaidane/jev-demos',
        'olivere/systemone',
        'p2kalita/Building-a-Harness-with-Jev-LangChain',
        'pavlealeksic/jev-hermes',
        'perezjohn0/jevpav',
        'piyushsonawane07/trueKeep',
        'prakash5284/jev-vs-llm-resume-jd-eval',
        'pratik-codechef/jev-model',
        'punitarani/jeve',
        'ravinarayanan89/JevForce',
        'rishhavv/tabjev',
        'ruslanlap/jev-gate',
        'sathwikkuncham/laya-snake-arena',
        'shivpratapsinghpanwar/edgefront',
        'singhdevhub-lovepreet/firstlight',
        'sliday/jev-chess-algo',
        'sunmont/pi-jev-dsk-agi',
        'theglitcharchitect/muse-skills',
        'uibuckets/ai-decision-lab',
        'uibuckets/laya-local-service',
        'wuxie888/jev-yaba-wechat',
        'AkashPriyadarshii/jev-seo',
        'dtduc-git/jevnav',
        'SoundBlaster/SwiftDecision',
        'Tongyun1/Jev-in-the-Loop',
        'hf:aimeigaoshou/agent-jev',
        'hf:clduab11/jev-calibration-statistics',
    ):
        if remainder_id not in notes147:
            failed.append(f"notes.md §148 missing remainder card {remainder_id}")
    notes150 = notes[notes.find("## 150. Hourly 1256 HIGH"):]
    for remainder_id in (
        "smartaces/jev-plays-streetfighter-2",
        "AboveColin/jevclient",
        "hf:libingzheren/Jev-Mem",
        "revsmoke/promptrejectormcp",
        "a1393323447/jevapi",
        "hfnissum-byte/Hunkpick",
        "lvzhaobo/jev-loop",
        "sirkirby/routr",
        "AviroopPaul/jev-playground",
        "Cognition-Forge/snake-laya",
        "DKim50/Jev-Beater-Reranker",
        "Debasishhh/jevguard",
        "GodModeAI2025/JevCoreML",
        "INV-32549632/account-notices-x4jevw5t",
        "MikeBinstock/llm2jev.com",
        "Nachi-Kulkarni/jev_voice_agents",
        "Neoo-Blue/vibecheck",
        "RavenValentin/TypeSafe.Jev",
        "SuperInstance/jev-receipts",
        "SuperInstance/jeviter",
        "TheNerdMan/docker-laya-api",
        "TheSeriousProgrammer/QwenJev",
        "WanLanglin/jev-wikirace",
        "actions-marketplace-validations/sathariels_jevtriage",
        "adorosario/jev-rag-claim-verification",
        "antodiazcano/jev",
        "breejesh/gen1",
        "bytelabs-oss/clash-jev",
        "caramellumm/jev-crap",
        "colin-hofer/will-it-jev",
        "dedene/jevspin",
        "dipendra-sharma/jev-cli",
        "fstandhartinger/who-is-right",
        "harlanljones/sabr-jev",
        "harrisonmuskat/jev-codenames",
        "heyaozh/jev-rust-crater",
        "hf:Cruzex/laya-typed-decisions-smoketest",
        "hf:abidlabs/jev-typed-decisions-causal-0-6b-trackio",
        "hf:abidlabs/jev-typed-decisions-causal-0.6b",
        "hf:abidlabs/jev-typed-decisions-causal-0.6b-smoke",
        "hf:s1lv3rj1nx/openjev-general-lora",
        "hf:suryatmodulus/open-jev-demo",
        "hqvdvn-cmd/astra-jev-benchmark",
        "ilumn/jev-proof-selector",
        "imranrkhan13/jevscope",
        "jverhoeks/claude-laya",
        "khursheed33/laya-routing-and-descision-making",
        "knishika62/laya-mlx-demo",
        "krisitown/jev-router",
        "krushideep/Worldtour",
        "ktaletsk/jevframe",
        "lldois/dsh-jev",
        "midorisawa/Shirakawa",
        "mraad/lunar-mpc-laya",
        "mrebbert/Jev-CustomerService-Demo",
        "mrrasmussendk/jev.net",
        "nadeemcite/jev-crash-course",
        "nadyth/jev-crash-course",
        "navidkashani/jev-guard",
        "nvkudva/laya-server",
        "paddix/JEV",
        "pb-crackers/Jev-Cognigy-QA-Suite",
        "seethinajayadileep/jev-desk",
        "sonson0910/jev-router",
        "tomfrazier/slopmop",
        "treble-maker123/jev-playground",
        "v60samurai/jev-atlas",
        "vincentlauriat/ClaudeMenu",
        "vishalbitit/jev-prior-auth-triage",
        "wbuecksler/jev-voice-browser-chrome-extension",
        "zsoist/BUILD-DAY---Danis-Project",
        "allebee/jevgrep",
        "harlanljones/jev-roster-shapes",
    ):
        if remainder_id not in notes150:
            failed.append(f"notes.md §150 missing remainder card {remainder_id}")

    for remainder_id in (
        "benjamincanac/tia",
        "MorrisZJ/AnyJev",
        "andududu/jeview",
        "karozi/awesome-jev-resources",
        "satiricalguru/Fast-Jev-Agents",
        "247arjun/JevPlayground",
        "Alberto-Codes/judgevet",
        "DanM3rcurius/po-radar",
        "Emlembow/jevgraph",
        "Faresabdelghany/jev-browser-test",
        "Ivanovskyi/typesafe-ai-gateway",
        "MatteoGauthier/laya-onnx",
        "SAITS-Swiss-AI-Tech-Services/jev-mcp",
        "SimonKaran13/DOOMJEV",
        "TokyoHunter/jev-animal-finder",
        "abe17124/jev-laya-chess-bench",
        "adelaserna82/jev-model-net-sdk",
        "aitofy-dev/jev-awesome-skills",
        "aleksvega/jev-skill-router",
        "alibowbow/jev",
        "anchorshell/relay",
        "ankurlamichhane90/mac-voice-assistant",
        "canok07/jev-router",
        "codeJRV/openjev-hermes-plugin",
        "d-callan/bionym",
        "deemkeen/jevgeni",
        "devanshbatham/nyx",
        "diluteoxygen/JevMood",
        "emipaz/jev",
        "fedorpark/jev-inbox-lab",
        "fredp74/calibrus",
        "gbesse/bevy-jev",
        "gbesse/figma-jev-review",
        "gbesse/jev-premiere-markers",
        "gbesse/jev-unreal-statetree",
        "ham-zax/awesome-jev",
        "harrymunro/jev-laya-benchmark",
        "hf:Wouze/laya-ara",
        "hf:Wouze/laya-ara-rag",
        "hf:abidlabs/jev-typed-decisions-causal-0.6b",
        "hf:abidlabs/jev-typed-decisions-demo",
        "hf:akhilaaa3/openjev-train",
        "hf:juspay/jev-trained",
        "hf:rarha/laya-onnx",
        "htpu/mailaya",
        "ilyaryabchinski/jevss",
        "individual11/jev-feedbin-filter",
        "jpvajda/jev-demo",
        "kevinaaaquil/jev-rubix",
        "koolerkx/vibe-discord-bot-jev",
        "marcelormendes/diffninja",
        "mbburabak/jev-safety-benchmark",
        "mwatkins03-netizen/The-Complaint-Atlas-Fable-5",
        "nautahakk/jev-codex-router",
        "pavan142/jev-experiments",
        "pedro-pscunha/guideme-python",
        "photuris/overseer-judge",
        "qasimhammad1/applyguard",
        "rscottstevens-byte/jev",
        "sed-ndi/test-jev",
        "tgallice/jev-go",
        "vaibhavgupta5/Jev-Email-Classifier",
        "vishalyadav28/resume-jev-match",
        "yangda611/omarchy-smart-paste",
        "zerowidth-ai/shims-sdk",
    ):
        if remainder_id not in notes151:
            failed.append(f"notes.md §151 missing remainder card {remainder_id}")
    algebra = (ROOT / ".agents/skills/augustus/references/composition-algebra.md").read_text(
        encoding="utf-8"
    )
    for n in list(range(289, 317)) + list(range(322, 330)) + list(range(330, 337)) + list(range(337, 353)) + list(range(353, 369)) + list(range(369, 385)) + list(range(385, 401)) + list(range(401, 417)) + list(range(417, 433)) + list(range(433, 449)) + list(range(449, 465)) + list(range(465, 481)) + list(range(481, 497)) + list(range(497, 505)) + list(range(505, 521)) + list(range(521, 537)) + list(range(537, 553)) + list(range(553, 569)) + list(range(569, 585)) + list(range(585, 601)) + list(range(601, 617)) + list(range(617, 633)) + list(range(633, 649)) + list(range(649, 665)) + list(range(665, 681)) + list(range(681, 697)) + list(range(697, 713)) + list(range(713, 729)) + list(range(729, 745)) + list(range(745, 761)) + list(range(761, 777)) + list(range(777, 793)) + list(range(793, 837)):
        needle = f"{n}. **"
        if needle not in algebra:
            failed.append(f"composition-algebra missing item {n}")
    for n in range(317, 322):
        needle = f"{n}. **"
        if needle in algebra:
            failed.append(f"composition-algebra stole unused item {n}")
    if "761. **Swift 6 bridge into Apple Foundation Models**" not in algebra:
        failed.append("composition item 761 is not the 1203 Swift bridge")
    if "777. **typed client is not a replica**:" not in algebra:
        failed.append("composition item 777 is not the 1256 typed client")
    if "809. **prompt-only investigation aid**:" not in algebra:
        failed.append("composition item 809 is not the ryana prompt-only aid")
    if "821. **Jev chooses, code acts, review before write**" not in algebra:
        failed.append("composition item 821 is not the 1454 otto action")
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
        "## Batch #128",
        "## Batch #129",
        "## Batch #130",
        "## Batch #131",
        "## Batch #132",
        "## Batch #133",
    ):
        if batch not in findings:
            failed.append(f"findings.md missing {batch}")
    if UNIQ_RYANA in findings:
        failed.append("findings.md holds the ryana uniqueness lock")
    if UNIQ_1454 in findings:
        failed.append("findings.md holds the 1454 uniqueness lock")
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
    digest_path_1110 = ROOT / "research/archive/hourly/2026-09-21T17/run_digest.json"
    if not digest_path_1110.is_file():
        failed.append("missing 1110 run_digest.json")
    else:
        digest1110 = json.loads(digest_path_1110.read_text(encoding="utf-8"))
        if digest1110.get("label") != "1110":
            failed.append(f"1110 run_digest label {digest1110.get('label')!r} != '1110'")
        if digest1110.get("notes_section") != "146":
            failed.append(
                f"1110 run_digest notes_section {digest1110.get('notes_section')!r} != '146'"
            )
        if digest1110.get("composition") != "745-760":
            failed.append(
                f"1110 run_digest composition {digest1110.get('composition')!r} != '745-760'"
            )
        if digest1110.get("findings_batch") != 128:
            failed.append(
                f"1110 run_digest findings_batch {digest1110.get('findings_batch')!r} != 128"
            )
        if digest1110.get("invented_signal") is not False:
            failed.append("1110 run_digest invented_signal is not false")
    digest_path_1203 = ROOT / "research/archive/hourly/2026-09-21T18/run_digest.json"
    if not digest_path_1203.is_file():
        failed.append("missing 1203 run_digest.json")
    else:
        digest1203 = json.loads(digest_path_1203.read_text(encoding="utf-8"))
        if digest1203.get("label") != "1203":
            failed.append(f"1203 run_digest label {digest1203.get('label')!r} != '1203'")
        if digest1203.get("notes_section") != "148":
            failed.append(
                f"1203 run_digest notes_section {digest1203.get('notes_section')!r} != '148'"
            )
        if digest1203.get("composition") != "761-776":
            failed.append(
                f"1203 run_digest composition {digest1203.get('composition')!r} != '761-776'"
            )
        if digest1203.get("findings_batch") != 129:
            failed.append(
                f"1203 run_digest findings_batch {digest1203.get('findings_batch')!r} != 129"
            )
        if digest1203.get("invented_signal") is not False:
            failed.append("1203 run_digest invented_signal is not false")
        if digest1203.get("novel_high") != 73:
            failed.append(
                f"1203 run_digest novel_high {digest1203.get('novel_high')!r} != 73"
            )
        if digest1203.get("revisit_high") != 6:
            failed.append(
                f"1203 run_digest revisit_high {digest1203.get('revisit_high')!r} != 6"
            )
    digest_path_1256 = ROOT / "research/archive/hourly/2026-09-21T1856/run_digest.json"
    if not digest_path_1256.is_file():
        failed.append("missing 1256 run_digest.json")
    else:
        digest1256 = json.loads(digest_path_1256.read_text(encoding="utf-8"))
        if digest1256.get("label") != "1256":
            failed.append(f"1256 run_digest label {digest1256.get('label')!r} != '1256'")
        if digest1256.get("notes_section") != "150":
            failed.append(
                f"1256 run_digest notes_section {digest1256.get('notes_section')!r} != '150'"
            )
        if digest1256.get("composition") != "777-792":
            failed.append(
                f"1256 run_digest composition {digest1256.get('composition')!r} != '777-792'"
            )
        if digest1256.get("findings_batch") != 130:
            failed.append(
                f"1256 run_digest findings_batch {digest1256.get('findings_batch')!r} != 130"
            )
        if digest1256.get("invented_signal") is not False:
            failed.append("1256 run_digest invented_signal is not false")

    digest_path_1352 = ROOT / "research/archive/hourly/2026-09-21T19/run_digest.json"
    if not digest_path_1352.is_file():
        failed.append("missing 1352 run_digest.json")
    else:
        digest1352 = json.loads(digest_path_1352.read_text(encoding="utf-8"))
        if digest1352.get("label") != "1352":
            failed.append(f"1352 run_digest label {digest1352.get('label')!r} != '1352'")
        if digest1352.get("notes_section") != "151":
            failed.append(
                f"1352 run_digest notes_section {digest1352.get('notes_section')!r} != '151'"
            )
        if digest1352.get("composition") != "793-808":
            failed.append(
                f"1352 run_digest composition {digest1352.get('composition')!r} != '793-808'"
            )
        if digest1352.get("findings_batch") != 131:
            failed.append(
                f"1352 run_digest findings_batch {digest1352.get('findings_batch')!r} != 131"
            )
        if digest1352.get("invented_signal") is not False:
            failed.append("1352 run_digest invented_signal is not false")
        if digest1352.get("novel_high") != 64:
            failed.append(
                f"1352 run_digest novel_high {digest1352.get('novel_high')!r} != 64"
            )
        if digest1352.get("revisit_high") != 1:
            failed.append(
                f"1352 run_digest revisit_high {digest1352.get('revisit_high')!r} != 1"
            )
        if "0.6234" not in (digest1352.get("primary") or ""):
            failed.append("1352 run_digest primary missing 0.6234")
        if "this fold is §151 only" not in notes151:
            failed.append("notes.md §151 missing §151-only occupancy")
        if "hourly 1256 §150 are on main" not in notes151:
            failed.append("notes.md §151 missing merged §150 occupancy")
        if "do not push onto open #75" in notes151 or "Open PR #75" in notes151:
            failed.append("notes.md §151 still claims open #75")
    digest_path_1454 = ROOT / "research/archive/hourly/2026-09-21T20/run_digest.json"
    if not digest_path_1454.is_file():
        failed.append("missing 1454 run_digest.json")
    else:
        digest1454 = json.loads(digest_path_1454.read_text(encoding="utf-8"))
        if digest1454.get("label") != "1454":
            failed.append(f"1454 run_digest label {digest1454.get('label')!r} != '1454'")
        if digest1454.get("notes_section") != "153":
            failed.append(
                f"1454 run_digest notes_section {digest1454.get('notes_section')!r} != '153'"
            )
        if digest1454.get("composition") != "821-836":
            failed.append(
                f"1454 run_digest composition {digest1454.get('composition')!r} != '821-836'"
            )
        if digest1454.get("findings_batch") != 133:
            failed.append(
                f"1454 run_digest findings_batch {digest1454.get('findings_batch')!r} != 133"
            )
        if digest1454.get("invented_signal") is not False:
            failed.append("1454 run_digest invented_signal is not false")
        if digest1454.get("novel_high") != 73:
            failed.append(
                f"1454 run_digest novel_high {digest1454.get('novel_high')!r} != 73"
            )
        if digest1454.get("revisit_high") != 5:
            failed.append(
                f"1454 run_digest revisit_high {digest1454.get('revisit_high')!r} != 5"
            )
        if "Jev chooses concrete actions" not in (digest1454.get("primary") or ""):
            failed.append("1454 run_digest primary missing otto action")
        if "this fold is §153 only" not in notes153:
            failed.append("notes.md §153 missing §153-only occupancy repeat")
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
        ("1110", UNIQ_1110),
        ("glance", UNIQ_GLANCE),
        ("1203", UNIQ_1203),
        ("1256", UNIQ_1256),
        ("1352", UNIQ_1352),
        ("ryana", UNIQ_RYANA),
        ("1454", UNIQ_1454),
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
    if UNIQ_RYANA in readme:
        failed.append("README.md holds the ryana uniqueness lock")
    if UNIQ_1454 in readme:
        failed.append("README.md holds the 1454 uniqueness lock")
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
        f"0049 chars={len(UNIQ_0049)} 0151 chars={len(UNIQ_0151)} 0248 chars={len(UNIQ_0248)} 0348 chars={len(UNIQ_0348)} 0445 chars={len(UNIQ_0445)} 0551 chars={len(UNIQ_0551)} 0707 chars={len(UNIQ_0707)} 0823 chars={len(UNIQ_0823)} 0923 chars={len(UNIQ_0923)} 1019 chars={len(UNIQ_1019)}  1110 chars={len(UNIQ_1110)} glance chars={len(UNIQ_GLANCE)} 1203 chars={len(UNIQ_1203)} 1256 chars={len(UNIQ_1256)} 1352 chars={len(UNIQ_1352)} ryana chars={len(UNIQ_RYANA)} 1454 chars={len(UNIQ_1454)} "
        f"revisit chars={len(REVISIT_LOCK)} "
        f"overlays={len(OVERLAYS)} "
        f"revisit_overlays={len(REVISIT_OVERLAYS)}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
