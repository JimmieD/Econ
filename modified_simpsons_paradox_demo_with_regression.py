
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Setting a random seed for reproducibility
np.random.seed(seed=None)

# Function to generate data for a group
def generate_data(mean_x, slope, intercept, std_dev=2, n=100):
    x = np.random.normal(mean_x, std_dev, n)
    y = slope * x + np.random.normal(0, 2, n) + intercept
    return x, y

# Function to perform linear regression and plot
def plot_regression(x, y, group_label, color):
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    plt.plot(x, intercept + slope * x, color=color, label=f'{group_label} Regression')
    plt.scatter(x, y, label=group_label)

# Generating data for 5 groups with different means and trends
x_a, y_a = generate_data(20, 0.5, 20)
x_b, y_b = generate_data(30, 0.5, -20)
x_c, y_c = generate_data(25, 0.5, 5)
x_d, y_d = generate_data(35, 0.5, -5)
x_e, y_e = generate_data(40, 0.5, -25)

# Combining the data
x_combined = np.concatenate([x_a, x_b, x_c, x_d, x_e])
y_combined = np.concatenate([y_a, y_b, y_c, y_d, y_e])

print(f"Correlation within Group A: {np.corrcoef(x_a, y_a)[0,1]:.2f}")
print(f"Correlation within Group B: {np.corrcoef(x_b, y_b)[0,1]:.2f}")
print(f"Correlation within Group A: {np.corrcoef(x_c, y_c)[0,1]:.2f}")
print(f"Correlation within Group B: {np.corrcoef(x_d, y_d)[0,1]:.2f}")
print(f"Correlation within Group A: {np.corrcoef(x_e, y_e)[0,1]:.2f}")
print(f"Correlation of Combined Groups: {np.corrcoef(x_combined, y_combined)[0,1]:.2f}")

# Plotting
plt.figure(figsize=(12, 8))

# Plot regression for each group
plot_regression(x_a, y_a, 'subgroup A', 'r')
plot_regression(x_b, y_b, 'subgroup B', 'g')
plot_regression(x_c, y_c, 'subgroup C', 'b')
plot_regression(x_d, y_d, 'subgroup D', 'c')
plot_regression(x_e, y_e, 'sibgroup E', 'm')

# Linear regression for combined data
slope, intercept, r_value, p_value, std_err = stats.linregress(x_combined, y_combined)
plt.plot(x_combined, intercept + slope * x_combined, 'k', linewidth=2, label='Combined Regression for A-E')

plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('Demonstration of Simpsons Paradox for Combined Collective A-E')
plt.show()
