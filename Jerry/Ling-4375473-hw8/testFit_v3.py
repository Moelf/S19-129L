#!/usr/bin/env python3
#
# Test of a simple linear fit using
# iminuit
#
# 
# CC 19 Feb 2019
#
# Added 1D chisquared scan
# CC 21 Feb 2019
#-----------------------
import numpy as np
import matplotlib.pyplot as plt
from iminuit import Minuit

# Minuit needs to define a function to minimize
# explicitely...it does not need to be a chisquared
def myChi2(slope, offset):
    global x
    global y
    global dy
    yfit = slope*x + offset
    temp = (y-yfit)/dy
    print(np.shape(temp*temp))
    return (temp*temp).sum()

x = np.array([1., 2., 3.])
y = np.array([1.1, 1.9, 3.1])     
dy = np.array([0.1, 0.07, 0.12])  # error in y

# Initialize Minuit
# It needs
# - the name of the function to minimize
# - initial value
# - print_level is for debug prints
# - errordef=1 is for chisquared-type  fits (0.5 for log-likelihoods)
# - print_level=0 is "silent"  Set it to 1 etc for more output
# - error_slope and error_offset are the "step sizes" for the initial
#   search for a minimum
m = Minuit(myChi2, slope=1., offset=0., print_level=0,
           errordef=1.0, error_slope=0.1, error_offset=0.1) 

# Migrad is the simplest minimization
fmin, param = m.migrad()

# fmin is a dictionary with lots of info on the status of the minimization
# Here is some of it
print('Value of minimized function at minimum = ',fmin['fval'])
print('Estimated distance to minimum          = ',fmin['edm'])
print('Is the fit valid = ', fmin['is_valid'])
print('Has covariance   = ', fmin['has_covariance'])
print('---------------')

# param is a list of dictionaries with info on the fit parameters
# Here is some of it
print('Parameter name  = ', param[0]['name'])
print('Parameter value = ', param[0]['value'])
print('Parameter error = ', param[0]['error'])
print(' ')
print('Parameter name  = ', param[1]['name'])
print('Parameter value = ', param[1]['value'])
print('Parameter error = ', param[1]['error'])
print(' ')

# Covariance Matrix
for i in [0,1]:
    for j in [0,1]:
        print("Cov(%d,%d) = %f" %(i,j,m.matrix()[i][j]))

# Minos calculates asymmetric errors for more complicated cases
m.minos(var="slope")
m.minos(var="offset")

# Some output
m.print_param()

# And now contours of the fitted function
# (very similar to testFit_V2.py version)
fittedSlope  = param[0]['value']
fittedOffset = param[1]['value']
fig2, ax2 = plt.subplots()

# bound=4   --> got to +/- 4 sigma
# bins=100  --> how many bins to do
xx, yy, zz = m.contour('slope', 'offset', subtract_min=True, bound=4, bins=100)
CS = ax2.contour(xx, yy, zz, [2.30, 5.99, 9.21])
fmt = {}
strs = [ '68%', '95%', '99%' ]
for l,s in zip( CS.levels, strs ):
    fmt[l] = s
ax2.clabel(CS, inline=True, fmt=fmt, fontsize=9)
ax2.plot(fittedSlope, fittedOffset, 'ko')
ax2.set_xlabel('slope')
ax2.set_ylabel('offset')
fig2.show()
input('Enter something to continue ')


# If we are particularly interested in one parameter
# (say: the slope) we can scan the chisquared as a function
# of "slope" minimizing wrt to the other parameter ("offset"
# in this case) at each point.  This is similar information
# as the previous contour but
# (a) Contours can only be drawn for two parameters whereas
#     this procedure can be done for as many parameters
#     as you wish, ie, you fix one parameter and then minimize
#     wrt all other parameters, and then you repeat by scanning
#     the value of the fixed parameter
# (b) The total 1 (2,3) sigma uncertainty for the scanned
#     parameter is taken at the value of the scanned parameter
#     where the chisquared increases by 1 (2^2=4, 3^2=9) from
#     its value at the minimum.
# For "well-behaved" problems (or in the limit of large statistics)
# this scan will look parabolic.
# This process is called "profiling"
xxx, yyy, _ = m.mnprofile('slope', subtract_min=True, bins=100, bound=3)
fig3, ax3 = plt.subplots()
ax3.plot(xxx,yyy,linestyle='solid', color='b')
ax3.set_ylim(0, 1.2*max(yyy))
ax3.set_xlim(min(xxx), max(xxx))
ax3.set_xlabel('slope')
ax3.set_ylabel('deltaChiSquared')
ax3.grid()
fig3.show()
input('Enter something to quit ')
