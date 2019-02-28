import numpy as np
import math

# constants given in the problem
N = int(input("N = "))
mu = int(input("mu = "))
sigma = float(input("sigma = "))
n = 5*10**4

# list of S to scan
Ss = np.linspace(0, max(13, N+np.sqrt(N)), 1200)
# generate a B for each S, out n is large enough
Bs = np.random.normal(mu, sigma, len(Ss))
try:
    Bs = Bs[Bs >= 0][:len(Ss)]
except IndexError:
    print("not enough B's, try again")

# list of len(Ss)=3000 elements, each is an tuple of
# (array of n=10^5 possion pick, S)
S_p_B = [(np.random.poisson(Ss[i]+Bs[i], n), Ss[i]) for i in range(0, len(Ss))]

# initialize a large number as upper limit
smallS = math.inf
n_tail = 0
for tup in reversed(S_p_B):
    # update smallS if less than 5% of n<N
    if sum(tup[0] < N) < (0.05 * len(Ss)):
        n_tail = 0
        smallS = tup[1] if (tup[1] < smallS) else smallS
    else:
        n_tail += 1
        if n_tail >= 80:
            break


print("95% CL excluding signal >= {:.2f}".format(smallS))
