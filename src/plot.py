import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def plot_vol_surface(df):
    fig = plt.figure(figsize=(10,7))
    ax = fig.add_subplot(111, projection='3d')
    X = df['strike']
    Y = (df['expiry'] - df['expiry'].min()).dt.days
    Z = df['implied_vol']
    ax.scatter(X, Y, Z, c=Z, cmap='viridis')
    ax.set_xlabel("Strike")
    ax.set_ylabel("Days to Expiry")
    ax.set_zlabel("Implied Vol")
    plt.show()

def plot_mc_paths(paths):
    plt.figure(figsize=(10,6))
    plt.plot(paths)
    plt.title("Monte Carlo Simulated Asset Paths")
    plt.xlabel("Steps")
    plt.ylabel("Price")
    plt.show()
