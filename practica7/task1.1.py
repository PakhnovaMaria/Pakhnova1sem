from math import *
def function(x):
    if x != 0 and x != -2:
        if (1/(exp(sin(x)+1)))/(5/4+1/x**15) > 0:
            a = log((1/(exp(1/(sin(x)+1))))/(5/4+1/(x**15)), ((1+x)**2))
            return a
        else:
            return None
print(function(1))
print(function(10))
print(function(1000))