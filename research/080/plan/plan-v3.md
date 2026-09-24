# Augustus 0.8.0 plan (v3)

**Confidential and local only.** Nothing has been pushed, posted or filed. This version supersedes
`plan-v2.md`. Each v2 re-review finding is dispositioned in `plan-v3-dispositions.md`.

**Provenance**

| Item | Record |
|---|---|
| Author | Revision lane, 2026-09-23. Observed identity: Opus 5.5 (`claude-opus-5-5[1m]`). No requested routing was stated to this lane |
| Fable v2 review | `reviews/fable-5.1-xhigh-v2.md`. Requested `claude-fable-5-1` at xhigh; observed "Fable 5.1"; effort unknown |
| Astra v2 review | Final `codex` block of `reviews/astra-max-v2.raw.log` (session `01a0cf9f…`). Requested `gpt-6-astra` at max. The Codex header reports `gpt-6-astra`, effort max, read-only sandbox: CLI configuration, not proof of the serving model. It contains 8 numbered findings (1 P0, 5 P1, 2 P2) |
| Status | Neither review is acceptance. Acceptance belongs to the maintainer |
| Baseline [Coord, 2026-09-23] | `origin/main` = `d8dc848` (hourly folds §167 and §168 landed after 0.7.2). `v0.7.2` → `30b6033`, released. Released `references/`: 16 files, 173,472 B (6,528 B below the 180,000 B cap). Released `SKILL.md`: 10,743 B. The `.local/` ignore exists only in `.git/info/exclude`. No published tag changes under this plan |
| Mac [Coord] | MacBook Air M4, 24 GB. Home 700; `~/.zshrc` 600; `~/.cache/huggingface/token` 600; `~/.codex` and `Augustus/.local` recursively go-rwx. A second admin account (uid 501) can sudo-read everything, so **no isolation claim rests on the Mac** |
| tabputer-1 [Coord] | CachyOS (Linux 7.2, rolling). Ryzen AI MAX+ 395 (32 threads). Radeon 8060S iGPU (gfx1151), ROCm present (`/opt/rocm`, `/dev/kfd`). About 124 GB RAM, up to about 133 GB GPU-addressable GTT. 688 GB free on a LUKS disk. Python 3.14.7, uv, rootless-capable podman, docker, ollama. The maintainer's user has passwordless sudo and is in `docker` and `wheel` (root-equivalent). ufw is active. k3s and other workloads hold about 108 GB of RAM today. No PyTorch |
| Maintainer decisions [Coord] | (1) The unattended patrol is **dropped** from 0.8.0; patrols stay manual (§5.2). (2) Experiments are sized to available compute, with an explicit prespecified **inconclusive** outcome; margins are never moved to manufacture a result |
| Checks by this lane | Local refs only, not fetched: `origin/main` = `d8dc848`; `v0.7.2^{commit}` = `30b6033`; byte sums at `v0.7.2`; `.gitignore` at `origin/main` lacks `.local/`. Arithmetic: `calc/calc_v3.py` (stdlib, deterministic), output in `calc/calc_v3.out.txt`. v2's `calc_v2.py` and Fable's appendix script were copied from the ephemeral scratchpad into `calc/` (sha256 `5d3a6d23…` and `e75b6308…`) |
| Not used | Third-party code, installs, network, SSH |

**Evidence labels.** [C] contract; [R] reported (third-party); [Rep] reproduced by our own execution
(so far: arithmetic, synthetic populations, fixtures, local observations); [H] hypothesis; [U]
unknown; [Coord] observed by the coordinator and relayed to this lane.

## 0. What changed from v2

1. **Execution moves to tabputer-1.** Every experiment, every third-party package, all model
   weights and any candidate or unreviewed LLM-authored code run there, under unprivileged users,
   inside rootless podman. Candidate code runs with `--network=none`. Setup downloads pass an
   nftables owner-match policy that allows only named hosts; the policy is then closed. Boundary
   tests must pass before any run (§4). The Mac is used for authoring and review only. The Mac
   users `augpatrol` and `augcand` are deleted from the plan.
2. **The patrol pilot is removed.** It is deferred with its prerequisites (§5.2).
3. **Sample sizes are recomputed** with the actual method, margin, family size and power (§2.7,
   `calc/calc_v3.py`). E1 is reachable because it now uses the full CivilComments data. M5 gains
   real-text tasks large enough for its margin. Anything still unreachable has a prespecified
   inconclusive or narrowed outcome.
4. **Controls are machinery controls.** They use planted, analytically known effects and identical
   frozen policies. Stale-threshold and independent-fit comparisons become experimental outcomes.
5. **E4a qualifies against a declared tolerance** with simultaneous upper bounds. Planted defects
   prove that it can fail.
6. **Pre-registration has two locks**: a design lock and an analysis lock (§2.7).
7. **Baseline refreshed** to the coordinator's facts. 0.7.2 is done. The `.gitignore` change has a
   concrete vehicle (decision 13).
8. **Decisions updated.** Resolved ones are dropped; tabputer-1 provisioning, memory, the ROCm
   wheel and Colab are added.

## 1. Goals and non-goals

**Goals.**

- **G1. Paper.** A per-action-family test for where an acting agent's decision policy belongs, and a
  protocol for accepting changes to it. At least one executed, pre-registered falsifier (E1),
  reported whatever the result, inconclusive included.
- **G2. Trainer.** `augustus-train`: a gated path from "don't train" to the cheapest rung that meets
  the workload's own acceptance policy.
- **G3. Tooling.** Confirmation modes and methods; a ledger with a provenance graph; a fail-closed
  overlap audit; a climb ledger; bibliography and claim gates.
- **G4. Design.** A restrained typeset paper, and a project site whose explorables each test one
  claim.

**Non-goals.**

- Publishing of any kind.
- Hosted or paid search, or paid compute without a decision.
- Claiming the architecture as novel, or selecting recipes by leaderboard rank.
- Training 9–27B generalists, or DPO/RLHF by default.
- Autonomous paper writing, or a third-party loop runtime.
- Unattended patrols.
- GitHub Actions.
- Jev output in any training path.

## 2. Paper

### 2.1 Position

A decision policy outside the weights, with LLMs as instruments, is already published.
Confidence-gated acceptance is classical. The paper claims neither. It contributes four things,
all [H] until E1, E3 and E4 report:

- the test in §2.3;
- an instrument/decision/authority vocabulary;
- the acceptance protocol in §2.4;
- the executed experiments.

Durability is claimed only for commitments (costs, authority, acceptance). It is not claimed for
scaffolding, which models absorb (2609.03141v1 [R]).

| Work | Already establishes | Leaves open |
|---|---|---|
| Sun, 2604.00414v1 | Signals separated from a deterministic δ(c) = argmax U | Preset thresholds; no acceptance on untouched data; no authority; no test of when *not* to separate; no always-expand baseline [H] |
| Papamarkou et al., 2605.00742v2 | Bayes-consistent controller; LLM observation models judged by calibration and utility | Position only; Bayesian-specific; no authority or acceptance |
| FABLE, 2608.00215v1 | Exogenous per-user layer, feasible set, anytime-valid false-promotion control | Personalization only; bandit-learned policy. **Closest on acceptance:** the paper compares against its promotion rule |
| Externalization, 2604.08224v1 §7.3 | Qualitative trade-offs | No measurable conditions or falsifiers |
| CaMeL, Progent, CapScope 2609.08371, AI control 2312.06942 | Enforcement outside the model (CapScope 33–47/75 vs 3/75 injected effects [R]) | Cost-derived thresholds. Cited, not claimed |
| HCPI, Seldonian NSF, SPIBB, CSPI-MT, LTT/CRC | Confidence-gated acceptance; "No Solution Found" | Evaluator isolation from the proposer; identification when actions change outcomes |
| LLM-Modulo 2402.01817; 2605.14744 | External verifiers and gates | Argue from incapability. Illustration only |

### 2.2 Definitions

The decision point for each action family is `(A, x, s(x), c, G, h)`. The paper separates three
properties.

- **Ownership:** who sets c, G and h, and whether they are versioned inputs.
- **Implementation:** closed-form, or learned (allowed if c and G enter at decision time).
- **Enforcement:** G is checked before the effect.

Trusted control inputs are c, G, the handler models, the rule version, and instrument outputs s(x)
under a versioned score contract. Raw x, retrieved text and tool output are untrusted.

