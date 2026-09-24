# Adversarial re-review of plan-v4.md — Fable lane, v4

## Reviewer identity and routing

- Requested routing: `claude-fable-5-xhigh` (this lane; the request named the Fable reviewer at
  xhigh effort).
- Observed identity, verbatim from my own environment/system prompt: "You are claude-fable-5-xhigh,
  a custom agent running in Amp." The effort marker `xhigh` appears only inside that agent name.
  No separate numeric reasoning-effort value is observable in this session; I state that plainly
  (the v3 lane could observe one; this one cannot).
- Date: 2026-09-24. Reviewed at HEAD `58be8b4e1bd0608029291f2cf711c7984084fcee`
  ("Add plan v4, its dispositions, and the v4 arithmetic") on `research/080-exopo-trainer`.
- SHA-256 of `research/080/plan/plan-v4.md`:
  `6102f850cbf94bb3da1f372127f660efcbea00d5a1e0ccf8400023d349483e50`.
- SHA-256 of `research/080/calc/calc_v4.py`:
  `4a2d2308f5f56533c056864f63342ebe2cb1f7dfda9b2a01c90bd2f88b4e8b80`; of
  `research/080/calc/calc_v4.out.txt`:
  `5d7e26442b0ef8f7c3ce1a2e4c04cfc70e5743c23c46e3b532d683d1a8050b7a`. Both match the prefixes in
  the plan's Sources row.

## What I read and what I executed

Read in full: `plan/plan-v4.md` (907 lines), `plan/plan-v4-dispositions.md`,
`plan/plan-v3-errata.md`, `reviews/fable-5.1-xhigh-v3.md`, `reviews/astra-max-v3.md`,
`receipts/m0-tabputer-1-2026-09-23.md`, `calc/calc_v4.py`, `calc/calc_v4.out.txt`,
repo `AGENTS.md`, `CONTRIBUTING.md`. Spot-read `plan/plan-v3.md` (confirmed L190 carries the
withdrawn "+154%/+364%") and the infra files (`infra/install.sh`, `infra/sbin/augwindow`,
`infra/nft/augexp.nft`) as text.

Executed:

1. `python3 research/080/calc/calc_v4.py` (Python 3.11.6, exit 0, ~30 s) and diffed against
   `calc_v4.out.txt`: **byte-identical**.
2. My own independent verification script (stdlib only, written from scratch; full source and
   output in the Appendix). It reproduces every number I rely on below, including the corrected
   E3 arithmetic, exact binomial tails, the Clopper–Pearson cutoff, and the E1 regret figures by
   analytic integration over the declared Beta(0.24, 2.76) population instead of the calc's
   simulation.
3. Greps of the infra scripts for forbidden host operations (`flush ruleset`, `pacman`, `reboot`,
   service restarts): none present. `install.sh` restarts only its own `augexp-nft.service` and
   stops its own dead-man timer; `augwindow` stops only `augproxy.service`. The `augproxy_out`
   nft chain contains the `ip daddr 127.0.0.53 … dport 53 accept` rule (the v3 P2-1 fix is
   installed, not just described).

Settled maintainer decisions (GPU-everything with Colab fallback; Jev everywhere except as
training data; PAW as a tested local arm; public research record) were treated as constraints and
are not re-litigated.

## Verdict

**NOT ACCEPTED - 0 P0, 2 P1, 8 P2**

Both P1s are localized and cheaply fixable; neither invalidates the plan's architecture. But both
sit on paths the M2 design lock would freeze (E3's R is explicitly part of the lock; the custody
path is M0b), so they must be fixed before execution, which is what P1 means here.

---

## Findings

### P1-A. E3's declared range R = 1.2 contradicts §2.4's own definition; the E3 EB intervals are anticonservative and every E3 planning number is wrong

Quote (§2.7 E3, Population row, L279):

> U = EM − λ·rounds/3 − μ·tokens/1000, **clipped to [−0.2, 1] at the design lock, so R = 1.2**

Quote (§2.4, L169–171, the binding definition):

> `s·sqrt(2 ln(2/δ)/n) + 7R ln(2/δ)/(3(n−1))`, with δ = α/(2m), s the sample sd of the paired
> differences and **R their range**.

