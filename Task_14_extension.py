import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
users = np.array([50,100,150,200,250,300,350.]); resp = np.array([82,95,115,145,185,238,305.])
print("--- PART C: compare linear, quadratic and cubic models ---")
for deg in (1,2,3):
    p = np.polyfit(users,resp,deg); pred = np.polyval(p,users); rmse = np.sqrt(np.mean((resp-pred)**2))
    print(f"degree {deg}: RMSE {rmse:.2f} ms, prediction at 400 users {np.polyval(p,400):.1f} ms")
r2 = lambda y,p: 1-((y-p)**2).sum()/((y-y.mean())**2).sum()
p2 = np.polyfit(users,resp,2); print("R^2 quadratic:", round(r2(resp,np.polyval(p2,users)),5))
r2_ = resp.copy(); r2_[-1] = 400
p = np.polyfit(users,r2_,2); print("If last reading were 400 ms instead of 305: quad coeff", round(p[0],6), "pred@400", round(np.polyval(p,400),1))
print("--- PART E: drug concentration decay, C(t)=C0*exp(-k t) ---")
t = np.array([0.5,1,2,3,4,6,8,12.]); c = np.array([8.3,7.6,6.4,5.4,4.5,3.2,2.2,1.1])
model = lambda t,C0,k: C0*np.exp(-k*t)
(P,cov) = curve_fit(model,t,c,p0=[10,0.2]); C0,k = P; err = np.sqrt(np.diag(cov))
pred = model(t,C0,k); rmse = np.sqrt(np.mean((c-pred)**2))
print(f"C0 = {C0:.3f} +/- {err[0]:.3f} mg/L, k = {k:.4f} +/- {err[1]:.4f} per hour, RMSE {rmse:.3f}")
print(f"Half-life = ln2/k = {np.log(2)/k:.2f} hours; predicted at 10 h: {model(10,C0,k):.2f} mg/L")
tt=np.linspace(0,12,200); plt.scatter(t,c,label="Measured"); plt.plot(tt,model(tt,C0,k),label="Fitted exponential")
plt.xlabel("Time (hours)"); plt.ylabel("Concentration (mg/L)"); plt.title("Drug concentration decay fit"); plt.legend(); plt.grid(True); plt.show()
