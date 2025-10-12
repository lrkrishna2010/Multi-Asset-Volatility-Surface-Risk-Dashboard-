import numpy as np
from scipy.stats import norm

def value_at_risk(pnl, alpha=0.05):
    return -np.percentile(pnl, alpha*100)

def conditional_var(pnl, alpha=0.05):
    var = value_at_risk(pnl, alpha)
    return -pnl[pnl <= -var].mean()

def greeks(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    delta = norm.cdf(d1)
    gamma = norm.pdf(d1)/(S*sigma*np.sqrt(T))
    vega = S*norm.pdf(d1)*np.sqrt(T)
    theta = -(S*norm.pdf(d1)*sigma)/(2*np.sqrt(T)) - r*K*np.exp(-r*T)*norm.cdf(d2)
    return delta, gamma, vega, theta
