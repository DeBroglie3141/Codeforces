import numpy as np

max_times = np.argmax(data, axis=1)
max_vals = data[np.arange(data.shape[0]), max_times]

means = np.mean(data, axis=1)
stds = np.std(data, axis=1)

stds_safe = np.where(stds == 0, 1, stds)

normalized = (data - means[:, None]) / stds_safe[:, None]

anomalies = np.sum(np.abs(normalized) > 2, axis=1)

for i in range(100):
    print(f"{max_vals[i]:.2f} {max_times[i]} {anomalies[i]}")