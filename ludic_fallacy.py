import numpy as np
import matplotlib.pyplot as plt

np.random.seed(seed=None)  # For reproducibility

# Parameters
n = 1000  # Number of data points
expected_return = 0.07  # Expected return (for the simplified model)
volatility = 0.1  # Volatility (for the simplified model)

# Simplified Model: Normal distribution of returns
simplified_returns = np.random.normal(loc=expected_return, scale=volatility, size=n)

# 'Real-World' Scenario: Including some unpredictable 'black swan' events
real_world_returns = np.copy(simplified_returns)
black_swan_events = np.random.choice(range(n), size=10, replace=False)  # Randomly pick events
real_world_returns[black_swan_events] *= np.random.pareto(2, size=len(black_swan_events))  # Amplify/Reduce returns

# Plotting
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.hist(simplified_returns, bins=100, color='skyblue', alpha=0.7)
plt.title('Simplified Model: Normal Distribution of Returns')
plt.xlabel('Returns')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
plt.hist(real_world_returns, bins=100, color='salmon', alpha=0.7)
plt.title('Real-World Scenario: Including "Black Swan" Events')
plt.xlabel('Returns')

plt.tight_layout()
plt.show()