δ is **executively exogenous** when three conditions hold: its parameters are owned and versioned;
it reads only trusted inputs; and G is enforced before effects.

**E1 arm classes, fixed at the design lock:**

| Arm | Definition | Class |
|---|---|---|
| A | Plug-in threshold C_FP/(C_FP+C_FN) on temperature-calibrated scores | Exogenous, closed-form |
| A_tuned | Threshold tuned per ratio on the calibration split | Exogenous parameter, tuned closed-form (descriptive only) |
| A-raw, A-recal | Under shift S: re-threshold only; or re-estimate the intercept from 200 deployment-prior labels, then re-threshold | Exogenous |
| B-stale | The 1:1-trained head at its own rule, which equals the plug-in frozen at 0.5 on the same scores | Endogenous, fixed cost |
| B-retrain_r | Cost-weighted head retrained on the fit data at ratio r | Endogenous, retrained per cost |
| B-retrain_S | Fit data importance-reweighted to the new prior, plus the same 200 labels, retrained at the S cost | Endogenous; the strongest cheap retrain |
| C, C\*, E | MLP given the raw ratio; logistic head given log(C_FP/C_FN) with a free coefficient; contextual-bandit policy gradient with c as input | Exogenous parameter, learned implementation |

### 2.3 The operational test

X2 is a commitment [C]. The other rows stay [H] until their falsifiers run. Each predicate
returns *holds*, *fails* or *unknown*. The principal sets every ε.

| Id | Holds when | If unknown | Rule | Counterexample | Falsifier → consequence |
|---|---|---|---|---|---|
| X1 Cost heterogeneity | Δ_c > ε_c (share of plug-in actions that flip across the plausible cost set), and costs change faster than retrain plus requalify | Measure Δ_c from scores and the cost set | c and thresholds are decision-time inputs | Stable population preference; act-all 0.698 vs threshold 1.369 [Rep toy] | E1: B-stale equivalent to A at every powered ratio, or B-retrain superior to A (or to A-recal under S) by more than δ → narrow or drop X1 for the task |
| X2 Effects and authority [C] | Effects outside a sandbox, delegated grants, no recoverable region, or attacker-writable input | Holds | Enforce G before the effect, with recovery. Never optimize G | Reversible sandboxed drafting | Sub-claim only: a gate with recovery lowers safe task success at a matched unauthorized-effect rate and workflow cost → "better recovery", never "no gate" |
| X3 Instrument churn | At least two instruments of differing reliability, or change faster than retraining, and requalification is measured cheaper | Estimate both costs | Per-instrument score contracts | One stable instrument (Mozannar–Sontag §5.1) | E2: joint L2D wins by more than the margin before and after a swap, at no greater adaptation cost → drop X3 |
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

### 2.4 The acceptance protocol

Four tests are reported separately. Any one of them can fail.

1. **Statistical support.** Mode, margin, α and method are fixed before confirmation. Δ =
   candidate loss − incumbent loss, so negative is better.
   - `hoeffding` and `empirical_bernstein` return a one-sided UCB(Δ) at α/K over K frozen
     finalists. Superiority holds when UCB < −m (m ≥ 0). Non-inferiority holds when UCB < +m_NI.
   - `sign_exact` has no UCB. Its rule: losses are in {0, 1}; m = 0; the one-sided exact binomial
     p on discordant pairs is ≤ α/K. It certifies direction only.
   - "Retain incumbent" is a first-class result.
2. **Eligibility.** `evidence_kind` is derived from provenance; the weakest source wins. Proxy or
   fixture evidence cannot support a margin.
3. **Identification.** X5b holds.
4. **Isolation.** The evaluator, splits and confirmation data are outside the proposer's read and
   write set, as tested by E4c.

Baselines always include constant policies and per-case-best headroom. The paper names what it
imports from HCPI, CSPI-MT and FABLE.

### 2.5 Preference and outcome optimization

**H-DPO [H].** Where X1, X2 or X6 holds, a system whose c and G are decision-time inputs has lower
change cost and a shorter audit path than an action policy trained by DPO, KTO or GRPO on
fixed-cost data, at non-inferior complete-episode loss.

GRPO and outcome RL also optimize episode outcomes; the claimed difference is where c and G live
and how changes are accepted. KTO is the strongest competitor for binary outcomes.
Preference-trained proposers and decision-trained instruments may sit inside the envelope.

Endogenous preference optimization is the right tool when all four of these hold: the output
distribution is the deliverable; there is no principal-specific cost matrix; there is no delegated
authority or irreversible effect; and preferences are stable relative to retraining.

Learning the action policy directly is favored by stable costs, dense identified outcomes,
insufficient exposed signals, and a direct policy that wins on untouched episode loss at equal
change and audit cost. E1's arm E is one small instance; nothing is generalized from it.

### 2.6 Claims and evidence

| # | Claim | Evidence now | Upgraded by |
|---|---|---|---|
| P1 | A stale threshold regrets heavily under cost shift: +154% at 1:9, +364% at 1:19 | Theory; [Rep] synthetic | E1: A vs B-stale |
| P2 | A fixed-cost head loses off its ratio; retraining per ratio and cost-conditioned heads are measured, not assumed | [H] | E1: B-retrain, C, C\*, E |
| P3 | Authority is a pre-effect contract | [C]; CapScope and the verifier tax [R] | Cited |
| P4 | Exogenous deferral adapts more cheaply after a handler change | [H] | E2 (optional) |
| P5 | Episode-level selection beats proxy selection | [H]; GEPA p = 0.29 [R] | E3 |
| P6 | Untouched incumbent–challenger lowers false adoption | [Rep sim] −1.8 vs −0.26 pp; AIRA-dojo is motivation only | E3, E4a |
| P7 | Learn utilities, not policies | [H], discussion only | — |
| P8 | Well-designed research loops keep acceptance exogenous | [C], motivation | E4 |
| P9 | Under prior shift, recalibrate-and-rethreshold is non-inferior to retraining at equal labels | [H] | E1-S |

### 2.7 Experiments

**Common rules**

- **Two locks.** Both are hashed and dated in `research/080/prereg/`, with read-only copies in
  `/srv/aug/ctl/` on tabputer-1.
  - The **design lock** comes before any download or data read. It fixes the estimands, the arms
    (encoding, model class, tuning budget, calibration), controls, margin *rules*, family and m,
    α = 0.05, power 0.8, CI method, seeds, split proportions, n rules, the powered-set rule, caps
    and outcome rows.
  - The **analysis lock** comes after fitting, calibration and pilots, and before any
    confirmation read. It records the split-manifest hashes, σ̂ per contrast, the numeric margins,
    the required n, the powered set, the allocation of n, the hashes of the frozen arms, and any
    prespecified narrowing.
  - The grader (`augctl`, §4.2) refuses to score confirmation data unless the analysis-lock hash
    is present and matches.
- **Family rule.** Each contrast gets a two-sided (1 − α/m) CI, with critical value
  z₁₋α/(2m). Superiority, inferiority, non-inferiority and equivalence are all read from that CI,
  so the probability of any false claim across the m contrasts is at most α.
  - The interval is normal-theory on paired per-case differences.
  - A contrast with fewer than 500 discordant cases also gets a paired percentile bootstrap
    (B = 10,000), and the wider of the two intervals is used.
- **n formulas** (80% power, stated once; the full derivation is in `calc_v3.py`):
  - equivalence at true Δ = 0: n = ((z₁₋α/(2m) + z₀.₉)·σ/δ)²;
  - one-sided non-inferiority or superiority with gap g between the truth and the bound:
    n = ((z₁₋α/(2m) + z₀.₈)·σ/g)².
- **Powered set.** A contrast is powered if its required n (from σ̂) is at most the available n.
  Unpowered contrasts are reported with their CIs, but they count toward no outcome row in either
  direction.
- **Margins** are fixed by substantive rationale at the design lock. They are never widened (which
  manufactures equivalence) or narrowed (which manufactures superiority) after an n requirement is
  seen. If compute or data bind, the prespecified narrowing or inconclusive row applies.
- **Controls test machinery only.** There are two kinds: an identical frozen policy loaded through
  the full pipeline (Δ ≡ 0), and planted effects whose value is known analytically. A failed
  control is a pipeline fault. Comparisons between genuinely different policies are outcomes.
- "Supports" requires significant pre-registered results. "Not rejected" never counts as support.

