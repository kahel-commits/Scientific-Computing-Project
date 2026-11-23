import numpy as np
def centrality(A):
    w,v = np.linalg.eig(A); i = np.argmax(w.real); vec = np.abs(v[:,i].real); return w[i].real, vec/vec.sum()
A = np.array([[0,1,1,0],[1,0,1,1],[1,1,0,1],[0,1,1,0.]])
print("--- PART C: add a link A-D (A and D become connected) ---")
A2 = A.copy(); A2[0,3]=A2[3,0]=1
for name,M in (("Original",A),("With A-D link",A2)):
    lam, c = centrality(M); print(f"{name}: dominant eigenvalue {lam:.4f}, importance A,B,C,D = {np.round(c,4)}")
A3 = A.copy(); A3[1,2]=A3[2,1]=0
lam,c = centrality(A3); print(f"Remove B-C link: dominant eigenvalue {lam:.4f}, importance = {np.round(c,4)}")
print("--- PART E: PageRank on a 4-page website (damping 0.85) ---")
pages = ["Home","Products","Blog","Contact"]
# links[i][j]=1 means page j links to page i
L = np.array([[0,1,1,1],[1,0,0,0],[1,0,0,1],[0,1,1,0.]])
M = L / L.sum(axis=0)
d=0.85; n=4
G = d*M + (1-d)/n*np.ones((n,n))
w,v = np.linalg.eig(G); i = np.argmax(w.real); pr = np.abs(v[:,i].real); pr/=pr.sum()
print("Dominant eigenvalue of Google matrix:", round(w[i].real,6))
for p,s in zip(pages,pr): print(f"{p:9s}: {s:.4f}")
r = np.ones(n)/n
for k in range(100): r = G@r
print("Power-iteration result:", np.round(r,4))
