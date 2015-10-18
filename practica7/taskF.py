import matplotlib.pyplot as plt
from math import cos, pi
import numpy as np

A=4
B=0.3

def func(x):
	y=x.copy()
	for i in range(len(x)):
		y[i] = sum([cos(pi*x[i]*A**j)*B**j for j in range(100)])
	return y

x=np.arange(-2,4.51,0.01)
plt.plot(x, func(x))
plt.show()