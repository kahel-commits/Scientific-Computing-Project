from scipy.optimize import root_scalar
def make(cf):
    npv = lambda r: sum(c/(1+r)**t for t,c in enumerate(cf))
    d = lambda r: sum(-t*c/(1+r)**(t+1) for t,c in enumerate(cf) if t>0)
    return npv, d
print("--- PART C: change cash flows and starting guess ---")
cf2 = [-10000,2500,3000,3500,2500]
npv,d = make(cf2)
n = root_scalar(npv, fprime=d, x0=0.10, method="newton"); print(f"Lower inflows {cf2}: IRR {n.root:.4%} ({n.iterations} its)")
cf = [-10000,3000,3500,4000,2500]; npv,d = make(cf)
for x0 in (0.0,0.5,1.0):
    try:
        n = root_scalar(npv, fprime=d, x0=x0, method="newton"); print(f"Original flows, Newton x0={x0}: IRR {n.root:.4%} ({n.iterations} its)")
    except Exception as e: print(f"Newton x0={x0}: failed ({e})")
print("--- PART E: effective cost of a loan (find monthly interest rate) ---")
principal = 100000; payment = 5000; months = 24
f = lambda r: principal - payment*(1-(1+r)**-months)/r
df = lambda r: -payment*( (months*(1+r)**(-months-1))/r - (1-(1+r)**-months)/r**2 )
n = root_scalar(f, fprime=df, x0=0.02, method="newton", xtol=1e-14)
s = root_scalar(f, x0=0.01, x1=0.03, method="secant", xtol=1e-14)
print(f"Monthly rate Newton {n.root:.6%} ({n.iterations} its), secant {s.root:.6%} ({s.iterations} its)")
print(f"Nominal annual rate {12*n.root:.3%}; effective annual rate {(1+n.root)**12-1:.3%}")
print(f"Total repaid {payment*months:,} on {principal:,} borrowed -> total interest {payment*months-principal:,}")
