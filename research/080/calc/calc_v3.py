"""Arithmetic behind plan-v3 (Augustus 0.8.0). Stdlib only; deterministic.

Run:  python3 calc_v3.py > calc_v3.out.txt
Every number here is planning arithmetic. Synthetic populations are labeled
[H]; nothing here is an experimental result.

Conventions (plan-v3 section 2.7, "Common rules"):
- Family rule: each contrast gets a two-sided (1 - alpha/m) CI. Superiority,
  inferiority, non-inferiority and equivalence are all read from it, so the
  probability of any false claim across the m contrasts is <= alpha.
  Critical value: z_{1 - alpha/(2m)}.
- Power target 0.8, stated once: TOST at true 0 uses z_{1-beta/2} = z_0.9;
  one-sided NI/superiority uses z_{1-beta} = z_0.8.
"""
from math import comb, erf, exp, lgamma, log, sqrt
import random
from statistics import NormalDist

ND = NormalDist()
z = ND.inv_cdf
Phi = ND.cdf
ALPHA = 0.05
POWER = 0.8
Z_TOST = z(1 - (1 - POWER) / 2)   # 1.2816
Z_ONE = z(POWER)                  # 0.8416


def zfam(m, alpha=ALPHA):
    return z(1 - alpha / (2 * m))


def n_tost(sigma, delta, m):
    return ((zfam(m) + Z_TOST) * sigma / delta) ** 2


def n_one(sigma, gap, m):
    """One-sided test read from the family CI; gap = distance from truth to bound."""
    return ((zfam(m) + Z_ONE) * sigma / gap) ** 2


def hoeffding_radius(n, k=1, alpha=ALPHA, rng=2.0):
    # Same as compare_workflows.py: sqrt(2*(log K - log alpha)/n) for range 2.
    return rng * sqrt(log(k / alpha) / (2 * n))


def eb_radius(s, n, k=1, alpha=ALPHA, rng=2.0):
    # Maurer-Pontil empirical Bernstein, one-sided, range rng, level alpha/k.
    d = alpha / k
    return s * sqrt(2 * log(2 / d) / n) + 7 * rng * log(2 / d) / (3 * (n - 1))


def min_n(power_fn, lo=50, hi=10_000_000):
    """Smallest n with power_fn(n) >= POWER (power_fn monotone in n)."""
    if power_fn(hi) < POWER:
        return None
    while lo < hi:
        mid = (lo + hi) // 2
        if power_fn(mid) >= POWER:
            hi = mid
        else:
            lo = mid + 1
    return lo


def log_binom_pmf(n, i, p):
    return lgamma(n + 1) - lgamma(i + 1) - lgamma(n - i + 1) + i * log(p) + (n - i) * log(1 - p)


def binom_cdf(n, x, p):
    if x < 0:
        return 0.0
    if x >= n:
        return 1.0
    return min(1.0, sum(exp(log_binom_pmf(n, i, p)) for i in range(0, x + 1)))


def binom_sf(n, x, p):
    """P(X >= x)."""
    return 1.0 - binom_cdf(n, x - 1, p)


def cp_upper(x, n, gamma):
    """One-sided Clopper-Pearson upper bound at level 1 - gamma."""
    if x >= n:
        return 1.0
    lo, hi = x / n, 1.0
    for _ in range(80):
        mid = (lo + hi) / 2
        if binom_cdf(n, x, mid) > gamma:
            lo = mid
        else:
            hi = mid
    return hi


def cp_lower(x, n, gamma):
    """One-sided Clopper-Pearson lower bound at level 1 - gamma."""
    if x <= 0:
        return 0.0
    lo, hi = 0.0, x / n
    for _ in range(80):
        mid = (lo + hi) / 2
        if binom_sf(n, x, mid) < gamma:
            lo = mid
        else:
            hi = mid
    return lo


def section(t):
    print()
    print("== " + t)


