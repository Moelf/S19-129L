#!/usr/bin/env python3
#
# Compare a "massaged" lognormal
# with a gaussian distributions.
#
# This massaged lognormal looks
# very much like a Gaussian but it has
# the nice property that it goes to
# zero at x=0.  
#
# For the Gaussian we truncate
# the distribution at zero in the
# plot, but then we weight the
# histogram so the total number in
# the histogram is the same for both
# lognormal and gaussian picks for
# a nice comparison of shapes.
#
# Play around with mean and sigma
# to see what it all looks like (!)
#
# https://en.wikipedia.org/wiki/Log-normal_distribution
#
# CC 5 Feb 2019
#----------------------
import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.stats as stats
import ccHistStuff as cc


# various parameters
mean  = 2.0    # mean of the Gaussian
sigma = 0.5    # uncertainty on the Gaussian
N     = 10000  # how many to pick
xmin  = 0.     # minimum for plotting
xmax  = 10.    # maximum for plotting
nbins = 100    # how many bins

# Initialize the random seed
np.random.seed(123456)

# pick x1 from gaussian, x2 from lognormal
x1 = np.random.normal(mean, sigma, N)
x2 = np.random.lognormal(math.log(mean), math.log(1+sigma/mean) , N)

# Number of gaussian picks greater than 0
ngood   = (x1>=0).sum()
w       = np.full( N, N/ngood ) 

# Define 1x1 figure
fig, ax = plt.subplots(1,1)

# the histogram
b = np.linspace(xmin,xmax,nbins+1)
c1, b1, _ = ax.hist(x1, b, histtype='step', color='black',
                    label="Gaussian", weights=w )
c2, b2, _ = ax.hist(x2, b, histtype='step', color='red',
                    label="LogNormal")
ax.set_xlim(b[0], b[-1])
ax.tick_params("both", direction='in', length=10, right=True)
ax.legend(loc='best')
ax.grid(True, which='both')

# show the figure
fig.show()
# plt.show()  (this would pause automatically)
input("Press any key to continue")

