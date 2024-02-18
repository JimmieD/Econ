import numpy as np
import matplotlib.pyplot as plt

# Set seed for reproducibility
np.random.seed(42)

# Parameters for the normal distribution simulation
n_observations = 500  # Number of observations in one experiment
n_experiments = 10000  # Number of experiments for ensemble probabilities
mean = 0.5  # Mean of the normal distribution
std_dev = 0.1  # Standard deviation of the normal distribution

# Simulate observations for ensemble probability using normal distribution
ensemble_results = np.random.normal(mean, std_dev, (n_experiments, n_observations))

# Calculate the observed mean for each experiment (ensemble)
observed_means_ensemble = np.mean(ensemble_results, axis=1)

# Simulate observations for time probability using normal distribution
time_results = np.random.normal(mean, std_dev, n_observations)

# Calculate the observed mean for the time probability
observed_mean_time = np.mean(time_results)

# Visualization
plt.figure(figsize=(14, 6))

# Visualizing Ensemble Probability
plt.subplot(1, 2, 1)
plt.hist(observed_means_ensemble, bins=40, color='skyblue', edgecolor='black')
plt.title('Ensemble Probability')
plt.xlabel('Observed Mean Outcome')
plt.ylabel('Frequency')

# Visualizing Time Probability with Observed Mean
plt.subplot(1, 2, 2)
plt.axhline(y=mean, color='red', linestyle='--', label='Expected Mean')
plt.axhline(y=observed_mean_time, color='green', linestyle=':', label=f'Observed Mean: {observed_mean_time:.2f}')
plt.title('Time Probability')
plt.xlabel('Observation Number')
plt.ylabel('Outcome')
plt.legend()

plt.tight_layout()
plt.show()
