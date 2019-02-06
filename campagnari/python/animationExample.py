#!/usr/bin/env python3

"""
A simple example of an animated plot
Stolen from
https://matplotlib.org/examples/animation/simple_anim.html
with som modifications by CC as noted
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)

# CC: commented out from the web example which was not quite
# working, at least on the MAC
#line, = ax.plot(x, np.sin(x))

# Added by CC
plt.axis( [0, 2*np.pi, -1.1, 1.1] )
line, = ax.plot(x, 10+np.sin(x))   # an initial "line" way off the screen

# CC comment: Note that line and x are "global variables"
# ie variables that are defined in the main program but
# also accessed by the function.
# This is the simplest way to do this, even though
# global variables are "evil"
# See https://matplotlib.org/api/animation_api.html
def animate(i):
    line.set_ydata(np.sin(x + i/10.0))  # update the data
    return line ,

# Init only required for blitting to give a clean slate.
# CC: blitting...see
# gamedevelopment.tutsplus.com/articles/gamedev-glossary-what-is-blitting--gamedev-2247
def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line ,

ani = animation.FuncAnimation(fig, animate, np.arange(1, 200),
                              init_func=init,
                              interval=25, blit=True, repeat=False)

# Commented out by CC
#plt.show()

# Added by CC
fig.show()
print("\n \n \n")
input("Enter CR to quit:")
