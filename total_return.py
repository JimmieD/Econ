import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np  # Import numpy for handling NaN
from datetime import datetime
import warnings

# Suppress future warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Define the tickers for the assets you're interested in
tickers = ["VTI", "QQQ", "AGG"]

# Define the period for which you want to calculate returns
start_date = "2017-01-01"
end_date = "2024-02-26"

# Initialize a DataFrame to store results
results = pd.DataFrame()
current_year = datetime.now().year
start_year = pd.to_datetime(start_date).year
end_year = pd.to_datetime(end_date).year
years_in_period = end_year - start_year + 1

for ticker in tickers:
    # Fetch the historical data from Yahoo Finance
    data = yf.download(ticker, start=start_date, end=end_date)
    ticker_info = yf.Ticker(ticker)
    dividends = ticker_info.dividends

    # Ensure 'Dividends' column exists, create it if not
    #if 'Dividends' not in data.columns:
    #    data['Dividends'] = 0.0

    # Calculate daily returns including dividends
    data['Total Return'] = data['Adj Close'].pct_change().fillna(0) #data['Total Return'] = (data['Adj Close'].pct_change() + data['Dividends'] / data['Adj Close']).fillna(0)

    # Calculate cumulative total returns
    data['Cumulative Total Returns'] = (1 + data['Total Return']).cumprod() - 1

    # Calculate daily volatility and annualize it
    volatility = data['Total Return'].std() * np.sqrt(252)

    # Correct max drawdown calculation
    cumulative_max = data['Cumulative Total Returns'].cummax()
    drawdown = data['Cumulative Total Returns'] - cumulative_max
    max_drawdown = drawdown.min()

    # Calculate the number of years for the period
    num_years = (pd.to_datetime(end_date) - pd.to_datetime(start_date)).days / 365.25

    # Calculate annualized return
    annualized_return = ((1 + data['Cumulative Total Returns'].iloc[-1]) ** (1/num_years)) - 1
    
    # Filter dividends for the period
    dividends_period = dividends[(dividends.index >= start_date) & (dividends.index <= end_date)]
    
    # Calculate annual dividends
    annual_dividends = dividends_period.resample('YE').sum()

    if not annual_dividends.empty:
        if annual_dividends.index[-1].year == current_year:
            # Determine the number of payments made so far this year
            payments_made = dividends[dividends.index.year == current_year].count()
            
            # Project annual dividends based on payments made so far
            if payments_made > 0:
                annual_dividends.iloc[-1] = (annual_dividends.iloc[-1] / payments_made) * 4  # Assuming 4 payments per year

        # Calculate the overall dividend growth rate from start to end
        if len(annual_dividends) > 1:
            overall_growth = (annual_dividends.iloc[-1] / annual_dividends.iloc[0]) - 1 if annual_dividends.iloc[0] != 0 else np.nan
            # Calculate annualized growth rate
            annualized_growth_rate = (overall_growth + 1) ** (1 / (years_in_period - 1)) - 1 if overall_growth >= 0 else np.nan
        else:
            overall_growth = np.nan
            annualized_growth_rate = np.nan
    else:
        overall_growth = np.nan
        annualized_growth_rate = np.nan


    # Store results
    results.loc[ticker, 'Cumulative Total Return'] = data['Cumulative Total Returns'].iloc[-1]
    results.loc[ticker, 'Annualized Volatility'] = volatility
    results.loc[ticker, 'Max Drawdown'] = max_drawdown
    results.loc[ticker, 'Annualized Return'] = annualized_return
    results.loc[ticker, 'Overall Div Gr Rate'] = overall_growth
    results.loc[ticker, 'Ann. Div Gr Rate'] = annualized_growth_rate

    # Plot cumulative total returns
    plt.plot(data.index, data['Cumulative Total Returns'], label=ticker)
# Print out results
print("Results from", start_date, "to", end_date)
results['Cumulative Total Return'] = results['Cumulative Total Return'] * 100  # Convert to percentage
results['Max Drawdown'] = results['Max Drawdown'] * 100  # Convert to percentage
results['Annualized Return'] = results['Annualized Return'] * 100  # Convert to percentage
print(results)

# Plot formatting
plt.title('Cumulative Total Returns')
plt.xlabel('Date')
plt.ylabel('Cumulative Total Returns')
plt.legend()
plt.show()

