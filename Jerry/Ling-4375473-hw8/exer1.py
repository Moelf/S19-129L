# for the juicy speed
from multiprocessing import Pool
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
from ccHistStuff import statBox
from iminuit import Minuit
# missing a few points doesn't seem to affect fitting
np.seterr(all='ignore')

# ---------------------------------
# Using numpy array in pdf and NLL is mandatory
# results in 10x speed difference
# ---------------------------------

# data histogram
measured = np.loadtxt("./mass.txt")
binEdges = np.linspace(100, 200, 25)
values, histx = np.histogram(measured, bins=binEdges)
# the way binning effects area needs to be accounted
# https://stackoverflow.com/questions/26399291/how-to-get-the-area-under-a-histogram-in-python
histArea = sum(np.diff(histx)*values)

xs = np.linspace(100, 200, 500)


def s_pdf(x):
    return norm.pdf(x, 155, 5)

# exponential falling background of exp(-a*mass)


def b_pdf0(a, mass):
    integration = 1/a * (np.exp(-100*a) - np.exp(-200*a))
    return np.exp(-a*mass) / integration


# power law falling background of a*mass^(-b)
def b_pdf1(a, b, mass):
    integration = a/(-b+1) * (np.power(200, (-b+1)) - np.power(100, (-b+1)))
    return a*np.power(mass, -b) / integration


# -a(x)^2 + bx + c
# a non-sense quadratic background at least need truncation but who cares
def b_pdf2(a, b, c, mass):
    integral = 100/3 * (-70000*a + 450*b + 3*c)
    return (-a*np.power((mass), 2) + b*mass + c)/integral


# corresponding NLL for each b_pdf
def NLL0(S, B, a):
    global measured
    temp = np.log(S*s_pdf(measured) + B*b_pdf0(a, measured))
    nll = S+B - temp.sum()
    return nll


def NLL1(S, B, a, b):
    global measured
    temp = np.log(S*s_pdf(measured) + B*b_pdf1(a, b, measured))
    nll = S+B - temp.sum()
    return nll


def NLL2(S, B, a, b, c):
    global measured
    temp = np.log(S*s_pdf(measured) + B*b_pdf2(a, b, c, measured))
    nll = S+B - temp.sum()
    return nll


# appropriate NLLS to minimize
m0 = Minuit(NLL0, S=20., B=180., a=0.5, errordef=0.5, print_level=0,
            error_S=1.0, error_B=1.0, error_a=0.1)
m1 = Minuit(NLL1, S=20., B=180., a=10., b=2, errordef=0.5, print_level=0,
            error_S=1.0, error_B=1.0, error_a=0.4, error_b=0.1)
m2 = Minuit(NLL2, S=20., B=180., a=0.001, b=-300, c=-30, print_level=0,
            errordef=0.5, error_S=1.0, error_B=1.0, error_a=0.1, error_b=0.1, error_c=0.1)

# so hakcy I hate it, if your function can't be pickle serilized
# multiprocessing cannot infer the environment, a work around is to bring
# everything back to global scope
mList = [m0, m1, m2]
all_ys = []
errs = []


def runm(i):
    global all_ys, xs, scale
    print("Minimization # {} started.".format(i+1))
    fmin, param = mList[i].migrad()
    mList[i].minos()
    print("Minimization # {} finished.".format(i+1))

    S, S_error = param[0]['value'], param[0]['error']
    errs.append(S_error)
    B = param[1]['value']
    arguments = [x['value'] for x in param[2:]]
    if i == 0:
        ys = S*s_pdf(xs) + B*b_pdf0(arguments[0], xs)
    elif i == 1:
        ys = S*s_pdf(xs) + B*b_pdf1(arguments[0], arguments[1], xs)
    elif i == 2:
        ys = S*s_pdf(xs) + B * \
            b_pdf2(arguments[0], arguments[1], arguments[2], xs)
    return ys*histArea/(S+B)


pool = Pool(processes=3)
all_ys = pool.map(runm, [0, 1, 2])
f, ax = plt.subplots(2, 3)
for i in range(3):
    ax[0, i].plot(xs, all_ys[i])
    ax[0, i].hist(measured, bins=binEdges, histtype='step')
    xxx, yyy, _ = mList[i].mnprofile('S', subtract_min=True, bins=25, bound=(0.1, 40))

    ax[1,i].plot(xxx, yyy, linestyle='solid', color='b')
    ax[1,i].set_xlim(min(xxx), max(xxx))
    ax[1,i].set_ylim(0.)
    ax[1,i].set_xlabel('S')
    ax[1,i].set_ylabel('deltaNLL')
    ax[1,i].plot([min(xxx), max(xxx)], [0.5, 0.5], linestyle='dashed', color='red')
    ax[1,i].plot([min(xxx), max(xxx)], [2.0, 2.0], linestyle='dashed', color='red')
    ax[1,i].plot([min(xxx), max(xxx)], [4.5, 4.5], linestyle='dashed', color='red')


# print(np.shape(all_ys))
plt.show()
# # import binary data set
# # set up bins and scale after observation
# fig, ax = plt.subplots()
# ax.hist(measured, bins=binEdges, align="left", histtype="step")
# # label everything
# plt.xlabel("Value")
# plt.ylabel("Events count")
# # add claudio's box
# statBox(ax, measured, binEdges)
# plt.title("Extraction of text file containing $e^+ e^-$ invar mass")
# plt.show()
