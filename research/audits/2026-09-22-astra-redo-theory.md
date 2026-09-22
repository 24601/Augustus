# Independent theory and classical-method redo — 2026-09-22

Disposition for this scope: **fix-first**. Preserve the current mission and
most of the curation. Correct the distinction between runtime detection and
enforcement, remove calibration as a universal requirement for selective
classification, qualify Alloy's temporal checking, and repair the Jensen row.
The frontier extension below adds T5, a narrow distillation overstatement.
This is not a whole-release verdict. The coordinator owns integration and
acceptance; no runtime files were changed by this reviewer.

## Identity, scope, and method

- Task: `/root/astra_redo_theory`; requested route in the assignment:
  `gpt-6-astra`, `xhigh`. Observable context describes Codex based on GPT-6;
  the agent-list tool exposes task names/status only. No serving-model build,
  actual inference-route receipt, or token-usage metadata was exposed to this
  worker. The requested route is not independent runtime attestation.
- Reviewed working tree on `refresh/2026-09-22`, package `0.6.1-dev`, with
  `HEAD=192faf0d18d511154228af8ac40e1393567d828c`; observations through
  `2026-09-22T16:14:51Z`, before any coordinator corrections to these findings.
- Read `AGENTS.md`, `CONTRIBUTING.md`, `research/protocol.md`, and its fold
  prompt. Used the Augustus skill. Read the complete current `SKILL.md` and
  references `mental-models.md`, `methods-catalog.md`, `mappings.md`,
  `toolbox-mapping.md`, `composition-algebra.md`, `formal-methods.md`,
  `formal-semi-formal.md`, plus `validation.md` and `judgment-class.md` to
  resolve routed causal/DFL/conformal guidance.
- Re-derived the review from the mission, mathematical counterexamples, and
  primary sources below. Prior agent verdicts are not evidence for acceptance.
  Compared the scoped diff against published HEAD and selected pre-session
  baseline sections at `0b43a8d3b8d2d389b59415747f566dcbaa3f3ec8`.
  Large historical inventories were not treated as instructions or exhaustively
  reviewed. Checked canonical literature IDs against the current source
  registry; the September availability paper already has a source entry.

## Corrections required

### T1 — Runtime monitoring does not by itself enforce a property

`mappings.md:160-170` calls an `action -> exact monitor/probe` sequence runtime
assurance and says the monitor can override. `formal-semi-formal.md:28` assigns
enforcement of a temporal property to a runtime monitor. A post-action monitor
can detect an irreversible violation without preventing it. It may control
later actions, but that is a different guarantee. Some temporal requirements
also remain undecided on a finite trace.

