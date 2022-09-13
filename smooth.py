from math import sin
from numpy import rad2deg


def smooth(x, dx):
    def inner(arg):
        for f in reversed(x):
            # f(x − dx), f(x) and f(x + dx)
            arg = f(arg)
        return arg

    return inner


def fn(f):
    return round(sin(rad2deg(f)), 3)


smoothFunc = smooth([fn], 15)

print(smoothFunc(10))
print(fn(10))
# smoothFunc = smooth(fn(sum) => sin(rad2deg(sum)), 15);
# smoothFunc(10) // ~ 0.438
