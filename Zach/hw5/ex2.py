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

pixColor=np.zeros( (xpix,ypix), dtype='uint8')

temp=np.zeros((xpix,ypix))

for ix in range(xpix):
	x=(ix-xc)/200
	for iy in range(ypix):
		y=(iy-yc)/200
		n=0.0
		n_max=255.0
		while x**2+y**2<2 and n<n_max:
			tempe=x**2-y**2
			ix=tempe+a
			iy=2*x*y+b
			n=n+1.0
		print(n)
			
#print(temp)
