import numpy as np

def simulate_gbm(S0, mu, sigma, T=1, steps=252, n_sim=1000):
    dt = T/steps
    paths = np.zeros((steps+1, n_sim))
    paths[0] = S0
    for t in range(1, steps+1):
        z = np.random.standard_normal(n_sim)
        paths[t] = paths[t-1] * np.exp((mu - 0.5*sigma**2)*dt + sigma*np.sqrt(dt)*z)
    return paths
