import numpy as np
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt
print("--- PART C: change cooling term amplitude 10 -> 20 and tolerance ---")
f = lambda T,A=10: T-25-A*np.exp(-T/20)
for A in (10,20):
    s = root_scalar(lambda T: f(T,A), bracket=[20,60], method="bisect", xtol=1e-10); print(f"A={A}: equilibrium {s.root:.6f} C after {s.iterations} bisection iterations")
for tol in (1e-2,1e-6,1e-10):
    s = root_scalar(f, bracket=[20,40], method="bisect", xtol=tol); print(f"tol={tol:.0e}: root {s.root:.8f}, iterations {s.iterations}")
print("--- PART E: break-even point of a small business ---")
# revenue: price falls with volume. R(x)=80x-0.02x^2 ; cost C(x)=5000+12x+0.01x^2 ... profit P=R-C
def profit(x): return (80*x-0.02*x**2) - (5000+12*x+0.01*x**2)
s = root_scalar(profit, bracket=[1,1000], method="bisect", xtol=1e-8)
print(f"Break-even quantity (bisection): {s.root:.4f} units  ({s.iterations} iterations)")
print(f"Profit at break-even: {profit(s.root):.6f}; at 1000 units: {profit(1000):.2f}")
g = lambda x: (5000 + 0.01*x**2 + 0.02*x**2 - 68*x + 68*x - 0)  # placeholder not used
# fixed-point form: 68x - 0.03x^2 - 5000 = 0 -> x = (5000 + 0.03x^2)/68
gfp = lambda x: (5000+0.03*x**2)/68
x=100.0; its=0
while True:
    xn=gfp(x); its+=1
    if abs(xn-x)<1e-10 or its>500: break
    x=xn
print(f"Fixed-point break-even: {xn:.6f} after {its} iterations")
xs = np.linspace(0,2000,400); plt.plot(xs, profit(xs)); plt.axhline(0,color="k",lw=.8); plt.axvline(s.root,ls="--")
plt.xlabel("Units sold"); plt.ylabel("Profit (currency units)"); plt.title("Profit curve and break-even point"); plt.grid(True); plt.show()
