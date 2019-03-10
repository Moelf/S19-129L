#!/usr/bin/env python3
#
# Same basic problem as poissonPosterior_v2.py
# but calculate a frequentist limit instead.
#
# 
# CC 11 Feb 2019
#--------------------------------
import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import ccHistStuff as cc

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
ntoy        = 10000          # number of toys to throw
limitStart  = 11.            # highest value that we check
dl          = 0.1
level       = 0.95

# init random number
np.random.seed(1234567)

# throw a bunch of gaussian numbers...truncate to zero
b = np.random.normal(mu, sigma, ntoy)
b = b[ b>0 ]
while len(b) < ntoy:
    n       = ntoy-len(b)
    more_bs = np.random.normal(mu, sigma, n)
    more_bs = more_bs[ more_bs > 0 ]
    b       = np.concatenate( (b,more_bs) )

limit = limitStart+dl
nlow  = 0
while nlow < (1-level)*ntoy:
    limit = limit-dl
    result = np.random.poisson(limit+b)
    nlow   = (result<=N).sum()

if abs(limit-limitStart)<0.001:
    print('Error: increase starting point!!!')
else:
    print("95%% frequentist limit is %5.2f" % limit)


