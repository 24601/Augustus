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
| Evidence-packet explorer (SWE finish) | [jevex](https://github.com/jimmyhealer/jevex) (was jev-semantic-explorer) | Author-run. Claude Code 6.8→2.2 files. SWE-bench Verified n=8: **1/8 → 6/8** finish. **n=16 delta** *theirs*: 160s→**69s**, $8.74→**$3.13**, 16/16 both arms; 90s cap 1/16 vs 11/16. Packet HitFile 0.233 diagnostic |
| Meaning-grep LLM-as-judge | [jev-semgrep](https://github.com/uehaj/jev-semgrep) | 10 cases × 51-line EN/JP corpus. Precision 0.94, recall 0.98 *theirs*. Not a Harbor taskset. Dedicated fold `notes.md` §86 |
| Closed-vote CU worked example | [JevOnly](https://github.com/buluoray/JevOnly) | 11 steps / 43 Jev calls / ~340k tok / ~$0.014 / 17 s *theirs*. No planner LLM. Not a bake-off |
| Host-owned product evals | [waymode](https://github.com/mossburgh/waymode) | 24/26 public suite; 34/36 completion regression *theirs*. Bounded development evidence, not a self-driving proof |
| OMP prompt suppression (permission vs probability) | [omp-greenlight](https://github.com/SemetricLabs/omp-greenlight) | 1,013 gated calls / 10 sessions / 8.95 h. Default **40.9%** prompts removed; **0 of 94** unsafe auto-approvals on 140-row corpus. Live traffic unlabelled. Operator owns bar. Not a sandbox. ~$0.05 / 1,013 *theirs* |
| Jev question as if-statement (instrument not score) | [dinostomp](https://github.com/collapseindex/dinostomp) | `dinostomp jev`: accuracy, p(yes) cut, ECE, blank-input lean, rewording flips. Demo *theirs* 24 examples: 100% / ECE **0.062**. FINDINGS 189 (F 52 / D 99 / N 38); 99 against itself. Beside jevals, not a Harbor taskset |
| SLO routing latency cost (sync Jev vs local features) | [slo-router](https://github.com/zeeshan8281/slo-router) | Live Jev vs `slo_no_jev` on sim backends. Same routes (fast 4 / strong 4) and 100% accuracy; p95 E2E **77.93 → 490.38 ms** (~6.3×). Jev feature p50 453.58 / p95 1257.50 ms. 16/16 Jev calls; no lexical fallbacks. 3/8 task-label disagreements did not change routes. Eight-row demo is **not** a benchmark. License null. *Their* integration card |
| Effect-based shell-gate certification | [construct-auto-classifier](https://github.com/godspede/construct-auto-classifier) | Main 113 + blind 82; 5 passes; **975 decisions/model**. Jev: **0** dangerous allowed, 100% caught, 99.5% correct, $0.047/1k. Every chat model leaked 16–104 dangerous. Only Jev certified. Through the whole gate, not a Harbor taskset |
| Docs-derived instruct seed | [INSTRUCT_JEV](https://huggingface.co/datasets/ctaxnagomi/INSTRUCT_JEV) | 119 rows (47 choice / 51 noul / 21 score); 24 typed question blocks / 7 typed answers. MIT. Open-replica / jevals seed. Not a bake-off |
| Evidence-gated question packs | [jev-packs](https://github.com/dtduc-git/jev-packs) + [jevassert](https://github.com/dtduc-git/jevassert) | Nine packs `verified` on pinned `jev-1.13.0` *theirs*. **Runner LANDED** (Apache-2.0; was 404 §64). Record/replay CI: accuracy/ECE/Brier/cost/latency offline; exit 0/1/2; McNemar. First matrix 2,990 cases: Jev/Sonnet 5 accuracy tie (Δ≤0.018); Jev better calibrated 7/9; ~250× cheaper. sms-spam this-pass 0.953/0.040. `unknown` mandatory. CC0 packs. Not a Harbor taskset |
| Ranking ≠ calibration (human annotations) | [does-jev-confidence-mean-anything](https://github.com/Adilmp/does-jev-confidence-mean-anything); [jevcal](https://github.com/Adilmp/jevcal) | 8,000 judgments, `jev-1.13.0`, $0.05. AUC **~0.91**; stated **~75%** vs human **~10%**. Recalibration removes **~96% ECE**, AUC unchanged. `natural`/tightened ECE 0.156 → 0.006. jevcal: ~100 rows (94% of error). ECE gameable (constant base-rate ECE 0). License null / MIT. One domain; do not cite `threat` (n=1) |
| Hot-click CU vs per-step LLM | [ego-jev](https://github.com/jiangkoumo/ego-jev) | Alternate 3-round medians *theirs*: HN 4.9 s vs 9.7 s; wiki 5.4 s vs 10.1 s (~2×). n=3; high variance (control 7.3–22 s). **Not a benchmark.** MIT |
| Verbatim compact vs truncate vs summarize | [jev-compactor](https://github.com/edwardyen724-g/jev-compactor) | Earlier vs-Sonnet card: 64.5% / 366 ms / 4 of 4 (`notes.md` §65). Later product-arm table *theirs*: **73%** (53–76%) / **350 ms** / $0.0004 / **4 of 4** vs Anthropic 86%/16.8s/3 of 4, Codex 85%, OpenCode 85%, Gemini 61%/4 of 4. 61k session 95.4%/593ms/$0.0014. 30–250× cheaper. Two synthetic sessions, not a survey. MIT |
| Pre-send tool-result views | [dizk/jev-lens](https://github.com/dizk/jev-lens) | 500 SWE-rebench trajectories; 3,300 large results; 11.6M → 2.4M = **79%** fewer tokens. 88% command / 31% code. Post-send prune +17% cost. Harm: 2/26 later edits missed block; 0.3% dropped line quoted; 2.2% dropped identifier. Claude plugin unmeasured. MIT. Distinct from rashedInt32/jev-lens |
| tools≠use / SessionStart | [jev-carryforward](https://github.com/Dharundp6/jev-carryforward) | Plugin eval: `recall` **0/4** with tools+skill. SessionStart hook is the actual intervention. 9×3 remains a hint. MIT |
| Independent open-Jev class | [openvons](https://github.com/genai-craft/openvons) | LM 4B+head 0.916 vs 27B zshot 0.875; 8q / 22.6 ms. Vision 1/34 VRAM 36×. Voice 50 ms; 100% chatter reject. JevPick 3.2–4.8× byte-identical. Flutter 2.0–2.2 s / 11 ms for 9 q. Apache-2.0 LICENSE / GitHub SPDX NOASSERTION. Not TypeSafe |
| Physical-world S1 | [HA-Jev](https://github.com/AboveColin/HA-Jev) | `background:` triples laundry separation *theirs*. Batching 3q 712 ms vs 100q 714 ms. 30 commands $0.0017. Confidence uncalibrated. 192 mocked tests. MIT; **17★**. Not for locks/heaters |
| Same-intent VOI cache | [jevcache](https://github.com/kushals256/jevcache) | n=100 live Jev **fp=0 / precision=1 / recall=0.38 / fpr=0** vs Jaccard@0.35 fp=24 / fpr=0.48; $0.00174 *theirs*. Fail-open. MIT |
| Zeroshot vs BERT-family | [jev-zeroshot-vs-bert](https://github.com/zhuyansen/jev-zeroshot-vs-bert) | Beats DeBERTa-c on 7 sets (+0.05–+0.13; PAWS AUC +0.03; arXiv 2026 +0.30). Contaminated 0.901 vs `-c` 0.763. ≈230 / >2048 labels. Banking77 512+ feature **hurts**. DiD 0.035 vs 0.112. MIT |
| Worth-your-attention VOI | [ThinkyMiner/Winnow](https://github.com/ThinkyMiner/Winnow) | Unreviewed goldens **80%** verdict / **90%** content-type *theirs*. Distinct from kevinpita/winnow. MIT |
| Local OpenJev `/v1/decide` | [IamBusy/OpenJev](https://github.com/IamBusy/OpenJev) | v0.3 **45/60** vs v0.2 39/60; reversal 100%. Not TypeSafe drop-in. Apache-2.0. Distinct from hraness/sysone runners |
| SemIf `/v1/systemone` runoff | [semif-serve](https://github.com/dddanielliu/semif-serve) | RTX 3080 Ti Qwen3.5-4B **1164 ms** vs hosted **178 ms** *theirs*. Wire-compat ≠ replica. pyproject MIT / GitHub SPDX null |
| Conflict ≠ ignorance | [jev-typed-evaluation-collapse](https://github.com/mleyvaz/jev-typed-evaluation-collapse) | Noul 0.50–0.57 vs 0.46–0.48; named Choice p=1.0; binary red 0.67–0.85 *theirs* (v0.3). License null. NCML field note |
| BM25 vs Jev skill routing | [pi-jev-skill-bench](https://github.com/iamdin/pi-jev-skill-bench) | 43 gold; roster 50–500. Harness, not a production claim. **No live Jev numbers this pass.** MIT |
| Decision-as-memory flywheel | [DGUI_HYPERMEM-JEV](https://huggingface.co/datasets/ctaxnagomi/DGUI_HYPERMEM-JEV) | 6 rows (analyze 4 / rerank 2 / supersede 0). Sibling INSTRUCT_JEV. MIT card |
| Stop-hook attention redirect | [jev-preflight](https://github.com/muse0509/jev-preflight) | Owner-run Claude Code 2.1.267: no-key fail-open PASS; key-enabled exactly one continuation. Live API smoke: jev-1.13.0, 898/151 tokens, eight Nouls. 0.85 uncalibrated. Go MIT |
| Receipts-not-leaderboard capability map | [jev-capability-atlas](https://github.com/Zaious/jev-capability-atlas) | Hold vs break with API receipts; not a ranking. Type-safe ≠ correct (DAIR Emotion 48% / mean conf 0.819). Axis already §49; 10★ this pass. README MIT / GitHub NOASSERTION |
| Jev vs thinking-budget Qwen3.5 | [jev-frontier-100](https://github.com/softpudding/jev-frontier-100) | 100×3; Jev **77.0%**; 4B off 56.0% / 512 78.3% / 2048 **96.7%** (+12.7 to +26.7). 2B/2048 82.0% (−2.3 to +12.3). Exploratory, not preregistered. MIT. Not a ceiling |
| OOD calibration / sign by type | [jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration) | 900 synthetic + 3,721 public; ~$0.06. Public OpenBookQA ECE 0.024 / T 0.96. Synthetic all ECE **0.107 = 4.4×** floor; priority 44.7% / mean p 0.74 / T **3.40**; boolean T **0.66**. MIT. Gateway has no model version |
| Memory-lease invalidation | [invalidate](https://github.com/chopratejas/invalidate) | 157 labeled cases *theirs*: 89.2% strict / 97.5% lenient / **0 of 157** false invalidations. Six Nouls then code. Apache-2.0. MED |
| Cost-aware PR prune (pilot) | [prune-review](https://github.com/shubhangi013/prune-review) | 22 paired runs: winning-only 27.9% (post hoc); all 22 incl. 305% outlier **1.18%**; excl. outlier 15.9%. Cost not quality. Source preview. Size 365 / 1★ this pass |
| Whole-repo intent (CLI, under construction) | [jev-intent-review](https://github.com/yottayoshida/jev-intent-review) | VERIFIED/VIOLATION/UNKNOWN/NOT_APPLICABLE. Empty search ≠ proof. missed-path 7–8 req / 2–3 s; omamori #559 31 req / 14 s *theirs*. Action not written |
| Failure-finding arena (not a leaderboard) | [jevarena](https://github.com/chenmingtang830/jevarena) | Apache-2.0 TS. Public preview. JevJudge-Bench harness **not measured findings**. **≠** meetr1912/jev-arena |
| BBQ stereotype/uncertainty/cost | [jev-bbq-experiment](https://github.com/simonmesmith/jev-bbq-experiment) | 58,492 Q; Jev 1.13.0 **97.28%**; amb 99.96% / inf 94.60%; bias 0.04 / 0.34; **$0.3429 / 7.75 min** *theirs*. 12/13 amb errors stereotype-aligned. Order diagnostic 1/484. License null. Not a bias cert |
| Sentence-as-rule lint corpus | [jevlint](https://github.com/mizchi/jevlint) | 13/15 naming/comment rules **1.00/1.00** *theirs*; comment-describes-block ships unseparated. Review 2 req / $0.00013. **≠** huntedman/JevLint |
| Rust/WebGPU System One (JGLUE) | [grande](https://github.com/bokuweb/grande) | E2B zshot JNLI **0.614** ECE 0.252→**0.088** T=2.81; JCQA **0.853**. 270M **0.710/0.710**. Isolation 0.098/0.996. Packed Δmax 7e-5. License null. Softmax ≠ Noul until T |
| Clojure Laya byte parity | [laya-jolt](https://github.com/jlt-commons/laya-jolt) | Byte-identical to Python `system_one` on README quickstart *theirs*. ~1e-7 last-digit drift. Apache-2.0. Was empty skip §61 |
| ONNX ModernBERT vs live Jev | [local-jev](https://github.com/kunchenguid/local-jev) | 136 checkpoints *theirs*: done **30%** / shape **57%** / r **−0.06**; gold done 26% vs Jev 87%; 112 min vs 21 s. Confidence omitted. Not equivalence |
| Persist constraints (pi) | [pi-heed](https://github.com/Nyarlathoteppppp/pi-heed) | 79 sessions / 261 labelled: v0.8.0+Jev recall **98.5%** / false block **0.0%** / $0.000058 *theirs*. Mid-session rule change 8/13 off vs 0/13 on. Fail-open |
| Harbor SGR-judge contract (no quality headline yet) | [jev-judge-bench](https://github.com/slavadubrov/jev-judge-bench) | Frozen SLA-150. Jev vs Luna / DeepSeek-flash / glm-5.3-flash. Invalid = FN. 21 offline tests. Canaries *theirs* **not quality**: Jev OpenRouter 5/5; Luna 10/10; DeepSeek GA 10/10; DeepSeek beta 8/10; GLM 5.3 10/10; GLM 4.7 4/10 overload. $10 live Berlin in progress. Direct TypeSafe untested. Five-field/H5 untested. README MIT / GitHub SPDX NOASSERTION. **≠** chenmingtang830/jevarena **≠** fstandhartinger/jevbench |
| OpenRouter recipe samples (not benches) | [jev-cookbook](https://github.com/nexibeo/jev-cookbook) | 15 recipes; samples 16–36 handmade. Live 2026-09-19 `jev-1.13-20260917`. Recipes 01–13: 425 calls / **$0.015**; median 0.34–0.45 s; browser 5/6 *theirs*. Authors: scores show technique, **not benchmarks** |
| Hand-no-text plugin loop | [jev-use](https://github.com/shitianfang/jev-use) | Vercel `typesafe-ai/jev`, 95 calls *theirs*: p50 **220 ms** / p95 423; 12q **186 vs 2,672 ms**; 20-step 4.3 s / 0 escalated; gate **12/12** / p50 199 ms. First loop 17/20 escalate then 0/20 at margin 0.4. MIT v0.4.1. **≠** jev-ultrafast |
| Competing NAR claims (audit, not endorsement) | [openJev-verdict-2.0](https://github.com/Heman10x-NGU/openJev-verdict-2.0) | README *theirs* N=2000: acc **77.10%** / Brier **0.0636** / ECE corr **0.0144** / dist **0.1513**. Jev row is Laya-catalogued vendor baseline, not independent. **Open PR #1**: 24.7 dec/s misread as 25 ms (actual 40.5 ms; 3.5× not 28×); Laya 76.60% inside 95% CI (parity); like-for-like dist ECE 15.13% vs 21.40%, Jev 14.40% slightly lower. **≠** IamBusy/OpenJev |
| 1-token logprob local vs Jev (GUI 336) | [chakuho](https://github.com/taku-me/chakuho) | *Theirs* 2026-09-19 DGX Spark. 27B NVFP4: ordinary **245/258 (95%)** / sheets **72/78 (92%)** vs Jev Gateway 230 (89%) / 64 (82%). `__none__` gold 30: 29 vs 27 vs 8B **3**. Coverage ≠ correctness. Softmax ≠ Noul. MIT |
| Open replica engine speedup | [jevinf](https://github.com/zerodegress/jevinf) | **2.57×** one request (25.80→10.06 s) / **2.27×** dev split (84.2→37.0 s) at **100% argmax** *theirs*. Not ECE. MPS only. MIT |
| Files-to-read n=16 SWE | [jevex](https://github.com/jimmyhealer/jevex) | agy + Gemini 3.8 Flash, 1200s cap *theirs*: 160s→**69s**, $8.74→**$3.13**, 16/16 both arms. 90s cap 1/16 vs 11/16. Keep n=8 1/8→6/8 |
| Commit pre-review calibration | [commitjev](https://github.com/yodablocks/commitjev) | 13 labelled: every rule fires on its defect; **0 false on 5 clean** *theirs* (small control). Own 16 commits 3 warn / 4 review / $0.0017. Spread 0.01–0.09 |
| Laya multilingual MASSIVE / XNLI | [laya-multilingual](https://huggingface.co/convaiinnovations/laya-multilingual) | 51 langs *theirs*: acc **0.366** / ECE **0.387** / 45 of 51 ≥3× random vs English laya 0.227 / 0.733 / 23 of 51. Khmer 0.000@0.952 conf. XNLI 14-lang 0.731 vs 0.521. Ships uncalibrated ECE 0.314→0.106 after T. Apache-2.0 |
| Schema-conditioned DeBERTa scorer | [jev-schema-scorer-deberta-v3-large](https://huggingface.co/mobarmg/jev-schema-scorer-deberta-v3-large) | Hub MIT; GitHub **404**. v2 Choice **0.841** (chance 0.214) vs v1-only 0.687 *theirs*. Peaked p = ranking. Synthetic English |
| HF access this pass | open-jev-laya-bench / jev-tree-choice-cap / INSTRUCT_JEV / jevlogs-log-triage-benchmark | First three **401** (do not re-fold; no new numbers). jevlogs GitHub 404 **and** HF 401 |
| Productized public classification (vs_jev + caveats) | [classifier-dev](https://github.com/mrmps/classifier-dev) | MIT; **185★**. README *theirs*: 400 headlines **650 ms**; packing 100 = one-at-a-time; emotion ≥0.9 → **82%** / <0.5 → **29%**; multi-label F1 **0.887** / **230 ms** vs cascade **0.799** / 1.5 s; gemini-3.8-flash 87.5→90.0 / 61.8→63.7. eval *theirs*: 232 ms; AG News **87.7%** vs ling-3.0-flash **82.0%**; emotion **60.5%** vs **57.0%**; granite-4.0-h-micro F1 **0.546** vs advertised ~**0.800**. n=7 train-on-test; ~0.03 coin flip. `/benchmark` = tracked `vs-jev.json`. Not a Harbor taskset |
| Systematic-review pointer (spot check, not a validation study) | [choxos/jev-reviewer](https://github.com/choxos/jev-reviewer) | MIT; **12★**; https://jevreviewer.xera.ac. **≠** egma-ai. README *theirs* sample study (712 lines, Sep 2026): 1q 10 req / 1.2–2 s / $0.0016; 9q 17 / 2.3 s / $0.0052; 18-q template 27 / **4.6 s** / **$0.0101**. Quotes = Noul ≥ 0.5. *Not found* is an answer. Treat as spot checks |
| Prompted-JSON `/v1/systemone` bake-off (not logits; not calibrated) | [githubnext/localjev](https://github.com/githubnext/localjev) | MIT; **261★**. 1,200 req / ~23.5 min / M5 Max / oMLX 0.6.4 / Bun 1.4.0 *theirs*. Short macro: Qwen3.6 **76.7%** (AG News **90.0%**); Gemma 4 26B-A4B **75.0%** (SST-5 MAE **0.533**); DiffusionGemma **74.2%** (BoolQ **87.5%**). Qwen vs Gemma 26B = 2/120 — no definitive winner. Long-input both **69.2%**. Do not treat as calibrated. **≠** kunchenguid/local-jev. **≠** razorback16 structured-read |
| Laya packaging vs-Jev (third-party unpublished-here; post-T ≠ raw) | [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya) | Apache-2.0; **710★**. README SHA `f12882b`. T4 *theirs*: 1q multilingual **32.8 ms** / 10q **72.3 ms**. Routed vs Jev 1.13.0 (Jev rows never measured here): typed-decisions **0.766** vs 0.727 (fine-tune; base 0.362/0.342 vs majority 0.461); Banking77 **0.425** vs **0.870** (77 vs 72 labels; ~3–4 tok/label); post-T ECE **0.081** vs 0.246 (raw 0.213 vs 0.144). Khmer **0.000@0.952**. Soft-acc 0.471 vs 0.580. 0.85 gating *theirs*. **≠** TypeSafe drop-in |
| External openjev census (tweet, not scores) | [@airesearch12 / Benchmark Heaven](https://x.com/airesearch12/status/2101259522933186879) | Named ~18 (system-one-open, openjev-sglang, DeBERTa open-jev, Needle 3, open-alternative-jev, Nimble 9B, SemIf, open-jev Dasein / JoshuaSP, OpenJev razorback16, mini-jev, system-one, system-one-gemma, jevlike, AlexWortega/openjev, GLiNER2, Succinct Router 14M, jev-model-router/Director/Loki). Engagement **ephemeral** (SIGNAL ~417/9/3; this pass 564/15/5). Watch [jev-models](https://benchmarkheaven.com/jev-models). **≠** jevbench v1.1. Scored sibling §78. Class-boundary: GLiNER2 + routers. Incomplete vs Laya/localjev/kev/TypeAR/openvons/… |
| Never-confidently-wrong protocol (TLA+ + chaos) | [jev-labs](https://github.com/copyleftdev/jev-labs) | 1,080 golden: 0 wrong under none/realistic/severe *theirs* (severe 314/46 escalate). Rule of three <0.28% at 95% — not a proof of zero. TLC 1,049,750 states / 0 errors. 1,490 calls `jev-1.13.0`. Synthetic, not clinical. MIT |
| Sureness metrics vs Jev `confidence` | [how-sure-is-jev](https://github.com/adarc8/how-sure-is-jev) | 60 live answers: Choice confidence = max_prob to 3 decimals. 75/25 → 0.5 vs entropy 0.19. Bands are policy. Zero-dep MIT |
| Jev-class bake-off v1.1 (historical) | [jevbench](https://github.com/fstandhartinger/jevbench) | 314 decisions. Main Score 0.6/0.2/0.2. Jev 1.13.0 **87.6** / Cap 97.8 / $0.0259/1k *theirs*. Calibration **reported, not scored**. Native vs verbalized. Partial runs not ranked. Unofficial MIT. **Superseded for the live board by v1.2** (not comparable) |
| Jev-class bake-off v1.2 (live board) | [jev-models](https://benchmarkheaven.com/jev-models) / [jevbench RESULTS-v1.2](https://github.com/fstandhartinger/jevbench/blob/main/RESULTS-v1.2.md) | Protocol `jevbench::v1.2`; scored 19 Sept 2026; 534 decisions (72/96/146/**220 hard**). Geo-mean I/C/S/K 25% each. Jev 1.13.0 **75.3** / SemIf **74.6** (−0.7) / OpenJev razorback16 67.6 *theirs*. Luna I **96.8** rank **#7**. Cal **ON** rank. Self-host latency ×2 assumption; many costs est. Option-order 72%→21%. Partial not ranked. Laya absent (gap, not named-excluded). Qwen3.8 27B Chutes TEE **≠** Archer. Unofficial MIT. README SHA `bf1e79ba`; RESULTS SHA `fdfab1a2`; HEAD `27ed3d6c`. **≠** tweet census **≠** v1.1 87.6 **≠** jev-judge-bench **≠** jevarena |
| Hourly 0842 already-folded watch (apply, don’t re-card) | `notes.md` §79 | Five HIGHs already §73–§78 (`5f44bf4` / `03fddc6` / `daa70b7` / `bcf66f1` / `db654b5`+`40a5f12`). Recipe: wire-compat ≠ logit-equiv; productize label+p + mark FALLBACK; packaging ≠ new species / script-before-p; pointer-not-generator two-pass; census ≠ scored bake-off. Skip thin (JEValuate / jevspeak / fable-jev; jev-semgrep now §86). Hard-gate Noul as PR/quality = soundness theater (totally-tim/jev-gate 0★ / claude-jev-warden 1★). Archer still Watch. Not a Harbor taskset |
| Local controller vs Live API (reflex A/B, not a bake-off) | [jev-reflex-autonomy-lab](https://github.com/khordoo/jev-reflex-autonomy-lab) | TypeScript; **7★**; license null. README SHA `130987c9`; ARCHITECTURE SHA `48da0769`; HEAD `e3297ebe`. Same physics/seed; toggle only changes where reflex decisions come from. Local = rule-based, no keys. Live = `POST /v1/systemone` `jev-latest`. 20% starting gate *theirs* does not start a mission. **≠** githubnext/localjev **≠** kunchenguid/local-jev. No ECE/taskset — Harbor-*adjacent* of backends, not a scored board. Seed = geometry ≠ async replay. `notes.md` §80 |
| OCR+AX desktop CU cost table (one screenshot, not a taskset) | [typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use) | MIT; **427★**. README SHA `369f4a6a`; HEAD `cc7b5066`. *Theirs*: $0.0002 vs Opus 5 $0.032 (155×); 0.13–0.38 s vs 5.2 s; ~1.5 s vs ~5.5 s e2e. Honest caveat: dates.py rebuilds pixel-free reasoning. 0.4 / 0.5 still soft. **≠** jev-ultrafast Flights clock. Not a Harbor taskset. `notes.md` §81 |
| ASR voice-browser fixtures (not a taskset) | [jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser) | JavaScript; MIT; **103★**. README SHA `fa033303`; HEAD `054db0f3`. *Theirs*: integration 27/27; Jev p50 ≈ 300 ms; ~$0.0002/call; demo ≈ $0.01. 0.5 / 0.55 / 0.6 still soft. **≠** Harbor. **≠** jev-voice-control. `notes.md` §82 |
| Wrap-as-execution (not a quality bench) | [AgentGhost](https://github.com/reddpy/AgentGhost) | TypeScript; MIT; **2★**. README SHA `44145fa9`; HEAD `ac04e4fb`. ASK throws; fail-closed. No Harbor numbers. **≠** actiongate **≠** toolgate. `notes.md` §83 |
| JP genre atlas (tweet, not scores) | [@studio_yebisu](https://x.com/studio_yebisu/status/2101065176069886152) | Apps by genre; SAM 3.1 + OpenRouter Jev noted. Engagement **ephemeral** (SIGNAL ~120k/1767/169; this pass 131,234/1,934/192). Stars research-time (typesafe-computer-use 203→427; jev-voice-browser 40→103). **≠** @airesearch12 **≠** v1.2. Not verified evals. `notes.md` §84 |
| External pedagogy (article, not scores) | [@akshay_pachaar](https://x.com/akshay_pachaar/status/2101037514945597645) | “Jev Clearly Explained.” 200×/400× TypeSafe ceiling *theirs*. schema-safe ≠ correct. Engagement **ephemeral** (SIGNAL ~183k/2095/220; this pass 233,495/2,280/235). **≠** Harbor. **≠** official docs. `notes.md` §85 |
| Meaning-grep dedicated (contrast-set, not scores) | [uehaj/jev-semgrep](https://github.com/uehaj/jev-semgrep) | JavaScript; MIT LICENSE / GitHub NOASSERTION; **51★** ephemeral (SIGNAL ★42; §61 0★). HEAD `21120e9`; README SHA `923e6a5`. Proposition ≠ embedding; all-six-refund contrast-set *theirs*; AND/OR/NOT after threshold; Semgrep.dev collision; not a gate. 0.94/0.98 keep as LLM-as-judge 10×51, not Harbor. `notes.md` §86 |
| Decision-validated UI (validity ≠ quality) | [gram-render](https://github.com/wei-b0/gram-render) / [jev2ui](https://github.com/dglazkov/jev2ui) | gram-render MIT **0★** README SHA `dd5fb44`; no quality headline. jev2ui Apache-2.0 **0★** README SHA `f0d477fc`; Jobs **11/11** vs Baseline **10/11** valid A2UI *theirs*; mock 13/13. Valid tree ≠ good screen. `notes.md` §87 |
| Decision-as-assert (thresholds, not a bench) | [jevtest](https://github.com/realZachi/jevtest) | MIT **1★**; npm 0.1.0; README SHA `6e432fc`. 0.85/0.15 still soft; ambiguous band fails both. No labeled suite. typesafe-ai/jevtest 404. `notes.md` §87 |
| Hybrid S1 offline/live cards | [anima3](https://github.com/hulryung-uo/anima3) | license null **0★**; README SHA `68d6eb5`. Offline 20-tick *theirs*; jeff economy 62 calls → **0** admitted. 0.35 gate still soft. Qwen logprob default. Not a Harbor taskset. `notes.md` §87 |
| Jev vs frontier (accuracy + ECE + $) | [jev-frontier-bench](https://github.com/manjunathshiva/jev-frontier-bench) | MIT **0★**; README SHA `a6a8447`. 200 decisions / $4.83 OpenRouter 19 Sep 2026 *theirs*. Jev **72.5%** ECE **0.161** vs Fable **84.0%** ECE **0.064**. Cascade **82.5%** at **$4.41**/1k (**in-sample** 0.9). ChaosNLI JS Jev **0.149** worse than uniform **0.127**. Conf = top of `probabilities`. **≠** jev-frontier-100. One run. `notes.md` §87 |
| Jev vs GLiClass product bakeoff | [jev-gliclass-bench](https://github.com/JoeSlain/jev-gliclass-bench) | MIT **0★**; README SHA `335043e`. n=100 seed=42. Jev **78%** / GLiClass **40%** / majority **49%** *theirs*. Teacher labels. Flattened encoder. Prefer log loss / Brier over `ece_maxprob`. `notes.md` §87 |
| Four engines / majority floor | [job-posting-triage](https://github.com/geckguy/job-posting-triage) | MIT LICENSE / GitHub SPDX other; **0★**; README SHA `bdafb39`. n=1000 / 53 fraud. Floor **0.947**. Jev on the floor (ECE 0.046). tfidf acc **0.970** F1 **0.700**. llm_local 1000/1000 conf 1.0 ECE **0.947**. Calibration ≠ discrimination. `notes.md` §87 |
| Pi compaction delta (~50× *theirs*) | [fast-jev-compaction-pi](https://github.com/zaycruz/fast-jev-compaction-pi) | MIT **0★**; npm 0.1.1; README SHA `809c0bd`. ~50× vs LLM summary; preserveCallInputs 8/8 + 17/17 paths; memory QA 6/8 ties built-in *theirs*. Two synthetic-ish sessions. **≠** pi-jev-compact **≠** pi-jev-compaction. `notes.md` §87 |
| Laya-class vision (cal ECE; `score` untrained) | [laya-vision-smolvlm-256m](https://huggingface.co/thaitea/laya-vision-smolvlm-256m) | CC-BY-NC-SA; code Apache-2.0. Val n=**8235** acc **75.2%** ECE raw 0.124 → cal **0.034** *theirs*. `score` meaningless. VQAv2 re-split **not** published VQAv2. **≠** blackwood **≠** Archer. `notes.md` §87 |
| Competing NAR (audit, not endorsement) | [Cerebellum-2B](https://github.com/mkeco/Cerebellum-2B) | Apache LICENSE / GitHub SPDX other; **1★**. Hub mkzero. Claimed **94.92%** vs Jev **81.1%** *theirs* **unverified**. `/v1/decide` ≠ TypeSafe. Wire-compat vs agent-routing as **separate** Harbor axes. README_EN SHA `f3e86883`. `notes.md` §87 |
| Laya grounding tradeoffs | [laya-grounded](https://huggingface.co/Luni/laya-grounded) | CC-BY-NC; GitHub 404. Grounding 5/5; phishing **0.611→0.512**; routing **2/3→1/3**; ECE **0.156** *theirs*. Platt not temperature. Entropy-confidence ≠ max_prob. Not a drop-in. `notes.md` §87 |
| Open LoRA replica vs hosted Jev (acc vs ECE) | [GestaltLabs/Jeff-1](https://huggingface.co/GestaltLabs/Jeff-1) | Apache-2.0; Hub **4 likes**; code **0★**. n=**9730** *theirs*: Jeff acc **0.8183** ECE **0.0807** vs Jev **0.8283** / **0.0932**. Acc/Brier lose; ECE wins. Set reused. **≠** logan-markewich/jeff. `notes.md` §88 |
| Jev-first bounded agent (coverage, not a bench) | [stanley-code](https://github.com/devagrawal09/stanley-code) | MIT **20★**; README SHA `59da9a1f`. Empty ≠ approve. 0.6/0.55/0.15 still soft. No quality headline. 0.1.0 not on npm. `notes.md` §88 |
| Sub-agent dispatch counts (not dollars) | [jevsubrouter](https://github.com/leftspace89/jevsubrouter) | MIT **4★**; README SHA `317996d0`. Stats are tier counts. Worker tokens invisible from a hook. ~300 ms warm *theirs*. Not a Harbor taskset. `notes.md` §88 |
| Question preflight (Nothing about accuracy) | [jev-reliability](https://github.com/vcjdeboer/jev-reliability) | SPDX NOASSERTION; **0★**; README SHA `eaad87f7`. noul-gate flip 0.0%/12.5%/3.6% *theirs* (112 calls). tier12-framing-fixed reworded 0.0% / paraphrase 1.7× null. **≠** dinostomp. `notes.md` §89 |
| Preregistered hallu bench (bars, not results) | [clduab11/jev-test](https://github.com/clduab11/jev-test) | MIT **0★**; README SHA `59115535`. “Nothing runs yet.” D bars ≥50% / ≤10% wrong / +0.15 vs B / ≥90% support — not scores. HTTP smoke ≠ quality. **≠** realZachi/jevtest. `notes.md` §89 |
| RAG rerank harness (no headline) | [jev-rag-benchmark](https://github.com/erendikmenn/jev-rag-benchmark) | MIT **0★**; README SHA `ea54bbe0`. “Jev wins” is not an assumption. `max_budget_usd` 0 blocks paid. **≠** Max-sm-yc/Jev-RAG. `notes.md` §89 |
| Triage vs Haiku (synthetic 120) | [dairui1/jev-lab](https://github.com/dairui1/jev-lab) | license null; **0★**; README SHA `4c006b68`. urgent **91%** vs Haiku **79%**; frustration 79/65; p(urgent) 0/21/41/75/100% *theirs*. **≠** BrendanH18/jev-lab. `notes.md` §89 |
| Grok Bot A/B proxies (not tokens) | [grok-bot-jev](https://github.com/Bodila51/grok-bot-jev) | MIT **1★**; README SHA `a03a16c9`. Browser 1→0; retries 3→0; 13.0× is a top-five cap. Not a token-savings claim. `notes.md` §89 |
| Pre-review typed PR gate | [ci-gatekeeper-bot-jev](https://github.com/NemanjaManic/ci-gatekeeper-bot-jev) | Own-repo live Jev: 504–629 ms; secondary ~4–5 s only on human-review + elevated risk. Conservative default escalated trivial diffs. `package.json` MIT / GitHub SPDX null |

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
0.94 / recall 0.98 *theirs* (LLM-as-judge, cached verdicts,
10 cases × 51-line corpus). Not Harbor. Dedicated fold:
proposition ≠ embedding; contrast-set; Semgrep.dev; not a
gate (`notes.md` §61, §86).
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
**Evidence-gated packs (Empirical as registry tables +
landed runner; Harbor/jevals practice; 2026-09-19 ~05:46).**
[jev-packs](https://github.com/dtduc-git/jev-packs): nine
packs `verified` on pinned `jev-1.13.0` *theirs*.
[jevassert](https://github.com/dtduc-git/jevassert) **LANDED**
(Apache-2.0; was 404 §64). `check` is offline from
recordings; accuracy/ECE/Brier/cost/latency; exit 0/1/2;
McNemar. Matrix 2,990 cases: Jev/Sonnet 5 accuracy tie;
Jev better calibrated 7/9; ~250× cheaper *theirs*.
`unknown` mandatory. CC0. Distinct from INSTRUCT_JEV
(no evidence gate) and dinostomp (instrument). Do not
copy uvx (`notes.md` §64, §70).
**Harbor SGR-judge contract (Empirical as frozen protocol,
not a quality score; 2026-09-19 ~06:43).**
[jev-judge-bench](https://github.com/slavadubrov/jev-judge-bench):
SLA-150; Jev vs schema-guided LLM judges; invalid = FN;
cost/latency first-class. 21 offline tests. Canaries *theirs*
are availability, **not** F1. **No quality headline yet.**
Distinct from jevarena (failure-finding) and jevbench (Main
Score). README MIT / GitHub SPDX NOASSERTION. Do not copy
`uvx` (`notes.md` §71).
**Competing NAR claim-audit (not endorsement; 2026-09-19
~06:43).**
[openJev-verdict-2.0](https://github.com/Heman10x-NGU/openJev-verdict-2.0):
README *theirs* 77.10%/0.0636/0.0144. Open PR #1 already
corrects throughput≠latency and Laya-parity. Like-for-like
distribution ECE vs Jev is not a win. **≠** IamBusy/OpenJev
(`notes.md` §71).
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
64.5% / 366 ms vs Sonnet (`notes.md` §65); later product-arm
**73%** / 350 ms / 4 of 4 vs shipped summarizers (`notes.md`
§68). Two synthetic sessions. Do not copy npm.
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

**VOI cache / zeroshot displacement / skill-routing harness /
typed-evaluation collapse / local class (Empirical as their
tables; 2026-09-19 ~04:39).**
[jevcache](https://github.com/kushals256/jevcache): n=100
live Jev **fp=0 / precision=1 / recall=0.38 / fpr=0** vs
cosine-Jaccard@0.35 fpr 0.48; $0.00174 *theirs*. Fail-open.
[jev-zeroshot-vs-bert](https://github.com/zhuyansen/jev-zeroshot-vs-bert):
Jev beats clean DeBERTa-c on all 7 sets (+0.05 to +0.13
acc; PAWS AUC +0.03; arXiv 2026 +0.30). Contaminated NLI
AG News 0.901 vs `-c` 0.763. Label-equivalence ~230 /
>2048. lr-bge+jev hurts Banking77 at 512+ (−0.044). DiD
Jev drop 0.035 vs DeBERTa-c 0.112. Cost not logged.
[ThinkyMiner/Winnow](https://github.com/ThinkyMiner/Winnow):
unreviewed goldens **80%** verdict / **90%** content-type
*theirs*. Distinct from kevinpita/winnow.
[IamBusy/OpenJev](https://github.com/IamBusy/OpenJev):
**45/60** vs v0.2 39/60; reversal 100%. `/v1/decide` ≠
TypeSafe.
[semif-serve](https://github.com/dddanielliu/semif-serve):
1164 vs 178 ms *theirs*. Wire-compat ≠ replica.
[pi-jev-skill-bench](https://github.com/iamdin/pi-jev-skill-bench):
43 gold; roster 50–500; **no live Jev numbers this pass**.
[jev-typed-evaluation-collapse](https://github.com/mleyvaz/jev-typed-evaluation-collapse):
Noul collapses conflict 0.50–0.57 vs ignorance 0.46–0.48;
named Choice separates p=1.0; binary Choice red 0.67–0.85
*theirs* (manuscript v0.3).
[DGUI_HYPERMEM-JEV](https://huggingface.co/datasets/ctaxnagomi/DGUI_HYPERMEM-JEV):
6-row flywheel (analyze 4 / rerank 2 / supersede 0);
sibling INSTRUCT_JEV.
TeoMastro `bench/results/summary.md` **404 this pass** —
do not invent numbers. `notes.md` §69. Do not copy npx /
uv / plugin how-to.

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
