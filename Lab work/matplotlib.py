

import seaborn as sns
import matplotlib.pyplot  as plt
import numpy as np

tips = sns.load_dataset('tips')
sns.scatterplot(x = "total_bill",y = "tip", data = tips)
plt.show()

sns.lineplot(x = "total_bill",y = "tip", data = tips)
plt.show()

sns.histplot(tips["total_bill"])
plt.show()

sns.boxplot(x="day",y="total_bill",data=tips)
plt.show()

data = np.random.rand(11,13)
sns.heatmap(data)
plt.show()

sns.pairplot(tips)
plt.show()

g = sns.FacetGrid(tips, col="time")
g.map(sns.histplot, "total_bill")
plt.show()