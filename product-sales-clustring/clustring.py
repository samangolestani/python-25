# Re-import necessary packages after code execution environment reset
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

# Reload the uploaded Excel file
file_path = "./product_sales_dataset.xlsx"
df = pd.read_excel(file_path)

# Group data by company_id and summarize features
company_summary = df.groupby("company_id").agg({
    "units_sold": "sum",
    "product_id": pd.Series.nunique,
    "channel": pd.Series.nunique,
    "region": pd.Series.nunique
}).rename(columns={
    "units_sold": "total_units_sold",
    "product_id": "unique_products",
    "channel": "channel_count",
    "region": "region_count"
})

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(company_summary)

# Apply KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=0)
company_summary['cluster'] = kmeans.fit_predict(X_scaled)

# Reduce dimensions to 2D using PCA for visualization
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Prepare DataFrame for plotting
plot_df = pd.DataFrame(X_pca, columns=['PCA1', 'PCA2'])
plot_df['cluster'] = company_summary['cluster'].values
plot_df['company_id'] = company_summary.index

# Plot the clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(data=plot_df, x='PCA1', y='PCA2', hue='cluster', palette='Set2', s=100)
plt.title('Company Clusters (PCA Reduced)')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend(title='Cluster')
plt.grid(True)
plt.tight_layout()
plt.show()
