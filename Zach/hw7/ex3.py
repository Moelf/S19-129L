#!/usr/bin/env python3

import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import chisquare
import ccHistStuff as cc

data=10**4*np.loadtxt("straightTracks.txt")

#Positions in micrometers
x1 = 2*10**4 
x2 = 3*10**4
x3 = 5*10**4
x4 = 7*10**4
difference  = []
pull_values = []
chi_squ     = []
def func(x,a1,a2,b):
	l = len(x)
	val = np.hstack([ a2*(x[:l] - b), a1*(x[l:2*l] - b) ])
	return val

for i in range(len(data)):
	x0  = data[i][0]
	y0  = data[i][1]
	y00 = data[i][2]
	y01 = data[i][3]
	y02 = data[i][4]
	y03 = data[i][5]
	y10 = data[i][6]
	y11 = data[i][7]
	y12 = data[i][8]
	y13 = data[i][9]

	x_data  = np.array([x1, x2, x3, x4])
	y0_data = np.array([y00, y01, y02, y03])
	y1_data = np.array([y10, y11, y12, y13])

	x_data_stack  = np.hstack([x_data,x_data])
	y_data_stack  = np.hstack([y0_data,y1_data])

	popt, pcov = curve_fit(func,x_data_stack,y_data_stack, p0=[.5,-.5,x0 ],method='trf')
	intercept  = popt[2]
	diff       = intercept - x0
	difference.append(diff)

	pull = diff/np.sqrt(np.diag(pcov)[2])
	pull_values.append(pull)

	#Chi-Squared Calculation (if desired)
	y0_theory = popt[0]*(x_data - intercept)
	y1_theory = popt[1]*(x_data - intercept)
	y_theory  = np.concatenate((y0_theory,y1_theory))
	y_data    = np.concatenate((y0_data,y1_data))
	chi       = chisquare(y_data, y_theory)[0]
	chi_squ.append(chi)
	
#Plotting
fig, ax = plt.subplots()

binEdges = np.linspace(-500,500,100)

ax.hist(difference, bins=binEdges, label='Difference', edgecolor='black')
cc.statBox(ax, difference, binEdges, label='Constrained Fit')
plt.legend(loc='center right')
plt.xlabel('Intercept Difference [micrometers]')
plt.ylabel('Number of Occurences')
fig.show()
input('Press <Enter> to continue')

fig, ax = plt.subplots()
binEdges = np.linspace(-.02,.02,100)
ax.hist(pull_values, bins=binEdges, label='Pull', edgecolor='black',log=True)
cc.statBox(ax, pull_values, binEdges, label='Pull')
plt.legend(loc='center right')
plt.xlabel('Pull')
plt.ylabel('Number of Occurences')
fig.show()
input('Press <Enter> to continue')

### Uncomment if you want to see plot of chi-squared values ###
"""
fig, ax = plt.subplots()
binEdges = np.linspace(0,.25*10**8,100)
ax.hist(chi_squ, bins=binEdges, label='Chi Squared', edgecolor='black')
cc.statBox(ax,chi_squ,binEdges,label='Chi Squared')
plt.xlabel('Chi Squared Value')
plt.ylabel('Number of Occurences')
fig.show()
input('Press <Enter> to continue')
"""


