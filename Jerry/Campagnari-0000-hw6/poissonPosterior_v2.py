#!/usr/bin/env python3
#
# Modification of poissonPosterior,py
# from a previous homework set.
# This now also calculate sbayesian 95% CL.
# Extend the plot way into the tail
# Start plotting at zero
# Binsize is 0.05
# Also add a cumulative plot (just for fun)
# CC   11 Feb 2019  
#--------------------------------
import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import ccHistStuff as cc

# The function that multiplies the Gaussian
def ff(x,y,N):
    return np.exp(-x-y) * (x+y)**N

# keyboard input
while True:
    try:
        N = int( input("Number of observed events N = ") )
        break
    except ValueError:
        print("Invalid input")

while True:
    try:
        mu = float( input("Mean expected background mu = ") )
        break
    except ValueError:
        print("Invalid input")

while True:
    try:
        sigma = float( input("Uncertainty (gaussian) on mu = ") )
        break
    except ValueError:
        print("Invalid input")

# other parameters
level   = 0.95
x1      = 0
x2      = 20.
npoints = 400            # number of points in x to plot/calculate
ntoy    = 1000           # for MC integration of y
dx      = (x2-x1)/100
xar     = np.linspace(x1, x2, npoints+1) # the points in x to plot

# init random number
np.random.seed(1234567)

# an array for f(x) initialized to zero
far = np.zeros(npoints+1)
i = 0
for x in xar:
    y      = np.random.normal(mu, sigma, ntoy)  # pick y
    y      = y[ y> 0 ]      # require y>0
    thisN  = len(y)         # how many "usable" y's do we really have?       
    ftoy   = ff(x, y, N)    
    far[i] = (1./thisN) * ftoy.sum()
    i      = i + 1

# now the plot
fig, ax = plt.subplots()
ax.plot(xar, far)
ax.set_xlim(x1,x2)
ax.set_ylim(0)
ax.grid(True, which='both')
fig.show()
input("blah to continue")

# This is the integral from 0 to 20 which for all
# intents and purposes is like 0 to infinity
total = far.sum()
cumul = (1./total) * far.cumsum()   # this is the "cumulatuve" normalized to 1
fig2, ax2 = plt.subplots()
ax2.plot(xar, cumul)
ax2.set_xlim(x1,x2)
ax2.set_ylim(0)
ax2.grid(True, which='both')
fig2.show()
input("blah to continue")

# the indeces where the cumulative is > level
indeces = np.nonzero(cumul>level)
# the zeroth element of indeces ought to be the first bin
# where the cumulative is > level (assuming that indeces
# is actually ordered).  But to be sure, take the minimum
i95 = np.min(indeces)

# The 95% Cl limit is in between xar[i95-1] and xar[i95]
# Let's interpolate....
dx    = xar[i95]   - xar[i95-1]
dcum  = cumul[i95] - cumul[i95-1]
lim   = xar[i95-1]  + dx*(0.95-cumul[i95-1])/dcum
print('95%% Bayesean CL is %5.2f' %lim)


