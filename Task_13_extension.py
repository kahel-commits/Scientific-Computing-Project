import numpy as np
from scipy.interpolate import interp1d, CubicSpline
import matplotlib.pyplot as plt
hours = np.array([8,9,10,11,12,13,14.]); temp = np.array([18.0,20.0,22.5,24.0,25.0,25.5,25.0])
print("--- PART C: use only every second reading (8,10,12,14) and compare estimates at 11:00 and 13:00 ---")
h2, t2 = hours[::2], temp[::2]
for kind, f in (("linear", interp1d(h2,t2)), ("cubic", CubicSpline(h2,t2))):
    print(f"{kind}: 11:00 -> {float(f(11)):.2f} C (measured 24.0), 13:00 -> {float(f(13)):.2f} C (measured 25.5)")
print("Extrapolation test, cubic at 15:00:", round(float(CubicSpline(hours,temp)(15)),2), "C (physically doubtful)")
try: interp1d(hours,temp)(15)
except ValueError as e: print("interp1d at 15:00 ->", "ValueError (outside range)")
print("--- PART E: soil-moisture sensor with a missing reading (fill the gap) ---")
t = np.array([0,1,2,4,5,6,7.]); m = np.array([32.0,30.5,29.2,26.8,25.9,25.2,24.7])  # hour 3 missing
lin = interp1d(t,m); cub = CubicSpline(t,m)
print(f"Estimated moisture at hour 3: linear {float(lin(3)):.2f}%, cubic spline {float(cub(3)):.2f}%")
tt = np.linspace(0,7,100)
plt.scatter(t,m,label="Recorded"); plt.plot(tt,lin(tt),label="Linear"); plt.plot(tt,cub(tt),label="Cubic spline")
plt.scatter([3],[float(cub(3))],marker="x",s=80,color="red",label="Filled value (cubic)")
plt.xlabel("Hour"); plt.ylabel("Soil moisture (%)"); plt.title("Filling a missing soil-moisture reading"); plt.legend(); plt.grid(True); plt.show()
