#!/usr/bin/env python3
#
# Put on the screen a pixel map with
# concentric circles
#
# CC 8-Feb-2019
#-----------------------
import numpy as np
import math
import matplotlib.pyplot as plt

# The color map..pick whatever you like
# More choices here
# https://matplotlib.org/examples/color/colormaps_reference.html
thisMap = "jet"
#thisMap = "brg"
#thisMap = "terrain"
#thisMap = "gnuplot"
#thisMap="ocean"
#thisMap ="brg"

# the size of the figure in pixels
xpix = 500
ypix = 200

# the center of the picture
xc = int(xpix/2)
yc = int(ypix/2)

# the pixel color map...instantiate a numpy array
# with one entry per pixel and of unsigned integer
# type, one byte (0 to 255)
# In other words: each pixel will be assigned
# a color from 0 to 255
pixColor = np.zeros( (xpix,ypix), dtype="uint8")

# we fill the "temp" array (brute force way)
temp     = np.zeros( (xpix,ypix) )
for ix in range(xpix):
    for iy in range(ypix):
        r = math.sqrt( (ix-xc)*(ix-xc) + (iy-yc)*(iy-yc) )
        temp[ix,iy] = r

# This is a different way of filling "temp"
# Maybe more elegant and faster. But more obscure
# x       = np.linspace(1, xpix, xpix)
# y       = np.linspace(1, ypix, ypix)
# x.shape = (xpix, 1)
# temp    = np.sqrt( (x-xc)*(x-xc) + (y-yc)*(y-yc) )

# the pixel map goes from 0 to 255
pixColor = 255 * temp / (temp.max())

# Stupid thing: when putting it on the screen
# the 1st index is the column and the 2nd index is the
# row.  So in order to really have [ix, iy] we need to
# transpose before plotting.
# Even more stupid: the vertical dimension increases
# from the top, not from the bottom.  The "flipud" function
# chnges the order of the rows
newpixColor = np.flipud(pixColor.transpose())

# now the plot
f1, ax1 = plt.subplots()
picture = ax1.imshow(newpixColor, interpolation="none", cmap=thisMap)
ax1.axis("off")   # axis labels off
f1.show()         # show it on the screen
input("Press <Enter> to exit")  # we are done
