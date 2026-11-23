import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
print("--- PART C: change N, capacity and seed ---")
exact=norm.sf(1000,850,120); print(f"Exact (normal tail) probability = {exact:.4%}")
for N in (100,1000,10_000,100_000,1_000_000):
    d=np.random.default_rng(42).normal(850,120,N); print(f"N={N:>9,}: estimate {np.mean(d>1000):.4%}, abs error {abs(np.mean(d>1000)-exact):.4%}")
for seed in (1,2,3):
    d=np.random.default_rng(seed).normal(850,120,10_000); print(f"seed={seed}, N=10,000: {np.mean(d>1000):.4%}")
for cap in (900,1000,1100,1200):
    d=np.random.default_rng(42).normal(850,120,100_000); print(f"capacity={cap}: overload probability {np.mean(d>cap):.4%} (exact {norm.sf(cap,850,120):.4%})")
d=np.random.default_rng(42).normal(850,200,100_000); print(f"std 120 -> 200 at capacity 1000: {np.mean(d>1000):.4%}")
print("--- PART E: project deadline risk (three tasks, triangular durations in days) ---")
rng=np.random.default_rng(7); N=200_000
a=rng.triangular(4,6,12,N); b=rng.triangular(8,10,18,N); c=rng.triangular(3,5,9,N)
total=a+b+c; deadline=25
print(f"Mean total {total.mean():.2f} days, std {total.std():.2f}, 90th percentile {np.percentile(total,90):.2f} days")
print(f"P(total > {deadline} days) = {np.mean(total>deadline):.3%}")
print(f"Most-likely-sum (6+10+5) = 21 days, but mean is {total.mean():.1f} because durations are right-skewed")
plt.hist(total,bins=60,density=True); plt.axvline(deadline,color="r",ls="--",label="Deadline 25 days"); plt.xlabel("Total project duration (days)"); plt.ylabel("Density"); plt.title("Monte Carlo project duration"); plt.legend(); plt.grid(True); plt.show()
