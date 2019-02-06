#!/usr/bin/env python3

# a possible way to store first and last names
# the two lists are clearly related
firstName = ['bob',   'maria', 'jen']
lastName  = ['smith', 'suarez', 'yoo']

# here is one way to loop
for i in range(3):
    print(firstName[i], lastName[i])

input("Enter something to continue: ")

# here is another way
i = 0
for f in firstName:
    print(f, lastName[i])
    i = i + 1

input("Enter something to continue: ")

# This way of arranging the data would have probably been smarter
# (a list of lists)
names = [ ['bob',    'smith'],
          ['maria', 'suarez'],
          ['jen',   'yoo']    ]
for n in names:
    print(n)  # but this output is ugly

input("Enter something to continue: ")

for n in names:
    print(n[0], n[1])  # this is nicer

input("Enter something to continue: ")

for n in names:
    print("%s %s" % tuple(n)) # this is compact (but hard to read)

# The print statement above is an example of formatting output.
# I think this is the old fashioned way (?)
# %s means: substitute a string here   (s=string, i=integer, etc)
# the values that get substituted are to be found in a tuple
# The % outside the string indicates that the tuple is following

input("Enter something to continue: ")

# zip "aggregates" iterables and we can iterate
# on more than iterable at the same time

for f, l in zip(firstName, lastName):
    print(f,l)

    
    