# ---------------------------------------------------------------------------
section("0. Family critical values z_{1-alpha/(2m)}, alpha=0.05")
for m in (1, 3, 6, 19, 38):
    print(f"  m={m:2d}: z={zfam(m):.4f}")
print(f"  power 0.8: z_TOST(1-beta/2)={Z_TOST:.4f}  z_one(1-beta)={Z_ONE:.4f}")

# ---------------------------------------------------------------------------
section("1. E1 planning on a synthetic calibrated population [H]")
# Scores p ~ Beta(a, b) with mean 0.08 (CivilComments toxicity>=0.5 prevalence
# is about 8% [H, recheck at M2]); y ~ Bernoulli(p), so scores are calibrated
# by construction. Concentration chosen to give AUC near 0.90 [H].
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
    ps, ys = draw(conc)
    a_ = auc(ps, ys)
    print(f"  concentration {conc}: AUC={a_:.3f} prevalence={sum(ys)/len(ys):.4f}")
    if best is None or abs(a_ - 0.90) < abs(best[1] - 0.90):
        best = (conc, a_, ps, ys)
conc, a_, ps, ys = best
print(f"  planning population: concentration {conc}, AUC {a_:.3f}")


def logit(p):
    p = min(max(p, 1e-12), 1 - 1e-12)
    return log(p / (1 - p))


def sig(x):
    return 1 / (1 + exp(-x))


eps_rng = random.Random(80_004)
TAUS = (0.10, 0.30)
eps = {t: [eps_rng.gauss(0, t) for _ in range(N_SYN)] for t in TAUS}
RATIOS = {"1:1": (1, 1), "1:4": (1, 4), "1:9": (1, 9), "1:19": (1, 19), "1:49": (1, 49), "4:1": (4, 1)}
M_E1 = 19
N_CONF_CIVIL = 1_600_000
N_CONF_CLINC = 12_850


def stats(d):
    n = len(d)
    mu = sum(d) / n
    var = sum((x - mu) ** 2 for x in d) / (n - 1)
    return mu, sqrt(var)


print(f"  family m={M_E1}; margin delta_r = 0.02 * cost_A(r); CivilComments conf n_max={N_CONF_CIVIL:,}; CLINC {N_CONF_CLINC:,}")
print("  ratio  cost_A  cost_Bst best_const delta_r | A-Bst: mean   sd    n_sup | C*~A tau=.1: sd  n_TOST | tau=.3: sd  n_TOST")
for name, (fp, fn) in RATIOS.items():
    cfp, cfn = fp / (fp + fn), fn / (fp + fn)
    t = cfp  # plug-in threshold C_FP/(C_FP+C_FN)

    def cost(flag, y):
        return cfp if (flag and not y) else (cfn if (y and not flag) else 0.0)

    cA = [cost(p >= t, y) for p, y in zip(ps, ys)]
    cB = [cost(p >= 0.5, y) for p, y in zip(ps, ys)]
    muA = sum(cA) / N_SYN
    muB = sum(cB) / N_SYN
    const = min(cfp * (1 - PREV), cfn * PREV)
    delta = 0.02 * muA
    dAB = [a - b for a, b in zip(cA, cB)]
    mAB, sAB = stats(dAB)
    gap = abs(mAB) - delta
    nsup = n_one(sAB, gap, M_E1) if gap > 0 else float("inf")
    row = f"  {name:5s} {muA:.4f}  {muB:.4f}   {const:.4f}   {delta:.5f} | {mAB:+.4f} {sAB:.4f} {nsup:9,.0f}"
    for tau in TAUS:
        cC = [cost(sig(logit(p) + e) >= t, y) for p, y, e in zip(ps, ys, eps[tau])]
        dCA = [c - a for c, a in zip(cC, cA)]
        _, sCA = stats(dCA)
        row += f" | {sCA:.4f} {n_tost(sCA, delta, M_E1):10,.0f}"
    print(row)
