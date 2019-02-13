#!/usr/bin/env python3

import numpy as np


# PDF
def myPDF(x, y):
	if (x_0<=x<=x_1) and (y_0<=y<=y_1):
		return (x+y)/7
	else:
		return 0.0

# Proposal
def valid_proposal(x1,y1,x2,y2):
	a=myPDF(x2,y2)/myPDF(x1,y1)
	a_0=min(1,a)
	return (np.random.rand() <= a_0)


# Function
def f(x,y):
	return 7*(x+2*y)

# initialize random number
np.random.seed(12345)

# Parameters of the chain
n      = 100000
nBurn  = 10000
x_0 = 0
x_1 = 1
y_0 = 2
y_1 = 4
x=np.random.uniform(0,1)
y=np.random.uniform(2,4)
d=.5

#initialize chain
chain=[]

# run through and generate the markov chain
for i in range(0,n):
	x_prop=np.random.uniform(x-d,x+d)
	y_prop=np.random.uniform(y-d,y+d)
	if valid_proposal(x,y,x_prop,y_prop):
		x,y=x_prop,y_prop
	else:
		pass
	chain.append([x,y])

# put list into array removing the burn in part
chain=chain[nBurn:]
N=len(chain)

#calculate the final integral
integral=np.sum([f(i[0], i[1]) for i in chain])/N

print('Using the Markov Chain method, the integral is: %.4f' %integral)

input("Press any key to continue")

