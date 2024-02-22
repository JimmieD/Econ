import yfinance as yf
import numpy as np
import pandas as pd

# Define assets
assets = ['WDS']  # Example assets

# Risk-free rate (annual), adjust as necessary
R_f = 0.0553  # Example: 2% annual risk-free rate

def calculate_kelly_criterion_with_dividends(ticker):
    # Fetch historical price data and dividend data for the asset
    data = yf.Ticker(ticker)
    prices = data.history(start='2023-01-01', end='2024-01-01')['Close']
    dividends = data.dividends
    
    # Calculate daily returns from prices
    daily_returns = prices.pct_change().dropna()
    
    # Calculate dividend yield (annualized)
    annual_dividends = dividends.sum()
    average_price = prices.mean()
    dividend_yield = annual_dividends / average_price
    
    # Calculate the expected annual return (including dividends) and annual variance
    annual_return_with_dividends = daily_returns.mean() * 252 + dividend_yield
    annual_variance = daily_returns.var() * 252
    
    # Calculate Kelly Criterion for the asset
    kelly_fraction = (annual_return_with_dividends - R_f) / annual_variance
    return kelly_fraction

# Calculate and print Kelly Criterion for each asset, including dividends
kelly_fractions_with_dividends = {asset: calculate_kelly_criterion_with_dividends(asset) for asset in assets}
print("Kelly Fractions for each asset (including dividends):")
for asset, kelly_fraction in kelly_fractions_with_dividends.items():
    print(f"{asset}: {kelly_fraction}")
