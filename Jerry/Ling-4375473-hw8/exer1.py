import math
# for the juicy speed
from multiprocessing import Pool
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
from ccHistStuff import statBox
from iminuit import Minuit

# data histogram
measured = np.loadtxt("./mass.txt")
binEdges = np.linspace(100, 200, 25)
xs = np.linspace(100, 200, 500)


def s_pdf(x):
    return norm.pdf(x, 155, 5)


# exponential falling background of exp(-a*mass)
def b_pdf0(a, mass):
    integration = 1/a * (math.exp(-100*a) - math.exp(-200*a))
    return math.exp(-a*mass) / integration


# power law falling background of a*mass^(-b)
def b_pdf1(a, b, mass):
    integration = a/(-b+1) * (200**(-b+1) - 100**(-b+1))
    return a*mass**(-b) / integration


# -(x+a)^2 + b*x
# a non-sense quadratic background at least need truncation but who cares
def b_pdf2(a, b, mass):
    integral = -100.0/3 * (3*a**2 + 900*a - 3*b + 70000)
    return (-(mass+a)**2 + b)/integral


def NLL0(S, B, a):
    global measured
    temp = [math.log(S*s_pdf(mass) + B*b_pdf0(a, mass))
            for mass in measured]
    nll = S+B - sum(temp)
    return nll


def NLL1(S, B, a, b):
    global measured
    temp = [math.log(S*s_pdf(mass) + B*b_pdf1(a, b, mass))
            for mass in measured]
    nll = S+B - sum(temp)
    return nll


def NLL2(S, B, a, b):
    global measured
    temp = [math.log(S*s_pdf(mass) + B*b_pdf2(a, b, mass))
            for mass in measured]
    nll = S+B - sum(temp)
    return nll


# appropriate NLLS to minimize
m0 = Minuit(NLL0, S=20., B=180., a=1., errordef=0.5, print_level=0,
            error_S=1.0, error_B=1.0, error_a=0.4)
m1 = Minuit(NLL1, S=20., B=180., a=10., b=2, errordef=0.5, print_level=0,
            error_S=1.0, error_B=1.0, error_a=0.4, error_b=0.1)
m2 = Minuit(NLL2, S=20., B=180., a=155, b=300, print_level=0,
            errordef=0.5, error_S=1.0, error_B=1.0, error_a=0.1, error_b=0.1)

# so hakcy I hate it, if your function can't be pickle serilized
# multiprocessing cannot infer the environment, a work around is to bring
# everything back to global scope
mList = [m0, m1, m2]
all_ys = []


def runm(i):
    global all_ys
    print("Minimization # {} started.".format(i+1))
    fmin, param = mList[i].migrad()
    mList[i].minos()
    print("Minimization # {} finished.".format(i+1))

    S, S_error = param[0]['value'], param[0]['error']
    B = param[1]['value']
    arguments = [x['value'] for x in param[2:]]
    if i == 0:
        ys = [(S*s_pdf(x) + B*b_pdf0(x, arguments[0])) for x in xs]
    elif i == 1:
        ys = [(S*s_pdf(x) + B*b_pdf1(x, arguments[0], arguments[1])) for x in xs]
    elif i == 2:
        ys = [(S*s_pdf(x) + B*b_pdf2(x, arguments[0], arguments[1])) for x in xs]
    return ys


pool = Pool(processes=3)
all_ys.append(pool.map(runm, [0,1,2]))
all_ys = np.array(all_ys)
print(np.shape(all_ys))
# xxx, yyy, _ = m1.mnprofile('S', subtract_min=True, bins=25, bound=(0, 25))

# fig3, ax3 = plt.subplots()
# ax3.plot(xxx, yyy, linestyle='solid', color='b')
# ax3.set_xlim(min(xxx), max(xxx))
# ax3.set_ylim(0.)
# ax3.set_xlabel('S')
# ax3.set_ylabel('deltaNLL')
# ax3.plot([min(xxx), max(xxx)], [0.5, 0.5], linestyle='dashed', color='red')
# ax3.plot([min(xxx), max(xxx)], [2.0, 2.0], linestyle='dashed', color='red')
# ax3.plot([min(xxx), max(xxx)], [4.5, 4.5], linestyle='dashed', color='red')
# # fig3.show()
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
