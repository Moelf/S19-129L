#!/usr/bin/env python3
#
# A demonstration of various histogramming options.
# Histograms will be filled with some random numbers.
#
# ccHistStuff contains a couple 
# of simple functions to display histograms
# better.  The most important one is that
# it can add a box with some statistics
# to a histogram.
# In order to use it, must have ccHistStuff.py
# in your working directory (or in a directory
# included in PYTHONPATH)
#
# CC 25 Jan 2019
#------------------------
import ccHistStuff as cc
import math
import numpy as np
import matplotlib.pyplot as plt


# Initaliize the random number generator
# in a repeatable way by specifying the seed
seed = 12345
np.random.seed(seed)

# We will be plotting in different ways two histograms.
# Both of them will be filled with random numbers
# - one of them with uniform random numbers btw 0 and 1
# - the other one by picking according to exponential
# Histograms will have same binning
beta = 0.2
x = np.random.rand(1000)    # 1K uniform random numbers
y = np.random.exponential(beta, 1000)  #1k according to exp(-y/beta)
  
# This is an array with histogram bin edges
# np.linspace returns evenly spaced numbers over a range
low   = 0.
high  = 1.
nbins = 10
bins  = np.linspace(low, high, nbins+1) # no. edges = no. bins + 1 (!!!)

#------------------------------------------------------
# Plot the 1st hitogram by itself.
# Will do some prettyfication
#------------------------------------------------------

# Figure with 1 plot only
# If we wanted (say) four plots in a 2x2 grid
# we would instead do plt.subplots(2,2)
fig, ax = plt.subplots()

# Define the histogram
# contents = an array with the bin contents
# binEdges = an array with the bin edges (which we already have in this case)
# _ ("underscore") is a "throwaway" variable name to indicate that part of a
# function result is being deliberately ignored  (this can also be omitted)
contents, binEdges, _ = ax.hist(x, bins, histtype='step', log=False, color='blue')

# Add a stats box at the top right edge (CUSTOM CODE)
cc.statBox(ax, x, binEdges)

# Add errors  (CUSTOM CODE)
cc.plotErr(ax, contents, binEdges, color='blue')

# The default is to *not* have the x axis run from
# the lowest bin edge to the highest bin edge.
#
# This seems pretty silly, so override this
ax.set_xlim(binEdges[0], binEdges[-1])

# Set a generous vertical range to leave room for the stat box
ax.set_ylim(0. , 1.4*np.max(contents))

# I do not like the defaults....
# I want the ticks to be into the plot, also on the right of the plot
ax.tick_params("both", direction='in', length=10, right=True)

# I want a (minor) tick at the edge of each x bin 
ax.set_xticks(binEdges, minor=True)
ax.tick_params("both", direction='in', length=7, right=True, which='minor')

# now we show it
fig.show()
input("Press any key to continue")

#------------------------------------------
# Next: two histograms on the same plot
#-------------------------------------------

fig2, ax2 = plt.subplots()

# The 2nd histogram....
# Will colorize it ("stepfilled") with some transparencies ("alpha")
c2, b2, _ = ax2.hist(y, bins, histtype='stepfilled', log=False, color='red', 
                     label='yyy', alpha=0.5)

# These statements are the same as the example above
# for the first histogram except that
# (a) added a "label" for the legend
# (b) no error bars
# (c) no stat box
c1, b1, _ = ax2.hist(x, bins, histtype='step', log=False, color='blue', label='xxx')
ax2.set_xlim(binEdges[0], binEdges[-1])
ax2.tick_params("both", direction='in', length=10, right=True)
ax2.set_xticks(binEdges, minor=True)
ax2.tick_params("both", direction='in', length=7, right=True, which='minor')

# We take the y axis to extend 10% above the largest bin of either histograms
ax2.set_ylim(0. , 1.1*max( np.max(c1),np.max(c2) ))

# Add a legend in the upprt right corner
ax2.legend(loc='upper right')

# Let's add a title and some labels, just for fun
ax2.set_xlabel("x axis label")
ax2.set_ylabel("y axis label")
ax2.set_title("This is a title")

# now we show it
fig2.show()
input("Press any key to continue")

