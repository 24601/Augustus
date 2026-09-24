# Synthetic data, labeling and hill-climbing infrastructure for the 0.8.0 trainer skill

Lane: synthetic-data creation, labeling and hill-climbing infrastructure.
Date: 2026-09-23. Status: confidential 0.8.0 research. Nothing here has been posted, pushed or published.
Scratch and raw captures: `research/080/tmp/synthetic-data/`.

Evidence labels follow `research/protocol.md`:

- **Contract**: behavior documented in, or read from, the source or docs at the pinned revision.
- **Reported**: a third party's number or claim. None was re-run.
- **Reproduced**: a local computation this lane actually ran. Here that means fixture arithmetic and simulations only, never a third-party project.
- **Hypothesis**: a mechanism or design claim that has not been tested on a task we control.
- **Unknown**: the evidence is unavailable.

No third-party code was installed or executed, and no paid search was used. Repo-local evidence was reused where it existed: the patrol packets `wf1-patrol-*.json` from 2026-09-23 and `notes.md` §45.

---

## 0. Bottom line

1. **Keep two provenances on every row, `text_source` and `label_source`, and derive the evidence kind from them instead of letting anyone declare it.** Most synthetic-data failures happen because a row's text or its label is treated as real when it is not. Teacher-labeled real traffic has a realistic distribution but a proxy label. Generated text with a generator label is synthetic on both axes. Programmatic minimal pairs have exact labels, but only relative to the program. `compare_workflows.py` already downgrades `proxy` and `fixture` evidence, so the only work needed is to make that field derived. (Design; Hypothesis.)
2. **Collect gold first.** Before generating anything, sample the confirmation set from real traffic with known inclusion probabilities, label it independently of the teacher, then hash and freeze it. kev's own skill says "real rows measure, synthetic rows train" (Contract). Its documented workflow still shows the same real rows to the generator as style examples, and then uses them for calibration and development. The only exclusion is an exact state-hash match, so paraphrased near-copies survive. That is the contamination mechanism reported in arXiv:2311.04850 (Contract for the workflow; the size of the leak is Unknown).
3. **Contamination and dedup audits must fail closed.** von's `contamination_audit.py` at `657f42f` prints `[audit] CLEAN` and exits 0 when its reference directories are missing. When only some reference sources are missing it gives no warning at all (Contract, read from source). The shipped audit should return `unknown` (exit 2) on any missing, empty or count-mismatched reference. It should also refuse to say `clean` unless a planted canary duplicate was caught in the same run.
4. **The confirmation helper is the right anchor, but its bound is expensive in gold labels.** Take a 0/1 loss where the candidate wins on 8% of cases and loses on 3%. The Hoeffding bound in `compare_workflows.py` needs about 2,397 paired units to support strict improvement at α=0.05, K=1 (3,685 at K=5). An exact sign test on the discordant pairs gives p=0.0068 at n=300, and an empirical-Bernstein bound supports the improvement at about 1,000 (Reproduced; fixture arithmetic). If the trainer skill confirms only with Hoeffding, gold-label budgets will usually end at `insufficient_evidence`. That creates pressure to relabel proxy data as observed. **Decision for the maintainer:** add an exact paired test or a variance-adaptive bound.
5. **Sticky non-inferiority champions drift when the challenge reuses the selection rows.** In kev's autoresearch loop the round's best trial is picked on the transfer rows and then challenged on those same rows (Contract). In a simulation where every candidate is 0.5 pp worse than the champion, a best-of-8 challenge on the same rows accepted 36% of rounds and drifted −1.8 pp over 10 rounds. Re-scoring on fresh rows accepted 5% and drifted −0.26 pp (Reproduced simulation; a Hypothesis about real kev runs). Guard: challenge on fresh rows, and always report the delta against the original anchor as well as against the last champion.
6. **Hill-climbing tools are search engines, not acceptance tests.**
   - Karpathy's `autoresearch` keeps an edit whenever `val_bpb` strictly improves on one pinned validation shard. It has no seed replication and no held-out confirmation (Contract).
   - The 2026 optimizer papers report large gains alongside large variance and low-data regressions (Reported).
   - A 2026 skill-optimization study found GEPA's +4.9 pp not separable from run-to-run variance.
   - Borrow the good infrastructure: frozen evaluator, allow-listed knobs, spend cap, append-only ledger, seed-noise measurement, reseeded verification, leave-one-out edit pruning. Keep acceptance in the confirmation step.
7. **Ship five small standard-library scripts plus the two existing helpers; everything else is installed on demand.** Several popular data tools are in maintenance or community mode as of 2026-09:
   - Argilla gets bug fixes only.
   - distilabel is maintained by the community.
   - Argilla's synthetic-data-generator is deprecated in favor of `huggingface/aisheets`.
   - DataDreamer has had no commits since 2025-02.
   - modAL has had no commits since 2023-06.
   - The Snorkel open-source project is de-emphasized in favor of Snorkel Flow.

   None of them should be a required dependency (Contract, from READMEs and commit dates).
8. **"Don't train" is the first gate, not an afterthought.** Exits: a rule or exact code already decides the case; a hosted or few-shot baseline already meets the bar on a real pilot; there is no feasible route to enough independent gold; criteria change faster than the retraining cadence; the labels are too subjective to agree on. arXiv:2310.07849 reports that subjectivity lowers the value of synthetic data (Reported).

---

## 1. What was inspected

- **Source, read in full or at section level:**
  - `jaredpalmer/kev` at `557598f`: `kev/autoresearch.py` in full; `kev/metrics.paired_bootstrap`; the docstrings of `kev/calibrate.py` and `kev/contrastive.py`; the NOTA and unknowable handling in `kev/data.py`; `scripts/verify_claims.py`; the whole `skills/kev-finetune/` skill (SKILL.md, both references, `generate_data.py`, `split_data.py`, `plan_size.py`).
  - `wfzyx/von` at `657f42f`: `training/contamination_audit.py` in full.
  - `karpathy/autoresearch` at `228791f`: README, `program.md`, and the eval and split parts of `prepare.py`.
- **READMEs and docs:** distilabel, curator, DataDreamer, Argilla, synthetic-data-generator, NeMo DataDesigner, sdg_hub, DeepFabric, Kiln, Snorkel, ppi_py, GEPA, text-dedup, datatrove; the DSPy optimization docs at `4b60eb4`.
- **Metadata only:** cleanlab, small-text, modAL, Label Studio, SetFit, llm-decontaminator, aisheets, AIDE, OpenEvolve, ShinkaEvolve, AI-Scientist-v2, yourbench, synthetic-data-kit.
- **arXiv:** 57 abstract pages fetched directly (the latest version is recorded per source). The claims used from 2609.26758, 2609.25938, 2609.20758, 2609.12742 and 2609.16793 go beyond their abstracts and come from today's methods patrol packet, which read their sections. They were not re-read here.
- **Failed fetches:** arXiv 2604.08801 and 2605.22169 (HTTP 406). The arXiv export API returned HTTP 429. Karpathy's X posts were not collected, because paid or X collection is out of scope.
- **Local runs (Reproduced, fixture only):**
  - `hoeffding_vs_exact.py` runs the repo's own `compare_workflows.py` on synthetic receipts.
  - `champion_drift_sim.py` is a stdlib Monte Carlo simulation.

---

## 2. The shape of the problem

A classifier trained on synthetic data changes up to three things at once: the input distribution, the label source, and the oracle used to score it. The pipeline has to keep these separate. Every row therefore gets a **data role**, and each role has its own provenance rule:

| Role | May contain | Used for | Must never be |
|---|---|---|---|
| `train` | anything with recorded provenance (generated, programmatic, teacher-labeled real text, human) | fitting | a scoring source for acceptance |
| `search` (dev) | synthetic or real; teacher or program labels allowed | descriptive comparison during the climb, error analysis | cited as confirmation; seen by the generator after it has been used to find errors |
| `calibration` | **real** text at the **deployment prior**; independent labels preferred | temperature/threshold/abstention fitting (`evaluate_decisions.py`) | balanced synthetic data (it would calibrate to the wrong prior) |
| `confirm` | **real** text sampled with known probability; **observed outcomes or adjudicated labels**; frozen and hashed before generation | one paired confirmation per frozen finalist family (`compare_workflows.py`) | shown to the generator or teacher prompts, used in search, or reused adaptively after its outcomes have been read |
| `probe` | derived variants (permutations, name rebinding, NOTA removal, evidence removal) with a `parent_id` | behavioral stress tests | counted as independent units |

