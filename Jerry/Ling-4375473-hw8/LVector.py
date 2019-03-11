import numpy as np
import math
class LVector:
    """
    Lorentz vector (Four vector) class
    CC 4 Jun 2018
    """
    def __init__(self, inputVector):
        """
        Initialize by passing array or list of 4 numbers.
        The zeroth element is the time component
        """
        self.v  = np.array(inputVector, dtype=float)  # in case we pass a list
        
    def copy(self):
        """
        Make copy
        """
        return LVector(self.v)

    def __str__(self):
        """
        Nicely formatted print
        """
        return "({0},{1},{2},{3})".format(self.v[0], self.v[1], self.v[2],
                                          self.v[3])

    def __add__(self, other):
        """
        Addition of four vectors
        """
        return LVector( self.v + other.v)

    def __sub__(self, other):
        """
        Subtraction of four vectors
        """
        return LVector( self.v - other.v)

    def __mul__(self, other):
        """ 
        Scalar product: vector*vector or scalar*vector
        """
        if type(other) == type(self):
            return self.v[0]*other.v[0] - (self.v[1:]*other.v[1:]).sum()
        else:
            return LVector(other*self.v)

    def __rmul__(self, other):
        """ 
        Allows vector*scalar syntax
        """
        return LVector(other*self.v)
        
    def square(self):
        """ 
        Returns the square of the vector as x0^2 - x1^2 - x2^2 - x3^2 
        """
        return self.v[0]**2 - (self.v[1:]**2).sum()

    def set_x0(self, val):
        """
        Set time component
        """
        self.v[0] = val
        
    def set_x1(self, val):
        """
        Set first space component
        """
        self.v[1] = val

    def set_x2(self, val):
        """
        Set second space component
        """
        self.v[2] = val

    def set_x3(self, val):
        """
        Set third space component
        """
        self.v[3] = val

    def set_r(self, val):
        """
        Set three-vector piece.  Expects array or list of 3 numbers
        """
        v_val = np.array(val, dtype=float)  # in case it is passed as list
        self.v[1:] = v_val
        
    def get_x0(self):
        """
        Get time component
        """
        return self.v[0] 
        
    def get_x1(self):
        """
        Get first space component
        """
        return self.v[1]

    def get_x2(self):
        """
        Get second space component
        """
        return self.v[2]
        
    def get_x3(self):
        """
        Get third space component
        """
        return self.v[3]

    def boost(self, beta):
        """
        Boost by beta.  Beta is a 3D array or list of velocity/c
        Convention is: boost to frame with (vector) velocity beta
        wrt original frame
        NOT protected against beta.sum() >= 1 ... use with care
        """
        vbeta = np.array(beta)        # make sure it is a vector (np.array)
        beta2 = (vbeta*vbeta).sum()   # beta squared
        gamma = np.sqrt( 1. / (1 - beta2 ) )
        n = vbeta / np.sqrt(beta2) # unit vector in direction of vbeta
        old = self.copy()  # 4 vector before the boost
        self.v[0] =  gamma * (old.v[0] - (old.v[1:] * vbeta).sum() ) 
        self.v[1:] = ( old.v[1:] +
                       (gamma-1) * (old.v[1:]*n).sum()       * n -
                       gamma     * old.v[0] * np.sqrt(beta2) * n )

    def get_rlength(self):
        """
        Length of 3-vector in xyz plane
        """
        return np.sqrt( (self.v[1:]*self.v[1:]).sum() )

    def get_rtlength(self):
        """
        Length of 3-vector in xy plane
        """
        return self.get_rlength() * math.sin(self.theta())

    def get_r(self):
        """
        3-vector components as np.array
        """
        return self.v[1:]

    def get_rt(self):
        """
        3-vector component in the xy plane
        """
        return np.array( [self.v[1], self.v[2], 0.0] )
        
    
    def phi(self):
        """
        Azimuthal angle, ie, angle with x-axis in xy-plane (0 to 2*pi) 
        """
        if self.v[1] == 0 and self.v[2] == 0:
            return 0.
        elif self.v[2] < 0:
            return math.atan2(self.v[2], self.v[1]) + 2*math.pi
        else:
            return math.atan2(self.v[2], self.v[1])
        
    def theta(self):
        """
        Polar angle, 0 to pi
        """
        if self.get_rlength() == 0:
            return 0.
        else:
            return math.acos(self.v[3] / self.get_rlength() )

    def Y(self):
        """
        Rapidity (high energy physics): (1/2) log( (x0+x3)/(x0-x3) )
        NOT protected against log(-ve)...use with care
        """
        return 0.5 * math.log( (self.v[0]+self.v[3]) / (self.v[0]-self.v[3]) )

    def eta(self):
        """
        Pseudorapidity: -log (tan (theta/2) ) )
        NOT protected against log(zero)...use with care
        """
        return -math.log( math.tan (self.theta()/2.) )

    def rotate_by_axis(self, axis, angle):
        """
        Rotate the 3 vector counter-clockwise by 
        angle around axis.
        axis is an array or a list of 3 numbers.
        Does not need to be normalized to 1.
        Returns the rotation matrix
        """
        vLen = math.sqrt( sum([xyz*xyz for xyz in axis]) )
        x, y, z = [xyz/vLen for xyz in axis]
        c = math.cos(angle)
        d = 1 - c
        s = math.sin(angle)
        R = [ [c+d*x*x,   d*x*y-s*z, d*x*z+s*y],
            [d*y*x+s*z, c+d*y*y,   d*y*z-s*x],
            [d*z*x-s*y, d*z*y+s*x, c+d*z*z  ] ]
        w = self.v[1:]
        wrot = np.matmul(R, w)
        self.v[1:] = wrot
        return R

    def rotate_by_matrix(self, M):
        """
        Rotate 3 vector by rotation matrix M
        """
        w = self.v[1:]
        wrot = np.matmul(M, w)
        self.v[1:] = wrot
        
                            

    
        
        
