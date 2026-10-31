# By Nehan mohammad
# 31-October-26, Saturday, question no: 3.8

import numpy as np
import matplotlib.pyplot as plt
import subprocess

# Define signal parameters and impulse summation limits
A0, f0 = 12, 50
M = 10
m = np.arange(-M, M + 1)
dm = 2 * A0 / (np.pi * (1 - 4 * m**2))
f_impulses = 2 * m * f0

# Plot the Fourier transform impulse spectrum
plt.figure(figsize=(9, 4), dpi=300)
plt.stem(f_impulses, dm, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.xlabel('Frequency (Hz)', fontsize=9)
plt.ylabel('Impulse weight', fontsize=9)
plt.title('Fourier Transform of $A_0 |\\sin(2\\pi f_0 t)|$', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('fourier_transform_impulses.png', dpi=300)
plt.close()

# subprocess.run(['termux-open', 'fourier_transform_impulses.png'])

# Verify the finite Fourier-series reconstruction
t = np.linspace(-0.02, 0.02, 2000)
x = A0 * np.abs(np.sin(2 * np.pi * f0 * t))
x_rec = np.zeros_like(t, dtype=complex)
for mi, coeff in zip(m, dm):
    x_rec += coeff * np.exp(1j * 2 * np.pi * (2 * mi * f0) * t)

plt.figure(figsize=(9, 4), dpi=300)
plt.plot(t, x, label='Original signal', color='blue', linewidth=0.5)
plt.plot(t, x_rec.real, '--', label='Fourier reconstruction', color='red', linewidth=0.5)
plt.xlabel('Time (s)', fontsize=9)
plt.ylabel('Amplitude', fontsize=9)
plt.legend(fontsize=8, loc='upper right')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('3_8.png', dpi=300)
plt.close()

# subprocess.run(['termux-open', 'fourier_transform_verify.png'])
