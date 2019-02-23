#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import math

n_x=2
n_y=5

d_x=.01
d_y=.01

y, x =np.meshgrid(np.linspace(0,1,500),np.linspace(0,1,500))

z=10**4*(np.sin(n_x*x*math.pi)*np.sin(n_y*y*math.pi))**2*d_x*d_y
"""
#z=z[:-1,:-1]
#z_min,z_max=-np.abs(z).max(), np.abs(z).max()

fig, ax = plt.subplots()
plot = ax.contour(x,y,z)
#ax.clabel(plot,fontsize=10)
ax.set_xlabel('X Coordinate')
ax.set_ylabel('Y Coordinate')

ax.locator_params(nbins=3)
ax.set_xticklabels( ('','0','L') )
ax.set_yticklabels( ('','0','L') )

fig.show()

input('Press <Enter> to continue')
"""
plt.contourf(x,y,z,levels=[0,.2,.4,.6,.8,1.0])
plt.xticks([0,1],['0','L'])
plt.yticks([0,1],['0','L'])
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
bar = plt.colorbar()
bar.set_ticks([0,.2,.4,.6,.8,1.0])
plt.show()