print("  Reading: n columns are per-ratio planning n; compare with n_max. Real sigma comes from the")
print("  calibration pilot at the analysis lock; this table only shows which ratios are plausibly powered.")

section("1b. Astra v2 counterexample: an estimated plug-in need not beat the stale threshold")
p_hat, p_true, cfp, cfn = 0.20, 0.05, 0.1, 0.9
loss_A = cfp * (1 - p_true) if p_hat >= cfp else cfn * p_true
loss_stale = cfp * (1 - p_true) if p_hat >= 0.5 else cfn * p_true
print(f"  A flags (p_hat {p_hat} >= t {cfp}): expected loss {loss_A:.3f}; stale t=0.5: {loss_stale:.3f}")

section("1c. E1-S prior-shift resample sizes")
for nconf in (N_CONF_CIVIL, 400_000):
    npos = PREV * nconf
    new_prior = min(3 * PREV, 0.5)
    print(f"  conf {nconf:,}: positives {npos:,.0f}; resample to prior {new_prior:.2f} -> n_S up to {npos/new_prior:,.0f}")
print("  CLINC equivalence is powered only if sigma/delta <= "
      f"{sqrt(N_CONF_CLINC)/(zfam(M_E1)+Z_TOST):.1f}; CivilComments if <= {sqrt(N_CONF_CIVIL)/(zfam(M_E1)+Z_TOST):.1f}")

# ---------------------------------------------------------------------------
section("2. E3 sample size: margin 0.02 utility, sigma 0.30 [H], power 0.8")
for m in (6, 3):
    n = n_tost(0.30, 0.02, m)
    print(f"  m={m}: z={zfam(m):.4f}; TOST n at true 0 = {n:,.0f}")
    for nc in (1_200, 3_500, 6_405):
        print(f"     half-width of (1-alpha/m) CI at n={nc:,}: {zfam(m)*0.30/sqrt(nc):.4f}")
for s in (0.25, 0.30, 0.35, 0.40, 0.45):
    print(f"  sigma {s:.2f}: n(m=6)={n_tost(s, 0.02, 6):,.0f}  n(m=3)={n_tost(s, 0.02, 3):,.0f}  (validation cap for confirmation 6,405)")
print("  Superiority read from the same CI, m=6: n to detect a true 0.04 gain beyond 0 margin"
      f" = {n_one(0.30, 0.04, 6):,.0f}; 0.03 gain = {n_one(0.30, 0.03, 6):,.0f}")

section("2b. E3 call budget (calls = questions x readers x 9)")
CALLS_PER_Q = 9  # 3 contexts x (answer, answerability score, implicit decision)
for label, nq, readers in (("planned 1,000 search + 3,500 conf, 2 readers", 4_500, 2),
                           ("max 1,000 + 6,405, 2 readers", 7_405, 2),
                           ("fallback 1,000 + 3,040, 1.7B only", 4_040, 1),
                           ("v2 (400 + 1,200) for comparison", 1_600, 2)):
    print(f"  {label:45s}: {nq*readers*CALLS_PER_Q:,} calls")

# ---------------------------------------------------------------------------
section("3. M5 non-inferiority at +0.01 (normalized cost in [0,1], paired range 2), K=3, power 0.8 at true 0")
MARGIN = 0.01
K_M5 = 3
print(f"  Reviewer checks: Hoeffding n for radius 0.01 at K=1: {2*log(1/ALPHA)/0.01**2:,.0f};"
      f" v2 E3 figure = one-sided superiority n at delta .03, alpha/3: {((z(1-ALPHA/3)+Z_ONE)*0.30/0.03)**2:,.0f}")
print("  Hoeffding (sigma-free radius):")
for n in (470, 3_400, 6_000, 15_000, 40_000, 60_000, 100_000):
    print(f"    n={n:7,d}: radius={hoeffding_radius(n, K_M5):.4f}")
