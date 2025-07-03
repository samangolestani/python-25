import numpy as np
import matplotlib.pyplot as plt
import math

# Define the functions
def f(x):
    return x*2 +1

def g(x):
    return math.cos(x)

# Sample the functions
N = 1000  # Number of points
x = np.linspace(-10, 10, N)
dx = x[1] - x[0]  # Spacing

f_samples = np.vectorize(np.sin)(x)
g_samples = np.vectorize(np.cos)(x)

# Pad signals to avoid circular convolution
padded_size = N + len(g_samples) - 1
f_padded = np.pad(f_samples, (0, padded_size - N), mode='constant')
g_padded = np.pad(g_samples, (0, padded_size - N), mode='constant')

# Compute FFT
fft_f = np.fft.fft(f_padded)
fft_g = np.fft.fft(g_padded)

# Multiply in frequency domain
fft_conv = fft_f * fft_g

# Inverse FFT to get convolution
conv_result = np.fft.ifft(fft_conv).real  # Take real part to remove tiny imaginary noise

# Trim and scale by dx (for proper integration approximation)
conv_result = conv_result[:N] * dx

# Direct convolution (for validation)
direct_conv = np.convolve(f_samples, g_samples, mode='same') * dx

# Plot results
plt.figure(figsize=(12, 6))
plt.plot(x, f_samples, label=r"$f(x) = sin(x)$")
plt.plot(x, g_samples, label=r"$g(x) = \mathrm{cos}(x)$")
plt.plot(x, conv_result, label="FFT-based convolution", linestyle="--", linewidth=2)
plt.plot(x, direct_conv, label="Direct convolution", linestyle=":", linewidth=2)
plt.xlabel("x")
plt.ylabel("Amplitude")
plt.title("FFT vs Direct Convolution")
plt.legend()
plt.grid(True)
plt.show()