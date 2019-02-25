import numpy as np
import matplotlib.pyplot as plt
from scipy.special import ellipk

# T0 cancels in the end so might as well just ignore
def ratio_intgrand(alpha, beta):
    alpha = np.pi * alpha / 180  # convert to radiant
    k = np.sin(alpha/2)
    return 1 / np.sqrt(1-np.power(k, 2) * np.power(np.sin(beta), 2))


# sample 180 points for \alpha between 0 to 90
Alphas = np.linspace(1, 90, 179)
Deviation_ratio = np.empty(len(Alphas))

# do a Reynmman sum of 2000 pieces
N = 2000
# xs is beta range, chopped in N
xs = np.linspace(0, np.pi/2, N)

for i, a in np.ndenumerate(Alphas):
    ys = [ratio_intgrand(a, beta) for beta in xs]  # all ys in reynmman sum
    y_avg = np.average(ys)  # integral area = y_avg * x_width
    Deviation_ratio[i] = y_avg

Verify = [2/np.pi*ellipk(np.sin((a/180 * np.pi/2))**2) for a in Alphas]
plt.scatter(Alphas, Deviation_ratio, label="our result")
plt.scatter(Alphas, Verify, label="verification with scipy.special", s=4)
plt.legend()
plt.title("$\\frac{T}{T_0}$ in pendulum vs. angle")
plt.ylabel("$\\frac{T}{T_0}$", rotation=0.5)
plt.xlabel("$\\alpha \\degree$")
plt.show()
