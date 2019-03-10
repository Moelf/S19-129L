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
