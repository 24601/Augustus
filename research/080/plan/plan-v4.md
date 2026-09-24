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
| Author | Revision lane, 2026-09-24. Requested routing: none stated to this lane. Observed identity: not exposed to this lane; it states that rather than claiming one (Fable v4 P2-5) |
| Fable v3 review | `reviews/fable-5.1-xhigh-v3.md`. Requested `claude-fable-5-1` at xhigh; observed "Fable 5.1" with `<reasoning_effort>80</reasoning_effort>`. NOT ACCEPTED: 0 P0, 1 P1, 10 P2 |
| Astra v3 review | `reviews/astra-max-v3.md` (session `01a0d0d9…`). Requested `gpt-6-astra` at max; the Codex header reports the same, which is CLI configuration, not proof of the serving model. NOT ACCEPTED: 0 P0, 3 P1, 4 P2 |
| v4 reviews (this revision answers them) | `reviews/astra-max-v4.md`: requested `gpt-6-astra-max`; **the reviewer could observe no model identity or effort and says so**, so no Astra identity is claimed. NOT ACCEPTED: 0 P0, 6 P1, 5 P2. `reviews/fable-5.1-xhigh-v4.md`: requested `claude-fable-5-xhigh`; observed "You are claude-fable-5-xhigh, a custom agent running in Amp", with no separate numeric effort visible. NOT ACCEPTED: 0 P0, 2 P1, 8 P2. Both reviewed plan sha256 `6102f850…`; this file is the revision that answers them, and the dispositions list every finding |
| Status | Neither review is acceptance. Acceptance belongs to the maintainer |
| Baseline [Coord] | `origin/main` = `d8dc848`; `v0.7.2` → `30b6033`, released. Released `references/`: 16 files, 173,472 B. Released `SKILL.md`: 10,743 B. M1 re-fetches and records the SHA it actually branches from |
| Host (tabputer-1) | **M0 passed** 2026-09-23: principals, containment, §4.4 GPU acceptance, B1–B15. `receipts/m0-tabputer-1-2026-09-23.md`. Containment code in `infra/`. Access from Amp is the runner `tabputer` (`/mnt/tst`, user `basit`, passwordless sudo) |
| Arithmetic | `calc/calc_v4.py` (stdlib, deterministic), output `calc/calc_v4.out.txt`. Their current sha256 values are recorded in `plan-v4-dispositions.md`, which is revised in the same commit, so the two never disagree. `calc_v3.py` is retained for the superseded normal-theory figures |
| Not used | Third-party runtime code, unreviewed installs, Colab, credentials on tabputer-1 |

**Evidence labels.** [C] contract; [R] reported (third-party); [Rep] reproduced by our own
execution; [H] hypothesis; [U] unknown; [Coord] observed by the coordinator and relayed.

## 0. What changed from v3

