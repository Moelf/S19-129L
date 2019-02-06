#!/usr/bin/env python3
#
# Demo of reading a text a file
#
import sys

# Open file, read one line at a time
# 'r'  --> read
# 'w'  --> write (and overwrite what is there)
# 'a'  --> append
# 'r+' --> read and write (special)
print("First Method: one line at a time")
f = open('testFile.txt', 'r')
line = f.readline()
while line != "":
    l = line.rstrip('\r\n')    # strip end of line stuff
    print(l)
    line = f.readline()
f.close()   # must close the file

blah = input("Enter q to quit:")
if blah == 'q': exit()


# This is more efficient, reads everything at once
print("Second method: everything at once, then loop")
f = open('testFile.txt', 'r')
for line in f:
    l = line.rstrip('\r\n')    # strip end of line stuff
    print(l)
f.close()

blah = input("Enter q to quit:")
if blah == 'q': exit()

# The recommended way of doing it is using "with"
# It will automatically handle the closing
print("Using with is recommended")
with open('testFile.txt', 'r') as f:
    for line in f:
        l = line.rstrip('\r\n')
        print(l)
        
blah = input("Enter q to quit:")
if blah == 'q': exit()


# Read everything into a long string
print("Put everything into a long string")
with open('testFile.txt', 'r') as f:
    lines = f.read()

print(type(lines))
print("The length of the string is ", len(lines))
l = lines.split("\n")
print(l)

