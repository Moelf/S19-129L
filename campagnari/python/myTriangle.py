import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Note: this makes use of some "magic methods"
# to "overload" operators like "*" to define
# the multiplication of a triangle by a number (!)
# For a list of such possibilities, see
# http://www.ironpythoninaction.com/magic-methods.html

class myTriangle:
    """
    Triangle class in 2D
    """

    def __init__(self, p0, p1, p2):
        """
        Initialize by passing the three points at the verteces.
        Each point can be a 2-element np.array of (x,y) or a list.
        We should probably protect against passing junk, but whatever.
        We will store the points as np.array
        """
        self.p0 = np.array(p0, dtype=float) # in case we pass a list
        self.p1 = np.array(p1, dtype=float) # in case we pass a list
        self.p2 = np.array(p2, dtype=float) # in case we pass a list

    def copy(self):
        """
        make a copy
        """
        return myTriangle(self.p0, self.p1, self.p2)

    def __str__(self):
        """
        Nicely formatted print
        """
        return " p0 = ({0}) \n p1 = ({1}) \n p2 = ({2})".format(self.p0,self.p1,self.p2)

    def center(self):
        """
        return center of gravity of triangle
        """
        return (1./3.) * (self.p0+self.p1+self.p2)

    def side(self, i):
        """
        Length of side i.
        i = 0 --> length between p0 and p1
        i = 1 --> length between p1 and p2
        i = 2 --> length between p2 and p0
        If i is out of range, return -9999
        Should have better way of returning an error!!!!!
        """
        if i == 0:
            length = math.sqrt( np.square(self.p0-self.p1).sum())
        elif i == 1:
            length = math.sqrt( np.square(self.p1-self.p2).sum())
        elif i == 2:
            length = math.sqrt( np.square(self.p2-self.p0).sum())
        else:
            length = -9999
        return length

    def perimeter(self):
        """
        Perimeter of triangle
        """
        return self.side(0)+self.side(1)+self.side(2)

    def area(self):
        """
        Area of the triangle
        Use the "shoelace" formula (check wikipedia!)
        """
        d1 = self.p0[0] - self.p2[0]
        d2 = self.p1[1] - self.p0[1]
        d3 = self.p0[0] - self.p1[0]
        d4 = self.p2[1] - self.p0[1]
        return 0.5 * abs( d1*d2 - d3*d4 )

    def angle(self,i):
        """
        angle at point i in radians
        i = 0  point is p0
        i = 1  point is p1
        i = 2  point is p2
        If i is out of range, return -9999
        Should have better way of returning an error!!!!!
        """
        # v and w are vectors along the sides 
        if i == 0:
            v = self.p1 - self.p0
            w = self.p2 - self.p0
        elif i == 1:
            v = self.p2 - self.p1
            w = self.p0 - self.p1
        elif i == 2:
            v = self.p1 - self.p2
            w = self.p0 - self.p2
        else:
            return 999

        # scalar product v*w = abs(v)*abs(w)*cos(angle)
        vlength = math.sqrt( np.square(v).sum() )
        wlength = math.sqrt( np.square(w).sum() )
        return math.acos( (v*w).sum() / (vlength*wlength) )

    def translate(self, v):
        """
        Translate triangle by vector v
        v can be 2-element np.array of (x,y) or a list.
        We should probably protect against passing junk, but whatever.
        """
        w = np.array(v, dtype=float) # in case we pass a list
        self.p0 = self.p0 + w
        self.p1 = self.p1 + w
        self.p2 = self.p2 + w

    def rotate(self, angle):
        """ 
        rotate counterclockwise by some angle (units=radians)
        around the center of gravity
        """
        center = self.center()
        c = math.cos(angle)
        s = math.sin(angle)
        rotationMatrix = np.matrix([ [c,-s], [s,c] ])
        self.translate(-center)
        self.p0 = np.dot( rotationMatrix, self.p0)  # this is a matrix now
        self.p1 = np.dot( rotationMatrix, self.p1)
        self.p2 = np.dot( rotationMatrix, self.p2)
        self.p0 = np.array(self.p0)[0]   # turn it back into an array
        self.p1 = np.array(self.p1)[0]   # turn it back into an array
        self.p2 = np.array(self.p2)[0]   # turn it back into an array
        self.translate(center)

    def __rmul__(self, scale):
        """
        return triangles resized by scale keeping center in same place
        """
        new = self.copy()
        oldCenter = new.center()
        # put p0 at the origin
        new.translate(-new.p0)
        new.p1 = scale * new.p1
        new.p2 = scale * new.p2
        newCenter = new.center()
        new.translate(oldCenter-newCenter)
        return new

    def draw(self, fig, ax):
        """
        Draw the triangle
        """
        line0 = Line2D( [self.p0[0], self.p1[0]], [self.p0[1], self.p1[1]] )
        line1 = Line2D( [self.p1[0], self.p2[0]], [self.p1[1], self.p2[1]] )
        line2 = Line2D( [self.p0[0], self.p2[0]], [self.p0[1], self.p2[1]] )
        ax.add_line(line0)
        ax.add_line(line1)
        ax.add_line(line2)
        fig.show()
                            

        
        
