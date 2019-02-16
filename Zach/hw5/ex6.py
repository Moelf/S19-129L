#!/usr/bin/env python3

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import squarewave

#Take a time constant as input
tau=-5
while tau<0:
	try:
		tau=float(input("Please pick a time constant: "))
		
	except ValueError:
		print("Please input a valid number ")
		continue

#Defining the differential equation
def V_in(t):
	return squarewave.square(t/2)

def f(t,V_out):
	return (1/tau)*(V_in(t)-V_out)


#Define Runge-Kutta algorithm
def rk(f,t_0,V_out_0,t_f,n):
	t_val = [0] * (n+1)
	V_out_val = [0] * (n+1)
	h = (t_f-t_0)/float(n)
	t_val[0]= t_n = t_0
	V_out_val[0] = V_out_n = V_out_0
	for i in range(1, n+1):
		k_1 = h*f(t_n, V_out_n)
		k_2 = h*f(t_n+h/2, V_out_n+k_1/2)
		k_3 = h*f(t_n+h/2, V_out_n+k_2/2)
		k_4 = h*f(t_n+h, V_out_n+k_3)
		t_val[i]  = t_n = t_0 + i * h
		V_out_val[i] = V_out_n = V_out_n + (1/6)*(k_1+2*k_2+2*k_3+k_4)
	return t_val, V_out_val


t_val, V_out_val = rk(f, 0, 0, 100, 100)

#plt.plot(t_val,V_out_val) #Full plot over interval 0<t<100

plt.plot(t_val[:10], V_out_val[:10], label='Transient Solution')
plt.xlabel('Time (microseconds)')
plt.ylabel('V_out')
plt.title('Transient Solution')
plt.show()



plt.plot(t_val[90:], V_out_val[90:], label='Steady State Solution')
plt.xlabel('Time (microseconds)')
plt.ylabel('V_out')
plt.title('Steady State Solution')
plt.show()
