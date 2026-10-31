# By Nehan mohammad
# 31-October-26, Saturday, question no: 1.1

import numpy as np
import matplotlib.pyplot as plt
import subprocess

# Generate time vector for two full cycles of the waveform
A0 = 12
f0 = 50
t = np.linspace(0, 2 / f0, 2000)

# Calculate the rectified sinusoidal signal values
xt = A0 * np.abs(np.sin(2 * np.pi * f0 * t))

# Configure plot parameters with high resolution and thin line width
plt.figure(figsize=(10, 4), dpi=300)
plt.plot(t, xt, color='b', linewidth=0.5)
plt.grid(True)
plt.title('Plot of $x(t) = A_0 |\\sin(2\\pi f_0 t)|$')
plt.xlabel('Time $t$ (s)')
plt.ylabel('$x(t)$')
plt.tight_layout()

# Save the figure to the local directory
plt.savefig('q1_1_plot.png', dpi=300)
plt.close()

# Open the saved image using termux-open via subprocess
# subprocess.run(['termux-open', 'rectified_sine.png'])