**This file was revised on 2026-09-24 after the two v4 reviews.** Every P1 either changed the
design or is answered in `plan-v4-dispositions.md`; the arithmetic was recomputed. The largest
changes are E3's loss range (2.4, not 1.2), one-sided power for non-inferiority, A2a inside the
M5 family, aggregate memory admission, candidate code on the GPU as D-b requires, and a weights
path that actually reaches run containers.

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
   - **Sampling assumption.** The theorem needs **independent** observations of the declared
     sampling unit. Equal inclusion probability alone does not give that: sampling one of two
     equal-size clusters uniformly gives every row equal inclusion probability, zero sample
     variance and zero coverage of the population mean (Astra v4 F7). The design lock names the
     independent unit; clustered or weighted designs are aggregated to that unit or refused as
     `unsupported_sampling_design`. Power is computed from the same unit.
   - **Why this and not v3's normal CI.** EB's coverage holds for any bounded independent-sample
     distribution,
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
4. **Isolation, scoped.** The evaluator, splits and confirmation labels are outside the
   proposer's read and write set **on this host**, as tested by E4c and B16(a). That is a
   host-path claim. It is **not** a claim that the proposer or a model rung is independent of the
   public benchmark's labels: B16(b) detects one named lookup-table fixture, and nothing detects
   memorization. **Contamination of public benchmarks is unresolved**, and it limits inferential
   eligibility: an artifact that had the labels is not made independent of them by being frozen,
   and measuring the benchmark exactly does not repair inference to the superpopulation. Every
   experiment reports this limitation beside its estimand (Astra v4 R2).

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
| P10 | The cheapest adequate **artifact form**, not the largest model, meets a bounded decision's policy | [Rep, arithmetic recomputed from RAP's frozen prediction files]: on RAP's **external** set of 160 author-constructed contrastive cases, bespoke lexical code reaches 0.993 rule-macro-F1; on its **controlled** set of 192 synthetic cases, the same code recalls only 0.771 and reaches 0.863 rule-macro-F1, where fine-tuned PAW reaches 1.000 recall and 0.961 rule-macro-F1. All of these cases are synthetic with labels fixed by construction, so they establish artifact-form ordering **on those cases only** | M5 (§3.3) |
| P11 | Programs lose on fuzzy real text | **[H]**, stated in advance so the M5 result is not read as a defect. RAP's synthetic contrast pairs cannot establish it (Astra v4 F10) | M5's T2a–c |

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
- **Powered set.** Three quantities are named separately and never conflated (Astra v4 F5):
  `true_delta` is the planning effect, `margin` is the test boundary, and the **gap**
  **signed distance** from the truth to that boundary is what the power calculation uses. The
  distance depends on the mode, so v4 writes it per mode rather than as one formula:
  non-inferiority (UCB < +margin) uses `margin − true_delta`; **superiority has two directions
  and they are not interchangeable** — a candidate-better read (UCB < −margin) uses
  `−margin − true_delta`, and an incumbent-better read such as M5's escalation row
  (LCB > +margin) uses `true_delta − margin`; equivalence at equality uses `margin` on each side.
  Taking an absolute value instead would silently accept the wrong direction (Astra v4 final R1).
  Each contrast's direction is fixed at the design lock, and a non-positive distance is a
  specification error, not a sample size. Equivalence and
  non-inferiority plan at `true_delta = 0`; superiority plans at the prespecified `true_delta`
  for that contrast type. **The power event matches the registered claim:** the
  two-sided equivalence event where the claim is equivalence, and the **one-sided** event
  `UCB < +margin` where the claim is non-inferiority. A contrast is powered if the n its method
  needs, at the **design-lock** `true_delta` and the analysis-lock σ̂, is at most the available n.
  Unpowered contrasts are reported with their intervals and count toward no outcome row in either
  direction. **"Powered" is per contrast**, so an outcome row quantified over tasks means powered
  for that row's own contrast (Fable v4 P2-7). **The rule is the computation, never a quoted
  σ̂ figure:** a contrast is powered iff its computed n at the observed σ̂ fits the available n.
  Every σ̂ threshold in this plan is a rounded-down illustration; the exact boundaries are
  0.24368057 (E3, m = 6), 0.26502213 (E3, m = 3) and 0.53538055 (M5 NI, K = 6, n = 60,000)
  [Rep calc §7b] (Astra v4 R6).
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
| Estimand | The superpopulation the corpus samples, at the declared independent unit (one comment). The exact finite-population Δ over the confirmation partition is reported beside every interval, so an enumerated quantity is never reported only as "unpowered" (Fable v4 P2-3). **Eligibility limit:** the instrument is a frozen MiniLM encoder plus a head we fit, so benchmark contamination is bounded here; where an arm embeds a pretrained generalist, the superpopulation reading is qualified by §2.4 item 4 |
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
| Population | HotpotQA distractor validation: CC-BY-SA-4.0, 7,405 hard questions [C, recheck]. Rounds read k ∈ {2, 4, 6} paragraphs and choose stop, expand or abstain. U = EM − λ·rounds/3 − μ·tokens/1000, **clipped to [−0.2, 1] at the design lock. Two utilities in an interval of width 1.2 differ by up to ±1.2, so the paired difference has range R = 2.4**; λ = 0.1 primary; μ fixed at the lock. **Estimand:** the superpopulation of questions the benchmark samples, not the enumerated 7,405; the exact finite-population Δ is reported beside every interval. **HotpotQA is public and the readers are pretrained, so the superpopulation reading carries the §2.4 item 4 contamination limit explicitly**; the finite-population Δ does not |
| Identification | Full-information replay: every answer at every k, so X5b holds by construction |
| Readers | Qwen3-1.7B and Qwen3-4B at pinned revisions, BF16, non-thinking, greedy. **Replay tables are generated once and frozen**, and every arm, resplit and P6 draw reads the same tables, so no claim depends on re-execution. The measured fact is a **59.8% per-prompt** batched-rerun identity rate [Rep]; the 0.0098 figure for a whole 9-call question is `0.598^9`, which assumes independence across calls **[H]**, not a measured joint law (Astra v4 F9, Fable v4 P2-8). M0's smoke test resubmitted the same prompt list and still disagreed, so a fixed input batch is not by itself a cure: the design lock records the batch-invariant setting used, and a 50-question check measures the realized rerun disagreement rate against a **pre-registered tolerance**, with a stated consequence (fall back to the frozen tables and report the rate) |
| Arms | (i) implicit prompt; (ii) threshold on LLM answerability; (iii) threshold on dense similarity; (iv) composite; (v) constants; (vi) proxy-selected threshold; (vii) outcome-selected threshold |
| Family (m = 6) | Per reader at λ = 0.1: best explicit − implicit; best explicit − best constant; (vii) − (vi). The best explicit arm is chosen on search and frozen |
| Margin | 0.02 utility (about 2 EM points), superiority and equivalence alike |
| n [Rep calc §3] | Search 1,000 questions (including a 100-question σ pilot and a 50-question timing pilot); confirmation the remaining 6,405. At R = 2.4, EB equivalence needs 5,181 at σ = 0.20, **6,598 at σ = 0.25 and 8,271 at σ = 0.30**, so at m = 6 the equivalence rows are powered only if **σ̂ ≤ 0.24**. The prespecified narrowing drops the 4B reader (m = 3), which needs 5,971 at σ = 0.25 and 7,501 at σ = 0.30: **powered only if σ̂ ≤ 0.26**. A true 0.04 gain is a gap of 0.02 beyond the 0.02 margin and needs 7,318 (m = 6) or 6,592 (m = 3) at σ = 0.30; a true 0.06 gain needs 2,498 or 2,243. These are **normal/fixed-SD planning approximations**, not finite-sample power guarantees: the acceptance interval is distribution-free, the power calculation is not |
| Calls | 9 per question per reader. **Full replay of all 7,405 is the planned workload**: 133,290 calls for two readers, 66,645 for the 1.7B-only narrowing (Astra v3 finding 4). At the measured 2,004 tok/s batched and 64 output tokens per call that is 1.2 and 0.6 GPU-h of decode [Rep calc §6]; prefill and the timing pilot govern the real figure |
| P6 population | The **6,405 confirmation questions**, which the search set never touched. Its finite-population truth uses their full replay (115,290 calls for two readers), and that truth is held by `augctl` and never exposed to selection |
| Cap and narrowing | 24 GPU-h for E3. If the timing pilot projects more, or if σ̂ > 0.24 at the analysis lock, the 4B reader is dropped before any confirmation read (m = 3). If σ̂ > 0.26 even then, the equivalence rows are declared **inconclusive** before confirmation; the superiority rows still run. The margin never changes, and the population is never enlarged after an outcome is seen |
| Outcomes per claim | *Explicit vs implicit* and *policy vs constants*: supported if the best explicit arm is superior by 0.02 for every powered reader; rejected if the two are equivalent for every powered reader; otherwise inconclusive. *P5*: (vii) superior to (vi) supports; equivalence rejects. *P6*: over 200 resplits, false adoption is judged against the 6,405-question truth. Incumbent–challenger lower than adopt-best, with the 95% CI of the difference excluding 0, supports |
| Controls | Identical frozen incumbent vs its copy: Δ ≡ 0, never adopted. A planted +0.05 utility shift on a replay copy must be adopted at its planned power. The per-question oracle is reported as headroom, not used as a control |