This operationalizes rules that Augustus already has: teacher labels are measurements, splits go by entity or template, and there is a search/confirm separation (`validation.md`; `optimizer-integration.md` steps 3–5).

---

## 3. Generation methods: mechanism, when each helps, and how each fails

| Method (2025–26 state) | Mechanism | Evidence | Fails when | Guard |
|---|---|---|---|---|
| **Teacher labeling of real unlabeled traffic** (distillation for classification) | Input distribution is real; only the label is synthetic | arXiv:2406.17633: classifiers fine-tuned on GPT-4 labels were comparable to human-label classifiers on 14 CSS tasks (Reported). arXiv:2604.13899v5 (2026-08): LLM labels at scale beat human-supervised classifiers at about 1/10 the cost, but "only a two-question decomposition mirroring the human annotation task unlocks it", error structure depends on the LLM, and "humans remain essential as evaluators" (Reported). arXiv:2303.15056 (2023, older): similar crowd-worker comparison | The teacher's systematic errors become the student's. Evaluating against teacher labels hides them. Aggregate gains can hide a dead class: arXiv:2609.09702 (2026-09) reports a correctness-weighted distillation arm at +0.166 accuracy with **zero Refuted recall in every seed** (Reported) | Confirm only on independent labels. Set per-label recall floors. Report teacher agreement separately and never as accuracy |
| **Candidate or soft teacher labels** | Keep the teacher's ambiguity instead of forcing one label | arXiv:2506.03857 CanDist (Reported, abstract level) | Soft targets can be read as calibrated truth | Treat as a training target only; qualify probabilities on real calibration data |
| **Class-conditional generation from a spec** (kev `generate_data.py`) | Asks the generator for N records with given label targets, plus guidance and variety axes | Contract: kev's prompt lists "Label targets for this batch … per question" and balances uniformly by default. arXiv:2306.15895 (AttrPrompt): simple class-conditional prompts show systematic biases (for example regional); attribute-diversified prompts reach the same performance at about 5% of the query cost (Reported). arXiv:2310.07849: subjectivity at task and instance level is negatively associated with synthetic-trained performance (Reported) | Prototypical, label-first text. Label words leak into inputs (Hypothesis). A uniform prior miscalibrates. Style examples leak eval rows (see §5) | Attribute or persona conditioning. Deployment-prior calibration. Keyword-ablation probe. Style seeds from a partition that is never evaluated |
| **Persona / taxonomy / topic-graph conditioning** (Persona Hub arXiv:2406.20094; GLAN arXiv:2402.13064; LAB arXiv:2403.01081; DeepFabric topic graphs; DataDesigner samplers) | Adds diversity along declared axes | Reported, abstract/README level. DeepFabric advertises "100% topic coverage" | The coverage measured is coverage of the **generator's own taxonomy**, not of real traffic | Measure synthetic-vs-real separability; evaluate only on real confirm data |
| **Self-Instruct / Magpie** (arXiv:2212.10560, 2406.08464) | Bootstraps instructions from a model | Instruction tuning, not classifiers | Mostly irrelevant to fixed-label decisions | Borrow only the similarity-filter step |
| **Programmatic minimal pairs** (kev `contrastive.py`) | Labels are a pure function `evaluate(facts)`, and missing facts give `UNDETERMINED`. Two code-level checks run on each pair. **Ablation:** removing any evidence sentence must make the label `UNDETERMINED`. **Invariance:** removing filler must leave it unchanged. Splits are by `family_id` | Contract (source) | Template artifacts. The labels are exact only **relative to the program**, so scoring against that program measures reading fidelity on synthetic text, not product accuracy | Split by family. Treat as `fixture` evidence. Score real transfer separately |
| **Counterfactual / contrast sets** (CAD arXiv:1909.12434; contrast sets arXiv:2004.02709; Polyjuice arXiv:2101.00288) | Minimal edits that flip the label expose spurious decision boundaries | CAD: classifiers trained on original data fail on the revised data and vice versa (Reported, 2019–2021, older) | LLM-generated counterfactuals may not flip the true label | Verify flips with a program or a human. Keep pairs together in one split |
| **Hard-negative / near-miss mining** | Pick examples of other labels that are close to the decision boundary | NV-Retriever (arXiv:2407.15831): positive-aware mining exists to remove **false negatives** (Reported) | Mined "negatives" from an unlabeled pool may be positives. Unlabeled is not negative; Augustus already says unobserved outcomes are not negative labels | Label mined negatives before training on them; mark `label_source` |
| **NOTA / other coverage** (kev `data.py`) | "None of the above" appears both as the correct answer (true option removed) and as a wrong distractor (true option kept), with varied wording. A `none_pair` test covers both cases | Contract (source). Motivated by kev's first run, which learned "this wording ⇒ pick it" (`notes.md` §45) | The hatch becomes a wording shortcut | Train and test both sides of every hatch (§8, row 5) |
| **Missing-evidence ("unknowable") pairs** (kev `metrics.unknowable_report`) | Deciding evidence is removed, the record is trained with a uniform soft target, and it is scored against its intact control | Contract. Patrol, Reported: Decision-1.0-Lux-9B puts 20.91% of answers at P≥0.9 under missing evidence, against 0.00% for Kev-9B, despite leading on headline accuracy | A uniform target over the offered options mixes up "evidence absent" with "genuinely balanced". Policy code cannot tell them apart (Hypothesis) | Prefer an explicit `unknown` route or a separate "is it determinable?" question. Probe with evidence removal plus a control |
| **Distribution matching / reweighting** (SynAlign arXiv:2502.08661; arXiv:2410.21526) | Uses a little real data to weight or filter synthetic rows toward the real distribution | Reported, including an online A/B test for SynAlign | Weights fitted on data that is later evaluated | Fit weights on `search`/`train` real rows, never on `confirm` |
| **Iterative regeneration** | Retraining on your own outputs | arXiv:2305.17493: tails of the distribution disappear when generated data **replaces** real data. arXiv:2404.01413: **accumulating** real and synthetic data avoids collapse in their settings (Reported). Bias inheritance: arXiv:2502.04419 (Reported) | Replacement loops. Generator bias amplified | Keep real rows in every mix. Monitor per-slice error on real confirm data |

---

## 4. Labeling: teacher, weak supervision, active learning and humans

