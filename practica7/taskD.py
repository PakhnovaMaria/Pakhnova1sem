import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-20, 25.01, 0.1)
#plt.xkcd()
formula_string = input("Введите формулу:")
b = eval(formula_string)
plt.plot(x, b)
plt.show()