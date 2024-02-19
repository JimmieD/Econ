import numpy as np
import matplotlib.pyplot as plt

# Set the random seed for reproducibility
np.random.seed(42)

# GARCH(1,1) parameters
alpha_0 = 0.2  # Constant term
alpha_1 = 0.5  # ARCH parameter
beta_1 = 0.3   # GARCH parameter

# Number of observations
n = 1000

# Pre-allocate arrays
eps = np.random.normal(0, 1, n)  # Random shocks, epsilon
sigma2 = np.zeros(n)             # Conditional variance, sigma^2
y = np.zeros(n)                  # Time series data

# Initial variance
sigma2[0] = alpha_0 / (1 - alpha_1 - beta_1)

# Simulate the GARCH(1,1) process
for t in range(1, n):
    sigma2[t] = alpha_0 + alpha_1 * eps[t-1]**2 + beta_1 * sigma2[t-1]
    y[t] = np.sqrt(sigma2[t]) * eps[t]

# Plot the simulated GARCH(1,1) process
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(y, label='Simulated GARCH(1,1) Process')
plt.title('Simulated GARCH(1,1) Process')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(sigma2, label='Conditional Variance (Volatility)')
plt.title('Conditional Variance (Volatility)')
plt.legend()

plt.tight_layout()
plt.show()
