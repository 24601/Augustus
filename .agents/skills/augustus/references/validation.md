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
  (ECE/NLL/Brier).

### Composition

| Layer | Tool | Scores |
|---|---|---|
| Decision stage (typed marginals) | jevals (+ contrastive pairs / Nimble-style) | accuracy, Brier/ECE, latency/$, traces |
| Perception→state contracts | schema PBT + stage metrics (IoU/WER) | interface falsifiers |
| End-to-end product / agent loop | Harbor taskset | behavioral assertions, cost/perf bounds |
| LM-program knobs only | DSPy/Ax (narrow) | never primary System One calibration score |
| Reward-hack / eval gaming | [rh-guard](https://github.com/24601/rh-guard) | structural deny + System One sidecar |
| Project soft-rule lint | [Abide](https://github.com/coldteadotai/abide) | Score per rule on the diff; bands; fail-open; replay + independent review |
| Collab / computer-use product loop | [jev-testbench](https://github.com/ufx7/jev-testbench); [solari-reflex](https://github.com/hitakshiA/solari-reflex) | Wilson/McNemar arms; independently checked task time |

rh-guard is a reward-hack hook, a different surface from jevgate and
from Abide (eval-integrity vs allowlist-remainder vs project soft
rules). One row each. ECE above is wanted, not a Nimble result.
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
vs 98.4 s (`notes.md` §48). **Collab-arm curriculum:**
[jev-testbench](https://github.com/ufx7/jev-testbench) —
`llm_autonomous` vs `scripted_plus_jev` vs `llm_plus_jev`; Wilson +
McNemar; Jev is not a peer arm. Bake into jevals/Harbor hygiene, do
not copy the harness.

### Bake-off mandate

Before adopting proprietary Jev vs Laya vs TypeAR vs Nimble vs kev vs
blackwood-rlcd vs Archer vs openjev-lm, run a jevals-shaped labeled suite (or an equivalent
with this hygiene) and, for a product loop, a Harbor taskset. A design
card with no eval path is incomplete. A green smoke test on
[jev-local](https://github.com/us/jev-local)'s **default stub** is not
that bake-off (`notes.md` §48).

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