#------------------------------------------------
# Next: two histograms side by side in a 2x2 grid
#------------------------------------------------

# ax3 is now a 2D array of axes
fig3, ax3 = plt.subplots(2,2)

# Put one histogram on the bottom right of the 2x2 grid
# and one histogram on the top left
# We will not bother with making things look pretty
topLeft  = ax3[0][0]
botRight = ax3[1][1]
ctl, btl, _ = topLeft.hist(y, bins, histtype='step', log=False, color='red') 
cbr, bbr, _ = botRight.hist(x, bins, histtype='step', log=False, color='blue')

# You would guess that if one of the axes is not used, its spot on
# the grid should be left blank.  You would be wrong (sigh).
# So "turn off" the bottom left and the top right 
ax3[1][0].axis("off")
ax3[0][1].axis("off")

# now we show iy
fig3.show()
input("Press any key to continue")

#------------------------------------------------------------
# Next: two "stacked" histograms.
# Useful when the data to be plotted has two
# components and you want to see the relative contributions
#-----------------------------------------------------------

# 1x1 grid
fig4, ax4 = plt.subplots()

# lists with the data, colors, and labels of the two hist 
blah   = [x, y]
colors = ['blue', 'red']
names  = ['xxx', 'yyy']

# the returned cc is now a list with contents of 1st and contents of 2nd
cc, bb, _ = ax4.hist(blah, binEdges, histtype='stepfilled', log=False,
                     color=colors, stacked='True', label = names, alpha=0.8)

ax4.set_xlim(binEdges[0], binEdges[-1])
ax4.tick_params("both", direction='in', length=10, right=True)
ax4.set_xticks(binEdges, minor=True)
ax4.tick_params("both", direction='in', length=7, right=True, which='minor')
ax4.set_ylim(0. , 1.1*max( np.array(cc[0]) + np.array(cc[1]) ) )
ax4.legend(loc='upper right')
fig4.show()
input("Press any key to continue")

#----------------------------------------
# Next: a scatter plot X vs Y
#----------------------------------------

# 1x1 grid
fig5, ax5 = plt.subplots()

# 'ro' means red circles
ax5.plot(x, y, 'ro', markersize=3, alpha=0.9)

# same stuff as before
ax5.set_xlim(binEdges[0], binEdges[-1])
ax5.tick_params("both", direction='in', length=10, right=True)
ax5.set_xticks(binEdges, minor=True)
ax5.tick_params("both", direction='in', length=7, right=True, which='minor')

fig5.show()
input("Press any key to continue")

#------------------------------------------------------
# Now we are going to put x and y into a 2d histogram
#
# Then we put it into a "temperature plot"
# For the color map, here are some choices
# https://matplotlib.org/examples/color/colormaps_reference.html
#------------------------------------------------------
xbins = np.linspace(0., 1., 21)  # 20 bins btw 0 and 1
ybins = np.linspace(0., 1., 11)  # 10 bins btw 0 and 1

# The color map..pick whatever you like
# More choices here
# https://matplotlib.org/examples/color/colormaps_reference.html
thisMap = "jet"
#thisMap = "brg"
#thisMap = "terrain"
#thisMap = "gnuplot"
#thisMap="ocean"
#thisMap ="brg"

fig6, ax6 = plt.subplots()
h, xedges, yedges, image = ax6.hist2d(x, y, bins=[xbins, ybins], cmap=thisMap, cmin=0.5)
fig6.colorbar(image)   # add a legend for the colors

fig6.show()
input("Press any key to continue")

#-----------------------------------------------------------
# Could have done the same through "imshow" instead
#-----------------------------------------------------------
fig7, ax7 = plt.subplots()
hh, xedges, yedges = np.histogram2d(x, y, bins=[xbins, ybins])

# Stupid thing: when putting it on the screen
# the 1st index is the column and the 2nd index is the
# row.  So in order to really have [ix, iy] we need to
# transpose before plotting.
hh = hh.transpose()

image2 = ax7.imshow(hh, cmap=thisMap, origin='lower', aspect='auto')
fig7.colorbar(image2)

fig7.show()
input("Press any key to continue")

