#!/usr/bin/env python3
#
# Test of a simple linear fit using np.polyfit
#
# 

# CC 19 Feb 2019
#-----------------------
import numpy as np

x = np.array([1., 2., 3.])
y = np.array([1.1, 1.9, 3.1])     
dy = np.array([0.1, 0.07, 0.12])  # error in y

# fit ignoring the errors on y gives slope=1, as expected,
degree = 1    # polynomial of degree 1
p = np.polyfit(x, y, degree)
print(p)
# The fit function is y = p[0]*x + p[1]
# The answer will be
# array([1.        , 0.03333333])

# fit including errors gives slope<1, as expected.
# Note the "w" parameter is the weight and needs to
# be equal to 1/error
p = np.polyfit(x, y, degree, w=1./dy)
print(p)
# The answer will be
# array([0.98      , 0.02909091])

# Trying to retrieve covariance matrix gives error
# on the numpy version installed on the rpi.
# This error does not make sense to me and triggered a
# discussion between developers
# https://mail.scipy.org/pipermail/numpy-discussion/2013-February/065649.html
#
# A later version of numpy is fixed but only with a special calling sequence
#
# This crashes on the numpy version installed on the rpi
# It does not crash but gives a "wrong" answer from the
# physicist point of view with later versions of numpy  
#p, cov = np.polyfit(x, y, degree, w=1./dy, cov=True)
#print(p)
#print(cov)
#
# This also crashes on the rpi but fives the "correct"
# answer on later versions of numpy
#p,cov = np.polyfit(x, y, degree, w=1/dy, cov='unscaled')
#print(p)
#print(cov)
