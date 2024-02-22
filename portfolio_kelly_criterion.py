import numpy as np
import pandas as pd
import yfinance as yf
from scipy.optimize import minimize

# Define the assets and the historical data period
assets = ['WDS', 'AGG']  # Example assets # Example assets
start_date = '2004-01-01'
end_date = '2024-02-16'

# Download historical data from Yahoo Finance
data = yf.download(assets, start=start_date, end=end_date)['Adj Close']

# Calculate daily returns
daily_returns = data.pct_change().dropna()

# Calculate expected annual returns and the annual covariance matrix
expected_returns = daily_returns.mean() * 252
covariance_matrix = daily_returns.cov() * 252

# Risk-free rate (annual), adjust as necessary
risk_free_rate = 0.0553
lambda_reg = 0.1  # Regularization parameter

# Number of assets
n_assets = len(assets)

# Objective function to maximize (negative for minimization function) with regularization
def objective(weights):
    # Adjust expected returns by subtracting the risk-free rate
    adj_expected_returns = expected_returns - risk_free_rate
    # Expected portfolio return
    port_return = np.dot(weights, adj_expected_returns)
    # Portfolio variance
    port_variance = np.dot(weights.T, np.dot(covariance_matrix, weights))
    # Regularization term (sum of squares of weights)
    regularization = lambda_reg * np.sum(weights**2)
    # Negative of the Kelly Criterion (since we are minimizing) with regularization
    return -port_return + 0.5 * port_variance + regularization

# Constraints: sum of weights = 1
constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})

# Bounds for each weight: no short selling, weights between 0 and 1
bounds = tuple((0, 1) for asset in range(n_assets))

# Initial guess for the weights
initial_guess = np.array([1./n_assets] * n_assets)

# Optimize
result = minimize(objective, initial_guess, method='SLSQP', bounds=bounds, constraints=constraints)

if result.success:
    optimized_weights = result.x
    # Print asset names with their optimized weights
    print("Optimized Weights (with regularization):")
    for asset, weight in zip(assets, optimized_weights):
        print(f"{asset}: {weight:.4f}")
else:
    print("Optimization failed:", result.message)