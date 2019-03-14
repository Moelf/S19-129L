import pickle
import math
from math import pi
import numpy as np
import matplotlib.pyplot as plt
from LVector import LVector as Lv

# 1000 finals states of the following decay chain
# http://pdglive.lbl.gov/Viewer.action
# http://pdg.lbl.gov/2017/reviews/rpp2017-rev-kinematics.pdf
# ---------------------------------------------------------
# B+ -> D*0 + pi+
#        |
#        ---> D0 + pi0
#             |     |
#             |     ---> gamma + gamma
#             ---> K- + pi+
# ---------------------------------------------------------

# mass constants in GeV
massB_p = 5.28
massD_star0 = 2.01
massD_0 = 1.86
massK_m = 0.494
massPi_p = 0.1396
massPi_0 = 0.1350


# http://mathworld.wolfram.com/SpherePointPicking.html
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


# calculate the first component of 4-vector E
# https://en.wikipedia.org/wiki/Four-momentum#Derivation
def EoverC(p, m):
    res = np.sqrt(np.dot(p, p) + m**2)
    return res


# get a 3 velocity a 4-momentum, for boost
def PtoV(p):
    p3 = p.get_r()
    v = p3/p.v[0]
    return v


# momentum of either particle in a rest frame decay
def restDecayMomentum(M, m1, m2):
    return np.sqrt((M**2 - (m1+m2)**2) * (M**2 - (m1-m2)**2))/(2*M)


# say, A is moving, then A->B+C
# v1 is 3-velocity of A in lab frame, v2 is 3-velocity of B or C in A's frame
def decayAngle(v1, v2):
    denom = np.sqrt(np.dot(v1, v1) * np.dot(v2, v2))
    return np.arccos(np.dot(v1, v2) / denom)


# R = x^3 -> x = (R)1/3
def SpinTheta():
    R = np.random.rand()
    theta = np.arccos((R)**(1/3))
    if np.random.rand() < 0.5:
        return -theta + pi/2
    else:
        return theta + pi/2


def restSpinLessDecay(M, m1, m2):
    p = restDecayMomentum(M, m1, m2)
    theta1, phi1 = randomTheta(), randomPhi()
    # 3-momentums
    p1 = p*spheToCartesian(phi1, theta1)
    p2 = -p1

    p1 = np.insert(p1, 0, EoverC(p1, m1))
    p2 = np.insert(p2, 0, EoverC(p2, m2))
    # NOW 4-momentums
    lvp1 = Lv(p1)
    lvp2 = Lv(p2)
    return lvp1, lvp2


def restSpinDecay(M, m1, m2):
    p = restDecayMomentum(M, m1, m2)
    # this account for the Wigner angle but in it's rest frame
    theta1 = SpinTheta()
    phi1 = randomPhi()
    # 3-momentums
    p1 = p*spheToCartesian(phi1, theta1)
    p2 = -p1

    p1 = np.insert(p1, 0, EoverC(p1, m1))
    p2 = np.insert(p2, 0, EoverC(p2, m2))
    # NOW 4-momentums
    lvp1 = Lv(p1)
    lvp2 = Lv(p2)
    return lvp1, lvp2


if __name__ == "__main__":
    output = []
    heli = []
    for _ in range(1000):
        pDstar0, pPi_p1 = restSpinLessDecay(massB_p, massD_star0, massPi_p)
        thetaDstar0, phiDstar0 = pDstar0.theta(), pDstar0.phi()
        axis = np.cross(pDstar0.get_r(), [0, 0, 1])
        angle = -np.arcsin(np.linalg.norm(axis)/pDstar0.get_rlength())

        # this is spin 1 decay
        pD0, pPi0 = restSpinDecay(massD_star0, massD_0, massPi_0)
        roteMatrix = pD0.rotate_by_axis(axis, angle)
        print(pD0.v)
        pPi0.rotate_by_matrix(roteMatrix)
        pD0.boost(PtoV(pDstar0))
        pPi0.boost(PtoV(pDstar0))

        pK_m, pPi_p2 = restSpinLessDecay(massD_0, massK_m, massPi_p)
        pK_m.boost(PtoV(pD0))
        pPi_p2.boost(PtoV(pD0))

        pGamma1, pGamma2 = restSpinLessDecay(massPi_0, 0, 0)
        pGamma1.boost(PtoV(pPi0))
        pGamma2.boost(PtoV(pPi0))

        output.append([pPi_p1, pK_m, pPi_p2, pGamma1, pGamma2])

    with open('data.pik', 'wb') as File:
        pickle.dump(output, File)
