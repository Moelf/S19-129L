#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import ccHistStuff as cc

x=np.load("dataSet.npy")

fig, ax = plt.subplots()

binEdges=np.linspace(0, 25, 50)

ax.hist(x,bins=binEdges, log=True)

cc.statBox(ax, x, binEdges)

plt.xlabel("Value")
plt.ylabel("Occurences")


fig.show()
#print(x)

input("Press any key to continue")


