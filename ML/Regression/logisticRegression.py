import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Parameters
mu = [0, 0]        # Mean for X1 and X2
sigma = [1, 1]     # Standard deviation for X1 and X2
n_samples = 300    # Total number of samples (divided among 3 classes)

# Generate synthetic data for three classes
def generate_class_data(label, mu, sigma, n):
    X1 = np.random.normal(mu[0], sigma[0], n)
    X2 = np.random.normal(mu[1], sigma[1], n)
    y = np.full(n, label)
    return np.column_stack((X1, X2)), y

# Create datasets for classes 'a', 'b', and 'c'
Xa, ya = generate_class_data('a', [0, 0], [1, 1], n_samples)
Xb, yb = generate_class_data('b', [3, 3], [1, 1], n_samples)
Xc, yc = generate_class_data('c', [0, 4], [1, 1], n_samples)

# Combine the datasets
X = np.vstack((Xa, Xb, Xc))
y = np.concatenate((ya, yb, yc))

# Encode target labels to numeric values
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.3, random_state=42)

# Logistic Regression (multinomial)
model = LogisticRegression(multi_class='multinomial', solver='lbfgs', max_iter=1000)
model.fit(X_train, y_train)

# Prediction and evaluation
y_pred = model.predict(X_test)
print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=le.classes_))
