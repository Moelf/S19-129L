import numpy as np

# function we're interested in, return 0 if MC walks out of range


def p(x, y):
    if (x_i <= x <= x_f) and (y_i <= y <= y_f):
        return (x+y)/7
    else:
        return 0.0


def g(x, y): return 7*(x+2*y)


def proposal_accept(x1, y1, x2, y2):
    """
    accept according to the r probability
    """
    r = min(1, p(x2, y2)/p(x1, y1))
    return (np.random.rand() <= r)  # this has probability r to be true


# length of chain
N = 100*1000
# x1, y1
x = np.random.uniform(0, 1)
y = np.random.uniform(2, 4)
# use uniform distribution in MC steps
delta = 0.5

# set limits of integral
x_i = 0
x_f = 1
y_i = 2
y_f = 4

burn_in = 0.1

# first element no use since gonna burn-in anyway
MC_chain = []
for _ in range(0, N):
    x_prime = np.random.uniform(x-delta, x+delta)  # get proposal
    y_prime = np.random.uniform(y-delta, y+delta)
    if proposal_accept(x, y, x_prime, y_prime):  # check, replace x,y if true
        x, y = x_prime, y_prime
    else:
        pass
    MC_chain.append([x, y])  # add x1 or x2 depends on validation result

MC_chain = np.array(MC_chain[int(burn_in*len(MC_chain)):])  # burn-in 10%
N = len(MC_chain)

# because p(x,y) and area info are encoded in the Markov chain
# we simply plug into g(x,y) and take average to get integral
integral = np.sum(g(MC_chain[:, 0], MC_chain[:, 1])) / N  # vectorize faster
print("Using %d Markov Chain points after burn-in, \
we find the integral is: %.3f" % (N, integral))
