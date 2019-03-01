#!/usr/bin/env python3
#
# Use the "odeint" finction to solve
# the 2nd order differential equation
# for a damped harmonic oscilator with
# an arbitrary driving force F(t)
#
# To remind you fo lower division physics:
#    ma = -k*x -beta*v + F(t) 
# which leads to
#    x'' = -w2*x -b*x' + f(t)
#
# Define y=x'
# This results in two coupled 1st oder diff equations for x and y
# (1)  x' = y
# (2)  y' = -w2*x -b*y + f(t)
#
# We define a list z = [x, y]
# and use odeint to solve simultaneously
#
#  CC 26-Feb-2019
#---------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import math

# the "driving" force (technically: F/m)
def f(t):
    return 0
#    return 1-2*((np.trunc(t))%2)   # a step function

# returns, as a list, the derivative of z wrt time
def dz_dt(z, t, b, w2):
    return [z[1], f(t)-b*z[1]-w2*z[0]]

# angular frequency squared of undamped oscillator
w2 = 4.

# damping term
b = 0.1

# initial condition (amplitude and velocity)
z0 = [0., 1.]

# undamped oscillator period
period = 2 * math.pi / math.sqrt(w2)

# time range for the calculation, number of time points
tmin = 0.
tmax = 20*period
n    = 30000
t    = np.linspace(tmin,tmax,n)

# solve the equation
zout = odeint(dz_dt, z0, t, args=(b, w2))
x    = zout[:,0]   # x as a function of t

# plot it
fig, ax = plt.subplots()
ax.plot(t, x)
ax.set_xlabel("time")
ax.set_ylabel('amplitude')
fig.show()
input('CR to quit :')
