from src.data_loader import load_data
from src.volatility import compute_iv_surface
from src.monte_carlo import simulate_gbm
from src.risk_metrics import value_at_risk, conditional_var, greeks
from src.plot import plot_vol_surface, plot_mc_paths

def main():
    # Load data
    df = load_data()

    # Compute implied volatilities
    df = compute_iv_surface(df)
    print(df.head())

    # Plot volatility surface
    plot_vol_surface(df)

    # Monte Carlo simulation example
    paths = simulate_gbm(S0=100, mu=0.05, sigma=0.2)
    plot_mc_paths(paths)

    # Compute portfolio risk metrics
    pnl = paths[-1] - 100
    print("VaR (5%):", value_at_risk(pnl))
    print("CVaR (5%):", conditional_var(pnl))
    delta, gamma, vega, theta = greeks(100, 100, 1, 0.01, 0.2)
    print("Greeks:", delta, gamma, vega, theta)

if __name__ == "__main__":
    main()