**E1: cost shift and prior shift.** Tests X1, P1, P2 and P9. Required. Runs on tabputer-1.

| Field | Specification |
|---|---|
| Data | **Primary family: CivilComments.** CC0; toxicity ≥ 0.5; about 2.0M rows over all splits [C, recheck]. Exact-normalized-text dedup across partitions. Seeded partitions: fit 200k; calibration 100k; M5 pool 100k (§3.3); confirmation the rest, about 1.6M. **Secondary family: CLINC150** (CC-BY-3.0; crowdsourced, human-written, not sampled traffic): about 23.9k rows resplit into fit 8k, calibration 3k and confirmation about 12.85k |
| Instrument | Frozen all-MiniLM-L6-v2 (pinned sha) plus logistic regression, temperature-calibrated |
| Costs | C_FP + C_FN = 1. Training range {1:1, 1:4, 1:9}; held out {1:19, 1:49, 4:1}. Shift S: ratio 1:9, with confirmation resampled to 3× the fit prior (about 0.24), capped at 0.5 |
| Family (m = 19 per dataset) | At each held-out ratio: A−B-stale; A−B-retrain_r; C−A; C\*−A; E−A (15). Under S: A-recal−B-retrain_S; A-raw−A-recal; C\*−A-recal; E−A-recal (4). A_tuned and in-range ratios are descriptive |
| Margin | δ_r = 0.02 × the calibration-split cost of A at ratio r: a relative cost difference below 2% is immaterial to the principal. Under S, 2% of A-recal's cost on the calibration split resampled to the S prior |
| Monotonicity | For each case, the action must switch at most once, from abstain to act, as C_FN/C_FP increases along 4:1, 1:1, 1:4, 1:9, 1:19, 1:49. Violations are counted per arm |
| Planning n [H, synthetic calibrated population, AUC 0.90, prevalence 0.08] | Equivalence of C\* to A, when C\* is A perturbed by logit noise τ = 0.1 or 0.3: n = 61k or 192k at 1:19; 91k or 271k at 1:49; 12k or 33k at 4:1. A vs B-stale: Δ = −0.042, −0.053 and −0.005 (superiority n ≤ 5.5k). All of these fit about 1.6M confirmation rows. The v2 97k test split alone would leave 1:19 and 1:49 unpowered at τ = 0.3. CLINC equivalence is powered only if σ/δ ≤ 26.4; expect superiority rows only |
| Rejects X1 on the task | B-stale equivalent to A at every powered held-out ratio; **or** B-retrain_r superior to A by more than δ_r at a powered ratio; **or** B-retrain_S superior to A-recal by more than δ |
| Narrows | **Ownership:** C\* or E equivalent to A at every powered held-out ratio and to A-recal under S, with zero monotonicity violations. The claim rests on c as an input, not on closed form. **Implementation:** B-stale superior to A at a powered ratio means the calibrated plug-in failed. This is Astra's case: p̂ = 0.2, true 0.05, costs 0.1/0.9, loss 0.095 vs 0.045 [Rep calc]. X1 is then unsupported on the task until calibration is repaired |
| Supports | At least 2 of the 3 held-out ratios are powered; A is superior to B-stale and non-inferior to B-retrain_r at every powered ratio; and, if S is powered, A-recal is non-inferior to B-retrain_S with no more labels |
| Inconclusive | Fewer than 2 powered held-out ratios, or none of the rows above |
| Outcomes, not controls | A fitted on a second, equal-size fit subsample vs A: reported as fit variance |
| Controls | Identical frozen A through the full pipeline: Δ ≡ 0 on every case. Semi-synthetic: on a copy of confirmation, draw y\* ~ Bernoulli(s_i) from A's calibrated scores, so each threshold policy's expected cost is analytic. Plant (a) two thresholds with analytically equal cost, (b) Δ = 1.5δ_r and (c) Δ = δ_r. Over 200 redraws the pipeline must claim equivalence in (a) at about its planned power, inferiority in (b), and false equivalence in (c) at most at the α/m rate (binomial CI) |

**E3: episode control and acceptance.** Tests X5, P5 and P6. Strongly recommended. Needs the
tabputer-1 GPU (§4.4).

| Field | Specification |
|---|---|
| Population | HotpotQA distractor validation: CC-BY-SA-4.0, 7,405 hard questions [C, recheck]. The train split mixes difficulty levels, so it is excluded. Rounds read k ∈ {2, 4, 6} paragraphs and choose stop, expand or abstain. U = EM − λ·rounds/3 − μ·tokens/1000; λ = 0.1 is primary; μ is fixed at the design lock |
| Identification | Full-information replay: every answer at every k, so X5b holds by construction. Live agents rarely have this |
| Readers | Qwen3-1.7B and Qwen3-4B at pinned revisions: BF16, non-thinking mode, greedy decoding. Distinct instruments. A 50-question determinism check reports the rerun disagreement rate |
| Arms | (i) implicit prompt; (ii) threshold on LLM answerability; (iii) threshold on dense similarity; (iv) composite; (v) constants; (vi) proxy-selected threshold; (vii) outcome-selected threshold |
| Family (m = 6) | Per reader at λ = 0.1: best explicit − implicit; best explicit − best constant; (vii) − (vi). The best explicit arm is chosen on search and frozen |
| Margin | 0.02 utility (about 2 EM points) |
| n | Planning σ = 0.30 [H] gives 3,457 at m = 6. The half-width at the v2 n of 1,200 is 0.0228, wider than the margin. Plan 1,000 search (including a 100-question σ pilot and a 50-question timing pilot) plus 3,500 confirmation. At the analysis lock, n_conf = min(6,405, n(σ̂)). σ̂ ≤ 0.40 fits (6,146). Beyond that the equivalence rows are unpowered; superiority rows still run |
| Calls | 9 per question per reader (3 contexts × answer, answerability score and implicit decision). Planned 81,000; maximum 133,290; 1.7B-only fallback 36,360 |
| Cap and narrowing | 24 GPU-hours for E3. If the timing pilot projects more, the 4B reader is dropped before any confirmation read (m = 3; n = 3,040 at σ = 0.30). If the projection still exceeds the cap, equivalence rows are inconclusive. The margin is never changed |
| Outcomes per claim | *Explicit vs implicit* and *policy vs constants*: supported if the best explicit arm is superior for every powered reader; rejected if the two are equivalent for every powered reader; otherwise inconclusive. *P5*: (vii) superior to (vi) supports; equivalence rejects. *P6*: over 200 resplits, false adoption is judged against the finite-population truth (all 7,405 questions). Incumbent–challenger lower than adopt-best, with the 95% CI of the difference excluding 0, supports; otherwise not supported |
| Controls | Identical frozen incumbent vs its copy: Δ ≡ 0, never adopted. A planted +0.05 utility shift on a replay copy must be adopted at its planned power (about 1). The per-question oracle is reported as headroom, not used as a control |

**E4: acceptance machinery.** Tests A and P6. Required. Fixture and simulation evidence only.

| Part | Design | Pass |
|---|---|---|
| E4a Monte Carlo diagnostic | **C = 108 cells:** `hoeffding` and `empirical_bernstein`, each 2 modes × n ∈ {300, 1,000, 2,500} × K ∈ {1, 5} × 4 loss distributions (three-point, two-point extreme, continuous, rare-large); plus `sign_exact` on the 2 binary distributions × 3 n × 2 K. **R = 40,000** replications at the boundary null (Δ = −m, or +m_NI). It calls the helper's own code. The coverage *claim* rests on the theorems and exact-rational unit tests; this diagnostic detects gross defects | Every cell's simultaneous (Bonferroni over 108, γ = 0.05) one-sided Clopper–Pearson upper bound is ≤ α + τ = 0.055, which means at most 2,049 adoptions per cell. A cell whose true rate is ≤ 4.5% fails with probability 2e-9. An exactly nominal cell fails with probability 0.128; the offered bounds are conservative (normal-approximation size at the boundary null ≤ 0.72% even for the two-point extreme distribution, σ = 1). A rate ≥ 6% is detected with probability ≈ 1 [Rep calc]. **Positive controls:** (1) three planted gross defects must fail: radius removed, Δ sign flipped, radius n inflated 100×; (2) power at the planning effect is reported per cell, and a method with power < 0.5 at a given n is not the default there. The v2 rule is reproduced as failed: 224/4,000 passed it, and 30 valid cells would fail it together with probability 0.528 |
| E4b Eligibility | Fixtures: teacher-labeled confirmation rows; synthetic text; unequal inclusion probabilities; the 50/950 case (−0.667 apparent vs +0.9 true); the sign case (p = 0.0068 while mean loss rises by 0.0292) | In order: `proxy_evidence_only`; `fixture_evidence_only`; `unsupported_sampling_design`; refused; `sign_exact` refuses non-binary input |
| E4c Isolation (tabputer-1) | A scripted adversary harness plants each exploit with a canary. Hard-coded confirmation IDs → leak gate. Gold in synthetic rows → overlap audit. Sibling-run read → per-run container mounts. Evaluator or split edit → owned by `augctl` (EACCES) and hash drift. Read of confirmation labels → not mounted, and EACCES on the host. Network exfiltration → `--network=none` plus the skuid drop. Write outside `/work` → EROFS. Resource exhaustion → cgroup limits and timeout | Every exploit is refused by its named mechanism, and its canary proves the plant was active. A benign planted improvement is accepted end to end |
| E4d Agent A/A (optional) | 20 incumbent-vs-itself runs. The proposer runs off tabputer-1, because it needs inference credentials; candidates execute only under the §4.2 profile | Reject at ≥ 3 adoptions: P = 0.0755; power 0.79 at a 20% rate. A smoke test only |

