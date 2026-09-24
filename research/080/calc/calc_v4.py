"""Arithmetic behind plan-v4 (Augustus 0.8.0). Stdlib only; deterministic.

Run:  python3 calc_v4.py > calc_v4.out.txt

Every number here is planning arithmetic. Synthetic populations are labeled
[H]; nothing here is an experimental result. Host measurements quoted in
section 6 come from receipts/m0-tabputer-1-2026-09-23.md [Rep].

What changed from calc_v3.py
----------------------------
v3 read every claim type from a two-sided normal-theory (1 - alpha/m) CI,
with a paired percentile bootstrap below 500 discordances. Astra v3 finding 2
showed that neither interval has justified coverage for bounded, sparse,
rare-large loss differences: both collapse to [0, 0] when no nonzero paired
difference is observed, and then certify equivalence falsely. v4 therefore
reads every acceptance claim from a two-sided **empirical Bernstein** (EB)
interval for bounded losses (Maurer-Pontil), at family level alpha/(2m) per
tail. Its radius never collapses, because the second term depends only on the
range, n and the level. Normal-theory intervals remain as descriptive
reporting only and carry no error claim.

Section 1 reproduces Astra's counterexample and shows the EB radius on the
same data, so the fix is checked rather than asserted.
"""

from math import ceil, exp, lgamma, log, sqrt
import random
from statistics import NormalDist

ND = NormalDist()
z = ND.inv_cdf
Phi = ND.cdf
ALPHA = 0.05
POWER = 0.8


def section(t):
    print()
    print("== " + t)


# --- intervals --------------------------------------------------------------

def eb_radius(s, n, delta_tail, rng):
    """Maurer-Pontil empirical Bernstein radius, one tail at level delta_tail.

    s: sample sd of the paired differences; rng: their range (b - a).
    Holds for any bounded distribution; no distributional assumption.
    """
    return s * sqrt(2 * log(2 / delta_tail) / n) + 7 * rng * log(2 / delta_tail) / (3 * (n - 1))


def hoeffding_radius(n, delta_tail, rng):
    return rng * sqrt(log(1 / delta_tail) / (2 * n))


def tail_level(m, alpha=ALPHA):
    """Two-sided Bonferroni over m contrasts: alpha/(2m) per tail."""
    return alpha / (2 * m)


def min_n(power_fn, lo=50, hi=200_000_000):
    if power_fn(hi) < POWER:
        return None
    while lo < hi:
        mid = (lo + hi) // 2
        if power_fn(mid) >= POWER:
            hi = mid
        else:
            lo = mid + 1
    return lo


def n_equiv_eb(sigma, margin, m, rng):
    """Smallest n giving 80% power to certify |Delta| < margin at true Delta=0.

    Two-sided equivalence: BOTH endpoints must lie inside the margin. Use this
    only where the registered claim is equivalence (E1's C*~A rows, E3's
    equivalence rows). Non-inferiority is one-sided; see n_ni_eb.
    """
    d = tail_level(m)

    def power(n):
        rad = eb_radius(sigma, n, d, rng)
        if rad >= margin:
            return 0.0
        return 2 * Phi((margin - rad) * sqrt(n) / sigma) - 1

    return min_n(power)


def n_ni_eb(sigma, margin, m, rng, true_delta=0.0):
    """Smallest n for 80% power on the ONE-SIDED non-inferiority event
    UCB(Delta) < +margin, at the stated true_delta (default equality).

    Astra v4 F5A: v4 originally used the two-sided equivalence event for M5's
    declared NI rule. That is conservative for false positives but wrong for
    the registered selection rule, because it calls powered tasks unpowered.
    """
    d = tail_level(m)

    def power(n):
        rad = eb_radius(sigma, n, d, rng)
        slack = margin - true_delta - rad
        if slack <= 0:
            return 0.0
        return Phi(slack * sqrt(n) / sigma)

    return min_n(power)


def n_super_eb(sigma, gap, m, rng):
    """Smallest n for 80% power to certify superiority, where `gap` is the
    distance from the TRUE effect to the test boundary:

        gap = |true_delta| - margin        (Astra v4 F5B)

    `gap` is never the true effect itself. Callers compute it explicitly."""
    d = tail_level(m)

    def power(n):
        rad = eb_radius(sigma, n, d, rng)
        if rad >= gap:
            return 0.0
        return Phi((gap - rad) * sqrt(n) / sigma)

    return min_n(power)


