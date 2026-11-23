import numpy as np, math
from decimal import Decimal
print("--- PART C: change tolerance and x values ---")
print("np.isclose(0.1+0.2, 0.3, rtol=0, atol=1e-20):", np.isclose(0.1+0.2, 0.3, rtol=0, atol=1e-20))
print("np.isclose(0.1+0.2, 0.3, rtol=0, atol=1e-15):", np.isclose(0.1+0.2, 0.3, rtol=0, atol=1e-15))
print("Gap |0.1+0.2-0.3| =", abs(0.1+0.2-0.3))
for x in [1e-10, 1e-14, 1e-16]:
    direct = (np.sqrt(1 + x) - 1) / x
    stable = 1 / (np.sqrt(1 + x) + 1)
    print(f"x={x:.0e}: direct={direct:.12f}, stable={stable:.12f}, direct rel.err={abs(direct-stable)/stable:.2e}")
approx = 1.41421356
print(f"More digits (1.41421356): abs err {abs(np.sqrt(2)-approx):.3e}, rel err {abs(np.sqrt(2)-approx)/np.sqrt(2):.3e}")
print("--- PART E: banking - adding 0.10 one million times ---")
s = 0.0
for _ in range(1_000_000): s += 0.10
print(f"Plain float sum   : {s!r}  error = {s-100000:.3e}")
print(f"math.fsum         : {math.fsum([0.10]*1_000_000)!r}")
d = sum([Decimal('0.10')]*1_000_000)
print(f"Decimal sum       : {d}")
print(f"Interest on 1,000,000.00 at 7.5%: float {1_000_000.00*0.075!r}; Decimal {Decimal('1000000.00')*Decimal('0.075')}")
