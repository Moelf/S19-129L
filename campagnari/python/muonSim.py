#!/usr/bin/env python3
#
# Plot the muon transverse momentum for
# a semi-realistic MC simulation of
# pp -> W -> mu nu
#
# CC 1-Feb-2019
# CC 4-Feb-2019 fixed typos in comments
#-------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import math
import ccHistStuff as cc

#------------------------------------------------------
def BreitWigner(m, m0, G):
    """
    Relativistic Breit Wigner for mass=m
    central value m0, width G
    The normalization is arbitrary
    """
    return 1./( (m*m - m0*m0)*(m*m - m0*m0) + m*m*G*G)
#------------------------------------------------------

#------------------------------------------------------
def getBW(mass, gamma, minMass, maxMass, n=1):
    """
    Pick from relativistic Breit Wigner
    between minMass and MaxMass
    n = number to return in np.array
    Use Accept/Reject method
    """
    # maximum of BW (allow for mass not in the interval)
    bwmax   = max(BreitWigner(minMass, mass, gamma),
                      BreitWigner(maxMass, mass, gamma),
                      BreitWigner(mass, mass, gamma))

    out  = np.array( [] )
    ntot = 0
    while ntot<n:
        x       = minMass + (maxMass-minMass) * np.random.rand(n-ntot)
        y       = BreitWigner(x, mass, gamma)
        yrand   = bwmax * np.random.rand(n-ntot)
        xgood   = x[y>yrand] 
        out     = np.append(out, xgood)
        ntot    = len(out)

    return out
#------------------------------------------------------

def pickCosTheta(n=1):
    """
    Pick cosTheta accoding to 1+cos^2
    n = number to return in np.array
    Note: if the order is important this series 
    will need to be shuffled
    """
    # The normalized pdf between -1 and 1 is
    # f(x)dx = 3/8 (1 +x^2)
    # The cumulative PDF would be
    # F(x)dx = 3/8 (x + x^3/3 + 4/3)
    # The direct method would require solving a
    # cubic F(x) = R which is ugly.
    # We could use acceptance/rejection
    # Instead notice that f(x) is the sum of
    # a flat pdf with probability 3/4
    # and g(x)dx = 3/2 x^2 with prob 1/4
    # Picking according to g(x) is easy.
    # The cumulative is 
    #  G(x) = 1/2 (x^3 + 1)
    #  G(x) = R  --->   x = (2R-1)^(1/3)
    #
    # Pick on average n1=3n/4 flat and n2=n/4 according to x^2
    # Careful about truncation.... crucial when n is small
    # Use np.cbrt(blah) instead of blah**(1/3) because the
    # latter returns a complex number when blah is negative
    s   = 0.5*np.random.rand()  # flat between 0 and 0.5
    n1  = int(3.*n/4. + s)
    n2  = n - n1
    x1  = -1 + 2*np.random.rand(n1)
    x2  = np.cbrt(2*np.random.rand(n2)-1)
    out = np.append(x1,x2)
    return out

def pickQt(qTmax, n=1):
    """
    pick n values according to
    f(x) = x*e-(x/25) / (x^2 + 25)
    between 0 and qTmax
    """
    def thisF(x):
        return x*np.exp(-x/25.) / (x*x + 25.)

    fmax = 0.09  #  close enough, it's a bit > than the max, I am lazy
    out  = np.array( [] )
    ntot = 0
    while ntot<n:
        x       = qTmax * np.random.rand(n-ntot)
        y       = thisF(x)
        yrand   = fmax * np.random.rand(n-ntot)
        xgood   = x[y>yrand] 
        out     = np.append(out, xgood)
        ntot    = len(out)

    return out
    
# initialize random number
np.random.seed(12345)

# parameters
N     = 10000   # numbers to generate
MW    = 80.4    # W mass
Gamma = 2.2     # W width
minM  = MW - 6*Gamma
maxM  = MW + 6*Gamma
qtMax = 30.    # maximum pt that give the W
ptRes = 0.015  # pt resolution (1.5%)

# Parameters in the rest frame
mass   = getBW(MW, Gamma, minM, maxM, N)
cTheta = pickCosTheta(N)
sTheta = np.sqrt(1 - cTheta*cTheta)
phi    = 2*math.pi*np.random.rand()
px     = 0.5 * mass * sTheta * np.cos(phi)
py     = 0.5 * mass * sTheta * np.sin(phi)

# the W pt...we assume that it is along the x axis
qt = pickQt(qtMax, N)

# the boost to the LAB frame
betaGamma = qt/mass
gamma      = np.sqrt(qt*qt + mass*mass) / mass
pxnew      = gamma*px + betaGamma * (0.5 * mass)

# the pt in the LAB
ptLab = np.sqrt(pxnew*pxnew + py*py)

# apply the resolution for th emeasurement in the LAB
ptMeasured = ptLab * np.random.normal(1.0, ptRes)

# sanity checks that the more complicated picks make sense...
fig, ax = plt.subplots(2,2)
axm = ax[0][0]
axc = ax[0][1]
axq = ax[1][0]
contMass, bm, _ = axm.hist(mass,   np.linspace(minM,maxM,101), histtype='step')
contCos,  bc, _ = axc.hist(cTheta, np.linspace(-1,1,101), histtype='step')
contQt,   bq, _ = axq.hist(qt,     np.linspace(0,qtMax,101), histtype='step')
cc.statBox(axm, mass,     bm, fontsize='x-small')
cc.statBox(axc, cTheta,   bc, fontsize='x-small')
cc.statBox(axq, qt ,      bq, fontsize='x-small')
fig.show()
input("Press any key to continue: ")

# and now the final plot!!!!!
fig2, ax2 = plt.subplots()
contents, bins, _ = ax2.hist(ptMeasured, np.linspace(20.,70.,101),
                                 histtype='step')
cc.statBox(ax2, ptMeasured, bins)
ax2.set_xlim(bins[0], bins[-1])
ax2.tick_params("both", direction='in', length=10, right=True)
fig2.show()
input("Press any key to continue: ")
