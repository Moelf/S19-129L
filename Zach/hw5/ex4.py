#!/usr/bin/env python3

value=-10


#Take user input within valid range of 16 bit integers
while value<0 or value>65535:
	try:
		value=int(input("Please input a valid integer within (0-65535): "))
	except ValueError:
		print("Input invalid, please use a valid number")
		continue

#Takes relevant parts of input
value_binary=bin(value)[2:].zfill(16)

channel=int(value_binary[0:4], 2)
time=int(value_binary[4:8], 2)
pulse_height=int(value_binary[8:16], 2)


print('The channel number is ', channel)
print('The time is ', time)
print('The pulse height is ', pulse_height)
