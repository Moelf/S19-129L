#!/usr/bin/env python3

import math


def f(x):
	return x*math.cos(x)-(1/2)

#Initial lower and upper bounds
x_l= .5
x_u= .8

#Limit interval based on which side of zero we are on
while True:
	x_m=(.5)*(x_l+x_u)
	if f(x_m)*f(x_l)<0.0:
		x_l=x_l
		x_u=x_m
	elif f(x_l)*f(x_m)>0.0:
		x_l=x_m
		x_u=x_u
	else:
		print("The root is %.5f" %x_m)
		break
