#!/usr/bin/env python3
#
# Various plots of Gaussians and
# error functions 
#
import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.stats as stats
import scipy.special as special
import ccHistStuff as cc



# plot gaussian of mean 0 and sigma 1
# xmin to xmax on both linear and log
xmin = -6
xmax =  6.
x = np.linspace(xmin, xmax, 1000)

f1, a1 = plt.subplots(2,1)
linScale = a1[0]
logScale = a1[1]
linScale.plot(x, stats.norm.pdf(x))
logScale.semilogy(x, stats.norm.pdf(x))

linScale.set_ylim(0)
linScale.set_xlim(xmin, xmax)
linScale.grid(True)
linScale.set_title("Gaussian on linear scale")

logScale.set_ylim(1e-9)
logScale.set_xlim(xmin, xmax)
logScale.grid(True, which='both')
logScale.set_title("Gaussian on log scale")

f1.show()
input("enter something to continue: ")

# error function erf is defined as
# integral(-x to x) of a Gaussian
f2, a2 = plt.subplots()
a2.plot(x, special.erf(x) )
a2.set_ylim(-1)
a2.set_xlim(xmin, xmax)
a2.set_title("special.erf(x)")
a2.grid(True, which='both')
f2.show()
input("enter something to continue: ")

# This is the integral from -inf to x of the gaussian
f3, a3 = plt.subplots()
a3.plot(x,  0.5*(1 + special.erf(x)) )
a3.set_ylim(0)
a3.set_xlim(xmin, xmax)
a3.set_title(" 0.5 * (1+special.erf(x) )")
a3.grid(True, which='both')
f3.show()
input("enter something to continue: ")

# This is the integral from x to infinity of the gaussian
# It is the one-sided p-value
f4, a4 = plt.subplots()
a4.semilogy(x,  1 - 0.5*(1 + special.erf(x)) )
a4.set_ylim(1e-10)
a4.set_xlim(xmin, xmax)
a4.set_title(" 1 - 0.5*(1+special.erf(x) )")
a4.grid(True, which='both')
f4.show()
input("enter something to continue: ")

# This is the integral from x to infinity of the gaussian
# It is the one-sided p-value
# Same as previous plot but zoomed in
f40, a40 = plt.subplots()
a40.semilogy(x,  1 - 0.5*(1 + special.erf(x)) )
a40.set_ylim(1e-10)
a40.set_xlim(0, 4)
a40.set_title(" 1 - 0.5*(1+special.erf(x) )")
a40.grid(True, which='both')

f40.show()
input("enter something to continue: ")

# This goes "the other way"
# Takes a one sided pvalue and returns the number of sigmas
f5, a5 = plt.subplots()
y = np.linspace(1e-3, 0.5, int(1e5))
a5.semilogx( y, stats.norm.ppf(1-y))
a5.set_xlim(y[0], y[-1])
a5.set_title("stat.norm.ppf(1-x)")
a5.grid(True, which='both')

f5.show()
input("enter something to continue: ")



