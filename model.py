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

# Optimal number of clusters 
optimal_k = 5
kmeans_model = KMeans(n_clusters=optimal_k, random_state=42, init='k-means++', n_init=50)
kmeans_model.fit(pca_data)

labels = kmeans_model.labels_

# Calculate silhouette score
score = silhouette_score(pca_data, labels)
print(f'The silhouette score for k = {optimal_k} is {score:.3f}')

# Calculate Davies-Bouldin Index using PCA data
dbi_score = davies_bouldin_score(pca_data, labels)
print(f"Davies-Bouldin Index: {dbi_score}")

# Add cluster labels back to the original data
data['cluster'] = labels

# Grouping by cluster and calculating means
cluster_means = data.groupby('cluster').mean()
print(cluster_means)

data['country'] = data_['country']  # Re-add country names

# Visualize the clusters
plt.figure(figsize=(8, 5))
plt.scatter(pca_data[:, 0], pca_data[:, 1], c=labels, s=30, cmap='viridis')
plt.title('PCA of Country Data with Clustering')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.colorbar(label='Cluster Label')
plt.grid()
plt.show()


# print(data[data['cluster'] == 0])               #First Cluster      (Tied in 2nd)
# print(data[data['cluster'] == 1])               #Second Cluster     Countries in direst need of aid (Last)
# print(data[data['cluster'] == 2])               #Third Cluster      (Tied in 2nd)
# print(data[data['cluster'] == 3])               #Fourth Cluster     (4th)
# print(data[data['cluster'] == 4])               #Fourth Cluster     Most Comfortable Countries (1st)

# Countries in direst need of aid 
dire_need_of_aid = data[data['cluster'] == 1]['country'].to_list()
print(f'Countries in dire need of aid are {len(dire_need_of_aid)} namely: {dire_need_of_aid}')

