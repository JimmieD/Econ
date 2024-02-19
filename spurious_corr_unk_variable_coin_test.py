import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt

# Set seed for reproducibility
np.random.seed(seed=None)

# Generate the 'unknown variable' representing underlying economic factors as a random walk
unknown_variable_economic = np.cumsum(np.random.normal(0, 0.5, 365))

# Simulate asset price 1: Random walk with a trend influenced by the economic factor
asset_price_1 = 100 + np.cumsum(np.random.normal(0.1, 1, 365) + 0.05 * unknown_variable_economic)

# Simulate asset price 2: Another random walk with a trend, also influenced by the economic factor but with a different variance
asset_price_2 = 100 + np.cumsum(np.random.normal(0.1, 1.5, 365) + 0.05 * unknown_variable_economic)

#Calculate correlation
correlation_assets = np.corrcoef(asset_price_1, asset_price_2)[0, 1]

# Regression to obtain residuals
X = sm.add_constant(asset_price_1)  # Adding a constant for the regression intercept
model = sm.OLS(asset_price_2, X).fit()
residuals = model.resid

# Augmented Dickey-Fuller test on the residuals
adf_result = adfuller(residuals)
print(f"ADF Statistic: {adf_result[0]}")
print(f"p-value: {adf_result[1]}")
for key, value in adf_result[4].items():
    print('Critial Values:')
    print(f"   {key}, {value}")

# Interpretation
if adf_result[1] < 0.05:
    print("The series is stationary. The asset prices are likely cointegrated.")
else:
    print("The series is not stationary. The asset prices are not cointegrated.")

# Plotting the asset prices and the economic factor
plt.figure(figsize=(12, 6))
plt.plot(asset_price_1, label='Asset Price 1')
plt.plot(asset_price_2, label='Asset Price 2')
#plt.plot(unknown_variable_economic, label='Economic Factor', linestyle='--')
plt.legend()
plt.title(f'Correlation Between Asset Prices (Correlation: {correlation_assets:.2f})')
plt.show()
