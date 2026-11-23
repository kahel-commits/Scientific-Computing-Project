import numpy as np
from scipy.optimize import minimize
print("--- PART C: change unit cost of A from 12 to 10 ---")
def solve(cA,cB,capA=100,capB=170,req=1000):
    s=minimize(lambda z:cA*z[0]+cB*z[1],[5,3],method="SLSQP",bounds=[(0,None)]*2,constraints={"type":"ineq","fun":lambda z:capA*z[0]+capB*z[1]-req})
    return s
for cA in (12,10):
    s=solve(cA,18); print(f"cost A={cA}: A={s.x[0]:.3f}, B={s.x[1]:.3f}, cost={s.fun:.2f}  (cost per capacity: A {cA/100:.4f}, B {18/170:.4f})")
s=solve(12,18,req=2000); print(f"Required capacity 2000: A={s.x[0]:.3f}, B={s.x[1]:.3f}, cost={s.fun:.2f}")
print("--- PART E: cloud plan with CPU and memory constraints, three server types ---")
# types: S (cost 10, 4 CPU, 16 GB), M (cost 18, 8 CPU, 40 GB), L (cost 34, 16 CPU, 96 GB); need >= 120 CPU and >= 600 GB
cost=np.array([10,18,34.]); cpu=np.array([4,8,16.]); mem=np.array([16,40,96.])
cons=[{"type":"ineq","fun":lambda z:cpu@z-120},{"type":"ineq","fun":lambda z:mem@z-600}]
s=minimize(lambda z:cost@z,[10,10,5],method="SLSQP",bounds=[(0,None)]*3,constraints=cons)
print("Continuous: ",np.round(s.x,3),"cost",round(s.fun,2),"CPU",round(cpu@s.x,1),"mem",round(mem@s.x,1),"success",s.success)
best=None
for a in range(0,41):
  for b in range(0,41):
    for c in range(0,21):
      z=np.array([a,b,c])
      if cpu@z>=120 and mem@z>=600:
        co=cost@z
        if best is None or co<best[0]: best=(co,a,b,c,cpu@z,mem@z)
print("Best whole-server combination (cost, S, M, L, CPU, GB):",best)
