#!/usr/bin/env python3

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import special

N=100000
np.random.seed(123456)

def g(a,b):
	return 1/math.sqrt(1-math.sin(a/2)**2*math.sin(b)**2)

a_values=np.linspace(1,90,1000)
f_values=[]

for a in a_values:
	
	b_values=np.random.uniform(0,math.pi/2,1000)
	g_values=[]
	for b in b_values:
		g_values.append(g(math.radians(a),b))
	f_values.append(np.mean(g_values))



ell=[]
for a in a_values:
	val=(2/math.pi)*special.ellipk(math.sin(math.radians(a/2))**2)
	ell.append(val)

plt.plot(a_values,f_values,'.',label='Calculated Values')
plt.plot(a_values,ell,label='Exact Values Using Elliptical Integral')
plt.xlabel('Alpha')
plt.ylabel('T Ratio')
plt.legend()

plt.show()
