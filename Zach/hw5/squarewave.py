import numpy as np
from numpy import asarray, zeros, place, nan, mod

def square(t,duty=.5):
	"""
	t = np.asarray(t)
	if t.dtype.char in ['fFdD']:
		ytype = t.dtype.char
	else:
		ytype = 'd'

	y = np.zeros(t.shape, ytype)

	tmod = np.mod(t, 1.0)
	mask1 = 1
	place(y,mask1,1)
	"""

	t, w = asarray(t), asarray(duty)
	w = asarray(w + (t - t))
	t = asarray(t + (w - w))
	if t.dtype.char in ['fFdD']:
		ytype = t.dtype.char
	else:
		ytype = 'd'

	y = zeros(t.shape, ytype)

    # width must be between 0 and 1 inclusive
	mask1 = (w > 1) | (w < 0)
	place(y, mask1, nan)

    # on the interval 0 to duty*1.0 function is 1
	tmod = mod(t, 1.0)
	mask2 = (1 - mask1) & (tmod < w * 1.0)
	place(y, mask2, 1)

    # on the interval duty*1.0 to 1.0 function is
    #  (.5*(w+1)-tmod) / (.5*(1-w))
	mask3 = (1 - mask1) & (1 - mask2)
	place(y, mask3, -1)
	return y
