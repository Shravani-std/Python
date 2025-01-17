

from sklearn.datasets import make_blobs

X, Y = make_blobs(n_samples=500, centers=3,
				random_state=0, cluster_std=0.50)

import matplotlib.pyplot as plt

# plotting scatters
plt.scatter(X[:, 0], X[:, 1], c=Y, s=50, cmap='spring');
plt.show()

# creating linspace between -1 to 3.5
import numpy as np
xfit = np.linspace(-1, 5.5)

# plotting scatter
plt.scatter(X[:, 0], X[:, 1], c=Y, s=50, cmap='spring')

# plot a line between the different sets of data
for m, b, d in [(1, 0.65, 0.33), (0.5, 1.6, 0.55), (-0.2, 2.9, 0.2)]:
	yfit = m * xfit + b
	plt.plot(xfit, yfit, '-k')
	plt.fill_between(xfit, yfit - d, yfit + d, edgecolor='none',
	color='#AAAAAA', alpha=0.4)

plt.xlim(-1, 3.5);
plt.show()

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


data = pd.read_csv('/content/wdbc.data', header=None)
print(data.head(10))

# Assuming the first two columns are x and y values
x = data[1]  # First column for x values
y = data[2]

plt.scatter(x, y, c=y, cmap='jet')
plt.colorbar()  # Optional: Adds a color bar to the plot
plt.xlabel('X-axis Label')  # Label for x-axis
plt.ylabel('Y-axis Label')  # Label for y-axis
plt.title('Scatter Plot from WDBC Data')  # Title for the plot
plt.show()

xfit = np.linspace(-1, 5.5)



# plot a line between the different sets of data
for m, b, d in [(1, 0.65, 0.33), (0.5, 1.6, 0.55), (-0.2, 2.9, 0.2)]:
	yfit = m * xfit + b
	plt.plot(xfit, yfit, '-k')
	plt.fill_between(xfit, yfit - d, yfit + d, edgecolor='none',
	color='#AAAAAA', alpha=0.4)

plt.xlim(-1, 3.5);
plt.show()