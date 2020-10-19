from .__init__ import *
from ..__init__ import Generator


def gcdFunc(maxVal=20):
    a = random.randint(1, maxVal)
    b = random.randint(1, maxVal)
    x, y = a, b
    while y:
        x, y = y, x % y
    problem = f"GCD of {a} and {b} = "
    solution = str(x)
    return problem, solution
