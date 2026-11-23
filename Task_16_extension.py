import numpy as np
from scipy.integrate import simpson
print("--- PART C: accuracy vs number of samples, integral of sin(x) from 0 to pi (true value 2) ---")
for n in (3,5,9,17,33):
    x=np.linspace(0,np.pi,n); y=np.sin(x)
    tr=np.trapezoid(y,x); si=simpson(y,x=x)
    print(f"{n:2d} points: trapezoid {tr:.6f} (err {abs(tr-2):.1e}), Simpson {si:.8f} (err {abs(si-2):.1e})")
th = np.array([0,2,4,6,8,10,12.]); p = np.array([0.8,1.0,1.4,1.8,1.6,1.2,0.9])
print("Original with every power reading raised by 20%:", round(np.trapezoid(1.2*p,th),3), "kWh trapezoid")
print("--- PART E: total water volume from river-gauge flow rate (hourly, m^3/s) over 12 h ---")
t = np.arange(0,13,1)*3600.0
q = np.array([12,12.5,14,18,26,38,45,41,33,26,20,16,14.])
vol_t = np.trapezoid(q,t); vol_s = simpson(q,x=t)
print(f"Volume trapezoid {vol_t:,.0f} m^3, Simpson {vol_s:,.0f} m^3, difference {abs(vol_t-vol_s):,.0f} m^3")
print(f"Mean flow {vol_s/t[-1]:.2f} m^3/s; peak flow {q.max()} m^3/s at hour {q.argmax()}")
print(f"Equivalent to {vol_s/2500:.0f} Olympic pools")