**E2 (optional; CIFAR-10H, CC BY-NC-SA).** Skipped by default (decision 5).

### 2.8 Outline

Seven sections, no subsections:

1. Two policies, and what is known.
2. Ownership, not weakness.
3. The test, with worked scenarios, including one human or organizational system.
4. Accepting a change.
5. Evidence: E1, E3 and E4, including inconclusive rows and what failed.
6. Preference, outcome RL and the boundary.
7. Limits and open falsifiers.

### 2.9 Placement and publication conditions

**Placement.** The draft is Typst, in `research/080/paper/`. The site is `docs/exogenous-policy/`.
Code and receipts go in `research/exogenous-policy/`, on the local branch only.

**Publish only when all of these hold:**

1. Confidentiality is lifted.
2. E1 ran as pre-registered and is reported whatever the result.
3. Every number is bound to an artifact or a Reported source, with its comparison, metric,
   population and conditions.
4. Every reference resolves by ID, with title and retraction checks.
5. A human has checked every load-bearing passage, including the seeded wrong-claim case.
6. Independent review on the requested models leaves no unresolved severe flaw.
7. The name is decided.
8. Licenses and TypeSafe terms are rechecked.
9. §6.7 passes, and `check_site.py` passes on the build: one `lang`; a pre-main skip link with
   `tabindex=-1`; a zoom-safe viewport; no `noindex`; named, focusable code and `.table-scroll`
   regions.
10. Font provenance is recorded.

**If scooped:** reframe within a week as replication plus E1, E3, E4 and the protocol. Watch
manually, weekly. Decide by 2026-11-15.

## 3. Trainer skill (`augustus-train`)

### 3.1 Packaging and repository checks

- **Packaging.** A second skill in the `augustus` plugin, invoked as
  `/augustus:augustus-train`. Move it to its own plugin if it fires on more than 10% of
  augustus-only activation prompts.
- **M1** branches from `origin/main` after `git fetch origin`, recording the SHA; today that is
  `d8dc848` [Coord]. It creates a valid skeleton at `0.8.0-dev` in both skills and the marketplace.
- It then generalizes `check_repo.py`, which still hard-codes one `SKILL_PATH` and one 180,000 B
  reference total: per-skill limits and totals, version parity, portable frontmatter, and
  per-skill reachability.
- The first 0.8.0 commit adds `.local/` and `.claude/` to `.gitignore` (decision 13).
- The augustus hand-off is one `SKILL.md` line (10,743 of 16,000 B at 0.7.2).
- Scenarios compare against the last published release, v0.7.2.

| Request | Owner |
|---|---|
| Choosing a classifier, Jev, an LLM or a rule; thresholds; calibration; prompt or DSPy climbing | `augustus` |
| Training, fine-tuning or distilling a head; creating or labeling data; training climbs | `augustus-train`, starting at G0 |
| Distilling Jev, or selecting by Jev uncertainty | `augustus-train`; the gate refuses |
| Tone fine-tuning | Neither |

### 3.2 G0: the don't-train check takes the acceptance policy as input

**Inputs:** the decision; the cost policy (units, mode, margin, α, method); the acceptance bar;
available independent gold (count, unit, sampling design); the label budget.

**Do not train when any of these holds:**

- an exact rule decides the case;
- a baseline meets the bar;
- the n the chosen method needs at the planning effect, including the fit/confirmation split,
  exceeds the independent units available (this is computed, not guessed);
- the criteria churn faster than retraining;
- labeler agreement is below the bar;
- the task needs multi-step reasoning.

**Small samples.** For a large prespecified binary effect, 20 discordant wins in 40 rows give
p ≈ 1e-6 under `sign_exact`. A 2 pp guarantee is infeasible at that size.

### 3.3 Ladder and the M5 rule

**Rungs.** R0 don't train; R1 frozen readout; R2 linear head; R3 small encoder; R4 LoRA plus a
head; R5 generalist, never the default. The runtime `recipes` reference states each rung's entry
and exit conditions and its guards. Reported numbers stay in `research/`. The shipped default is a
procedure: stop at the cheapest rung that meets the workload's policy on untouched, group-split
data.

| M5 element | Pre-registered rule |
|---|---|
| Arms | R0; R1 (Qwen3.5-2B frozen: raw, two-order averaging, L0, then OOF temperature); R2a (LR on MiniLM); R2b (ridge/LDA on R1's ⅔-depth state); R3a (SetFit, pinned body). R3b (DeBERTa-v3-large) runs only if the GPU passes §4.4 (decision 23); otherwise it ships labeled "untested in 0.8.0". R4 is a documented escalation, untested |
| Tasks | **T1** (generated, code-labeled): `fixture_evidence_only`. It informs the guard text (NOTA, twins, negation) and makes no margin claim. **Eligible real-text confirmation**, all human-written, with seeded equal-probability splits; the population is the benchmark, not deployment traffic: **T2a** BANKING77, full 77-way, CC BY 4.0, about 13.1k rows, real-query provenance checked at M2; **T2b** CLINC150 plus OOS, route-or-abstain, reusing E1's seeded CLINC partition (the two experiments ask different questions, and neither selects on the other's confirmation outcomes); **T2c** CivilComments, the E1-disjoint 100k pool. Fixed cost matrices: misroute 1, abstain 0.3, correct 0 for T2a and T2b; C_FP:C_FN = 1:4 for T2c |
| Estimand and test | Δ = loss(low rung) − loss(R3a) in normalized cost. Non-inferiority: EB UCB(Δ) < +0.01, over K = 3 low rungs (R1, R2a, R2b) at α/3 per task. Tasks combine by intersection-union, so no cross-task correction is needed. The margin is v1's 1 pp and is not widened |
| n [Rep calc, `calc_v3.py` §3] | At true Δ = 0 with 80% power, EB needs 5,025 rows (σ = 0.10), 10,175 (0.20) or 18,136 (0.30). Hoeffding needs about 87k–97k. v2's 470 had a radius of 0.132. Planned confirmation: T2a about 6,000 (powered only if σ ≤ 0.10); T2b about 12,850 (σ ≤ 0.20); T2c 40,000, expandable to 60,000 (every σ up to 0.35). A genuinely better low rung can pass even on an unpowered task, but only powered tasks count toward outcomes |
| Stop at R2 | One low rung is non-inferior on every powered real task, and at least 2 tasks are powered. The recipe says R2 matched R3a within 1 pp on those public tasks; R3a becomes an escalation |
| Narrowed | The same, but with only 1 powered task. The recipe names that task type only |
| Escalate | R3a superior to every low rung by more than 0.01 (EB LCB(Δ) > +0.01) on a powered task. The recipe says the low rungs fell short on that task type |
| Workload-local | Mixed results across powered tasks |
| **Inconclusive** | Everything else, including no powered task. No rung recommendation: the default stays the procedure, and the recipe states that the 0.8.0 reproduction was inconclusive at 1 pp |

### 3.4 Data protocol

Each rule is conditional and is stated once, in `data-and-labels.md`.

