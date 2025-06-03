import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from sklearn.datasets import make_blobs

# Generate a sample dataset with some outliers
X , y = make_blobs(n_samples=300 , centers=1, cluster_std=0.60,random_state=0)
outliers = np.random.uniform(low=-6,high=6, size=(20,2))
X = np.vstack((X, outliers))

# Fit the Isolation Forest model
model = IsolationForest(contamination=0.1,random_state=42)
model.fit(X)

# Predict anomalies
outliers = model.predict(X)

# Anomolies will be labeled as -1, and inliers will be labeld as 1
anomalies = X[outliers == -1]

# Plotting the results
plt.figure(figsize=(10,6))
plt.scatter(X[:,0], X[:,1], c ='blue', s=50, label= 'Inliers')
plt.scatter(anomalies[:,0], anomalies[:,1], 
            c='red', s=100, label='Anomalies',edgecolors='k')

plt.title('Anomaly Detection using Isolation Forest')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.show()