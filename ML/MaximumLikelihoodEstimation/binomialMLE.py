from scipy.optimize import minimize
from scipy.stats import binom
import numpy as np

# Simulate binomial data: 10 trials per experiment, p=0.6, repeated 100 times
n = 10
np.random.seed(0)
data = np.random.binomial(n=n, p=0.73
                          , size=1000)

# Negative log-likelihood for binomial
def neg_log_likelihood_binom(p):
    if p <= 0 or p >= 1:
        return np.inf
    return -np.sum(binom.logpmf(data, n=n, p=p))

# Optimize
result = minimize(neg_log_likelihood_binom, x0=[0.5], bounds=[(0.0001, 0.9999)])
mle_p = result.x[0]
print(f"MLE estimate for p: {mle_p:.4f}")
