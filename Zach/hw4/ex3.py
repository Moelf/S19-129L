#!/usr/bin/env python3

import numpy as np

N=100000
np.random.seed(12345)

#Simple monte carlo integral using uniform random values

x=np.random.uniform(low=0.0,high=1.0,size=N)
y=np.random.uniform(low=2.0,high=4.0,size=N)
z=np.random.uniform(low=0.0,high=45.0,size=N)

def f(x,y):
	return( (x+2.0*y)*(x+y) )

integral=np.sum(z<f(x,y))/N*2.0*45.0

print("The calculated value is", integral)
