import numpy as np
import matplotlib.pyplot as plt

# Set seed for reproducibility
np.random.seed(42)

# Parameters
n_flips = 1000  # Number of coin flips in one experiment
n_experiments = 10000  # Number of experiments to simulate ensemble probabilities

# Simulate coin flips for ensemble probability
ensemble_results = np.random.binomial(n_flips, 0.5, n_experiments)

# Simulate coin flips for time probability
time_results = np.random.binomial(1, 0.5, n_flips)

# Visualization
plt.figure(figsize=(14, 6))

# Visualizing Ensemble Probability
plt.subplot(1, 2, 1)  # First subplot for ensemble probabilities
plt.hist(ensemble_results, bins=np.arange(n_flips+2)-0.5, color='skyblue', edgecolor='black')
plt.title('Ensemble Probability')
plt.xlabel('Number of Heads in 1000 Flips')
plt.ylabel('Frequency')
plt.xticks(np.arange(n_flips+1, step=50))

# Visualizing Time Probability
plt.subplot(1, 2, 2)  # Second subplot for time probabilities
cumulative_heads = np.cumsum(time_results)
expected_heads = np.arange(1, n_flips + 1) * 0.5
cumulative_deviation = cumulative_heads - expected_heads

plt.plot(range(1, n_flips + 1), cumulative_deviation, color='orange', marker='o', linestyle='-', markersize=4)
plt.axhline(y=0, color='grey', linestyle='--')
plt.title('Time Probability')
plt.xlabel('Flip Number')
plt.ylabel('Cumulative Deviation from Expected Heads')

plt.tight_layout()
plt.show()
