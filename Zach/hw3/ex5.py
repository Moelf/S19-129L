#!/usr/bin/env python3

import numpy as np
import math
import matplotlib.pyplot as plt

np.random.seed(12345)

unif=np.random.rand(10000)
val=np.arange(0,1,.1)

def pdf(x):
	return ((1+4*x)/3)*1000
def cdf(x):
	return (3*(-1/3 + math.sqrt(1/9+8*x/3))/4)

num=[cdf(x) for x in unif]

plt.hist(num,bins=val,label='Histogram')
plt.plot(val,pdf(val), label='PDF', color='r')
plt.xticks(val)
plt.legend()
plt.show()
