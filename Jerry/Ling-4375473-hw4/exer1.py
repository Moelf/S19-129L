import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------
#
# A bunch of functions to make
# numpy histograms look better
#
#  CC 27 Jan 2019
# ---------------------------------


def statBox(ax, entries, binEdges, x=0.96, y=0.98, fontsize='medium'):
    """
    Put a stat box on the histogram at coord x and y
    font = medium is appropriate for 1x1.  Other choices are
    size in points, 'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'
    """
    en = len(entries)                   # number of entries
    ov = (entries > binEdges[-1]).sum()   # overflows
    uf = (entries < binEdges[0]).sum()    # underflows
    mn = entries.mean()                 # mean
    sd = entries.std()                  # standard deviation
    textstr = 'N=%i \nOverflow=%i \nUnderflow=%i \n$\mu=%.2f$ \n$\sigma=%.2f$' % (
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


fig, ax = plt.subplots()
# import binary data set
x = np.load("./dataSet.npy")
# set up bins and scale after observation
binEdges = np.linspace(0, 25, 50)
ax.hist(x, bins=binEdges, log=True)
# label everything
plt.xlabel("Value")
plt.ylabel("Events count")
# add claudio's box
statBox(ax, x, binEdges)
plt.title("Extraction of npy file")
plt.show()
