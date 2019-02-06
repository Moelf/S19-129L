#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import math

n_x=2
n_y=5

d_x=.01
d_y=.01

y, x =np.meshgrid(np.linspace(0,1,500),np.linspace(0,1,500))

z=(2*np.sin(n_x*x*math.pi)*np.sin(n_y*y*math.pi))**2*d_x*d_y

z=z[:-1,:-1]
z_min,z_max=-np.abs(z).max(), np.abs(z).max()

fig, ax=plt.subplots()

graph=ax.pcolormesh(x, y, z, cmap='RdBu', vmin=0, vmax=z_max)
ax.set_title('Position PDF')
ax.set_xlabel('X')
ax.set_ylabel('Y')
#ax.axis([x.min(), x.max(), y.min(), y.max()])
fig.colorbar(graph)#, ax=ax)
plt.show()