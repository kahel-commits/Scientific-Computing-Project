import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
print("--- PART C: change R, and add discharge ---")
def rc(R,C=0.001,Vs=5.0,V0=0.0,T=10):
    s=solve_ivp(lambda t,V:[(Vs-V[0])/(R*C)],(0,T),[V0],t_eval=np.linspace(0,T,400),rtol=1e-9,atol=1e-11); return s
for R in (500,1000,2000):
    s=rc(R); tau=R*0.001; i=np.argmin(abs(s.t-tau))
    print(f"R={R}: tau={tau:.1f} s, V(tau)={s.y[0][i]:.3f} V (63.2% of 5 = 3.160), V(10 s)={s.y[0][-1]:.4f} V")
s=rc(1000,Vs=0.0,V0=5.0); print(f"Discharge from 5 V: V(1 s)={s.y[0][np.argmin(abs(s.t-1))]:.3f} V, V(5 s)={s.y[0][np.argmin(abs(s.t-5))]:.4f} V")
plt.figure()
for R in (500,1000,2000):
    s=rc(R); plt.plot(s.t,s.y[0],label=f"R={R} ohm")
plt.xlabel("Time (s)"); plt.ylabel("Capacitor voltage (V)"); plt.title("RC charging for different resistances"); plt.legend(); plt.grid(True); plt.show()
print("--- PART E: SIR epidemic model, N=1,000,000 ---")
N=1_000_000; beta=0.30; gamma=0.10
def sir(t,y):
    S,I,R=y; return [-beta*S*I/N, beta*S*I/N-gamma*I, gamma*I]
for beta in (0.30,0.18):
    s=solve_ivp(sir,(0,300),[N-10,10,0],t_eval=np.linspace(0,300,601),rtol=1e-8,atol=1e-8)
    S,I,R=s.y; pk=I.argmax()
    print(f"beta={beta}: R0={beta/gamma:.1f}, peak infected {I[pk]:,.0f} on day {s.t[pk]:.0f}, total ever infected {R[-1]:,.0f} ({R[-1]/N:.1%})")
    if beta==0.30: base=(s.t,S.copy(),I.copy(),R.copy())
plt.figure(); plt.plot(base[0],base[1],label="Susceptible"); plt.plot(base[0],base[2],label="Infected"); plt.plot(base[0],base[3],label="Recovered")
plt.xlabel("Day"); plt.ylabel("People"); plt.title("SIR epidemic (beta=0.30, gamma=0.10)"); plt.legend(); plt.grid(True); plt.show()
