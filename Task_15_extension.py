import numpy as np
import matplotlib.pyplot as plt
print("--- PART C: step size study on f(x)=sin(x), true f'(1)=cos(1) ---")
x=1.0; true=np.cos(1.0)
print(f"{'h':>8} {'forward err':>14} {'central err':>14}")
hs = [1,0.1,0.01,0.001,1e-6,1e-8,1e-10,1e-12,1e-14]
fe=[];ce=[]
for h in hs:
    f=(np.sin(x+h)-np.sin(x))/h; c=(np.sin(x+h)-np.sin(x-h))/(2*h); fe.append(abs(f-true)); ce.append(abs(c-true))
    print(f"{h:8.0e} {fe[-1]:14.3e} {ce[-1]:14.3e}")
plt.loglog(hs,fe,"o-",label="Forward"); plt.loglog(hs,ce,"s-",label="Central"); plt.xlabel("Step size h"); plt.ylabel("Absolute error"); plt.title("Differentiation error vs step size"); plt.legend(); plt.grid(True); plt.show()
print("--- PART E: acceleration of a vehicle from speed data using np.gradient ---")
t = np.arange(0,11,1.0); v = np.array([0,3.1,6.0,8.6,10.9,12.8,14.4,15.5,16.3,16.8,17.0])
a = np.gradient(v,t)
for ti,vi,ai in zip(t,v,a): print(f"t={ti:4.0f}s speed={vi:5.1f} m/s acceleration={ai:5.2f} m/s^2")
print(f"Peak acceleration {a.max():.2f} m/s^2 at t={t[a.argmax()]:.0f} s; acceleration near zero at t=10 s -> speed levels off")
