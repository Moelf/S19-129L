#!/usr/bin/env python3


import numpy as np

np.random.seed(12345)

# parameters
s_count = 1500
s_min   = 0
s_max   = 15
N       = -1
mu      = -1
sigma   = -1
while N<0:
		try:
			N = float(input('Please pick a value for N: '))
		except ValueError:
			print('Input a number please')
while mu<0:
		try:
			mu = float(input('Please pick a value for mu: '))
		except ValueError:
			print('Input a number please')
while sigma<0:
		try:
			sigma = float(input('Please pick a value for sigma: '))
		except ValueError:
			print('Input a number please')

s_values = np.random.uniform(s_min,s_max,s_count)
excluded = []
for s in s_values:
	B = np.random.normal(mu,sigma,s_count)
	B = B[B>0]
	n = np.random.poisson(s+B)
	fraction = len(n[n<N])/len(n)
	if fraction<.05:
		excluded.append(s)
	else:
		continue

min_cl = min(excluded)

print('The 95%% CL limit is %.2f' %min_cl)
