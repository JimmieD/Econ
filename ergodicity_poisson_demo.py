import numpy as np
import matplotlib.pyplot as plt

# Set seed for reproducibility
np.random.seed(seed=None)

# Parameters
n_observations = 100  # Number of observations in one experiment for time probability
n_experiments = 100000 # Number of experiments for ensemble probabilities
lambda_ = 5  # λ (lambda) - Mean rate of occurrence for Poisson distribution

# Simulate observations for ensemble probability using Poisson distribution
ensemble_results = np.random.poisson(lambda_, (n_experiments, n_observations))
# Calculate the observed mean for each experiment (ensemble)
observed_means_ensemble = np.mean(ensemble_results, axis=1)

# Simulate observations for time probability using Poisson distribution
time_results = np.random.poisson(lambda_, n_observations)
# Calculate cumulative deviation from the mean for time probability
deviation_from_mean = time_results - lambda_
cumulative_deviation = np.cumsum(deviation_from_mean)

# Visualization with an additional subplot for actual observations
plt.figure(figsize=(14, 8))

# Visualizing Ensemble Probability
plt.subplot(2, 2, 1)
min_bin = np.min(ensemble_results)
max_bin = np.percentile(ensemble_results, 100)  # Adjust this percentile as needed to capture outliers
bins = np.linspace(min_bin, max_bin, 100)  # Adjust the number of bins as desired

plt.hist(observed_means_ensemble, bins=bins, color='skyblue', edgecolor='black')
plt.title('Ensemble Probability')
plt.xlabel('Observed Mean Outcome')
plt.ylabel('Frequency')

# Visualizing Time Probability with Cumulative Deviation from the Mean
plt.subplot(2, 2, 2)
plt.plot(range(1, n_observations + 1), cumulative_deviation, color='blue', linestyle='-', label='Cumulative Deviation from Mean')
plt.axhline(y=0, color='red', linestyle='--', label='Expected Mean Level')
plt.title('Time Probability: Cumulative Deviation')
plt.xlabel('Observation Number')
plt.ylabel('Cumulative Deviation')
plt.legend()

# Additional subplot for actual observations
plt.subplot(2, 1, 2)
plt.plot(range(1, n_observations + 1), time_results, color='green', marker='o', linestyle='none', markersize=4, label='Actual Observations')
plt.axhline(y=lambda_, color='red', linestyle='--', label='Expected Mean')
plt.title('Time Probability: Actual Observations')
plt.xlabel('Observation Number')
plt.ylabel('Number of Events')
plt.legend()

plt.tight_layout()
plt.show()
