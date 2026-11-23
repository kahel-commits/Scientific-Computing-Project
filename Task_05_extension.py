import numpy as np
points = np.array([[0.,0.],[1.,0.],[1.,1.],[0.,1.]])
def tf(angle_deg, sx, sy):
    a = np.deg2rad(angle_deg)
    R = np.array([[np.cos(a),-np.sin(a)],[np.sin(a),np.cos(a)]])
    S = np.diag([sx, sy])
    return R @ S
print("--- PART C: change angle to 90 deg and scale to (3, 1) ---")
T = tf(90, 3, 1)
print("Matrix:\n", np.round(T,4)); print("Transformed:\n", np.round(points @ T.T,4))
print("Determinant:", round(np.linalg.det(T),4), "(area scale factor)")
print("Reflection test, scale (1,-1), 0 deg: det =", np.linalg.det(tf(0,1,-1)))
print("--- PART E: robot/drone path - rotate 30 deg then translate by (5, 2) using homogeneous coordinates ---")
path = np.array([[0,0],[2,0],[2,1],[4,1],[4,3]], dtype=float)
a = np.deg2rad(30)
H = np.array([[np.cos(a), -np.sin(a), 5],[np.sin(a), np.cos(a), 2],[0,0,1]])
ph = np.hstack([path, np.ones((len(path),1))])
new = (H @ ph.T).T[:, :2]
print("Homogeneous matrix:\n", np.round(H,4)); print("New path:\n", np.round(new,3))
d_old = np.linalg.norm(np.diff(path,axis=0),axis=1).sum(); d_new = np.linalg.norm(np.diff(new,axis=0),axis=1).sum()
print(f"Path length before {d_old:.4f}, after {d_new:.4f} (rigid motion preserves length)")
