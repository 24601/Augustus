# Augustus 0.8.0 plan (v4)

**Public.** The maintainer lifted confidentiality on 2026-09-23 (errata D-c/D-d), so this plan,
its reviews and its research cards live on the `research/080-exopo-trainer` branch. Delegate
reviews send the whole plan to hosted inference providers under their API terms [C, recheck];
that is a deliberate disclosure, recorded here because the plan's own provenance rules demand it
(Fable v3 P2-6). No published tag changes under this plan. Nothing releases without an explicit
maintainer "go".

This version supersedes `plan-v3.md` and folds in `plan-v3-errata.md`, both v3 reviews, the M0
receipt, and the five research cards. Findings are dispositioned in `plan-v4-dispositions.md`.

**Provenance**

| Item | Record |
|---|---|
| Author | Revision lane, 2026-09-24. Requested routing: none stated to this lane. Observed identity recorded in the dispositions |
| Fable v3 review | `reviews/fable-5.1-xhigh-v3.md`. Requested `claude-fable-5-1` at xhigh; observed "Fable 5.1" with `<reasoning_effort>80</reasoning_effort>`. NOT ACCEPTED: 0 P0, 1 P1, 10 P2 |
| Astra v3 review | `reviews/astra-max-v3.md` (session `01a0d0d9…`). Requested `gpt-6-astra` at max; the Codex header reports the same, which is CLI configuration, not proof of the serving model. NOT ACCEPTED: 0 P0, 3 P1, 4 P2 |
| Status | Neither review is acceptance. Acceptance belongs to the maintainer |
| Baseline [Coord] | `origin/main` = `d8dc848`; `v0.7.2` → `30b6033`, released. Released `references/`: 16 files, 173,472 B. Released `SKILL.md`: 10,743 B. M1 re-fetches and records the SHA it actually branches from |
| Host (tabputer-1) | **M0 passed** 2026-09-23: principals, containment, §4.4 GPU acceptance, B1–B15. `receipts/m0-tabputer-1-2026-09-23.md`. Containment code in `infra/`. Access from Amp is the runner `tabputer` (`/mnt/tst`, user `basit`, passwordless sudo) |
| Arithmetic | `calc/calc_v4.py` (stdlib, deterministic; sha256 `4a2d2308…`), output `calc/calc_v4.out.txt` (sha256 `5d7e2644…`). `calc_v3.py` is retained for the superseded normal-theory figures |
| Not used | Third-party runtime code, unreviewed installs, Colab, credentials on tabputer-1 |

**Evidence labels.** [C] contract; [R] reported (third-party); [Rep] reproduced by our own
execution; [H] hypothesis; [U] unknown; [Coord] observed by the coordinator and relayed.

## 0. What changed from v3

1. **One interval carries the error claim.** Astra v3 finding 2 showed that v3's normal-theory
   family CI and its bootstrap fallback both collapse to `[0, 0]` on rare-large bounded losses,
   and then certify equivalence falsely (`0.9999^12850 = 0.2766`; jointly with a 3,000-row pilot
   `0.2049` [Rep]). v4 reads **every** acceptance claim from a two-sided **empirical Bernstein**
   interval for bounded losses at α/(2m) per tail. Its radius floor cannot collapse. Normal-theory
   intervals remain descriptive and carry no error claim (§2.4, §2.7).
2. **Downloads are sequenced in three named windows.** The design lock precedes every
   experiment-dataset download; provisioning downloads (wheels, base image, acceptance weights)
   are not experiment data and are named as such. M2 depends on M0's decisions only
   (Fable v3 P1-1, Astra v3 finding 3; §4.2, §7).
3. **Candidates never see a complete labeled dataset.** Acquisition lands in a quarantine tree,
   splitting runs as `augctl`, and the stage publishes only the partitions a run is entitled to,
   with confirmation **inputs** stripped of labels. B16 is an adversary test that tries to
   reconstruct confirmation labels and must fail (Astra v3 finding 1; §4.2, §4.3).
4. **The ladder is artifact forms, not models.** Exact program → agent-synthesized program →
   compiled function (PAW) → model rungs → generalist, under one acceptance gate, with composed
   decision programs (§3.3). PAW-ft and a synthesized-program arm are tested M5 arms.
5. **GPU for everything** (errata D-b). E4a becomes a vectorized GPU Monte Carlo; the one
   remaining CPU step is the exact-rational `sign_exact` qualification, which is arithmetic, not
   sampling (§2.7 E4a). If the GPU cannot run a job, the fallback is Colab, never CPU.
6. **The host profile is the measured one.** uids 48201/48202, `--memory-swap=16g`,
   `systemd-run --user`, an explicit GPU budget because GTT is not charged to the container
   cgroup, a real MemAvailable watchdog, and vLLM batched throughput of about 2,000 tok/s with
   only 59.8% batched-rerun identity (§4.2, §4.5).
7. **Jev is usable everywhere except as our training data** (errata D-d). Comparator, baseline,
   experiment arm, router, selector and inference-time feature are all allowed. No counsel step.
   In the shipped skill, a Jev-generated training corpus is refused by default with one quoted
   line of MCA §2.3(b), and the user can override it (§3.6).
8. **RAP is required prior art.** Exogenous rule checks are detection, not gating (§2.1).
9. **The sweeps' decision-changing items land**: a multimodal side ladder documented and untested
   by default, mandatory modality blind-arm gates for any media claim, an `input_coverage` field
   in the data protocol and the decision record, and precision parity as a release check
   (§3.3, §3.4, §4.4).
10. **The memory blocker is gone.** MemAvailable was 121,366,040 kB at 18:38 MDT on 2026-09-23
    [Coord]; the large allocation was a stopped vLLM server, not k3s. The envelope rules stand and
    `blocked(memory)` is derived from the launch measurement, never from a stale note
    (Astra v3 finding 7).

## 1. Goals and non-goals

**Goals.**

- **G1. Paper.** A per-action-family test for where an acting agent's decision policy belongs, and
  a protocol for accepting changes to it. At least one executed, pre-registered falsifier (E1),
  reported whatever the result, inconclusive included.
- **G2. Trainer.** `augustus-train`: a gated path from "don't train" to the cheapest **artifact
  form** that meets the workload's own acceptance policy.
- **G3. Tooling.** Confirmation modes and methods; a ledger with a provenance graph; a fail-closed
  overlap audit; a climb ledger; bibliography and claim gates.
- **G4. Design.** A restrained typeset paper, and a project site whose explorables each test one
  claim.

**Non-goals.** Claiming the architecture as novel; selecting recipes by leaderboard rank; training
9–27B generalists; DPO/RLHF by default; autonomous paper writing; a third-party loop runtime;
unattended patrols; GitHub Actions; **Jev output in any training path of ours**.

## 2. Paper

### 2.1 Position

A decision policy outside the weights, with LLMs as instruments, is already published.
Confidence-gated acceptance is classical. The paper claims neither. It contributes the test in
§2.3, an instrument/decision/authority vocabulary, the acceptance protocol in §2.4, and the
executed experiments. Durability is claimed only for commitments (costs, authority, acceptance),
not for scaffolding, which models absorb (2609.03141v1 [R]).

| Work | Already establishes | Leaves open |
|---|---|---|
| Sun, 2604.00414v1 | Signals separated from a deterministic δ(c) = argmax U | Preset thresholds; no acceptance on untouched data; no authority |
| Papamarkou et al., 2605.00742v2 | Bayes-consistent controller; LLM observation models judged by calibration and utility | Position only; Bayesian-specific; no authority or acceptance |
| FABLE, 2608.00215v1 | Exogenous per-user layer, feasible set, anytime-valid false-promotion control | Personalization only; bandit-learned policy. **Closest on acceptance**; the paper compares against its promotion rule |
| **Rules as Programs (RAP)**, `programasweights/rules-as-programs`, MIT, head `901acfbbde` [Rep table] | **The closest direct prior art on placement**: versioned natural-language rules, outside the agent's weights, compiled to exact Python plus PAW functions, checking an agent's responses and tool calls through lifecycle hooks. Findings are bound to rule revisions; operational failure is never recorded as `OK` | **It reports and never blocks.** That is detection, not gating: for an irreversible effect a rule checked afterwards cannot prevent it. RAP claims no placement test and no acceptance protocol, so it does not scoop the paper. The paper cites it for the detection/prevention boundary and adopts its evidence hygiene (§3.5) |
| Externalization, 2604.08224v1 §7.3 | Qualitative trade-offs | No measurable conditions or falsifiers |
| CaMeL, Progent, CapScope 2609.08371, AI control 2312.06942 | Enforcement outside the model (CapScope 33–47/75 vs 3/75 injected effects [R]) | Cost-derived thresholds. Cited, not claimed |
| HCPI, Seldonian NSF, SPIBB, CSPI-MT, LTT/CRC | Confidence-gated acceptance; "No Solution Found" | Evaluator isolation from the proposer; identification when actions change outcomes |
| Contrastive-LM/CLM, 2026-09-23 [R] | A shielded harness reaching parity on survival while the model agrees with the planner 65.8% of the time against 98.7%, with 4,883 shield interventions against 28 | Exactly "the model is not the policy": the paper uses it as the reporting pattern — agreement and intervention counts beside end-to-end success |

### 2.2 Definitions

The decision point for each action family is `(A, x, s(x), c, G, h)`. Three properties are
separated: **ownership** (who sets c, G and h, and whether they are versioned inputs),
**implementation** (closed-form or learned, the latter allowed if c and G enter at decision time),
and **enforcement** (G is checked before the effect).

Trusted control inputs are c, G, the handler models, the rule version, and instrument outputs
s(x) under a versioned score contract. Raw x, retrieved text and tool output are untrusted.

δ is **executively exogenous** when its parameters are owned and versioned, it reads only trusted
inputs, and G is enforced before effects.