# --- exact binomial ---------------------------------------------------------

def log_binom_pmf(n, i, p):
    return (lgamma(n + 1) - lgamma(i + 1) - lgamma(n - i + 1)
            + i * log(p) + (n - i) * log(1 - p))


def binom_cdf(n, x, p):
    if x < 0:
        return 0.0
    if x >= n:
        return 1.0
    return min(1.0, sum(exp(log_binom_pmf(n, i, p)) for i in range(x + 1)))


def binom_sf(n, x, p):
    return 1.0 - binom_cdf(n, x - 1, p)


def cp_upper(x, n, gamma):
    if x >= n:
        return 1.0
    lo, hi = x / n, min(1.0, x / n + 0.05)
    for _ in range(80):
        mid = (lo + hi) / 2
        if binom_cdf(n, x, mid) > gamma:
            lo = mid
        else:
            hi = mid
    return hi


# ---------------------------------------------------------------------------
section("0. Family levels (two-sided Bonferroni, alpha=0.05)")
for m in (1, 3, 5, 6, 19):
    print(f"  m={m:2d}: per-tail level alpha/(2m)={tail_level(m):.6f}"
          f"  normal z={z(1 - tail_level(m)):.4f}  ln(2/delta)={log(2/tail_level(m)):.4f}")

# ---------------------------------------------------------------------------
section("1. Astra v3 finding 2: the v3 intervals collapse; the EB interval does not")
P_RARE, D_RARE, N_CLINC = 0.0001, 0.98, 12_850
p_none = (1 - P_RARE) ** N_CLINC
p_none_pilot = (1 - P_RARE) ** 3_000
print(f"  rare-large difference: value {D_RARE} w.p. {P_RARE}, else 0; true mean"
      f" {P_RARE * D_RARE:.6f}; equivalence margin 0.00005")
print(f"  P(no nonzero difference in {N_CLINC:,} rows) = {p_none:.10f}")
print(f"  P(also none in a 3,000-row pilot)          = {p_none * p_none_pilot:.10f}")
print("  On that event the normal CI and the percentile bootstrap are both [0, 0]"
      " -> false equivalence.")
sd_true = sqrt(P_RARE * (1 - P_RARE)) * D_RARE
print(f"  true sd of that difference = {sd_true:.6f}")
for m, rng in ((19, 1.96), (19, 2.0)):
    d = tail_level(m)
    print(f"  EB radius at n={N_CLINC:,}, m={m}, range {rng}, observed sd 0:"
          f" {eb_radius(0.0, N_CLINC, d, rng):.6f}"
          f"  (observed sd {sd_true:.4f}: {eb_radius(sd_true, N_CLINC, d, rng):.6f})")
print("  Both exceed the 0.00005 margin by orders of magnitude, so EB reports"
      " 'unpowered/inconclusive' where v3 certified equivalence. That is the fix:")
print("  the radius floor 7*R*ln(2/delta)/(3(n-1)) cannot collapse with the sample.")
n_rare = n_equiv_eb(sd_true, 0.00005, 19, 1.96)
print(f"  n EB would need for that margin at sd {sd_true:.4f}: "
      f"{'infeasible (> 2e8)' if n_rare is None else format(n_rare, ',')}")

# ---------------------------------------------------------------------------
section("2. E1 planning under EB on the v3 synthetic calibrated population [H]")
rnd = random.Random(80_003)
PREV = 0.08
N_SYN = 300_000


def draw(conc):
    a, b = PREV * conc, (1 - PREV) * conc
    ps = [rnd.betavariate(a, b) for _ in range(N_SYN)]
    ys = [1 if rnd.random() < p else 0 for p in ps]
    return ps, ys


def auc(ps, ys):
    order = sorted(range(len(ps)), key=lambda i: ps[i])
    rank_sum, npos = 0, 0
    for r, i in enumerate(order, 1):
        if ys[i]:
            rank_sum += r
            npos += 1
    nneg = len(ps) - npos
    return (rank_sum - npos * (npos + 1) / 2) / (npos * nneg)


