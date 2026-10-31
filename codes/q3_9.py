# By Nehan mohammad
# 31-October-26, Saturday, question no: 3.9

import numpy as np
import matplotlib.pyplot as plt
import subprocess

# Define frequency and time domains for triangular pulse
f = np.linspace(-8, 8, 1601)
t = np.linspace(-2, 2, 8001)
tri = np.maximum(0, 1 - np.abs(t))

# Calculate numerical Fourier integral
Tri_num = np.array([
    np.trapezoid(tri * np.exp(-1j * 2 * np.pi * fi * t), t)
    for fi in f
])
Tri_exact = np.sinc(f)**2

# Plot analytical vs numerical Fourier transform
plt.figure(figsize=(9, 4), dpi=300)
plt.plot(f, Tri_exact, label='Analytical sinc^2(f)', color='blue', linewidth=0.5)
plt.plot(f, Tri_num.real, '--', label='Numerical Fourier transform', color='red', linewidth=0.5)
plt.xlabel('Frequency (Hz)', fontsize=9)
plt.ylabel('Magnitude / real part', fontsize=9)
plt.legend(fontsize=8, loc='upper right')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('3_9.png', dpi=300)
plt.close()

# Open generated image using termux-open
# subprocess.run(['termux-open', 'triangular_fourier.png'])
