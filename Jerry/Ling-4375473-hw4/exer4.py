import numpy as np

p = lambda x,y: (x+y)/7
g = lambda x,y: 7*(x+2*y)
f = lambda x,y: p(x,y)*g(x,y)

scale = 45
x_i = 0
x_f = 1
y_i = 2
y_f = 4
area = (x_f - x_i) * (y_f - y_i)
N = 100*1000

x = np.random.uniform(x_i,x_f, N)
y = np.random.uniform(y_i,y_f, N)
z = np.random.uniform(0,scale, N)


integral = np.sum(z < f(x, y)) / N * area * scale


print("Using %d MC points, we find the integral is: %f" % (N,integral))