best = None
for conc in (1.0, 1.5, 2.0, 3.0):
    p_, y_ = draw(conc)
    a_ = auc(p_, y_)
    if best is None or abs(a_ - 0.90) < abs(best[1] - 0.90):
        best = (conc, a_, p_, y_)
conc, a_, ps, ys = best
print(f"  population: Beta concentration {conc}, AUC {a_:.3f}, prevalence"
      f" {sum(ys)/len(ys):.4f} (same seeds as calc_v3.py)")


def logit(p):
    p = min(max(p, 1e-12), 1 - 1e-12)
    return log(p / (1 - p))


def sig(x):
    return 1 / (1 + exp(-x))


eps_rng = random.Random(80_004)
TAUS = (0.10, 0.30)
eps = {t: [eps_rng.gauss(0, t) for _ in range(N_SYN)] for t in TAUS}
RATIOS = {"4:1": (4, 1), "1:1": (1, 1), "1:4": (1, 4),
          "1:9": (1, 9), "1:19": (1, 19), "1:49": (1, 49)}
M_E1 = 19
N_CONF_CIVIL = 1_400_000   # v4: a second 200k fit subsample is carved out (Fable v3 P2-4)
N_CONF_CLINC = 12_850


def stats(d):
    n = len(d)
    mu = sum(d) / n
    var = sum((x - mu) ** 2 for x in d) / (n - 1)
    return mu, sqrt(var)


print(f"  m={M_E1}; margin delta_r = 0.02*cost_A(r); range R_r = 2*max(C_FP,C_FN);"
      f" CivilComments confirmation {N_CONF_CIVIL:,}; CLINC {N_CONF_CLINC:,}")
print("  ratio  R_r   cost_A  delta_r  | A-Bstale: mean     sd   n_sup(EB) | C*~A tau=.1 sd  n_eq(EB) | tau=.3 sd  n_eq(EB)")
for name, (fp, fn) in RATIOS.items():
    cfp, cfn = fp / (fp + fn), fn / (fp + fn)
    t = cfp
    rng_r = 2 * max(cfp, cfn)

    def cost(flag, y):
        return cfp if (flag and not y) else (cfn if (y and not flag) else 0.0)

    cA = [cost(p >= t, y) for p, y in zip(ps, ys)]
    cB = [cost(p >= 0.5, y) for p, y in zip(ps, ys)]
    muA = sum(cA) / N_SYN
    delta = 0.02 * muA
    mAB, sAB = stats([a - b for a, b in zip(cA, cB)])
    # gap = |true effect| - superiority margin (delta_r), never the effect itself
    gap = abs(mAB) - delta
    nsup = n_super_eb(sAB, gap, M_E1, rng_r) if gap > 0 else None
    row = (f"  {name:5s} {rng_r:.2f}  {muA:.4f}  {delta:.5f} |"
           f" {mAB:+.4f} {sAB:.4f} {('n/a' if nsup is None else format(nsup, ',')):>12}")
    for tau in TAUS:
        cC = [cost(sig(logit(p) + e) >= t, y) for p, y, e in zip(ps, ys, eps[tau])]
        _, sCA = stats([c - a for c, a in zip(cC, cA)])
        neq = n_equiv_eb(sCA, delta, M_E1, rng_r)
        row += f" | {sCA:.4f} {('infeasible' if neq is None else format(neq, ',')):>12}"
    print(row)
print("  Claim P1 regret of the stale 0.5 threshold on THIS population (Fable v3 P2-10):")
for name, (fp, fn) in (("1:9", (1, 9)), ("1:19", (1, 19)), ("1:49", (1, 49))):
    cfp, cfn = fp / (fp + fn), fn / (fp + fn)

    def cost2(flag, y, cfp=cfp, cfn=cfn):
        return cfp if (flag and not y) else (cfn if (y and not flag) else 0.0)

    muA = sum(cost2(p >= cfp, y) for p, y in zip(ps, ys)) / N_SYN
    muB = sum(cost2(p >= 0.5, y) for p, y in zip(ps, ys)) / N_SYN
    print(f"    {name:5s}: cost_A {muA:.4f}  cost_B-stale {muB:.4f}  regret {muB/muA - 1:+.0%}"
          f"  (v3 text said +154%/+364% from an earlier population)")
