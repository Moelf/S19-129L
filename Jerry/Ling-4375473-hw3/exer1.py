import math
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def MC1(N):
    print("N = %d" % N)
    coords = np.random.random((N,2))-0.5 #center at 0
    lengths = np.hypot(coords[:,0],coords[:,1])
    n = len(list(filter(lambda x: x<0.5, lengths)))
    print("n = %f" % n)
    our_f = n/N
    ourPi = 4.0 * our_f
    print("ourPi = %.4f" % ourPi, "is %.4f %% away.\n" % abs( 100*(ourPi - math.pi)/math.pi))
    sigma_f = math.sqrt(our_f*(1-our_f)/N)
    sigma_pi = 4*sigma_f
    rho = (ourPi - math.pi)/sigma_pi
    return rho**2

np.random.seed(387645)
ChiSqu = 0
for N in{100,1000,10000,100000,1000000}:
    ChiSqu += MC1(N)
prob = 1 - stats.chi2.cdf(ChiSqu, 5)
print("\nChi Squared Probability is %.3f %%" % (prob*100))
