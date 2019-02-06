lambda x : x**2 * (1-x)
def f_prime(x,h):
    return (f(x+h)-f(x))/h

for i in range(2,17):
    h = 10**(-i)
    print("h = %.20f" % h)
    print("f'(1) = %.20f" % f_prime(1,h))
