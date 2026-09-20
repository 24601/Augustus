#!/usr/bin/env python3
"""Uniqueness gate for merged 0843 (§114), merged 0915 NanoJev (§115),
merged 0920 jcr (§116), merged 0922 SemIf (§117), merged 0940
llm-to-jev (§118), hourly 0947 HIGH (§119), hourly 1049 HIGH (§120),
and hourly 1143 HIGH (§121).

Each lock must appear as one consecutive substring in every listed overlay.
Fragments scattered across files do not count.

Also: YAML-parse SKILL.md frontmatter; notes.md owns §114–§121;
composition items 289–316, 322–329, 330–336, 337–352, 353–368, and 369–384 exist;
findings batches #97–#104 exist. Items 317–321 stay unused.
CHANGELOG.md must not hold uniqueness dump walls (dumps live in
changelog-hourly.md). README.md must not hold the 0743 dump wall.
Pages greps stay in docs/index.md and docs/_layouts/default.html.
The 0843 ecosystem blurb cites notes.md §114. Does not fetch the
network. Does not treat a lock as a Harbor score.
"""

from pathlib import Path
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
    algebra = (ROOT / ".agents/skills/augustus/references/composition-algebra.md").read_text(
        encoding="utf-8"
    )
    for n in list(range(289, 317)) + list(range(322, 330)) + list(range(330, 337)) + list(range(337, 353)) + list(range(353, 369)) + list(range(369, 385)):
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
    ):
        if batch not in findings:
            failed.append(f"findings.md missing {batch}")
    skill = (ROOT / ".agents/skills/augustus/SKILL.md").read_text(encoding="utf-8")
    try:
        fm = load_skill_frontmatter(skill)
    except Exception as e:
        failed.append(f"SKILL.md yaml.safe_load: {e}")
        fm = {}
    else:
        if fm.get("name") != "augustus":
            failed.append("SKILL.md name != augustus")
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
        f"overlays={len(OVERLAYS)}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