**E1 arm classes, fixed at the design lock.** Calibration for the no-shift arms is
**temperature only, with no intercept**, so B-stale is exactly the plug-in frozen at 0.5 on the
same scores (Fable v3 P2-8).

| Arm | Definition | Class |
|---|---|---|
| A | Plug-in threshold C_FP/(C_FP+C_FN) on temperature-calibrated scores | Exogenous, closed-form |
| A_tuned | Threshold tuned per ratio on the calibration split | Exogenous parameter, tuned closed-form (descriptive only) |
| A-raw, A-recal | Under shift S: re-threshold only; or re-estimate the intercept from 200 deployment-prior labels, then re-threshold | Exogenous |
| B-stale | The 1:1-trained head at its own rule, equal to the plug-in frozen at 0.5 | Endogenous, fixed cost |
| B-retrain_r | Cost-weighted head retrained on the fit data at ratio r | Endogenous, retrained per cost |
| B-retrain_S | Fit data importance-reweighted to the new prior, plus the same 200 labels, retrained at the S cost | Endogenous; the strongest cheap retrain |
| C, C\*, E | MLP given the raw ratio; logistic head given log(C_FP/C_FN) with a free coefficient; contextual-bandit policy gradient with c as input | Exogenous parameter, learned implementation |

### 2.3 The operational test

X2 is a commitment [C]. The other rows stay [H] until their falsifiers run. Each predicate returns
*holds*, *fails* or *unknown*. The principal sets every ε.

| Id | Holds when | If unknown | Rule | Counterexample | Falsifier → consequence |
|---|---|---|---|---|---|
| X1 Cost heterogeneity | Δ_c > ε_c (share of plug-in actions that flip across the plausible cost set), and costs change faster than retrain plus requalify | Measure Δ_c from scores and the cost set | c and thresholds are decision-time inputs | Stable population preference; act-all 0.698 vs threshold 1.369 [Rep toy] | E1: B-stale equivalent to A at every powered ratio, or B-retrain superior to A (or to A-recal under S) beyond δ → narrow or drop X1 for the task |
| X2 Effects and authority [C] | Effects outside a sandbox, delegated grants, no recoverable region, or attacker-writable input | Holds | Enforce G before the effect, with recovery. Never optimize G | Reversible sandboxed drafting | Sub-claim only: a gate with recovery lowers safe task success at a matched unauthorized-effect rate and workflow cost → "better recovery", never "no gate" |
| X3 Instrument churn | At least two instruments of differing reliability, or change faster than retraining, and requalification is measured cheaper | Estimate both costs | Per-instrument score contracts | One stable instrument (Mozannar–Sontag §5.1) | E2: joint L2D wins beyond the margin before and after a swap, at no greater adaptation cost → drop X3 |
| X4 Signal sufficiency | After exposing fields, R_suff ≤ ε | Expose fields first | If it fails beyond repair: an endogenous decision inside an exogenous envelope | Hidden stake +57.7% regret [Rep toy] | End-to-end still wins after exposure → envelope |
| X5a Observability | Complete-episode outcomes for a known-probability sample that includes auto-accepts | Specify and audit | "Optimize" also needs X5b | Selective labels | E3: proxy selection equivalent to outcome selection |
| X5b Identification | Policy-invariant labels, full-information replay, randomized rollout, or logged propensities with overlap | `insufficient_causal_evidence` | Incumbent–challenger on identified outcomes | Shadow mode (`validation.md` L156–160) | A condition |
| X6 Contestability | A contract, regulator or principal requires reproduction [C] | Ask | Exogenous decision record | Entertainment | Untested |
| X7 Absorption | X1, X3 and X6 fail; stable and outcome-dense; measured overhead exceeds gain | Never by default | Distill; keep the exogenous incumbent | The principal is not the model owner | The absorbed version retrains no more often than the exogenous one re-thresholds |
| A Acceptance | The proposer can see or influence the evaluation channel | Holds | Acceptance outside the proposer's read and write set | autoreason [R]; 2606.11045 [R] | E4 fails → the protocol is not adopted |

**Procedure.** (1) If effects exist, G is a contract. (2) If X4 fails beyond repair, use the
envelope. (3) If X1, X3 or X6 holds, the parameters are exogenous; the implementation may be
learned. (4) If a rule works and nothing holds, retain it. (5) Absorb only with X7's measured
justification. (6) Claim "optimize" only under X5a and X5b. Unknowns route to measurement.

**Detection is not prevention.** A rule evaluated after an effect, as in RAP, is a monitor. It
belongs in the record and in the climb ledger, and it never satisfies X2.

### 2.4 The acceptance protocol

Four tests are reported separately. Any one of them can fail.

1. **Statistical support.** Mode, margin, α, method and family size are fixed before confirmation.
   Δ = candidate loss − incumbent loss, so negative is better. Losses are **bounded**, and the
   design lock records the bound.
   - The claim-bearing interval is a two-sided **empirical Bernstein** (Maurer–Pontil) interval
     for bounded losses, at α/(2m) per tail over the m contrasts of the family. Radius:
     `s·sqrt(2 ln(2/δ)/n) + 7R ln(2/δ)/(3(n−1))`, with δ = α/(2m), s the sample sd of the paired
     differences and R their range. Superiority holds when UCB < −m_sup; non-inferiority when
     UCB < +m_NI; equivalence when the whole interval lies inside ±margin.
   - **Why this and not v3's normal CI.** EB's coverage holds for any bounded distribution,
     including sparse rare-large differences, and its radius floor cannot collapse when no
     nonzero difference is observed. On Astra's counterexample, the normal CI and the bootstrap
     both give `[0, 0]` with probability 0.2766 at n = 12,850, while the EB radius is 0.00261
     against a 0.00005 margin, so v4 reports *unpowered*, which is correct [Rep, calc §1].
   - `hoeffding` stays available and is the conservative σ-free fallback. It is byte-identical to
     0.7.2's output, with a regression test.
   - `sign_exact` has no UCB. Its rule: losses in {0, 1}; m = 0; the one-sided exact binomial p on
     discordant pairs is ≤ α/K. It certifies direction only.
   - Normal-theory intervals may be *reported* for readability. They carry no error claim, and the
     helper labels them `descriptive_only`.
   - "Retain incumbent" is a first-class result.
2. **Eligibility.** `evidence_kind` is derived from provenance; the weakest source wins. Proxy or
   fixture evidence cannot support a margin.
3. **Identification.** X5b holds.
4. **Isolation.** The evaluator, splits and confirmation labels are outside the proposer's read
   and write set, as tested by E4c and B16.

Baselines always include constant policies and per-case-best headroom. The paper names what it
imports from HCPI, CSPI-MT and FABLE.

### 2.5 Preference and outcome optimization

**H-DPO [H].** Where X1, X2 or X6 holds, a system whose c and G are decision-time inputs has lower
change cost and a shorter audit path than an action policy trained by DPO, KTO or GRPO on
fixed-cost data, at non-inferior complete-episode loss.

GRPO and outcome RL also optimize episode outcomes; the claimed difference is where c and G live
and how changes are accepted. KTO is the strongest competitor for binary outcomes.
Preference-trained proposers and decision-trained instruments may sit inside the envelope.

Endogenous preference optimization is right when all four hold: the output distribution is the
deliverable; there is no principal-specific cost matrix; there is no delegated authority or
irreversible effect; and preferences are stable relative to retraining.

### 2.6 Claims and evidence

| # | Claim | Evidence now | Upgraded by |
|---|---|---|---|
| P1 | A stale 0.5 threshold regrets heavily under cost shift: **+95% at 1:9, +216% at 1:19, +553% at 1:49** on the v3/v4 synthetic calibrated population | [Rep, calc §2]. v3's "+154% / +364%" came from an earlier population and is withdrawn (Fable v3 P2-10) | E1: A vs B-stale |
| P2 | A fixed-cost head loses off its ratio; retraining per ratio and cost-conditioned heads are measured, not assumed | [H] | E1: B-retrain, C, C\*, E |
| P3 | Authority is a pre-effect contract | [C]; CapScope and the verifier tax [R]; RAP's report-only hooks as the counter-case [Rep] | Cited |
| P4 | Exogenous deferral adapts more cheaply after a handler change | [H] | E2 (optional) |
| P5 | Episode-level selection beats proxy selection | [H]; GEPA p = 0.29 [R] | E3 |
| P6 | Untouched incumbent–challenger lowers false adoption | [Rep sim] −1.8 vs −0.26 pp | E3, E4a |
| P7 | Learn utilities, not policies | [H], discussion only | — |
| P8 | Well-designed research loops keep acceptance exogenous | [C], motivation | E4 |
| P9 | Under prior shift, recalibrate-and-rethreshold is non-inferior to retraining at equal labels | [H] | E1-S |
| P10 | The cheapest adequate **artifact form**, not the largest model, meets a bounded decision's policy; programs lose on fuzzy real text | [Rep table] RAP: bespoke lexical code 0.993 macro-F1 externally, but 0.771 recall where lexical matching cannot see the distinction, where fine-tuned PAW reaches 0.961 | M5 (§3.3) |

### 2.7 Experiments

**Common rules**

- **Two locks**, hashed and dated in `research/080/prereg/`, with read-only copies under `augctl`.
  - The **design lock** precedes any **experiment-dataset download or any read of dataset text or
    labels**. Provisioning artifacts — wheels, the base image, and the §4.4 acceptance weights
    (MiniLM, Qwen3-1.7B) — are explicitly not experiment data, and §4.4 runs on synthetic texts,
    as M0 did [Rep]. The lock fixes estimands, arms, controls, margin rules, family and m,
    α = 0.05, power 0.8, the bound R on each loss, the method, seeds, split proportions, the n
    rule, **the per-contrast planning gap g**, caps and outcome rows.
  - The **analysis lock** follows fitting, calibration and pilots, and precedes any confirmation
    read. It records split-manifest hashes, σ̂ per contrast, the numeric margins, the required n,
    the powered set, the allocation of n, the hashes of the frozen arms and any prespecified
    narrowing. It never re-chooses g.
  - The grader (`augctl`) refuses to score confirmation data unless the analysis-lock hash matches.
  - **Confirmation texts** are released to the run stage only after the analysis lock; labels are
    never released (Fable v3 P2-8, Astra v3 finding 1).