Failure path. §2.4 defines R as the range of the **paired differences**, and E1 and M5 follow
that convention exactly (E1: "the paired difference has range R_r = 2·max(C_FP, C_FN)"; M5:
"Losses ∈ [0, 1], so paired differences have range R = 2"). E3's per-question utility is clipped
to [−0.2, 1], so the paired difference of two arms' utilities lies in [−1.2, +1.2]: its range is
**2.4, not 1.2**. The Maurer–Pontil bound requires the range of the variable the interval is on.
With R = 1.2 the bias term `7R ln(2/δ)/(3(n−1))` is exactly half its valid size, the interval is
too narrow, and the §2.4 coverage claim ("the probability of any false claim across the m
contrasts is at most α") does not hold for E3. Executed as written, E3 can certify equivalence or
non-inferiority (e.g. "proxy selection equivalent to outcome selection", P5) at less than the
stated coverage — a wrong, overclaimed result. M2 locks R, so the defect would be frozen into the
prereg hash.

All E3 planning numbers inherit the error. As written (R = 1.2) vs corrected (R = 2.4), from my
independent script (margin 0.02, power 0.8, planning at true Δ = 0; superiority at the 0.04 gap,
σ = 0.30):

| Quantity | Plan (R = 1.2) | Corrected (R = 2.4) |
|---|---|---|
| n_equiv, m = 6, σ = 0.25 | 5,178 | **6,598** (> 6,405 available) |
| n_equiv, m = 6, σ = 0.30 | 6,794 | **8,271** |
| n_equiv, m = 3, σ = 0.25 | 4,705 | **5,971** |
| n_equiv, m = 3, σ = 0.30 | 6,185 | **7,501** (> 6,405) |
| n_super, m = 6 | 1,830 | **2,498** |
| powered iff σ̂ ≤ (at n = 6,405, m = 6) | "about 0.29" (I get 0.2887) | **0.2437** |
| powered iff σ̂ ≤ (n = 6,405, m = 3) | 0.3068 | **0.2650** |

So under the corrected range, even σ̂ = 0.25 leaves the m = 6 equivalence rows unpowered on the
6,405 confirmation questions, and the prespecified narrowing to m = 3 is unpowered at σ̂ = 0.30.
The plan's stated feasibility ("powered only if σ̂ ≤ about 0.29") is materially wrong, not just
imprecise. Nothing becomes unreachable — the powered-set rule would route unpowered rows to
inconclusive — but the coverage defect stands on its own: an interval computed with R = 1.2 makes
claims it cannot support.

Minimum correction: set E3's R to the range of the paired differences (2.4 under the declared
clip), or declare per-arm bounds that genuinely imply a tighter difference range and justify them;
recompute calc §3; update the E3 n row and both σ̂ thresholds — all **before the M2 design lock**.
No other experiment is affected (E1 and M5 apply the convention correctly; I verified T2c's
1:4 costs give an actual difference range 1.6 ≤ the declared R = 2, which is conservative and
valid).

### P1-B. The custody path as written never delivers model weights to run containers; every GPU run is unreachable, and the obvious workaround reopens Astra v3 finding 1

Quote (§4.2, L587–593):

> Downloads land in `/srv/aug/quarantine`, owned by `augexp` during the window, together with the
> HF cache. At window close, `augwindow close` re-owns the whole tree to root with an ACL for
> `augctl` only, so `augexp` loses it. `augctl` then splits, hashes and publishes into
> `/srv/aug/stage/parts/<partition-id>/`, root-owned and read-only: fit and calibration partitions
> with labels, **confirmation inputs with labels removed**, and nothing else. Each run mounts only
> the partitions the design lock entitles it to.

Failure path. W1 and W2 downloads include model weights: the §4.4 acceptance weights (MiniLM,
Qwen3-1.7B), the E3 readers, the M5 readers (Qwen3.5-2B, SetFit body, DeBERTa-v3-large), PAW
checkpoints, and the A2b teacher — all landing in the quarantine tree "together with the HF
cache". At window close `augexp` loses the whole tree. What `augctl` publishes is data partitions
"and nothing else", and runs mount "only the partitions the design lock entitles it to". No
sentence in §4.2, §4.3 or §4.5 states how any weight file reaches a run container after window
close. Read literally, every model-loading run — §4.4 re-runs, E1 embedding, E3 decoding, all of
M5 — fails at load time: an unreachable experiment. The tempting implementation shortcut (leave
the HF cache readable to `augexp`) reopens Astra v3 finding 1, because W2's **dataset** downloads
(HF-hosted CivilComments/CLINC150/BANKING77/HotpotQA) land in the same cache, and B16 would then
(correctly) fail on "search every readable tree and the HF cache for the original labeled
corpus".

Minimum correction, either of:

- `augctl` verifies (checksums against the acquisition manifest, confirms label-free) and
  publishes weight snapshots into a named root-owned read-only tree, e.g.
  `/srv/aug/stage/weights/`, which runs may mount; add that tree to B16's search scope; or
- separate cache roots for datasets vs weights, with only the dataset root under quarantine
  custody, stated in §4.2.

Both preserve the isolation argument; the plan just has to pick one and say it. B16 already
searches the HF cache, so the corrected design stays testable as specified.

### P2-1. E4a's positive control states a wrong expected rate for skewed cells

Quote (§2.7 E4a, L296): "**Positive controls**, each naming the cell class that must fail (Fable
v3 P2-7): radius removed → every cell (size 0.50)".

Failure path: "size 0.50" holds only where the sample mean falls below the boundary with
probability ½ (symmetric distributions). For the rare-large distribution (0.98 jump w.p. 1e-4)
shifted to the boundary null, the radius-removed adoption rate is ≈ P(no event) — my script:
0.970 (n = 300), 0.905 (n = 1,000), 0.779 (n = 2,500) — not 0.50. The control still fails every
cell (all ≫ 0.055), so detection works; but a pre-registered expected rate that is wrong for a
named cell class invites a spurious "control anomaly" investigation or, worse, loosening the
check. Minimum correction: state "size 0.50 for symmetric cells; ≈ P(no event) ≥ 0.78 for
rare-large cells" or just "every cell fails".

