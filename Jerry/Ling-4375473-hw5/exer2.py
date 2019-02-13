import matplotlib.pyplot as plt
import numpy as np

xpix_range = 640  # setting up pixel range
ypix_range = 400


def nFinder(z, interation=0):
    if abs(z) > 2:
        return 0  # standard case
    elif interation > 255:  # truncate
        return 255
    else:
        return 1+nFinder(f(z), interation+1)  # tail recursion 1+1+....+0

# f(z) we are given


def f(z):
    c = complex(-0.79, 0.56)
    return z**2 + c


# initialize pixel map
pixMap = np.zeros((xpix_range, ypix_range), dtype='uint8')

for xpix in range(0, xpix_range):
    for ypix in range(0, ypix_range):
        x_coord = -1.6 + 3.2 * xpix / xpix_range  # scale to math coordinates
        y_coord = -1 + 2 * ypix / ypix_range
        z = complex(x_coord, y_coord)
        n = nFinder(z)
        pixMap[xpix][ypix] = n

pixMap = np.flipud(pixMap.transpose())  # correct the orientation

picture = plt.imshow(pixMap, interpolation='none', cmap='terrain')
plt.title("Julia set for $c = -0.79 + i0.56$")
plt.show()
