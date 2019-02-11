import numpy as np


# function we're interested to integrate
def f(x, y): return (x+2*y)*(x+y)


# observe the maximum in the range of integrtaion
scale = 45
# set limits of integral
x_i = 0
x_f = 1
y_i = 2
y_f = 4
area = (x_f - x_i) * (y_f - y_i)

# number of MC trials
N = 100*1000

x = np.random.uniform(x_i, x_f, N)
y = np.random.uniform(y_i, y_f, N)
z = np.random.uniform(0, scale, N)


# integral = Volume * Number of points in / Total points
integral = np.sum(z < f(x, y)) / N * area * scale


print("Using %d MC points, we find the integral is: %f" % (N, integral))
