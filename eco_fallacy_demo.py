import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set seed for reproducibility
np.random.seed(42)

# Function to generate individual-level data with a positive correlation
def generate_group_data(mean_x, mean_y, n=100):
    x = np.random.normal(mean_x, 5, n)
    y = 0.5 * x + np.random.normal(mean_y, 2, n) - mean_x * 0.4  # Ensuring a positive correlation within the group
    return x, y

# Generating data for 3 groups
groups = ['Group 1', 'Group 2', 'Group 3']
data = []
for i, group in enumerate(groups):
    x, y = generate_group_data(i * 10, i * 5, 100)
    data.append(pd.DataFrame({'X': x, 'Y': y, 'Group': np.repeat(group, 100)}))

# Concatenating all group data
df = pd.concat(data)

# Aggregating data
df_agg = df.groupby('Group').mean().reset_index()

# Plotting individual-level data
plt.figure(figsize=(10, 5))
for group in groups:
    subset = df[df['Group'] == group]
    plt.scatter(subset['X'], subset['Y'], label=group)
plt.title('Individual-Level Data: Positive Correlation Within Each Group')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

# Plotting aggregated data
plt.figure(figsize=(5, 5))
plt.scatter(df_agg['X'], df_agg['Y'], color='red')
for i, txt in enumerate(df_agg['Group']):
    plt.annotate(txt, (df_agg['X'][i], df_agg['Y'][i]))
plt.title('Aggregated Data Showing Negative Trend')
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(df_agg['X'], np.poly1d(np.polyfit(df_agg['X'], df_agg['Y'], 1))(df_agg['X']), color="blue")  # Linear fit
plt.show()
