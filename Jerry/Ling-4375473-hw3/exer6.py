import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
fig, ax = plt.subplots()

step = np.array([[0,1],[0,-1],[1,0],[-1,0]])
moves = [step[x] for x in np.random.randint(0,4,1000)]
posList = [[0,0]]

for i in range(0,1000):
    posList.append(np.add(posList[-1], moves[i]))

x = [n[0] for n in posList]
y = [n[1] for n in posList]
line, = ax.plot(x[0], y[1])

def init():
    line.set_ydata([np.nan] * len(posList[0]))
    return line,


def animate(i):
    line, = ax.plot(x[0:i], y[0:i],"red")
    return line,
ani = animation.FuncAnimation(
    fig, animate, init_func=init, interval=3, blit=True, save_count=5000)

plt.xlim(-25,25)
plt.ylim(-25,25)
plt.title("2-D Random Walk")
plt.show()
