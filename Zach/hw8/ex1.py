#!/usr/bin/env python3

import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import special
import ccHistStuff as cc
from iminuit import Minuit
from scipy.stats import norm
 
# Read the masses into an array 
data     = np.loadtxt("mass.txt")
x_values = np.linspace(100,200,500)

m1 = 100.0
m2 = 200.0


mu_S    = 5.0
sigma_S = 155.0
alpha   = 5
def S_pdf(x):
    return norm.pdf(x,mu_S,sigma_S)

def B_pdf(x,alpha): #Test an exponential?
    return alpha * np.exp(-alpha*x) / (np.exp(-alpha * m1) - np.exp(-alpha * m2) )

#s_pdf = S_pdf(x_values)
#b_pdf = B_pdf(x_values)
# Negative log likelihood

def NLL(S,B,alpha):
    temp = np.log(S*S_pdf(x_values) + B*B_pdf(x_values, alpha) )
    #temp = np.log(S*s_pdf + B*b_pdf)
    return S + B - temp.sum()


m = Minuit(NLL, S=10., B=500.,alpha=.5, print_level=0, errordef=0.5, error_S=1.0, error_B=1.0)

fmin, param = m.migrad()
print(param)
print(fmin)


#xxx, yyy, _ = m.mnprofile('S', subtract_min=True )

#print(xxx)
#print(yyy)


"""
x1 = 100.
x2 = 200.
nb = 20
bins = np.linspace(x1, x2, nb+1)

# plot now
f, a = plt.subplots()
c, b, _ = a.hist(mass, bins, histtype='step')
cc.statBox(a, mass, b)
a.set_xlim(b[0], b[-1])
a.tick_params("both", direction='in', length=10, right=True)
a.set_xticks(b, minor=True)
a.tick_params("both", direction='in', length=7, right=True, which='minor')
f.show()

input("Press <Enter> to continue")
"""


