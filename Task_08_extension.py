import numpy as np
import matplotlib.pyplot as plt
exec(open("code/Task_08_iterative_linear.py").read().split("x_j, err_j")[0].split("b = np.array")[0])
src = open("code/Task_08_iterative_linear.py").read()
exec("def jacobi" + src.split("def jacobi")[1].split("x_j, err_j")[0])
print("--- PART C: change tolerance and grid size ---")
def system(n, left, right):
    A = 2*np.eye(n) - np.eye(n,k=1) - np.eye(n,k=-1); b = np.zeros(n); b[0]=left; b[-1]=right; return A,b
A,b = system(5,100,20)
for tol in (1e-4,1e-8,1e-12):
    _,ej = jacobi(A,b,tol=tol); _,eg = gauss_seidel(A,b,tol=tol)
    print(f"n=5 tol={tol:.0e}: Jacobi {len(ej)} its, Gauss-Seidel {len(eg)} its")
for n in (5,10,20,40):
    A,b = system(n,100,20); _,ej = jacobi(A,b,max_iter=20000); _,eg = gauss_seidel(A,b,max_iter=20000)
    print(f"n={n:2d}, tol=1e-8: Jacobi {len(ej):5d} its, Gauss-Seidel {len(eg):5d} its")
print("--- PART E: 2-D heated plate (Laplace), top edge 100 C, other edges 0 C, 8x8 interior grid ---")
m = 8; n = m*m
I = np.eye(m); T1 = 2*np.eye(m)-np.eye(m,k=1)-np.eye(m,k=-1)
A = np.kron(I,T1) + np.kron(T1,I)
b = np.zeros(n); b[:m] = 100.0   # top row
x, errs = gauss_seidel(A, b, tol=1e-6, max_iter=5000)
Tgrid = x.reshape(m,m)
print("Gauss-Seidel iterations:", len(errs))
print("Direct solve max difference:", np.max(np.abs(x-np.linalg.solve(A,b))))
print("Plate temperature rows (top to bottom, centre column):", np.round(Tgrid[:,m//2],2))
plt.imshow(Tgrid, cmap="hot"); plt.colorbar(label="Temperature (C)"); plt.title("Steady-state plate temperature (top edge 100 C)"); plt.show()
