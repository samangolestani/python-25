import numpy as np
import matplotlib.pyplot as plt

# Generate some example data
# X is the feature, and y is the target variable
np.random.seed(42)
X = np.random.rand(100, 1) * 10  # 100 data points from 0 to 10
y = 2.5 * X + np.random.randn(100, 1) * 2  # y = 2.5 * X + noise

# Add a bias column (a column of ones) to X to account for the intercept
X_b = np.c_[np.ones((X.shape[0], 1)), X]

# Compute the optimal weights using the Normal Equation: θ = (X^T * X)^(-1) * X^T * y
theta = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

# Predict using the computed theta
y_pred = X_b.dot(theta)

# Visualize the result
plt.scatter(X, y, color='blue', label='Data points')
plt.plot(X, y_pred, color='red', label='Fitted line')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()

print(f"Optimal parameters (theta): {theta}")
