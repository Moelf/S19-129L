import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from ccHistStuff import statBox
from iminuit import Minuit
# Flag to include/exclude the systematics
# on the background shape
shapeSyst = False


measured = np.loadtxt("./mass.txt")
binEdges = np.linspace(100,200,25)


def s_pdf(x):
    return norm(155, 5).pdf(x)

# assume our falling background is a*exp(-b*mass)


def b_pdf1(a, b, mass):
    integration = a/b * (math.exp(-100*b) - math.exp(-200*b))
    return a * math.exp(-b*mass) / integration


def NLL(S, B, a, b):
    global measured
    # alpha=0  ---> use b_pdf
    # alpha=1  ---> use b1_pdf
    # alpha=-1 ---> use b2_pdf
    # (and smoothly interpolates vs. alpha)
    new_b_pdf = b_pdf1
    # if alpha > 0:
    #     new_b_pdf = b_pdf + alpha*(b1_pdf-b_pdf)
    # else:
    #     new_b_pdf = b_pdf - alpha*(b2_pdf-b_pdf)
    # should be already normalized, but make sure
    temp = [math.log(S*s_pdf(mass) + B*new_b_pdf(a, b, mass))
            for mass in measured]
    nll = S+B - sum(temp)
    return nll


m = Minuit(NLL, S=20., B=180., a=1., b=1., print_level=1,
           errordef=0.5, error_S=1.0, error_B=1.0, error_a=0.1, error_b=0.1,
           fix_a=(not shapeSyst))
m.migrad()
m.minos()

xxx, yyy, _ = m.mnprofile('S', subtract_min=True, bins=25, bound=(0, 25))

fig3, ax3 = plt.subplots()
ax3.plot(xxx, yyy, linestyle='solid', color='b')
ax3.set_xlim(min(xxx), max(xxx))
ax3.set_ylim(0.)
ax3.set_xlabel('S')
ax3.set_ylabel('deltaNLL')
ax3.plot([min(xxx), max(xxx)], [0.5, 0.5], linestyle='dashed', color='red')
ax3.plot([min(xxx), max(xxx)], [2.0, 2.0], linestyle='dashed', color='red')
ax3.plot([min(xxx), max(xxx)], [4.5, 4.5], linestyle='dashed', color='red')
# fig3.show()
# import binary data set
# set up bins and scale after observation
fig, ax = plt.subplots()
ax.hist(measured, bins=binEdges, align="left", histtype="step")
# label everything
plt.xlabel("Value")
plt.ylabel("Events count")
# add claudio's box
statBox(ax, measured, binEdges)
plt.title("Extraction of text file containing $e^+ e^-$ invar mass")
plt.show()
