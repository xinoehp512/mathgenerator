from .__init__ import *
from ..__init__ import Generator


def factorialFunc(maxInput=6):
    a = random.randint(0, maxInput)
    n = a

    problem = str(a) + "! = "
    b = 1

    while a != 1 and n > 0:
        b *= n
        n -= 1
    solution = str(b)
    return problem, solution
