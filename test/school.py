import sys
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 9])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.savefig("diagramm.png")

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
