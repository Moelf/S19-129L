from math import pi
import numpy as np
from LVector import LVector as Lv


# http://mathworld.wolfram.com/SpherePointPicking.html
def randomPhi():
    return 2*pi*np.random.rand()


def randomTheta():
    v = np.random.rand()
    return np.arccos(2*v - 1)

# since 4-vectors are in catetian coord


def spheToCartesian(phi, theta):
    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)
    return np.array([x, y, z])


# calculate the first component of 4-momentum E
# given the 3-momentum
# https://en.wikipedia.org/wiki/Four-momentum#Derivation
def EoverC(p, m):
    res = np.sqrt(np.dot(p, p) + m**2)
    return res


# get a 3 velocity a 4-momentum, i.e beta vector
def PtoV(p):
    beta = p.get_r()/p.get_x0()
    return beta


# momentum scalar of particle in a rest frame decay
def restDecayMomentum(M, m1, m2):
    return np.sqrt((M**2 - (m1+m2)**2) * (M**2 - (m1-m2)**2))/(2*M)


# pdf of spin = 1 decay angle
# R = x^3 -> x = (R)1/3
def SpinTheta():
    R = np.random.rand()
    costheta = ((R)**(1/3))
    # because pdf is about cos(theta), split sign before arccoskhj
    if np.random.rand() < 0.5:
        costheta = -costheta
    return np.arccos(costheta)


def restDecay(M, m1, m2, spin=0):
    p = restDecayMomentum(M, m1, m2)
    if spin == 0:
        theta1, phi1 = randomTheta(), randomPhi()
    elif spin == 1:
        theta1 = SpinTheta()
        phi1 = randomPhi()
    # 3-momentums, cononical conservation
    p1 = p*spheToCartesian(phi1, theta1)
    p2 = -p1

    p1 = np.insert(p1, 0, EoverC(p1, m1))
    p2 = np.insert(p2, 0, EoverC(p2, m2))
    # NOW 4-momentums
    lvp1 = Lv(p1)
    lvp2 = Lv(p2)
    return lvp1, lvp2
