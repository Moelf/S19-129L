#!/usr/bin/env python3
#
# This is a test an example of the use of
# minuit for a binned extended maximum
# likelihood fit
#
# To understand what is going on here
# should look at the lecture slides
# http://hep.ucsb.edu/people/claudio/ph129-w19/ExtendedNLLExample.pdf
#
# One thing that is done differently here
# wrt the description in the slides is
# that I included a switch to turn on/off
# the treatment of background shape systematics
# This is the "shapeSyst" boolean defined at the begiining of the code/
#
# This code needs to read the data from
# HistForMinuitFit.npz
#
# CC 28 February 2019
#--------------------------------------

# iminuit tutorial at
# https://nbviewer.jupyter.org/github/iminuit/iminuit/blob/master/tutorial/basic_tutorial.ipynb
import numpy as np
import matplotlib.pyplot as plt
from iminuit import Minuit

# Flag to include/exclude the systematics 
# on the background shape
shapeSyst = True

# Read the arrays that were prepared for us separately
# b_pdf    = the default background hist pdf 
# b1_pdf   = 1st alternative to hist b_pdf
# b2_pdf   = 2nd alternative to hist b_pdf
# s_pdf    = the hist pdf for signal
# binCen   = the center of the hist bins
# binEdges = the edges of the bins
# The arrays were saved with this command:
# np.savez("histForMinuitFit.npz", b_pdf, b1_pdf, b2_pdf, s_pdf, d, binCen, binEdges,
#           b_pdf=b_pdf, b1_pdf=b1_pdf, b2_pdf=b2_pdf, s_pdf=s_pdf, d=d,
#          binCen=binCen, binEdges=binEdges)
npzfile  = np.load("histForMinuitFit.npz")
b_pdf    = npzfile['b_pdf']
b1_pdf   = npzfile['b1_pdf']
b2_pdf   = npzfile['b2_pdf']
s_pdf    = npzfile['s_pdf']
d        = npzfile['d']
binCen   = npzfile['binCen']
binEdges = npzfile['binEdges']

# All pdfs should already be normalized to 1.
# But just in case, normalize them again
b_pdf  = b_pdf  / b_pdf.sum()
b1_pdf = b1_pdf / b1_pdf.sum()
b2_pdf = b2_pdf / b2_pdf.sum()
s_pdf  = s_pdf  / s_pdf.sum()

# Just for fun, plot the pdfs
f1, a1 = plt.subplots()
a1.hist(binCen,binEdges,weights=b_pdf, histtype='step', log=True, color='blue')
a1.hist(binCen,binEdges,weights=b1_pdf, histtype='step', linestyle='dashed', log=True, color='red')
a1.hist(binCen,binEdges,weights=b2_pdf, histtype='step', linestyle='dashed', log=True, color='green')
a1.set_xlim(binEdges[0], binEdges[-1])
f2,a2 = plt.subplots()
a1.set_title("Background PDF")
a2.hist(binCen,binEdges,weights=s_pdf, histtype='step', log=True, color='red')
a2.set_xlim(binEdges[0], binEdges[-1])
a2.set_title("Signal PDF")
a1.set_xlabel("Boosted Decision Tree Score")
a1.set_ylabel("Fraction of events")
a2.set_xlabel("Boosted Decision Tree Score")
a2.set_ylabel("Fraction of events")
f1.show()
f2.show()

# Just for fun, plot the data as well
f4,a4 = plt.subplots()
c4, b4, _ = a4.hist(binCen, binEdges, weights=d, log=True, color='black', histtype='step')
a4.set_xlim(b4[0], b4[-1])
a4.set_xlabel("Boosted Decision Tree Score")
a4.set_ylabel("Number of events")
a4.set_title("(Pseudo) Data")
f4.show()

