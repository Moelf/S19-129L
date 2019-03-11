import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from ccHistStuff import statBox


fig, ax = plt.subplots(nrows=2)
# import text data set
# this has shape (1000,10)
raw = np.array(np.loadtxt("./straightTracks.txt"))
# x positions of pixel layer
layer_x = np.array([2, 3, 5, 7], dtype=float)


def line(x, a, b):
    return (x-a)*b


# set up array
histX1X0 = np.empty(len(raw))
histX2X0 = np.empty(len(raw))
histXav = np.empty(len(raw))
for i, data in enumerate(raw):
    # position in the length 10 line
    ytrack1 = data[2:6]
    ytrack2 = data[6:]
    X0 = data[0]

    # ptop is the [a,b] parameter
    ptop1, pcov1 = curve_fit(line, layer_x, ytrack1, method="trf")
    ptop2, pcov2 = curve_fit(line, layer_x, ytrack2, method="trf")
    X1, X2 = ptop1[0], ptop2[0]
    Xav = (X1+X2)/2 - X0

    histX1X0[i] = X1-X0
    histX2X0[i] = X2-X0
    histXav[i] = Xav

# convert to micrometer
histX1X0 *= 10**4
histX2X0 *= 10**4
histXav *= 10**4

# set up bins and scale after observation
binEdges = np.linspace(-500, 500, 100)
ax[0].hist([histX1X0, histX2X0], bins=binEdges,
           align="left", label=["X1X0", "X2X0"])
ax[0].legend(loc="upper left")
ax[1].hist(histXav, bins=binEdges, align="left")
# label everything
ax[0].set_title("(X1 or X2) - X0")
ax[1].set_title("Xav - X0")
ax[0].set(xlabel="$\Delta$ X ($\mu m$)")
ax[1].set(xlabel="$\Delta$ X ($\mu m$)")
# add claudio's box
statBox(ax[0], histX1X0, binEdges, name="X1X0")
statBox(ax[0], histX2X0, binEdges, name="X2X0", y_shift=-0.3)
statBox(ax[1], histXav, binEdges)

# maxmize window
mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
plt.show()
