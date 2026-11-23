import numpy as np, timeit
from scipy.linalg import lu_factor, lu_solve
print("--- PART C: change matrix diagonal (3 -> 2.2) and compare LU vs repeated solve on a larger matrix ---")
A = np.array([[4.,-1,0],[-1,4,-1],[0,-1,2.2]])
b = np.array([15.,10,10]); x = np.linalg.solve(A,b)
print("Solution with A[2,2]=2.2:", x, " cond:", round(np.linalg.cond(A),3))
n = 800; rng = np.random.default_rng(0)
M = rng.normal(size=(n,n)) + n*np.eye(n); rhs = rng.normal(size=(100, n))
t_solve = timeit.timeit(lambda: [np.linalg.solve(M, r) for r in rhs], number=1)
def with_lu():
    lu, piv = lu_factor(M)
    return [lu_solve((lu,piv), r) for r in rhs]
t_lu = timeit.timeit(with_lu, number=1)
print(f"800x800 system, 100 right-hand sides: repeated solve {t_solve:.3f}s, LU once + reuse {t_lu:.3f}s, speed-up {t_solve/t_lu:.1f}x")
print("--- PART E: implicit heat conduction in a rod (same matrix every time step) ---")
n=50; alpha=1.0; dx=1.0/(n+1); dt=0.001; r=alpha*dt/dx**2
L = np.diag(-2*np.ones(n)) + np.diag(np.ones(n-1),1) + np.diag(np.ones(n-1),-1)
Amat = np.eye(n) - r*L
lu, piv = lu_factor(Amat)
T = np.zeros(n); T[n//2-3:n//2+3] = 100.0
print(f"Initial: max {T.max():.1f} C, total heat {T.sum():.1f}")
for step in range(1, 201):
    T = lu_solve((lu,piv), T)
    if step in (1,50,200): print(f"step {step:3d} (t={step*dt:.3f}): max {T.max():.3f} C, centre {T[n//2]:.3f} C, total {T.sum():.1f}")
