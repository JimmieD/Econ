import matplotlib.pyplot as plt
import numpy as np

# Generating individual data points for two groups
np.random.seed(42)  # For reproducibility
group_A_ages = np.random.normal(40, 15, 100)  # Group A with mean age 30
group_B_ages = np.random.normal(60, 20, 100)  # Group B with mean age 40

# Concatenate data for plotting
all_ages = np.concatenate([group_A_ages, group_B_ages])
group_labels = ['A'] * 100 + ['B'] * 100  # Labels for groups

# Calculating group averages
average_age_A = np.mean(group_A_ages)
average_age_B = np.mean(group_B_ages)

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(range(200), all_ages, c=['blue' if label == 'A' else 'green' for label in group_labels], alpha=0.5, label='Individuals')
plt.plot([0, 100], [average_age_A, average_age_A], color='darkblue', label='Group A Average', linestyle='--')
plt.plot([100, 200], [average_age_B, average_age_B], color='darkgreen', label='Group B Average', linestyle='--')

plt.xlabel('Individuals')
plt.ylabel('Some Quantified Characteristic or Property')
plt.title('Simple Demo of an Ecological Fallacy (Individuals are not Averages)')
plt.legend()
plt.show()