**E4: acceptance machinery.** Tests A and P6. Required. Fixture and simulation evidence only.

| Part | Design | Pass |
|---|---|---|
| E4a Monte Carlo diagnostic, **on the GPU** | **C = 108 cells**: `hoeffding` and `empirical_bernstein`, each 2 modes × n ∈ {300, 1,000, 2,500} × K ∈ {1, 5} × 4 loss distributions (three-point, two-point extreme, continuous, rare-large); plus `sign_exact` on the 2 binary distributions × 3 n × 2 K. **R = 40,000** replications at the boundary null. It is a vectorized reduction over at most 108 × 40,000 × 2,500 = 1.08e10 sampled losses, chunked at 2,000 replications × 2,500 (19.1 MiB fp32), 2,160 kernel batches [Rep calc §5]. The coverage *claim* rests on the theorems and exact-rational unit tests; this detects gross defects. **`sign_exact` cells stay exact-rational on the CPU**: their qualification is arithmetic, not sampling, which is the one recorded CPU step under D-b | Every cell's simultaneous (Bonferroni over 108, γ = 0.05) one-sided Clopper–Pearson upper bound ≤ α + τ = 0.055, i.e. at most **2,049** adoptions per cell [Rep calc §5]. A cell at 4.5% fails with probability 1.9e-9; an exactly nominal cell fails with 0.128; 6% is detected with probability ≈ 1. **Positive controls**, each naming its detecting cell **and that cell's own expected rate**, fixed at the design lock with the loss distribution, the margin and the assumed joint dependence (Astra v4 F11, Fable v4 P2-1). "Radius removed → size 0.50" is true only for a symmetric continuous single-finalist cell: the rare-large mean-zero cell at n = 300 adopts at 0.970444, the K = 5 any-of-five event at independent finalists is 0.96875, and `sign_exact` has no radius to remove, so it needs its own mutation (dropping the discordant-pair restriction) [Rep calc §5b]. Radius n inflated 100× → Hoeffding and EB cells at σ ≥ 0.3. Δ sign flipped → non-inferiority cells, at the margin/radius configurations where it is detectable; it is invisible to the size test in superiority mode. The planning effect per distribution is fixed at the design lock. Cap 1 GPU-h; exceeding it narrows to n ∈ {300, 1,000} |
| E4b Eligibility | Fixtures: teacher-labeled confirmation rows; synthetic text; unequal inclusion probabilities; the 50/950 case (−0.667 apparent vs +0.9 true); the sign case (p = 0.0068 while mean loss rises by 0.0292); **a zero-discordance rare-large case** | In order: `proxy_evidence_only`; `fixture_evidence_only`; `unsupported_sampling_design`; refused; `sign_exact` refuses non-binary input; the rare-large case returns `unpowered`, never equivalence |
| E4c Isolation (tabputer-1) | A scripted adversary harness plants each exploit with a canary. Hard-coded confirmation IDs → leak gate. Gold in synthetic rows → overlap audit. Sibling-run read → per-run container mounts. Evaluator or split edit → owned by `augctl` (EACCES) and hash drift. Read of confirmation labels → not mounted, EACCES on the host, **and B16's reconstruction attempt from every readable corpus**. Network exfiltration → `--network=none` plus the skuid drop. Write outside `/work` → EROFS. Disk exhaustion → ENOSPC on the `/work` tmpfs, with the host disk untouched (B17). Resource exhaustion → cgroup limits, GPU budget and timeout | Every exploit is refused by its named mechanism, and its canary proves the plant was active. A benign planted improvement is accepted end to end |
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
| Estimand and test | Δ = loss(low rung) − loss(R3a) in normalized cost. **One-sided** non-inferiority: EB UCB(Δ) < +0.01 over **K = 6** low rungs — R1, R2a, R2b, A1, **A2a** and A2b — at the family level. A2a is a tested arm, so it is inside the confirmatory family; leaving it out would allow escalation past an artifact form that met the same gate (Astra v4 F6, Fable v4 P2-7). The family is fixed at the design lock and never chosen after results. Escalation uses the matching **EB LCB(Δ) > +0.01 at the same α/(2K) tail** (Fable v3 P2-9). Tasks combine by intersection-union; R0 is a G0 exit, not a family member |
| n [Rep calc §4] | At equality with 80% power on the **one-sided NI event**, EB at K = 6 needs 6,354 rows (σ = 0.10), 12,698 (0.20) or 22,467 (0.30). (v4's first pass used the two-sided equivalence event, which is conservative for false positives but misclassifies powered tasks: 6,851 / 14,385 / 26,142. Astra v4 F5A.) Planned confirmation: T2a about 6,000 (powered only if σ̂ ≤ 0.09); T2b 12,850 (σ̂ ≤ 0.20); T2c 40,000, **expanded to 60,000 by the analysis-lock n(σ̂) rule, not by discretion** (σ̂ ≤ 0.53). Fable's estimate that a 77-way task disagreeing on 7% of rows has σ ≈ 0.26 makes T2a likely unpowered; the narrowed and inconclusive rows exist for exactly that. Planning approximations, as in E3 |
| Stop at a low rung | One low rung is non-inferior on every powered real task, and at least 2 tasks are powered. The recipe names the artifact form that sufficed and the task type |
| Narrowed | The same with only 1 powered task. The recipe names that task type only |
| Escalate | R3a superior to every low rung by more than 0.01 on a powered task |
| Workload-local | Mixed results across powered tasks |
| **Inconclusive** | Everything else, including no powered task. No rung recommendation: the default stays the procedure, and the recipe states that the 0.8.0 reproduction was inconclusive at 1 pp |

**Multimodal side ladder. A pilot runs in 0.8.0 (decision 9): M-R1 and M-R2 on one public image
task plus one code-rendered task, at 2B, after the M2 lock.** M-R3 and above stay documented and
untested. M-R0 don't train or route → M-R1 frozen VLM readout (candidate-letter logits in
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
| Teacher route | A teacher is used | Code-computed labels or a local open-weight teacher by default. A **named** hosted teacher passes, with its provider, model, revision, access channel and date recorded; an **unnamed** one is `unknown`, because there is nothing to record (decision 12) |
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

**Emitted decision servers (decision 13).** When the skill generates a `/v1/systemone`-shaped
endpoint, every response carries three declarations beside the number, and the skill refuses to
emit a server that cannot supply them:

- `confidence_convention`: `top_minus_mean_of_others`, `top_probability`, or a named other. There
  is no default, because a default is how the convention silently changes under a client.
- `calibration_status`: `calibrated(method, split, date)` or `uncalibrated`. An ordinal margin is
  never reported as a probability.
- `serving_precision`: the precision and quantization the calibration was fit at, which §3.4
  already binds the calibrator to.

Wire compatibility is not semantic compatibility, and the skill says so wherever it emits the
shape. This is the same failure the paper is about: the interface suggests the decision is
portable when the decision policy is not.

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
  abstention, never a commitment. **A headline computed as agreement with a teacher is labeled
  agreement and never reported as accuracy**, and it cannot support a margin when the same teacher
  family labeled the training rows (LaKun is the in-the-wild instance: 86.14% choice agreement
  against its own `qwen3.8-flash` labels [R]).
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
- **Hosted non-Jev teachers pass, with provenance recorded** (decision 12, maintainer
  2026-09-24). A named provider, model, revision and access channel are written to the graph and
  the run record, and nothing is gated on them. **0.8.0 checks no provider's terms except
  TypeSafe's, and the skill says so on every pass**: a recorded teacher is an audit trail, not a
  permission, and the user owns the terms question for their own provider. What is still refused
  is an *unnamed* teacher, because a corpus whose labeler cannot be identified cannot be
  re-audited later — that is `unknown` on missing parents, not a terms judgment.
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
| A corpus described by a third party as generic "LLM-teacher soft labels" whose declared parent is Jev (`SargeDev/jev-distill-corpus-v3`) | **Refused**, and so is anything inheriting from it. A description is not a lineage: the gate resolves declared parents, which is why `derived_from` is transitive |
| An evaluation record holding per-row Jev predictions (`dylantom2012/open-system-one-bench`) | **Recorded** where no edge reaches the training artifact; **refused** the moment one does. Comparison records are safe until they are joined |
| A trace log with no labeler field | `unknown` |
| Inputs synthesized by a **named** hosted provider at a stated revision, with human labels | Passes; provider, revision, channel and date recorded, with the "declared provenance only, no terms checked" note |
| The same with the provider or revision undisclosed | `unknown` on the input edge: nothing can be recorded |
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
| **S12a: EB one-sided NI, K = 3, margin 0.01, R = 2, observed mean 0.000, sd 0.10, 3,000 rows** | The EB radius is 0.014573, so UCB = 0.014573 > 0.01: **not certified**. The required n at equality is 5,691. The margin is not widened |
| **S12b: the same with sd 0.02** | Radius 0.009737, UCB 0.009737 < 0.01: **certified**. The skill must not refuse a feasible low-variance case |
| **S12c: the same as S12b but observed mean +0.005** | UCB 0.014737: **not certified**. Identical n and sd, opposite verdict, which is why a scenario must supply the observed mean and not only a planning assumption (Astra v4 F8) |
| S13–S15: Bayes threshold, prompt climb, tone fine-tune | Not triggered |
| **S16: an exact program already decides the family** | A0; no training, and no compile |
| **S17: a rule check runs after an irreversible effect** | Named as detection, not prevention; X2 unsatisfied |
| **S18: "give me a drop-in `/v1/systemone` server"** | Emitted, with `confidence_convention`, `calibration_status` and `serving_precision` declared in the response, and a stated warning that a client swapping backends inherits a different convention |
| **S19: the same, but the head is an uncalibrated contrastive margin** | Still emitted, with `calibration_status: uncalibrated` and the margin reported as ordinal. The skill refuses to call it a probability or to route on it as one |

The activation suite is opt-in, in `tests/plugin-evals/`, at most $10 per release candidate.

## 4. Compute and isolation

§4 describes the host **as M0 built and measured it**, not as v3 proposed it.

### 4.1 Hosts and roles

| Host | Used for | Never used for |
|---|---|---|
| Mac | Authoring; review; `make check`; Typst; serving a built site copy; delegate reviews | Experiments; model weights; candidate code; any isolation claim |
| tabputer-1 | Every experiment (E1, E3, E4, M5); third-party packages and weights; candidate code; the site build in a container | Holding credentials; isolation claims against root, the maintainer's account or privileged k3s workloads |
| Colab | The GPU fallback under D-b, per experiment, with public data and code only | Anything the maintainer has not approved for that experiment. Colab runs carry no B1–B20 claim |

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

**Acquisition and staging (Astra v3 finding 1; Fable v4 P1-B).** Acquisition uses **two separate
cache roots**, because weights and datasets need opposite treatment:

- `/srv/aug/quarantine/data` takes every dataset download and its HF dataset cache. At window
  close, `augwindow close` re-owns that tree to root with an ACL for `augctl` only, so `augexp`
  loses it. `augctl` then splits, hashes and publishes `/srv/aug/stage/parts/<partition-id>/`,
  root-owned and read-only: fit and calibration partitions with labels, **confirmation inputs with
  labels removed**, and nothing else.
- `/srv/aug/quarantine/weights` takes model weights, the base image layers and wheels. The split
  is enforced by **separate acquisition steps, each with its own complete cache environment**, not
  by one split of two variables. `HF_HUB_CACHE` holds the raw Hub files of *both* models and
  datasets, so pointing it at the weights root would put ordinary dataset downloads there and the
  close-time check would block W2 (Astra v4 final N1). Instead, a dataset step exports **both**
  `HF_HUB_CACHE` and `HF_DATASETS_CACHE` under `/srv/aug/quarantine/data`, and a weights step
  exports `HF_HUB_CACHE` under `/srv/aug/quarantine/weights`; each download also passes an
  explicit `cache_dir`. The two never run in one process, and `augwindow` refuses to close a
  window in which a dataset repository landed under the weights root. `augctl` then publishes an artifact only if
  (a) its digest matches the acquisition manifest entry recorded when the window opened, (b) its
  repository id is on the design lock's weights list, and (c) its file types are weights, configs
  and tokenizer files — no `.parquet`, `.arrow`, `.csv` or `.jsonl`, which is what a dataset
  arrives as. Publication goes to `/srv/aug/stage/weights/`, root-owned and read-only, which runs
  mount; that is how any model loads at all. The check is a **provenance and file-type check, not
  a semantic scan**: it cannot prove a weight file encodes no label, which is the memorization
  limit §4.6 already records.

Each run mounts only the partitions and weights the design lock entitles it to. **B16 searches
both trees**, so the separation is tested rather than assumed. Window close is a teardown, not a
rename: every acquisition process under `augexp` is stopped and its open descriptors are gone
before the re-own, and the receipt records that no `augexp` process survives the window
(Astra v4 F2). Complete labeled corpora never exist in any tree a candidate can read.

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
host is needed. `/stage` partitions and `/stage/weights` mount read-only. **`/work` is a sized tmpfs**
(`--mount type=tmpfs,destination=/work,tmpfs-size=...`), not a host bind mount, so the host disk
is never written by a run at all and there is nothing for a candidate to fill. A tmpfs is charged
to the container's memory cgroup, so `--memory=16g --memory-swap=16g` already bounds it: one
mechanism instead of two that can disagree. Persisted output goes to `/srv/aug/pred`, which is
small, append-only per run and owned through the `augpred` group. M0b first tried a loop-mounted
ext4 image for `/work`; its filesystem corrupted under the fill test (`EUCLEAN`) while the host
filesystem stayed healthy, which is a good reason not to run a second filesystem implementation
underneath the experiments. Each candidate gets its own container and `/work`.

**Candidate code runs on the GPU, but not by default on this host** (Astra v4 F4 and R3). v3
denied candidates GPU devices, which contradicts the binding D-b ("everything has to run on
GPU… including candidate and hill-climb code") and would have made GPU-dependent candidates
unreachable. But a candidate's GPU allocation **cannot be bounded on tabputer-1**: the declared
budget is a per-process allocator limit the candidate's own code can ignore, open a second
instance around, or allocate outside, and the watchdog is detection after the fact. Serialization
caps concurrency, not the sum. So:

- **Candidate and hill-climb GPU work runs on Colab** (decision 18, maintainer 2026-09-24), with
  public code and data only and no B1–B20 claim. The platform is fixed per experiment at its
  analysis lock.
- **B19 is answered: FAIL, and nothing is blocked.** M0b found `dmem` present in the root cgroup
  but **not delegated to augexp's user slice** [Rep, M0b], so a rootless container's GPU
  allocation cannot be bounded here without enabling a controller on slices that are not ours,
  which §4.1 forbids. Candidate GPU work therefore stays on Colab, as decision 18 already
  required. This is a measured answer, not an open question.

§4.6 records the residual cost: where B19 passes, `/dev/kfd` exposes the driver's attack surface
to candidate code, which the boundary does not claim to contain.

**GPU budget and aggregate admission (mandatory).** GPU memory is **not charged to the container
cgroup**: 24 GiB of bf16 tensors were held while `memory.current` stayed at 0.56 GiB [Rep, M0].
Every run declares its own GPU budget — `torch.cuda.set_per_process_memory_fraction` or vLLM
`gpu_memory_utilization` — recorded in its receipt. Planned budgets against 124 GiB visible
[Rep calc §6]: E1 MiniLM **8 GiB** (0.065); E3 readers 14 GiB (0.113); M5 R1 6 GiB (0.048); M5 PAW-ft
38 GiB (0.306); SetFit/DeBERTa 10 GiB (0.081). **E1's figure was 2 GiB and that was wrong**: a
MiniLM forward pass at batch 256 and length 256 hit `torch.OutOfMemoryError` inside the first
batch, with 812 MiB of the 2 GiB reserved but unallocated, so fragmentation as well as size. A
planning figure for activation memory is a guess until a forward pass disputes it.

**A fixed 24 GiB launch floor is not an admission rule** (Astra v4 F3): PAW-ft's 38 GiB GPU budget
plus a 16 GiB CPU cgroup, plus its teacher server, is well over 54 GiB of allowance on a UMA host,
so a compliant run could be admitted at 24 GiB and still exhaust memory. Admission is therefore
**aggregate**: a run launches only if

    MemAvailable ≥ GPU budget + CPU cap + declared service memory + 8 GiB overhead + 6 GiB reserve

**Service memory is declared separately and is never assumed to be inside a run's GPU budget.**
PAW-ft with a local teacher declares 38 GiB for the training job and 9 GiB for the vLLM teacher
server, so it needs 38 + 16 + 9 + 8 + 6 = **77 GiB** free. A run with no service declares 0, so
E3's readers need 14 + 16 + 0 + 8 + 6 = 44 GiB. The 24 GiB figure survives only as a floor below
which nothing launches at all.

**The declared budgets are allocator limits, not a GPU cgroup.** PyTorch's fraction bounds one
process's caching allocator; vLLM's utilization bounds one instance and can be overridden by an
explicit KV-cache size. Neither is adversary-resistant across processes. For **first-party** runs,
whose code we wrote and review, the budget plus aggregate admission, one run at a time and the
watchdog are adequate. For **candidate** code they are not, which is why candidate GPU work needs
B19 or Colab. §4.6 records this limit.

**The MemAvailable watchdog is real code**, not a note: the wrapper samples `/proc/meminfo` **every
500 ms** (fast enough that a bounded first-party allocation burst is caught between samples, which
B18 measures), refuses to launch when the aggregate check fails, and kills the container below the
6 GiB reserve, writing the reason into the run record.

**Egress.** The installed `inet augexp` nftables table matches `meta skuid` and never flushes the
ruleset. `augexp` (and its subuid range 165536–231071) may reach only `lo` TCP 3128, and only
during an open window; everything else is logged, counted and dropped. `augctl`: everything
dropped. `augproxy`: TCP 443 to public addresses plus the local DNS stub. Rootless podman's
user-mode networking runs as `augexp`, so a container started with `pasta` or `--network=host` by
mistake also reaches nothing (B10, verified).

**Three named download windows.** Each is maintainer-attended, opened and closed with
`sudo augwindow open|close`, followed by a B9/B10 re-run and a dated receipt. **No experiment or
candidate container runs while a proxy rule exists.**

**What a window does and does not govern.** A window controls `augexp`'s egress, through the nft
skuid rules and the proxy. It says nothing about the maintainer's own account fetching a git
checkout, which is ordinary host use and is not staged into any experiment. Conflating the two
stalled the first E1 fit attempt: "offline" was read as forbidding `git fetch` as `basit`, which
it never meant. An experiment container is offline because it runs `--network=none`, not because a
window is shut.

**A run mounts `/srv/aug/stage/weights` as well as its entitled partitions.** An embedder cannot
load from a tree that is not mounted, and weights are provisioning artifacts rather than labels.
`/srv/aug/ctl` and the quarantine roots are never mounted into a run.

| Window | When | What | Allowlist |
|---|---|---|---|
| W1 provisioning | M0, before the design lock | uv CPython, hashed wheels-only lock, the base image (local transfer), and the §4.4 acceptance weights (MiniLM, Qwen3-1.7B) | `pypi.org`, `files.pythonhosted.org`, `huggingface.co`, `us.aws.cdn.hf.co` (the last a recorded edit from the refusal log) |
| W2 experiment data | **After the M2 design lock** | CivilComments, CLINC150, BANKING77, HotpotQA; the M5 readers; PAW checkpoints if the PAW arm is locked in | The same, plus entries added only from the refusal log, each edit recorded. **Ran 2026-09-24**, 14:48:11–14:51:25 UTC, after the 14:45:35 lock commit. One edit: `api.github.com`, because HF's parquet conversion for BANKING77 404s and its pinned loader points upstream; the CSVs came from an immutable upstream commit and their hashes match HF's pinned `dataset_infos.json` |
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
| **B16** | **Confirmation-label reconstruction**, in two parts. (a) *On-host*: as `augexp`, inside a run container, search every readable tree, `/srv/aug/stage/weights` and both quarantine roots for the original labeled corpus; join stage inputs to any readable corpus by text, normalized text or identifier. A canary label is planted in the confirmation partition. (b) *Frozen-artifact* (Astra v4 F2): a first-party adversary proposer that **has** the public labeled corpus embeds a normalized-text-hash → label table in an A1 artifact, which is then frozen and run under the ordinary profile with no network and no corpus access | (a) every attempt fails and the canary appears in no candidate-readable output. (b) the embedded table is **detected** by the artifact audit — a frozen artifact carrying a label lookup keyed on confirmation text fails the overlap audit before scoring. The plan does not claim that it is prevented; see §4.6 |
| **B17** | **Disk exhaustion.** Fill `/work` past its tmpfs size from inside the container, with idle host drift measured as a control | Three conditions, because "host free space unchanged" is not achievable on a host that also runs k3s, docker and journald: (a) `df` inside shows `tmpfs` on `/work`; (b) the fill hits ENOSPC at the declared size; (c) the host free-space movement during the fill sits **within measured idle drift** and nowhere near the volume written. M0b measured idle drift of 0.85–1.72 GiB per 30 s (Fable v3 P2-5) |
| **B18** | **GPU budget, admission and burst.** (a) A run exceeding its declared GPU budget. (b) A launch attempt whose aggregate requirement exceeds MemAvailable, tested by **mocking the `/proc/meminfo` reading**, never by consuming host memory (Fable v4 P2-4). (c) A bounded first-party allocation burst toward a raised test floor, to measure kill latency against the 500 ms sampling cadence | (a) the allocator limit aborts the allocation. (b) admission refuses, naming the shortfall. (c) the watchdog kills the container before the reserve is crossed, and the measured latency is recorded. A failure here narrows the affected arm or moves it to Colab; the host is never deliberately driven to OOM |

| **B20** | **GPU hang response, tested by fixture.** The wrapper's heartbeat and fault path are exercised with **injected** stalls and synthetic amdgpu error records — a run that stops emitting heartbeats, and a fabricated driver-error line. **The GPU is never deliberately wedged**: a memory budget does not contain an execution hang, and inducing one endangers the maintainer's other workloads on a shared host (Astra v4 final N2). A genuine device-wedge test needs authorized disposable hardware | The wrapper detects the stall, kills the container and records `blocked(gpu_fault)`. **The record carries wrapper observations only.** M0b measured `kernel.dmesg_restrict` on this host: `augexp` gets `Operation not permitted` reading the ring buffer [Rep], so a fault record cannot carry verified kernel context, and the plan does not change a sysctl to obtain it. The recovery policy is unchanged and **not validated by this fixture**: no `amdgpu` module reload, no GPU reset command and no reboot. If a real device does not recover, the run is abandoned and the maintainer decides at the console; the affected arm moves to Colab (Fable v4 delta P2-3) |
| **B19** | **Can a candidate's GPU allocation be bounded?** Apply a `dmem` cgroup limit to a rootless container and allocate past it, first-party. Measure whether amdgpu GTT is charged and capped | The allocation fails at the limit and host MemAvailable is unaffected. **If it does not, candidate GPU work moves to Colab** and candidates on this host get no devices (Astra v4 R3) |

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
| Windows W1–W3 + B1–B20 | About 45 GB of downloads | Network-bound | 0.5–1 day, attended | — |
| E4a | 4.32M replications, 1.08e10 sampled losses, chunked | [H] 2e8–2e9 elements/s | 0.1–0.9 min, cap 1 GPU-h | 4 GiB (aggregate admission 34 GiB) |
| E1 | Embed about 2.1M texts; fit arms; 38 intervals; 200 control redraws | MiniLM measured 2.1 s per 1,000 on GPU [Rep] | ≤ 2 h, cap 6 h | 2 GiB |
| E3 | 133,290 calls (66,645 narrowed) | Measured vLLM 2,004 tok/s batched [Rep] | 1.2 GPU-h of decode plus prefill; the timing pilot governs; cap 24 GPU-h | 14 GiB |
| M5 | R1 readout; SetFit; A1; PAW-standard compile; PAW-ft; optional R3b | [H], pilots replace it | cap 24 GPU-h | 6–38 GiB (PAW-ft's aggregate admission is 68 GiB) |
| Site build | One github-pages 232 build in a container | — | Minutes | — |

**Envelope.** One run at a time; `--memory=16g --memory-swap=16g`; an explicit GPU budget per run;
launch only at MemAvailable ≥ 24 GiB; abort below 6 GiB. At 18:38 MDT on 2026-09-23 MemAvailable
was 121,366,040 kB of 131,007,996 kB [Coord], so nothing is `blocked(memory)` on a stale note;
the state is derived from the launch measurement.

### 4.6 What is not claimed

- No protection against tabputer-1's root, the maintainer's root-equivalent account, privileged or
  hostPath k3s workloads, kernel or GPU-driver exploits, or side channels.
- `/dev/kfd` and `/dev/dri/renderD128` are mode 0666 host-wide, so `render` membership is not a
  control. Candidate containers get the devices only if B19 shows the allocation can be bounded;
  otherwise their GPU work goes to Colab (§4.2). Where they do get them, the driver's attack
  surface is exposed to candidate code and the boundary does not claim to contain it.
- New world-readable trees created later by other workloads are covered only when B4 and B5 are
  rerun.
- The proxy binds SNI to the CONNECT host, but tunnel contents after the ClientHello are not
  inspected: **domain fronting through a CDN that permits a Host header differing from SNI is not
  prevented.**
- **`dmem` does not bound amdgpu GTT here.** M0b measured it present in the root cgroup's
  controllers and absent from `augexp`'s user slice [Rep], so it is not delegated and enabling it
  elsewhere would touch slices §4.1 forbids. The GPU budget and the MemAvailable watchdog are what
  stand in for it, for first-party code only.
- **A GPU-fault record has no kernel context.** `kernel.dmesg_restrict` denies `augexp` the ring
  buffer, so `blocked(gpu_fault)` is a wrapper-side observation and nothing more.
- A run writes nothing to the host disk, because `/work` is a tmpfs. The host filesystem's own
  health is outside this boundary: M0b observed a nonzero btrfs `corruption_errs` counter on the
  root filesystem that predates this boot, and whether to scrub is the maintainer's decision.
- **Filesystem custody prevents label exfiltration from this host; it cannot make public
  benchmark labels secret.** CLINC150, BANKING77, CivilComments and HotpotQA are public, so a
  model rung's pretraining, or a proposer that read the corpus before freezing an artifact, can
  reproduce labels having read no file here. B16(b) detects an embedded lookup table; nothing
  prevents memorization. **Contamination is therefore unresolved and it limits inferential
  eligibility** (§2.4 item 4). The earlier rationale that "the declared population is the
  benchmark" is **withdrawn**: E1 and E3 declare superpopulation estimands, and measuring the
  benchmark exactly does not repair inference to them (Astra v4 F2 and final R2, Fable v4 P2-6).
- **The GPU budgets are allocator limits, not a GPU cgroup.** They bound first-party code, which
  we wrote and review. They do not bound candidate code, which is why candidate GPU work requires
  B19's `dmem` result or Colab.
- The Mac provides no isolation. Colab provides none of these claims.
- "Sandbox" means exactly the mechanisms B1–B20 test, rerun after any system update.

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
| M0b | B16–B20; the quarantine-and-split custody path; the MemAvailable watchdog; the GPU-budget wrapper | M0 | 1 | A dated receipt showing B16–B20 pass |
| M1 | Skeleton (`0.8.0-dev`, `.gitignore`); generalized `check_repo`; modes, methods, `loss_bound` and design check; ledger and provenance graph; overlap audit; climb ledger. **Small PRs, at most 500 changed lines and 15 files each** | M0 decisions | 4–5 | `make check` green, with the CONTRIBUTING numerical tests |
| M2 | Design locks for E1, E3, E4 and M5, including each loss range R, each `true_delta`, and the PAW/A1/A2a arms; BANKING77 provenance check **from cards, papers and metadata only** — no dataset text or labels are read before the lock, and any check that would need rows moves after it with a prespecified abort rule (Fable v4 P2-2) | **M0 decisions only** | 1 | Hashed **before window W2 opens** |
| M2b | Window W2: experiment datasets and M5 readers; B9/B10 re-run; receipt | M2, M0b | 0.5 | Dated window receipt, proxy closed |
| M3 | E4a–c (E4d optional); T1 generator with fact–text binding | M1, M2b, B1–B20 | 2 | E4 criteria met |
| M4 | E1, then E3, each with its analysis lock before confirmation | M3; §4.4 parity checks for E3 | 2 + 1–2 days of compute | Results against each lock, inconclusive rows included |
| M5 | Trainer reproduction: R0, A1, A2a, A2b, R1, R2a, R2b vs R3a (R3b if parity passes) | M1, M3; Qwen3.5 and PAW parity | 3–4 | §3.3 rule applied, including inconclusive |
| M5b | **Multimodal pilot** (decision 9): M-R1 and M-R2 on Qwen3-VL-2B, one public image task plus one code-rendered task, with the blind-arm gate and the VLM parity receipt | M2, M5 | 1–2 | F1 and F4 applied; "not a media decision" is a valid outcome. Does not gate the release |
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
| GPU nondeterminism (59.8% per-prompt batched-rerun identity [Rep]) | **Frozen once-generated replay tables** that every arm, resplit and P6 draw reads, so no claim depends on re-execution. The batch-invariant setting is recorded at the lock, a 50-question check measures the realized rate against a pre-registered tolerance, and the joint whole-question figure stays **[H]** |
| gfx1151 kernel gaps (Qwen3.5 FLA, PAW, VLM) | Parity checks before the arm; Colab fallback, never CPU |
| A rolling CachyOS update mid-study | Versions in every receipt; updates held during windows; B1–B20 and §4.4 rerun after an update |
| A candidate reconstructs confirmation labels | Quarantine custody, label-free confirmation inputs, B16 |
| A candidate fills the shared disk | Size-bounded run filesystem, B17 |
| Isolation overclaimed | Claims limited to B1–B20; §4.6, including the memorization and allocator-limit non-claims |
| A GPU-holding candidate attacks the driver | Accepted and recorded as a non-claim; it is the price of D-b. One run at a time, no network, per-run `/work`, aggregate admission |
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
| 1 | Name and slug | **DECIDED** (maintainer, 2026-09-24): "When the Model Is Not the Policy", subtitle naming the test and acceptance; slug `exogenous-policy`. ExoPO stays a description in the text, not a method name in the title, because E1 has not reported |
| 2 | Type and venue | A position paper with executed E1, plus E3 and E4; Pages first |
| 3 | E2 (CC BY-NC-SA) | Skip in 0.8.0 |
| 4 | Packaging | A second skill in the augustus plugin, with the 10% switch rule |
| 5 | Confirmation sampling | Equal-probability only in 0.8.0 |
| 6 | Pre-registration custody | Design and analysis locks: hashes plus your dated note in `research/080/prereg/`, read-only copies under `augctl` |
| 7 | Paper typography | **DECIDED** (maintainer, 2026-09-24): STIX Two Text and Math for body and math, Geist for heads, tables and labels. The M8 A/B against all-Geist is run on **a math page and a table page only**, which is where it is decided |
| 8 | **PAW arms** | Run A2a and A2b locally (local compiler, local teacher). Hosted compile stays unused unless the local path fails on gfx1151, and then only with public examples |
| 9 | **Multimodal pilot in 0.8.0?** | **DECIDED: yes** (maintainer, 2026-09-24). M-R1 and M-R2 on one public image task plus one code-rendered task, after the M2 lock, under the blind-arm gate F1 and the per-type rule F4. It is a **pilot**: it can end at "not a media decision", and it does not gate the release |
| 10 | **Container cap for a 4B VLM or an audio LoRA** | **DECIDED: no** (maintainer, 2026-09-24). The 16 GB CPU cgroup and declared GPU budgets stand, so audio stays at M-R2 and the VLM pilot stays at 2B |
| 11 | **One backbone or two for text R1 and M-R1** | **DECIDED: two** (maintainer, 2026-09-24). Qwen3.5-2B for text R1, Qwen3-VL-2B for media, each with its own parity receipt. If the Qwen3.5 linear-attention parity check fails, Qwen3-1.7B becomes R1 and the media backbone is unaffected |
| 12 | **Hosted non-Jev teachers** | **DECIDED: pass them through with provenance recorded, no gate** (maintainer, 2026-09-24, option C). Only TypeSafe's terms are encoded, because D-d requires it; no other provider's terms are read or asserted. **Accepted consequence, recorded rather than hidden:** the provenance gate now fires on exactly two things — a Jev-generated training corpus (refused by default, user-overridable) and missing or disputed lineage. It is not a general terms checker, and the skill must not present it as one |
| 13 | **The `/v1/systemone` wire format** | **DECIDED: emit it when the user asks for a drop-in** (maintainer, 2026-09-24), because refusing a shape 210 sweep items already use is precious. **But the semantics do not travel with the shape**, so an emitted response must declare its `confidence` convention, its calibration status and the precision it was calibrated at (§3.5). Evidence: three conventions already ship under one field name — TypeSafe Jev and CLM use top probability minus the mean of the others, Jev-Omni uses top probability [R], and several sweep items use an entropy-derived number, which the climb ledger rejects outright. CLM's is uncalibrated by construction, since InfoNCE fits retrieval rank and not class posteriors [R]. A client swapping backends therefore gets a working HTTP call and a silently different number driving its threshold |
| 14 | Activation spend | **DECIDED: at most $20 per release candidate** (maintainer, 2026-09-24), still per RC rather than per PR. A run that would exceed it stops at `paused_budget` and reports what it did not cover, rather than silently sampling less |
| 15 | Scoop timebox | Reframe, don't restart; decide by 2026-11-15 |
| 16 | Site placement | Standalone layout under `docs/exogenous-policy/`; the PDF in the sitemap |
| 17 | Paper gates the release? | No |
| 18b | **A paid Colab tier?** | **Not yet, and not speculatively.** The maintainer has offered one. Nothing currently queued needs it: first-party experiments, the PAW-ft 38 GiB job and the M5b multimodal pilot all stay on tabputer-1, and the Colab lane carries only candidate and hill-climb code, which is small heads and programs. Decide at M5's timing pilot, which is the first measurement of climb rounds and per-round wall clock. **Buy a paid tier when any of these is observed, not before:** a climb round is cut off by a session limit, background execution is needed to finish a bounded round, or a candidate genuinely needs more device memory than the free tier allocates. Until then the free tier is the assumption, and a Colab run that cannot finish is recorded as `paused_budget`, never as a result |
| 18 | Colab | **DECIDED: Colab-first for candidate and hill-climb GPU work** (maintainer, 2026-09-24: "colab first is fine, honestly… everything is cuda anyway"). Public data and code only. B19's `dmem` result is then an optimization, not a prerequisite: if it passes, local candidate runs become available; if it fails, nothing is blocked. First-party experiment runs stay on tabputer-1 |

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
| 56 | `calc/calc_v4.py` and `calc/calc_v4.out.txt`; current digests in `plan-v4-dispositions.md` | This lane | Executed | Rep (arithmetic; synthetic populations [H]) |

v3 sources 43–48 carry over. v3's P1 percentages (+154% / +364%) are **withdrawn** and replaced by
source 56's +95% / +216% / +553%. v3's normal-theory family CI is **superseded** by §2.4.
