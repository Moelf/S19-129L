#!/usr/bin/env python3

#Calculating chi-squared and iterative algoorithm using Campagnari's outline in notes



import numpy as np
import matplotlib.pyplot as plt
import ccHistStuff as cc
from scipy.optimize import curve_fit
import math

# read the data set
data = np.load("dataSet.npy")

# Define relevant functions
def f(x,p_0,p_1):
	return p_0*np.exp(-p_1*x)
def chi_sq(x,p_0,p_1,N):
	return (N-f(x,p_0,p_1) )**2/N
def dfdp_0(x,p_1):
	return np.exp(-p_1*x)
def dfdp_1(x,p_0,p_1):
	return -x*p_0*np.exp(-p_1*x)
# Initialize arrays and settings
np.seterr(all='ignore')
sigma = 2.28
W = (1/sigma**2)*np.identity(25)
A_col = np.zeros((25,1))

# Parameter guesses
p_0 = 10000
p_1 = 1

alpha = np.array([[p_0],[p_1]])
np.random.seed(12345)
chi_square_calculated = np.random.uniform(1,1000,10)
while np.std(chi_square_calculated[-5:])>5: #Keep iterating until chi_squared values stop changing significantly
		y_values = np.array([])
		x_values = np.array([])
		chi_squared = np.array([])		
		for i in range(1,26):
			bin_lower = .5*(i-1)
			bin_upper = .5*i
			N = len(data[(data>=bin_lower) & (data<bin_upper)]) #Number of entries in bin
			x = np.mean([bin_lower, bin_upper]) #Center of bin
			chi = chi_sq(x,p_0,p_1,N)
			chi_squared = np.append(chi_squared, chi)
			A_col[i-1] = x
			y_values = np.append(y_values, N)
			x_values = np.append(x_values, x)

		chi_square = np.sum(chi_squared) #Chi-squared for these parameters

		#Various matrices for determining next iteration of parameters
		a = np.apply_along_axis(dfdp_0,0,A_col,p_1)
		b = np.apply_along_axis(dfdp_1,0,A_col,p_0,p_1)
		A = np.hstack((a,b)) 
		#print(A)

		C = np.matmul(np.matmul(np.linalg.inv(np.matmul( np.matmul(A.T,W), A) ), A.T), W)
		#print(C)

		y_delta = y_values[np.newaxis].T - f(x_values,p_0,p_1)[np.newaxis].T
		#print(y_delta)
		

		alpha = alpha + np.matmul(C, y_delta)
		p_0 = alpha[0]
		p_1 = alpha[1]

	
		chi_square_calculated = np.append(chi_square_calculated, chi_square)

print('The minimized Chi-Squared Value is %.4f' %chi_square)
print('The optimal parameters are P_0=%.4f and P_1=%.4f' %(p_0,p_1) )



# Plotting stuff (default: one subplot in x and one in y)
thisFigure, thisAxes = plt.subplots()

# the bin edges (nbins + 1 because of lower and upper edge)
nbins = 40
bins  = np.linspace(0, 20, nbins+1)

# the histogram
fig, ax = plt.subplots()
contents, binEdges, _ = ax.hist(data, bins, histtype='step', log=True, color='black',label='Raw Data')

# We were asked to add labels and stat box
ax.set_xlabel('X')
ax.set_ylabel('Entries per 0.5')
cc.statBox(ax, data, binEdges)

# This is purely esthetics (personal preference)
ax.tick_params("both", direction='in', length=10, right=True)
ax.set_xticks(binEdges, minor=True)
ax.tick_params("both", direction='in', length=7, right=True, which='minor')
ax.set_xlim(0, 20)

plt.plot(data, f(data,p_0,p_1),label='Chi-Squared Fit' )

plt.legend(loc='center left')
fig.show()
input('Press <Enter> to continue')
