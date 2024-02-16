import numpy as np
import matplotlib.pyplot as plt

# Generate the 'unknown variable' representing underlying economic factors as a random walk
unknown_variable_economic = np.cumsum(np.random.normal(0, 0.5, 365))

# Simulate asset price 1: Random walk with a trend influenced by the economic factor
asset_price_1 = 100 + np.cumsum(np.random.normal(0.1, 1, 365) + 0.05 * unknown_variable_economic)

# Simulate asset price 2: Another random walk with a trend, also influenced by the economic factor but with a different variance
asset_price_2 = 100 + np.cumsum(np.random.normal(0.1, 1.5, 365) + 0.05 * unknown_variable_economic)

# Calculate the correlation between the two asset prices
correlation_assets = np.corrcoef(asset_price_1, asset_price_2)[0, 1]

# Plot the simulated asset prices
plt.figure(figsize=(12, 8))
plt.plot(np.arange(365), asset_price_1, label='Asset Price 1') #(Random Walk with Trend))
plt.plot(np.arange(365), asset_price_2, label='Asset Price 2') #(Random Walk with Trend)
plt.title(f'Correlation Between Asset Prices (Correlation: {correlation_assets:.2f})')
plt.xlabel('Time')
plt.ylabel('Asset Price')
plt.legend()
plt.show()
