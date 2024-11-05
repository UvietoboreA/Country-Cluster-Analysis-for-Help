import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score

# Load the dataset
data_ = pd.read_csv('Country-data.csv', low_memory=False)

# Drop the 'country' column for clustering
data = data_.drop(columns=['country'])

# Log-transform specific columns
data['income'] = np.log1p(data['income'])  # Handle zero values gracefully
data['gdpp'] = np.log1p(data['gdpp'])      # Handle zero values gracefully

# Perform PCA
pca = PCA(n_components=0.95)
pca_data = pca.fit_transform(data)

# Elbow method for KMeans
inertias = []
k_values = range(1, 11)
for k in k_values:
    kmeans = KMeans(n_clusters=k, init='k-means++', n_init=15, random_state=42)
    kmeans.fit(pca_data)
    inertias.append(kmeans.inertia_)

# Plotting the elbow method
plt.figure(figsize=(8, 5))
plt.plot(k_values, inertias, marker='o')
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.grid()
plt.show()