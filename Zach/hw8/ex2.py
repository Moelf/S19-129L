#!/usr/bin/env python3

import pickle
from math import pi
import numpy as np
import matplotlib.pyplot as plt
from LVector import LVector as Lv
import scipy.stats as st

# mass constants in GeV
massB_p = 5.28
massD_star0 = 2.01
massD_0 = 1.86
massK_m = 0.494
massPi_p = 0.1396
massPi_0 = 0.1350

np.random.seed(12345)

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

#class wigner_pdf(st.rv_continuous):
#	def _pdf(self,x):
#		return (3/2)*x**2
#my_cv = wigner_pdf(a=-1,b=1, name='wigner_pdf')



def randomSpinTheta():
	R = np.random.rand()
	theta = np.arccos(R**(1/3) )
	if np.random.rand() < .5:
		return -theta + pi/2
	else:
		return theta + pi/2
	#return my_cv.rvs()

"""
y = np.zeros(500)
for i in range(len(y)):
	y[i] = randomSpinTheta()
plt.hist(y)
plt.show()
"""



# calculate the first component of 4-vector E
def EoverC(p, m):
    res = np.sqrt(np.dot(p, p) + m**2)
    return res


# get a 3 velocity a 4-momentum, for boost
def PtoV(p):
    p3 = p.get_r()  #p[1:]
    v  = p3/p.v[0]            #p3/float(p[0])
    return v


# 3 Momentum of either particle in a rest frame decay
def restDecayMomentum(M, m1, m2):
    return np.sqrt((M**2 - (m1+m2)**2) * (M**2 - (m1-m2)**2))/(2*M)


# if A is moving and A -> B + C
# v1 is 3-velocity of A in lab frame, v2 is 3-velocity of B or C in A's frame
def decayAngle(v1, v2):
    denom = np.sqrt(np.dot(v1, v1) * np.dot(v2, v2))
    return np.arccos(np.dot(v1, v2) / denom)


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
    theta1, phi1 = randomSpinTheta(), randomPhi()
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
        """
        ###Testing###
        test = Lv([5,1,2,3])
        r = Lv.get_r(test)
        axis = np.cross([0,0,1],r)
        theta = Lv.theta(test)
        test.rotate_by_axis(axis,-theta)
        print(test, r, axis, theta)
        """
        # first decay
        pDstar0, pPi_p1 = restSpinLessDecay(massB_p, massD_star0, massPi_p)
        #theta = pDstar0.theta()
        axis = np.cross([0,0,1],Lv.get_r(pDstar0))
        theta = np.arcsin(np.linalg.norm(axis)/pDstar0.get_rlength() )		
        # second decay
        pD0, pPi0 = restSpinDecay(massD_star0, massD_0, massPi_0)
        rot_mat = pD0.rotate_by_axis(axis,-1*theta)
        test_pDstar0 = pDstar0
        test_pDstar0.rotate_by_matrix(rot_mat)
        print(test_pDstar0)
        pPi0.rotate_by_matrix(rot_mat)
        pD0.boost(PtoV(pDstar0))
        pPi0.boost(PtoV(pDstar0))

        # third decay
        pK_m, pPi_p2 = restSpinLessDecay(massD_0, massK_m, massPi_p)
        pK_m.boost(PtoV(pD0))
        pPi_p2.boost(PtoV(pD0))

        # fourth decay
        pGamma1, pGamma2 = restSpinLessDecay(massPi_0, 0, 0)
        pGamma1.boost(PtoV(pPi0))
        pGamma2.boost(PtoV(pPi0))

        output.append([pPi_p1, pK_m, pPi_p2, pGamma1, pGamma2])

    with open('data.pik', 'wb') as File:
        pickle.dump(output, File)

