#!/usr/bin/env python3

import numpy as np
import ccHistStuff as cc
import matplotlib.pyplot as plt


x=np.loadtxt("mass.txt")

fig, ax = plt.subplots()

binEdges=np.linspace(100, 200, 50)

ax.hist(x,bins=binEdges, log=False,edgecolor='black')

cc.statBox(ax, x, binEdges)

plt.xlabel("Value")
plt.ylabel("Occurences")
plt.title("Masses of Electron Positron Pairs")

fig.show()
#print(x)

input("Press any key to continue")

