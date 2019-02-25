import math
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# constants given in the problem
N = int(input("N = "))
mu = int(input("mu = "))
sigma = float(input("sigma = "))
# pick 100 spaced fixed x's, S>0
xs = np.linspace(0, 20, 2000)


# normal(3,0.5) virtually don't have anything smaller than 0,
# it's 6 sigmas away
# N y's will be drawn from this distribution
def G(n): return np.random.normal(mu, sigma, n)


# integrate with MC integral with 1000 samples at given x
def integrand(x, sample=1500):
    y = G(sample)
    return np.sum(np.exp(-x-y) * np.power((x+y), N)) / sample


# set up 100 list of list of y values ( so we have 100 y at the each fixed x)
ys = [integrand(x) for x in xs]
# notmalization
integral = np.trapz(ys, xs)
ubound = 0
for i in range(1, len(ys)):
    # find from the TAIL till are > 5% of integral
    if np.trapz(ys[-i:], xs[-i:]) > 0.05*integral:
        ubound = -i
        print("We are excluding S > {:.2f}, at 95% CL".format(xs[-i]))
        break


# plot all y values overlapping
plt.scatter(xs, ys,  marker='.', label="pdf")


plt.title("MC integral bands")
plt.xlabel("x")
plt.ylim(bottom=0)
plt.ylabel("$f(x) = \int_0^{\infty} exp(-x-y)\cdot (x+y)^N$")
plt.fill_between(xs[ubound:], 0, ys[ubound:],
                 label="5 % integral", color="green")
plt.legend()
plt.show()
