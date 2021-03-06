import numpy as np
import matplotlib.pyplot as plt


# time constant
tau, h = 0.0, 0.0
try:
    tau = float(input("Set time-constant tau: "))
    # set time step
    h = tau/500
except ValueError:
    print("Bad input, try again")


def V_in(time):
    # square wave using floor of a float
    if int(np.floor(time)) % 2 == 0:
        return 1

    return -1


# this is dVout / dt = f(x,y)
def f(time, V_out):
    return (V_in(time) - V_out) / tau


# initial time, 100 mu sec is hard-coded
total_step = min(1000000, int(100/h))
time_s = np.linspace(0, 100, total_step)
# lists to hold all steps, total steps = time / time_step
# this also fits initial condition, V_out(0) = 0
V_out_s = np.zeros(total_step)
# V_out_s = [0]

# main Runge-Kutta loop untill time reached
for i, time_point in np.ndenumerate(time_s):
    # make i an integer instead of tuple
    i = i[0]
    x_n = time_point
    y_n = V_out_s[i]
    k1 = h * f(x_n, y_n)
    k2 = h * f(x_n + h/2, y_n + k1/2)
    k3 = h*f(x_n + h/2, y_n + k2/2)
    k4 = h*f(x_n + h, y_n + k3)
    y_np1 = y_n + 1/6 * (k1 + 2*k2 + 2*k3 + k4)

    # prevent out of bound
    if i+1 < len(V_out_s):
        V_out_s[i+1] = y_np1

plt.title("time from $0 \mu s$ to $10 \mu s$ ")
plt.scatter(time_s[:int(len(time_s)*0.1)],
            V_out_s[:int(len(time_s)*0.1)], s=0.8)
plt.xlabel("time ($\mu s$)")
plt.ylabel("$V_{out}$", rotation=2)
plt.show()
plt.title("time from $90 \mu s$ to $100 \mu s$ ")
plt.xlabel("time ($\mu s$)")
plt.ylabel("$V_{out}$", rotation=2)
plt.scatter(time_s[int(len(time_s)*0.9):],
            V_out_s[int(len(time_s)*0.9):], s=0.8)
plt.show()