| Rule | Applies when | Guard or check |
|---|---|---|
| Gold first | Always | Confirmation data are sampled from real traffic with equal inclusion probability (or a self-weighting design), labeled independently, frozen and hashed before any generation |
| Teacher route | A teacher is used | Code-computed labels or a local open-weight teacher by default; a hosted teacher must pass §3.6 |
| Double agreement | One teacher labels real text | Not needed for code-computed labels |
| NOTA as answer and distractor | A NOTA option exists | Pair probe |
| Style-seed partition | Style seeds are used | Overlap audit |
| Neutral IDs | Label names are free-form | Rebinding probe (0/1 → no/yes moved AUC from .94 to .23 [R]) |
| Same-split families | Pairs or generation families exist | Group split and a ledger property test |
| Missing-evidence twins | Evidence can be absent | Uniform targets vs abstention (decision 9) |
| Accumulate real rows | Always | Ledger |
| Fact–text binding | Labels are computed from facts | A constrained renderer or an independent extractor; evidence ablation; filler invariance; corrupted-rendering fixtures. All fixture evidence |
| Real text for T2 | M5 | T2a–T2c as in §3.3. WANLI (2201.05955, C via reviewer) is an optional generated-text stress test only |

### 3.5 Confirmation and the climb ledger

`compare_workflows.py` gains four things:

- a `mode` (superiority or non-inferiority);
- a `method`: `hoeffding` (the default), `empirical_bernstein`, or `sign_exact`, which follows the
  §2.4 rule;
- a required `sampling_design`, which must be `equal_probability` for confirmation in 0.8.0;
- `sampling_unit` semantics: episode, person or cluster.

**Rules for the helper**

- Bonferroni applies over `comparison_count` for every method.
- Hoeffding output stays byte-identical, with a regression test.
- `--help` states each method's estimand, its assumptions, and what it cannot certify.
- Numerical tests follow CONTRIBUTING.
- Byte copies of the helper ship with a parity test.
- `audit_sample.py` is a monitoring estimator, not an acceptance bound.

**Climb ledger.** It is controller-owned and append-only.

- The config is immutable. The evaluator and splits are hashed, and drift fails closed.
- Candidates are challenged on fresh rows.
- Every round reports Δ against the original anchor. Rounds are bounded.
- Probes and per-label recall floors are hard gates.
- A metered budget moves the run to `paused_budget`.
- The K finalists are frozen, and confirmation data are burned once read.

**Terminal states:** `promoted_candidate`, `incumbent_retained`, `dont_train(reason)`,
`insufficient_evidence`, `insufficient_causal_evidence`, `unsupported_sampling_design`,
`paused_budget`, `blocked`, `needs_human(one question)`.

### 3.6 Provider-provenance graph gate

**Graph.**

- Nodes: rows, texts, labels, features, filter and selection decisions, datasets, derived corpora,
  checkpoints, prompts and external models.
- Edges: `generated_by`, `labeled_by`, `filtered_by`, `selected_by`, `featurized_by`,
  `derived_from`, `trained_on`, `accessed_via`.

**Resolution.** Each external model resolves separately to its model, provider and revision, and
to its access channel. The verdict is the most restrictive of the provider's terms, the channel's
terms and the weight license.

**Permission records.** Each record binds one artifact or revision, one channel and one use. An
`allowed` record without its URL, digest and clause is rejected.

**Rules.**

- A path from a barred node to a training artifact, through any edge, is refused.
- TypeSafe/Jev, its aliases and declared Jev-derived corpora (for example
  `SargeDev/jev-distill-corpus`) are barred.
- A named approval can clear `unknown` for one artifact and one use. It never clears `barred`.
- Missing parents make lineage unknown.
- **The gate checks declared provenance only**, and the skill says so whenever it reports a pass.

| Test case | Expected |
|---|---|
| Human-labeled row selected by Jev uncertainty; row filtered by Jev; Jev-derived features; corpus inheriting from a Jev distill corpus; Jev through an alias | Refused |
| Unknown lineage | `unknown` |
| Named approval on a barred node | Still refused |
| `allowed` without a digest | Rejected |
| Local Apache-2.0 teacher with declared lineage | Passes; provenance recorded |

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
| S7: distill Jev, or select by Jev uncertainty | Refuse; offer compliant routes; say provenance is declared |
| S8: train the JevBench leader | Rank is not a selector |
| S9: multi-step dates | Reasoning exit |
| S10: unequal-probability confirmation sample | `unsupported_sampling_design` |
| S11: the challenger changes approvals | `insufficient_causal_evidence` |
| S12: 1 pp margin, 3k rows | Required n shown; inconclusive predicted; margin not widened |
| S13–S15: Bayes threshold, prompt climb, tone fine-tune | Not triggered |

The activation suite is opt-in, in `tests/plugin-evals/`, at most $10 per release candidate.

## 4. Compute and isolation

### 4.1 Hosts and roles

| Host | Used for | Never used for |
|---|---|---|
| Mac | Authoring; review; `make check` on reviewed first-party repo code; Typst; serving a built site copy with `python3 -m http.server`; delegate reviews | Experiments; third-party packages beyond those already installed; model weights; candidate or unreviewed generated code; any isolation claim |
| tabputer-1 | Every experiment (E1, E3, E4, M5); third-party packages and weights; candidate code; the Jekyll build, in a container | Holding the plan, reviews, research notes or any credential; isolation claims against root, the maintainer's account or privileged k3s workloads |
| Colab | Nothing by default (decision 24) | Confidential code or data without a per-experiment approval |

**Transfers.** The maintainer copies a hashed run bundle (code, configs, prereg copies) into
`/srv/aug/inbox/`, and copies receipts back. Bundles are built from an explicit file list, so
`.local/` and `.claude/` content never travels except the named bundle files. This lane does not SSH. An agent on tabputer-1 is
possible only if the maintainer grants it.

### 4.2 tabputer-1 execution profile

| Principal | Role | Groups | Reads | Writes | Network |
|---|---|---|---|---|---|
| `augexp` | Setup downloads; the runner; every container | Own group, plus `render` and `video` for the GPU. Not in `wheel`, `docker`, `adm`, `systemd-journal` or sudoers | Own home; `/srv/aug/stage` (read-only, root-owned after setup); `/srv/aug/runs/<id>` | Own home, per-run directories, `/srv/aug/pred/<id>` | Setup: only the local proxy. Closed: nothing |
| `augctl` | Holds confirmation labels, manifests, the grader and prereg copies; scores predictions; writes receipts | Own group | `/srv/aug/ctl` (700); predictions (read-only through a group) | Receipts | Nothing, ever |
| `augproxy` | First-party stdlib CONNECT proxy, used during setup only | Own group | Its allowlist | Its connection log | TCP 443 to public addresses; private and loopback ranges dropped |

**Staging.** Public datasets, weights, the base image and the uv virtualenv (a uv-managed CPython
3.12 with a hashed lock and wheels only, so no install-time code runs) are fetched by `augexp`
through the proxy. They are then moved under `/srv/aug/stage/`, owned by root and read-only to
`augexp`, with `HF_HOME` and `HF_HUB_OFFLINE=1` pointing there. `augexp` has `umask 077` and
`TMPDIR` in its own home.

**Containers.** `podman run --rm --network=none --read-only --tmpfs /tmp --cap-drop=all
--security-opt=no-new-privileges --pids-limit=512 --memory=16g --ipc=private`, with `/stage`
mounted read-only and `/work` bound to a fresh per-run directory. There is one base image, pinned
by digest. GPU devices (`/dev/kfd`, `/dev/dri/renderD*`, `--group-add keep-groups`) are passed only
to first-party experiment runs that need them. Candidate code never gets the GPU. Each candidate
gets its own container and `/work`; runs are sequential until B14 passes.

**Egress.** The maintainer installs a separate nftables table (`inet augexp`) and never flushes the
ruleset, so the ufw and k3s rules are untouched. Its output chain matches `meta skuid`:

- **`augexp`** may reach only `lo` TCP 3128 (the proxy), and only during setup. Everything else is
  logged, counted and dropped: DNS, the loopback services (ollama 11434, k3s 6443, kubelet 10250),
  the node address, and the pod and service CIDRs. At close, the proxy rule is deleted.
- **`augctl`**: everything dropped.
- **`augproxy`**: TCP 443 only, never to private ranges.

