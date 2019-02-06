f = lambda x : x**2 * (1-x)
def f_prime(x,h):
    return (f(x+h)-f(x))/h

for i in range(2,18):
    h = 10**(-i)
    print("for h = 10^-%d, " % i, "f'(1) = %.20f" % f_prime(1,h))
