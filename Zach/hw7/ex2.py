#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import ccHistStuff as cc

# read the data set
data = np.load("dataSet.npy")

p_0 = 1
p_1 = 2

def f(x,p_0,p_1):
	return p_0*np.exp(-p_1*x)
def chi_sq(x,p_0,p_1,N):
	return (N-f(x,p_0,p_1) )**2/N

chi_squared=np.array([])
for i in range(1,26):
	bin_lower = .5*(i-1)
	bin_upper = .5*i
	N = len(data[(data>=bin_lower) & (data<bin_upper)]) #Number of entries in bin
	x = np.mean([bin_lower, bin_upper]) #Center of bin
	chi = chi_sq(x,p_0,p_1,N)
	chi_squared = np.append(chi_squared, chi)

print(np.sum(chi_squared))

"""

# Plotting stuff (default: one subplot in x and one in y)
thisFigure, thisAxes = plt.subplots()

# the bin edges (nbins + 1 because of lower and upper edge)
nbins = 40
bins  = np.linspace(0, 20, nbins+1)

# the histogram
fig, ax = plt.subplots()
contents, binEdges, _ = ax.hist(data, bins, histtype='step', log=True, color='black')

# We were asked to add labels and stat box
ax.set_xlabel('X')
ax.set_ylabel('Entries per 0.5')
cc.statBox(ax, data, binEdges)

# This is purely esthetics (personal preference)
ax.tick_params("both", direction='in', length=10, right=True)
ax.set_xticks(binEdges, minor=True)
ax.tick_params("both", direction='in', length=7, right=True, which='minor')
ax.set_xlim(0, 20)

plt.plot(data, f(data,p_0,p_1) )


fig.show()
input('Press <Enter> to continue')
"""
