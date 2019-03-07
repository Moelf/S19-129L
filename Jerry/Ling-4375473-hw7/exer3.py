import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from ccHistStuff import statBox


fig, ax = plt.subplots(nrows=2)
# introduce binary data set
# this has shape (1000,10)
raw = np.array(np.loadtxt("./straightTracks.txt"))
# x positions of pixel layer
layer_x = np.array([2, 3, 5, 7], dtype=float)


# a 3 parameter function describe our 2 lines
def lines(x, s1, s2, c):
    # c is the x-intersect
    lineone = s1*(x[:4] - c)
    linetwo = s2*(x[4:] - c)
    res = np.hstack([lineone, linetwo])
    return res


# set up array
histConst = np.empty(len(raw))
histXav = np.empty(len(raw))
for i, data in enumerate(raw):
    # position in the length 10 line
    ytrack1 = data[2:6]
    ytrack2 = data[6:]
    X0 = data[0]

    xStack = np.hstack([layer_x, layer_x])
    # print(np.shape(xStack))
    yStack = np.hstack([ytrack1, ytrack2])
    # print(np.shape(yStack))

    popt, pcov = curve_fit(lines, xStack, yStack, method='trf')
    x_intercept = popt[2]
    diff = x_intercept - X0
    histConst[i] = diff

    # these 4 are from exer1
    # for comparison
    X1 = np.polyfit(layer_x, ytrack1, 1)[1]
    X2 = np.polyfit(layer_x, ytrack2, 1)[1]
    Xav = (X1+X2)/2 - X0
    histXav[i] = Xav

# convert units to micrometer
histConst *= 10**4
histXav *= 10**4

# set up bins and scale after observation
binEdges = np.linspace(-500, 500, 100)
ax[0].hist(histConst, bins=binEdges, align="left",
           label="Constrained fit")
# ax[0].legend(loc="upper left")
ax[1].hist(histXav, bins=binEdges, align="left")
# label everything
ax[0].set_title("X0 - Xf with constrain")
ax[1].set_title("Xav - X0")
ax[0].set(xlabel="$\Delta$ X ($\mu m$)")
ax[1].set(xlabel="$\Delta$ X ($\mu m$)")
# add claudio's box
statBox(ax[0], histConst, binEdges, name="Constrain")
# statBox(ax[0], histX2X0, binEdges, name="X2X0", y_shift=-0.3)
statBox(ax[1], histXav, binEdges, name="Average")

# maxmize window
mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
plt.show()
