#!/usr/bin/env python3


def num_even_digits(x):
    return len([ y for y in str(x) if int(y) % 2 == 0])

print(num_even_digits(123456))
