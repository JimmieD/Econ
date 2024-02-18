import numpy as np
import matplotlib.pyplot as plt

# Set seed for reproducibility
np.random.seed(42)

# Parameters
n_flips = 100  # Number of coin flips in one experiment
n_experiments = 10000  # Number of experiments to simulate ensemble probabilities

# Simulate coin flips for ensemble probability
ensemble_results = np.random.binomial(n_flips, 0.5, n_experiments)

# Simulate coin flips for time probability
time_results = np.random.binomial(1, 0.5, n_flips)

# Visualization with an added subplot for actual observations
plt.figure(figsize=(14, 9))  # Adjusted size for better layout

# Visualizing Ensemble Probability
plt.subplot(2, 2, 1)  # Adjusted for a 2x2 layout
plt.hist(ensemble_results, bins=np.arange(n_flips+2)-0.5, color='skyblue', edgecolor='black')
plt.title('Ensemble Probability')
plt.xlabel('Number of Heads in 100 Flips')
plt.ylabel('Frequency')
plt.xticks(np.arange(0, n_flips+1, step=100))  # Adjust ticks for clarity

# Visualizing Time Probability (Cumulative Deviation)
plt.subplot(2, 2, 2)  # Adjusted for a 2x2 layout
cumulative_heads = np.cumsum(time_results)
expected_heads = np.arange(1, n_flips + 1) * 0.5
cumulative_deviation = cumulative_heads - expected_heads
plt.plot(range(1, n_flips + 1), cumulative_deviation, color='orange', marker='o', linestyle='-', markersize=4)
plt.axhline(y=0, color='grey', linestyle='--')
plt.title('Time Probability')
plt.xlabel('Flip Number')
plt.ylabel('Cumulative Deviation from Expected Heads')

# Additional Subplot for Actual Observations
plt.subplot(2, 1, 2)  # New subplot for actual observations over time
plt.plot(range(1, n_flips + 1), time_results, 'go', label='Actual Heads (0 or 1)')
plt.title('Actual Observations Over Time')
plt.xlabel('Flip Number')
plt.ylabel('Heads Outcome')
plt.yticks([0, 1], ['Tails', 'Heads'])  # Since outcomes are 0 or 1

plt.tight_layout()
plt.show()
