import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-6, 6, 0.01)

def gaussian(x, mean, sigma):  
    return (1 / np.sqrt(2*np.pi * sigma**2)) * np.exp(- (x-mean)**2 / (2*sigma**2))


plt.plot(x, gaussian(x, 0, 1))
plt.xlim(-6,6)
plt.show()