#!/usr/bin/env python3
#
# Test of a simple linear fit using
# scipy.optimize.curve_fit
#
# 

# CC 19 Feb 2019
#-----------------------
from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

# curve_fit needs to define a function explicitely
def myFunc(x, slope, offset):
    return slope*x+offset


x = np.array([1., 2., 3.])
y = np.array([1.1, 1.9, 3.1])     
dy = np.array([0.1, 0.07, 0.12])  # error in y

# The calling sequence to curve_fit requires an initial
# guess for the parameters
myGuess = [0., 1.]
p, cov = curve_fit(myFunc, x, y, p0=myGuess, sigma=dy, absolute_sigma=True)
print("Fit parameters = \n",p)
print("Covariance Matrix = \n", cov)

# Annoyingly enough you need to calculate the chisquared yourself
temp = (y - myFunc(x,p[0],p[1]))/dy
chisq = (temp*temp).sum()
print("Chisq = ", chisq)

# Chisquared contour plot
# Make the plot to +\- 4 sigma on either side of the fit values
#
# First step:
# Fill (brute force) a 2D array as a function of (p[0],p[1])
# which contains the difference between this particular value
# of chisq calculated with (p[0],p[1]) and the minimized value of chisq 
horizMin = p[0] - 4*np.sqrt(cov[0][0])
horizMax = p[0] + 4*np.sqrt(cov[0][0])
vertMin  = p[1] - 4*np.sqrt(cov[1][1])
vertMax  = p[1] + 4*np.sqrt(cov[1][1])
horiz    = np.linspace(horizMin, horizMax, 100)
vert     = np.linspace(vertMin,  vertMax,  100)
dchi     = np.zeros(shape=(100,100))
for i in range(0, len(horiz)):
    p0 = horiz[i]
    for j in range(0, len(vert)):
        p1 = vert[j]
        temp = (y - myFunc(x,p0,p1))/dy
        thisChi = (temp*temp).sum()
        dchi[i][j] = thisChi - chisq

# Second step:
# Define a contour.  The hardwired numbers correspond
# to the 68% 95% 99% coverage for 2 parameters
# Particle Data Group (PDG) Table 38.2
# http://pdg.lbl.gov/2015/reviews/rpp2015-rev-statistics.pdf
fig2, ax2 = plt.subplots()
CS = ax2.contour(horiz, vert, dchi, [2.30, 5.99, 9.21])
fmt = {}
strs = [ '68%', '95%', '99%' ]
for l,s in zip( CS.levels, strs ):
    fmt[l] = s
ax2.clabel(CS, inline=True, fmt=fmt, fontsize=9)

# Third step:
# Stick a point at the best fit value, show the grid, cleanup axes
ax2.plot(p[0], p[1], 'ko')
ax2.set_xlim(horiz[0], horiz[-1])
ax2.set_ylim(vert[0],  vert[-1]) 
ax2.set_xlabel('slope')
ax2.set_ylabel('offset')
fig2.show()
input('Enter something to quit ')



