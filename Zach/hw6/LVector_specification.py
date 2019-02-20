#!/usr/bin/env python3

# The 4 vector class should be saved in file LVector.py
import LVector as lv
import numpy as np

# The 4-vector convention is (x0, x1, x2, x3) where
# in the case of space/time 4-vector
#      x0=ct  x1=x  x2=y  x3=z
# in the case of the energy momentum 4-vector
#      x0=E/c x1=px  x2=py  x3=pz
#
# A 4-vector can be initialized through either a
# np.array or a list...both are allowed
p = [ 20., 1., 2., 3. ]
q = np.array( [40., 2., 4., 9.] )
a = lv.LVector(p)
b = lv.LVector(q)

# There should be a nicely implemented print method
print(a)

# Subtraction and additions should be possible through
# the "+" and "-" operators
c = a + b
d = a - b

# Should be able to multiply a vector by a scalar or multiply
# two vectors.  In case of two vector*vector multiplication,
# the sign convention should be x*y = x0*y0 - x1*y1 - x2*y2 - x3*y3
cc   = 4*a    # scalar*vector gives a vector
dd   = a*4    # this should be allowed and give same result as previous line
blah = a*b    # "blah" is a number

# square of a vector...
foo = a.square()     # returns a*a

# can set any component to a float
a.set_x0(340.)  # change the 0th component to 340
a.set_x1(35.)   # change the 1st component to 35
a.set_x2(36.)   # change the 2nd component to 36
a.set_x3(37.)   # change the 3rd component to 37

# length of the 3 vector sqrt(x1*x1 + x2*x2 + x3*x3)
rl = a.get_rlength()   

# component of the 3 vector in the (x1,x2) plane, sqrt(x1*x1 + x2*x2)
rt = a.get_rtlength()

# the 3 vector as a np.array of dimension 3 with components (x1,x2,x3)
rvector = a.get_r()

# projection of the  3 vector onto the (x1,x2) plane, ie, same np.array
# as the get_r() methhod but with the x3 component set to zero
rtvector = a.get_rt()    # np.array with 3 components

# The azimuthal angle in polar coordinates, ie, the angle between the
# "rtvector" defined above and the x1-axis (between 0 and 2pi)
phi = a.phi()
# the polar angle, ie, the angle between the "rvector" defined above and
# the x3 axis (between 0 and pi)
theta = a.theta()
# Pseudo-rapidity.  This is defined as -log( tan(theta/2) )
eta = a.eta()

# Rapidity.  This is defined as 0.5*log( (x0+x3) / (x0 -x3) )
y = a.Y()

# Boost by beta.  Beta is a 3D array or list of v/c
# Convention is: boost to frame with (vector) velocity
# beta wrt original frame
# A compact way of writing the boost equation in an
# arbitrary direction is equation 5.35 of
# https://users.physics.ox.ac.uk/~smithb/website/coursenotes/rel_A.pdf
#
# Equivalent formula
# https://en.wikipedia.org/wiki/Lorentz_transformation
# (scroll down and look for the boxed equation in
# the section on "Vector transformations"
#
beta1 = [0.1, 0.2, 0.3]
beta2 = [0.11, 0.3, 0.1]
a.boost(beta1)
b.boost(beta2)

# Sanity check...the scalar products must be boost-invariants
s1 = a*b
print(a)
print(b)
a.boost(beta1)
b.boost(beta1)
print(a)
print(b)
s2=a*b
print(s1,s2)  # these better be the same!!!!