### P2-2. The M2-time provenance/recheck items may require reading dataset text before the design lock is hashed

Quotes: M2 row (L829): "Design locks for E1, E3, E4 and M5, including R, g and the PAW/A1 arms;
BANKING77 provenance check"; §3.3 T2a (L396): "real-query provenance checked at M2"; E1 Data row
(L259): "about 2.0M rows [C, recheck at M2]"; precondition (L227): the design lock "precedes any
experiment-dataset download or **any read of dataset text or labels**".

Failure path: M2 both performs the checks and hashes the lock; if "provenance check" means
sampling actual BANKING77 rows (e.g. the HF viewer) or the row-count recheck means opening the
dataset, that is a read of dataset text before the lock — the exact class of contamination the
three-window design exists to prevent, reintroduced in miniature inside M2 itself. Minimum
correction: state that all M2-time checks use card/paper/metadata only, or move any text-sampling
check after the lock with a prespecified abort rule if it fails.

### P2-3. E3's (and E1's) inferential population is unstated, and full replay makes "unpowered" a category error under one reading

Quote (§2.7 E3 n row, L285): "confirmation the remaining 6,405 … the equivalence rows are powered
only if σ̂ ≤ about 0.29" — while P6 commits to full replay of all 6,405 questions, and E1 uses the
entire ~1.4M remainder as confirmation.

Failure path: when the whole finite confirmation set is enumerated and replayed
(batch-invariant mode fixes decoding), the finite-population Δ is known exactly and an EB
interval "unpowered" verdict is meaningless for that estimand; the powered/unpowered machinery is
coherent only for superpopulation inference (benchmark rows as i.i.d. draws from a
question-generating process). M5 states its population ("the population being the benchmark");
E1/E3 do not. An executor could report "inconclusive (unpowered)" about a quantity the run
measured exactly. Minimum correction: one sentence per experiment naming the estimand population
(superpopulation vs the enumerated set), and for the finite reading, report the exact Δ alongside
any interval.

### P2-4. B18 does not test the GTT allocation-burst race, and the launch-below-floor test method is unstated

Quotes: §4.5 Envelope (L698–700): "launch only at MemAvailable ≥ 24 GiB; abort below 6 GiB";
B18 (L657): "A run exceeding its declared GPU budget, and a run launched while MemAvailable is
below the floor → The budget aborts the allocation; the watchdog refuses the launch and kills a
run that crosses the abort floor." Receipt (measured, [Rep]): 24 GiB of GPU tensors held while the
container cgroup read 0.56 GiB — GTT is not charged to the cgroup; `dmem` untested.

Failure path: on this UMA APU a first-party bug (wrong `gpu_memory_utilization`, retry loop) can
allocate GTT faster than the watchdog samples (the sampling cadence is nowhere stated); between
samples MemAvailable can cross from above 6 GiB to exhaustion, and because GTT pages are not
attributed to the run's cgroup, the kernel OOM killer may select k3s/docker/sshd processes — harm
to the maintainer's host of exactly the kind §4.1 forbids. B18 as specified tests a slow budget
exceed and a low launch, not a burst. Separately, "a run launched while MemAvailable is below the
floor" has no stated test method; simulating it by actually pressuring host RAM would itself
endanger the host. Minimum correction: state the watchdog cadence; add a bounded first-party
burst sub-test (e.g. allocate at a declared rate toward a raised test floor, verify kill latency);
test the launch check by mocking the MemAvailable reading, never by consuming host memory; keep
one-run-at-a-time as the backstop it already is.

### P2-5. The plan points at an author-identity record that does not exist

Quote (L17): "Author | Revision lane, 2026-09-24. Requested routing: none stated to this lane.
**Observed identity recorded in the dispositions**."

Failure path: `plan-v4-dispositions.md` records the two reviewers' identities (its Inputs list)
but contains no observed-identity line for the v4 author lane; the provenance pointer dangles.
AGENTS.md requires recording requested routing separately from observable runtime identity.
Minimum correction: add the author lane's observed identity line to the dispositions (or state in
the plan that it was not observable).

### P2-6. Pretraining memorization of public benchmarks is an unclosable label-recovery route and deserves an explicit non-claim

Quote (§4.2, L592–593): "Complete labeled corpora never exist in any tree a candidate can read."

Failure path: M5 candidates on the model rungs embed pretrained LLMs; CLINC150, BANKING77 and
CivilComments labels are plausibly in their pretraining corpora, so a candidate can emit gold
labels having read no file — B16 cannot detect this by construction. The acceptance claims
survive because the population is declared to be the benchmark itself (memorized performance is
real performance on that population), but the quoted sentence invites reading the custody path as
label secrecy for public data, which it cannot provide. Minimum correction: a one-line §4.6
non-claim: filesystem custody prevents label *exfiltration from this host*, not knowledge of
public benchmarks; external validity is limited accordingly (the plan already says the latter for
M5).

### P2-7. A2a runs as an M5 arm but is outside the K = 5 family, so no error-controlled claim attaches to it; "powered task" is per contrast but the outcome rows speak per task

