import numpy as np


class LVector:
    """
    A very ineffecient implementation of Lorentz vector
    """

    def __init__(self, coords):
        self.coords = np.array(coords, dtype=float)
        self.x0 = self.coords[0]
        self.x1 = self.coords[1]
        self.x2 = self.coords[2]
        self.x3 = self.coords[3]

    def set_x0(self, value):
        self.x0 = value
        self.coords[0] = value

    def set_x1(self, value):
        self.x1 = value
        self.coords[1] = value

    def set_x2(self, value):
        self.x2 = value
        self.coords[2] = value

    def set_x3(self, value):
        self.x3 = value
        self.coords[3] = value

    def __str__(self):
        return " x0 = ({0}) \n x1 = ({1}) \n x2 =\
        ({2}) \n x3 = ({3})".format(self.x0, self.x1, self.x2, self.x3)

    def __add__(self, other_vector):
        return LVector(self.coords+other_vector.coords)

    def __sub__(self, other_vector):
        return LVector(self.coords-other_vector.coords)

    def __mul__(self, other):
        if isinstance(other, LVector):
            return self.x0*other.x0\
                - self.x1*other.x1\
                - self.x2*other.x2\
                - self.x3*other.x3

        # default scaler product
        return LVector(self.coords*other)

    def __rmul__(self, other):
        # a*b == b*a
        return self.__mul__(other)

    def get_r(self):
        return self.coords[1:]

    def get_rt(self):
        temp = self.coords[1:]
        temp = temp[-1] = 0
        return temp

    def get_rlength(self):
        return np.sqrt(np.dot(self.get_r(), self.get_r()))

    def get_rtlength(self):
        return np.srqt(np.dot(self.get_rt(), self.get_rt()))
