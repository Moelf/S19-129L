#!/usr/bin/env python3

import numpy as np
import math
import matplotlib.pyplot as plt

N=100000
np.random.seed(12345)

mean=3.0
stddev=0.5
N=5.0
f_values=[]

#Take 100 x values between -3 and 15
x_values=np.linspace(-3,15, num=100)

def g(x,y):
	return math.exp( -(x+y) ) * (x+y)**N
#Calculate the integral, f(x), at each given x value using monte carlo method
for x in x_values:

	y_values=np.random.normal(mean,stddev,1000)
	y_values=y_values[y_values>0]
	f_value=[]
	for i in y_values:
		g_values=g(x,i)
		f_x=np.mean(g_values)
		f_value.append(f_x)
	f_values.append(np.mean(f_value))

#plot final function f(x)
plt.plot(x_values,f_values, 'x')
plt.xlabel('X')
plt.ylabel('f(x)')
plt.show()
