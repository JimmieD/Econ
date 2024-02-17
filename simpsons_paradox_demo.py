import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Setting a random seed for reproducibility
np.random.seed(42)

# Generating data for Group A
x_a = np.random.normal(20, 5, 100)
y_a = 0.5 * x_a + np.random.normal(0, 2, 100) + 20

# Generating data for Group B
x_b = np.random.normal(30, 5, 100)
y_b = 0.5 * x_b + np.random.normal(0, 2, 100) - 20

# Combining the data
x_combined = np.concatenate([x_a, x_b])
y_combined = np.concatenate([y_a, y_b])

# Performing linear regression within each group and on the combined data
slope_a, intercept_a, _, _, _ = stats.linregress(x_a, y_a)
slope_b, intercept_b, _, _, _ = stats.linregress(x_b, y_b)
slope_combined, intercept_combined, _, _, _ = stats.linregress(x_combined, y_combined)

# Plotting
plt.figure(figsize=(12, 6))

# Group A
plt.scatter(x_a, y_a, color='blue', alpha=0.5, label='Group A')
line_a = slope_a * x_a + intercept_a
plt.plot(x_a, line_a, color='blue', linewidth=2, label='Trend A')

# Group B
plt.scatter(x_b, y_b, color='red', alpha=0.5, label='Group B')
line_b = slope_b * x_b + intercept_b
plt.plot(x_b, line_b, color='red', linewidth=2, label='Trend B')

# Combined regression line
line_combined = slope_combined * x_combined + intercept_combined
plt.plot(x_combined, line_combined, color='green', linewidth=2, linestyle='--', label='Combined Trend')

plt.title("Visual Demonstration of Simpson's Paradox")
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

# Displaying correlation coefficients
print(f"Correlation within Group A: {np.corrcoef(x_a, y_a)[0,1]:.2f}")
print(f"Correlation within Group B: {np.corrcoef(x_b, y_b)[0,1]:.2f}")
print(f"Correlation of Combined Groups: {np.corrcoef(x_combined, y_combined)[0,1]:.2f}")