print(f"  Powered iff the planning n fits {N_CONF_CIVIL:,} (CivilComments) or"
      f" {N_CONF_CLINC:,} (CLINC). sigma-hat at the analysis lock decides; this is planning only.")

# ---------------------------------------------------------------------------
section("3. E3 under EB: margin 0.02 utility; utility clipped to [-0.2, 1], so the PAIRED"
        " DIFFERENCE range is R = 2.4")
# Astra v4 F1 / Fable v4 P1-A: v4 first declared R = 1.2, the range of ONE utility.
# Two utilities in an interval of width w differ by up to +/- w, so R = 2w = 2.4.
R_E3 = 2.4
N_E3_CONF = 6_405
for m in (6, 3):
    for s_ in (0.20, 0.25, 0.30, 0.35):
        n = n_equiv_eb(s_, 0.02, m, R_E3)
        fits = "" if n is None else ("  fits 6,405" if n <= N_E3_CONF else "  EXCEEDS 6,405")
        print(f"  m={m} sigma={s_:.2f}: n_equiv(EB) = "
              f"{'infeasible' if n is None else format(n, ',')}{fits}")
    hi = None
    for i in range(10, 45):
        n = n_equiv_eb(i / 100, 0.02, m, R_E3)
        if n is not None and n <= N_E3_CONF:
            hi = i / 100
    print(f"  m={m}: equivalence rows are powered at n={N_E3_CONF:,} only if sigma-hat <= {hi}")
    # superiority: gap = |true effect| - margin
    for true_delta in (0.04, 0.06):
        gap = true_delta - 0.02
        print(f"    m={m} true gain {true_delta}: gap = {gap:.2f} beyond the 0.02 margin ->"
              f" n_super(EB) = {format(n_super_eb(0.30, gap, m, R_E3), ',')} at sigma 0.30")
print("  (v4's first pass printed 'n_super at a true 0.04 gain' while passing 0.04 as the gap,")
print("   which is a true gain of 0.06. Astra v4 F5B.)")
print("  HotpotQA distractor validation has 7,405 questions; v4 reserves 1,000 for search,")
print(f"  leaving {N_E3_CONF:,} for confirmation. P6 needs full replay (Astra v3 finding 4):")
for label, nq, readers in (("full replay, 2 readers", 7_405, 2),
                           ("full replay, 1.7B only", 7_405, 1)):
    print(f"    {label:28s}: {nq*readers*9:,} calls")
print(f"    v3 'planned' 4,500 x 2 x 9  : {4500*2*9:,} calls (short by"
      f" {7405*2*9 - 4500*2*9:,}; v4 drops it)")
print("  v4 restricts P6's finite population to the 6,405 confirmation questions, which the")
print(f"    search set never touched: {6405*2*9:,} of those calls (2 readers),"
      f" {6405*9:,} under the 1.7B-only narrowing.")

# ---------------------------------------------------------------------------
section("4. M5 under EB: ONE-SIDED non-inferiority at +0.01, normalized cost in [0,1] so R=2")
# Astra v4 F5A (one-sided NI, not equivalence) and F6 / Fable v4 P2-7 (A2a belongs in
# the confirmatory family, so K = 6, not 5).
R_M5 = 2.0
M5_MARGIN = 0.01
for K in (5, 6):
    for s_ in (0.10, 0.20, 0.30):
        n_ni = n_ni_eb(s_, M5_MARGIN, K, R_M5)
        n_eq = n_equiv_eb(s_, M5_MARGIN, K, R_M5)
        print(f"  K={K} sigma={s_:.2f}: n_NI(one-sided) = {format(n_ni, ',')}"
              f"   [v4's first pass used the two-sided equivalence event: {format(n_eq, ',')}]")
    for avail, nm in ((6_000, "T2a BANKING77"), (12_850, "T2b CLINC150"),
                      (40_000, "T2c 40k"), (60_000, "T2c 60k")):
        best = None
        for i in range(5, 90):
            if n_ni_eb(i / 100, M5_MARGIN, K, R_M5) <= avail:
                best = i / 100
        print(f"    K={K} {nm} at n={avail:,}: powered up to sigma {best if best else 'none'}")
