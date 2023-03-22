import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

def gaussian(x, y, x0, y0, sigma_x, sigma_y, A):
    return A * np.exp(-((x - x0)**2 / (2 * sigma_x**2) + (y - y0)**2 / (2 * sigma_y**2)))


x, y = np.meshgrid(np.linspace(-6, 6, 100), np.linspace(-6, 6, 100))
z = gaussian(x, y, 0, 0, 1, 1, 1)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z)
ax.plot_surface(x, y, z, cmap=cm.viridis)
plt.show()