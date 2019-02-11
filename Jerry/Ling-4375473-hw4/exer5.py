import math
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# constants given in the problem
N = 5
mu = 3
sigma = 0.5
xs = np.linspace(-3, 15, 1000)
# normal(3,0.5) virtually don't have anything smaller than 0,
# it's 6 sigmas away


# N y's will be drawn from this distribution
def G(N=1): return np.random.normal(mu, sigma, N)


# integrate with MC integral with 1000 samples
def integrand(x, sample=1000):
    y = G(sample)
    return np.sum(np.exp(-x-y) * np.power((x+y), N)) / sample


# set up 100 list of list of y values ( so we have 100 y given the same x)
ys = [[integrand(x) for x in xs] for _ in range(0, 100)]

# plot all y values overlapping
for y in ys:
    plt.scatter(xs, y,  s=0.5, marker='.', alpha=0.5)
plt.title("100 MC integrali bands")
plt.xlabel("x")
plt.ylabel("$f(x)$")
plt.show()