print("  K=6 is the v4 low-rung family: R1, R2a, R2b, A1, A2a (PAW-standard), A2b (PAW-ft).")
print("  Escalation uses the matching one-sided LCB at the same tail level.")
print("  Superiority of R3a over a low rung, margin 0.01:")
for true_delta in (0.02, 0.03):
    gap = true_delta - M5_MARGIN
    print(f"    true gain {true_delta} -> gap {gap:.2f}: n_super(EB, K=6, sigma 0.20) ="
          f" {format(n_super_eb(0.20, gap, 6, R_M5), ',')}")

section("4b. Scenario S12 (Astra v4 F8): planning n vs an OBSERVED certification")
for sd in (0.10, 0.02):
    n_req = n_ni_eb(sd, M5_MARGIN, 3, R_M5)
    rad = eb_radius(sd, 3_000, tail_level(3), R_M5)
    print(f"  K=3, n=3,000, sd {sd:.2f}: EB radius {rad:.6f}; planning n for 80% NI power"
          f" at equality = {format(n_req, ',')}")
    for observed_mean in (0.0, 0.005):
        ucb = observed_mean + rad
        print(f"    observed mean {observed_mean:+.3f} -> UCB {ucb:.6f} ->"
              f" {'NI certified' if ucb < M5_MARGIN else 'not certified'}")
print("  So S12 must state the OBSERVED mean, not only n and sd: at sd 0.02 a mean of 0 certifies")
print("  and a mean of +0.005 does not, on identical n and sd.")

# ---------------------------------------------------------------------------
section("5. E4a on the GPU (errata D-b): cells, replications, qualification cutoff")
C_CELLS = 2 * 2 * 3 * 2 * 4 + 3 * 2 * 2
R_REPS = 40_000
gamma = ALPHA / C_CELLS
xmax = max(k for k in range(2_000, 2_100) if cp_upper(k, R_REPS, gamma) <= 0.055)
print(f"  cells C={C_CELLS}; replications per cell R={R_REPS:,};"
      f" total replications {C_CELLS*R_REPS:,}")
print(f"  qualify iff adoptions <= {xmax:,} (CP upper {cp_upper(xmax, R_REPS, gamma):.5f}"
      f" <= 0.055; {xmax+1} -> {cp_upper(xmax+1, R_REPS, gamma):.5f})")
for p in (0.045, 0.05, 0.06):
    print(f"    P(cell fails | true rate {p}) = {binom_sf(R_REPS, xmax+1, p):.3e}")
# GPU feasibility: the diagnostic is a reduction over an (R x n) loss matrix.
MAX_N = 2_500
elems = C_CELLS * R_REPS * MAX_N
print(f"  vectorized form: at most {C_CELLS} x {R_REPS:,} x {MAX_N:,} ="
      f" {elems:,} sampled losses")
print(f"    fp32 bytes if fully materialized: {elems*4/2**30:,.1f} GiB -> must be chunked")
CHUNK_ROWS = 2_000
print(f"    chunk of {CHUNK_ROWS:,} replications x {MAX_N:,} fp32 ="
      f" {CHUNK_ROWS*MAX_N*4/2**20:.1f} MiB; {ceil(R_REPS/CHUNK_ROWS)} chunks per cell,"
      f" {C_CELLS*ceil(R_REPS/CHUNK_ROWS):,} kernel batches total")
for rate in (2e9, 2e8):
    print(f"    at {rate:.0e} sampled-loss elements/s on gfx1151 [H]:"
          f" {elems/rate/60:.1f} min")
print("    v3's stdlib CPU path was 9.0 CPU-h. v4 caps E4a at 1 GPU-h wall clock;")
print("    exceeding it is a prespecified narrowing to n in {300, 1,000} only.")
section("5b. E4a positive-control expected rates per cell class (Astra v4 F11 / Fable v4 P2-1)")
print("  'radius removed -> every cell at size 0.50' is false for skewed and multi-finalist cells:")
p_rare = (1 - 0.0001) ** 300
print(f"    rare-large, mean-zero difference at n=300, strict acceptance below 0:"
      f" adoption = P(no rare event) = {p_rare:.6f}, not 0.50")
