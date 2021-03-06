#!/usr/bin/python
"""Script to generate fibonacci sequence upto a maximum value
or 1000 if no input using generator functions"""
from sys import argv


# generator function
def fib():
    """Generator function"""
    # initial steps
    a = 0
    b = 1
    while True:
        # generator yield step
        yield a
        # fibonacci sum and swap step
        a, b = b, (a + b)


if __name__ == "__main__":
    # accept input or use 1000 as max fibonacci
    if len(argv) == 1:
        n = 1000
    else:
        n = int(argv[1])
    for i in fib():
        if i > n:
            break
        print i,
