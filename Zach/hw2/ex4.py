#!/usr/bin/env python3

for i in range(100,401):
	evens=len([n for n in str(i) if int(n) % 2 == 0]) #Counts number of even digits
	if evens==len(str(i)):                            #Checks if all digits are even
		print(i)
	else:
		continue
