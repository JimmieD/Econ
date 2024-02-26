import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np  # Import numpy for handling NaN

# Define the tickers for the assets you're interested in
tickers = ["SCHD", "DIVB", "VTI"]

# Define the period for which you want to calculate returns
start_date = "2019-02-23"
end_date = "2024-02-23"

# Initialize a DataFrame to store results
results = pd.DataFrame()

for ticker in tickers:
    # Fetch the historical data from Yahoo Finance
    data = yf.download(ticker, start=start_date, end=end_date)

    # Ensure 'Dividends' column exists, create it if not
    if 'Dividends' not in data.columns:
        data['Dividends'] = 0.0

    # Calculate daily returns including dividends
    data['Total Return'] = (data['Adj Close'].pct_change() + data['Dividends'] / data['Adj Close']).fillna(0)

    # Calculate cumulative total returns
    data['Cumulative Total Returns'] = (1 + data['Total Return']).cumprod() - 1

    # Calculate daily volatility and annualize it
    volatility = data['Total Return'].std() * np.sqrt(252)

    # Correct max drawdown calculation
    cumulative_max = data['Cumulative Total Returns'].cummax()
    drawdown = data['Cumulative Total Returns'] - cumulative_max
    max_drawdown = drawdown.min()

    # Store results
    results.loc[ticker, 'Cumulative Total Return'] = data['Cumulative Total Returns'].iloc[-1]
    results.loc[ticker, 'Annualized Volatility'] = volatility
    results.loc[ticker, 'Max Drawdown'] = max_drawdown

    # Plot cumulative total returns
    plt.plot(data.index, data['Cumulative Total Returns'], label=ticker)

# Plot formatting
plt.title('Cumulative Total Returns')
plt.xlabel('Date')
plt.ylabel('Cumulative Total Returns')
plt.legend()
plt.show()

# Print out results
print("Results from", start_date, "to", end_date)
results['Cumulative Total Return'] = results['Cumulative Total Return'] * 100  # Convert to percentage
results['Max Drawdown'] = results['Max Drawdown'] * 100  # Convert to percentage
print(results)