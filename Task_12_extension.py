import numpy as np
from scipy.optimize import root
print("--- PART C: radius 4 -> 1 (circle x^2+y^2=1) with several guesses ---")
eq = lambda z: [z[0]**2+z[1]**2-1, z[1]-(z[0]**2-1)]
found=set()
for g in ([1,1],[-1,1],[0.1,-0.9],[0.5,0.5],[2,2]):
    s = root(eq, g)
    print(f"guess {g}: {np.round(s.x,5)} converged={s.success}")
print("Roots of x^2-5x+6 via np.roots:", np.roots([1,-5,6]))
print("--- PART E: projectile (v=25 m/s, 40 deg) landing on a hillside y = 0.2x ---")
v=25.0; th=np.deg2rad(40); g=9.81
def landing(z):
    x,y = z
    return [y - (x*np.tan(th) - g*x**2/(2*v**2*np.cos(th)**2)), y - 0.2*x]
for guess in ([5,1],[40,8]):
    s = root(landing, guess); print(f"guess {guess}: landing (x,y) = {np.round(s.x,4)} m, residual {np.abs(landing(s.x)).max():.1e}, converged {s.success}")
x_land = 2*v**2*np.cos(th)**2*(np.tan(th)-0.2)/g
print(f"Analytic landing x = {x_land:.4f} m; flat-ground range would be {v**2*np.sin(2*th)/g:.4f} m")
