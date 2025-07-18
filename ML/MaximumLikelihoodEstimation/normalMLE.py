import numpy as np
from scipy.optimize import minimize
from scipy.stats import norm  # <--- This line fixes the error

# Generate synthetic data
np.random.seed(42)
data = np.random.normal(loc=5, scale=2, size=100)

# Negative log-likelihood function
def negative_log_likelihood(params):
    mu, sigma = params[0], params[1]
    if sigma <= 0:
        return np.inf
    return -np.sum(norm.logpdf(data, loc=mu, scale=sigma))

initial_guess = [0, 1]
result = minimize(negative_log_likelihood, initial_guess, method='L-BFGS-B', bounds=[(None, None), (1e-5, None)])
mle_mu, mle_sigma = result.x
print(f"MLE estimate for mu: {mle_mu:.4f}")
print(f"MLE estimate for sigma: {mle_sigma:.4f}")
