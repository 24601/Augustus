from math import comb, log, sqrt
from statistics import NormalDist
N=NormalDist()
def tail(n,p,k): return sum(comb(n,i)*p**i*(1-p)**(n-i) for i in range(k,n+1))
print("A/A n=20 p=.05: P>=1 %.4f P>=2 %.4f P>=3 %.4f" % (tail(20,.05,1),tail(20,.05,2),tail(20,.05,3)))
for k in range(5,10): print(" n=60 P>=%d %.4f" % (k, tail(60,.05,k)))
print(" zero-in-20 upper95 %.4f" % (1-0.05**(1/20)))
# power of A/A rule to detect inflated rate 0.20
print(" power n=20 reject>=3 when true .20: %.3f; when .15: %.3f" % (tail(20,.2,3), tail(20,.15,3)))
print(" power n=60 reject>=7 when true .20: %.3f; .15: %.3f" % (tail(60,.2,7), tail(60,.15,7)))
# Monte Carlo calibration: N reps, rate .05, 2SE
for R in (2000,4000): print(" MC R=%d SE %.4f" % (R, sqrt(.05*.95/R)))
# sign test counterexample
print(" sign ex: mean delta %.4f" % ((9*1-24*0.01)/300))
# inclusion prob example
print(" incl ex: sample delta %.3f pop %.3f" % ((10-50)/60,(950-50)/1000))
# TOST n: sigma of paired cost diff, margin delta, alpha per side a, power 0.8 at true 0
def n_tost(sigma,delta,a,power=.8):
    z1=N.inv_cdf(1-a); z2=N.inv_cdf(1-(1-power)/2)
    return ((z1+z2)*sigma/delta)**2
for s,d in ((0.10,0.004),(0.10,0.002),(0.05,0.002),(0.15,0.005)):
    print(" TOST sigma %.2f delta %.3f a=.01: n=%d" % (s,d,n_tost(s,d,0.01)))
# superiority n (one-sided) for E3
def n_sup(sigma,delta,a,power=.8):
    return ((N.inv_cdf(1-a)+N.inv_cdf(power))*sigma/delta)**2
for s,d,a in ((0.30,0.03,0.05/3),(0.30,0.02,0.05/3),(0.25,0.03,0.05/3)):
    print(" sup sigma %.2f delta %.2f a %.4f n=%d" % (s,d,a,n_sup(s,d,a)))
# Hoeffding n for strict improvement given delta, K
for d,K in ((0.05,1),(0.05,5)): print(" hoeff n", d, K, round(2*log(K/0.05)/d**2))
