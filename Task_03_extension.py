import numpy as np, timeit
print("--- PART C: change N (array size) ---")
for N in [100_000, 1_000_000, 5_000_000]:
    rng = np.random.default_rng(42)
    x = rng.uniform(5, 250, N)
    def loop():
        out=[]
        for v in x:
            s=v/1000.0; out.append(s**2)
        return out
    def vec():
        return (x/1000.0)**2
    lt = timeit.timeit(loop, number=1); vt = timeit.timeit(vec, number=3)/3
    print(f"N={N:>9,}: loop {lt:.4f} s, vectorized {vt:.5f} s, speed-up {lt/vt:.0f}x")
print("--- PART E: RMS of accelerometer vibration signal (vectorized) ---")
rng = np.random.default_rng(1)
t = np.linspace(0, 10, 1_000_000)
signal = 0.5*np.sin(2*np.pi*50*t) + rng.normal(0, 0.1, t.size)
rms = np.sqrt(np.mean(signal**2))
def rms_loop():
    s=0.0
    for v in signal: s += v*v
    return (s/len(signal))**0.5
lt = timeit.timeit(rms_loop, number=1); vt = timeit.timeit(lambda: np.sqrt(np.mean(signal**2)), number=3)/3
print(f"RMS = {rms:.4f} g (theory sqrt(0.5^2/2+0.1^2)= {np.sqrt(0.125+0.01):.4f})")
print(f"Loop {lt:.3f}s vs vectorized {vt:.5f}s -> {lt/vt:.0f}x faster")
