import numpy as np
import matplotlib.pyplot as plt
print("--- PART C: step size h and cooling constant k ---")
def euler(h,k=0.12,T0=90,Ta=25,end=30):
    t=np.arange(0,end+h/2,h); T=np.zeros_like(t); T[0]=T0
    for i in range(len(t)-1): T[i+1]=T[i]+h*(-k*(T[i]-Ta))
    return t,T
for h in (5,2,1,0.5,0.1):
    t,T=euler(h); ex=25+65*np.exp(-0.12*t[-1]); print(f"h={h:4}: Euler {T[-1]:.4f}, exact {ex:.4f}, error {abs(T[-1]-ex):.4f}")
t,T=euler(10); print("h=10 (k*h=1.2): values", np.round(T,2), "-> overshoots ambient (oscillation)")
t,T=euler(1,k=0.3); print(f"k=0.3, h=1: after 30 min {T[-1]:.3f} C (cools faster)")
fig=plt.figure()
for h in (5,1,0.1):
    t,T=euler(h); plt.plot(t,T,label=f"Euler h={h}")
tt=np.linspace(0,30,300); plt.plot(tt,25+65*np.exp(-0.12*tt),"k--",label="Exact"); plt.xlabel("Time (min)");plt.ylabel("Temperature (C)"); plt.title("Effect of step size on Euler cooling"); plt.legend(); plt.grid(True); plt.show()
print("--- PART E: logistic population growth dP/dt = rP(1-P/K), Euler vs exact ---")
r,K,P0=0.4,1000.0,50.0
for h in (1.0,0.1):
    t=np.arange(0,30+h/2,h); P=np.zeros_like(t); P[0]=P0
    for i in range(len(t)-1): P[i+1]=P[i]+h*r*P[i]*(1-P[i]/K)
    ex=K/(1+(K-P0)/P0*np.exp(-r*t)); print(f"h={h}: P(10)={P[int(10/h)]:.1f} (exact {ex[int(10/h)]:.1f}), P(30)={P[-1]:.1f} (exact {ex[-1]:.1f}), max error {np.max(np.abs(P-ex)):.2f}")
