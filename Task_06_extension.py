import numpy as np
print("--- PART C: new totals 24 CPU and 80 GB; then 21 CPU, 70 GB ---")
A = np.array([[4.,2.],[8.,12.]])
for b in ([24.,80.],[21.,70.]):
    x = np.linalg.solve(A, np.array(b)); print(f"b={b}: A servers {x[0]:.3f}, B servers {x[1]:.3f}")
print("det(A) =", np.linalg.det(A), " cond(A) =", round(np.linalg.cond(A),3))
print("--- PART E: two-loop electrical circuit (mesh currents) ---")
R1,R2,R3 = 4.0, 6.0, 3.0; V1,V2 = 12.0, 6.0
A = np.array([[R1+R2, -R2],[-R2, R2+R3]]); b = np.array([V1, -V2])
I = np.linalg.solve(A, b)
print("Matrix:\n", A, "\nRHS:", b)
print(f"Mesh currents: I1 = {I[0]:.4f} A, I2 = {I[1]:.4f} A")
print(f"Current through shared R2 (I1-I2): {I[0]-I[1]:.4f} A")
print("Residual norm:", np.linalg.norm(b-A@I))
print(f"Power dissipated: R1 {R1*I[0]**2:.3f} W, R2 {R2*(I[0]-I[1])**2:.3f} W, R3 {R3*I[1]**2:.3f} W")
print(f"Power supplied: {V1*I[0] + V2*(-I[1]):.3f} W  (V2 oriented opposite)")