print(f"    a symmetric continuous cell at K=5, any-of-five adoption, independent finalists:"
      f" {1 - 0.5 ** 5:.5f}, not 0.50")
print("    sign_exact has no radius to remove, so the mutation does not apply; it needs its own")
print("    mutation (for example, dropping the discordant-pair restriction).")
print("  Each detecting cell therefore pre-registers its own expected rate, with the loss")
print("  distribution, the margin and the assumed joint dependence stated.")

print("  sign_exact cells stay exact-rational on the CPU: their qualification rests on the")
print("  exact binomial above, not on sampling. That is the one recorded CPU step (D-b).")

# ---------------------------------------------------------------------------
section("6. Host envelope from the M0 receipt [Rep] and what it changes")
VLLM_TOKS = 2_004          # measured batched output tok/s, Qwen3-1.7B bf16
BATCH_IDENTITY = 0.598     # measured batched-rerun identity
print(f"  measured vLLM batched output throughput: {VLLM_TOKS:,} tok/s"
      f" (v3 assumed 800 tok/s decode, unbatched measured 15.1 tok/s)")
TOK_PER_CALL = 64
for label, nq, readers in (("E3 full replay, 2 readers", 7_405, 2),
                           ("E3 full replay, 1.7B only", 7_405, 1)):
    calls = nq * readers * 9
    hours = calls * TOK_PER_CALL / VLLM_TOKS / 3600
    print(f"    {label:28s}: {calls:,} calls x {TOK_PER_CALL} output tok ="
          f" {hours:.1f} GPU-h of decode at the measured rate (cap 24 GPU-h)")
print(f"  MEASURED [Rep]: batched-rerun identity {BATCH_IDENTITY:.1%} PER PROMPT.")
print(f"  HYPOTHETICAL [H]: if the 9 calls of a question were independent with that marginal,"
      f" a whole question would replay identically with probability {BATCH_IDENTITY**9:.4f}.")
print("    M0 measured neither the joint law nor a cure: its smoke test resubmitted the SAME")
print("    prompt list and still disagreed, so a fixed input batch is not an established fix.")
print("    v4's mechanism is therefore frozen once-generated replay tables that every arm,")
print("    resplit and P6 draw reads, with the batch-invariant setting recorded at the lock.")
GPU_VISIBLE = 124.0
for label, need in (("E1 MiniLM embed", 2.0), ("E3 Qwen3-1.7B + 4B", 14.0),
                    ("M5 R1 Qwen3.5-2B", 6.0), ("M5 PAW-ft (compile-by-training)", 38.0),
                    ("M5 SetFit / DeBERTa-v3-large", 10.0)):
    print(f"    GPU budget {label:34s}: {need:5.1f} GiB ="
          f" gpu_memory_utilization {need/GPU_VISIBLE:.3f} of {GPU_VISIBLE:.0f} GiB visible")
print("  CPU cgroup stays --memory=16g --memory-swap=16g; GTT is NOT charged to it (B12, M0).")
print("  Aggregate admission (Astra v4 F3): MemAvailable must cover")
print("    GPU budget + CPU cap + declared service memory + 8 GiB overhead + 6 GiB reserve.")
for label, gpu, svc in (("E1 MiniLM embed", 2.0, 0.0), ("E3 readers", 14.0, 0.0),
                        ("M5 PAW-ft + local teacher", 38.0, 9.0)):
    print(f"    {label:26s}: {gpu:.0f} + 16 + {svc:.0f} + 8 + 6 = {gpu + 16 + svc + 8 + 6:.0f} GiB free required")
print("  The 24 GiB figure survives only as an absolute floor below which nothing launches.")
print("  Watchdog cadence 500 ms. The allocator limits are per-process/per-instance and are NOT")
print("  an enforced aggregate bound, which is why unrestricted GPU candidates go to Colab")
print("  unless the dmem cgroup controller is shown to bound amdgpu GTT (test B19).")

