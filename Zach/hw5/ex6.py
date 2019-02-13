#!/usr/bin/env python3

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import squarewave

t=np.linspace(0,20,1000)

plt.plot(t,squarewave.square(t/2))
plt.show()

"""
x=np.linspace(0,20,1000)

duty=1/(2*np.pi)

plt.plot(x,signal.square(x,duty))
plt.show()
"""
