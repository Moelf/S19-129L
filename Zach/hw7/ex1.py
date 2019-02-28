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
difference0  = []
difference1  = []
differenceav = []

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


	popt0, pcov0 = curve_fit(func,x_data,y0_data)
	intercept0 = popt0[1]

	popt1, pcov1 = curve_fit(func,x_data,y1_data)
	intercept1 = popt1[1]

	diff0  = intercept0 - x0
	diff1  = intercept1 - x0
	diffav = np.mean([intercept0,intercept1]) - x0	
	difference0.append(diff0)
	difference1.append(diff1)
	differenceav.append(diffav)

#Plotting
fig, ax = plt.subplots()

binEdges = np.linspace(-.05,.05,100)

ax.hist([difference0,difference1],bins=binEdges,label=['X1-X0', 'X2-X0'])
cc.statBox(ax, difference0, binEdges, x=.21, y=.98,label='Track 1')
cc.statBox(ax, difference1, binEdges, x=.98, y=.98,label='Track 2')
plt.legend(loc='center right')
plt.xlabel('Intercept Difference [cm]')
plt.ylabel('Number of Occurences')
fig.show()
input('Press <Enter> to continue')

fig, ax = plt.subplots()
binEdges = np.linspace(-.05,.05,100)
ax.hist(differenceav,bins=binEdges,label='Xav-X0',edgecolor='black')
cc.statBox(ax,differenceav,binEdges,label='Average of Tracks')
plt.legend(loc='center right')
plt.xlabel('Average Intercept Difference [cm]')
plt.ylabel('Number of Occurences')
fig.show()
input('Press <Enter> to continue')