Quotes: Arms row (L395) lists "**A2a** PAW-standard via the local single-GPU compiler"; the test
row (L397): "Non-inferiority: EB UCB(Δ) < +0.01 over **K = 5** low rungs (R1, R2a, R2b, A1, A2b)";
outcome rows (L399/L401): "One low rung is non-inferior on every powered real task" / "R3a
superior to every low rung by more than 0.01 on a powered task".

Failure path: A2a's contrast is computed but sits outside the family, so any statement about
PAW-standard would carry no coverage guarantee; unlabeled, it will read as a finding. And
"powered" is decided per contrast (per rung's σ̂), so "a powered task" is ambiguous when a task is
powered for some rungs and not others; the intersection-union reading needs the per-contrast
powered set. Minimum correction: label A2a descriptive-only in the arms row, and define "powered
task" as "powered for the specific contrast in that row's quantifier".

### P2-8. A [Rep] label covers an independence assumption

Quote (E3 Readers row, L281): "batched reruns matched on only 59.8% of prompts in M0 [Rep]; over
9 calls a whole question replays identically with probability 0.0098 [Rep calc §6]".

Failure path: 0.598^9 = 0.0098 is arithmetic, but treating the 9 calls' identity events as
independent is a modeling assumption, not a measurement; per-question replay probability could be
much higher (correlated batch compositions) or lower. The number feeds the batch-invariant-mode
justification, which stands regardless. Minimum correction: "assuming independence across calls
[H]; the measured fact is the 59.8% per-prompt rate [Rep]".

---

## Prior-findings closure table

"Genuine" means the fix changes what an executor would do, not just the text.

| Prior finding | v4 disposition | Actually closed? |
|---|---|---|
| Fable P1-1 — design lock after downloads / contamination ordering | Three named windows W1–W3; M2 depends on "M0 decisions only" and is hashed before W2 opens; provisioning artifacts named non-experiment-data; §6.2 puts window receipts beside lock dates | **Closed, genuine.** The milestone graph really is re-ordered (M2 → M2b → M3) and the precondition now names "any read of dataset text or labels". Residual: P2-2 above (M2-time provenance checks may read text) |
| Fable P2-1 — proxy DNS egress | Allowlist + DNS to the systemd-resolved stub only | **Closed, genuine and installed** — verified `ip daddr 127.0.0.53 … dport 53 accept` in `infra/nft/augexp.nft` `augproxy_out` |
| Fable P2-2 — research record on tabputer-1 | Modified: record is public (maintainer decision D-c); site source may stage there | **Closed as modified**; hard host-safety rules preserved verbatim in §4.1 |
| Fable P2-3 — margins/power conventions unstated | Margins per experiment; g fixed at design lock; powered set from design-lock g and analysis-lock σ̂; calc §7 | **Closed, genuine** |
| Fable P2-4 — second fit subsample double-counted | fit-B 200k carved out; confirmation 1.4M; calc uses 1.4M | **Closed, genuine** |
| Fable P2-5 — disk exhaustion | B17: size-bounded fs for /srv/aug/runs and /srv/aug/pred; ENOSPC contained | **Closed, genuine** (and safe on the host) |
| Fable P2-6 — disclosure header | Release disclosure header row present | **Closed** |
| Fable P2-7 — positive controls name no cell class | Controls name cell classes; "inflated 100× → Hoeffding and EB cells at σ ≥ 0.3" matches the v3 appendix sizes; sign-flip named invisible to superiority mode | **Closed, genuine**, with one new nit: "(size 0.50)" is wrong for rare-large cells (P2-1 above) |
| Fable P2-8 — profile/boundary nits (pred group, B10 criterion, B14 containers, B5 regex, confirmation texts, calibrator identity) | `augpred` setgid group; B10 pass criterion corrected; B14 test containers; B5 regex + 12 matches in receipt; confirmation texts only after analysis lock; temperature no-intercept | **Closed, genuine** |
| Fable P2-9 — escalation asymmetry / T2c n rule / CLINC E1 decision | Escalation via EB LCB at the same α/(2K) tail; T2c n(σ̂) rule "not by discretion"; CLINC decision defined | **Closed, genuine** |
| Fable P2-10 — stale numbers (Mac row, +154%/+364%, R1 tokens) | Mac row removed; regrets recomputed as +95%/+216%/+553% [Rep calc §2]; v3 figures withdrawn by name | **Closed, genuine.** I verified the replacements analytically: +95%/+215%/+542% by exact integration over Beta(0.24, 2.76); the small 1:49 gap vs the calc's +553% is finite-sim noise of their frozen 300k draw, not an error |
| Astra 1 — data custody / candidate reads labels | Quarantine + split custody + B16 canary/join tests | **Closed in design, genuine — but P1-B above is a hole in the same section** (weights path unstated; the wrong fix reopens this finding). Must be resolved without weakening it |
| Astra 2 — interval collapse on zero observed variance | Two-sided empirical Bernstein at α/(2m) per tail; radius floor 7R ln(2/δ)/(3(n−1)); counterexample now refused (floor 0.002608 at n = 12,850, m = 19, R = 1.96 — verified) | **Closed for the method, genuine.** New defect P1-A is in E3's *application* (wrong R), not in the machinery |
| Astra 3 — window/lock ordering | Same as Fable P1-1 | **Closed** |
| Astra 4 — P6 replay shortfall (81,000 < needed) | Full replay; P6 population restricted to the 6,405 confirmation questions; 115,290 calls (2 readers); v3's plan withdrawn by name | **Closed, genuine** (calls arithmetic verified) |
| Astra 5 — disputed lineage / substring alias | Lineage by declaration, never name substring; fourth verdict state `disputed`; named approval preserves the allegation; both concrete cases are test rows | **Closed, genuine** |
| Astra 6 — skill refuses feasible low-variance case / accepts infeasible | S12a: required n 6,164 shown, refusal correct; S12b: σ̂ = 0.02 at 3,000 rows certifiable (radius 0.009737 < 0.01 — verified) | **Closed, genuine** |
| Astra 7 — stale memory-blocked state | Measured MemAvailable 121,366,040 kB [Coord]; state derived from launch measurement; watchdog | **Closed** |

## What v4 gets right

So the fixes do not over-correct:

- **The §2.4 machinery is sound.** The radius is exactly Maurer–Pontil Theorem 4 scaled to range
  R; per-tail δ = α/(2m) gives two-sided per-contrast coverage 1 − α/m and family coverage 1 − α
  by Bonferroni; on the joint coverage event every superiority, non-inferiority and equivalence
  claim read from the same two-sided interval is simultaneously true, so reading all three from
  one interval is valid (and conservative — no change needed). The intersection-union combination
  across M5 tasks is size-valid. The radius floor genuinely refuses the Astra counterexample
  (0.002608 ≫ the 5e-5 margin; 0.9999^12850 = 0.2766 and jointly 0.2049 both verified).
- **E1's R_r = 2·max(C_FP, C_FN) and M5's R = 2 are correct** applications of the
  paired-difference convention; T2c's declared R = 2 is conservative (actual 1.6). Only E3
  deviates (P1-A).
- **Every number I recomputed reproduces**, from my own implementations: tail levels; M5 n's
  6,671/14,035/25,535 and σ̂ thresholds 0.08/0.18/0.49 (0.0872/0.1870/0.4924); escalation n 4,181;
  S12a 6,164; S12b radius 0.009737; E4a cutoff 2,049 (CP upper 0.054975 vs 0.055001 at 2,050),
  fail probabilities 0.128 / 1.86e-9 / ≈1; E4a 108 cells, 1.08e10 elements, 19.07 MiB chunks,
  2,160 batches, 0.09–0.9 min; E4d 0.0755 and power 0.794; G0's 0.5^20 = 9.5e-7; 0.598^9 = 0.0098;
  decode 1.18 GPU-h; 133,290/115,290 calls; the Astra-case plug-in failure 0.095 vs 0.045;
  milestone sums 13–16 critical path and 22.5–27.5 total. `calc_v4.py` re-runs byte-identical.
- **The E1 regret replacements for v3's withdrawn figures are real**: analytic integration over
  the declared population gives +95%/+215%/+542% against the plan's +95%/+216%/+553% (frozen-draw
  sim noise at 1:49; direction and magnitude confirmed).
