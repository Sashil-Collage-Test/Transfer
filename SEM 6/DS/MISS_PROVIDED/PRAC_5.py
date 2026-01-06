import warnings
warnings.filterwarnings("ignore")
import os
os.environ["LOLY_MAX_CPU_COUNT"]="1"
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
X,_=make_blobs(n_samples=300, centers=4, random_state=42)
inertia=[]
K_range=range(1,11)
for k in K_range:
    kmeans=KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X)
    inertia.append(kmeans.inertia_)
plt.plot(K_range, inertia, marker='o', linestyle='--')
plt.xlabel('Number of Cluster(k)')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal k')
plt.show()
kmeans=KMeans(n_clusters=4, random_state=42, n_init=10)
y_kmeans=kmeans.fit_predict(X)
plt.scatter(X[:,0], X[:,1], c=y_kmeans, cmap='viridis', edgecolors='k')
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1],
            s=200, marker='X', label='Centroids')
plt.title('K-Means Clustering Result')
plt.legend()
plt.show()
