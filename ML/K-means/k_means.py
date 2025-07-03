import numpy as np
import matplotlib.pyplot as plt

def initialize_centroids(X, k):
    """Seleciona aleatoriamente k pontos como centróides iniciais."""
    indices = np.random.choice(X.shape[0], k, replace=False)
    return X[indices]

def assign_clusters(X, centroids):
    """Atribui cada ponto ao centróide mais próximo."""
    distances = np.linalg.norm(X[:, np.newaxis] - centroids, axis=2)
    return np.argmin(distances, axis=1)

def update_centroids(X, labels, k):
    """Atualiza os centróides calculando a média de cada grupo."""
    return np.array([X[labels == i].mean(axis=0) for i in range(k)])

def has_converged(old_centroids, new_centroids, tol=1e-4):
    """Verifica se os centróides mudaram menos que a tolerância."""
    return np.linalg.norm(new_centroids - old_centroids) < tol

def kmeans(X, k, max_iters=100):
    centroids = initialize_centroids(X, k)
    for _ in range(max_iters):
        labels = assign_clusters(X, centroids)
        new_centroids = update_centroids(X, labels, k)
        if has_converged(centroids, new_centroids):
            break
        centroids = new_centroids
    return centroids, labels

# Exemplo de uso
if __name__ == "__main__":
    from sklearn.datasets import make_blobs

    # Gerando dados fictícios
    X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.6, random_state=0)
    
    # Rodando K-means
    k = 3
    centroids, labels = kmeans(X, k)

    # Visualizando
    plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
    plt.scatter(centroids[:, 0], centroids[:, 1], s=200, c='red', marker='X')
    plt.title('K-Means Clustering')
    plt.show()
