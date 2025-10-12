import numpy as np
from scipy.stats import norm
from scipy.optimize import brentq

def bs_call_price(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    return S*norm.cdf(d1) - K*np.exp(-r*T)*norm.cdf(d2)

def implied_vol_call(price, S, K, T, r):
    """Compute implied volatility using Brent's method"""
    f = lambda sigma: bs_call_price(S, K, T, r, sigma) - price
    try:
        return brentq(f, 1e-6, 5)
    except:
        return np.nan

def compute_iv_surface(df, r=0.01):
    df['implied_vol'] = [
        implied_vol_call(row.price, row.underlying, row.strike,
                        (row.expiry - row.date).days/365, r)
        for _, row in df.iterrows()
    ]
    return df