- **The window/lock re-ordering is a genuine fix**, not cosmetic: the dependency graph, the
  precondition wording, and the receipts-page layout all changed consistently.
- **The infra is host-safe as written**: no ruleset flush, no pacman, no reboot, no restarts of
  protected services; the dead-man timer protects SSH during nft installs; `augwindow` touches
  only `augproxy.service`. The DNS fix is installed.
- **Honesty is generally good**: §4.6 names dmem as untested and the watchdog as a stand-in;
  E4a is labeled a gross-defect detector with the coverage claim resting on theorems and
  exact-rational unit tests; T2a is pre-flagged as likely unpowered using my v3 σ estimate; the
  sign_exact CPU carve-out is recorded against D-b with a reason.

## Not covered

- I did not run `make check` or the repo's behavioral scenario suite; my only change is this file.
- I did not touch tabputer-1 or any host: no nft/podman/ROCm/watchdog testing; infra reviewed as
  text only. B1–B18 pass/fail claims were checked against the receipt's text, not re-executed.
- I did not re-run the v3 appendix Monte Carlo (E4a cell sizes at σ grid) — I verified the
  qualification arithmetic and the control-rate claims analytically instead.
- I did not fetch dataset cards, licenses, or arXiv sources; [C] and [R] rows were checked for
  label discipline, not against the external sources themselves.
- E1's population-dependent planning n's (e.g. 1,425/18,754) were verified only via the
  byte-identical calc re-run plus the analytic regret cross-check; I did not independently
  re-derive them from a fresh population draw.
- I did not audit the 0.7.2 skill code (`compare_workflows.py`) beyond the v3 review's findings;
  the "byte-identical to 0.7.2" regression claim is taken as a test obligation, not verified here.

## Appendix: independent verification script and output

