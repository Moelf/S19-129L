#!/usr/bin/env python3


def f():
    x = 3  # x is now local
    print("x in f ",x)
    print("y in f",y)  # picks up from main but cannot change it
    global z
    print("z in f",z)
    z = 76
    print("z in f after reassignment",z)
    print(" ")
    return 34

    
x = 10
y = 11
z = 12
print("x in main before calling f", x)
print("y in main before calling f", y)
print("z in main before calling f", z)
print(" ")
a = f()
print("x in main after  calling f", x)
print("y in main after  calling f", y)
print("z in main after  calling f", z)
