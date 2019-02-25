import math
import numpy as np

"""
x cos(x) = 12, near x = 0.7

"""

# we want to solve this


def f(x): return x*np.cos(x) - 1/2


# starting point
x1, x2 = 0.6, 0.8

while np.abs(x1-x2) >= 0.000005:
    mid = (x2+x1) / 2.0
    if f(x1)*f(mid) < 0:
        x1, x2 = x1, mid
    elif f(x2)*f(mid) < 0:
        x1, x2 = mid, x2

ans = (x2+x1)/2

print("Solution for x*cos(x) - 0.5 = 0\
has a solution x = %.4f" % ans)