```python
#!/usr/bin/env python3
"""Independent verification for the Fable v4 re-review of research/080/plan/plan-v4.md.

Written from scratch against the plan's stated formulas (Maurer-Pontil empirical
Bernstein, Bonferroni per-tail levels, exact binomial arithmetic, analytic
integration over the declared Beta population). Not derived from calc_v4.py
except for matching its stated conventions: POWER = 0.8, alpha = 0.05,
tail level alpha/(2m), planning at true Delta = 0 (equivalence/NI) or at the
stated gap (superiority).
"""
from math import erf, exp, lgamma, log, sqrt

ALPHA, POWER = 0.05, 0.8


def Phi(x):
    return 0.5 * (1.0 + erf(x / sqrt(2.0)))


def tail(m):
    return ALPHA / (2 * m)


def eb_rad(s, n, d, R):
    return s * sqrt(2 * log(2 / d) / n) + 7 * R * log(2 / d) / (3 * (n - 1))


def min_n(power, lo=50, hi=200_000_000):
    if power(hi) < POWER:
        return None
    while lo < hi:
        mid = (lo + hi) // 2
        if power(mid) >= POWER:
            hi = mid
        else:
            lo = mid + 1
    return lo


def n_equiv(sigma, margin, m, R):
    d = tail(m)

    def p(n):
        r = eb_rad(sigma, n, d, R)
        return 0.0 if r >= margin else 2 * Phi((margin - r) * sqrt(n) / sigma) - 1

    return min_n(p)


def n_super(sigma, gap, m, R):
    d = tail(m)

    def p(n):
        r = eb_rad(sigma, n, d, R)
        return 0.0 if r >= gap else Phi((gap - r) * sqrt(n) / sigma)

    return min_n(p)


def sigma_max_equiv(n, margin, m, R, lo=1e-4, hi=2.0):
    """Largest sigma with n_equiv(sigma) <= n (power >= 0.8 at that n)."""
    d = tail(m)

    def pw(s):
        r = eb_rad(s, n, d, R)
        return 0.0 if r >= margin else 2 * Phi((margin - r) * sqrt(n) / s) - 1

    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if pw(mid) >= POWER:
            lo = mid
        else:
            hi = mid
    return lo


print("== A. Tail levels ==")
for m in (19, 6, 5, 3):
    print(f"  m={m}: alpha/(2m) = {tail(m):.6f}")

print("\n== B. E3 as written (R=1.2) vs corrected (R=2.4) ==")
print("  plan: 'clipped to [-0.2, 1] ... so R = 1.2'; sec 2.4: R = range of the PAIRED DIFFERENCES")
print("  paired diff of two utilities in [-0.2,1] lies in [-1.2,+1.2] -> range 2.4")
for R in (1.2, 2.4):
    for m in (6, 3):
        row = ", ".join(
            f"sigma={s}: n={n_equiv(s, 0.02, m, R):,}" for s in (0.25, 0.30)
        )
        print(f"  R={R} m={m}: {row}")
    print(f"  R={R} m=6: n_super(gap 0.04, sigma 0.30) = {n_super(0.30, 0.04, 6, R):,}")
    print(f"  R={R} m=3: n_super(gap 0.04, sigma 0.30) = {n_super(0.30, 0.04, 3, R):,}")
for R in (1.2, 2.4):
    for m in (6, 3):
        print(
            f"  R={R} m={m}: powered-sigma threshold at n=6,405 = "
            f"{sigma_max_equiv(6405, 0.02, m, R):.4f}"
        )

print("\n== C. M5 (margin 0.01, R=2, K=5) ==")
for s in (0.10, 0.20, 0.30):
    print(f"  sigma={s}: n = {n_equiv(s, 0.01, 5, 2.0):,}")
for n in (6000, 12850, 40000, 60000):
    print(f"  powered-sigma threshold at n={n:,}: {sigma_max_equiv(n, 0.01, 5, 2.0):.4f}")
print(f"  escalate n_super(sigma 0.2, gap 0.02, m=5, R=2) = {n_super(0.2, 0.02, 5, 2.0):,}")

print("\n== D. S12 scenarios (K=3, margin 0.01, R=2) ==")
print(f"  S12a required n at sigma 0.10 (equiv convention): {n_equiv(0.10, 0.01, 3, 2.0):,}")
r = eb_rad(0.02, 3000, tail(3), 2.0)
print(f"  S12b EB radius at n=3,000, s=0.02: {r:.6f}  (<0.01: {r < 0.01})")

print("\n== E. Radius floor / Astra counterexample ==")
fl = eb_rad(0.0, 12850, tail(19), 1.96)
print(f"  s=0, n=12,850, m=19, R=1.96: radius = {fl:.6f} (plan: 0.0026)")
print(f"  0.9999^12850 = {0.9999**12850:.4f}; 0.9999^(12850+3000) = {0.9999**15850:.4f}")
print(f"  0.598^9 = {0.598**9:.4f};  0.5^20 = {0.5**20:.2e}")

print("\n== F. Exact binomial: E4a qualification and E4d ==")


def log_binom(n, k):
    return lgamma(n + 1) - lgamma(k + 1) - lgamma(n - k + 1)


def binom_cdf(x, n, p):
    lp, lq = log(p), log(1 - p)
    return sum(exp(log_binom(n, k) + k * lp + (n - k) * lq) for k in range(0, x + 1))


def binom_sf(x, n, p):  # P(X >= x)
    lp, lq = log(p), log(1 - p)
    return sum(exp(log_binom(n, k) + k * lp + (n - k) * lq) for k in range(x, n + 1))


def cp_upper(x, n, gamma):
    lo, hi = x / n, 1.0
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if binom_cdf(x, n, mid) > gamma:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


g = ALPHA / 108
print(f"  gamma per cell = 0.05/108 = {g:.6e}")
for x in (2049, 2050):
    print(f"  CP upper bound at x={x}, n=40,000: {cp_upper(x, 40000, g):.6f}")
print(f"  P(Bin(40000,0.050) >= 2050) = {binom_sf(2050, 40000, 0.050):.4f}   (plan: 0.128)")
print(f"  P(Bin(40000,0.045) >= 2050) = {binom_sf(2050, 40000, 0.045):.3e} (plan: 1.9e-9)")
print(f"  P(Bin(40000,0.060) >= 2050) = {binom_sf(2050, 40000, 0.060):.6f} (plan: ~1)")
print(f"  E4d P(Bin(20,0.05) >= 3) = {binom_sf(3, 20, 0.05):.4f} (plan 0.0755); "
      f"power at 0.20 = {binom_sf(3, 20, 0.20):.3f} (plan 0.79)")

print("\n== G. E4a arithmetic and rare-large control size ==")
cells = 2 * 2 * 3 * 2 * 4 + 2 * 3 * 2
elems = 108 * 40000 * 2500
print(f"  cells = {cells}; elements = {elems:.3e}; chunk MiB = {2000*2500*4/2**20:.2f}; "
      f"chunks = {108 * (40000 // 2000)}")
print(f"  minutes at 2e9/s: {elems/2e9/60:.2f}; at 2e8/s: {elems/2e8/60:.2f}")
for n in (300, 1000, 2500):
    print(f"  radius-removed size for mean-shifted rare-large (p=1e-4), n={n}: "
          f"P(no event) = {(1 - 1e-4)**n:.3f}  (plan says 'size 0.50')")

print("\n== H. E1 regret figures, analytic (Beta(0.24,2.76) population) ==")
A, B = 0.24, 2.76
lnB = lgamma(A) + lgamma(B) - lgamma(A + B)


def integrate(f, lo, hi, k=100_000):
    """Simpson on u in [lo,hi] of f(p(u)) * (1-p(u))^(B-1) / A with p = u^(1/A)."""
    if hi <= lo:
        return 0.0
    h = (hi - lo) / k

    def g(u):
        p = u ** (1 / A)
        return f(p) * (1 - p) ** (B - 1) / A

    s = g(lo) + g(hi)
    for i in range(1, k):
        s += g(lo + i * h) * (4 if i % 2 else 2)
    return s * h / 3


norm = integrate(lambda p: 1.0, 0.0, 1.0) / exp(lnB)
mean = integrate(lambda p: p, 0.0, 1.0) / exp(lnB)
print(f"  normalization check: {norm:.6f} (want 1); mean p = {mean:.4f} (want 0.08)")


def cost(t, cfp, cfn):
    ut = t ** A
    below = integrate(lambda p: cfn * p, 0.0, ut)          # p < t: abstain -> FN cost
    above = integrate(lambda p: cfp * (1 - p), ut, 1.0)    # p >= t: act -> FP cost
    return (below + above) / exp(lnB)


for cfp, cfn, name in ((0.1, 0.9, "1:9"), (0.05, 0.95, "1:19"), (0.02, 0.98, "1:49")):
    ca, cb = cost(cfp, cfp, cfn), cost(0.5, cfp, cfn)
    print(f"  {name}: cost_A(t=cfp) = {ca:.4f}, cost_B(t=0.5) = {cb:.4f}, "
          f"regret = +{100*(cb/ca - 1):.0f}%")

print("\n== I. Miscellaneous plan arithmetic ==")
print(f"  Astra-case plug-in failure: act loss 0.95*0.1 = {0.95*0.1:.3f}; "
      f"abstain loss 0.05*0.9 = {0.05*0.9:.3f}")
print(f"  E3 replay calls: 7,405*18 = {7405*18:,}; confirmation-only 6,405*18 = {6405*18:,}")
print(f"  decode hours: 133,290*64/2004/3600 = {133290*64/2004/3600:.2f}; "
      f"115,290 -> {115290*64/2004/3600:.2f}")
print(f"  E1 embed: 2.1e6 texts * 2.1 s/1000 = {2.1e6*2.1/1000/3600:.2f} h")
print(f"  critical path: 1+4+2+3+2+1 = {1+4+2+3+2+1} .. 1+5+2+4+3+1 = {1+5+2+4+3+1}")
print(f"  total agent-days: {1+4+1+0.5+2+2+3+2+6+1} .. {1+5+1+0.5+2+2+4+3+8+1}")
```

