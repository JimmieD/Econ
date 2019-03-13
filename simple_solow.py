#Written in Jupyter Notebook

from itertools import product

def plot_path(ax, alpha_s, s_vals, delta_s, series_length=50):
    """
    Add a time series plot to the axes ax for all given parameters.
    """
    k = np.empty(series_length)

    for (a, s, d) in product(alpha_s, s_vals, delta_s):
        k[0] = 1
        for t in range(series_length-1):
            k[t+1] = s * k[t]**a + (1 - d) * k[t]
        ax.plot(k, 'o-', label=r"$\alpha = {0},\; s = {1},\; \delta = {2}$".format(a, s, d))

    ax.grid(lw=0.2)
    ax.set_xlabel('time')
    ax.set_ylabel('capital')
    ax.set_ylim(0, 18)
    ax.legend(loc='upper left', frameon=True, fontsize=14)

fig, axes = plt.subplots(3, 1, figsize=(12, 15))

# Parameters (αs, s_vals, δs)
set_one = ([0.25, 0.33, 0.45], [0.4], [0.1])
set_two = ([0.33], [0.3, 0.4, 0.5], [0.1])
set_three = ([0.33], [0.4], [0.05, 0.1, 0.15])

for (ax, params) in zip(axes, (set_one, set_two, set_three)):
    alpha_s, s_vals, delta_s = params
    plot_path(ax, alpha_s, s_vals, delta_s)

plt.show()