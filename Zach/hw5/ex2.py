#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


xpix=640
ypix=400

xc=int(xpix/2)
yc=int(ypix/2)

a=-.79
b=.56
c=complex(a,b)

def f(z):
	return z**2+c

temp=np.zeros((xpix,ypix))
for ix in range(xpix):
	for iy in range(ypix):
		n=0.0
		n_max=255.0
		while ix**2+iy**2<2 and n<n_max:
			tempe=ix**2-iy**2
			ix=tempe+a
			iy=iy=2*ix*iy+b
			n=n+1.0
		temp[int(ix),int(iy)]=n
			
print(temp)
