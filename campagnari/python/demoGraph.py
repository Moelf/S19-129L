#!/usr/bin/env python3
#
# A demonstration of plotting lines and graphs
#
# CC 25 Jan 2019
#------------------------
import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Initaliize the random number generator
# in a repeatable way by specifying the seed
seed = 12345
np.random.seed(seed)

# some arbitrary data set including error
x  = np.array([1., 4.,  5.,   2.,  9.])
y  = np.array([7., 12., 10.4, 8.6, 9.])
dy = 0.2*y                  # 20% uncertainty
dx = np.full( len(y), 0.3)  # all 0.3

# plot the data set with errors, no line joining
fig1, ax1 = plt.subplots()
ax1.errorbar(x, y, xerr=dx, yerr=dy, linestyle='none',
                 color='red', marker='o', markersize=4.)
xmin = x.min()-2
xmax = x.max()+2
ymin = 0.
ymax = y.max()+5
ax1.set_xlim(xmin, xmax)
ax1.set_ylim(ymin, ymax)

# lets add some functions
xf = np.linspace(xmin, xmax, 1000)
yf = xf + 0.1*xf*xf                      # a linear function
yg = 80*stats.norm.pdf(xf, 5., 3.)       # gaussian mean=6 sigma=2
ax1.plot(xf, yf, color='orange', linestyle='solid')
ax1.plot(xf, yg, color='black',  linestyle='dashed')


fig1.show()
input("Press any key to continue")
