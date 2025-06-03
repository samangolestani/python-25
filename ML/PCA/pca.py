import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA

#load A sample dataset (Iris dataset)
data = load_iris()
X = data.data # Feature data

# Standardize the data (very important for PCA)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

# Apply PCA

pca = PCA(n_components=2) # We want to reduce to 2 dimensions

X_pca =  pca.fit_transform(X_scaled)

#  Explained variance ratio
print("Explained variance ratio:",
      pca.explained_variance_ratio_)

# Plotting the PCA results
plt.figure(figsize = (8,6))
plt.scatter(X_pca[:,0], X_pca[:,1], c=data.target, cmap = 'viridis', edgecolors='k', s=100)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA of Iris Dataset')
plt.colorbar(label = 'Classes')
plt.show()