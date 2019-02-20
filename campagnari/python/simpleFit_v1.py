#!/usr/bin/env python3
#
# Example of simple fit.
# The data set is generated from
# y = 2+x^2 with some smearing of y
# to simulate life not being perfect
#
# The fitting function is
# y = p[0] + p[1]*x^2
#
# To understand the notation for the
# fitting code, it helps to look at the
# lecture notes
#
# This is actualy a linear problem, and
# the 4 iterations are not necessary
#
# CC 10 Feb 2019
#----------------------------------
import numpy as np
import matplotlib.pyplot as plt

# We make a fake data set y=2+x*x, but
# We smear y a little bit by adding to
# it a random number between -0.5*d and 0.5*d
np.random.seed(912436455)
x = np.array([0.,0.5,1.,1.5,1.8, 2.1])
y = 2+x*x
N = len(x)   # number of points
d = 1.0
y = y + d*np.random.rand(N) - 0.5*d

# The error in y is d/sqrt(12).
# This is because the variance of a random
# uniform variable bewtween a and b
# is (b-a)**2/12.  Thus d/sqrt(12)...
e2 = np.full(N, d*d)/12.   # variance of y

# The inverse covariance matrix of the y's
W = np.diag(1./e2)

# we will fit as y=p[0] + p[1]*x*x
p  = np.array([-3., 10.])  # initial guess (way off!!!!)
y0 = p[0] +p[1]*x*x

# number of iterations, although in this case 1 is enough
# because the problem is linear
niter = 4

# matrices A and At are the derivatives of y wrt p
# (deriv. wrt p[0] is 1; deriv. with respect to p[1] is x^2) 
for iteration in range(niter):
    At = np.array( [np.full(N,1), x*x] )  # 2xN matrix
    A  = (At.T).copy()                    # Nx2 matrix
    dy = (np.array( [(y-y0),] )).T        # Nx1 column vector
    # debug: look at these matrices on the 1st iteration (just for fun)
    if iteration == 0:
        print(" ")
        print("-- At ---")
        print(At)
        print(" ")
        print("-- A ---")
        print(A)
        print(" ")
        print("-- W ---")
        print(W)
        print(" ")
        print("-- dy ---")
        print(dy)
        input("Enter something to continue")
                          
    # find the matrix to be inverted, and invert it
    temp  = np.matmul(At, W)       # 2xN * NxN = 2xN
    temp2 = np.matmul(temp, A)     # 2xN * Nx2 = 2x2
    temp3 = np.linalg.inv(temp2)   # 2x2 ... this is the covariance matrix

    # multiply again
    temp4 = np.matmul(temp3, At)     # 2x2 * 2xN = 2xN
    temp5 = np.matmul(temp4, W)      # 2xN * NxN = 2xN
    dpar  = np.matmul(temp5, dy)     # 2xN * Nx1 = 2x1 column vector

    # the new values of the parameters
    p[0] = p[0] + dpar[0][0]
    p[1] = p[1] + dpar[1][0]

    # the currently fitted value of y
    y0 = p[0] +p[1]*x*x

    # the chisq
    chisq = ((y0-y)*(y0-y)/e2).sum()

    # output stuff
    print("   ")
    print("Iteration no. ", iteration)
    print(chisq)
    print("p[0] = ", p[0])
    print("p[1] = ", p[1])
    print("Covariance:")
    print(temp3)

# Now plot it
f, a = plt.subplots()
xmin = x.min()-1
xmax = x.max()+0.2
a.errorbar(x, y, yerr=np.sqrt(e2), linestyle='none', color="red", marker='o')
a.set_xlim(xmin, xmax)
xpl = np.linspace(xmin, xmax, 1000)
ypl = p[0] + p[1]*xpl*xpl
a.set_xlabel("x")
a.set_ylabel("y")
a.plot(xpl, ypl, color='blue', linestyle='solid')
f.show()
input('Enter something to continue')

# Now a scan of the chisq
# We calculate the chisq for various values of p[0] and p[1]
# Note: temp3[0][0] and temp3[1][1] are the diagonal
# elements of the covariance matrix, ie, the square of the errors
# on p[0] and [p1],
# We will scan out to 4 sigma
fig2, ax2 = plt.subplots()
p0min = p[0] - 4*np.sqrt(temp3[0][0])
p0max = p[0] + 4*np.sqrt(temp3[0][0])
p1min = p[1] - 4*np.sqrt(temp3[1][1])
p1max = p[1] + 4*np.sqrt(temp3[1][1])
nscan = 100
p0 = np.linspace(p0min, p0max, nscan)
p1 = np.linspace(p1min, p1max, nscan)
ax2.set_xlim(p0min,p0max)
ax2.set_ylim(p1min,p1max)
z = np.zeros( shape=(nscan,nscan) )   # an emptyt array for now
for i0 in range(0, nscan):
    this_p0 = p0[i0]
    for i1 in range(0, nscan):
        this_p1   = p1[i1]
        yy        = this_p0 + this_p1 * x * x
        z[i0][i1] = ((yy-y)*(yy-y)/e2).sum() - chisq

# "z" is a map of chisq-chisq_at_minimum
# Correspond to the 68% 95% 99% coverage for 2 parameters
# (PDG Table 38.2)
CS = ax2.contour(p0, p1, z, [2.30, 5.99, 9.21])
fmt = {}
strs = [ '68%', '95%', '99%' ]
for l,s in zip( CS.levels, strs ):
    fmt[l] = s
ax2.clabel(CS, inline=True, fmt=fmt, fontsize=10)
    
# put a point at the best fit
ax2.plot(p[0], p[1], 'ko')

# put a grid
ax2.grid()

#show the figure
fig2.show()
input("Press <Enter> to continue") 
