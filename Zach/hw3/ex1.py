#!/usr/bin/env python3

import numpy as np
import math
from scipy import stats
import matplotlib.pyplot as plt

np.random.seed(12345)

def toy(N):
	print('N= %d' %N)
	coord=np.random.random((N,2)) -1/2 #N pairs centered at zero
	length=np.hypot(coord[:,0],coord[:,1])
	n=len([i for i in length if i<.5]) #Number of points in semicircle
	#print('n=',n)
	f_tilde=n/N
	pi_tilde=4.0*f_tilde #Calculated pi value
	off=100*(pi_tilde-math.pi)/math.pi #Percent off
	print("The calculated pi value = %.5f" %pi_tilde, "is %.5f %% off" %off)
	sigma_f_tilde=math.sqrt(f_tilde*(1-f_tilde)/N) #Uncertainty in f
	rho=(pi_tilde-math.pi)/(4*sigma_f_tilde) #Pull calculation
	return rho**2

chisquared=0
for N in [100,1000,10000,100000,1000000]:
	chisquared += toy(N)

prob=1-stats.chi2.cdf(chisquared,5)
print("The calculated chi-squared value is: ", chisquared)
print("The probability of finding a chi-squared larger than this is: ", prob)