for s in (0.10, 0.20, 0.30):
    nh = min_n(lambda n, s=s: Phi((MARGIN - hoeffding_radius(n, K_M5)) * sqrt(n) / s))
    print(f"    Hoeffding n for 80% power at true 0, sigma {s:.2f}: {nh:,}")
print("  Empirical Bernstein (Maurer-Pontil), radius uses sample sd ~ sigma:")
for s in (0.10, 0.15, 0.20, 0.25, 0.30, 0.35):
    ne = min_n(lambda n, s=s: Phi((MARGIN - eb_radius(s, n, K_M5)) * sqrt(n) / s))
    print(f"    sigma {s:.2f}: n={ne:,}")
print("  Binary 0/1 losses: sigma^2 ~= discordance q. q=2% -> sigma .141; 4% -> .200; 9% -> .300")
AVAIL = {"T2a BANKING77 (77-way)": 6_000, "T2b CLINC150 (+OOS), E1 partition": 12_850, "T2c CivilComments subsample": 40_000}
print("  Planned confirmation rows (after fit/dev/calibration):", AVAIL)
for task, nav in AVAIL.items():
    ok = [s for s in (0.10, 0.15, 0.20, 0.25, 0.30, 0.35)
          if (min_n(lambda n, s=s: Phi((MARGIN - eb_radius(s, n, K_M5)) * sqrt(n) / s)) or 10**9) <= nav]
    print(f"    {task}: EB powered at 0.01 for sigma in {ok if ok else 'none of the grid'}")
print("  A genuinely better low rung can still pass: at n=6,000, sigma .30, true Delta=-0.02,"
      f" EB power={Phi((MARGIN + 0.02 - eb_radius(0.30, 6_000, K_M5)) * sqrt(6_000) / 0.30):.3f}")

# ---------------------------------------------------------------------------
section("4. E4a qualification arithmetic")
# Astra v2 finding 5 reproduction.
R = 4_000
x = 224
lo95 = cp_lower(x, R, 0.025)
print(f"  v2 rule: 224/4000={x/R:.3f}; two-sided 95% CP lower={lo95:.4f} (passes 'lower <= alpha' though rate > alpha)")
xf = next(k for k in range(150, 400) if cp_lower(k, R, 0.025) > ALPHA)
pf = binom_sf(R, xf, ALPHA)
print(f"  v2 rule fails a valid 5% cell from {xf} adoptions: P={pf:.5f}; 30 cells: {1-(1-pf)**30:.3f}")
# v3 rule: simultaneous one-sided CP upper at gamma/C against alpha + tau.
C = 2 * 2 * 3 * 2 * 4 + 1 * 3 * 2 * 2   # hoeffding+EB: modes x methods x n x K x dists; sign_exact
print(f"  v3 cells C={C} (hoeffding, EB: 2 modes x 3 n x 2 K x 4 dists each; sign_exact: 3 n x 2 K x 2 binary dists)")
for R, tau in ((4_000, 0.005), (40_000, 0.005), (40_000, 0.010)):
    gam = 0.05 / C
    tol = ALPHA + tau
    xmax = max(k for k in range(int(ALPHA * R * 0.8), int(tol * R) + 1) if cp_upper(k, R, gam) <= tol)
    se = sqrt(ALPHA * (1 - ALPHA) / R)
    fail_nom = binom_sf(R, xmax + 1, ALPHA)
    fail_045 = binom_sf(R, xmax + 1, 0.045)
    det = {p: binom_sf(R, xmax + 1, p) for p in (0.06, 0.065, 0.075, 0.10)}
    print(f"  R={R:,} tau={tau}: MC SE at 5%={se:.5f}; qualify iff adoptions <= {xmax} ({xmax/R:.4f});"
          f" false-fail at exactly 5%: {fail_nom:.4f}/cell, at 4.5%: {fail_045:.2e}/cell;"
          f" detect " + ", ".join(f"{p:.3f}:{v:.3f}" for p, v in det.items()))