- **Family rule.** Bonferroni over the m contrasts of the family, two-sided, α/(2m) per tail, read
  from the EB interval of §2.4. Every claim type is read from that one interval.
- **Powered set.** A contrast is powered if the n its method needs, at the **design-lock** g and
  the analysis-lock σ̂, is at most the available n. g = 0 for equivalence and non-inferiority
  (true Δ = 0 is the planning point) and the prespecified planning effect for superiority
  (Fable v3 P2-3). Unpowered contrasts are reported with their intervals and count toward no
  outcome row in either direction.
- **Margins** are fixed by substantive rationale at the design lock and never moved afterwards.
  If compute or data bind, the prespecified narrowing or inconclusive row applies.
- **Superiority margins are stated**, not implied: δ_r in E1, 0.02 utility in E3, 0.01 in M5.
- **Controls test machinery only**: an identical frozen policy through the full pipeline (Δ ≡ 0),
  and planted effects whose value is known analytically. A failed control is a pipeline fault.
  Comparisons between genuinely different policies are outcomes.
- "Supports" requires significant pre-registered results. "Not rejected" never counts as support.

**E1: cost shift and prior shift.** Tests X1, P1, P2 and P9. Required. Runs on tabputer-1.

| Field | Specification |
|---|---|
| Data | **Primary: CivilComments.** CC0; toxicity ≥ 0.5; about 2.0M rows [C, recheck at M2]. Exact-normalized-text dedup across partitions. Seeded partitions: fit 200k; **fit-B 200k** (the source of the "second, equal-size fit subsample", Fable v3 P2-4); calibration 100k; M5 pool 100k; confirmation the rest, about **1.4M**. **Secondary: CLINC150** (CC-BY-3.0, human-written): 23.9k resplit into fit 8k, calibration 3k, confirmation 12,850 |
| CLINC decision (Fable v3 P2-9) | Binary route-or-abstain against the OOS class: s(x) = 1 − P(OOS); an FP is routing an OOS query to an intent handler, an FN is abstaining on an in-scope query. The same cost ratios and plug-in rule apply |
| Instrument | Frozen all-MiniLM-L6-v2 (pinned sha) plus logistic regression, **temperature-calibrated with no intercept** |
| Costs | C_FP + C_FN = 1. Training range {1:1, 1:4, 1:9}; held out {1:19, 1:49, 4:1}. Shift S: ratio 1:9, confirmation resampled to 3× the fit prior (about 0.24), capped at 0.5 |
| Family (m = 19 per dataset) | At each held-out ratio: A−B-stale; A−B-retrain_r; C−A; C\*−A; E−A (15). Under S: A-recal−B-retrain_S; A-raw−A-recal; C\*−A-recal; E−A-recal (4). A_tuned and in-range ratios are descriptive |
| Margin | δ_r = 0.02 × the calibration-split cost of A at ratio r. Under S, 2% of A-recal's calibration cost at the S prior |
| Loss bound | Per-case cost ∈ {0, C_FP, C_FN}, so the paired difference has range R_r = 2·max(C_FP, C_FN): 1.00 at 1:1 up to 1.96 at 1:49. The design lock records R_r per ratio |
| Monotonicity | For each case the action switches at most once, abstain → act, as C_FN/C_FP increases along 4:1, 1:1, 1:4, 1:9, 1:19, 1:49. Violations are counted per arm |
| Planning n [H, synthetic population, AUC 0.901, prevalence 0.080; Rep calc §2] | Equivalence of C\* to A (A perturbed by logit noise τ): at τ = 0.1, n = 78k (1:1) to 401k (1:49); at τ = 0.3, 159k to 688k. All fit 1.4M. Superiority of A over B-stale: 1,425 (1:49) to 18,754 (4:1). **CLINC at 12,850 powers no equivalence contrast at any ratio**, so CLINC contributes superiority rows only |
| Rejects X1 on the task | B-stale equivalent to A at every powered held-out ratio; **or** B-retrain_r superior to A beyond δ_r at a powered ratio; **or** B-retrain_S superior to A-recal beyond δ |
| Narrows | **Ownership:** C\* or E equivalent to A at every powered held-out ratio and to A-recal under S, with zero monotonicity violations. **Implementation:** B-stale superior to A at a powered ratio means the calibrated plug-in failed (Astra's case: p̂ = 0.2, true 0.05, costs 0.1/0.9, loss 0.095 vs 0.045 [Rep]); X1 is then unsupported on the task until calibration is repaired |
| Supports | At least 2 of the 3 held-out ratios powered; A superior to B-stale by δ_r and non-inferior to B-retrain_r at every powered ratio; and, if S is powered, A-recal non-inferior to B-retrain_S with no more labels |
| Inconclusive | Fewer than 2 powered held-out ratios, or none of the rows above |
| Outcomes, not controls | A fitted on fit-B vs A fitted on fit: reported as fit variance |
| Controls | Identical frozen A through the full pipeline: Δ ≡ 0 on every case. Semi-synthetic: on a copy of confirmation, draw y\* ~ Bernoulli(s_i) from A's calibrated scores, so each threshold policy's expected cost is analytic. Plant (a) two analytically equal-cost thresholds, (b) Δ = 1.5δ_r, (c) Δ = δ_r. Over 200 redraws the pipeline must claim equivalence in (a) at about its planned power, inferiority in (b), and false equivalence in (c) at most at the α/m rate (binomial CI) |

**E3: episode control and acceptance.** Tests X5, P5 and P6. Strongly recommended. Needs the GPU.

| Field | Specification |
|---|---|
| Population | HotpotQA distractor validation: CC-BY-SA-4.0, 7,405 hard questions [C, recheck]. Rounds read k ∈ {2, 4, 6} paragraphs and choose stop, expand or abstain. U = EM − λ·rounds/3 − μ·tokens/1000, **clipped to [−0.2, 1] at the design lock, so R = 1.2**; λ = 0.1 primary; μ fixed at the lock |
| Identification | Full-information replay: every answer at every k, so X5b holds by construction |
| Readers | Qwen3-1.7B and Qwen3-4B at pinned revisions, BF16, non-thinking, greedy. **Served by the image's vLLM in batch-invariant mode or with a fixed batch composition**, because batched reruns matched on only 59.8% of prompts in M0 [Rep]; over 9 calls a whole question replays identically with probability 0.0098 [Rep calc §6]. A 50-question determinism check reports the realized rerun disagreement rate before confirmation |
| Arms | (i) implicit prompt; (ii) threshold on LLM answerability; (iii) threshold on dense similarity; (iv) composite; (v) constants; (vi) proxy-selected threshold; (vii) outcome-selected threshold |
| Family (m = 6) | Per reader at λ = 0.1: best explicit − implicit; best explicit − best constant; (vii) − (vi). The best explicit arm is chosen on search and frozen |
| Margin | 0.02 utility (about 2 EM points), superiority and equivalence alike |
| n [Rep calc §3] | Search 1,000 questions (including a 100-question σ pilot and a 50-question timing pilot); confirmation the remaining 6,405. EB needs 5,178 at σ = 0.25 and **6,794 at σ = 0.30**, so at m = 6 the equivalence rows are powered only if σ̂ ≤ about 0.29. The prespecified narrowing drops the 4B reader (m = 3), where 6,185 suffices at σ = 0.30. Superiority at a 0.04 planning gap needs 1,830 (m = 6) |
| Calls | 9 per question per reader. **Full replay of all 7,405 is the planned workload**: 133,290 calls for two readers, 66,645 for the 1.7B-only narrowing (Astra v3 finding 4). At the measured 2,004 tok/s batched and 64 output tokens per call that is 1.2 and 0.6 GPU-h of decode [Rep calc §6]; prefill and the timing pilot govern the real figure |
| P6 population | The **6,405 confirmation questions**, which the search set never touched. Its finite-population truth uses their full replay (115,290 calls for two readers), and that truth is held by `augctl` and never exposed to selection |
| Cap and narrowing | 24 GPU-h for E3. If the timing pilot projects more, the 4B reader is dropped before any confirmation read. If the projection still exceeds the cap, equivalence rows are inconclusive. The margin never changes |
| Outcomes per claim | *Explicit vs implicit* and *policy vs constants*: supported if the best explicit arm is superior by 0.02 for every powered reader; rejected if the two are equivalent for every powered reader; otherwise inconclusive. *P5*: (vii) superior to (vi) supports; equivalence rejects. *P6*: over 200 resplits, false adoption is judged against the 6,405-question truth. Incumbent–challenger lower than adopt-best, with the 95% CI of the difference excluding 0, supports |
| Controls | Identical frozen incumbent vs its copy: Δ ≡ 0, never adopted. A planted +0.05 utility shift on a replay copy must be adopted at its planned power. The per-question oracle is reported as headroom, not used as a control |

**E4: acceptance machinery.** Tests A and P6. Required. Fixture and simulation evidence only.

| Part | Design | Pass |
|---|---|---|
| E4a Monte Carlo diagnostic, **on the GPU** | **C = 108 cells**: `hoeffding` and `empirical_bernstein`, each 2 modes × n ∈ {300, 1,000, 2,500} × K ∈ {1, 5} × 4 loss distributions (three-point, two-point extreme, continuous, rare-large); plus `sign_exact` on the 2 binary distributions × 3 n × 2 K. **R = 40,000** replications at the boundary null. It is a vectorized reduction over at most 108 × 40,000 × 2,500 = 1.08e10 sampled losses, chunked at 2,000 replications × 2,500 (19.1 MiB fp32), 2,160 kernel batches [Rep calc §5]. The coverage *claim* rests on the theorems and exact-rational unit tests; this detects gross defects. **`sign_exact` cells stay exact-rational on the CPU**: their qualification is arithmetic, not sampling, which is the one recorded CPU step under D-b | Every cell's simultaneous (Bonferroni over 108, γ = 0.05) one-sided Clopper–Pearson upper bound ≤ α + τ = 0.055, i.e. at most **2,049** adoptions per cell [Rep calc §5]. A cell at 4.5% fails with probability 1.9e-9; an exactly nominal cell fails with 0.128; 6% is detected with probability ≈ 1. **Positive controls**, each naming the cell class that must fail (Fable v3 P2-7): radius removed → every cell (size 0.50); radius n inflated 100× → Hoeffding and EB cells at σ ≥ 0.3; Δ sign flipped → non-inferiority cells only, because it is invisible to the size test in superiority mode. The planning effect per distribution is fixed at the design lock, and the K = 5 event is any-of-five adoption. Cap 1 GPU-h; exceeding it narrows to n ∈ {300, 1,000} |
| E4b Eligibility | Fixtures: teacher-labeled confirmation rows; synthetic text; unequal inclusion probabilities; the 50/950 case (−0.667 apparent vs +0.9 true); the sign case (p = 0.0068 while mean loss rises by 0.0292); **a zero-discordance rare-large case** | In order: `proxy_evidence_only`; `fixture_evidence_only`; `unsupported_sampling_design`; refused; `sign_exact` refuses non-binary input; the rare-large case returns `unpowered`, never equivalence |
| E4c Isolation (tabputer-1) | A scripted adversary harness plants each exploit with a canary. Hard-coded confirmation IDs → leak gate. Gold in synthetic rows → overlap audit. Sibling-run read → per-run container mounts. Evaluator or split edit → owned by `augctl` (EACCES) and hash drift. Read of confirmation labels → not mounted, EACCES on the host, **and B16's reconstruction attempt from every readable corpus**. Network exfiltration → `--network=none` plus the skuid drop. Write outside `/work` → EROFS. Disk exhaustion → ENOSPC on a size-bounded run filesystem (B17). Resource exhaustion → cgroup limits, GPU budget and timeout | Every exploit is refused by its named mechanism, and its canary proves the plant was active. A benign planted improvement is accepted end to end |
| E4d Agent A/A (optional) | 20 incumbent-vs-itself runs. The proposer runs off tabputer-1; candidates execute only under the §4.2 profile | Reject at ≥ 3 adoptions: P = 0.0755; power 0.79 at a 20% rate. A smoke test only |

**E2 (optional; CIFAR-10H, CC BY-NC-SA).** Skipped by default (decision 5).

### 2.8 Outline

Seven sections: (1) two policies, and what is known; (2) ownership, not weakness; (3) the test,
with worked scenarios including one human or organizational system; (4) accepting a change;
(5) evidence — E1, E3, E4, including inconclusive rows and what failed; (6) preference, outcome RL
and the boundary; (7) limits and open falsifiers.

### 2.9 Placement and publication conditions

The draft is Typst in `research/080/paper/`; the site is `docs/exogenous-policy/`; code and
receipts are in `research/080/`.

**Publish only when all hold:** E1 ran as pre-registered and is reported whatever the result;
every number is bound to an artifact or a Reported source with its comparison, metric, population
and conditions; every reference resolves by ID with title and retraction checks; a human has
checked every load-bearing passage, including the seeded wrong-claim case; independent review on
the requested models leaves no unresolved severe flaw; the name is decided; licenses and TypeSafe
terms are rechecked; §6.5 passes and `check_site.py` passes on the build; font provenance is
recorded.

**If scooped:** reframe within a week as replication plus E1, E3, E4 and the protocol. Watch
manually, weekly. Decide by 2026-11-15.

## 3. Trainer skill (`augustus-train`)

### 3.1 Packaging and repository checks

- A second skill in the `augustus` plugin, invoked as `/augustus:augustus-train`. Move it to its
  own plugin if it fires on more than 10% of augustus-only activation prompts.
- **M1** branches from `origin/main` after `git fetch origin`, recording the SHA it actually used.
  It creates a valid skeleton at `0.8.0-dev` in both skills and the marketplace.
- It then generalizes `check_repo.py`, which still hard-codes one `SKILL_PATH` and one 180,000 B
  reference total: per-skill limits and totals, version parity, portable frontmatter, per-skill
  reachability.
- The first 0.8.0 commit adds `.local/` and `.claude/` to `.gitignore`.
- The augustus hand-off is one `SKILL.md` line (10,743 of 16,000 B at 0.7.2).
- Scenarios compare against the last published release, v0.7.2.

| Request | Owner |
|---|---|
| Choosing a classifier, Jev, an LLM or a rule; thresholds; calibration; prompt or DSPy climbing | `augustus` |
| Training, fine-tuning or distilling a head; creating or labeling data; training climbs; **compiling a program to a function** | `augustus-train`, starting at G0 |
| Distilling Jev, or selecting training rows by Jev output | `augustus-train`; refused by default, overridable (§3.6) |
| Tone fine-tuning | Neither |

### 3.2 G0: the don't-train check takes the acceptance policy as input

**Inputs:** the decision; the cost policy (units, mode, margin, α, method, loss bound); the
acceptance bar; available independent gold (count, unit, sampling design); the label budget.

**Do not train when any of these holds:**

- an exact program decides the case, or a program plus a small exact check does;
- a baseline meets the bar;
- the n the chosen method needs, at the planning effect and including the fit/confirmation split,
  exceeds the independent units available (computed, not guessed);
- the criteria churn faster than retraining;
- labeler agreement is below the bar;
- the task needs multi-step reasoning;
- **an exact simulator makes search cheaper than a learned policy** (a second R0 exit; jev-echo's
  Echo+search beat its teacher 9/10 at equal latency because the rules predict the next state
  exactly [R, n = 10]).

**Small samples.** For a large prespecified binary effect, 20 discordant wins in 40 rows give
p ≈ 1e-6 under `sign_exact`. A 2 pp guarantee is infeasible at that size.

### 3.3 The ladder is artifact forms, under one acceptance gate

v3's ladder was models only. v4's rungs are **artifact forms**. The gate, the splits and the
margin are identical across them; only the artifact changes.

| Rung | Artifact | Entry | Exit |
|---|---|---|---|
| **A0** | **Exact program.** Deterministic code the maintainer wrote or reviewed | Always first | It cannot express the distinction the decision needs |
| **A1** | **Agent-synthesized program.** An agent writes deterministic code; the artifact is **frozen and hashed before any confirmation read**, so the agent is not in the loop at acceptance | A0's logic is discoverable from examples | Fuzzy language defeats it |
| **A2** | **Compiled function (PAW).** A spec plus examples compiled to an adapter over a small frozen interpreter; inference is local and offline | The rule is semantic but stable, and latency or offline operation matters | It loses to a head on the same gate |
| **A3–A6** | Model rungs: R1 frozen readout → R2 linear head → R3 small encoder → R4 LoRA plus head | The lower forms fail the gate | — |
| **A7** | Generalist. Never the default | Research only | — |

**Composed decision programs.** Code decomposes the decision, and each sub-decision takes its own
cheapest adequate form: an exact check, a head, a PAW function, or a Jev call at inference, which
D-d permits. Acceptance is end-to-end **plus per stage**; sub-call latency and cost count. AND is
never a product of marginals: ask the compound question, or aggregate batched judgments in code.
Program structure is a climb, so it goes through the climb ledger and the frozen-confirmation rule.

**Circularity trap.** A synthesized program scored on code-computed labels from its own family is
circular. T1 therefore stays `fixture_evidence_only` and informs guard text only. The honest arms
are the real-text tasks T2a–c, **and that is where programs are expected to lose**; the plan says
so in advance and reports it either way.

| M5 element | Pre-registered rule |
|---|---|
| Arms | R0; **A1** (synthesized program, frozen); **A2a** PAW-standard via the local single-GPU compiler; **A2b** PAW-ft with a local teacher (our vLLM Qwen3-4B-Instruct-2507) and a local initial compile; R1 (Qwen3.5-2B frozen: raw, two-order averaging, L0, then OOF temperature); R2a (LR on MiniLM); R2b (ridge/LDA on R1's ⅔-depth state); R3a (SetFit, pinned body) as the comparator. R3b (DeBERTa-v3-large) runs if the GPU passes §4.4; R4 is a documented escalation, untested |
| Tasks | **T1** (generated, code-labeled): `fixture_evidence_only`. **Real-text confirmation**, human-written, seeded equal-probability splits, the population being the benchmark and not deployment traffic: **T2a** BANKING77, 77-way, CC BY 4.0, about 13.1k rows, real-query provenance checked at M2; **T2b** CLINC150 plus OOS, route-or-abstain, reusing E1's seeded CLINC partition; **T2c** CivilComments, the E1-disjoint 100k pool. Fixed cost matrices: misroute 1, abstain 0.3, correct 0 for T2a/T2b; C_FP:C_FN = 1:4 for T2c. Losses ∈ [0, 1], so paired differences have range R = 2 |
| Estimand and test | Δ = loss(low rung) − loss(R3a) in normalized cost. Non-inferiority: EB UCB(Δ) < +0.01 over **K = 5** low rungs (R1, R2a, R2b, A1, A2b) at the family level. Escalation uses the matching **EB LCB(Δ) > +0.01 at the same α/(2K) tail** (Fable v3 P2-9). Tasks combine by intersection-union |
| n [Rep calc §4] | At true Δ = 0 with 80% power, EB at K = 5 needs 6,671 rows (σ = 0.10), 14,035 (0.20) or 25,535 (0.30). Planned confirmation: T2a about 6,000 (powered only if σ̂ ≤ 0.08); T2b 12,850 (σ̂ ≤ 0.18); T2c 40,000, **expanded to 60,000 by the analysis-lock n(σ̂) rule, not by discretion** (σ̂ ≤ 0.49). Fable's estimate that a 77-way task disagreeing on 7% of rows has σ ≈ 0.26 makes T2a likely unpowered; the narrowed and inconclusive rows exist for exactly that |
| Stop at a low rung | One low rung is non-inferior on every powered real task, and at least 2 tasks are powered. The recipe names the artifact form that sufficed and the task type |
| Narrowed | The same with only 1 powered task. The recipe names that task type only |
| Escalate | R3a superior to every low rung by more than 0.01 on a powered task |
| Workload-local | Mixed results across powered tasks |
| **Inconclusive** | Everything else, including no powered task. No rung recommendation: the default stays the procedure, and the recipe states that the 0.8.0 reproduction was inconclusive at 1 pp |

**Multimodal side ladder (documented, untested in 0.8.0 unless the maintainer approves a pilot;
decision 9).** M-R0 don't train or route → M-R1 frozen VLM readout (candidate-letter logits in
fp32, OOF temperature per question type) → M-R2 head on frozen features → M-R3 small perception
fine-tune → M-R4 language-tower LoRA, vision frozen → M-R5 never the default. Two rules bind any
media claim we make or ship:

- **Modality blind-arm gate.** The sighted arm must beat the best blind arm — text-only,
  options-only, blank media, media swapped across items — through the same trained pipeline, on
  untouched group-split data, with a paired cluster bootstrap by media group and an NLL-delta
  lower bound above 0. If it fails, it is not a media decision; route to the text ladder and train
  nothing multimodal. Evidence for the gate's necessity: MedQA-MM text-only 53.96% against full
  62.63%; an image-free decomposition matching a reported joint 0.69 at about 0.71 [Rep] [R].
- **Per-type, per-head outcomes.** A pooled metric never decides (a dead choice head at 0.159
  inside a pooled 0.82 [R]).

### 3.4 Data protocol

Each rule is conditional and stated once, in `data-and-labels.md`.

| Rule | Applies when | Guard or check |
|---|---|---|
| Gold first | Always | Confirmation data are sampled from real traffic with equal inclusion probability, labeled independently, frozen and hashed before any generation |
| Teacher route | A teacher is used | Code-computed labels or a local open-weight teacher by default; a hosted teacher must pass §3.6 |
| Double agreement | One teacher labels real text | Not needed for code-computed labels |
| NOTA as answer and distractor | A NOTA option exists | Pair probe |
| Style-seed partition | Style seeds are used | Overlap audit |
| Neutral IDs | Label names are free-form | Rebinding probe (0/1 → no/yes moved AUC from .94 to .23 [R]) |
| Same-split families | Pairs or generation families exist | Group split and a ledger property test. **Media rows group by media SHA-256** |
| Missing-evidence twins | Evidence can be absent | Uniform targets vs abstention |
| **`input_coverage`** | Always | Every row and every decision record states what the model actually saw: frame count, audio window and crop rule, image budget, truncation, candidate pruning. Every carded multimodal recipe dropped evidence silently [R]; a coverage field is what makes that visible |
| **Serving precision** | Always | The calibrator is bound to the precision and quantization it was fit at, and refit after any change. Measured drift up to 0.2 in probability between FP32 and reduced precision on a shipped loader [R] |
| **State-space dedup** | Logged traces | Dedup on the state before any random split; time-ordered splits for logged traces |
| **Labeler identity** | Always | Each row records label source and terms; a row with no labeler field is `unknown` |
| Accumulate real rows | Always | Ledger |
| Fact–text binding | Labels are computed from facts | A constrained renderer or an independent extractor; evidence ablation; filler invariance; corrupted-rendering fixtures. All fixture evidence |
| Real text for T2 | M5 | T2a–T2c as in §3.3. WANLI is an optional generated-text stress test only |

### 3.5 Confirmation and the climb ledger

`compare_workflows.py` gains:

- a `mode` (superiority or non-inferiority);
- a `method`: `empirical_bernstein` (the **default**, because it carries the coverage claim for
  bounded losses), `hoeffding` (byte-identical to 0.7.2, regression-tested), or `sign_exact`;
- a required `loss_bound` (the range R), without which EB and Hoeffding refuse to run;
- a required `sampling_design`, which must be `equal_probability` for confirmation in 0.8.0;
- `sampling_unit` semantics: episode, person or cluster;
- a `descriptive_only` label on any normal-theory interval it prints.

**Rules for the helper.** Bonferroni applies over `comparison_count` for every method. `--help`
states each method's estimand, its assumptions, and what it cannot certify. Numerical tests follow
CONTRIBUTING, and include the zero-discordance rare-large case. Byte copies ship with a parity
test. `audit_sample.py` is a monitoring estimator, not an acceptance bound.

**Climb ledger.** Controller-owned and append-only.

- The config is immutable; the evaluator and splits are hashed, and drift fails closed.
- Candidates are challenged on fresh rows; every round reports Δ against the original anchor;
  rounds are bounded.
- Probes and per-label recall floors are hard gates. The v4 hard gates add, from the sweep's
  recurring defects: the calibration split must differ from the reported split; a temperature at a
  grid bound is flagged; ECE computed on an entropy "confidence" is rejected; pooled test+OOD
  headlines are refused in favor of per-split rows; an "OOD" or "held-out generator" claim needs
  per-split source ids; a checkpoint chosen on test rows fails; an empty conformal set is an
  abstention, never a commitment.
- **Operational failure is never recorded as a pass** (RAP's rule): a rule that failed to load, a
  compiler that was unavailable and an inference error are distinct states from `OK`.
- **Comparator isolation in code, not prose.** Comparator outputs (including Jev's) live on a path
  the trainer cannot read, are never loaded on the selection split, and are recorded with request
  hash, pinned model and timestamp after data and weights are committed.
- A metered budget moves the run to `paused_budget`. The K finalists are frozen, and confirmation
  data are burned once read.

**Terminal states:** `promoted_candidate`, `incumbent_retained`, `dont_train(reason)`,
`insufficient_evidence`, `insufficient_causal_evidence`, `unsupported_sampling_design`,
`paused_budget`, `blocked`, `needs_human(one question)`.

### 3.6 Provider-provenance graph gate

**Graph.** Nodes: rows, texts, labels, features, filter and selection decisions, datasets, derived
corpora, checkpoints, prompts and external models. Edges: `generated_by`, `labeled_by`,
`filtered_by`, `selected_by`, `featurized_by`, `rewarded_by`, `preferred_by`, `relabeled_by`,
`derived_from`, `trained_on`, `accessed_via`. The three new edges exist because reward use,
preference pairs and DAgger relabels are training uses that v3's edge set could not express.

**Resolution.** Each external model resolves separately to its model, provider and revision, and
to its access channel, **by declared lineage and never by name substring**. The verdict is the
most restrictive of the provider's terms, the channel's terms and the weight license.

**Verdict states.** `allowed` (with URL, digest and clause, or it is rejected), `unknown` (missing
parents), `disputed` (a sourced, revision-bound allegation contradicts a declared lineage), and
`refused`.

**Rules.**

- A path from a refused node to a training artifact, through any edge, is refused.
- **Jev (errata D-d).** Jev is allowed as a comparator, baseline, experiment arm, router, selector
  and inference-time feature. **Jev output never becomes training data.** In our own experiments
  that is absolute. In the shipped skill, a Jev-generated training corpus is **refused by default
  with one quoted line of MCA §2.3(b)**, and the user may override it with a recorded
  acknowledgment (artifact, use, date). There is no counsel step and no other ceremony.
- A named approval can clear `unknown` for one artifact and one use. It never silently clears
  `disputed`: the approval record preserves the outstanding allegation and is never described as
  verified lineage.
- Missing parents make lineage unknown.
- **The gate checks declared provenance only**, and the skill says so whenever it reports a pass.

| Test case | Expected |
|---|---|
| Row selected, filtered or featurized by Jev; corpus inheriting from a declared Jev-derived corpus; Jev reached through a router alias such as `typesafe/jev-1.13` | Refused by default; overridable with a recorded acknowledgment |
| Jev output used as an RL reward, a preference pair or a DAgger relabel | Same; the new edges make it reachable |
| A third-party model with "Jev" in its name, a non-Jev declared base, a no-Jev-output attestation and undisclosed training data (Jev-Omni) | `unknown` on missing parents. Not `barred` by name; not `allowed` by attestation. Its three derivatives inherit through `derived_from` |
| A dataset whose card leaves the teacher unnamed, while a third-party README alleges Jev labeling at an unspecified revision (`LocalLLaMA/typed-decisions`) | `disputed`; blocked for training pending resolution, with the allegation and its source recorded |
| A repo that co-hosts Jev-distilled data: an artifact derived from that lineage | Refused; a sibling lineage resolves on its own parents |
| A human label stored in a field named "jev" | Resolves by lineage, not by the name |
| A corpus row carrying a Jev `prediction` field | Field stripped or row refused |
| A trace log with no labeler field | `unknown` |
| Inputs synthesized by a hosted provider with human labels | `unknown` on the input edge |
| Open-weight generated labels with declared lineage | Passes; provenance recorded |
| `allowed` without a digest | Rejected |

### 3.7 Tests and scenarios

Script tests cover the ledger; the fail-closed audit; the climb ledger; every mode, method and E4b
fixture; §3.6; and a teacher-slice error that gold exposes. Behavioral scenarios run with the
skill, without it, and against v0.7.2, using fresh agents and a dated audit.

| Scenario | Expected |
|---|---|
| S1: 5k synthetic rows | Proxy or fixture; real confirmation required |
| S2a: 40 rows, rare-error guarantee | Don't train or shadow, with the arithmetic |
| S2b: 40 rows, large prespecified binary effect | A bounded pilot with a pre-registered sign test |
| S3: a baseline meets the bar | Don't train |
| S4: "CLEAN" without references | `unknown` |
| S5: "climb until plateau" | Ledger, anchor Δ, fresh confirmation |
| S6: review-queue errors | A known-probability audit including auto-accepts |
| S7: "log your Jev calls and distill them" | Refuse by default with the quoted MCA line; offer outcome labels, human adjudication, code labels or a local permissive teacher; state that the override is the user's to record |
| S8: train the JevBench leader | Rank is not a selector |
| S9: multi-step dates | Reasoning exit |
| S10: unequal-probability confirmation sample | `unsupported_sampling_design` |
| S11: the challenger changes approvals | `insufficient_causal_evidence` |
| **S12a: EB non-inferiority, K = 3, margin 0.01, σ̂ = 0.10, 3,000 rows** | Required n 6,164 shown; **inconclusive**; margin not widened (Astra v3 finding 6: the scenario now states method, mode, family and variance instead of inferring infeasibility from the row count) |
| **S12b: the same at σ̂ = 0.02** | Non-inferiority **certified** at 3,000 rows; the skill must not refuse a feasible low-variance case |
| S13–S15: Bayes threshold, prompt climb, tone fine-tune | Not triggered |
| **S16: an exact program already decides the family** | A0; no training, and no compile |
| **S17: a rule check runs after an irreversible effect** | Named as detection, not prevention; X2 unsatisfied |

The activation suite is opt-in, in `tests/plugin-evals/`, at most $10 per release candidate.

## 4. Compute and isolation

§4 describes the host **as M0 built and measured it**, not as v3 proposed it.

### 4.1 Hosts and roles

| Host | Used for | Never used for |
|---|---|---|
| Mac | Authoring; review; `make check`; Typst; serving a built site copy; delegate reviews | Experiments; model weights; candidate code; any isolation claim |
| tabputer-1 | Every experiment (E1, E3, E4, M5); third-party packages and weights; candidate code; the site build in a container | Holding credentials; isolation claims against root, the maintainer's account or privileged k3s workloads |
| Colab | The GPU fallback under D-b, per experiment, with public data and code only | Anything the maintainer has not approved for that experiment. Colab runs carry no B1–B17 claim |

**Access.** Amp reaches tabputer-1 only through the runner `tabputer` (`/mnt/tst`, user `basit`,
passwordless sudo). No SSH from the orb. Every runner task repeats the hard rules: never reboot
(LUKS, console-only passphrase); no `pacman`; never `nft flush ruleset` and never touch ufw, the
docker/k3s tables or `inet modyl_jit`; no restart of docker, k3s, sshd, tailscaled or networking;
no mode changes to `/home/basit` or `/srv/ci`; nothing experimental as `basit` or root; no
credentials on the box.

Now that the research record is public, the site build may stage `docs/exogenous-policy/` on
tabputer-1; it is public material, which resolves Fable v3 P2-2.

### 4.2 Execution profile (as installed)

| Principal | uid | Role | Reads | Writes | Network |
|---|---|---|---|---|---|
| `augexp` | **48201** | Setup downloads; the runner; every container | Own home; `/srv/aug/stage/parts/<run>` (read-only, root-owned); `/srv/aug/runs/<id>` | Own home, per-run directories, `/srv/aug/pred/<id>` | Setup windows: only the local proxy. Closed: nothing |
| `augctl` | **48202** | Acquisition custody, splitting, confirmation labels, manifests, the grader, prereg copies; scores predictions; writes receipts | `/srv/aug/ctl` (700); `/srv/aug/quarantine`; predictions read-only through group `augpred` | `/srv/aug/ctl`, `/srv/aug/stage/parts`, receipts | Nothing, ever |
| `augproxy` | 947 | First-party stdlib CONNECT proxy, used during windows only | Its allowlist | Its connection log | TCP 443 to public addresses, plus DNS to the local stub `127.0.0.53` so CONNECT hosts resolve (Fable v3 P2-1, installed); private and loopback ranges otherwise dropped |

`augpred` is the setgid group on `/srv/aug/pred`; `augexp` writes, `augctl` reads, and no one else
is a member (Fable v3 P2-8).

**Acquisition and staging (Astra v3 finding 1).** Downloads land in `/srv/aug/quarantine`, owned
by `augexp` during the window, together with the HF cache. At window close, `augwindow close`
re-owns the whole tree to root with an ACL for `augctl` only, so `augexp` loses it. `augctl` then
splits, hashes and publishes into `/srv/aug/stage/parts/<partition-id>/`, root-owned and read-only:
fit and calibration partitions with labels, **confirmation inputs with labels removed**, and
nothing else. Each run mounts only the partitions the design lock entitles it to. Complete labeled
corpora never exist in any tree a candidate can read.

**Containers.** Runs launch with `systemd-run --user` inside `augexp`'s own user manager, never
`sudo -u … podman` from another session (B15). Linger is enabled for the window and disabled after.

```
podman run --rm --network=none --read-only --tmpfs /tmp --cap-drop=all \
  --security-opt=no-new-privileges --pids-limit=512 \
  --memory=16g --memory-swap=16g --ipc=private
```

`--memory-swap=16g` is required: with 125 GB of zram, `--memory=16g` alone did not cap memory
(B12, M0) [Rep]. GPU runs add `--device /dev/kfd --device /dev/dri/renderD128 --group-add
keep-groups`. One base image, pinned by digest, loaded from a local `docker save` so no registry
host is needed. `/stage` partitions mount read-only; `/work` binds a fresh per-run directory on a
size-bounded filesystem. Each candidate gets its own container and `/work`. Candidate code never
gets GPU devices.

**GPU budget (mandatory).** GPU memory is **not charged to the container cgroup**: 24 GiB of bf16
tensors were held while `memory.current` stayed at 0.56 GiB [Rep, M0]. Every run therefore
declares its own GPU budget — `torch.cuda.set_per_process_memory_fraction` or vLLM
`gpu_memory_utilization` — recorded in its receipt. Planned budgets against 124 GiB visible
[Rep calc §6]: E1 MiniLM 2 GiB (0.016); E3 readers 14 GiB (0.113); M5 R1 6 GiB (0.048); M5 PAW-ft
38 GiB (0.306); SetFit/DeBERTa 10 GiB (0.081). **A MemAvailable watchdog is real code**, not a
note: the wrapper samples `/proc/meminfo` every 5 s, refuses to launch below 24 GiB and kills the
container below 6 GiB, writing the reason into the run record.

**Egress.** The installed `inet augexp` nftables table matches `meta skuid` and never flushes the
ruleset. `augexp` (and its subuid range 165536–231071) may reach only `lo` TCP 3128, and only
during an open window; everything else is logged, counted and dropped. `augctl`: everything
dropped. `augproxy`: TCP 443 to public addresses plus the local DNS stub. Rootless podman's
user-mode networking runs as `augexp`, so a container started with `pasta` or `--network=host` by
mistake also reaches nothing (B10, verified).

**Three named download windows.** Each is maintainer-attended, opened and closed with
`sudo augwindow open|close`, followed by a B9/B10 re-run and a dated receipt. **No experiment or
candidate container runs while a proxy rule exists.**

| Window | When | What | Allowlist |
|---|---|---|---|
| W1 provisioning | M0, before the design lock | uv CPython, hashed wheels-only lock, the base image (local transfer), and the §4.4 acceptance weights (MiniLM, Qwen3-1.7B) | `pypi.org`, `files.pythonhosted.org`, `huggingface.co`, `us.aws.cdn.hf.co` (the last a recorded edit from the refusal log) |
| W2 experiment data | **After the M2 design lock** | CivilComments, CLINC150, BANKING77, HotpotQA; the M5 readers; PAW checkpoints if the PAW arm is locked in | The same, plus entries added only from the refusal log, each edit recorded |
| W3 site build | Before M9 | github-pages 232 gems | The gem host, added from the refusal log |

`typesafe.ai` and its subdomains stay denied in every window, because setup never needs them. The
proxy binds the TLS SNI to the CONNECT host before connecting [Rep]. IP literals and non-443 ports
are refused.

### 4.3 Boundary tests (all pass before any run; dated receipt)

B1–B15 are as installed and **passed at M0** [Rep, `receipts/m0-tabputer-1-2026-09-23.md`]:
principals and credentials (B1, B2), the maintainer's home and `/root` (B3), other workloads
(B4), the machine-wide readable sweep with a declared marker regex and its 12 known
public-documentation matches (B5), `/srv/aug/ctl` and its canary (B6), writes (B7), persistence
(B8), window-open and window-closed egress including local IPC, D-Bus resolve1 and the tailscaled
LocalAPI (B9, B10), `augctl` (B11), memory and pids (B12), GPU acceptance (B13), sibling runs
(B14), and no foreign process on a principal uid (B15).

v4 adds three, all of which must pass before M3:

| # | Test | Pass |
|---|---|---|
| **B16** | **Confirmation-label reconstruction.** As `augexp`, inside a run container, try to recover confirmation labels: search every readable tree and the HF cache for the original labeled corpus; join stage inputs to any readable corpus by text, normalized text or identifier; read `/srv/aug/quarantine`. A canary label is planted in the confirmation partition | Every attempt fails; the canary appears in no candidate-readable output (Astra v3 finding 1) |
| **B17** | **Disk exhaustion.** Write beyond the quota of the size-bounded filesystem carrying `/srv/aug/runs` and `/srv/aug/pred` | ENOSPC inside the container only; host free space and k3s are unaffected (Fable v3 P2-5) |
| **B18** | **GPU budget.** A run exceeding its declared GPU budget, and a run launched while MemAvailable is below the floor | The budget aborts the allocation; the watchdog refuses the launch and kills a run that crosses the abort floor |

B10's criterion is corrected: inside a `--network=none` netns, host-IP connects fail at
ENETUNREACH without incrementing host counters, so a non-incrementing counter is not a failure;
only the with-networking sub-test must increment `augexp_drop` (Fable v3 P2-8). B14 runs against
test containers, so "all pass before any run" has no ordering contradiction.

### 4.4 GPU acceptance and parity

§4.4 **passed at M0** on the local vLLM ROCm image `sha256:e5e47f6a…` (Python 3.12.13,
torch 2.12.0, HIP 7.2.53211, gfx1151, 124 GiB visible; host ROCm 7.2.4; no
`HSA_OVERRIDE_GFX_VERSION`) [Rep]: bf16 matmul 0.0029 relative, fp32 9.7e-7, softmax 0.0063, SDPA
0.0033, MiniLM GPU-vs-CPU min cosine 0.99999976 on 1,000 **synthetic** texts, Qwen3-1.7B greedy
50/50 identical on rerun, and a 30-minute soak with no amdgpu reset. This answers decision 23.

Three parity checks are added before the arms that need them, each with its bound fixed first:

1. **Qwen3.5 linear attention.** M5's R1 arm is Qwen3.5-2B, whose hybrid GatedDeltaNet layers were
   not exercised by M0's standard-attention acceptance. Compare the flash-linear-attention kernel
   against the torch reference, forward and backward, tolerance 5e-2. Until it passes, R1's
   throughput assumption is unbacked and Qwen3-1.7B is the fallback R1 model. Shared-prefix
   question packing is invalid for that family, because masks cannot isolate GatedDeltaNet state.
2. **PAW interpreter parity.** Run the interpreter as an exported PEFT adapter under transformers
   on the GPU, and compare against the SDK's llama.cpp GGUF runtime on a sample: argmax agreement
   and max |Δp| bounds fixed at the design lock.
3. **Serving-precision parity.** Whatever precision an arm ships, its calibration and its gate are
   evaluated at that precision, and the receipt reports argmax flips and max |Δp| against fp32.

If a check fails, the fallback is Colab (D-b), never CPU, and the platform is fixed per experiment
at its analysis lock.

### 4.5 Runtime and compute budget

| Run | Work | Basis | Wall-clock | GPU budget |
|---|---|---|---|---|
| Windows W1–W3 + B1–B18 | About 45 GB of downloads | Network-bound | 0.5–1 day, attended | — |
| E4a | 4.32M replications, 1.08e10 sampled losses, chunked | [H] 2e8–2e9 elements/s | 0.1–0.9 min, cap 1 GPU-h | 4 GiB |
| E1 | Embed about 2.1M texts; fit arms; 38 intervals; 200 control redraws | MiniLM measured 2.1 s per 1,000 on GPU [Rep] | ≤ 2 h, cap 6 h | 2 GiB |
| E3 | 133,290 calls (66,645 narrowed) | Measured vLLM 2,004 tok/s batched [Rep] | 1.2 GPU-h of decode plus prefill; the timing pilot governs; cap 24 GPU-h | 14 GiB |
| M5 | R1 readout; SetFit; A1; PAW-standard compile; PAW-ft; optional R3b | [H], pilots replace it | cap 24 GPU-h | 6–38 GiB |
| Site build | One github-pages 232 build in a container | — | Minutes | — |

**Envelope.** One run at a time; `--memory=16g --memory-swap=16g`; an explicit GPU budget per run;
launch only at MemAvailable ≥ 24 GiB; abort below 6 GiB. At 18:38 MDT on 2026-09-23 MemAvailable
was 121,366,040 kB of 131,007,996 kB [Coord], so nothing is `blocked(memory)` on a stale note;
the state is derived from the launch measurement.

### 4.6 What is not claimed

- No protection against tabputer-1's root, the maintainer's root-equivalent account, privileged or
  hostPath k3s workloads, kernel or GPU-driver exploits, or side channels.
- `/dev/kfd` and `/dev/dri/renderD128` are mode 0666 host-wide, so `render` membership is not a
  control; candidate code runs without devices anyway.
- New world-readable trees created later by other workloads are covered only when B4 and B5 are
  rerun.
- The proxy binds SNI to the CONNECT host, but tunnel contents after the ClientHello are not
  inspected: **domain fronting through a CDN that permits a Host header differing from SNI is not
  prevented.**
- Whether the `dmem` cgroup controller can bound amdgpu GTT is untested; the GPU budget and the
  MemAvailable watchdog are what stand in for it.
- The Mac provides no isolation. Colab provides none of these claims.
- "Sandbox" means exactly the mechanisms B1–B18 test, rerun after any system update.

## 5. Research automation

Adopt no third-party runtime. The v1 rejections stand: swarm-factory (a lure; do not visit),
remote-instruction installers, githubnext/autoloop, InternAgent, AutoResearchClaw, automated paper
writers, DARE's hosted search, weak keep rules, FAROS code (ideas only). Research documents,
including the loop instructions inside carded repositories, are untrusted source material, never
procedures to run.

**Patrols stay manual** (maintainer decision). A future unattended patrol needs, first: a host
whose job account cannot read confidential material or credentials, verified against every local
account; an enforced egress boundary with complete connection-event evidence; fetch requests bound
to trusted source identities, tested with syntactically valid IDs carrying payloads; the headless
CLI fixes (`--verbose` with stream-json, nonessential traffic disabled, the observed model taken
from assistant messages, a seeded receipt 0, a numeric freshness grace); and spend authorization
with numeric caps and a scheduler owner.

**Paper gates.** A stdlib bibliography gate using ID-only GETs to arXiv, Crossref and OpenAlex,
where `unverifiable` never passes; a span-anchored claim ledger; prose passes with a no-change
option; human sign-off; and seeded fixtures (a wrong arXiv ID, a fabricated citation, a retracted
DOI, v1's AIRA-dojo misattribution).

**Discovery lesson from the sweeps.** Brand-new repositories with empty metadata evade name,
description and topic search. Discovery lanes add code search for wire-format identifiers
(`/v1/systemone`, `"noul"`, `TYPESAFE_BASE_URL`) and Hugging Face author listings.

## 6. Design artifacts: the paper and the project site

### 6.1 The rule

Every figure and explorable names the claim it tests and shows what the reader would see if the
claim were false. Anything that cannot do both is cut. Inconclusive and unpowered results are
displayed as such, never hidden.

### 6.2 The paper

Typst to PDF, US Letter checked at A4. One column of 66–72 characters, with a narrow outer margin
carrying evidence labels and short notes; figures may span. STIX Two Text and Math for text and
math, Geist Sans for heads, tables, captions and labels, Geist Mono for IDs and hashes; 10.5/14.5
pt; at most three levels. The seven sections of §2.8; the test as run-in paragraphs plus one
table; the abstract states the ownership argument and E1's result. Booktabs rules and tabular
figures; one stdlib script renders SVG from the same data as the site's fallbacks; captions state
the parameter state and the label; grayscale plus one accent. Front matter carries the version,
the commit and both lock hashes — and `/evidence/` shows the **window receipts beside the lock
dates**, so a reader can check that no experiment dataset was downloaded before its design lock
(Fable v3 P1-1).

### 6.3 Site

A standalone layout under `docs/exogenous-policy/`, using the site's tokens and local Geist fonts,
with no marketing chrome.

| Page | Reader's job | Contents |
|---|---|---|
| `/` | Follow the argument | A 120-word summary, then the seven sections with explorables at their claims. Labels sit in the margin at ≥ 1200px and inline below that |
| `/test/` | Apply the test | X-5 full width, state in the URL hash, producing a copyable decision record |
| `/evidence/` | Check the experiments | Per experiment: both lock hashes and dates, the window receipts, each contrast's interval drawn against its margin with a powered flag, status (not run / rejected / narrowed / supported / inconclusive), receipts |
| `paper.pdf` | Cite | The canonical artifact |

**Explorables.** X-1 costs move the threshold, not the weights (the stale threshold's regret grows
to +95% at 1:9 and +216% at 1:19 on the planning population; the region where a constant wins is
marked; re-thresholding without recalibration fails under shift). X-2 uncertainty scores are not
interchangeable. X-3 deferral under a handler swap. X-4 accepting a change, including the
"inconclusive" verdict when the interval's half-width exceeds the margin. X-5 the test as a
procedure. X-6 (optional) expose the field. Shared behavior: native controls showing their values;
`aria-live="polite"` outputs; a `<details>` table for every chart; controls inserted only by JS;
seeded PRNGs with a JS-to-Python parity fixture run locally in Node, no npm packages.

### 6.4 Visual system and build

Geist Sans and Mono only, from local OFL WOFF2 files; body 17px/1.6, 62–70ch, at most five sizes.
The site's neutral tokens, with **one accent for data state only**, never headings, links, buttons
or backgrounds; light and dark values at ≥ 3:1 as a graphic and ≥ 4.5:1 with text; no beige,
cream, green, gradients or tints. Labels and series differ by text, shape and dash, not hue. A
1280px ruled grid, a 680px reading column, explorables at 960px, a 220px margin column at ≥
1200px; mobile one column with 16px outer gutters and no horizontal page scroll; wide tables
scroll in named, focusable regions. Headings only where the argument turns; at most a 120 ms
opacity change, removed under reduced motion. WCAG 2.2 AA; full keyboard operation; visible focus;
44px targets; nothing by color alone; reflow at 400% and 320px. Everything reads without JS.

Pages builds with Jekyll 3.10 (github-pages 232). Explorables are hand-written ES modules: no
framework, no CDN, no third-party requests. At most 300 KB per page excluding fonts and the PDF,
and 60 KB of JS. The Pages-equivalent build and `check_site.py` run on tabputer-1 in a container
(gems through window W3, then network-none); the built `_site` is copied back and served on the
Mac for review.

### 6.5 Design review

Freeze source hashes, the build command and font status in a dated audit. Screenshots: essay top,
each explorable in default and one manipulated state, `/test/`, `/evidence/`, at 320, 390, 768 and
1440 px, light and dark, recording **requested and observed** viewport and theme and the count of
unique observed configurations. Interaction: keyboard pass, JS off, reduced motion, 200% and 400%
zoom, VoiceOver on X-1 and X-5. PDF: page 1, a math page, a figure page and the references, at
100% and in grayscale. Mechanical: `check_site.py`, the accent through the dataviz validator, a
network log with no third-party requests. Independent review on the requested models, never
substituted, on frozen screenshots and source, with taste kept apart from blockers. Brief checks:
beige, green or tint; gimmicky type; a heading wall; an explorable without a claim and
counter-case.

## 7. Milestones

Effort is in agent-days, excluding compute. **The ordering below is the fix for Fable v3 P1-1 and
Astra v3 finding 3**: provisioning and acceptance first, then the design locks, then the
experiment-data window.

| ID | Milestone | Depends | Effort | Exit criterion |
|---|---|---|---|---|
| M0 | Provisioning; containment; **window W1 (infrastructure only)**; §4.4 acceptance on synthetic texts; B1–B15 | — | **Done 2026-09-23** | `receipts/m0-tabputer-1-2026-09-23.md` |
| M0b | B16–B18; the quarantine-and-split custody path; the MemAvailable watchdog; the GPU-budget wrapper | M0 | 1 | A dated receipt showing B16–B18 pass |
| M1 | Skeleton (`0.8.0-dev`, `.gitignore`); generalized `check_repo`; modes, methods, `loss_bound` and design check; ledger and provenance graph; overlap audit; climb ledger. **Small PRs, at most 500 changed lines and 15 files each** | M0 decisions | 4–5 | `make check` green, with the CONTRIBUTING numerical tests |
| M2 | Design locks for E1, E3, E4 and M5, including R, g and the PAW/A1 arms; BANKING77 provenance check | **M0 decisions only** | 1 | Hashed **before window W2 opens** |
| M2b | Window W2: experiment datasets and M5 readers; B9/B10 re-run; receipt | M2, M0b | 0.5 | Dated window receipt, proxy closed |
| M3 | E4a–c (E4d optional); T1 generator with fact–text binding | M1, M2b, B1–B18 | 2 | E4 criteria met |
| M4 | E1, then E3, each with its analysis lock before confirmation | M3; §4.4 parity checks for E3 | 2 + 1–2 days of compute | Results against each lock, inconclusive rows included |
| M5 | Trainer reproduction: R0, A1, A2a, A2b, R1, R2a, R2b vs R3a (R3b if parity passes) | M1, M3; Qwen3.5 and PAW parity | 3–4 | §3.3 rule applied, including inconclusive |
| M6 | Author `augustus-train`; hand-off; scenarios; independent review; activation suite | M5 | 2–3 | Budgets pass; no unresolved severe flaw |
| M8 | Paper and site: tokens, figures, explorables with parity, gates, design review | M3, M4 | 6–8 | §2.9 conditions |
| M9 | Local 0.8.0-rc | M6 | 1 | Plugin validates; an isolated install shows 2 skills; **no tag and no release without the maintainer's explicit go** |

**Critical path:** M0b→M1→M3→M5→M6→M9, about 13–16 agent-days. The paper path M2→M4→M8 runs
alongside. **Total:** about 22–28 agent-days plus 2–3 days of compute.

**Scope cut.** The minimum 0.8.0 is the trainer with G0, the artifact-form ladder, the provenance
gate, the confirmation modes and E4. E3, E2, the multimodal pilot and X-6 can slip to 0.8.1. The
paper does not gate the release.

## 8. Risks

| Risk | Mitigation |
|---|---|
| The test is scooped (RAP is the nearest work) | RAP claims no placement test or acceptance protocol; reframe rule and decision date |
| E1 or E3 favors the learned or endogenous arm | Pre-registered rows; report and narrow |
| **Programs lose on fuzzy text and the ladder reads as a failure** | It is predicted in advance (§3.3) and reported as a placement result, not a defect |
| An interval overclaims | EB carries the claim; normal-theory is `descriptive_only`; E4b includes the zero-discordance case |
| Memory contention or an OOM killing other workloads | Container cap with `--memory-swap`; GPU budget; MemAvailable watchdog; one run at a time |
| GPU nondeterminism (59.8% batched-rerun identity) | Batch-invariant mode or fixed batch composition wherever replay matters; the realized rate is reported |
| gfx1151 kernel gaps (Qwen3.5 FLA, PAW, VLM) | Parity checks before the arm; Colab fallback, never CPU |
| A rolling CachyOS update mid-study | Versions in every receipt; updates held during windows; B1–B18 and §4.4 rerun after an update |
| A candidate reconstructs confirmation labels | Quarantine custody, label-free confirmation inputs, B16 |
| A candidate fills the shared disk | Size-bounded run filesystem, B17 |
| Isolation overclaimed | Claims limited to B1–B18; §4.6 |
| Underpowered results read as negatives | Powered-set rule with design-lock g; inconclusive rows; `/evidence/` shows it |
| Mislabeled provenance | Declared-only limit; the `disputed` state; S7 |
| A hosted PAW compile publishes a spec | Local compiler by default; hosted compile is a fallback with public data only |
| A delegate model is substituted | Record requested and observed identity; no fallback |

## 9. Decisions for the maintainer

**Closed since v3:** SSH and sudo for provisioning (D-a); GPU-everything with a Colab fallback
(D-b); publishing, with Jev usable everywhere except as our training data and no counsel step
(D-c/D-d); PAW as a tested arm (D-e); the base image and ROCm wheel (answered by M0); the memory
envelope (measured); the `.gitignore` vehicle.

| # | Decision | Recommended default |
|---|---|---|
| 1 | Name and slug | "When the Model Is Not the Policy", subtitle naming the test and acceptance; slug `exogenous-policy` |
| 2 | Type and venue | A position paper with executed E1, plus E3 and E4; Pages first |
| 3 | E2 (CC BY-NC-SA) | Skip in 0.8.0 |
| 4 | Packaging | A second skill in the augustus plugin, with the 10% switch rule |
| 5 | Confirmation sampling | Equal-probability only in 0.8.0 |
| 6 | Pre-registration custody | Design and analysis locks: hashes plus your dated note in `research/080/prereg/`, read-only copies under `augctl` |
| 7 | Paper typography | STIX Two plus Geist; A/B against all-Geist at the start of M8 |
| 8 | **PAW arms** | Run A2a and A2b locally (local compiler, local teacher). Hosted compile stays unused unless the local path fails on gfx1151, and then only with public examples |
| 9 | **Multimodal pilot in 0.8.0?** | **Default: no.** Ship the M-ladder documented and labeled "untested in 0.8.0". A pilot would be M-R1/M-R2 on one public image task plus one code-rendered task, with the blind-arm gate, after the M2 lock |
| 10 | **Container cap for a 4B VLM or an audio LoRA** | Keep 16 GB CPU / declared GPU budget; audio stays at M-R2 unless you raise it |
| 11 | **One backbone or two for text R1 and M-R1** | Keep the split (Qwen3.5-2B text, Qwen3-VL-2B media) unless the Qwen3.5 parity check fails, in which case Qwen3-1.7B becomes R1 |
| 12 | **Hosted non-Jev teachers** | Ship every hosted teacher as `unknown` with a named-approval path; 0.8.0 checks no provider terms beyond TypeSafe's |
| 13 | **Jev wire format** | Do not emit `/v1/systemone`-shaped servers by default from the skill |
| 14 | Activation spend | At most $10 per release candidate |
| 15 | Scoop timebox | Reframe, don't restart; decide by 2026-11-15 |
| 16 | Site placement | Standalone layout under `docs/exogenous-policy/`; the PDF in the sitemap |
| 17 | Paper gates the release? | No |
| 18 | Colab | Per-experiment approval, public data and code only; no current experiment needs it |

## Sources (delta from v3)

| # | Source | Revision or time | Depth | Label |
|---|---|---|---|---|
| 49 | `receipts/m0-tabputer-1-2026-09-23.md` and the `infra/` tree | 2026-09-23 | Executed | Rep |
| 50 | `reviews/fable-5.1-xhigh-v3.md`; `reviews/astra-max-v3.md` | 2026-09-23 | Full | Mixed |
| 51 | `plan-v3-errata.md` (maintainer decisions D-a…D-e, verbatim) | 2026-09-23 | Full | Coord |
| 52 | `sources/paw-rap-2026-09-23.md` (PAW 2607.02512; `rules-as-programs` `901acfbbde`; `compiler`; `compile-by-training`) | 2026-09-23 | Deep, table reproduced | R / Rep |
| 53 | `sources/clm-2026-09-23.md` | 2026-09-23 | Deep | R |
| 54 | `sources/jev-omni-2026-09-23.md` | 2026-09-23 | Deep | R |
| 55 | `sources/trainer-sweep-2026-09-23.md` (298 items) and `sources/trainer-sweep-multimodal-2026-09-23.md` (139 items) | 2026-09-23 | Synthesis | R |
| 56 | `calc/calc_v4.py` (sha256 `4a2d2308…`) and `calc/calc_v4.out.txt` (sha256 `5d7e2644…`) | This lane | Executed | Rep (arithmetic; synthetic populations [H]) |

v3 sources 43–48 carry over. v3's P1 percentages (+154% / +364%) are **withdrawn** and replaced by
source 56's +95% / +216% / +553%. v3's normal-theory family CI is **superseded** by §2.4.
