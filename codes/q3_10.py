# By Nehan mohammad
# 31-October-26, Saturday, question no: 3.10

import numpy as np
import matplotlib.pyplot as plt
import subprocess

# Define frequency and time domains for exponential decay
f = np.linspace(-10, 10, 2001)
t = np.linspace(0, 5, 5001)
a = 2.0
exp_signal = np.exp(-a * t)

# Calculate numerical Fourier integral
Exp_num = np.array([
    np.trapezoid(exp_signal * np.exp(-1j * 2 * np.pi * fi * t), t)
    for fi in f
])
Exp_exact = 1.0 / (a + 1j * 2 * np.pi * f)

# Plot analytical vs numerical real part
plt.figure(figsize=(9, 4), dpi=300)
plt.plot(f, Exp_exact.real, label='Analytical Real Part', color='blue', linewidth=0.5)
plt.plot(f, Exp_num.real, '--', label='Numerical Real Part', color='red', linewidth=0.5)
plt.xlabel('Frequency (Hz)', fontsize=9)
plt.ylabel('Real part', fontsize=9)
plt.legend(fontsize=8, loc='upper right')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('3_10.png', dpi=300)
plt.close()

# Open generated image using termux-open
# subprocess.run(['termux-open', 'exponential_fourier_real.png'])
