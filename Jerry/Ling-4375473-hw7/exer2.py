import numpy as np
import matplotlib.pyplot as plt
from ccHistStuff import statBox


def getChisq(y0, y, e2):
    return ((y-y0)*(y-y0)/e2).sum()
# fitting function
def f(x, p):
    return p[0]*np.exp(-p[1]*x)
def dydp(i, p, x):
    temp = -p[1]*x
    if i == 0:
        return np.exp(temp)
    elif i == 1:
        return -p[0]*x*np.exp(temp)


fig, ax = plt.subplots()
# import binary data set
raw = np.load("./dataSet.npy")
# set up histogram as desired
# ([counts], [bin edges])
# ((40,),(41))
rawhis = np.histogram(raw, bins=40, range=(0, 20))
# extract y's, sigmas, and x's for fitting
x = np.array([(rawhis[1][i]+rawhis[1][i+1])/2 for i in range(0, 25)])
y = np.array(rawhis[0][:25])
e2 = y
# sigma^2 = N in our case
W = np.diag(1/y)
# some not too wild guess based on shape and starting f(x=0)
p = np.array([8000, 0.6])
y0 = f(x, p)
for _ in range(5):
    At = np.array([dydp(0, p, x), dydp(1, p, x)])  # 2xN matrix
    A = (At.T).copy()                    # Nx2 matrix
    dy = (np.array([(y-y0), ])).T        # Nx1 column vector

    # find the matrix to be inverted, and invert it
    temp = np.matmul(At, W)       # 2xN * NxN = 2xN
    temp2 = np.matmul(temp, A)     # 2xN * Nx2 = 2x2
    temp3 = np.linalg.inv(temp2)   # 2x2 ... this is the covariance matrix

    # multiply again
    temp4 = np.matmul(temp3, At)     # 2x2 * 2xN = 2xN
    temp5 = np.matmul(temp4, W)      # 2xN * NxN = 2xN
    dpar = np.matmul(temp5, dy)     # 2xN * Nx1 = 2x1 column vector

    # the new values of the parameters
    p[0] = p[0] + dpar[0][0]
    p[1] = p[1] + dpar[1][0]

    # update fitted value of y
    y0 = f(x, p)

# set up bins and scale after observation
xs = np.linspace(0, 20, 40)
ax.hist(raw, bins=rawhis[1], log=True, label="Raw data")
fitline, = ax.plot(xs, f(xs, p), c='r', linestyle='-',
                   label="$\chi^2$ fit with first 25 bins")
# label everything
plt.xlabel("Value")
plt.ylabel("Events count")
# add claudio's box
statBox(ax, raw, rawhis[1])
plt.title("Fitting npy file")
plt.legend(loc="upper center")
plt.show()
