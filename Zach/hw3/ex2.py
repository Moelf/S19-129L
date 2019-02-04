#!/usr/bin/env python3

def f(x):
	return x**2*(1-x)

def f_prime(x,h):
	return (f(x+h)-f(x))/h

for i in range(2,20):
	print("f'(1) is %.20f for h=10^%.1f" % (f_prime(1,10**-i), -i))
