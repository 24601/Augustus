# Validation: the design gate, eval recipes, and Jev-for-skills

## The gate (run before building)

1. Exact computation, semantic judgment, or both? Exact parts stay in code.
2. Can the right answer be represented? (candidate present? level exists?
   `other` option where coverage is open?) Missing `other` on an open
   coverage set forces a wrong Choice at confidence 1.00 — **confidence
   gating cannot catch it**. Lint the *request* (broken state paths,
   bundled judgments) before you trust the answer
   ([wellposed](https://github.com/suraj-phanindra/wellposed) recipe;
   `tenbin` owns the skill; `question-design.md`; `notes.md` §46).
3. Missing / contradictory / malicious / stale evidence — what happens?
4. Which constraints must code enforce regardless of model output?
5. What does each number mean — and which reading would be invalid?
6. Baseline + labeled cases + held-out split defined before tuning?
7. Rubric design, threshold selection, and final evaluation on separate data?
8. What triggers reevaluation? (model, rubric, source, or policy change.)

## Behavioral tests (measure; Jev promises no invariances)

Candidate removal (drop the winner — does probability spread sensibly?);
option-order shuffle; **letter-shuffle on screenshot Choice**
(blackwood-rlcd card: flip **0.133** vs Jev 1.13 text-only **0.587** on
300 web steps — vendor receipt, not re-run; `notes.md` §46); **irrelevant-option / IIA** (append an option that
should not move odds among the rest — Hume's reconstruction,
`research/notes.md` §31, not a new invariance the API promises);
public cousin for the read-the-letter graph:
[`Mikhail/mini-jev-runs`](https://huggingface.co/datasets/Mikhail/mini-jev-runs)
`read_letters_rotated_options` (scores not calibrated; `notes.md` §33);
**paraphrase pairs** (semantically equivalent
wording — does p swing enough to change the *act*? `mappings.md` §17);
irrelevant distractor injection in state; no-match and
empty-evidence cases; policy-boundary cases just above/below thresholds;
contradictory-output handling (operation says X, target says Y).
Game-loop cousin this hour: [`jev-plays-games`](https://github.com/vtrivedy/jev-plays-games)
`research/FINDINGS.md` — both option orders on six positions; Choice
probabilities are not win odds; a 0.50 confidence gate would have
rejected two correct mates (`notes.md` §42).
149-row cousin: [`typesafe-jev-tools`](https://github.com/wotai-dev/typesafe-jev-tools)
— Jev confidence monotonic vs Haiku invert in 0.80–0.95; do not copy
the hook.
Open reconstruction cousin: [`jaredpalmer/kev`](https://github.com/jaredpalmer/kev)
— isolation packed vs separate max Δ 3.7e-6; secret-in-sibling p=0.03
vs in-state 0.99; permute argmax flips 7.4%; IIA log-odds shift mean
0.13; boundary forgery held. Those tests mirror Archer probes; they do
not prove kev = Jev (`notes.md` §45). Hub fetch path this pass:
[`jaredpalmer/kev-0.5b`](https://huggingface.co/jaredpalmer/kev-0.5b)
(`--run` accepts Hub ids). Dedicated `none_of_the_above` eval (true
option present vs removed) is the training-side cousin of wellposed's
request hatch; **no published rates this pass** (`notes.md` §45 delta).

## Offline eval: selective binary decisions

Run `scripts/evaluate_decisions.py` on application-exported JSONL
(`{id, p, y, group}` + optional baseline `p_base`, costs). It reports Brier
score, reliability bins with counts, and coverage/FP/FN/cost across
thresholds. Rules: select thresholds on split A, report final numbers on
split B; no universal pass mark; missing labels/costs → stated limitation,
never invented defaults. Ranking/search metrics stay checklist-level until a
real application justifies executable support. A complementary labeled-case
workbench for running Jev questions (Noul / Choice / Score) and comparing
runs is [dayhaysoos/jevals](https://github.com/dayhaysoos/jevals) (MIT,
local; WebMCP + agent skill; not affiliated with TypeSafe) — the empirical
acceptance-test *surface* for Hypothesis mapping cards; this script remains
the offline Brier / reliability / cost evaluator. Pointer only
(`research/notes.md` §24); Augustus is not a jevals how-to. Hygiene,
the Harbor substrate, and the one composition table are **Eval &
hill-climb** below — do not restate them here. A bake-off
candidate on that same labeled-case surface, beside Laya, openjev-lm,
TypeAR, and [kev](https://github.com/jaredpalmer/kev), is
[Bespoke Nimble](https://github.com/bespokelabsai/nimble)
— an open LoRA recipe, not a Jev distill; their 324-example holdout is
a named receipt, not a ranking (`research/notes.md` §35). kev is the
runnable Archer-reconstruction candidate on the same surface (public
gold, measured ID ECE, not a teacher-copy; `notes.md` §45). Same
acceptance-test *surface*, different UI:
[jeiel85/jevscope](https://github.com/jeiel85/jevscope) (local-first
visual debugger + JSONL regression; policy buckets are JevScope-derived,
not Jev answers). Pointer only; do not copy ports or env into skill cards.
Online, full-traffic cousin (not a Harbor replacement):
[`memovai/openevals`](https://github.com/memovai/openevals) grades every
step then writes scores back to Langfuse; code graders first.
`notes.md` §42.

## Jev for agents and skills (dogfooding)

- **Skill routing**: for large rosters, copy the skill_suggestion shape — one
  request ranks all skills (Choice over index descriptions) plus gate nouls
  for whether any skill fits; a second request reranks the top-3 with full
  descriptions and per-candidate fits-nouls that may reject all. Suggest at
  most one skill; keep the suggestion overridable so prefix caching holds.
- **Self-monitoring tool calls**: after an agent acts, ask decomposed Nouls
  over {request, tool schema, trace}: right tool? arguments match schema?
  result matches call? units/dates verified in code? Escalate on low
  confidence, never auto-retry blindly.
- **Grounding/citation checks**: one Choice (supports / contradicts /
  unrelated) per claim-evidence pair plus a confidence review flag; verify
  against source documents, never against another model's prose.
- **Testing a skill**: define the skill's decision surface (which judgments,
  which policies), build labeled cases per judgment, run the gate's
  behavioral tests, and score with the evaluator script. A skill passes when
  its card's falsifying experiment fails to reject it — not when a demo
  looks clever.
- **Modularity**: one skill per decision-design responsibility; share
  reference files instead of forking near-duplicate skills; prefer a thin
  router (rank-then-verify) over hundreds of micro-skills AND over one fat
  skill. Merge two skills when their design cards are identical except nouns.

## Threshold non-transfer (Empirical, FirasSX914/calibre)

Calibration and routing thresholds measured on one dataset do **not** transfer to
another — and neither does routing's ROI. calibre: Banking77 Jev→DeepSeek route @0.67
gives 80.2% at $0.103 vs Jev alone 77.8%@$0.051; on Web of Science the same routing
ties Jev alone (52.8% both) for 46% more money. The optimal threshold, the sign of
the model gap, and whether routing pays at all all flipped. Rule: every gate/threshold
is a per-dataset measurement, not a constant. Re-measure on your data before shipping
and re-measure when the distribution shifts; treat any borrowed threshold as a prior,
never a setting.

## Shadow mode before gating

Adoption pattern (AntonioCoppe/jev-harness): run the Jev judgment in parallel with
the live system and only **log what you would have done** (policy + gate applied)
until behavioral evals over replayed fixtures pass; then flip to enforcement. Assert
on the *action* (block/warn/pass), not on free text. This is the safe path for any
confidence gate added to an existing pipeline. Harbor/jevals-adjacent
practice, not a second eval product: LLM-as-judge is not the primary
System One score (`faq.md`). Recipes in that repo (alerts, RTB, sports-bet,
prediction-markets) are existence proofs of the same substrate across
business and life, not SWE-only (`notes.md` §44). Do not copy the client.

## Frontmatter (by agents and by Jev rankers)

- `name`: gerund, hyphenated, matches directory; specific over clever.
- `description`: third person, what + when, with the trigger terms users
  and rankers actually emit (e.g. name the primitives: Choice, Score, Noul;
  name the jobs: routing, reranking, verification, decomposition).
- Write descriptions like Choice criteria: `what` it covers, `not_for` its
  neighbor, examples of triggering requests. Distinct descriptions are a
  retrieval feature — the skill_suggestion cookbook shows lookalike
  descriptions are the top failure source.

## Perception → decision: pipeline, measure, hill-climb (Hypothesis)

Upgraded into **Eval & hill-climb** below — one section, not two essays.
The one-liner is kept there: Taskset first → stage contracts → stage
metrics + e2e → HoH hill-climb; DSPy/Ax only on the LM-program slice;
jevals/calibration for the decision slice; Harbor for product e2e.
Stages, IDF1, frozen taskset, and the climb axes live in that section.
Pipeline note: `notes.md` §41. Harbor and jevals hygiene: `notes.md` §40.

## Eval & hill-climb

Canonical measurement home. Jevals falsifies the **decision stage**.
Harbor, read with Will Brown's taskset × harness × runtime split, is
the ideal substrate for the **product loop**. This is design-judgment
hygiene, not a Jev wrapper, not a jevals tutorial, and not a Harbor
install guide. The workbench is external
([dayhaysoos/jevals](https://github.com/dayhaysoos/jevals), pin `af6fecc`).
Flags, keys, and ports stay in that README. PRODUCT.md at that pin says
no npm publication has been performed, so do not treat a package name
as an install path.

**Order.** Taskset first → stage contracts → stage metrics + e2e → HoH
hill-climb; DSPy/Ax only on the LM-program slice; jevals/calibration
for the decision slice; Harbor for product e2e.

### Pipeline (upgraded from the shorter hill-climb card)

**Hypothesis.** Basit ask, primary post not retrieved. This is how you
measure the perception-then-judgment composition
(`judgment-class.md`, `notes.md` §39), not a second composition
doctrine and not a SAM, ASR, DSPy, or Ax how-to.

Stages, not one blob: (1) perception (SAM 3.1 / ASR / OCR) → schema'd
objects, tracks, utterances; (2) optional fusion in code; (3) decision
(Choice / Noul / Score) → typed marginals; (4) policy — thresholds,
abstention, escalate — in code, never inside the scorer. The handoff
from (1) to (3) is a **versioned contract**. Property-test it
(`formal-methods.md`). Meijer: marginals at (3); joints across stages
live in code. Atallah's low and medium buckets are those typed
decisions when they really are decisions — product rhetoric, not a
meter. "Review this PR" is still partly generative. "First model ever"
is a claim. A Noul is not over raw pixels. Fail-open is not universal.

Measure before any optimizer. Stage metrics: IoU, track IDF1, word
error rate; decision accuracy plus Brier or ECE plus option-order
sensitivity; policy regret under a cost matrix you wrote. End-to-end
is task success on a **frozen taskset**. Falsifiers: contrastive pairs
(Nimble-style, a falsifier not a training tutorial); garbage-in (a bad
mask or transcript must not look confidently correct); TOCTOU between
perceive and act.

Hill-climb axes, apart from each other: perception quality; the state
schema; the decision backend (Jev vs TypeAR vs Nimble vs `openjev-lm`);
thresholds and abstention; and, only when end-to-end gains stall on
interface loss, a native multimodal System One. Climb latency and cost
separately from quality. The loop: the Planner writes a bounded change
from evidence; the Developer changes one stage or one interface; QA is
read-only and black-box on the frozen taskset and emits the next
evidence (`notes.md` §41). The HoH line later in this section (Planner
writes no code) is the same ask's other paraphrase — keep both.
DSPy/Ax stay on the LM-program slice
(`optimizer-integration.md`) — narrow yes, not a call shape.

### Jevals practices (decision-stage falsification)

[dayhaysoos/jevals](https://github.com/dayhaysoos/jevals) (MIT, local,
not affiliated with TypeSafe) sits next to a design card as the
acceptance surface. Complements `scripts/evaluate_decisions.py`. Files
fetched at `af6fecc`: README, PRODUCT.md, DESIGN.md, and
[`skills/jevals/SKILL.md`](https://github.com/dayhaysoos/jevals/blob/af6fecc0776dd5d97d5dc89fc0a72cae5e3e2580/skills/jevals/SKILL.md).
Paraphrase only. `notes.md` §40.

1. **Independent answer keys.** Derive each expected answer from the
   criteria and the case evidence *before* a run. Never copy a model
   prediction into a label to raise accuracy. Model-generated keys are
   proposals until a person reviews them. Say who reviewed them.
2. **Primitives.** Noul, Choice, Score, and mixed questions share case
   state. Stable question IDs connect the definition, the case
   expectations, and the results.
3. **Correctness is not confidence.** Confidence describes the
   distribution; it does not establish correctness. Report both.
   Choice: accuracy and multiclass Brier. Score: mean absolute error
   and a within-tolerance rate. This composes with the existing
   readout: Choice `confidence` `(p_max−1/K)/(1−1/K)` is a transform
   of the distribution, not a second learned score (`notes.md` §31,
   FAQ). A peaked distribution can be wrong. ECE in the table below is
   a metric this skill wants, not a number Nimble published — their
   holdout was agreement on synthetic labels (`notes.md` §35).
4. **Held-out discipline.** Reserve independently reviewed held-out
   cases before looking at predictions. The agent skill states there
   is no dedicated split control: use a separate held-out Jeval with
   equivalent questions, and do not tune against it. README,
   PRODUCT.md, and DESIGN.md do not document a built-in train/held-out
   split either. Development examples are not held-out reliability.
5. **Compare only compatible datasets.** Same case set, and only fully
   successful runs. Ranking is question-scoped. Do not blend accuracy
   across unrelated questions or Jevals.
6. **Immutable runs.** Inspect the exact run ID and the definition
   snapshot that executed. A current draft may differ. Do not tune
   against held-out.
7. **Ambiguity.** If the evidence or the criteria cannot determine an
   answer, surface it for review. The agent skill forbids an
   unsupported `unknown` label; DESIGN.md: an unset expectation blocks
   a run. Do not invent an abstain label.
8. **Agent workflow.** The workbench skill's WebMCP loop, in order:
   discover the workspace → define the judgment → author independent
   keys → save and verify the saved revision → run only inside the
   authorization already given → inspect that exact run. One pointer
   to the skill above. Do not copy it, and do not copy its tool names
   into this card.

### Harbor as the ideal substrate

Harbor was not named in this repo before this section. **Basit ask,
primary post not retrieved** (no tweet id). The bullets that the
fetched docs do not state are labeled as that ask. Do not invent a
second Harbor, and do not invent a Harbor CLI.

Verified:

- [harbor-framework/harbor](https://github.com/harbor-framework/harbor)
  README: a framework from the Terminal-Bench creators for evaluating
  and optimizing agents and models — arbitrary agents, shared
  benchmarks, parallel environments, rollouts for RL.
  [Task docs](https://www.harborframework.com/docs/tasks): by default
  the verifier runs in the same container as the agent. A separate
  verifier environment exists when grading code must not be visible
  to the agent; sidecar evidence can be pulled from a filesystem the
  agent container cannot write.
- [PrimeIntellect-ai/verifiers](https://github.com/PrimeIntellect-ai/verifiers),
  originally Will Brown. The
  [v1 post](https://www.primeintellect.ai/blog/verifiers-v1)
  (Will Brown, Mika Senghaas, Florian Brand, 2026-07-10) splits an
  environment into a **taskset** (data, tools, and scoring), a
  **harness** (the program that rolls out: a loop, a coding-agent CLI,
  or your own), and a **runtime** (local process, container, or a
  sandbox). A taskset runs under compatible harnesses. Harbor is the
  first fully supported third-party *taskset format* inside verifiers
  — one substrate, not two products.

Rules:

- **Taskset = what to do + tools + how to score** (the product claim).
  Write the score before picking a model. Scoring lives on the task;
  the harness only rolls out. The "before the model" clause is the
  Basit ask; the blog is what puts scoring on the taskset.
- **Harness is swappable.** Blog examples are a loop or a coding-agent
  CLI. A Room driver is the Basit ask, not a Harbor agent this pass
  verified. Same taskset under more than one harness. If only one
  harness passes, you measured the harness.
- **Runtime is swappable** (local, container, sandbox). A live Room is
  the Basit ask for the third seat, not a runtime name in the v1 post.
- **Independent validator.** Use Harbor's separate verifier environment
  when the worker must not see or rewrite the grade. The default
  shared container is not that guarantee.
- **HoH loop** (Basit ask, primary post not retrieved): Planner writes
  no code, only a bounded change from evidence E → Developer is the
  single writer and changes one stage or one interface → QA is
  read-only and black-box on the frozen taskset and returns the next
  evidence. The next loop starts from (A, E).
- **Room / omni products** (same ask): structural gates first;
  video-as-judge last. Same sandwich as allowlist-then-remainder
  (`mappings.md` §18). Perception-then-judgment is composition;
  information dies at the act. A shared multimodal decide head still
  judges marked candidates, not an open click (`notes.md` §39, §46).
  LLM-as-judge is not the primary score for a
  calibrated System One. Shared bake-off exemplar:
  [open-jev-laya-bench](https://huggingface.co/datasets/pngwn/open-jev-laya-bench)
  (ECE/NLL/Brier). Harbor-style class bake-off:
  [DMB](https://github.com/nibzard/decision-model-benchmark) (v2).
  Public log feedstock:
  [jevals-data](https://github.com/Jevals/jevals-data) (CC-BY-4.0).

### Composition

| Layer | Tool | Scores |
|---|---|---|
| Decision stage (typed marginals) | jevals (+ contrastive pairs / Nimble-style) | accuracy, Brier/ECE, latency/$, traces |
| Perception→state contracts | schema PBT + stage metrics (IoU/WER) | interface falsifiers |
| End-to-end product / agent loop | Harbor taskset | behavioral assertions, cost/perf bounds |
| LM-program knobs only | DSPy/Ax (narrow) | never primary System One calibration score |
| Reward-hack / eval gaming | [rh-guard](https://github.com/24601/rh-guard) | structural deny + System One sidecar |
| Project soft-rule lint | [Abide](https://github.com/coldteadotai/abide) | Score per rule on the diff; bands; fail-open; replay + independent review |
| Collab / computer-use product loop | [jev-testbench](https://github.com/ufx7/jev-testbench); [solari-reflex](https://github.com/hitakshiA/solari-reflex); [gliner2-ultrafast](https://github.com/sahibzada-allahyar/gliner2-ultrafast); [cua-s1](https://github.com/trycua/cua/tree/main/libs/cua-s1); [Stagehand #2955](https://github.com/browserbase/stagehand/pull/2955) | Wilson/McNemar arms; independently checked task time; `DONE` ≠ success; Cua-S1 source-only (metric names, no checkpoint scores); Stagehand 37/75 no-LLM ~0.5s vs 4.37s *their* card; pick ≠ replacement; draft |
| Agent routing on vs off | [jev-gateway-bench](https://github.com/vinilana/jev-gateway-bench) | Hidden perft; cost/quality; one-run signal this pass |
| Command-output prune (needle/noise) | [jev-pruner](https://github.com/tamaratran/jev-pruner) | Manual `trimOutput` sweep (theirs); plugin eval cannot reach Jev (fail-safe original); Terminal-Bench paired pilot is integration, not a full bench |
| Pre-registered cascade vs nano/frontier/encoder | [jev-baselines-eval](https://github.com/ickma2311/jev-baselines-eval) | Both experiments **AMBIGUOUS**; cascade sign-flip at exact parity; confidence=1.0 theater; encoder 0.933/9ms with labels; serving-path ≠ model-speed; same-day errata ×3 |
| Healthcare S1+S2 (synthetic FHIR) | [explore-typesafe-ai](https://github.com/si618/explore-typesafe-ai) | Labels committed first; 60 requests / 403 judgments; **not clinically validated**; Claude wrote labels |
| Precision PDF (honest negative) | [databricks-jev-pdf-lab](https://github.com/laurentfabre/databricks-jev-pdf-lab) | No quality-equivalent Jev payoff; no OSS license selected |
| Meaning-search without embeddings | [jevgrep](https://github.com/Bentlybro/jevgrep) | 228-q stripped Flask/httpx/Django/AutoGPT: 79% top-5 vs BM25 40% / grep 20%; keyword still wins exact (BM25 top-10 96% vs 85%); not a Harbor taskset |
| RAG rerank vs generative rerank | [Jev-RAG](https://github.com/Max-sm-yc/Jev-RAG) | One-run ~30k tokens: ≥70% cost / 72% latency vs Spark *rerank*; full-context Spark still 10.60 s; costs include embeddings |
| Skills→oxlint remainder | [jev-oxlint](https://github.com/cephalization/jev-oxlint) | Phoenix: answer-key agree on every fixture; routing 0.80–0.94 vs <0.50; coarse hint not; experiment; not a hard gate |
| Native-probability calibration (analytic worlds) | [jev-arena](https://github.com/meetr1912/jev-arena) | Live *theirs* (`jev-1.13.0`, 145 noul, 2 req / 710 ms): Brier 0.0059, log loss 0.5393, ECE 0.0620; overconfident in low bins; always-0.5 Brier 0.0766. Oracle stub 0.0000. Fan-out economics. Offline default |
| Fan-out suite (heatmap / CDF / bracket) | [jev-sonar](https://github.com/meetr1912/jev-sonar); [jev-vickrey](https://github.com/meetr1912/jev-vickrey); [jev-bracket](https://github.com/meetr1912/jev-bracket) | Sonar: heatmap-as-policy; offline 75% win / Brier 0.1615; live 1-game Brier 0.1092. Vickrey: Jev never bids; live Brier 0.1391 / ECE 0.1321; oracle regret 0. Vickrey live second-price profit −163.4. Bracket: live Brier 0.2853 vs Elo 0.2322 (trailed Elo; honest) |
| Typed control plane vs DSPy / JSON Schema | [jev-dspy-control-plane](https://github.com/manikanda-kumar/jev-dspy-control-plane) | Same ontology/dataset/state/allow-list/metrics; intent/sub-intent, invalid/policy-violation, abstention/coverage, Brier/ECE, consistency, p50/p95. Offline heuristic ≠ quality |
| Tetris legal-set Choice vs Haiku | [jev-tetris-benchmark](https://github.com/planstack-ai/jev-tetris-benchmark) | Use-case demo; code enumerates ≤12 legal placements; **not a rigorous eval** |
| Domain specialist vs few-shot hosted | [Domain-jev-maker](https://github.com/help-er/Domain-jev-maker) | Independent CLINC gold (not Jev teacher). Matched-precision KL (2-decimal, zeros→0.0025): local 0.168 vs hosted 0.580 banking; r +0.933 vs +0.343. Few-shot hosted determinate McNemar n.s. (p=0.134 / 1.000). Train specialist when policy reads p |
| Cascade compare arms (native vs verbalized vs logprob) | [jav-email-cascade](https://github.com/skiingfalcon/jav-email-cascade) | 74 labelled emails; jev / gen-json / gen-logprob; shared Answer schema. Mock: gen-json confidence flat. Noul 0.5 never rounded. License null. **Not** a live Jev vs Haiku bake-off |
| ORDER BY ranking vs calibration | [jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench) | `jev-1.13.0` six gates pass. Boolean inversion 0.036; Score ordinal **0.143** vs 0.15; 53-way 0.99 tie; ECE 0.0453 / Brier 0.0524. recodelabs batch-40 inversion 0.171 **fail**. Calibration ≠ sortable |
| Class-backend economics (GLiFormer `/v1/systemone`) | [jeff](https://github.com/logan-markewich/jeff) | 1,600 items. L4 HTTP ~$2.6 vs jev ~$15.6 (~6×); A10G direct ~$0.65 (~24×); AG News 75.5% vs 90.5%; p50 151 vs 129 ms. CPU 6–20× *more* expensive. Encoder ≠ Jev replica. License null |
| Jev vs local MLX PCD vs AR JSON | [system-one-benchmark](https://github.com/mallahyari/system-one-benchmark) | LMSYS toxic-chat **n=50**. Jev-1.13.0 **84.0%** acc / Brier **0.1096** / p50 356.5 ms; PCD Qwen2.5-1.5B 52% / Brier 0.3884 / p50 227.2 ms / 1 pass O(1); AR 54% / ~30.8 passes / 98% schema errors. License null. Small n — *their* card, not a large Harbor taskset. PCD O(1) ≠ calibrated Noul |
| Evidence-packet explorer (SWE finish) | [jev-semantic-explorer](https://github.com/jimmyhealer/jev-semantic-explorer) | Author-run. Claude Code 6.8→2.2 files / 8.6→3.2 tools. SWE-bench Verified n=8: **1/8 → 6/8** finish (empty = miss). Packet n=50 HitFile 0.233 vs BM25 0.159 — diagnostic, not product KPI |
| Meaning-grep LLM-as-judge | [jev-semgrep](https://github.com/uehaj/jev-semgrep) | 10 cases × 51-line EN/JP corpus. Precision 0.94, recall 0.98 *theirs*. Not a Harbor taskset |
| Closed-vote CU worked example | [JevOnly](https://github.com/buluoray/JevOnly) | 11 steps / 43 Jev calls / ~340k tok / ~$0.014 / 17 s *theirs*. No planner LLM. Not a bake-off |
| Host-owned product evals | [waymode](https://github.com/mossburgh/waymode) | 24/26 public suite; 34/36 completion regression *theirs*. Bounded development evidence, not a self-driving proof |
| OMP prompt suppression (permission vs probability) | [omp-greenlight](https://github.com/SemetricLabs/omp-greenlight) | 1,013 gated calls / 10 sessions / 8.95 h. Default **40.9%** prompts removed; **0 of 94** unsafe auto-approvals on 140-row corpus. Live traffic unlabelled. Operator owns bar. Not a sandbox. ~$0.05 / 1,013 *theirs* |
| Jev question as if-statement (instrument not score) | [dinostomp](https://github.com/collapseindex/dinostomp) | `dinostomp jev`: accuracy, p(yes) cut, ECE, blank-input lean, rewording flips. Demo *theirs* 24 examples: 100% / ECE **0.062**. FINDINGS 189 (F 52 / D 99 / N 38); 99 against itself. Beside jevals, not a Harbor taskset |
| SLO routing latency cost (sync Jev vs local features) | [slo-router](https://github.com/zeeshan8281/slo-router) | Live Jev vs `slo_no_jev` on sim backends. Same routes (fast 4 / strong 4) and 100% accuracy; p95 E2E **77.93 → 490.38 ms** (~6.3×). Jev feature p50 453.58 / p95 1257.50 ms. 16/16 Jev calls; no lexical fallbacks. 3/8 task-label disagreements did not change routes. Eight-row demo is **not** a benchmark. License null. *Their* integration card |
| Effect-based shell-gate certification | [construct-auto-classifier](https://github.com/godspede/construct-auto-classifier) | Main 113 + blind 82; 5 passes; **975 decisions/model**. Jev: **0** dangerous allowed, 100% caught, 99.5% correct, $0.047/1k. Every chat model leaked 16–104 dangerous. Only Jev certified. Through the whole gate, not a Harbor taskset |
| Docs-derived instruct seed | [INSTRUCT_JEV](https://huggingface.co/datasets/ctaxnagomi/INSTRUCT_JEV) | 119 rows (47 choice / 51 noul / 21 score); 24 typed question blocks / 7 typed answers. MIT. Open-replica / jevals seed. Not a bake-off |
| Evidence-gated question packs | [jev-packs](https://github.com/dtduc-git/jev-packs) | Nine packs `verified` on pinned `jev-1.13.0` *theirs* (single-run). citation-support 800 / acc 0.919 / ECE 0.022; banking-intent 150 / 0.840 / 0.090. `unknown` mandatory. jevassert **not released** (404). CC0. Not a Harbor taskset |
| Ranking ≠ calibration (human annotations) | [does-jev-confidence-mean-anything](https://github.com/Adilmp/does-jev-confidence-mean-anything); [jevcal](https://github.com/Adilmp/jevcal) | 8,000 judgments, `jev-1.13.0`, $0.05. AUC **~0.91**; stated **~75%** vs human **~10%**. Recalibration removes **~96% ECE**, AUC unchanged. `natural`/tightened ECE 0.156 → 0.006. jevcal: ~100 rows (94% of error). ECE gameable (constant base-rate ECE 0). License null / MIT. One domain; do not cite `threat` (n=1) |
| Hot-click CU vs per-step LLM | [ego-jev](https://github.com/jiangkoumo/ego-jev) | Alternate 3-round medians *theirs*: HN 4.9 s vs 9.7 s; wiki 5.4 s vs 10.1 s (~2×). n=3; high variance (control 7.3–22 s). **Not a benchmark.** MIT |
| Verbatim compact vs truncate vs summarize | [jev-compactor](https://github.com/edwardyen724-g/jev-compactor) | One synthetic 64-msg / 12.7k-token session, 6k budget, `jev-1.13.0`. 64.5% / 366 ms / $0.0004 / 0 hallucinated paths / 4 of 4 facts vs truncate 53% / 1 of 4 vs Sonnet 96.2% / 6.1 s / $0.0305 / 1 invented path. MIT. Not a survey |
| Receipts-not-leaderboard capability map | [jev-capability-atlas](https://github.com/Zaious/jev-capability-atlas) | Hold vs break with API receipts; not a ranking. Type-safe ≠ correct (DAIR Emotion 48% / mean conf 0.819). Axis already §49; 10★ this pass. README MIT / GitHub NOASSERTION |
| Jev vs thinking-budget Qwen3.5 | [jev-frontier-100](https://github.com/softpudding/jev-frontier-100) | 100×3; Jev **77.0%**; 4B off 56.0% / 512 78.3% / 2048 **96.7%** (+12.7 to +26.7). 2B/2048 82.0% (−2.3 to +12.3). Exploratory, not preregistered. MIT. Not a ceiling |
| OOD calibration / sign by type | [jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration) | 900 synthetic + 3,721 public; ~$0.06. Public OpenBookQA ECE 0.024 / T 0.96. Synthetic all ECE **0.107 = 4.4×** floor; priority 44.7% / mean p 0.74 / T **3.40**; boolean T **0.66**. MIT. Gateway has no model version |
| Memory-lease invalidation | [invalidate](https://github.com/chopratejas/invalidate) | 157 labeled cases *theirs*: 89.2% strict / 97.5% lenient / **0 of 157** false invalidations. Six Nouls then code. Apache-2.0. MED |
| Cost-aware PR prune (pilot) | [prune-review](https://github.com/shubhangi013/prune-review) | 22 paired runs: winning-only 27.9% (post hoc); all 22 incl. 305% outlier **1.18%**; excl. outlier 15.9%. Cost not quality. Source preview |

rh-guard is a reward-hack hook, a different surface from jevgate and
from Abide (eval-integrity vs allowlist-remainder vs project soft
rules). One row each. [dinostomp](https://github.com/collapseindex/dinostomp)
is the **instrument** auditor beside that row: data/scorer/runs/claims,
plus `dinostomp jev` if-statement hygiene for a TypeSafe question
(`notes.md` §62). ECE above is wanted, not a Nimble result.
Abide replay (author-reported, not re-run; `notes.md` §47): 93
sessions, 1,256 edits / 147 turns; independent-reviewer precision
**edit ~26% / turn ~73%** before calibrate/tune. Harbor-adjacent
measurement (frozen transcripts, phase split, independent
confirmation), not a Harbor taskset and not a jevals substitute.
Turn-phase soft rules held up better; false positives mostly fixable
in the rubric. Text/diff only.

**Harbor-style computer-use receipt this hour:**
[solari-reflex](https://github.com/hitakshiA/solari-reflex) scores
the *task* (Stripe API / answer key), not a paragraph judge. Observe
→ decide → verified act; no screenshots. Author table vs Codex on
the same Solari machines: 60.2 s vs 194.9 s; 66 s vs 460 s; 24.2 s
vs 98.4 s (`notes.md` §48). Encoder-backend cousin:
[gliner2-ultrafast](https://github.com/sahibzada-allahyar/gliner2-ultrafast)
— same hole, local GLiNER2; their Flights demo (12.20 s visible /
13.785 s loop / ~$0.0001 API) is a **demonstration**, not a bake-off
or a vs-Jev-Ultrafast table; `DONE` is not the Harbor score
(`notes.md` §52). Specialist-form cousin, **not TypeSafe Jev:**
[Cua-S1](https://github.com/trycua/cua/tree/main/libs/cua-s1) —
option-attention among observed elements; plan ≠ execute; dry-run
default; source-only this pass. Offline utilities *name* accuracy,
abstention, coverage, wrong actions/targets, and unsafe-when-should-
abstain; **no checkpoint scores**. Tests exercise implementation, not
quality. Do not invent a vs-Jev table. Watch for `cua-s1-form-v0`
(`notes.md` §54). **Harness extract card (their PR body, not
re-run; 2026-09-19 ~00:48):**
[Stagehand #2955](https://github.com/browserbase/stagehand/pull/2955)
— gemini-3.8-flash, Browserbase, local, 25 tasks × 3: 69/75 vs
23/25 baseline (92% both). **37/75** no-LLM in **~0.5 s** vs
baseline **4.37 s** and two LLM calls; LLM-off **36/75**. Pick is a
**fast path, not a replacement.** Draft stack #2951–#2955. In-sample
thresholds on the act suite (#2953). Not Harbor. Do not merge with
solari / Flights / Cua-S1 clocks (`notes.md` §57).
**Collab-arm curriculum:**
[jev-testbench](https://github.com/ufx7/jev-testbench) —
`llm_autonomous` vs `scripted_plus_jev` vs `llm_plus_jev`; Wilson +
McNemar; Jev is not a peer arm. Bake into jevals/Harbor hygiene, do
not copy the harness.

**Harbor on/off routing (Empirical as a *shape* and as a one-run
signal, not a measurement; 2026-09-18 ~16:48).**
[jev-gateway-bench](https://github.com/vinilana/jev-gateway-bench)
(MIT): real coding agents on chess-engine tasks; Jev routing on vs
off; hidden perft verifier the agent never sees; fresh gateway per
run. Author: first signal, not a measurement; <5 runs/mode the
summary says so. Preliminary `chess-bugfix` Codex: both 36/36
checks; on 4 LLM req / 76,678 in / 35 s vs off 6 / 118,709 / 88 s;
Jev 4 calls ~$0.0008. A cheaper unsolved run is not a saving. A
wrongly forced tool can derail a turn. Product sibling
[jev-gateway](https://github.com/vinilana/jev-gateway) fails open if
Jev is down. Pair CI merge-gate
([latch](https://github.com/CaseReed/latch)) with this substrate
(frozen JUnit artifacts × PASS/BLOCK) and rh-guard (eval-integrity).
Do not copy npm/ports (`notes.md` §51).

**Pre-registered independent eval (Empirical as Harbor/jevals
*practice*, including the honest negative; 2026-09-18 ~17:48).**
[jev-baselines-eval](https://github.com/ickma2311/jev-baselines-eval)
(MIT): kill/go printed by the scripts; **both AMBIGUOUS**. CLINC150
Jev 0.870 vs nano 0.795 vs Terra 0.915. Banking77 encoder **0.933 /
9 ms** wins. Cascade Δ +0.265 at 1pp-below-frontier; **at exact
parity the sign flips** (R_jev=1.000) because confidence is exactly
1.0 on 102/200 including 6 wrong. AUROC neither direction; **no
ECE**. Latency ~2.2× of two serving paths, not 40–200×, not
model-speed. Same-day errata three rounds. Do not copy pip
(`notes.md` §55).

**Healthcare Harbor-shaped receipt (Empirical as that named
report; not clinical validation; 2026-09-18 ~17:48).**
[explore-typesafe-ai](https://github.com/si618/explore-typesafe-ai)
— 100 synthetic Synthea patients; labels committed before any Jev
run; 60 requests to jev-1.13.0; Claude S2 blinded review. Report:
NEWS2 alone under-triaged 10/20, NEWS2+Jev 1/20; 403 judgments /
p50 329 ms / $0.0038. Claude wrote the labels. 20 cases/scenario.
**Not clinically validated.** License not in GitHub API this pass
(`notes.md` §55).

**Honest-negative PDF lab (Empirical as a negative; no OSS
license).**
[databricks-jev-pdf-lab](https://github.com/laurentfabre/databricks-jev-pdf-lab)
— no quality-equivalent end-to-end Jev payoff. Compact tokens
changed 26/236 recommendations. Public snapshot cannot reproduce
historical accuracy. Typed output is not truth (`notes.md` §55).

**Meaning-search Harbor-shaped card (Empirical as their stripped-
repo table; 2026-09-18 ~18:46).**
[jevgrep](https://github.com/Bentlybro/jevgrep): 228 questions on
Flask/httpx/Django/AutoGPT with docstrings and comments removed.
Right file in top 5: **79%** vs BM25 40% / grep 20%. Honest
negative: BM25 top-10 96% vs 85% when the exact wording is known.
Packed+parallel 0.9 s vs serial ~23 min on AutoGPT 4,329 files.
Frozen copies + labeled questions + comparable harnesses — not a
Harbor taskset, not Wilson/McNemar published. Do not copy
`install.sh` (`notes.md` §58).

**Measured RAG rerank vs generative rerank (Empirical as one-run;
Hypothesis as a transfer).**
[Jev-RAG](https://github.com/Max-sm-yc/Jev-RAG): RAG+Jev+Spark
$0.00122838 / 62.3 s vs RAG+Spark-rerank+Spark $0.00421838 /
228.14 s vs Spark full-context $0.0032 / **10.60 s**. ≥70% cost
and 72% latency vs Spark *rerank*, not vs no-RAG. Costs include
embeddings. License null. Do not invent a bake-off
(`notes.md` §58).

**jevals-shaped oxlint remainder (Empirical as Phoenix fixtures;
experiment).**
[jev-oxlint](https://github.com/cephalization/jev-oxlint): human
answer key vs Noul on every fixture (agree, wide margins); routing
sharp 0.80–0.94 vs <0.50 across 41 files; coarse hint not. Found
a real flush-only-on-success bug (noul 0.07). ~$0.002 / ~$0.015;
second run zero requests. Not a hard gate. `tenbin` owns the lint
skill (`notes.md` §58).

**Native-probability calibration arena (Empirical as their live
card; 2026-09-18 ~19:48).**
[jev-arena](https://github.com/meetr1912/jev-arena): analytically-
known worlds; native `noul`/`choice`/`score`, not verbalized
confidence. Live `--live --trials 200 --seed 7`, `jev-1.13.0`:
**145 noul**, Brier **0.0059**, log loss 0.5393, ECE **0.0620**,
**2 requests / 710 ms**. Overconfident in low bins. Oracle stub
0.0000. Cite as *theirs*. Fan-out suite: sonar heatmap-as-policy
(offline 20-game Brier 0.1615 / 75% win; live 1-game small
sample); vickrey threshold CDF (Jev never bids; live Brier
0.1391); bracket Brier vs Elo (live **trailed Elo** 0.2853 vs
0.2322 — honest). Harbor/jevals-shaped: exact oracle, proper
scores, teeth stubs, offline default (`notes.md` §59).
**Typed control-plane bake-off shape (Empirical as metric list,
not as a quality number):**
[jev-dspy-control-plane](https://github.com/manikanda-kumar/jev-dspy-control-plane)
shares ontology/dataset/state/allow-list across OpenJEV / DSPy /
JSON Schema. Offline heuristic + contract stubs are plumbing
regression, **not** model generalization. Accuracy alone is not
enough (`notes.md` §59).
**Tetris legal-set demo (not a rigorous eval):**
[jev-tetris-benchmark](https://github.com/planstack-ai/jev-tetris-benchmark)
— code enumerates ≤12 legal placements; Jev Choice vs Haiku.
Same hole as jev-plays-games (`notes.md` §59).

**Domain specialist vs few-shot hosted (Empirical as their
RESULTS.md; 2026-09-18 ~20:43).**
[Domain-jev-maker](https://github.com/help-er/Domain-jev-maker):
independent CLINC-150 labels, not a Jev teacher-copy.
Matched-precision KL (both rounded to two decimals, zeros →
0.0025): local 1.5B 0.168 vs hosted zero-shot 0.580 banking
(r +0.933 vs +0.343). Few-shot hosted determinate McNemar
n.s. (p=0.134 banking / p=1.000 travel). Train the specialist
when policy reads p; hosted+examples when only argmax. Do not
copy train how-to (`notes.md` §60).
**Cascade compare arms (Empirical as README + mock; not a live
Jev vs Haiku bake-off):**
[jav-email-cascade](https://github.com/skiingfalcon/jav-email-cascade)
— 74 labelled emails; jev vs gen-json vs gen-logprob on one
Answer schema. Mock: gen-json confidence essentially flat.
Noul 0.5 never rounded. License null this pass (`notes.md` §60).
**ORDER BY ranking family (Empirical as independent
measurement):**
[jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench)
— `jev-1.13.0` passes six pre-registered gates. Boolean
inversion 0.036; Score ordinal **0.143** vs 0.15 (weak link /
sort key); 53-way 0.99 tie; ECE 0.0453 / Brier 0.0524.
recodelabs batch-40 **fails** ranking (inversion 0.171).
Calibration ≠ sortable. Request shape is part of the
measurement (`notes.md` §60).
**Class-backend economics (Empirical as their RESULTS.md):**
[jeff](https://github.com/logan-markewich/jeff) — GLiFormer-400M
`/v1/systemone`. 1,600 items: L4 HTTP ~$2.6 vs jev ~$15.6
(~6×); A10G direct ~$0.65 (~24×); AG News 75.5% vs 90.5%; p50
151 vs 129 ms. CPU 6–20× *more* expensive. Encoder ≠ Jev
replica. License null this pass (`notes.md` §60).

**Harbor Jev vs local MLX PCD vs AR JSON (Empirical as their
README table; 2026-09-18 ~21:39).**
[system-one-benchmark](https://github.com/mallahyari/system-one-benchmark):
`jev-1.13.0` vs Qwen2.5-1.5B 4-bit MLX PCD vs AR JSON on
lmsys/toxic-chat **n=50**. Jev **84.0%** acc, Brier
**0.1096**, precision 90.9% (1 FP), p50 356.5 ms. PCD 52% /
Brier 0.3884 / p50 227.2 ms / 1 pass. AR 54% / ~30.8 passes
/ 98% schema errors. **PCD proves O(1) speed; uncalibrated
likelihoods ≠ Noul.** License null. Clone URL still
`your-username`. Small n — *their* card, not a large Harbor
taskset. Cousin of DMB / open-jev-laya-bench / pcdServer /
jevify. Do not copy pip how-to (`notes.md` §61).
**Evidence-packet explorer (Empirical as their performance.md,
author-run):**
[jev-semantic-explorer](https://github.com/jimmyhealer/jev-semantic-explorer)
— SWE-bench Verified n=8: **1/8 → 6/8** finish (empty
output = miss); about half the model bill. Claude Code
6.8→2.2 files. Packet n=50 HitFile 0.233 vs BM25 0.159 is
**not** the product KPI. n=8 is small (`notes.md` §61).
**Meaning-grep judge test (Empirical as their report.md):**
[jev-semgrep](https://github.com/uehaj/jev-semgrep) precision
0.94 / recall 0.98 *theirs* (LLM-as-judge, cached verdicts).
Not Harbor (`notes.md` §61).
**OMP prompt suppression (Empirical as measured traffic +
labelled corpus; 2026-09-18 ~22:38).**
[omp-greenlight](https://github.com/SemetricLabs/omp-greenlight):
1,013 gated calls / 10 sessions / 8.95 h. Default **40.9%**
prompts removed; **0 of 94** unsafe auto-approvals on a
140-row corpus. Live traffic unlabelled. Operator owns the
bar; plugin never self-tunes. Not a sandbox. ~$0.05 / 1,013
*theirs*. Do not copy `omp plugin` (`notes.md` §62).
**Eval-instrument / Jev-as-if (Empirical as FINDINGS.md +
demo card; Harbor/jevals-adjacent hygiene).**
[dinostomp](https://github.com/collapseindex/dinostomp):
checks the instrument, not just the score. FINDINGS 189
(F 52 / D 99 / N 38); 99 against itself. `dinostomp jev`
demo *theirs* (24 examples): 100% accuracy, ECE **0.062**,
blank 'no' at 0.81, 0/60 rewording flips. Beside jevals,
not a Harbor taskset. Do not copy pip (`notes.md` §62).
**SLO routing latency cost (Empirical as live analysis
*negative* for sync Jev; 2026-09-18 ~23:40).**
[slo-router](https://github.com/zeeshan8281/slo-router):
sim backends + real Jev. SLO no-Jev p95 **77.93 ms** vs
SLO+Jev p95 **490.38 ms**; accuracy 100% both; same routes.
Jev disagreed on 3/8 task labels and did not change routes.
Author: keep Jev off the synchronous path for this
workload. Eight-row demo is not a benchmark. Harbor-style
ablation of decision-model latency. License null. Do not
copy uvicorn (`notes.md` §63).
**Effect-gate certification (Empirical as their report;
not a Harbor taskset).**
[construct-auto-classifier](https://github.com/godspede/construct-auto-classifier):
975 decisions/model; Jev **0** dangerous allowed; every
chat model leaked 16–104. Privilege ≠ verdict. Fail-closed.
Pair with dinostomp (instrument) before treating 0/975 as
class truth. Do not copy bun (`notes.md` §63).
**Instruct seed (feedstock, not a score):**
[INSTRUCT_JEV](https://huggingface.co/datasets/ctaxnagomi/INSTRUCT_JEV)
119 rows (47/51/21); 24 typed questions / 7 typed answers.
jevals-shaped open replica. MIT.
**Evidence-gated packs (Empirical as registry tables;
Harbor/jevals practice; 2026-09-19 ~00:39).**
[jev-packs](https://github.com/dtduc-git/jev-packs): nine
packs `verified` on pinned `jev-1.13.0` *theirs*
(single-run). No `evidence.md`, no endorsement. `unknown`
mandatory. Named runner jevassert is **not released**
(404). CC0. Distinct from INSTRUCT_JEV (no evidence gate)
and dinostomp (instrument). Do not copy uvx (`notes.md` §64).
**Ranking ≠ calibration (Empirical as human-annotated
audit + tool).**
[does-jev-confidence-mean-anything](https://github.com/Adilmp/does-jev-confidence-mean-anything):
8,000 judgments vs `civil_comments`; AUC ~0.91; stated
~75% vs human ~10%; ~96% ECE removed without rank change.
[jevcal](https://github.com/Adilmp/jevcal): ~100 labelled
rows; demo 0.9 → 33% on 1,600. ECE gameable — they decide
on Brier. One domain. Do not cite `threat` (`notes.md` §64).
**Hot-click CU (Empirical as n=3 medians, not a bench;
2026-09-19 ~00:39).**
[ego-jev](https://github.com/jiangkoumo/ego-jev): HN 4.9 s vs
9.7 s; wiki 5.4 s vs 10.1 s vs per-step `kimi-k3`. High
variance. Selector-hardcoded code beats both. Do not copy
`install.sh` (`notes.md` §65).
**Verbatim compact vs summarize (Empirical as one synthetic
session).**
[jev-compactor](https://github.com/edwardyen724-g/jev-compactor):
64.5% / 366 ms / $0.0004 / 0 invented paths / 4 of 4 facts
vs Sonnet summary 96.2% / 6.1 s / 1 invented path. Not a
survey. Was empty skip §61. Do not copy npm (`notes.md` §65).
**Eval integrity cluster (Empirical as their tables;
2026-09-19 ~01:47; not leaderboard theater).**
[jev-capability-atlas](https://github.com/Zaious/jev-capability-atlas)
receipts, not a ranking; type-safe ≠ correct (axis already
§49; 10★ this pass).
[jev-frontier-100](https://github.com/softpudding/jev-frontier-100):
Jev 77.0% vs Qwen3.5 4B/2048 96.7% (4B off 56.0%);
exploratory, attach the thinking budget.
[jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration):
900 tickets ECE 0.107 = 4.4× floor; priority unknowable
(44.7% / mean p 0.74 / T 3.40); sign flips by type.
Do not copy npm / Ollama (`notes.md` §66).

**Harbor-adjacent stdout prune (Empirical as README / evals README
behavior, not a full Terminal-Bench ranking; 2026-09-18 ~17:15).**
[jev-pruner](https://github.com/tamaratran/jev-pruner) ships
needle/noise graders and a Harbor Terminal-Bench 2.0 adapter in-repo.
Manual `trimOutput` sweep (theirs, 2026-09-18, 3 runs, `jev-latest`):
needles **24/24**; mean reduction **83% (71–92%)** on trim scenarios;
wrongly trimmed **0/12**; mean latency **240 ms**. Wider: standard
8/8 / 83%; accuracy 36/36 / 87%; real captures 10/10 / 54%; needle
matrix 9/9. `claude plugin eval` **cannot exercise pruning** (Jev
fetch refused → fail-safe original). Six-run paired Terminal-Bench
pilot is **integration, not a significance test** (full set 89 tasks
/ 178 trials; no published full-run scores this pass). Do not merge
those tables. Do not copy the Harbor launcher (`notes.md` §53).

**Harbor-style frozen protocol vs constrained LLMs (Empirical as that
named receipt, not a ranking).**
[`nibzard/decision-model-benchmark`](https://github.com/nibzard/decision-model-benchmark)
(DMB): jev vs 8 constrained LLMs vs keyword/majority/random; five
suites; **$28.34**; raw logs. **`results/v2/v2.md` is the report of
record.** Protocol frozen before the run; negative results ship;
unknown usage is never a measured zero; later runs replace cells
whole. jev S1 banking **76.3%**, S2 spam **93.0%**, S3 **100%*** at
valid coverage **72.7%** (225 failed = 256+ Choice cap), S4 flip
**13%**, S5 admits-ignorance **49.7%** / ECE **0.246**; p50
**264–276 ms**; S1 cost/1k **$0.07**. No class wins on quality.
Do not copy `uv`. Do not merge this Banking77 with atlas 87% or
jevals.com 79.67% (`notes.md` §49).

**Feedstock / recompute-from-logs (not a third ranking).**
[`Jevals/jevals-data`](https://github.com/Jevals/jevals-data)
(CC-BY-4.0): release boards + per-decision JSONL + suite files for
[jevals.com](https://jevals.com). 2026-09-18 board, suite 0.1.0, 8
systems (banking77 / helpsteer2 / pubmedqa). Formulas:
https://jevals.com/methodology/. Jev on *this* board (n=300×5):
banking77 acc **0.7967**, ECE **0.0981**, p50 **467 ms**, cost/1k
**$0.043**. Cite the release; recompute from logs; do not dump the
board as a ranking.

**Negative: combinatorial assembly ≠ extractive keep/drop.**
[`simonmesmith/jev-arc-agi-v1-experiment`](https://github.com/simonmesmith/jev-arc-agi-v1-experiment)
— Direct Jev on ARC-AGI-1 public eval **4/400 (1%)**, 1.125%
task-weighted, ~$2.32, 10 min. Cell-wise Choice; dimensions ~90%;
rarely a complete grid. A frozen Harbor-shaped protocol that
falsifies "many small decisions add up to a puzzle."

### Bake-off mandate

Before adopting proprietary Jev vs Laya vs TypeAR vs Nimble vs kev vs
blackwood-rlcd vs Archer vs openjev-lm vs a constrained LLM vs von vs
open-alternative-jev, run a jevals-shaped labeled suite (or an equivalent
with this hygiene) and, for a product loop, a Harbor taskset. A design
card with no eval path is incomplete. A green smoke test on
[jev-local](https://github.com/us/jev-local)'s **default stub** is not
that bake-off (`notes.md` §48). von's 14 MB needle at 52.6% authored144
is not that bake-off either (`notes.md` §49). DMB is the frozen-protocol
exemplar for decision-model vs constrained-LLM vs baselines; jevals-data
is the public log feedstock. Do not promote a vendor table into a ranking.

**Shared bake-off exemplar (Empirical as that named receipt, not a
ranking).** [`pngwn/open-jev-laya-bench`](https://huggingface.co/datasets/pngwn/open-jev-laya-bench)
(`RESULTS.md` this pass): System One Qwen3.5-4B scorer vs Laya 421M,
**26 neutral + 9 home**, **11,959** test / **3,269** cal. Scores are
accuracy + **ECE / NLL / Brier** (acc@50% coverage too). Neutral macro
acc Δ **+0.023 [+0.013, +0.032]**; home Δ **+0.229 [+0.198, +0.262]**
(intervals exclude 0). **Not TypeSafe Jev vs Laya.** Neutral prompted-
instruct on the same 4B is statistically tied with the fine-tune
(+0.003, interval includes 0). **LLM-as-judge is not the primary
System One score.** Harbor/jevals practice in the wild: held-out
`test`, temperature on `cal`, leave-one-task-out, prompted arms.
`notes.md` §46. Do not copy the scoring scripts.

Archer weights are still a **Watch** — not on the Hub as of 2026-09-18
(`notes.md` §31–§33). That bake-off is future, not Empirical. kev is
the shipped 0.5B reconstruction on the trained decision-only path, not
that drop (`notes.md` §45). blackwood-rlcd is the open multimodal
decide head on that path **now** (CC BY-NC; Jev still leads general
text; `notes.md` §46). "A 9B
LoRA is enough versus Jev" stays **Hypothesis** (`notes.md` §35).
openjev-lm is the name of that distill. kev is not a Jev distill.
Nimble is not a Jev distill
(model card Apache-2.0; GitHub LICENSE was 404). Meijer: marginals,
not a PPL, not Kleisli (`notes.md` §34). djev-spark is a third compute
graph, not the winner of this bake-off (`notes.md` §36). Do not
promote a vendor table into a ranking.
