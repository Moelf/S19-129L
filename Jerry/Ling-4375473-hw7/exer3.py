import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from ccHistStuff import statBox

# change to nrows=3 if want to compare to average approach
fig, ax = plt.subplots(nrows=2)
# introduce text data set
# this has shape (1000,10)
raw = np.array(np.loadtxt("./straightTracks.txt"))
# x positions of pixel layer in cm
layer_x = np.array([2, 3, 5, 7], dtype=float)


# a 3-parameter function describe our 2 lines
def lines(x, s1, s2, c):
    # c is the x-intersect
    lineone = s1*(x[:4] - c)
    linetwo = s2*(x[4:] - c)
    res = np.hstack([lineone, linetwo])
    return res


# set up histogram array
histConst = np.empty(len(raw))
histPull = np.empty(len(raw))
histXav = np.empty(len(raw))

xStack = np.hstack([layer_x, layer_x])
for i, data in enumerate(raw):
    # position in the length 10 line
    # truth information we are assessing against
    X0 = data[0]

    # skip X0 Y0
    yStack = data[2:]
    ytrack1 = yStack[:4]
    ytrack2 = yStack[4:]

    popt, pcov = curve_fit(lines, xStack, yStack, method='trf')
    x_intercept = popt[2]
    diff = x_intercept - X0
    histConst[i] = diff

    # the covariant matrix pcov correspont is 3x3 (remember index are 0,1,2)
    # it's a covariant matrix so we want the element 2,2 of it
    # print(pcov[2][2])
    pull = diff/np.sqrt(pcov[2][2])
    histPull[i] = pull

    # these 4 are from exer1
    # for comparison
    X1 = np.polyfit(layer_x, ytrack1, 1)[1]
    X2 = np.polyfit(layer_x, ytrack2, 1)[1]
    Xav = (X1+X2)/2 - X0
    histXav[i] = Xav

# convert units to micrometer
histConst *= 10**4
# histPull *= 10**4
histXav *= 10**4

# set up bins and scale after observation
binEdges = np.linspace(-500, 500, 100)
ax[0].hist(histConst, bins=binEdges, align="left",
           label="Constrained fit")
statBox(ax[0], histConst, binEdges, name="Constrain")
ax[0].set_title("X0 - Xf with constrain")
ax[0].set(xlabel="$\Delta$ X ($\mu m$)")
# ax[1].hist(histPull, bins=binEdges, log=True, align="left")
pullbinEdges = np.linspace(-5, 5, 100)
ax[1].hist(histPull, bins=pullbinEdges, log=True, align="left")
ax[1].set_title("Pull of constrained fit")
ax[1].set(xlabel="$\Delta$ X ($\mu m$)")

# ----------------un-comment and change line 7 to compare to average method ---
# ax[2].hist(histXav, bins=binEdges, align="left")
# ax[2].set_title("Xav - X0")
# # label everything
# ax[2].set(xlabel="$\Delta$ X ($\mu m$)")
# # add claudio's box
# statBox(ax[2], histXav, binEdges, name="Average")
# ----------------un-comment to compare to average method ---------------------

# maxmize window, comment out if causing issue
mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
plt.show()
