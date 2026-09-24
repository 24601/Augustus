"""Independent arithmetic for the v2 re-review. Stdlib only."""
from math import comb, log, sqrt
from statistics import NormalDist

N = NormalDist()
z = N.inv_cdf

print("== E4d binomial (n=20, p=.05)")
tail = lambda n, p, k: sum(comb(n, i) * p**i * (1 - p) ** (n - i) for i in range(k, n + 1))
print(f"  P(>=3)={tail(20,.05,3):.4f}  power@.20={tail(20,.20,3):.3f}  zero-in-20 upper95={1-0.05**(1/20):.3f}")
print(f"  E4a MC SE at 5%, R=4000: {sqrt(.05*.95/4000):.4f}")

print("== E4b sign case: 24 wins of 0.01 vs 9 losses of 1 in n=300")
p_one_sided = sum(comb(33, k) for k in range(0, 10)) / 2**33
print(f"  one-sided p={p_one_sided:.4f}; mean loss delta=+{(9-0.24)/300:.4f}")
print(f"  G0: 20 discordant all wins p={0.5**20:.2e}")

print("== E1 n rule: n=((z_{1-a/m}+z_0.9)*sigma/delta)^2, sigma=.10")
for m in (4, 5, 6, 13, 26):
    for d in (0.004, 0.002, 0.001):
        n = ((z(1 - 0.05 / m) + z(0.9)) * 0.10 / d) ** 2
        print(f"  m={m:2d} delta={d}: n={n:,.0f}")
print("  note: z_0.9 as the second term = TOST at 80% power, or one-sided superiority at 90%")

print("== E3: sigma=.30; declared margin 0.02; declared family m=6; plan n_conf=1,200")
for label, m, d, zp in (("plan text 'a/3, delta .03'", 3, 0.03, z(0.8)),
                        ("same at 90% power", 3, 0.03, z(0.9)),
                        ("margin .02, m=3, 80%", 3, 0.02, z(0.8)),
                        ("margin .02, m=6, 80% (TOST at true 0)", 6, 0.02, z(0.9)),
                        ("margin .02, m=6, 90% TOST", 6, 0.02, z(0.95))):
    n = ((z(1 - 0.05 / m) + zp) * 0.30 / d) ** 2
    print(f"  {label:40s}: n={n:,.0f}")
for m in (3, 6):
    hw = z(1 - 0.05 / m) * 0.30 / sqrt(1200)
    print(f"  (1-2a/m) CI half-width at n=1200, m={m}: {hw:.4f}  (margin 0.02 -> {'fits' if hw < 0.02 else 'does NOT fit even at true delta = 0'})")
print(f"  compute: 1200*6*2={1200*6*2:,}; (400+1200)*6*2={(1600)*6*2:,}")

print("== M5 non-inferiority at +0.01, normalized cost per case in [0,1] (paired diff range 2)")
a = 0.05
for n in (470, 800, 2000, 3400):
    hoeff = 2 * sqrt(log(1 / a) / (2 * n))
    # Maurer-Pontil empirical Bernstein, one-sided, range R=2, empirical sd s
    def eb(s, n=n, R=2):
        return s * sqrt(2 * log(2 / a) / n) + 7 * R * log(2 / a) / (3 * (n - 1))
    print(f"  n={n:5d}: Hoeffding radius={hoeff:.3f}; EB radius s=.10: {eb(.10):.3f}, s=.20: {eb(.20):.3f}, s=.30: {eb(.30):.3f}")
print(f"  Hoeffding n for radius 0.01: {4*log(1/a)/(2*0.01**2):,.0f}; for 0.05: {4*log(1/a)/(2*0.05**2):,.0f}")
# smallest n with EB radius <= 0.01 at s=0.10
n = 470
while True:
    s = .10
    r = s * sqrt(2 * log(2 / a) / n) + 7 * 2 * log(2 / a) / (3 * (n - 1))
    if r <= 0.01:
        break
    n += 10
print(f"  EB n for radius 0.01 at s=.10 (best case): {n:,}")

print("== E1 relative margin at extreme ratios: delta_r = 2% of A's cost")
for costA in (0.20, 0.10, 0.05, 0.03):
    d = 0.02 * costA
    n = ((z(1 - 0.05 / 13) + z(0.9)) * 0.10 / d) ** 2
    print(f"  A cost {costA:.2f} -> delta {d:.4f} -> n (m=13, sigma .10)={n:,.0f}")
