import math
import numpy as np
from scipy.stats import norm


# signal pdf, mass 155GeV, energy resolution 5GeV
def s_pdf(x):
    return norm.pdf(x, 155, 5)


# exponential falling background of a*exp(-b*mass)
def b_pdf1(a, mass):
    integration = 1/a * (math.exp(-100*a) - math.exp(-200*a))
    return math.exp(-a*mass) / integration


# power law falling background of a*mass^(-b)
def b_pdf2(a, b, mass):
    integration = a/(-b+1) * (200**(-b+1) - 100**(-b+1))
    return a*mass**(-b) / integration


# a non-sense background of a*mass + b, at least need truncation but who cares
def b_pdf3(a, b, mass):
    integration = a/2 * 200**2 + 200 * b - a/2 * 100**2 - 100 * b
    return a*mass + b / integration

def NLL1(S, B, a):
    global measured
    temp = [math.log(S*s_pdf(mass) + B*b_pdf1(a, mass))
            for mass in measured]
    nll = S+B - sum(temp)
    return nll


def NLL2(S, B, a, b):
    global measured
    temp = [math.log(S*s_pdf(mass) + B*b_pdf2(a, b, mass))
            for mass in measured]
    nll = S+B - sum(temp)
    return nll


def NLL3(S, B, a, b):
    global measured
    temp = [math.log(S*s_pdf(mass) + B*b_pdf3(a, b, mass))
            for mass in measured]
    nll = S+B - sum(temp)
    return nll
