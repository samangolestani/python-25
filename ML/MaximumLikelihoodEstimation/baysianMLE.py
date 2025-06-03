import pymc as pm
import numpy as np
from scipy.signal import gaussian

data = np.random.normal(5, 2, 100)

with pm.Model() as model:
    mu = pm.Normal("mu", mu=0, sigma=10)
    sigma = pm.HalfNormal("sigma", sigma=10)
    y = pm.Normal("y", mu=mu, sigma=sigma, observed=data)

    # MAP estimate = mode of posterior (close to MLE with flat priors)
    map_estimate = pm.find_MAP()
    print(map_estimate)
