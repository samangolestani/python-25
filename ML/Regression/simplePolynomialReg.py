import numpy as np
import matplotlib.pyplot as plt

# Generate some example data
np.random.seed(42)
X = np.random.rand(100, 1) * 10  # 100 data points from 0 to 10
y = X**3 # Non-linear (quadratic) function + noise

# Transform X to include polynomial features (degree 2 in this case)
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=3)
X_poly = poly.fit_transform(X)

# Fit the polynomial regression model
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_poly, y)

# Predict using the model
y_pred = model.predict(X_poly)

# Visualize the result
plt.scatter(X, y, color='blue', label='Data points')
plt.plot(X, y_pred, color='red', label='Fitted polynomial curve')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()

print(f"Polynomial regression coefficients: {model.coef_}")
print(f"Intercept: {model.intercept_}")
