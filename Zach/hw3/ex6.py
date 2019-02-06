#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax=plt.subplots()
np.random.seed(12345)

position=[[0,0]]
step=np.array([[1,0],[-1,0],[0,1],[0,-1]])

steps=[step[i] for i in np.random.randint(0,4,1000)]

for j in range(0,1000):
	position.append(np.add(steps[j],position[-1]))
	
x=[k[0] for k in position]
y=[k[1] for k in position]

line, =ax.plot(x[0],y[0])

def animate(i):
	line,=ax.plot(x[0:i], y[0:i])
	return line,
	
ani=animation.FuncAnimation(fig,animate,interval=5)

plt.show()