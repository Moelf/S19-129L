#!/usr/bin/env python3

import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import special
import ccHistStuff as cc
from iminuit import Minuit
from scipy.stats import norm
import warnings

warnings.filterwarnings("ignore")
# Read the initial data and parameters
data     = np.loadtxt("mass.txt")
x_values = np.linspace(100,200,500)

m1 = 100.0
m2 = 200.0


mu_S    = 155.0
sigma_S = 5.0

# Defining PDFs
def S_pdf(x):
    return norm.pdf(x,mu_S,sigma_S)
def B_pdf_0(x,alpha): #Test an exponential
    return alpha * np.exp(-alpha*x) / (np.exp(-alpha * m1) - np.exp(-alpha * m2) )
def B_pdf_1(x,m,b):   #Test linear
	intgrl = (1/2)*(m2-m1)*(2*b+m*(m1+m2))
	return (m*x + b)/intgrl
def B_pdf_2(x,a,c): #Test interesting trig
	intgrl = (1/3)*(-a*m1**3+a*m2**3-3*c*m1+3*c*m2)
	return (a*x**2 + c)/intgrl

# Negative log likelihood
def NLL_0(S,B,alpha):
    temp1 = S*S_pdf(data) + B*B_pdf_0(data, alpha)
    temp2 = np.log(temp1)
    return S + B - temp2.sum()

def NLL_1(S,B,m,b):
	temp1 = S*S_pdf(data) + B*B_pdf_1(data,m,b)
	temp2 = np.log(temp1)
	return S + B - temp2.sum()

def NLL_2(S,B,a,c):
	temp1 = S*S_pdf(data) + B*B_pdf_2(data,a,c)
	temp2 = np.log(temp1)
	return S + B - temp2.sum()


# Fitting
m_0 = Minuit(NLL_0, S=20., B=180.,alpha=.5, print_level=0, errordef=0.5, error_S=1.0, error_B=1.0,error_alpha=.1)
fmin_0, param_0 = m_0.migrad()

m_1 = Minuit(NLL_1, S=20., B=180., m=-.5, b=20, print_level=0, errordef=0.5, error_S=1.0, error_B=1.0,error_m=.1, error_b=1)
fmin_1, param_1 = m_1.migrad()

m_2 = Minuit(NLL_2, S=20., B=180., a=10, c=10, print_level=0, errordef=0.5, error_S=1.0, error_B=1.0,error_a=1,error_c=1)
fmin_2, param_2 = m_2.migrad()

# Extracting fitted data
S_0        = param_0[0]['value']
S_0_er     = param_0[0]['error']
B_0        = param_0[1]['value']
alpha      = param_0[2]['value']
y_values_0 = 5*(S_0*S_pdf(x_values) + B_0*B_pdf_0(x_values,alpha) )

S_1        = param_1[0]['value']
S_1_er     = param_1[0]['error']
B_1        = param_1[1]['value']
m_1        = param_1[2]['value']
b_1        = param_1[3]['value']
y_values_1 = 5*(S_1*S_pdf(x_values) + B_1*B_pdf_1(x_values,m_1,b_1) )

S_2        = param_2[0]['value']
S_2_er     = param_2[0]['error']
B_2        = param_2[1]['value']
a_2        = param_2[2]['value']
c_2        = param_2[3]['value']
y_values_2 = 5*(S_2*S_pdf(x_values) + B_2*B_pdf_2(x_values,a_2,c_2) )

# Plotting
nb = 20
bins = np.linspace(m1, m2, nb+1)
fig, ax = plt.subplots()
ax.plot(x_values,y_values_0)
ax.hist(data, bins, histtype='step')
plt.title('Exponential Background with S=%.1f $\pm$ %.1f' %(S_0,S_0_er) )
fig.show()
input("Press <Enter> to continue")

fig, ax = plt.subplots()
ax.plot(x_values,y_values_1)
ax.hist(data, bins, histtype='step')
plt.title('Linear Background with S=%.1f $\pm$ %.1f' %(S_1,S_1_er) )
fig.show()
input("Press <Enter> to continue")

fig, ax = plt.subplots()
ax.plot(x_values,y_values_2)
ax.hist(data, bins, histtype='step')
plt.title('Quadratic Background with S=%.1f $\pm$ %.1f' %(S_2,S_2_er) )
fig.show()
input("Press <Enter> to continue")
