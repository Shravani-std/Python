

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.mixture import GaussianMixture

# Step 1: Generate a synthetic dataset with 4 clusters
X, y = make_blobs(n_samples=500, centers=4, cluster_std=1.05, random_state=42)

plt.figure(figsize=(12, 8))
plt.scatter(X[:, 0], X[:, 1], s=30, c='black', label='Data Points')
plt.title("Generated Data with 4 Clusters")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.grid()
plt.show()

# Step 2: K-Means Clustering
kmeans = KMeans(n_clusters=4, random_state=42)
kmeans_labels = kmeans.fit_predict(X)

plt.figure(figsize=(12, 8))
plt.scatter(X[:, 0], X[:, 1], c=kmeans_labels, cmap='viridis', s=30)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', s=100, label='Centroids')
plt.title("K-Means Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.grid()
plt.show()

# Step 3: Hierarchical Clustering
agg_clustering = AgglomerativeClustering(n_clusters=4)
agg_labels = agg_clustering.fit_predict(X)

plt.figure(figsize=(12, 8))
plt.scatter(X[:, 0], X[:, 1], c=agg_labels, cmap='viridis', s=30)
plt.title("Hierarchical Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.grid()
plt.show()

# Step 4: DBSCAN Clustering
dbscan = DBSCAN(eps=0.3, min_samples=10)
dbscan_labels = dbscan.fit_predict(X)

plt.figure(figsize=(12, 8))
plt.scatter(X[:, 0], X[:, 1], c=dbscan_labels, cmap='viridis', s=30)
plt.title("DBSCAN Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.grid()
plt.show()

# Step 5: Gaussian Mixture Model Clustering
gmm = GaussianMixture(n_components=4, random_state=42)
gmm_labels = gmm.fit_predict(X)

plt.figure(figsize=(12, 8))
plt.scatter(X[:, 0], X[:, 1], c=gmm_labels, cmap='viridis', s=30)
plt.title("Gaussian Mixture Model Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.grid()
plt.show()