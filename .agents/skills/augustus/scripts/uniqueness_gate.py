#!/usr/bin/env python3
"""Uniqueness gate for merged 0843 (§114), merged 0915 NanoJev (§115),
merged 0920 jcr (§116), merged 0922 SemIf (§117), merged 0940
llm-to-jev (§118), hourly 0947 HIGH (§119), hourly 1049 HIGH (§120),
hourly 1143 HIGH (§121), hourly 1248 HIGH (§123), hourly 1340 HIGH (§124), hourly 1441 HIGH (§125), hourly 1542 HIGH (§126), hourly 1643 HIGH (§127), hourly 1746 HIGH (§128), hourly 1843 HIGH (§129), user-provided 1936 HIGH (§130), Open-Jev densify (§125), hourly 1946 HIGH (§131), hourly 2049 HIGH (§132), hourly 2146 HIGH (§133), hourly 2246 HIGH (§134), hourly 2347 HIGH (§135), hourly 0049 HIGH (§136), and hourly 0151 HIGH (§137).

Each lock must appear as one consecutive substring in every listed overlay.
Fragments scattered across files do not count.

Revisit / since-last-look protocol (`notes.md` §122) is a consecutive
substring in the skill + research files (not a 21-overlay dump wall).
Hourly must treat revisit HIGH like novel HIGH. Star-noise is not a fold.

Also: YAML-parse SKILL.md frontmatter; notes.md owns §114–§137;
composition items 289–316, 322–329, 330–336, 337–352, 353–368, 369–384, 385–400, 401–416, 417–432, 433–448, 449–464, 465–480, 481–496, 497–504, 505–520, 521–536, 537–552, 553–568, 569–584, 585–600, and 601–616 exist;
findings batches #97–#119 exist. Items 317–321 stay unused.
The 1843 archive run_digest must claim §129 / 481–496 / #111.
The 1946 archive run_digest must claim §131 / 505–520 / #113
(not the 1746 IDs §128 / 465–480 / #110).
The 2049 archive run_digest must claim §132 / 521–536 / #114.
The 2146 archive run_digest must claim §133 / 537–552 / #115.
The 2246 archive run_digest must claim §134 / 553–568 / #116.
The 2347 archive run_digest must claim §135 / 569–584 / #117.
The 0049 archive run_digest must claim §136 / 585–600 / #118.
The 0151 archive run_digest must claim §137 / 601–616 / #119.
CHANGELOG.md must not hold uniqueness dump walls (dumps live in
changelog-hourly.md). README.md must not hold the 0743 dump wall.
Pages greps stay in docs/index.md and docs/_layouts/default.html.
The 0843 ecosystem blurb cites notes.md §114. Does not fetch the
network. Does not treat a lock as a Harbor score.
"""

from pathlib import Path
import json
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
    "README.md",
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


def main() -> int:
    failed = []
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
    algebra = (ROOT / ".agents/skills/augustus/references/composition-algebra.md").read_text(
        encoding="utf-8"
    )
    for n in list(range(289, 317)) + list(range(322, 330)) + list(range(330, 337)) + list(range(337, 353)) + list(range(353, 369)) + list(range(369, 385)) + list(range(385, 401)) + list(range(401, 417)) + list(range(417, 433)) + list(range(433, 449)) + list(range(449, 465)) + list(range(465, 481)) + list(range(481, 497)) + list(range(497, 505)) + list(range(505, 521)) + list(range(521, 537)) + list(range(537, 553)) + list(range(553, 569)) + list(range(569, 585)) + list(range(585, 601)) + list(range(601, 617)):
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
        if meta.get("version") != "0.5.0":
            failed.append(
                f"SKILL.md metadata.version {meta.get('version')!r} != '0.5.0'"
            )
        desc = fm.get("description") or ""
        haystack = desc + "\n" + skill
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
        ):
            if frag not in haystack:
                failed.append(f"SKILL.md missing fragment {frag!r}")
        proto_line = ""
        for line in skill.splitlines():
            if "cascade sign-flip / calibration theater" in line:
                proto_line = line
                break
        if not proto_line:
            failed.append("SKILL.md protocol missing cascade sign-flip line")
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
    ):
        if lock in changelog:
            failed.append(
                f"CHANGELOG.md holds {name} uniqueness dump "
                "(v0.4.0: dumps live in changelog-hourly.md)"
            )
    if "Hourly 0743 uniqueness lock:" in changelog:
        failed.append("CHANGELOG.md holds 0743 uniqueness dump")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "Hourly 0743 uniqueness lock:" in readme:
        failed.append("README.md holds 0743 uniqueness dump (#33 map + later lock lines)")
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
        f"0049 chars={len(UNIQ_0049)} 0151 chars={len(UNIQ_0151)} "
        f"revisit chars={len(REVISIT_LOCK)} "
        f"overlays={len(OVERLAYS)} "
        f"revisit_overlays={len(REVISIT_OVERLAYS)}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
