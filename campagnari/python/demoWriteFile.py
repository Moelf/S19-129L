#!/usr/bin/env python3

f = open("newFile.txt", "w")

# need rge end of line to go to next line
f.write("blah")
f.write(" blah again \n")
f.write("A new line \n")

# example of formatted writing (j, x, t) is a tuple
j = 36
x = 34.12
t = "blah"
f.write("An integer %d then a float %f then a string %s \n" % (j, x, t))

# I could stich my variables into a string instead.
# Then I can do anything I want with the string...
# including writing it to the file
u =  "A float %f" % x
f.write(u + "\n")

# Here is how I could control the floating format
u =  "A float with 8 decimal digits %.8f" % x   # 8 decimal digits
f.write(u + "\n")

# Fixed width of 9 with 3 decimal digits
x = 34.12
y = 1289.98
u =  "A float width 9 %9.3f" % x   
v =  "A float width 9 %9.3f" % y   
f.write(u + "\n" + v + "\n")

# And now exponential
f.write("Exponential = %e" % y)

# And there are many more ways of controling the output
# Note: this is the "old-style" formatting.
# The "new style" uses the string.format(...) syntax


f.close()