Output (Python 3.11.6):

```
== A. Tail levels ==
  m=19: alpha/(2m) = 0.001316
  m=6: alpha/(2m) = 0.004167
  m=5: alpha/(2m) = 0.005000
  m=3: alpha/(2m) = 0.008333

== B. E3 as written (R=1.2) vs corrected (R=2.4) ==
  plan: 'clipped to [-0.2, 1] ... so R = 1.2'; sec 2.4: R = range of the PAIRED DIFFERENCES
  paired diff of two utilities in [-0.2,1] lies in [-1.2,+1.2] -> range 2.4
  R=1.2 m=6: sigma=0.25: n=5,178, sigma=0.3: n=6,794
  R=1.2 m=3: sigma=0.25: n=4,705, sigma=0.3: n=6,185
  R=1.2 m=6: n_super(gap 0.04, sigma 0.30) = 1,830
  R=1.2 m=3: n_super(gap 0.04, sigma 0.30) = 1,649
  R=2.4 m=6: sigma=0.25: n=6,598, sigma=0.3: n=8,271
  R=2.4 m=3: sigma=0.25: n=5,971, sigma=0.3: n=7,501
  R=2.4 m=6: n_super(gap 0.04, sigma 0.30) = 2,498
  R=2.4 m=3: n_super(gap 0.04, sigma 0.30) = 2,243
  R=1.2 m=6: powered-sigma threshold at n=6,405 = 0.2887
  R=1.2 m=3: powered-sigma threshold at n=6,405 = 0.3068
  R=2.4 m=6: powered-sigma threshold at n=6,405 = 0.2437
  R=2.4 m=3: powered-sigma threshold at n=6,405 = 0.2650

== C. M5 (margin 0.01, R=2, K=5) ==
  sigma=0.1: n = 6,671
  sigma=0.2: n = 14,035
  sigma=0.3: n = 25,535
  powered-sigma threshold at n=6,000: 0.0872
  powered-sigma threshold at n=12,850: 0.1870
  powered-sigma threshold at n=40,000: 0.3922
  powered-sigma threshold at n=60,000: 0.4924
  escalate n_super(sigma 0.2, gap 0.02, m=5, R=2) = 4,181

== D. S12 scenarios (K=3, margin 0.01, R=2) ==
  S12a required n at sigma 0.10 (equiv convention): 6,164
  S12b EB radius at n=3,000, s=0.02: 0.009737  (<0.01: True)

== E. Radius floor / Astra counterexample ==
  s=0, n=12,850, m=19, R=1.96: radius = 0.002608 (plan: 0.0026)
  0.9999^12850 = 0.2766; 0.9999^(12850+3000) = 0.2049
  0.598^9 = 0.0098;  0.5^20 = 9.54e-07

== F. Exact binomial: E4a qualification and E4d ==
  gamma per cell = 0.05/108 = 4.629630e-04
  CP upper bound at x=2049, n=40,000: 0.054975
  CP upper bound at x=2050, n=40,000: 0.055001
  P(Bin(40000,0.050) >= 2050) = 0.1283   (plan: 0.128)
  P(Bin(40000,0.045) >= 2050) = 1.862e-09 (plan: 1.9e-9)
  P(Bin(40000,0.060) >= 2050) = 1.000000 (plan: ~1)
  E4d P(Bin(20,0.05) >= 3) = 0.0755 (plan 0.0755); power at 0.20 = 0.794 (plan 0.79)

== G. E4a arithmetic and rare-large control size ==
  cells = 108; elements = 1.080e+10; chunk MiB = 19.07; chunks = 2160
  minutes at 2e9/s: 0.09; at 2e8/s: 0.90
  radius-removed size for mean-shifted rare-large (p=1e-4), n=300: P(no event) = 0.970  (plan says 'size 0.50')
  radius-removed size for mean-shifted rare-large (p=1e-4), n=1000: P(no event) = 0.905  (plan says 'size 0.50')
  radius-removed size for mean-shifted rare-large (p=1e-4), n=2500: P(no event) = 0.779  (plan says 'size 0.50')

== H. E1 regret figures, analytic (Beta(0.24,2.76) population) ==
  normalization check: 1.000000 (want 1); mean p = 0.0800 (want 0.08)
  1:9: cost_A(t=cfp) = 0.0302, cost_B(t=0.5) = 0.0589, regret = +95%
  1:19: cost_A(t=cfp) = 0.0196, cost_B(t=0.5) = 0.0617, regret = +215%
  1:49: cost_A(t=cfp) = 0.0099, cost_B(t=0.5) = 0.0633, regret = +542%

== I. Miscellaneous plan arithmetic ==
  Astra-case plug-in failure: act loss 0.95*0.1 = 0.095; abstain loss 0.05*0.9 = 0.045
  E3 replay calls: 7,405*18 = 133,290; confirmation-only 6,405*18 = 115,290
  decode hours: 133,290*64/2004/3600 = 1.18; 115,290 -> 1.02
  E1 embed: 2.1e6 texts * 2.1 s/1000 = 1.23 h
  critical path: 1+4+2+3+2+1 = 13 .. 1+5+2+4+3+1 = 16
  total agent-days: 22.5 .. 27.5
```
