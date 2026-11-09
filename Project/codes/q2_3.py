# By Nehan mohammad
# 31-October-26, Saturday, question no: 2.3

import numpy as np
import matplotlib.pyplot as plt
import subprocess

# Define signal parameters and truncation limit N for Fourier series
A0 = 12
f0 = 50
N = 14

# Generate time vector for one full period from 0.005s to 0.015s
t = np.linspace(0.005, 0.015, 2000)

# Calculate the original rectified sinusoidal wave
x_orig = A0 * np.abs(np.sin(2 * np.pi * f0 * t))

# Reconstruct wave using truncated complex exponential Fourier series coefficients
x_recon = np.zeros_like(t, dtype=complex)
for k in range(-N, N + 1):
    if k % 2 == 0:
        ck = (2 * A0) / (np.pi * (1 - k**2))
    else:
        ck = 0.0
    x_recon += ck * np.exp(1j * 2 * np.pi * k * f0 * t)

# Configure clean proportions, thin line widths, and legible font sizes
plt.figure(figsize=(8, 4), dpi=300)
plt.plot(t, x_orig, label='Original $x(t)$', color='blue', linewidth=0.5)
plt.plot(t, x_recon.real, label=f'Reconstructed ($N={N}$)', color='red', linestyle='--', linewidth=0.5)
plt.xlim(0.005, 0.015)
plt.grid(True, linestyle='--', alpha=0.5)
plt.title('Fourier Series Reconstruction vs Original Signal', fontsize=10)
plt.xlabel('Time $t$ (s)', fontsize=9)
plt.ylabel('$x(t)$', fontsize=9)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
plt.legend(fontsize=8, loc='upper right')
plt.tight_layout()

# Save the generated figure locally and close the plot instance
plt.savefig('2_3.png', dpi=300)
plt.close()

# Open the image file using termux-open via subprocess
# subprocess.run(['termux-open', 'fourier_reconstruction.png'])
