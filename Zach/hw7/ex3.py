#!/usr/bin/env python3

import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import ccHistStuff as cc

data=np.loadtxt("straightTracks.txt")

#Positions in cm
x1 = 2 
x2 = 3
x3 = 5
x4 = 7
difference  = []
pull_values = []

def func(x,a,b):
	return a*x+b

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

	x_data  = [x0,x1, x2, x3, x4]
	y0_data = [y0, y00, y01, y02, y03]
	y1_data = [y0, y10, y11, y12, y13]

	x_data  = np.hstack([x_data,x_data])
	y_data  = np.hstack([y0_data,y1_data])

	popt, pcov = curve_fit(func,x_data,y_data)
	intercept  = popt[1]
	diff       = intercept - x0
	difference.append(diff)

	pull = diff/np.diag(pcov)[1]
	pull_values.append(pull)
	
#Plotting
fig, ax = plt.subplots()

binEdges = np.linspace(-.05,.05,100)

ax.hist(difference, bins=binEdges, label='Difference', edgecolor='black')
cc.statBox(ax, difference, binEdges, label='Constrained Fit')
plt.legend(loc='center right')
plt.xlabel('Intercept Difference [cm]')
plt.ylabel('Number of Occurences')
fig.show()
input('Press <Enter> to continue')

fig, ax = plt.subplots()
binEdges = np.linspace(-.05,.05,100)
ax.hist(pull_values, bins=binEdges, label='Pull', edgecolor='black')
cc.statBox(ax, pull_values, binEdges, label='Pull')
plt.legend(loc='center right')
plt.xlabel('Pull')
plt.ylabel('Number of Occurences')
fig.show()
input('Press <Enter> to continue')