Primary support: [Schneider, Enforceable Security Policies, 2000, §§2–4](https://www.cs.cornell.edu/fbs/publications/EnfSecPols.pdf)
characterizes execution-monitor enforcement with explicit restrictions;
[Black-Box Simplex, arXiv:2102.12981v3, definitions 3–5 and theorem 1](https://arxiv.org/pdf/2102.12981v3)
requires a decision module that preserves a safe continuation. These are theory
under their models, not evidence that this repository implements assurance.

Replace the mapping's diagram and adjacent explanation with:

```text
observe -> judgment proposal -> policy -> exact enforcement -> action
        -> authoritative outcome monitor/probe
```

> A monitor reports properties of the observed trace. Prevention additionally
> needs an enforceable property and a mechanism that can block or switch before
> the violation, with justified timing and recovery assumptions. A post-action
> probe cannot undo an irreversible act. In a physical controller, retain a
> safe fallback and a justified recoverable region; in software, validate and
> authorize the proposed operation and target at the effect boundary. Keep
> unknown or pending monitor results distinct from satisfaction.

In the short formal guide, change the row to “Monitor a stated trace property”
and add “Enforce a preventable violation | interlock/shield/controller with
explicit enforcement assumptions.” Link the detailed caveat once from the
canonical formal card. Falsifier: a payment/deletion or unsafe control command
can occur before the monitor's first veto. This is the highest-priority finding.

### T2 — Selective classification need not consume calibrated probabilities

`methods-catalog.md:30` requires target-population calibration for the entire
selective-classification row. This incorrectly excludes a margin, anomaly
score, or other ranking statistic whose accept/reject policy has been properly
evaluated. It also conflicts with the more precise indicator row later in the
same file.

[Geifman and El-Yaniv, arXiv:1705.08500v2, §§2–4](https://arxiv.org/pdf/1705.08500v2)
defines selective risk and coverage separately from a confidence ranking;
probability calibration is not a prerequisite for that ranking. Its particular
risk-control algorithm has additional sampling and selection assumptions.
This supports a broader placement, not permission to claim a guarantee after
an ordinary threshold sweep.

Use this replacement row:

```text
Selective classification | score/ranking or probability evidence for act/abstain |
selection rule, fallback, risk/coverage evaluation |
deployment-relevant labels and valid selection/evaluation;
calibration additionally required when policy interprets values as probabilities
```

Keep the separate cost-derived Bayes rule, with its probability and loss
assumptions. Falsifier: apply a strictly increasing transformation to a score
and transform the threshold accordingly. The accepted set and its selective
risk are unchanged although numerical probability calibration generally is not.

### T3 — Distinguish Alloy's object scope from its time horizon

`formal-methods.md:41,52-53` and `formal-semi-formal.md:31-34` describe the finite
relational/SAT mode but omit an available mode that changes the claim a green
run can support. [Official Alloy 6 documentation](https://alloytools.org/alloy6.html)
documents bounded temporal exploration and complete temporal checking through
NuSMV/nuXmv. The latter covers all traces within the finite signature scope.
It does not prove arbitrary object counts or the deployed implementation.

Suggested replacement:

> Alloy analyzes relational models in a finite signature scope. Alloy 6 also
> supports bounded temporal checking and, with a suitable backend, complete
> checking of all temporal traces in that finite scope. Record object bounds,
> temporal mode, backend, and completed result separately.

Keep the distinction from TLA+/TLC/Apalache. This is an official documented
capability, not a local reproduction. Counterexample to the old shorthand:
an Alloy 6 `1.. steps` run may establish a temporal property over all traces
of its fixed finite model; “only checked the first ten steps” would be wrong.

### T4 — Jensen permits equality

The theorem table in `methods-catalog.md` uses `E[f(X)] != f(E[X])` as its
Jensen condition. This is false for affine functions and some other cases.
The new permutation-averaging paragraph in `composition-algebra.md` correctly
uses a non-strict convex inequality and should be the consistent model.

Replace the table cell with:

> For convex `f`, `f(E[X]) <= E[f(X)]`; concavity reverses the inequality.
> Equality is possible. Preserve the distribution and utility assumptions.

Executed counterexample: for `X` equally supported at `0.8, 0.4` and
`f(x)=2x+1`, both sides equal `2.2`. No benchmark is needed to reject the
universal inequality-as-disequality.

## Guidance independently retained

- **Mission and no-model choices:** the entry point starts with evidence,
  action cost, and baseline; the toolbox rejects exact calculation, missing
  observations, proof, and authority as direct judgment substitutions.
  Domain examples span organizations, business, knowledge work, software,
  and personal workflows. The family catalog permits classical supervised
  models; Jev remains a preference, not an empirical dominance claim.
- **Policy arithmetic:** the binary threshold follows by comparing
  `(1-p) C_FP` with `p C_FN` under constant error costs and zero correct-action
  loss. EVSI compares optimal expected loss before and after an observation,
  net of its cost. Neither is a generic confidence threshold. MCDA keeps
  vetoes outside compensating sums and warns about Score units. If the
  weighted sum is intended as a representation of preferences, test omitted
  interactions as well as weight sensitivity; stable ordinal anchors alone
  do not establish cardinal utility.
- **Dependence and search:** same-state marginals do not identify a joint;
  empirical path-score products do not become calibrated path probabilities.
  A learned A* heuristic needs the relevant admissibility/consistency proof
  before optimality is claimed. A simulator supplies transitions and rewards
  only within its justified scope.
- **Permutation composition:** Jensen's comparison to average member loss is
  correct, including correlated members. It does not compare to the best
  member. Full permutation-group averaging of a fixed predictor, with aligned
  semantic IDs, is invariant to presented order; sampled permutations and
  service randomness need separate qualification. Executed `p=[0.8,0.4]`
  gives mixture log loss `0.510826`, average member loss `0.569717`, and best
  member loss `0.223144`. Binary Brier values are `0.16`, `0.20`, `0.04`.
  A three-label position-sensitive fixture gave identical aligned full-group
  averages under all six input orderings. These are arithmetic fixtures,
  not evidence of a provider's quality or runtime behavior.
- **Causal policy:** `judgment-class.md` correctly separates historical outcome
  prediction from intervention benefit. [Athey and Wager, arXiv:1702.02896v6,
  §§1–2](https://arxiv.org/pdf/1702.02896v6) supports learning constrained
  treatment policies under an identified causal design. Extend the design
  card with consistency/interference assumptions when the application needs
  them; do not require one identification strategy universally. Shadow labels
  alone do not reveal outcomes of actions never taken.
- **Decision-focused learning:** the existing family row appropriately changes
  the training objective and evaluation target while keeping constraints in
  the solver. [SPO, arXiv:1710.08005, §3](https://arxiv.org/pdf/1710.08005)
  measures downstream decision regret, with explicit treatment of optimizer
  ties. [DF², UAI 2025](https://proceedings.mlr.press/v286/kong25a.html) learns
  an expected optimization objective; its abstract is sufficient here only
  to confirm that distinct family shape. Its reported experiments were not
  reproduced and no universal advantage is inferred. No additional runtime
  catalog expansion is justified by this review.
- **Conformal methods:** the current validation card properly separates
  marginal set coverage, probability calibration, and conditional selective
  error. [Conformal Risk Control, theorem 1](https://arxiv.org/pdf/2208.02814)
  concerns an expected loss under exchangeability, boundedness, monotonicity,
  right-continuity, and an admissible conservative endpoint. It is not a
  per-case or simultaneous-subgroup certificate. The card's instruction to
  inspect the actual theorem is appropriate; its ordinary evaluator does not
  implement this procedure.
- **September 2026 evidence:** independently inspected [Available Guardrails,
  arXiv:2609.22048v1, September 18, §§3.1–3.2](https://arxiv.org/pdf/2609.22048v1).
  Planning accepted-case support per required reporting unit materially affects
  whether a policy can be certified. The existing validation addition keeps
  the frozen-policy/IID and multiplicity limits and does not claim to implement
  the paper's optimizer. Executed exact-binomial arithmetic confirms the
  95% upper bound after 20 error-free cases is `0.139108`; 298 cases give
  `0.0100024`, and 299 give `0.00996915`. These calculations do not reproduce
  the paper's empirical results.

## Evidence limits and integration gate

Primary literature and official documentation above were retrieved on
2026-09-22. Article PDFs were inspected at the cited definitions/theorems;
this was a targeted conceptual review, not an exhaustive 2026 literature
census or proof audit of every tool named in the catalog. The unversioned
CRC/SPO PDF endpoints should be pinned if promoted to a durable source card.
The availability HTML route returned 404; its versioned PDF was available.
The CRC v5 HTML route and one Apalache principles URL failed; no conclusion
was inferred from those failures. No paid search, external model inference,
third-party code/weights, external write, or Git mutation was performed.

Checks run on the observed shared tree: `make check` passed repository checks,
53 unit tests, both numerical self-tests, and shell syntax; `git diff --check`
passed. The report was read back in full. These checks precede T1–T4 integration.
The arithmetic above was computed with local Python standard-library code;
the following reproduces its principal counterexample and sample-support values:

```python
from math import ceil, log
p = (0.8, 0.4)
m = sum(p) / len(p)
print(-log(m), sum(-log(x) for x in p) / len(p), min(-log(x) for x in p))
print((1-m)**2, sum((1-x)**2 for x in p) / len(p), min((1-x)**2 for x in p))
print(sum(2*x+1 for x in p) / len(p), 2*m+1)
print(1-0.05**(1/20), ceil(log(0.05)/log(0.99)))
```

Before accepting this scope, integrate T1–T4 and inspect the complete diff.
Exercise fresh behavioral prompts covering an irreversible action followed
by a monitor, an uncalibrated score with a measured reject policy, and an
Alloy temporal result. Repository checks cannot certify those answers.
The coordinator retains final acceptance and any broader release decision.

## Frontier-research redo extension

This independently closes the separately identified `research_frontier`
assignment as well as the original `curate_theory` scope. Additional inspected
artifacts: complete `research/decision-model-review-2026-09-21.md`, current
`research/decision-model-review-2026-09-22.md`,
`research/archive/pre-review-2026-09-21.json`, the relevant research README,
and complete `optimizer-integration.md` and `mixed-architecture.md` references.
The archive manifest identifies pre-review source commit
`0b43a8d3b8d2d389b59415747f566dcbaa3f3ec8` and per-file fingerprints; it is a
preservation receipt, not proof that those recommendations are sound. Inspected
selected Git history, including integration commit `1a42174`; no Git mutation.
Old reports supplied candidate claims to investigate, never acceptance evidence.

### Promoted concepts independently retained

- **Family boundaries:** [GLiClass v1, methods and limitations](https://arxiv.org/html/2508.07662v1)
  supports prompt-label classification; its main uni-encoder jointly processes
  text and labels. The paper also reports calibration and label-granularity
  limitations. [GLiNER, NAACL 2024](https://aclanthology.org/2024.naacl-long.300/)
  supports open-schema entity extraction with a bidirectional encoder. These
  distinguish classification from locating evidence, not calibrated probability
  from uncalibrated probability. The current [GLiNER2 official repository](https://github.com/fastino-ai/GLiNER2)
  documents extraction, classification, and structured outputs. The current
  skill correctly allows multiple surfaces from one family; a brand is not an
  immutable single-task type. No model was run, and no latency/quality advantage
  was independently measured.
- **Tabular placement and artifact identity:** the [TabPFN Nature paper](https://www.nature.com/articles/s41586-024-08328-6)
  evaluates a particular small/medium-tabular regime, including datasets capped
  at 10,000 samples and 500 features. It does not establish supremacy for all
  table sizes, nonsmooth tasks, or later checkpoints. Separately, the pinned
  [v9.0.0 release](https://github.com/PriorLabs/TabPFN/releases/tag/v9.0.0)
  and [v9.0.0 README](https://raw.githubusercontent.com/PriorLabs/TabPFN/v9.0.0/README.md)
  document a 3.5 default and separate code/weight licensing. Preserve explicit
  checkpoint, runtime, resource, and license review; do not transfer paper
  findings to a version merely sharing the name. Documentation claims are not
  local benchmarks or legal approval. No authentication, installation, weights,
  or provider inference was attempted.
- **Routing:** [RouteLLM, ICLR 2025, §§3–4](https://proceedings.iclr.cc/paper_files/paper/2025/file/5503a7c69d48a2f86fc00b3dc09de686-Paper-Conference.pdf)
  learns relative model preference using pairwise data and a cost/quality
  threshold. That target is not a general probability of task success. Retain
  the skill's always-small/always-large/rules comparisons, total routing cost,
  residual-population evaluation, and selection-propensity logging. Conditioning
  on the route changes the evaluated population; global model calibration does
  not establish calibration there. Routing also does not grant action authority.
- **Prompt optimization:** [GEPA, §3 and evaluation design](https://arxiv.org/pdf/2507.19457)
  uses execution traces and feedback to propose prompt changes, with
  task-instance Pareto selection. It supports the current reflection-loop
  description, not a guarantee that reflection beats simpler search on a new
  task. Retain frozen tests outside feedback, independent outcome metrics,
  versioned candidates, and comparisons at equal total evaluation cost. Its
  own validation rollouts contribute material cost. The retrieved PDF was an
  unversioned endpoint; pin the exact revision before a durable implementation
  decision. No Ax/DSPy API or optimizer execution was validated here.
- **Evaluation and selection:** [Reassessing How to Compare and Improve the Calibration of Machine Learning Models, ICLR 2025, §3](https://proceedings.iclr.cc/paper_files/paper/2025/file/9a30247fcca95299c2fd48d4667282de-Paper-Conference.pdf)
  constructs recalibration that can improve calibration metrics while degrading
  proper scores. This independently supports the current warning against
  ECE-plus-accuracy as a complete quality criterion. Risk/coverage and proper
  scoring rules answer different questions. The September 21 report's
  requirement that every selective score be calibrated is rejected by T2;
  retaining that report as history must not restore the requirement.
- **Causal versus decision-focused learning:** the fresh Athey–Wager and SPO
  inspections above support distinct questions: identifying intervention value
  versus training for downstream optimization loss. Neither a prognostic score
  nor decision-focused training supplies missing causal identification. DF²'s
  abstract confirms another objective-learning family, not deployment advantage.
  Current runtime placement is appropriately conditional; no new mandatory
  solver, causal estimator, or family expansion follows from these papers.

### Recent sources: useful caveats versus watchlist metadata

| Source and inspected depth | Independent disposition |
|---|---|
| [Selective Conformal Risk Control, 2512.12844v2](https://arxiv.org/pdf/2512.12844v2), theorem 2, §4.4, and calibration-only variant | Retain the need for a selection-aware procedure. §4.4 explicitly excludes the practical set-size threshold search from theorem 2. Its reusable-threshold PAC variant uses different assumptions and a finite-grid bound. Watchlist, not a certificate for the repository's threshold sweep. |
| [Action-Conditional Conformal Prediction, 2606.05551v2](https://arxiv.org/pdf/2606.05551v2), theorem 4.3/corollary 4.4 | Conditional coverage requires its construction and assumptions; rare actions affect efficiency bounds. Inference: conditioning on a chosen action is not identification of outcomes under an intervention. Keep the existing causal boundary. No implementation or proof reproduction. |
| [Available Guardrails, 2609.22048v1](https://arxiv.org/pdf/2609.22048v1), September 18, certification construction | Independently retained above because accepted-case sample support changes certification planning. Frozen-policy and reporting-unit/multiplicity limits remain material. No empirical performance claim adopted. |
| [Drift-Aware LLM Routing, 2609.00662v1](https://arxiv.org/pdf/2609.00662v1), September 1, model, audit assumptions, controller, theorem statement | The hard resource meter supplies pathwise feasibility; prediction uncertainty does not. Statistical claims assume appropriate feedback, and audit expense sits outside the displayed routing budget. Its comparator is a paced fluid benchmark, not an unrestricted oracle. Watchlist; useful reinforcement of existing effect-boundary enforcement and full-cost accounting, not a new production router. |
| [Strategic Decision-Focused Learning, 2609.14907v1](https://arxiv.org/abs/2609.14907v1), September 14, abstract only | Strategic response can decouple predictive accuracy from payoff. Retain as a feedback-loop research question; no theorem, reproducibility, or runtime promotion independently established. Versioned PDF retrieval failed. |
| [Decision-Focused Learning tutorial, 2606.21773](https://arxiv.org/abs/2606.21773), abstract only | A useful research pointer, not additional evidence for a general performance rule. No runtime expansion. |
| [Population AURC, ICML 2025](https://proceedings.mlr.press/v267/zhou25y.html), metadata/abstract; [selective classification under shift, 2405.05160v2](https://arxiv.org/abs/2405.05160v2), abstract | Research leads, not inspected estimator/proof implementations. Existing risk/coverage guidance rests on the separately inspected selective-classification definitions; no claim to reproduce these papers. |

The distinction in the table is intentional: checking a canonical identity,
abstract, or release contract closes a metadata question, not its empirical or
mathematical claims. The failed DF² PDF fetch likewise leaves that entry at
abstract depth. September additions do not displace the simplest viable
rules/classical/no-model baseline.

### T5 — Distillation can inherit errors, but need not reproduce all of them

`optimizer-integration.md:201-202`, observed at `2026-09-22T16:25:12Z`, says
that distillation reproduces teacher errors unless independent outcomes
correct them. This is too categorical. A constant-probability student trained
only by cross-entropy to teacher probabilities `[.9,.9,.1,.9,.9]` has optimum
`q=.74`. On five equally likely inputs whose true labels are all positive,
the teacher has error `0.2` and the student `0`. The true labels are used to
evaluate this counterexample, not to train its student. The restricted student
family can suppress an error without new corrective labels. This is an
existence counterexample, not a prescription to distill without evaluation.

Executed local standard-library arithmetic confirmed those values and a
teacher-only mean loss of `0.573057` at the optimum versus `0.595882` at `.64`
and `0.605493` at `.84`. [Born-Again Neural Networks, equations 2–3 and §4](https://proceedings.mlr.press/v80/furlanello18a/furlanello18a.pdf)
also studies teacher-target training and reports students improving on their
teachers; those experiments were not reproduced.

Replacement:

> Distillation can inherit teacher errors; teacher agreement alone does not
> establish correctness. Evaluate against independent outcomes.

Keep the independent-outcome gate and the warning that a compatible wire
format does not imply equivalent semantics. If retaining “Training requires
independent gold,” make clear that it is this workflow's qualification policy,
not a universal mathematical requirement for training a student.

### Extension limits and handoff

Requested route remains `gpt-6-astra/xhigh`; this worker still has no independent
serving-route receipt. This extension used fresh primary-source reads, not
previous agents' endorsements. It does not reproduce model benchmarks, run
third-party code, establish commercial license eligibility, audit every proof,
or claim an exhaustive September literature search. Historical popularity,
release counts, and earlier package-version observations were not promoted.

At extension readback the coordinator's T1–T4 corrections were present in the
scoped runtime text and addressed the reported conceptual defects. That is a
textual integration observation, not whole-release acceptance. Frontier-scope
disposition: **fix-first for T5; otherwise retain current conditional guidance
and leave the listed research leads on the watchlist**. The coordinator owns
T5 integration, fresh behavioral acceptance, and any broader release verdict.

Extension checks on the shared tree: `make check` passed repository checks,
68 unit tests, both numerical self-tests, and shell syntax; `git diff --check`
passed. The extended report was read back. The higher test count reflects
concurrent coordinator/team work, not tests authored by this reviewer.
