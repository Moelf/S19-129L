import math
import numpy as np
import matplotlib.pyplot as plt
N = 10000
UniN = np.random.rand(N)
t = np.arange(0,1,0.1)
pdf = lambda x: N/10 * (1+4*x)/3
cdF = lambda x: ((-1/3 + math.sqrt(1/9 + 8*x/3))/4*3)
samples = [cdF(x) for x in UniN]

plt.hist(samples, bins=np.arange(0,1,0.1),label="Hist")
plt.plot(t, pdf(t), 'r-',label="PDF")
plt.xticks(np.arange(0,1,0.1))
plt.legend()
plt.title("Sampling vs. pdf scaled")
plt.show()
