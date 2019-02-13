import math
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# constants given in the problem
N = 5
mu = 3
sigma = 0.5
# pick 100 spaced fixed x's
xs = np.linspace(-3, 15, 100)


# normal(3,0.5) virtually don't have anything smaller than 0,
# it's 6 sigmas away
# N y's will be drawn from this distribution
def G(N=1): return np.random.normal(mu, sigma, N)


# integrate with MC integral with 1000 samples at given x
def integrand(x, sample=1000):
    y = G(sample)
    return np.sum(np.exp(-x-y) * np.power((x+y), N)) / sample


# set up 100 list of list of y values ( so we have 100 y at the each fixed x)
ys = [[integrand(x) for x in xs] for _ in range(0, 100)]

# plot all y values overlapping
for y in ys:
    plt.scatter(xs, y,  marker='.')
plt.title("100 MC integral bands")
plt.xlabel("x")
plt.ylabel("$f(x)$")
plt.xlim(-4, 15)
plt.ylim(-3, 23)
plt.show()