**Proxy allowlist**, named at the design lock and verified at setup [U]: `pypi.org`,
`files.pythonhosted.org`, the chosen PyTorch or AMD wheel index, `huggingface.co` and its current
storage hosts, the uv Python-build host, and the base image's registry hosts. `typesafe.ai` and all
its subdomains are explicitly denied. IP literals and ports other than 443 are refused.

Because rootless podman's user-mode networking runs as `augexp`, a container started without
`--network=none` by mistake is also dropped. The alternative of nft IP sets built from resolved
names is weaker, since CDN addresses are shared.

### 4.3 Boundary tests (all must pass before any run; results in a dated receipt)

| # | Test (as the named principal, on the host and inside a container) | Pass |
|---|---|---|
| B1 | `id`; `sudo -n true`; polkit admin check | No admin groups; sudo and polkit denied |
| B2 | Credential inventory: `~/.ssh`, `.netrc`, git credentials, `gh`, HF token, `~/.docker`, `~/.kube`; environment variables matching `*_TOKEN`, `*_KEY` or `*SECRET*` | Empty |
| B3 | Read the maintainer's home and `/root` | EACCES; zero readable files |
| B4 | Other workloads: `/etc/rancher/k3s/k3s.yaml`, `/var/lib/{rancher,kubelet,docker,containers}`, `/run/k3s`, `docker.sock`, containerd, `/run/user/<maintainer>`, ollama's store and unit drop-ins; `docker ps`; `kubectl get pods` | Unreadable or refused |
| B5 | Machine-wide sweep: readable files outside `/usr`, `/proc`, `/sys`, the principal's own home and `/srv/aug/stage`, grepped for key and token markers (including `/etc`, `/tmp` and `/dev/shm`) | Zero hits |
| B6 | `augexp` reads `/srv/aug/ctl`, including a planted canary | EACCES; the canary never appears in any output |
| B7 | Writes to the maintainer's home, `/srv/aug/stage`, `/srv/aug/ctl`, `/etc`, `/usr` and `/opt/rocm`; inside a container, anywhere except `/work` and `/tmp` | EACCES or EROFS |
| B8 | Persistence: crontab; enabling a systemd user unit | Denied, or no lingering outside windows |
| B9 | Setup open: a named host through the proxy; `example.com` through the proxy; direct HTTPS with no proxy; `typesafe.ai` variants (case, trailing dot, punycode, subdomain); an IP-literal CONNECT; loopback services; node, pod and service IPs; DNS to 1.1.1.1 and to the local resolver | Only the first succeeds; every refusal appears in the proxy log or the nft counter |
| B10 | Setup closed: repeat B9 on the host; inside a `--network=none` container, resolve a name and connect to host IPs; start a container *with* networking | All fail; nft counters increase |
| B11 | `augctl` attempts any connection | Dropped |
| B12 | A container allocates more than 16 GB; fork bomb; the wrapper's MemAvailable abort | OOM or pids limit inside the container only; the wrapper aborts below 6 GB. Memory-controller delegation is [U] until tested |
| B13 | GPU acceptance (§4.4) | Pass, or a CPU-only fallback is recorded |
| B14 | Sibling runs: run A reads run B's `/work` host path, `/proc/<pid>/root`, `/tmp` and `/dev/shm` | ENOENT or EACCES |

### 4.4 ROCm and GPU acceptance

- **Candidates, in order** (decision 23): PyTorch's stable ROCm index; AMD's release wheels; AMD's
  gfx1151 builds. Take the first whose `torch.cuda.get_arch_list()` includes `gfx1151`, on uv
  CPython 3.12 (cp314 ROCm wheels are [U]).
- `HSA_OVERRIDE_GFX_VERSION` is not used without approval.
- Record per receipt: the kernel, the amdgpu firmware, the host ROCm and the wheel hashes.
- **Acceptance tests:**
  - matmul, softmax and SDPA agree with a CPU fp32 reference within bf16 tolerance;
  - MiniLM embeddings on GPU vs CPU have cosine ≥ 0.9999 on 1,000 texts;
  - Qwen3-1.7B greedy output on 50 prompts is identical on a GPU rerun ≥ 98% of the time
    (GPU-vs-CPU agreement is reported);
  - a 30-minute soak raises no amdgpu reset.
- **If nothing passes:** CPU-only torch. E1, E4 and M5 run on CPU (R1 limited to T2a and T2b; no
  R3b). E3 slips to 0.8.1, because the 4B reader on CPU projects about 103 hours [H].

### 4.5 Runtime and compute budget (tabputer-1)

Throughputs are [H], BF16 through PyTorch ROCm, and are replaced by each timing pilot. Memory is
shared with the GTT, so the wrapper watches system MemAvailable.

| Run | Models (size) | Work | Throughput assumption [H] | Wall-clock [H] | Peak RAM [H] |
|---|---|---|---|---|---|
| Setup + B1–B14 | — | About 45 GB of downloads (venv 10–15 GB, weights 22 GB, data 2 GB) | Network-bound | 0.5–1 day, maintainer-attended | — |
| E4a | stdlib | 4.32M replications, about 13M helper calls | About 2.5 ms per call | 9 CPU-h; about 20 min on 30 processes | < 2 GB |
| E1 | MiniLM-L6 (22.7M, 0.09 GB) | Embed 2.12M texts; fit arms; 38 CIs; 200 control redraws | 5,000/s GPU or 800/s CPU | 7 min or 44 min to embed; ≤ 2 h total | ≤ 10 GB |
| E3 | Qwen3-1.7B (about 4 GB); Qwen3-4B (about 8 GB) | 4,500–7,405 questions × 9 calls × 2 readers | Prefill 4,000 / 1,600 tok/s; decode 800 / 350 tok/s | 1.6 + 4.1 h planned; 2.7 + 6.7 h maximum; cap 24 GPU-h | 6 / 12 GB |
| M5 | MiniLM; SetFit body (about 110M); Qwen3.5-2B (about 4.5 GB); optional DeBERTa-v3-large (435M) | R1 readout of about 19.7M tokens; SetFit on 4 tasks; optional R3b | Prefill 3,000 tok/s | About 2 h R1, about 2 h SetFit, 2–6 h R3b; cap 24 GPU-h | ≤ 14 GB |
| Jekyll build | github-pages 232 container | One site build | — | Minutes | < 2 GB |

**Envelope** (decision 22): one run at a time; a 16 GB container cap; launch only if MemAvailable
is at least 24 GB; abort below 6 GB. Today about 16 GB is free [Coord], so runs stay `blocked(memory)`
until the maintainer confirms a window.

### 4.6 What is not claimed

- No protection against tabputer-1's root, the maintainer's root-equivalent account, privileged or
  hostPath k3s workloads, kernel or GPU-driver exploits, or side channels.
- Anything staged there is readable by those principals, so only run bundles and public data are
  staged.
- `render` membership exposes the GPU driver's attack surface, which is why candidate code runs
  without devices.
- The Mac provides no isolation.
- "Sandbox" means exactly the mechanisms B1–B14 test. The tests run again after any system update.

## 5. Research automation

### 5.1 Stance

Adopt no third-party runtime. The v1 rejections stand: swarm-factory (a lure; do not visit);
remote-instruction installers; githubnext/autoloop; InternAgent; AutoResearchClaw; automated paper
writers; DARE's hosted search; weak keep rules; FAROS code (ideas only).

### 5.2 Patrol: deferred from 0.8.0 (maintainer decision)

Patrols stay manual. A future unattended patrol needs all of the following before any pilot.

| Prerequisite | Source |
|---|---|
| A host where the job's account cannot read confidential material or credentials, verified against every local account including admins. Not this Mac | Fable v2 P0-1; Astra v2 1; [Coord] |
| An enforced egress boundary with complete connection-event evidence (an nft or pf log, or a proxy log), not socket sampling | Astra v2 7; Fable v2 P2-1 |
| Fetch requests bound to trusted source identities: IDs taken only from the collector's own discovery feeds, or approved by a human. Tests include syntactically valid IDs that carry a payload | Astra v2 7 |
| Headless CLI fixes: `--verbose` with stream-json; nonessential traffic disabled; the observed model taken from assistant messages; a seeded receipt 0; a numeric freshness grace | Fable v2 P2-1, P2-7 |
| Spend authorization, numeric caps, a scheduler owner, and `maintenance.md` receipts | v2 §4.2–4.3 |

### 5.3 Paper gates

- A stdlib bibliography gate using ID-only GETs to arXiv, Crossref and OpenAlex. This is manual
  tooling; `unverifiable` never passes.
