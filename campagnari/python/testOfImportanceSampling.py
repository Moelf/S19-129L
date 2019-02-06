#!/usr/bin/env python3
#
# MC Integration of the function
# f(x) = sin(x)
# from 0 to pi/2 in two ways.
#
# First by picking x uniformly
# Then using importance sampling
# with pdf(x)=8x/pi^2
# CDF is 4x^2/pi^2 = R
# This gives x = (pi/2) * sqrt(R)
#
# First show the sin(x) and pdf(x) curves.
#
# Repeat the procedure n times and
# each time pick N random numbers
#
# CC 3-Feb2019
#-----------------------------------
import math
import numpy as np
import matplotlib.pyplot as plt

# how many times (n) and how many samples each time (N)
N = 30
n = 100

# We store the results in these lists
res1 = []   # without importance sampling
res2 = []   # with importance sampling

# initialize random seed
np.random.seed(1234579)

# Repeat n times
for i in range(n):

    # Without importance sampling
    x1   = 0.5 * math.pi * np.random.rand(N)
    fx1  = np.sin(x1)
    int1 = (0.5 * math.pi/N) * fx1.sum()
    res1.append(int1)

    # With importance sampling
    x2   = 0.5 * math.pi* np.sqrt(np.random.rand(N))
    fx2  = np.sin(x0) / (8 * x2 / (math.pi*math.pi) )
    int2 = (1./N) * fx2.sum()
    res2.append(int2)


# Show the functions
f,a = plt.subplots()
x = np.linspace(0., 0.5*math.pi, 100)
a.plot(x, np.sin(x),             color='green',  linestyle='solid',
           label='f(x) = sin(x)')
a.plot(x, 8*x/(math.pi*math.pi), color='orange', linestyle='solid',
           label='f(x) = 8x/pi^2')
a.legend(loc='best')
a.set_ylim(0., 1.5)
a.set_xlim(0., 0.5*math.pi  )
a.set_xlabel("x")
a.set_ylabel("f(x)")
f.show()
input("Enter anything to continue  ")

# Show the results  
fig, ax = plt.subplots()
ax.plot(np.linspace(1,len(res1), len(res1)), res1, marker='o',
            label="w/o importance sampling", color="blue", linestyle='none')
ax.plot(np.linspace(1,len(res2), len(res2)), res2, marker='x', 
            label="with importance sampling", color='red', linestyle='none')
ax.plot([1, len(res1)],  [1, 1], color='black')
ax.legend(loc='best')
ax.set_ylim(0.2, 2)
ax.set_xlabel("Sample number")
ax.set_ylabel("Estimate of integral")
fig.show()
input("Enter anything to continue and exit  ")
