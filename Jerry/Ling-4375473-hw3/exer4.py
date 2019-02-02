import matplotlib.pyplot as plt
import numpy as np
import math
fig, ax = plt.subplots()

dx, dy = 0.005, 0.005
nx, ny = 2,5
kx, ky = math.pi, math.pi

psi = lambda x,y: np.sin(nx*kx*x)*np.sin(ny*ky*y)

x,y = np.mgrid[slice(0,1+dx, dx), slice(0, 1+dy, dy)]
z = 100*psi(x,y)**2*dx*dy
z_min, z_max = -np.abs(z).max(), np.abs(z).max()

plt.pcolor(x, y, z, cmap='Blues', vmin=0, vmax=z_max)
plt.xlabel("X")
plt.ylabel("Y",rotation=0)
plt.xticks([0,1],['0','L'])
plt.yticks([0,1],['0','L'])
plt.title('PDF of $n_x=2$, $n_y = 5$')
cbar = plt.colorbar()
cbar.set_ticks([0,0.0025])
cbar.set_ticklabels(['0', 'large'])

plt.show()