- A span-anchored claim ledger.
- Prose passes, with a no-change option.
- Human sign-off.
- Seeded fixtures: a wrong arXiv ID; a fabricated citation; a retracted DOI; v1's AIRA-dojo
  misattribution.

## 6. Design artifacts: the paper and the project site

### 6.1 What the design must do

The brief asks for restraint without trend styling (no beige or green, no gimmicky type, no wall
of headings), interactivity that explains the mechanism, and honesty about evidence.

**Rule:** every figure and explorable names the claim it tests and shows what the reader would see
if the claim were false. Anything that cannot do both is cut. Inconclusive and unpowered results
are displayed as such, never hidden.

### 6.2 The paper

| Element | Rule |
|---|---|
| Format | Typst to PDF; US Letter, checked at A4 |
| Measure | One column of 66–72 characters. A narrow outer margin carries the evidence labels and short notes. Figures may span |
| Type (decision 15) | STIX Two Text and Math (OFL) for text and math. Geist Sans for heads, tables, captions and labels; Geist Mono for IDs and hashes. 10.5/14.5 pt. Three levels at most |
| Structure | The seven sections of §2.8; the test as run-in paragraphs plus one table. The abstract states the ownership argument and E1's result |
| Tables and figures | Booktabs rules and tabular figures. One stdlib script renders SVG from the same data as the site's fallbacks. Captions state the parameter state and the label. Grayscale plus one accent |
| Front matter | Version, commit, and both lock hashes. No ornament |

### 6.3 Site information architecture

The site is a standalone layout under `docs/exogenous-policy/`. It uses the site's tokens and local
Geist fonts, with no marketing chrome.

| Page | Reader's job | Contents |
|---|---|---|
| `/` | Follow the argument | A 120-word summary, then the seven sections with explorables at their claims. Labels sit in the margin at ≥ 1200px and inline below that. Sources at the end |
| `/test/` | Apply the test | X-5 full width, with state in the URL hash. It produces a copyable decision record |
| `/evidence/` | Check the experiments | Per experiment: both lock hashes and dates; each contrast's CI drawn against its margin, with a powered flag; status (not run / rejected / narrowed / supported / inconclusive); receipts |
| `paper.pdf` | Cite | The canonical artifact |

### 6.4 Explorables

| # | Claim | Reader manipulates | Reader sees, including the counter-case | Data | Without JS |
|---|---|---|---|---|---|
| X-1 | Costs move the threshold, not the weights (X1, P1, P2, P9) | Log slider from 1:49 to 49:1; a prior-shift toggle | The threshold moves; the stale threshold's regret grows; the retrained head is shown; the region where a constant wins is marked; re-thresholding without recalibration fails under shift | [Rep sim] until E1, then E1 confirmation scores (CC0), with the switch labeled | SVGs at 1:1, 1:9 and 1:49; a regret table |
| X-2 | Uncertainty scores are not interchangeable | Drag probability mass across a menu | Entropy and top-mass order two cases oppositely | Exact | Two worked cases |
| X-3 | Deferral under a handler swap (X3) | Pool, deferral cost, rule | The population threshold fails when errors concentrate; the joint-training win can be selected | Simulation [H] | Before/after SVGs |
| X-4 | Accepting a change (A, P6) | K, true effect, search n, confirmation n, margin, family size; a seeded "200 resplits" button | Adopt-best adopts under zero effect; incumbent–challenger mostly retains; when the CI half-width exceeds the margin, the verdict reads "inconclusive" | [Rep sim]; E3 once run | Histograms and a table |
| X-5 | The test is a procedure | Each predicate: holds, fails or unknown | The route | [H] | The table and the procedure |
| X-6 (optional) | Expose the field (X4) | Hidden-stake toggle | +57.7% regret vanishes | [Rep toy] | Two SVGs |

**Shared behavior:**

- native controls that show their values;
- `aria-live="polite"` text outputs;
- a `<details>` table for every chart;
- controls are inserted only by JS;
- seeded PRNGs, with a JS-to-Python parity fixture run locally in Node, with no npm packages.

### 6.5 Visual system

