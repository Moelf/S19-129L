import matplotlib.pyplot as plt
import numpy as np
import math
fig, ax = plt.subplots()

dx, dy = 0.01, 0.01
nx, ny = 2, 5
kx, ky = math.pi, math.pi


def psi(x, y): return np.sin(nx*kx*x)*np.sin(ny*ky*y)


x, y = np.mgrid[slice(0, 1+dx, dx), slice(0, 1+dy, dy)]
z = psi(x, y)**2*dx*dy
scale = 1/np.max(z)
z = z*scale
z_min, z_max = -np.abs(z).max(), np.abs(z).max()

CS = ax.contour(x, y, z)
plt.pcolor(x, y, z, cmap='Blues', vmin=0, vmax=z_max)
plt.xlabel("X")
plt.ylabel("Y", rotation=0)
plt.xticks([0, 1], ['0', 'L'])
plt.yticks([0, 1], ['0', 'L'])
plt.title('PDF of particle in a box with: $n_x=2$, $n_y = 5$')
ax.clabel(CS, inline=True, fontsize=10)
cbar = plt.colorbar()
cbar.set_ticks([0, z_max])
cbar.set_ticklabels(['0', 'large'])

plt.show()
