# -*- coding: UTF-8 -*-

a = 5


def f(n=a):
    """Do nothing, but document it."""
    return n


a = 6
print(f())