# ---------------------------------------------------------------------------
section("7. Distance to the tested boundary (Fable v3 P2-3; Astra v4 F5B and R1)")
print("  Three quantities, never conflated. `true_delta` is the planning effect (negative is")
print("  better), `margin` is the tested boundary, and the SIGNED DISTANCE from the truth to")
print("  that boundary is what the power calculation uses:")
print("    non-inferiority  (UCB < +margin): distance = margin - true_delta")
print("    superiority      (UCB < -margin): distance = -margin - true_delta = |true_delta| - margin")
print("                                      for a candidate better by |true_delta|")
print("    equivalence at equality:          distance = margin on each side")
print("  v4's first pass wrote 'g = 0 for equivalence and non-inferiority', and then also called")
print("  the true effect g for superiority. Both are corrected here and in the plan.")


def distance(mode, true_delta, margin):
    if mode == "ni":
        return margin - true_delta
    if mode == "sup":
        return abs(true_delta) - margin
    return margin  # equivalence at equality


ROWS = (
    # name, mode, true_delta, margin, sigma, m, range
    ("E1 A vs B-stale (sup)", "sup", -0.042, 0.02, 0.05, 19, 2.0),
    ("E3 explicit vs implicit (sup)", "sup", -0.04, 0.02, 0.30, 6, R_E3),
    ("E3 narrowed, 1 reader (sup)", "sup", -0.04, 0.02, 0.30, 3, R_E3),
    ("M5 R3a vs low rung (sup)", "sup", 0.02, 0.01, 0.20, 6, R_M5),
    ("M5 low rung NI (ni)", "ni", 0.0, 0.01, 0.20, 6, R_M5),
    ("E3 equivalence (equiv)", "equiv", 0.0, 0.02, 0.25, 6, R_E3),
)
for name, mode, td, margin, sigma, m, rng in ROWS:
    d = distance(mode, td, margin)
    if mode == "sup":
        n = n_super_eb(sigma, d, m, rng)
    elif mode == "ni":
        n = n_ni_eb(sigma, margin, m, rng, true_delta=td)
    else:
        n = n_equiv_eb(sigma, margin, m, rng)
    print(f"    {name:32s} true_delta={td:+.3f} margin={margin:.2f} -> distance {d:+.3f};"
          f" sigma={sigma} m/K={m} R={rng}: n = {'infeasible' if n is None else format(n, ',')}")
print("  The analysis lock records sigma-hat and the resulting powered set; it never re-chooses")
print("  true_delta or the margin, so the powered set has no post-calibration free parameter.")

section("7b. Exact sigma-hat boundaries (Astra v4 R6): the powered rule is n(sigma-hat) <= available")
print("  The 0.01-grid figures quoted in prose are ROUNDED-DOWN illustrations, not the rule.")


def max_sigma(fn, available, lo=0.01, hi=1.0):
    for _ in range(60):
        mid = (lo + hi) / 2
        n = fn(mid)
        if n is not None and n <= available:
            lo = mid
        else:
            hi = mid
    return lo


print(f"    E3 equivalence, m=6, R={R_E3}, n=6,405: exact sigma-hat boundary"
      f" {max_sigma(lambda s_: n_equiv_eb(s_, 0.02, 6, R_E3), 6_405):.8f} (prose says 0.24)")
print(f"    E3 equivalence, m=3, R={R_E3}, n=6,405: exact"
      f" {max_sigma(lambda s_: n_equiv_eb(s_, 0.02, 3, R_E3), 6_405):.8f} (prose says 0.26)")
print(f"    M5 NI, K=6, R={R_M5}, n=60,000: exact"
      f" {max_sigma(lambda s_: n_ni_eb(s_, 0.01, 6, R_M5), 60_000):.8f} (prose says 0.53)")
print("  A contrast is powered iff its computed n at the observed sigma-hat fits the available n.")
print("  The prose figures never decide; the computation does.")

# ---------------------------------------------------------------------------
section("8. Hoeffding comparison (kept as the conservative default where it is powered)")
for n in (6_000, 12_850, 60_000, 1_400_000):
    print(f"  n={n:9,}: Hoeffding radius (m=19, R=2) ="
          f" {hoeffding_radius(n, tail_level(19), 2.0):.5f};"
          f" EB at sd 0.05 = {eb_radius(0.05, n, tail_level(19), 2.0):.5f}")
print("  EB beats Hoeffding once the observed sd is small, which is why v4 makes EB the")
print("  default and keeps Hoeffding available for byte-identical regression only.")