print("  Reading: the conservative bounds (Hoeffding, EB, exact sign) sit well below alpha at the boundary null,"
      " so their false-fail probability is far below the exactly-nominal figure; the diagnostic detects gross defects.")
# Boundary-null size of Hoeffding and EB under a normal approximation, to show conservatism.
for s in (0.10, 0.30, 1.00):
    for n in (300, 1_000, 2_500):
        rh = hoeffding_radius(n, 1)
        re = eb_radius(s, n, 1)
        print(f"   approx size at boundary null, sigma {s}, n {n}: Hoeffding {Phi(-rh*sqrt(n)/s):.2e}, EB {Phi(-re*sqrt(n)/s):.2e}")

section("4b. E4d agent A/A smoke test (carried from v2)")
tail = lambda n, p, k: sum(comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(k, n + 1))
print(f"  n=20, reject at >=3: P(null .05)={tail(20,.05,3):.4f}; power at .20={tail(20,.20,3):.3f}; zero-in-20 upper95={1-0.05**(1/20):.3f}")

# ---------------------------------------------------------------------------
section("5. tabputer-1 runtime budget [H: throughput assumptions, replaced by timing pilots]")
H = {  # tokens/s, aggregate, BF16 on gfx1151 via PyTorch ROCm [H]
    "qwen3-1.7b": {"prefill": 4_000, "decode": 800},
    "qwen3-4b": {"prefill": 1_600, "decode": 350},
    "qwen3.5-2b": {"prefill": 3_000, "decode": 600},
}
PREFILL_Q = 4_950   # 3 contexts (about 300/550/800 tokens) x 3 passes, no prefix reuse [H]
DECODE_Q = 60
for model in ("qwen3-1.7b", "qwen3-4b"):
    per_q = PREFILL_Q / H[model]["prefill"] + DECODE_Q / H[model]["decode"]
    print(f"  E3 {model}: {per_q:.2f} s/question; 4,500 q = {per_q*4_500/3600:.1f} h; 7,405 q = {per_q*7_405/3600:.1f} h")
cpu_prefill_4b = 60
print(f"  E3 qwen3-4b on CPU [H, {cpu_prefill_4b} tok/s prefill]: {PREFILL_Q/cpu_prefill_4b*4_500/3600:.0f} h for 4,500 q (not viable)")
# M5 R1 frozen readout (two label orders), qwen3.5-2b
rows = {"T2a": (13_083, 40), "T2b": (23_850, 40), "T2c": (80_000, 100), "T1": (6_000, 60)}
tot_tokens = sum(n * 2 * t for n, t in rows.values())
print(f"  M5 R1 readout tokens (2 orders, prompts prefix-cached) = {tot_tokens:,}; at 3,000 tok/s = {tot_tokens/3000/3600:.1f} h")
emb = 2_000_000 + 23_850 + 13_083 + 80_000
for label, rate in (("GPU [H] 5,000/s", 5_000), ("CPU 32 threads [H] 800/s", 800)):
    print(f"  MiniLM embeddings for {emb:,} texts, {label}: {emb/rate/60:.0f} min")
reps = C * 40_000
evals = reps * 3
print(f"  E4a: {reps:,} replications, ~{evals:,} helper evaluations at ~2.5 ms = {evals*0.0025/3600:.1f} CPU-h; /30 processes = {evals*0.0025/3600/30*60:.0f} min")
mem = {"E4a": 2, "E1": 10, "E3 1.7B": 6, "E3 4B": 12, "M5 R1 2B": 7, "M5 SetFit": 4, "M5 R3b DeBERTa (opt.)": 14}
print("  Peak memory per run, GB [H]:", mem, "-> container cap 16 GB; launch floor MemAvailable >= 24 GB")
