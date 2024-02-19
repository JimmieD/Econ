import numpy as np
import matplotlib.pyplot as plt

# Set seed for reproducibility
np.random.seed(seed=None)

# Generate time series data
n_time_points = 1000
time = np.arange(n_time_points)

# Parameters for the drift and increasing variance
drift_rate = 0.05  # This controls the rate of the drift over time
variance_increase = 0.1  # This controls how quickly the variance increases

# Generate data with increasing variance over time and drift
mean = 0  # Initial mean, which will be modified by drift over time
data_with_drift = np.random.randn(n_time_points) * np.sqrt(variance_increase * time) + (mean + drift_rate * time)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(time, data_with_drift, marker='o', linestyle='-', color='blue', label='Data with Increasing Variance and Drift')
plt.fill_between(time, (mean + drift_rate * time) + 2 * np.sqrt(variance_increase * time), (mean + drift_rate * time) - 2 * np.sqrt(variance_increase * time), color='lightblue', alpha=0.5, label='Approx. 95% Confidence Interval')
plt.title('Time Series with Heteroskedasticity and Drift')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.show()
