#!/usr/bin/env python3

while True:
	try:
		num=int(input("Input an integer: "))
		break
	except ValueError:
		print("Please input a valid integer")
		continue

print(num**2)

