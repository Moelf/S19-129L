import numpy as np
import scipy
import matplotlib.pyplot as plt
# ---------------------------------
# A bunch of functions to make
# numpy histograms look better
#
#  CC 27 Jan 2019
# ---------------------------------


def statBox(ax, entries, binEdges, x=0.96, y=0.98, fontsize='medium', name='', y_shift=0):
    """
    Put a stat box on the histogram at coord x and y
    font = medium is appropriate for 1x1.  Other choices are
    size in points, 'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'
    """
    y = y+y_shift
    en = len(entries)                   # number of entries
    ov = (entries > binEdges[-1]).sum()   # overflows
    uf = (entries < binEdges[0]).sum()    # underflows
    mn = entries.mean()                 # mean
    sd = entries.std()                  # standard deviation
    textstr = '%s\n N=%i \nOverflow=%i \nUnderflow=%i \n$\mu=%.2f$ \n$\sigma=%.2f$' % (name,
                                                                                       en, ov, uf, mn, sd)
    props = dict(boxstyle='round', facecolor='white', alpha=0.5)
    ax.text(x, y, textstr,
            transform=ax.transAxes,
            bbox=props,
            fontsize=fontsize,
            horizontalalignment='right',
            verticalalignment='top')

# Claudio's code ends
# ---------------------------------


fig, ax = plt.subplots(nrows=2)
# import binary data set
# this has shape (1000,10)
raw = np.array(np.loadtxt("./straightTracks.txt"))
# x positions of pixel layer
layer_x = np.array([2, 3, 5, 7], dtype=float)

# set up array
histX1X0 = np.empty(len(raw))
histX2X0 = np.empty(len(raw))
histXav = np.empty(len(raw))
for i, data in enumerate(raw):
    # position in the length 10 line
    ytrack1 = data[2:6]
    ytrack2 = data[6:]
    X0 = data[0]

    # [1] in fit is the constant term correspond to y-axis intersect
    X1 = np.polyfit(layer_x, ytrack1, 1)[1]
    X2 = np.polyfit(layer_x, ytrack2, 1)[1]
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
