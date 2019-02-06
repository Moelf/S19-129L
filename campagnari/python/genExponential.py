#!/usr/bin/env python3
#
# Generate and plot exponential numbers
# as exp(-t/tau)
# 
# CC 29 Jan 2019
#--------------------------
import argparse
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import ccHistStuff as cc

# Define the arguments 
parser =  argparse.ArgumentParser(description="Generate and plot an exponential", add_help=True)
parser.add_argument('-s', '--seed', help='Random seed. Default=10', required=False, type=int, default=10)
parser.add_argument('-n', '--nEvents', help='Number of events. Default=50000', required=False, type=int, default=50000)
parser.add_argument('-t', '--tau', help='Lifetime. Default=2.3', required=False, type=float, default=2.3)
parser.add_argument('-b', '--bins', help='Number of bins.  Default=30', required=False, type=int, default=30)
parser.add_argument('-m', '--maxHist', help='Max. of hist in units of tau.  Default=8', required=False, type=float, default=8)

# This is a dictionary containing the arguments
args = vars(parser.parse_args())

# Extract the arguments
seed   = args['seed']
N      = args['nEvents']
tau    = args['tau']
nbins  = args['bins']
tmax   = args['maxHist']*tau

# Initialize random number
np.random.seed(seed)

# the times (could have used np.random.exponential instead)
times = -tau * np.log(np.random.rand(N))

# Plotting stuff (default: one subplot in x and one in y)
fig, ax = plt.subplots(1,1)

# the bin edges (nbins + 1 because of lower and upper edge)
bins = np.linspace(0, tmax, nbins+1)

# the histogram
contents, binEdges, _ = ax.hist(times, bins, histtype='step', log=True, color='black')
cc.statBox(ax, times, binEdges)
ax.set_xlim(binEdges[0], binEdges[-1])
ax.tick_params("both", direction='in', length=10, right=True)

# show the figure
fig.show()
# plt.show()  (this would pause automatically)
input("Press any key to continue")
