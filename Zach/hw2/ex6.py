#!/usr/bin/env python3


try:
	num=int(input("Please input an integer >1: "))
except:
	print("Number invalid, please try again")

i=2
prime_factors=dict()
while i<=num:
	while num%i==0:
		num/=i
		if i in prime_factors.keys():
			prime_factors[i] +=1
		else:
			prime_factors[i] =1
	i+=1

for key in prime_factors.keys():
	print(key, ' to the power ', prime_factors[key])
