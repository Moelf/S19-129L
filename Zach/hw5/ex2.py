#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


xpix = 640
ypix = 400

xc = int(xpix/2)
yc = int(ypix/2)

a = -.79
b = .56
c = complex(a, b)


def f(z):
    return z**2+c


pixColor = np.zeros((xpix, ypix), dtype='uint8')

temp = np.zeros((xpix, ypix))

for ix in range(xpix):
    x = (ix-xc)/200
    for iy in range(ypix):
        y = (iy-yc)/200
        n = 0.0
        n_max = 255.0
        z = complex(x, y)
        while np.abs(z) < 2 and n < n_max:
            z = f(z)
            n += 1
        # print(n)
        temp[ix, iy] = n

color = np.flipud(temp.transpose())

f1, ax1 = plt.subplots()
picture = ax1.imshow(color, interpolation='none', cmap='jet')
ax1.axis("off")
plt.title("Julia plot")
f1.show()

input("Press any button to exit")
