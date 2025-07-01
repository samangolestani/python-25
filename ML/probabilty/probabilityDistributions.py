import numpy as np
import matplotlib.pyplot as plt

# Parameters
p = 0.6  # Probability of success (1)
size = 10  # Number of trials

# Generate Bernoulli random variables
# data = np.random.binomial(n=1, p=p, size=size)
# Generate Binomial random variables
# data = np.random.binomial(n=10,p=p,size=size)
# Generate Geometrics random variables
# data = np.random.geometric(p = 0.1, size=size)
# Generate poisson random variables
# data = np.random.poisson(lam=3.7,size=size)
# Plotting the distribution
# Generate exponential random variables
lambda_param = 1  # Rate parameter (λ)
scale = 1 / lambda_param
# data = np.random.exponential(scale=scale,size=size)

mu = 0.5  # Mean (center of the distribution)
sigma = 2 # Standard deviation (spread)
# Generate normal random variables
data = np.random.normal(mu, sigma, size)

plt.hist(data, bins=20, edgecolor='black', alpha=0.7, density=True)
plt.title(f'Normal Distribution (µ={mu}, σ={sigma})')
plt.xlabel('Value')
plt.ylabel('Density')
plt.grid(True)

# Plotting the theoretical normal curve for comparison
x = np.linspace(min(data), max(data), 1000)
y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
plt.plot(x, y, 'r-', lw=2)

plt.show()

# Display the first 10 values to verify
print(data[:10])