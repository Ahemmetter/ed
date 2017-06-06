import matplotlib.pyplot as plt
import numpy as np
from numpy.lib.scimath import sqrt as csqrt

c = 3
n = 4
d = 1

(k, w) = np.meshgrid(np.linspace(0, 100, 1000), np.linspace(0, 200, 1000))

a = csqrt((n ** 2 * (w/c) ** 2) - k ** 2)
b = csqrt((w/c) ** 2 - k ** 2)

A = (1 - a/b)*(1 - b / a) * np.exp(1j * a * d) + (1 + a / b) * (1 + b / a) * np.exp(-1j * a * d)
plt.contour(k, w, A, [0])
plt.show()