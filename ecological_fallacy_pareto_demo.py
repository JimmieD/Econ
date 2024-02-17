import matplotlib.pyplot as plt
import numpy as np

# Generating individual data points for two groups with Pareto distribution
np.random.seed(42)  # For reproducibility
# Parameters for the Pareto distribution: scale (x_m) and shape (alpha)
scale_A, alpha_A = 1, 5  # Group A
scale_B, alpha_B = 1, 4  # Group B
size = 100  # Number of individuals in each group

group_A_property = (np.random.pareto(alpha_A, size) + 1) * scale_A
group_B_property = (np.random.pareto(alpha_B, size) + 1) * scale_B

# Concatenate data for plotting
all_property = np.concatenate([group_A_property, group_B_property])
group_labels = ['A'] * size + ['B'] * size  # Labels for groups

# Calculating group averages
average_property_A = np.mean(group_A_property)
average_property_B = np.mean(group_B_property)

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(range(2*size), all_property, c=['blue' if label == 'A' else 'green' for label in group_labels], alpha=0.5, label='Individuals')
plt.plot([0, size], [average_property_A, average_property_A], color='darkblue', label='Group A Average', linestyle='--')
plt.plot([size, 2*size], [average_property_B, average_property_B], color='darkgreen', label='Group B Average', linestyle='--')

plt.xlabel('Individuals')
plt.ylabel('Some Quantified Characteristic or Propert (note the scale)')
plt.title('Demonstration of the Ecological Fallacy with Pareto Distribution')
plt.yscale('log')  # Using logarithmic scale for better visualization of Pareto distribution
plt.legend()
plt.show()