# Now comes the negative log likelihood function
#
# d, s_pdf, b_bdf, b1_pdf, b2_pdf are np.arrays 
# d      = contents of data histogram 
# s_pdf  = contents of signal pdf histogram 
# b_pdf  = contents of default background pdf histogram
# b1_pdf = contents of alternative 1 to b_pdf
# b2_pdf = contents of alternative 2 too b_pdf
# S      = number of signal events
# B      = number of background events
# alpha  = parameter to interpolate between pdfs
# Assume that pdf's are normalized, eg s_pdf.sum()=1
def NLL(S,B,alpha):
    # alpha=0  ---> use b_pdf
    # alpha=1  ---> use b1_pdf
    # alpha=-1 ---> use b2_pdf
    # (and smoothly interpolates vs. alpha)
    if alpha>0:
        new_b_pdf = b_pdf + alpha*(b1_pdf-b_pdf)
    else:
        new_b_pdf = b_pdf - alpha*(b2_pdf-b_pdf)    
    # should be already normalized, but make sure
    new_b_pdf = new_b_pdf / new_b_pdf.sum()  
    temp = d * np.log(S*s_pdf + B*new_b_pdf)
    return S + B - temp.sum() + alpha*alpha/2.

# Setup the fitter.  S, B, alpha are the initial guesses
# print_level=0 --> suppress print of intermediate information 
# errordef = 0.5   because for NLL 1 sigma errors are  from
#                  NLL-NLL(at minimum) = 0.5
# error_S, error_B, alpha: are initial steps to look for minimum
# We fix alpha=0 if shapeSyst=False
m = Minuit(NLL, S=10., B=500., alpha=0., print_level=1,
           errordef=0.5, error_S=1.0, error_B=1.0, error_alpha=0.1,
           fix_alpha=(not shapeSyst))

# Run the fitter
m.migrad()
m.minos()
m.print_param()

# Profile scan of the fitted function (NLL).
# At each FIXED value of S, fit again for B,
# extract the NLL at the minimum, subtract 
# the NLL at the GLOBAL minimum, and plot it
xxx, yyy, _ = m.mnprofile('S', subtract_min=True, bins=100, bound=(0,60))

# m.mnprofile does all the work... 
# Now we just plot the results
# deltaNLL = 0.5 (2, 4.5 ) corresponds to 1 (2, 3) sigma
fig3, ax3 = plt.subplots()
ax3.plot(xxx,yyy,linestyle='solid', color='b')
ax3.set_xlim(min(xxx), max(xxx))
ax3.set_ylim(0.)
ax3.set_xlabel('S')
ax3.set_ylabel('deltaNLL')
ax3.plot([min(xxx), max(xxx)], [0.5, 0.5], linestyle='dashed', color='red')
ax3.plot([min(xxx), max(xxx)], [2.0, 2.0], linestyle='dashed', color='red')
ax3.plot([min(xxx), max(xxx)], [4.5, 4.5], linestyle='dashed', color='red')
fig3.show()

# Show the data...first get fit parameters
fittedB = m.values['B']
fittedS = m.values['S']
fitteda = m.values['alpha']
if fitteda>0:
    bf_pdf = b_pdf + fitteda*(b1_pdf-b_pdf)
else:
    bf_pdf = b_pdf - fitteda*(b2_pdf-b_pdf)
bf_pdf = bf_pdf / bf_pdf.sum()
    
# Then plot stacked histograms of S and B
# lists with the data, colors, and labels of the two hist 
blah   = [binCen, binCen]
colors = ['blue', 'red']
names  = ['Background', 'Signal']
w2     = [fittedB*bf_pdf, fittedS*s_pdf]

fig42, ax42 = plt.subplots()
ax42.hist(blah, binEdges, histtype='stepfilled', log=True,
          color=colors, stacked='True', label=names, weights=w2, alpha=0.4)
ax42.errorbar(binCen, d, yerr=np.sqrt(d), linestyle='none', marker='o', 
              color='black', markersize=4)
ax42.set_ylim(0.1)
ax42.set_xlim(binEdges[0], binEdges[-1])
ax42.legend()
ax42.set_ylabel("Number of events")
fig42.show()
input('Enter something to quit')
