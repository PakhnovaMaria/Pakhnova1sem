import numpy as np
import math
import pylab
from matplotlib import mlab

tlist = np. arange(-2*np.pi,2*np.pi, 0.01)

pylab. ion()

for a in range (50):
    xlist = [np.sin (t+a/10) for t in tlist]
    ylist = [np.cos(2*t) for t in tlist]
    pylab. clf()
    pylab.plot (xlist,ylist)
    pylab.draw()

pylab.close()