#!/usr/bin/env python3

import pickle
import numpy as np
from LVector import LVector as lv
from math import pi

# Initialize constants
massB_p  = 5.28
massD_s0 = 2.01
massD_0  = 1.86
massK_m  = 0.494
masspi_p = 0.1396
masspi_0 = 0.1350
mass_ph  = 0.0

def randomphi():
	return np.random.uniform(0,2*pi)
def randomtheta():
	v = np.random.rand()
	return np.arccos(2*v - 1)
def sphtocart(phi,theta):
	x = np.sin(theta) * np.cos(phi)
	y = np.sin(theta) * np.sin(phi)
	z = np.cos(theta)
	return np.array([x,y,z])
