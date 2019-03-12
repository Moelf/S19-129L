#!/usr/bin/env python3

import pickle
import numpy as np
from math import pi
from LVector import LVector as Lv

# mass constants in GeV
massB_p = 5.28
massD_star0 = 2.01
massD_0 = 1.86
massK_m = 0.494
massPi_p = 0.1396
massPi_0 = 0.1350


# Pick random point on sphere
def randomPhi():
    return np.random.uniform(0, 2*pi)


def randomTheta():
    v = np.random.rand()
    return np.arccos(2*v - 1)


def spheToCartesian(phi, theta):
    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)
    return np.array([x, y, z])


# Calculate P_0 = E/c
def EoverC(p, m):
    return np.sqrt(np.dot(p, p) + m**2)


# Momentum of each particle in a rest frame decay
def restDecayMomentum(M, m1, m2):
    return np.sqrt((M**2 - (m1+m2)**2) * (M**2 - (m1-m2)**2))


# If moving A decays in B and C,
# v1 is 3-velocity of A in lab frame, v2 is 3-velocity of B or C in A's frame
#def decayAngle(v1, v2):



def restSpinLessDecay(M, m1, m2):
    p = restDecayMomentum(M, m1, m2)
    theta1, phi1 = randomTheta(), randomPhi()
    theta2, phi2 = randomTheta(), randomPhi()
    # 3-momentums
    p1 = p*spheToCartesian(phi1, theta1)
    p2 = p*spheToCartesian(phi2, theta2)

    np.insert(p1, 0, EoverC(p1, m1))
    np.insert(p2, 0, EoverC(p2, m2))
    # NOW 4-momentums
    p1 = Lv(p1)
    p2 = Lv(p2)
    return p1, p2


if __name__ == "__main__":
    output = []
    for _ in range(1000):
        pDstar0, Ppi1 = restSpinLessDecay(massB_p, massD_star0, massPi_p)

        pD0, Ppi0 = restSpinLessDecay(massD_star0, massD_0, massPi_0) #need to take spin into account?

        PK, Ppi2 = restSpinLessDecay(massD_0, massK_m, massPi_p)

        Pg1, Pg2 = restSpinLessDecay(massPi_0, 0, 0)

        output.append([Ppi1, PK, Ppi2, Pg1, Pg2])

    with open('data.pik', 'wb') as File:
        pickle.dump(output, File)