| Dimension | Rule |
|---|---|
| Type | Geist Sans and Mono only, from local OFL WOFF2 files. Body 17px/1.6 (a recorded long-form exception to the 16px base); 62–70ch; at most five sizes. No variable-weight animation, outlined or gradient type, uppercase label walls or italic flourishes |
| Color | The site's neutral tokens. **One accent, for data state only** (the reader's parameter and the chosen action): never headings, links, buttons or backgrounds. Light and dark values, at ≥ 3:1 as a graphic and ≥ 4.5:1 with text. No beige, cream, green, gradients or tints |
| Encoding | Labels and series differ by text, shape and dash, not by hue |
| Grid | The 1280px ruled grid; a 680px reading column; explorables at 960px; a 220px margin column at ≥ 1200px. Mobile: one column, 16px outer gutters (aligned with the repo guidance; v2's 12px is withdrawn), no horizontal page scroll. Wide tables scroll in named, focusable regions |
| Headings and motion | Only where the argument turns. No motion: at most a 120 ms opacity change, removed under reduced motion |
| Accessibility | WCAG 2.2 AA; full keyboard operation; visible focus; 44px targets; nothing by color alone; reflow at 400% and 320px; text alternatives |
| No-JS and themes | Everything reads without JS. Light and dark come from tokens. No images of text |

### 6.6 Build constraints

- **Pages** builds with Jekyll 3.10 (github-pages 232). Explorables are hand-written ES modules: no
  framework, no CDN, no third-party requests.
- **Weight:** at most 300 KB per page, excluding fonts and the PDF, and 60 KB of JS.
- **Builds:** the Pages-equivalent build and `check_site.py` run on tabputer-1 in a container (gems
  fetched through the setup proxy, then network-none). The built `_site` is copied back and served
  on the Mac for review. Nothing is installed on the Mac.
- **No uploads:** confidential content never goes to Stitch or similar tools.

### 6.7 Design review

| Step | Scope | Evidence kept |
|---|---|---|
| Freeze | Source hashes; the build command; font status | Dated audit |
| Screenshots | Essay top; each explorable in its default and one manipulated state; `/test/`; `/evidence/`; at 320, 390, 768 and 1440 px, light and dark | Requested and observed viewport and theme; unique-configuration count |
| Interaction | Keyboard pass; JS off; reduced motion; 200% and 400% zoom; VoiceOver on X-1 and X-5 | Notes |
| PDF | Page 1, a math page, a figure page and the references, at 100% and in grayscale | Images |
| Mechanical | `check_site.py`; the accent through the dataviz validator; a network log with no third-party requests | Output |
| Independent review | The requested models, never substituted, on frozen screenshots and source; taste kept apart from blockers | Findings table |
| Brief checks | Beige, green or tint; gimmicky type; a heading wall; an explorable without a claim and counter-case | Pass or fail |

## 7. Milestones

Effort is in agent-days, excluding compute. The v2 IDs are kept; M7 (the patrol) is removed.

| ID | Milestone | Depends | Effort | Exit criterion |
|---|---|---|---|---|
| M0 | §9 decisions; counsel questions; tabputer-1 provisioning (three users, `/srv/aug`, the nft table, the proxy with unit tests); B1–B14; GPU acceptance; memory window confirmed | — | 1.5 + maintainer time | Receipt showing every boundary test passed |
| M1 | Skeleton (`0.8.0-dev`, `.gitignore`); generalized `check_repo`; modes, methods and design check; ledger and provenance graph; overlap audit; climb ledger (on the Mac) | M0 decisions | 4–5 | `make check` green, with the CONTRIBUTING numerical tests |
| M2 | Design locks for E1, E3, E4 and M5; BANKING77 provenance check | M0 | 1 | Hashed before any download |
| M3 | E4a–c on tabputer-1 (E4d optional); T1 generator with fact–text binding | M1, M2, B1–B14 | 2 | E4 criteria met |
| M4 | E1, then E3, each with its analysis lock before confirmation | M3; GPU acceptance for E3 | 2 + about 1–2 days of compute | Results against each lock, inconclusive rows included |
| M5 | Trainer reproduction R0–R3a (R3b if the GPU passes) | M1, M3 | 3 | §3.3 rule applied, including inconclusive |
| M6 | Author `augustus-train`; hand-off; scenarios; independent review; activation suite | M5 | 2–3 | Budgets pass; no unresolved severe flaw |
| M8 | Paper and site: tokens, figures, explorables with parity, gates, design review | M3, M4 | 6–8 | §2.9 conditions 2–10 |
| M9 | Local 0.8.0-rc | M6; decision 11 answered or an accept-risk note | 1 | Plugin validates; an isolated install and Skills CLI `--list` show 2 skills; no push until "go" |

**Critical path:** M0→M1→M3→M5→M6→M9, about 13.5–15.5 agent-days. The paper path, M2→M4→M8, runs
alongside. **Total:** about 22–27 agent-days, plus about 2–3 days of compute inside the envelope.

**Scope cut.** The minimum 0.8.0 is the trainer with G0, the provenance gate, the confirmation
modes, and E4. E3, E2 and X-6 can slip to 0.8.1. The paper does not gate the release.

## 8. Risks

| Risk | Mitigation |
|---|---|
| The test is scooped | Reframe rule and decision date |
| E1 or E3 favors the learned or endogenous arm | Pre-registered rows; report and narrow |
| Too little memory on tabputer-1, or contention with k3s | Launch floor, cap and abort floor; `blocked(memory)`; windows confirmed by the maintainer |
| An OOM on tabputer-1 kills other workloads | Container cgroup cap; GTT watched through MemAvailable; one run at a time |
| gfx1151 ROCm immaturity or nondeterminism | §4.4 acceptance; determinism rate reported; CPU fallback; E3 slips |
| A rolling CachyOS update mid-study | Versions in every receipt; updates held during windows; B1–B14 and §4.4 rerun after an update |
| Staged bundles are readable by root or privileged pods on tabputer-1 | Stage only bundles and public data (decision 21) |
| Isolation overclaimed | Claims are limited to B1–B14; §4.6 |
| Underpowered results read as negatives | Powered-set rule; inconclusive rows; X-4 and `/evidence/` show it |
| Margin pressure after seeing n | Margins fixed at the design lock; the analysis lock records n before confirmation |
| Proxy data relabeled as gold | Derived `evidence_kind`; E4b |
| Mislabeled provenance | Declared-only limit; S7 |
| Explorable numbers drift from the paper | One figure script; parity fixture |
| Trend styling; font licensing | §6.5 rules and §6.7 checks; OFL faces only |
| Ambiguous MCA scope | Default deny; counsel; accept-risk note |
| A delegate model is substituted | Record requested and observed identity; no fallback |

## 9. Decisions for the maintainer

**Resolved since v2 [Coord]:** 0.7.2 released; Mac permissions tightened; the patrol dropped;
experiments sized with an inconclusive outcome. The v2 decisions on GPU spend (11), patrol
authorization (14) and the scheduler (15) are therefore withdrawn.

| # | v2 # | Decision | Recommended default |
|---|---|---|---|
| 1 | 1 | Name and slug | "When the Model Is Not the Policy", with a subtitle naming the test and acceptance; slug `exogenous-policy` |
| 2 | 2 | Type and venue | A position paper with executed E1, plus E3 and E4; Pages first |
| 3 | 3 | Installs and downloads | On tabputer-1 only, as `augexp` through the proxy: uv CPython 3.12; a hashed, wheels-only lock (the torch build from decision 23, transformers, sentence-transformers, setfit, scikit-learn, numpy, huggingface_hub); one pinned base image; pinned weights and data (about 45 GB); github-pages 232 in a container before M9. On the Mac: Geist OTF only |
| 4 | 4 | Scope | LLM agents plus one human or organizational example; no human-subject experiments |
| 5 | 5 | E2 (CC BY-NC-SA) | Skip in 0.8.0 |
| 6 | 6 | Packaging | A second skill in the augustus plugin, with the 10% switch rule |
| 7 | 7 | Confirmation methods | Add `empirical_bernstein`, `sign_exact` (§2.4 rule) and `mode`. Hoeffding stays the default where E4a power allows; M5 uses EB |
| 8 | 8 | Confirmation sampling | Equal-probability only in 0.8.0 |
| 9 | 9 | Missing-evidence design | Test both; ship abstain plus `unknown` unless uniform wins |
| 10 | 10 | "Learn utilities, not policies" | Discussion only |
| 11 | 12 | Counsel on MCA §2.3(b) | Ask at M0 (comparator use; bound Customer; whether the skill facilitates; channel terms). Jev excluded everywhere until answered or risk accepted |
| 12 | 13 | TypeSafe Website Terms §3(b)(vi) | Manual reads only; `typesafe.ai` denied in every automation allowlist, including the setup proxy |
| 13 | 16 | `.gitignore` vehicle | Add `.local/` and `.claude/` in the first 0.8.0 commit (M1). Optionally, you land the same line as a no-release public housekeeping PR, so that re-clones are covered. `.git/info/exclude` covers this checkout meanwhile |
| 14 | 17 | Pre-registration custody | Design and analysis locks: hashes plus your dated note in `research/080/prereg/`, with read-only copies under `augctl` |
| 15 | 18 | Paper typography | STIX Two plus Geist; A/B against all-Geist at the start of M8 |
| 16 | 19 | Scoop timebox | Reframe, don't restart; decide by 2026-11-15 |
| 17 | 20 | Site placement | Standalone layout under `docs/exogenous-policy/`; the PDF in the sitemap |
| 18 | 21 | Paper gates the release? | No |
| 19 | 22 | Activation spend | At most $10 per release candidate |
| 20 | 23 | Third-party pilots | Defer |
| 21 | new | tabputer-1 provisioning and staging | Authorize `augexp`, `augctl`, `augproxy`, `/srv/aug`, the `inet augexp` table and the proxy, all set up by you with sudo. You transfer bundles and receipts. Stage only run bundles and public data, accepting that root, your account and privileged k3s workloads can read them. No agent gets sudo or SSH there unless you grant it |
| 22 | new | Memory envelope and windows | One run at a time; 16 GB container cap; launch at MemAvailable ≥ 24 GB; abort below 6 GB; system updates held during windows; caps of E1 6 h, E4a 4 h, E3 24 GPU-h and M5 24 GPU-h. You confirm windows in which the k3s workloads leave ≥ 24 GB. About 16 GB is free today, so runs block until then |
| 23 | new | ROCm PyTorch wheel | The first of PyTorch stable ROCm, AMD release, or AMD gfx1151 builds that lists `gfx1151` and passes §4.4, on CPython 3.12. No `HSA_OVERRIDE_GFX_VERSION`. If none passes: CPU-only; E3 slips to 0.8.1; R3b stays untested. If one passes, R3b runs in M5 |
| 24 | new | Colab | No subscription. Consider it only if a named experiment needs CUDA-only kernels or more GPU memory than tabputer-1's envelope. It needs a per-experiment approval, because code and data would go to Google, in interactive notebooks. No current experiment needs it |

## Sources (delta from v2)

v2 rows 1–42 carry over, except these changes: v1 row 2 (repo at `4236a60`) and v2 row 34 (7118537)
are **superseded** by row 43; v2 rows 35 (Mac modes) and 36 (the patrol CLI) are **historical**.
v2 row 38 now points to `calc/calc_v2.py`.

| # | Source | Revision or time | Depth | Label |
|---|---|---|---|---|
| 43 | Coordinator facts: `origin/main` d8dc848; v0.7.2 → 30b6033; released byte counts; ignore location; Mac permissions; tabputer-1 inventory; maintainer decisions | 2026-09-23 | Relayed | Coord (refs cross-checked locally by this lane, unfetched) |
| 44 | Fable v2 review, `reviews/fable-5.1-xhigh-v2.md` | 2026-09-23 12:54 | Full | Mixed |
| 45 | Astra v2 review, final `codex` block, `reviews/astra-max-v2.raw.log` | Session 01a0cf9f…, 13:10 | Final block, full | Mixed |
| 46 | `calc/calc_v3.py` and `calc/calc_v3.out.txt` | This lane | Executed | Rep (arithmetic; synthetic populations [H]) |
| 47 | `compare_workflows.py` radius `sqrt(2(log K − log α)/n)` × bound; `check_repo.py` constants (16,000 / 180,000 B) | `d8dc848` | Targeted | C |
| 48 | Dataset sizes (CivilComments ~2.0M, CLINC150 23.9k, BANKING77 13.1k, HotpotQA dev 7,405) | Dataset cards, not re-read | — | C, recheck at M2 |