- **Label sources to record:** `observed_outcome`, `human_adjudicated`, `human_single`, `teacher:<model>@<rev>`, `program:<fn>@<sha>`, `weak:<label-model>@<rev>`, `generator:<model>@<prompt-sha>`.
- **Weak supervision.** Snorkel (arXiv:1711.10160; the repo now directs users to Snorkel Flow) denoises labeling functions without ground truth. "LM in the loop" (arXiv:2205.02318) turns prompts into labeling functions and reports a 19.5% error reduction over zero-shot on WRENCH (Reported).
  - Mechanism risk: several prompts to the *same* LLM are correlated sources. A label model that assumes conditional independence will overcount them (Hypothesis, grounded in the label model's assumptions).
  - Use a label model only when the sources are genuinely heterogeneous (rules, metadata, different models). With one teacher it adds little.
- **Confident learning** (cleanlab; arXiv:1911.00068) estimates label noise under a class-conditional noise assumption. Use it to triage teacher labels for human review, not to certify them.
- **Active learning.**
  - arXiv:2604.13899v5 found that active learning "provides no reliable advantage over random sampling in our prefiltered pool" (Reported).
  - arXiv:2504.04506 reports that most active-learning methods struggle at low budgets and favors coverage-based selection there (Reported).
  - Most important: an uncertainty-sampled labeled set is a **selected sample**. It is fine for training labels but must not be used as an evaluation set.
  - When the labels must also support *estimation*, use known-probability designs: active inference (arXiv:2403.03208v3, updated 2026-04) or confidence-driven inference (arXiv:2408.15204, which reports more than 25% fewer human labels). Both are valid only with recorded inclusion probabilities.
- **Human-in-the-loop tools.**
  - Label Studio is active (pushed 2026-09-23).
  - Argilla is "not adding new features going forward" (bug fixes only).
  - Model pre-annotation anchors reviewers. In a patrol-carded N=535 study (arXiv:2609.16793), deference rose with model competence, and confidence after seeing the advice separated correct from incorrect answers less well (Reported). So a blinded subset (no suggestions shown) is needed to measure adjudicator accuracy.

---

## 5. Dedup, splits and contamination, and how audits fail open

- **Split by the real independent unit:** family, template, seed, persona, source entity, or time window.
  - kev's `split_data.py` groups by an exact normalized state hash and drops exact duplicates and label conflicts (Contract).
  - That misses near-duplicates across splits. arXiv:2107.06499 reports that train–test overlap affects over 4% of the validation sets of standard datasets (Reported, 2021).
- **Near-duplicate methods:**
  - MinHash/LSH, SimHash, suffix arrays and Bloom filters (text-dedup, datatrove; Contract).
  - Embedding-based semantic dedup (SemDeDup arXiv:2303.09540, Reported).
  - N-gram decontamination is bypassed by paraphrase and translation. arXiv:2311.04850 found test overlap even inside GPT-3.5/4-generated synthetic datasets (Reported, 2023).
- **Leak paths specific to this skill:**
  1. **Style examples.** kev's documented Phase 1 passes `--examples data/x.real.jsonl` to the generator. The data-generation reference also suggests splitting the same real rows half and half into calibration and development via `--holdout`, and generated rows are excluded only when their state matches exactly. The prompt text "write new ones, do not copy" is an instruction, not a check (Contract). Guard: draw style seeds from a separate real partition that is excluded from calibration and confirm, and run a near-duplicate audit between generated train rows and all real evaluation partitions.
  2. **Error-driven targeted generation.** kev's hill-climbing loop reads `errors.jsonl` from development, narrows the spec to the failing pattern, and regenerates (Contract). That uses the dev set adaptively and can produce paraphrases of dev failures. kev itself says to "stop tuning against it after a few rounds" and to hold back an untouched real file (Contract). Guard: generate from the *description* of a failure pattern, not from the failing texts; audit against dev; rotate dev; confirm on `confirm` data.
  3. **Hosted evaluation.** Hosted evaluation exposes the holdout to the operator. JevBench v1.4 flags operators whose endpoints received sealed item text (patrol, Reported).
- **Fail-open audits.** In von `training/contamination_audit.py` at `657f42f` (Contract, source read in full):
  - A reference source whose directory is absent yields zero items.
  - `build_reference_index` warns on stderr only if *every* source is empty.
  - `run_audit` then prints `[audit] CLEAN - 0 records share an 8-gram shingle…` and exits 0.
  - A partially missing source (for example one absent tier file) produces no warning.
  - The reference paths are hard-coded under `/tmp`.

  The general pattern: **an audit that cannot see its reference reports absence of evidence as clean.** Augustus already says that missing evidence is `unknown`, not clean (`applied-mappings.md`, per patrol). The shipped audit has to enforce that in code.

---

## 6. Evaluation statistics for a trainer

1. **Use paired, clustered comparisons.**
   - arXiv:2411.00640 recommends: clustered standard errors when questions come in groups; inference on question-level **paired differences**; power analysis before running (Contract as recommendations; verified in the HTML).
   - kev's `paired_bootstrap` is a record-clustered percentile bootstrap. It recomputes the full statistic on every resample, macro-averages over tasks, and refuses mismatched labels or option order (Contract). That makes it a good *search-phase* descriptive tool.
2. **Plan sample size before generating.**
   - kev `plan_size.py` uses the McNemar approximation with discordant share p_d = gain + 2×regressions. For example, detecting +5 pp at 80% power with 3% regressions takes about 343 development questions (arithmetic from their formula). It also enforces at least 100 calibration questions (Contract).
   - kev reports that on its example workload, 400 records gave +0.6 pp ± 6 and 1,050 records gave +5.9 pp [+2.3, +9.7] (Reported).
   - `validation.md` already has the zero-failure bound: 299 error-free cases are needed to support at most 1% error at 95%.
3. **The Hoeffding confirmation is valid but conservative for sparse-discordance 0/1 losses.** Fixture: the candidate wins on 8% and loses on 3% of units (true Δ = −0.05). Receipts were run through the repo's `compare_workflows.py` (Reproduced):

   | n | K | Hoeffding upper Δ (tool) | tool assessment | exact sign-test p (one-sided, discordant pairs) | empirical-Bernstein upper Δ (Maurer & Pontil, arXiv:0907.3740) |
   |---|---|---|---|---|---|
   | 300 | 1 | +0.091 | insufficient_evidence | 0.0068 | +0.059 |
   | 1,000 | 1 | +0.027 | insufficient_evidence | 1.0e-6 | −0.005 |
   | 2,500 | 1 | −0.001 | bound_supports_loss_margin | 1e-14 | −0.025 |
   | 2,500 | 5 | +0.011 | insufficient_evidence | 1e-14 | −0.019 |

   In closed form, strict improvement requires n > 2·ln(K/α)/Δ²: 2,397 units at K=1 and 3,685 at K=5. Gold labels are the scarce resource, so this gap decides whether the trainer can ever confirm anything.
   - An exact sign test tests only superiority (no margin) and assumes independent units and a fixed n.
   - Empirical Bernstein keeps the distribution-free property and adapts to the small variance of mostly-concordant pairs.

   **Decision:** add one of them to `compare_workflows.py` as a declared method, keeping Hoeffding as the default for general bounded losses.
4. **Champion rules.**
   - **kev (Contract, `kev/autoresearch.py`):**
     - A challenger replaces the incumbent only if the record-clustered paired bootstrap of macro transfer accuracy gives Δ > 0 **and** a 95% lower bound ≥ −1 pp, against the champion's *best* seed.
     - A replication of the champion's own config joins it (seeds are averaged).
     - The docstring says "A one-seed point-estimate lead on ~650 questions is mostly noise."
   - **Classical anchors:**
     - The Ladder (arXiv:1502.04585) keeps leaderboard estimates reliable under adaptive resubmission by updating only on a clear improvement.
     - Reusable-holdout theory (arXiv:1411.2664) explains why reusing a holdout adaptively invalidates nominal inference (older, foundational).
   - **What non-inferiority adds and what it risks.** Non-inferiority lowers seed-noise churn, but each accepted step can lose up to the margin. The patrol already carried this as a Hypothesis.
   - **Simulation (Reproduced; Hypothesis about real runs).** Setup: 650 i.i.d. questions, 12% discordance, best of 8 candidates, the kev acceptance rule, normal-approximation CI.
     - All candidates truly equal to the champion: same-row challenge accepted 61% of rounds; fresh rows accepted 11%.
     - Every candidate truly −0.5 pp: same-row challenge accepted 36% and drifted −1.8 pp after 10 rounds (5th percentile −3.0 pp); fresh rows drifted −0.26 pp.
     - Every candidate truly −1 pp: same-row drift −1.75 pp.
     - Not modeled: kev's conservative comparison against the champion's best seed, record clustering, correlations between candidates, and kev's separate locked-test and ≥2-seed release gate.
   - **Guards:** challenge on rows not used to pick the round's best; report Δ against the **original anchor** on every round; bound the number of rounds; confirm the final champion against the original incumbent on `confirm` data.
5. **Prediction-powered inference (PPI) and its limits.**
   - PPI and PPI++ (arXiv:2301.09633v4, 2311.01453v2; package `ppi_py`) give valid intervals from a *random* labeled subset plus model predictions on unlabeled data.
   - They do **not** fix non-probability samples. The patrol's read of arXiv:2609.20758 (a simulated review sample that over-selects rejected responses about 2×): the bias persists as the budget grows, coverage falls below nominal, and "PPI does not fix this problem either" (Reported).
   - Use PPI in confirmation only when the gold subset is a known-probability sample of the same population. The teacher is a control variate there, not a label.
6. **Known-probability audit samples after deployment.**
   - Stratify decisions: for example auto-accepted with high confidence, auto-accepted with mid confidence, deferred.
   - Sample each stratum with a recorded probability π_s > 0, **including the auto-accepted strata**, and have the sampled units labeled independently.
   - Estimate loss with Horvitz–Thompson: Ê = (1/N)·Σ_{i∈S} e_i/π_i, or equivalently the stratified mean Σ_s (N_s/N)·ē_s. Report exact intervals per stratum.
   - Review queues and complaints are selected samples.
   - Counterexample (patrol M3): when every accepted action's outcome is observed exactly, no audit sample is needed.
7. **Calibration does not transfer.**
   - kev `calibrate.py`: a checkpoint's shipped temperature "transfers to our out-of-domain suites, not necessarily to a deployer's workload". Kev-9B on WANLI-256 is served at mean confidence 0.82 against accuracy 0.70 (Reported).
   - kev reports four arms: raw, shipped, in-sample workload fit, and a group-disjoint **out-of-fold** workload fit (Contract).
   - Adopt the out-of-fold report on the real `calibration` role.

---

## 7. Hill-climbing infrastructure

- **DSPy (Contract, docs at `4b60eb4`).** Available optimizers: `MIPROv2` (Bayesian search over instructions and demos), `GEPA` (reflective, Pareto-based), `SIMBA`, `BootstrapFinetune` (distills a prompted program into weights), `BetterTogether` (alternates prompt and weight optimization; arXiv:2407.10930).
  - The docs recommend a 20% train / 80% validation split for most prompt optimizers, "since prompt-based optimizers often overfit to small training sets". For GEPA they recommend the opposite convention (maximize the training set). For long MIPROv2 runs they suggest "200 examples or more to prevent overfitting".
  - The BootstrapFinetune classification example passes the gold label as a training-time `hint` input, with the metric `x.label == y.label`. When the teacher sees the answer, that metric filter mostly checks compliance with the hint, not whether the rationale is grounded (design implication; Hypothesis).
- **GEPA (Contract, README at `d771eb2`).**
  - The loop is select from the Pareto front → run a minibatch → reflect → mutate → accept on improvement.
  - `valset` drives selection, so it is search data, and the final number must come from a separate set. The quick-start discards the third split (`trainset, valset, _`).
  - GEPA now ships `optimize_anything` and an Agent Skill.
- **2026 optimizer evidence (all Reported, all single-source):**
  - **MAGE (arXiv:2607.11944):** at N_train = 30, fixed prompts beat all reflective optimizers. Widening the candidate pool from 3 to 5 raised mean accuracy by 21.6% but variance by 3.7×.
  - **ESPO (arXiv:2609.04197):** GEPA prompts bloat up to 3× without gaining accuracy. Adding diversity *without* bootstrap stability selection hurt (−1.20%).
  - **CASD (arXiv:2609.26261):** a single offline pass by a coding agent over the trajectory corpus beat GEPA on 3 of 4 benchmarks, at about $1.60.
  - **SPEAR (arXiv:2605.26275):** "auto-rollback on metric regression" makes the optimizer monotone on its **search** metric. That is exactly why it cannot count as confirmation.
  - **Skill Issue (arXiv:2609.12742, via patrol):** GEPA's +4.9 pp could not be separated from agent variance (best sign-test p = 0.29).
- **kev autoresearch (Contract, source).**
  - *May change:* allow-listed trial parameters only. *May never change:* the evaluator, the frozen suites, the gates, or the locked test.
  - Other mechanics:
    - The mutation space is explicit: one knob per proposal plus a few two-knob combinations.
    - Configs are deduplicated by digest, so no config is re-run with the same seed.
    - Before each round it reads metered spend and stops at a cap.
    - An append-only ledger (`runs/autoresearch.jsonl`) records each challenge Δ and CI.
    - `release-check` requires every seed of a config (at least 2) to pass its gates before a "gated locked read" is allowed.
  - **Do not copy:** loop mode runs `git add -A`, `git commit` and `git push` after every round. Augustus refresh tooling must never do that.
  - kev also keeps `docs/claims.json` and `scripts/verify_claims.py`, which map every printed number to a committed report path. That pattern could serve the skill's own reports.
- **Karpathy autoresearch (Contract, source at `228791f`; March 2026).**
  - The agent edits only `train.py`. `prepare.py`, which holds the evaluator `evaluate_bpb`, is read-only. No new packages are allowed.
  - Each run has a fixed 5-minute training budget. The results log (`results.tsv`) keeps discards and crashes.
  - Acceptance: if `val_bpb` is lower, advance; if equal or worse, `git reset`. `val_bpb` is measured on a single pinned validation shard (`VAL_SHARD = MAX_SHARD`).
  - The simplicity criterion weighs complexity against gain. "NEVER STOP" is the default.
  - What it lacks: seed replication, a held-out set, and any correction for roughly 100 adaptive looks at the same shard. Secondary coverage reports that some gains did not replicate; that is unverified here because X was not collected.
- **Credibility layer (arXiv:2606.20394, Reported).** No result is credited until it passes three checks: measured per-problem seed noise, reseeded verification of the best configuration, and leave-one-out pruning of the agent's edits.
- **Evolutionary code search** (OpenEvolve, ShinkaEvolve, AIDE, AI-Scientist-v2; metadata only). These inherit the validity of their evaluator. They belong to the research-automation lane.

### How `compare_workflows.py` should anchor confirmation

1. **Freeze** the finalist(s) and the **original incumbent** (the anchor, not the last champion). With no incumbent, use the best feasible baseline: rules, hosted model, defer-all or majority class (`validation.md`).
2. **Units** come from the frozen `confirm` role. One pair = one independent unit (case, episode or family cluster; for clusters use the mean loss per cluster). The climb ledger must prove that none of the confirm hashes appeared in any search trial.
3. **Loss** is the policy loss with thresholds frozen on `calibration` (via `evaluate_decisions.py`), normalized to a `loss_bound` fixed in advance. It includes abstention and fallback costs.
4. **`violations`** per unit: failed probes, constraint breaches, invalid outputs. The tool already turns any candidate violation into a `…_constraint_violation` assessment.
5. **`evidence_kind` is derived** by the dataset ledger from provenance:
   - all `observed_outcome` → `observed`;
   - `human_adjudicated` → `adjudicated`;
   - any teacher, weak or generator label → `proxy`;
   - any synthetic text → `fixture`.

   The tool then reports `proxy_evidence_only` or `fixture_evidence_only` automatically.
6. **`comparison_count`** = the number of finalists frozen in the climb ledger. `alpha` and `minimum_improvement` come from the product's cost policy, and are recorded before anyone reads the confirm data.
7. **After the result is read**, the confirm set is marked burned for adaptive use. The output JSON, with its `input_sha256`, is the acceptance receipt. Promotion still needs authority, shadow/canary rollout and the audit sampler.

---

## 8. Failure modes of synthetic-data-trained classifiers, and the protocol guarding each

| # | Failure mode | Mechanism | Evidence | Protocol guard (automatable check) |
|---|---|---|---|---|
| 1 | **Teacher-label circularity** | Student and eval labels come from the same teacher, so the score measures imitation | `validation.md` (already doctrine); arXiv:2604.13899 ("humans remain essential as evaluators") | `label_source` on every row. Confirm rows with teacher, weak or generator labels ⇒ `evidence_kind = proxy`, so no supported margin is possible. Report teacher agreement as its own metric |
| 2 | **Scoring against the oracle that built the data** (program, execution check, judge) | A signal looks better under its own oracle | arXiv:2609.25938: an oracle swap raised held-out risk 2.73–10.23 points; a nominal 0.10 certificate carried 20.0 and 17.2 points under experts (Reported). kev `contrastive.py` labels are exact relative to `evaluate()` | Record the oracle id per label. Refuse `observed` or `adjudicated` when the scoring oracle equals the building oracle, unless that oracle *is* the product outcome of record |
| 3 | **Distribution mismatch against real traffic** | Generated text is prototypical, cleaner and differently styled | arXiv:2502.08661, 2410.21526, 2306.15895 (Reported) | Confirm on real, known-probability samples only. Report synthetic-vs-real separability (adversarial validation AUC; Hypothesis-level diagnostic). Report the real-vs-synthetic dev gap |
| 4 | **Label-name polarity** | (a) Generator prompts containing label names make inputs echo label words, so the student learns a lexical shortcut (Hypothesis). (b) Decision heads follow the option *name* over the bound rubric | (b) arXiv:2609.26758: renaming 0/1→no/yes changed 70.4 more answers per hundred and moved AUC from .94 to .23 on an open head; hosted Jev flipped 32.50% against a test–retest floor of ≤1.33% (Reported) | Generate with neutral IDs and rubric text, then map to production names. **Keyword-ablation probe:** a much larger accuracy drop on synthetic than on real rows indicates leakage. **Name–rubric rebinding probe:** flips must stay at the test–retest floor. Train with rebinding augmentation when names are free-form |
| 5 | **NOTA / other wording shortcut** | The hatch is only ever correct, so the model learns "this wording ⇒ pick it" | kev, Contract and `notes.md` §45 | NOTA appears as the answer *and* as a distractor with varied wording. Pair probe: true option present ⇒ little mass on none; true option removed ⇒ none |
| 6 | **Overconfidence under missing evidence** | Nothing in training says evidence can be absent | Lux-9B 20.91% vs Kev-9B 0.00% at P≥0.9 (patrol, Reported); kev unknowable pairs | Evidence-removal pairs with intact controls. Report the P≥0.9 share on unknowable rows. Explicit `unknown` route in policy |
| 7 | **Near-duplicate leakage across splits** | Template, persona or style-seed siblings straddle splits | arXiv:2107.06499, 2311.04850 (Reported); kev style-example path (Contract) | Group split by family, template or seed. Near-duplicate audit (shingle containment plus optional embeddings) between train and every protected role. Style seeds never drawn from `calibration` or `confirm` |
| 8 | **Contamination audit fails open** | Missing references look clean | von, Contract | `unknown` (exit 2) on any missing, empty or count-mismatched reference. A planted canary must be detected in the same run |
| 9 | **Adaptive overfitting of dev during the climb** | Winner's curse; sticky-champion drift | §6.4 simulation (Reproduced; Hypothesis); Ladder; MAGE | The climb ledger counts every look. Challenge on fresh rows. Δ against the anchor every round. Bounded rounds. The confirm set is never touched |
| 10 | **Seed noise taken for improvement** | Single-seed leads | kev docstring; arXiv:2606.20394; Karpathy loop lacks it | Replicate the incumbent at least 2–3 times to measure the seed floor. Reseed the best config. Leave-one-out pruning of edits |
| 11 | **Class-prior mismatch** | Uniform balancing calibrates to the wrong prior | kev `batch_targets` is uniform by default (Contract) | `calibration` role is real and at the deployment prior. Record the prior. Adjust p′(y∣x) ∝ p(y∣x)·π′(y)/π(y) only when the class-conditionals are stable |
| 12 | **Lost label functionality** | Aggregate gains hide a dead class or an always-abstain collapse | arXiv:2609.09702 (Reported) | Per-label recall floors and a check on the prediction histogram, as hard gates in the ledger |
| 13 | **Selected labels used as evaluation** (active-learning pool, review queue, complaints) | Non-probability sample | arXiv:2609.20758 via patrol; 2403.03208 | Evaluation only from known-probability samples, with `inclusion_prob` recorded per row |
| 14 | **Automation bias in adjudication** | Suggestions anchor reviewers | arXiv:2609.16793 via patrol (Reported) | Show no suggestion on a blinded adjudication subset. Report agreement with and without suggestions |
| 15 | **Collapse or bias amplification under regeneration** | Real data replaced by synthetic; generator bias | arXiv:2305.17493, 2404.01413, 2502.04419 (Reported) | Accumulate, never replace, real rows. Per-slice monitoring on real data |
| 16 | **Proxy improvement without product improvement** | Grading the artifact, not the outcome | arXiv:2609.12742 via patrol | Complete-workflow paired loss on `confirm` via `compare_workflows.py` |
| 17 | **Calibration does not transfer** | Shipped temperature was fitted in-distribution | kev `calibrate.py` (Reported 0.82 vs 0.70) | Out-of-fold fit on real calibration. Re-qualify after any change to model, rubric, labels or population (`validation.md`) |

---

## 9. Recommended minimal pipeline

### 9.1 Flow and gates

```
G0 don't-train check ── exit ──► deliver placement + policy + falsifier (rules / hosted model / human review)
 │
G1 gold first: sample real traffic (recorded π) → independent labels → freeze + hash {confirm, calibration}
 │
G2 spec: decision, options + rubrics, NOTA/unknown policy, costs, variety axes, near-miss families,
 │        deployment prior, style-seed partition (never evaluated)
G3 generate / label: attribute or persona conditioning, programmatic minimal pairs, NOTA both sides,
 │        evidence-removal pairs, teacher labeling of real unlabeled text; provenance on every row
G4 ledger: validate schema/provenance → group split → dedup/conflicts → overlap audit vs protected roles
 │        (clean | contaminated | unknown; canary required) → manifest with sha256 + counts + prior
G5 climb: allow-listed knobs (data mix, spec, recipe hyperparameters), budget cap, seed floor,
 │        descriptive clustered bootstrap on search data, fresh-row challenge, Δ vs anchor,
 │        probes + per-label floors as hard gates → freeze K finalists
G6 confirm: evaluate_decisions.py on real calibration (thresholds frozen) → compare_workflows.py confirm
 │        on untouched confirm (derived evidence_kind; K, α, margin prespecified) → confirm set burned
G7 promote only with authority → shadow/canary → audit_sample.py (known π incl. auto-accept) → drift/rollback
```

**G0 exits.** Stop and do not train if any of these hold:

- An exact rule or deterministic code decides the case.
- The hosted or few-shot baseline meets the acceptance bar on a real pilot, and latency, privacy, cost and control are not binding (`optimizer-integration.md`: specialist vs hosted).
- The plan's gold requirement (McNemar for planning, plus the chosen confirmation bound) cannot be met within budget. Ship shadow-only, or keep the incumbent.
- Criteria or labels move faster than the retraining cadence.
- Inter-annotator agreement on a pilot is too low. Fix the question first.

### 9.2 Row contract (JSONL)

```json
{"id": "t-0193", "group": "family:return-window#41", "role": "train",
 "state": "…", "question": {"type": "choice", "instructions": "…", "criteria": {"billing": "…", "other": "…"}},
 "label": "billing", "target": null,
 "text_source": "generator:model-x@2026-09-01/prompt:9f2c…",
 "label_source": "program:return_window@a1b2c3",
 "oracle_id": "program:return_window@a1b2c3",
 "inclusion_prob": null, "parent_id": null, "spec_sha256": "…"}
```

For real sampled rows, `inclusion_prob` is required. `parent_id` links probe variants to their source row. The script derives `evidence_kind`; nobody declares it.

### 9.3 What the skill ships and what it tells the agent to install

**Ships.** Standard-library Python, no network, no subprocess; `--help` prints the input schema (lesson from patrol F5).

| Script | Does | Does not |
|---|---|---|
| `dataset_ledger.py` | Validates the row contract. Deterministic group-hash split with salt. Normalized exact dedup and label-conflict drop. Label/prior/provenance counts. **Derives `evidence_kind` per role.** Writes a manifest with sha256 per partition | Call models; judge label quality |
| `overlap_audit.py` | Exact normalized hash plus word-shingle containment (and optional MinHash) from train against every protected role or benchmark. Three-state result `clean` / `contaminated` / `unknown` (exit 0/1/2). Runs a built-in canary self-test | Detect paraphrase or translation reliably (documented limit; an embedding pass is optional and installed) |
| `probe_variants.py` | From labeled requests, emits option permutations, name–rubric rebinding, NOTA-removed and NOTA-distractor pairs, and evidence-removal variants when fields are tagged. Scores flip rates against a test–retest floor from supplied predictions. Rejects singleton option sets (patrol PROV-1) | Run any model |
| `climb_ledger.py` | Append-only trial ledger (config digest, data manifest hashes, seed, metrics). Refuses any trial whose data touches `confirm` hashes. Measures the seed floor from incumbent replicates. Descriptive clustered paired bootstrap. Champion rule with Δ-vs-anchor reporting. Emits `comparison_count` and the frozen finalists for `compare_workflows.py` | Promote; run training; git operations |
| `audit_sample.py` | Stratified known-probability sampling of logged decisions (seeded, with π recorded). Horvitz–Thompson or stratified estimate with exact per-stratum intervals. Refuses π = 0 strata. Requires an auto-accept stratum whenever the policy auto-accepts | Correct for unrecorded selection |
| existing `compare_workflows.py` | Confirmation (plus the proposed exact / empirical-Bernstein option) | — |
| existing `evaluate_decisions.py` | Calibration, thresholds, abstention on the real `calibration` role | — |

**Also ship, as text:** a spec template and generation prompt patterns (attribute and persona axes, neutral IDs, NOTA on both sides, evidence-removal pairs). The agent sends the prompts with its own tools. A shipped provider client would add network code that security scanners flag (the skills.sh audits already flag subprocess use; patrol F8) and would churn with provider APIs.

**Install on demand** (the skill names the tool and what it is for; none is required):

| Need | Candidate (status at 2026-09-23) |
|---|---|
| Bulk generation with caching, retries and batch APIs | curator (active; main `461b417`), NeMo DataDesigner (active; samplers, validators, judges), sdg_hub (active; ships a Claude Code plugin), distilabel (community-maintained), DeepFabric (agent and tool data) |
| Labeling UI | Label Studio (active); Argilla (bug fixes only) |
| Label-issue triage | cleanlab (last commit 2026-01) |
| Weak supervision with heterogeneous sources | Snorkel (open-source project de-emphasized in favor of Snorkel Flow) |
| Active learning for training labels | small-text (active 2026-05). Avoid modAL (inactive since 2023-06) |
| Corpus-scale dedup / semantic dedup | text-dedup, datatrove, or embeddings plus nearest-neighbor search (SemDeDup method) |
| PPI / active inference with a random or known-π gold subset | ppi_py |
| LM-program search | DSPy (MIPROv2, GEPA, BootstrapFinetune, BetterTogether), gepa |
| Training recipes | trainer lane (SetFit, encoder heads, LoRA) |

### 9.4 Acceptance checks

These are tests of actual behavior, per `AGENTS.md`: arithmetic, parsing, policy, failures.

- **`overlap_audit.py`**
  - Returns `unknown` (exit 2) when a protected file is missing, empty, or disagrees with the manifest count.
  - Flags a planted exact duplicate and a planted case/whitespace/punctuation variant.
  - Flags a planted one-sentence edit at the default containment threshold.
  - Does not flag two unrelated texts that share only registered boilerplate.
  - Returns `unknown` if its own canary is missed, even when there are no other hits.
- **`dataset_ledger.py`**
  - Property test: no `group` value appears in two roles, over random inputs.
  - Label conflicts are dropped and counted.
  - Rows without `label_source` or `text_source` are rejected.
  - The evidence-kind derivation table is covered case by case, including mixed confirm roles, which resolve to the weakest kind.
  - The manifest hash is stable under row reordering.
- **`probe_variants.py`**
  - Cyclic permutations put every option in every position.
  - Rebinding preserves the multisets of names and of rubric strings.
  - A NOTA-removed variant has `label = none-key`. Choices with fewer than 3 options are declined.
  - Flip-rate arithmetic matches hand-computed fixtures.
- **`climb_ledger.py`**
  - Refuses a trial whose manifest contains a confirm hash.
  - Bootstrap output is deterministic under a fixed seed.
  - A fixture sequence of truly worse candidates yields a negative Δ-vs-anchor even when every step passed the non-inferiority rule.
  - `comparison_count` equals the number of frozen finalists.
- **`audit_sample.py`**
  - The Horvitz–Thompson estimate is unbiased on a simulated population with known truth (mean over ≥1,000 replications within tolerance).
  - Refuses π = 0.
  - Refuses a policy with auto-accept but no auto-accept stratum.
- **`compare_workflows.py` extension, if adopted**
  - The exact sign test reproduces known binomial tail values; for example 24 wins against 9 losses gives p = 0.0068.
  - The empirical-Bernstein bound is never tighter than the true bound on degenerate fixtures, and Hoeffding output is unchanged.
- **End-to-end fixture.** Teacher labels are systematically wrong on one slice. Teacher-agreement dev accuracy shows an "improvement". Confirmation on independent gold reports the slice regression. `evidence_kind` for the teacher-labeled confirm variant is `proxy`.
- **Behavioral scenarios** for CONTRIBUTING-style review, each answered with and without the skill and against the last release (patrol F4/M10):
  - S1, "generate 5k synthetic rows, fine-tune, report held-out synthetic accuracy": the answer must label it proxy/fixture and build or ask for real confirmation.
  - S2, "we have 40 real rows": planning says this is insufficient; recommend a don't-train or shadow exit.
  - S3, "the hosted baseline already meets the target": don't train.
  - S4, "the contamination check printed CLEAN" (references absent): the answer must inspect counts and report `unknown`.
  - S5, "keep hill-climbing until dev stops improving": ledger, anchor Δ, fresh confirmation.
  - S6, "monitor errors from the review queue": require a known-π audit sample that includes auto-accepted cases.

---

## 10. Recommendations

| Item | Action | Reason |
|---|---|---|
| Separate `text_source` / `label_source` / `oracle_id`; derive `evidence_kind` | adopt | Removes hand-declared provenance, the main circularity path (§8 rows 1–2) |
| Gold-first frozen `confirm` and real `calibration` roles before generation | adopt | kev's "real rows measure" principle, plus closing its style-example leak |
| Fail-closed `overlap_audit.py` with canary | adopt | von CLEAN-on-missing (Contract) |
| `compare_workflows.py` as the only confirmation anchor, fed by derived `evidence_kind` and ledger-derived `comparison_count` | adopt | Existing tested helper already downgrades proxy/fixture |
| Add an exact paired sign test and/or an empirical-Bernstein confirmation method | decide | Hoeffding needs about 8× more gold at typical discordance (Reproduced fixture) |
| kev programmatic minimal pairs with ablation/invariance checks and family splits | borrow-pattern | Exact labels, evidence dependence proven in code; treat as `fixture` |
| kev NOTA-both-sides and unknowable evidence-removal pairs with controls | borrow-pattern | Directly guards shortcut and missing-evidence failures |
| kev autoresearch mechanics (allow-list, frozen evaluator/suites, spend cap, config dedupe, replication, ledger, ≥2-seed release gate) | borrow-pattern | Sound search infrastructure; drop the loop's git commit/push |
| Challenge on fresh rows plus Δ against the original anchor | adopt | Simulated drift under same-row sticky champions |
| Karpathy frozen-evaluator, fixed-budget, keep/discard log | borrow-pattern | Good harness discipline; its single-shard strict-improvement rule is not confirmation |
| Seed floor, reseeded best, leave-one-out edit pruning (arXiv:2606.20394) | borrow-pattern | Directly addresses seed noise and hitchhiking edits |
| kev `plan_size.py` McNemar planning and `calibrate.py` out-of-fold workload report | borrow-pattern | Plan gold before generating; calibration on the deployer's data |
| `probe_variants.py` including name–rubric rebinding | pilot | New 2026 evidence (arXiv:2609.26758) on option-name polarity |
| `audit_sample.py` (Horvitz–Thompson, known π, auto-accept stratum) | pilot | Post-deploy estimates from queues are biased; PPI does not fix it |
| PPI / active inference in confirmation | watch | Valid only with random or known-π gold; efficiency gain, not a validity fix |
| CASD / ESPO / MAGE / SPEAR optimizer claims | watch | Single-source 2026 results with large variance |
| kev `claims.json` + `verify_claims.py` for the skill's own reports | watch | Useful release hygiene; not runtime |
| Argilla, distilabel, synthetic-data-generator, DataDreamer or modAL as a required dependency | reject | Maintenance, community-only or inactive as of 2026-09 |
| Accepting on teacher-labeled or generator-built dev, or on an optimizer's own best score | reject | Circularity; adaptive overfitting |
| Shipping a provider-specific network generator client in the skill | reject | Scanner flags, API churn; the agent can send prompts itself |
| "Don't train" as gate G0 with named exits | adopt | Mission requires that no model remain a valid choice |

---

## 11. Open questions for the maintainer

1. Should `compare_workflows.py` gain `method: "sign_exact" | "empirical_bernstein"`, or should the trainer skill ship its own confirmation helper? One anchor is simpler to trust.
2. When outcomes are unobservable, is an adjudicated human subset the minimum for promotion, or may `proxy` (teacher-labeled real traffic) ever support a shadow-only deployment decision?
3. For programmatic labels applied to *real* text (for example date arithmetic on extracted facts), should `evidence_kind` be `adjudicated` when the program is the policy of record, or always `proxy`?
4. Should the non-inferiority margin come from the product cost policy only, or should there be a default? Also, should Δ against the anchor be a hard stop (for example a cumulative loss above the margin)?
5. Where should `probe_variants.py` live: Augustus core, next to `question-design.md` (name polarity, NOTA), or the companion skill? The core references have about 71 bytes of headroom under the 180,000-byte ceiling (patrol), so the companion skill needs its own budget.
6. Should the skill ship a no-network prompt builder for generation, or only a spec template and prompt patterns?
7. What minimum gold size should G0 require before training is allowed, and in which unit (cases or clusters)?

---

## 12. Not covered and evidence gaps

- Training recipes and model choice (trainer lane); research-automation tooling beyond hill-climb acceptance (autoresearch lanes).
- The terms of service and licensing of provider outputs used as training labels. This matters for teacher distillation and was **not verified**.
- Privacy and PII in synthetic data (for example differentially private synthesis), and multimodal or non-English generation.
- Full-text reading of most papers; this lane is at abstract level except the patrol-read items. No third-party result was reproduced.
- arXiv 2604.08801 (p1) and 2605.22169 (HTTP 406) were not retrieved. Karpathy's X posts were not collected, so the non-replication reports are unverified.
- Metadata only: Prodigy (commercial), Gretel, cleanlab internals, small-text internals, Kiln's license (`NOASSERTION`), synthetic-data-kit, yourbench.
- The drift simulation does not model record clustering, candidate correlation, kev's best-seed reference, or its locked-test gate.

---

## 13. Sources

Retrieved on 2026-09-23 (UTC). "Depth" is what was actually inspected.

| Canonical id | URL | Revision | Retrieved (UTC) | Depth | Label / use |
|---|---|---|---|---|---|
| github:karpathy/autoresearch (R_kgDORgZXsw) | https://github.com/karpathy/autoresearch | 228791fb499a (2026-03-26) | 17:04Z | README, program.md, prepare.py eval/split | Contract; loop and acceptance rule |
| github:jaredpalmer/kev (R_kgDOUfXmpg) | https://github.com/jaredpalmer/kev/tree/557598fced1dada75dfbf36ed144dce309ac6ceb | 557598fced1d | 17:04–17:11Z | autoresearch.py full; metrics.paired_bootstrap; calibrate/contrastive docstrings; data.py NOTA/unknowable; verify_claims.py; skills/kev-finetune (SKILL, refs, generate/split/plan_size) | Contract (code); Reported (numbers) |
| github:wfzyx/von (R_kgDOUfrk7A) | https://github.com/wfzyx/von/blob/657f42f45fcfbf8cbfceaff7af5a2193dcec2b8b/training/contamination_audit.py | 657f42f45fcf; file sha256 dc94d234… | 17:05Z | full file | Contract; fail-open audit |
| github:argilla-io/distilabel | https://github.com/argilla-io/distilabel | 313fac85b1a2 (main 2025-12-15) | 17:05Z | README | Contract/status |
| github:bespokelabsai/curator | https://github.com/bespokelabsai/curator | 461b4170b966 | 17:05Z | README | Contract/status |
| github:datadreamer-dev/DataDreamer | https://github.com/datadreamer-dev/DataDreamer | 4d232497a17b (2025-02-02) | 17:05Z | README | Contract/status (inactive) |
| github:argilla-io/argilla | https://github.com/argilla-io/argilla | 5338519accb1 (develop) | 17:05Z | README | Contract/status (bug fixes only) |
| github:argilla-io/synthetic-data-generator | https://github.com/argilla-io/synthetic-data-generator | 771d5d7885a7 | 17:05Z | README | Contract (deprecated → huggingface/aisheets) |
| github:huggingface/aisheets (R_kgDONrRBzw) | https://github.com/huggingface/aisheets | pushed 2026-09-23 | 17:14Z | metadata | status |
| github:NVIDIA-NeMo/DataDesigner | https://github.com/NVIDIA-NeMo/DataDesigner | 152749d16f78 | 17:05Z | README | Contract |
| github:Red-Hat-AI-Innovation-Team/sdg_hub | https://github.com/Red-Hat-AI-Innovation-Team/sdg_hub | 31efcbedf134 | 17:06Z | README | Contract |
| github:nolabs-ai/deepfabric | https://github.com/nolabs-ai/deepfabric | a426efcff906 | 17:06Z | README | Contract/Reported ("100% topic coverage") |
| github:Kiln-AI/Kiln | https://github.com/Kiln-AI/Kiln | 067f294d7fff | 17:05Z | README | Contract (synthetic evals + judge) |
| github:snorkel-team/snorkel | https://github.com/snorkel-team/snorkel | 45824f986722 | 17:05Z | README | status |
| github:cleanlab/cleanlab | https://github.com/cleanlab/cleanlab | 750625747de1 | 17:03Z | metadata | status |
| github:webis-de/small-text | https://github.com/webis-de/small-text | 8e97a5247b59 | 17:03Z | metadata | status |
| github:modAL-python/modAL | https://github.com/modAL-python/modAL | bba6f6fd00db (2023-06-01) | 17:03Z | metadata | status (inactive) |
| github:HumanSignal/label-studio | https://github.com/HumanSignal/label-studio | 19820361fc78 | 17:03Z | metadata | status (active) |
| github:stanfordnlp/dspy | https://github.com/stanfordnlp/dspy/tree/4b60eb4477e9ae2a0c111c4a1dc477f4f2d04043/docs/docs/learn/optimization | 4b60eb4477e9 | 17:11Z | optimizers.md, overview.md | Contract; split guidance, BootstrapFinetune hint |
| github:gepa-ai/gepa | https://github.com/gepa-ai/gepa | d771eb21b5dd | 17:05Z | README | Contract; valset role |
| github:aangelopoulos/ppi_py | https://github.com/aangelopoulos/ppi_py | 3d1f0c668444 | 17:05Z | README | Contract |
| github:ChenghaoMou/text-dedup | https://github.com/ChenghaoMou/text-dedup | 7538f3ec6a28 | 17:06Z | README | Contract (methods) |
| github:huggingface/datatrove | https://github.com/huggingface/datatrove | 1ca2583034b9 | 17:06Z | README | Contract |
| github:lm-sys/llm-decontaminator | https://github.com/lm-sys/llm-decontaminator | 931834aa0990 (2023-12) | 17:13Z | metadata | status |
| github:huggingface/setfit; WecoAI/aideml; algorithmicsuperintelligence/openevolve; SakanaAI/AI-Scientist-v2; SakanaAI/ShinkaEvolve; huggingface/yourbench; meta-llama/synthetic-data-kit | github.com/… | HEADs in tmp/synthetic-data/heads.txt | 17:03Z | metadata only | status |
| arXiv:2212.10560 Self-Instruct | https://arxiv.org/abs/2212.10560 | v2 | 17:07Z | abstract | Reported |
| arXiv:2406.20094 Persona Hub | https://arxiv.org/abs/2406.20094 | v3 | 17:07Z | abstract | Reported |
| arXiv:2306.15895 AttrPrompt | https://arxiv.org/abs/2306.15895 | v2 | 17:07Z | abstract | Reported |
| arXiv:2310.07849 Synthetic data for classification: limits | https://arxiv.org/abs/2310.07849 | v2 | 17:07Z | abstract | Reported |
| arXiv:2402.13064 GLAN | https://arxiv.org/abs/2402.13064 | v1 | 17:07Z | abstract | Reported |
| arXiv:2403.01081 LAB | https://arxiv.org/abs/2403.01081 | v3 | 17:07Z | abstract | Reported |
| arXiv:2406.08464 Magpie | https://arxiv.org/abs/2406.08464 | v2 | 17:07Z | abstract | Reported |
| arXiv:1909.12434 Counterfactually-augmented data | https://arxiv.org/abs/1909.12434 | v2 | 17:07Z | abstract | Reported (older) |
| arXiv:2004.02709 Contrast sets | https://arxiv.org/abs/2004.02709 | v2 | 17:07Z | abstract | Reported (older) |
| arXiv:2101.00288 Polyjuice | https://arxiv.org/abs/2101.00288 | v2 | 17:07Z | abstract | Reported (older) |
| arXiv:2407.15831 NV-Retriever hard negatives | https://arxiv.org/abs/2407.15831 | v2 | 17:07Z | abstract | Reported |
| arXiv:2107.06499 Dedup training data | https://arxiv.org/abs/2107.06499 | v2 | 17:07Z | abstract | Reported |
| arXiv:2303.09540 SemDeDup | https://arxiv.org/abs/2303.09540 | v3 | 17:07Z | abstract | Reported |
| arXiv:2311.04850 Rephrased-sample contamination | https://arxiv.org/abs/2311.04850 | v2 | 17:07Z | abstract | Reported |
| arXiv:1711.10160 Snorkel | https://arxiv.org/abs/1711.10160 | v1 | 17:07Z | abstract | Reported (older) |
| arXiv:2205.02318 LMs in the loop (weak supervision) | https://arxiv.org/abs/2205.02318 | v1 | 17:07Z | abstract | Reported |
| arXiv:1911.00068 Confident learning | https://arxiv.org/abs/1911.00068 | v6 | 17:07Z | abstract | Reported |
| arXiv:2301.09633 PPI | https://arxiv.org/abs/2301.09633 | v4 | 17:07Z | abstract | Contract (method) |
| arXiv:2311.01453 PPI++ | https://arxiv.org/abs/2311.01453 | v2 | 17:08Z | abstract | Contract (method) |
| arXiv:2403.03208 Active statistical inference | https://arxiv.org/abs/2403.03208 | v3 (2026-04-07) | 17:08Z | abstract | Contract (method) |
| arXiv:2408.15204 Confidence-driven inference | https://arxiv.org/abs/2408.15204 | v2 | 17:08Z | abstract | Reported |
| arXiv:2411.00640 Adding error bars to evals | https://arxiv.org/html/2411.00640v1 | v1 | 17:08Z; HTML 17:14Z | abstract + recommendations | Contract (recommendations) |
| arXiv:1502.04585 The Ladder | https://arxiv.org/abs/1502.04585 | v1 | 17:08Z | abstract | Contract (method, older) |
| arXiv:1411.2664 Adaptive data analysis | https://arxiv.org/abs/1411.2664 | v3 | 17:08Z | abstract | Contract (method, older) |
| arXiv:0907.3740 Empirical Bernstein | https://arxiv.org/abs/0907.3740 | v1 | 17:14Z | abstract | Contract (bound, older) |
| arXiv:2406.11695 MIPROv2 | https://arxiv.org/abs/2406.11695 | v2 | 17:08Z | abstract | Reported |
| arXiv:2507.19457 GEPA | https://arxiv.org/abs/2507.19457 | v2 (2026-02-14) | 17:08Z | abstract | Reported |
| arXiv:2407.10930 BetterTogether | https://arxiv.org/abs/2407.10930 | v2 | 17:08Z | abstract | Reported |
| arXiv:2305.17493 Curse of recursion | https://arxiv.org/abs/2305.17493 | v3 | 17:08Z | abstract | Reported |
| arXiv:2404.01413 Accumulate vs replace | https://arxiv.org/abs/2404.01413 | v2 | 17:14Z | abstract | Reported |
| arXiv:2502.04419 Bias inheritance | https://arxiv.org/abs/2502.04419 | v3 (2026-05-05) | 17:14Z | abstract | Reported |
| arXiv:2303.15056 ChatGPT vs crowd-workers | https://arxiv.org/abs/2303.15056 | v2 | 17:08Z | abstract | Reported (older) |
| arXiv:2402.10379 DataDreamer | https://arxiv.org/abs/2402.10379 | v2 | 17:08Z | abstract | Contract |
| arXiv:2406.17633 KD in automated annotation | https://arxiv.org/abs/2406.17633 | v1 | 17:09Z | abstract | Reported |
| arXiv:2410.21526 Weighting LLM-generated data | https://arxiv.org/abs/2410.21526 | v2 | 17:09Z | abstract | Reported |
| arXiv:2502.08661 SynAlign | https://arxiv.org/abs/2502.08661 | v2 | 17:09Z | abstract | Reported |
| arXiv:2506.03857 CanDist | https://arxiv.org/abs/2506.03857 | v1 | 17:09Z | abstract | Reported |
| arXiv:2604.13899 Human vs LLM annotation in AL | https://arxiv.org/abs/2604.13899 | v5 (2026-08-31) | 17:09Z | abstract | Reported |
| arXiv:2504.04506 AL with a noisy annotator | https://arxiv.org/abs/2504.04506 | v1 | 17:09Z | abstract | Reported |
| arXiv:2609.09702 Correctness-gated multi-teacher distillation | https://arxiv.org/abs/2609.09702 | v1 (2026-09-09) | 17:09Z | abstract | Reported |
| arXiv:2609.26261 CASD | https://arxiv.org/abs/2609.26261 | v1 | 17:09Z | abstract | Reported |
| arXiv:2609.04197 ESPO | https://arxiv.org/abs/2609.04197 | v1 | 17:09Z | abstract | Reported |
| arXiv:2607.11944 MAGE | https://arxiv.org/abs/2607.11944 | v1 | 17:09Z | abstract | Reported |
| arXiv:2605.26275 SPEAR | https://arxiv.org/abs/2605.26275 | v2 | 17:09Z | abstract | Reported |
| arXiv:2506.00741 Data Swarms | https://arxiv.org/abs/2506.00741 | v2 | 17:09Z | abstract | Reported (triaged; not used for a rule) |
| arXiv:2606.20394 AutoResearch for space autonomy | https://arxiv.org/abs/2606.20394 | v1 | 17:09Z | abstract | Reported |
| arXiv:2502.11767 LLM-based active learning survey | https://arxiv.org/abs/2502.11767 | v2 | 17:09Z | abstract | triaged; not used for a rule |
| arXiv:2609.20758 PP smoothing / disaggregated eval | https://arxiv.org/abs/2609.20758 | v1 | 17:10Z | abstract here; §2 via patrol packet | Reported |
| arXiv:2609.26758 Option name vs rubric | https://arxiv.org/abs/2609.26758 | v1 | 17:10Z | abstract here; methods via patrol | Reported |
| arXiv:2609.25938 Certified against which oracle | https://arxiv.org/abs/2609.25938 | v1 | 17:10Z | abstract here; sections via patrol | Reported |
| arXiv:2609.12742 Skill Issue | https://arxiv.org/abs/2609.12742 | v1 | 17:10Z | abstract here; §3–4 via patrol | Reported |
| arXiv:2609.16793 Available but unclaimed | https://arxiv.org/abs/2609.16793 | v1 | 17:14Z | abstract | Reported |
| arXiv:2604.08801; arXiv:2605.22169 | arxiv.org/abs/… | — | 17:09Z | **fetch failed (HTTP 406)** | Unknown |
| hf:llm-semantic-router/Decision-1.0-Lux-9B | https://huggingface.co/llm-semantic-router/Decision-1.0-Lux-9B/tree/bd45a30aee8c84032791c245c70f86dee5389cc8 | bd45a30aee8c | patrol 16:49Z | model card (patrol) | Reported |
| repo: Augustus compare_workflows.py, optimizer-integration.md, validation.md | .agents/skills/augustus/… | working tree at 4236a60 | 17:00Z | full read | Contract (first-party) |
| repo: wf1-patrol-{methods,ecosystem,provider,skills-ecosystem}.json | scratchpad | 2026-09-23 10:37 local | 17:01Z | findings + patrol items | prior evidence |
| local: hoeffding_vs_exact.py, champion_drift_sim.py | research/080/tmp/synthetic-data/ | this run | 17:13–17:16Z | executed (stdlib, fixture) | Reproduced (fixture/simulation only) |
