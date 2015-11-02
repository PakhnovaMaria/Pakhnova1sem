from math import *
def formula1(x):
    if x != 1:
        a = ((x**7) + ((2 * x)**6) - (3/(1+x)))/((1/(1-x)) + 21/7)
        return a
    else:
        return None
print(formula1(1))
