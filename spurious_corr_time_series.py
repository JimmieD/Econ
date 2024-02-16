import numpy as np
import matplotlib.pyplot as plt

# Seed the random number generator for different results on each run
np.random.seed(None)

# Generate a time series for the x-axis (e.g., days, years)
time = np.arange(0, 365, 1)  # Simulating daily data for a year

# Generate a trending time series (linearly increasing with some noise)
trend_series = time * 0.1 + np.random.normal(0, 1, len(time))

# Generate a seasonal time series (simulating annual seasonality with noise)
seasonal_series = np.sin(time * 2 * np.pi / 365) * 10 + np.random.normal(0, 1, len(time))

# Calculate the correlation coefficient between the two datasets
correlation_time_series = np.corrcoef(trend_series, seasonal_series)[0, 1]

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(time, trend_series, label='Trending Time Series')
plt.plot(time, seasonal_series, label='Seasonal Time Series')
plt.title(f'Spurious Correlation in Time Series Data (Correlation: {correlation_time_series:.2f})')
plt.xlabel('Day of the Year')
plt.ylabel('Value')
plt.legend()
plt.show()
