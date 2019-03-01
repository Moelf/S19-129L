#!/usr/bin/env python3
#
# Solution of Homework 5 Exercise 6 using a prepackaged
# code to solve differential equations
#
# CC 26 Feb 2019
#-----------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#--------------------------------
# This is the vin(t) function
# Note: I would like to take int(t)
# but this does not work so well
# for np arrays (try it!)
# trunc does essentially the same thing
# but it returns a float, which is OK
#-------------------------------
def vin(t):
    return 1-2*((np.trunc(t))%2)

#---------------------------------
# This is dvout/dt
#--------------------------------
def dvout_dt(vout, t, tau):
    return (1./tau)*(vin(t)-vout)

# Get input from keyboard
while True:
    try:
        tau = float(input("Please enter tau in microseconds "))
        break                # get out of the while loop
    except ValueError:
        print("You did not enter a valid float, try again")

# minimum and maximum for the calculation
tmin =  0.
tmax = 100.

# Seems sensible that the time steps
# be smaller than tau.
# step = tau/50 seems reasonable
# Then again, CPU is cheap, so we can
# probably easily afford 10K steps.
step  = tau/50.
nstep = int( (tmax-tmin)/step )
if nstep < 100000:
    nstep = 100000
step = (tmax-tmin)/nstep
print("We will use nstep = ", nstep)

# t is the time
t = np.linspace(tmin, tmax, nstep)

# vout at time t=0
# We assume that the vin square wave is
# turned on at time t=0
vout0 = 0  

# The odeint function solves the differential equation
# The 1st parameter is the name of the function that
# calculates the derivative.
# The 2nd parameter is the initial condition
# The 3rd argument is the time array
# "args" is a tuple that contains constants that need
# to be passed on the function.  Careful: a tuple
# with only one entry needs to have a comma after
# the entry to avoid confusion with just an ordinary
# variable in (useless) parenthesis
vout = odeint(dvout_dt, vout0, t, args=( tau, ))

# odeint documentation says that vout is
#   "vout:  array, shape (len(t), len(yvout))
#    Array containing the value of vout for
#    each desired time in t, with the initial
#    value y0 in the first row"
# So we need to "collapse" the array to 1D
vout = np.array(vout).flatten()

# and now plot the results
fig, ax = plt.subplots(2,1)
ax[0].plot(t, vout)
ax[0].plot(t, vin(t) )
ax[0].set_xlim(0, 10)
ax[0].grid(True, which='both')

ax[1].plot(t, vout)
ax[1].plot(t, vin(t) )
ax[1].set_xlim(90, 100)
ax[1].grid(True, which='both')

fig.show()
input("Carriage return to continue....")


