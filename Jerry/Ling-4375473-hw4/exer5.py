import math
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

N = 5
mu = 3
sigma = 0.5
xs = np.linspace(-3, 15, 1000)
# we notice normal(3,0.5) don't have anything smaller than 0, 6 sigmas away


def G(N=1): return np.random.normal(mu, sigma, N)


def integrand(x, sample=100):
    y = G(sample)
    return np.sum(np.exp(-x-y) * np.power((x+y), N)) / sample


ys = [integrand(x) for x in xs]

plt.scatter(xs, ys)
plt.show()
