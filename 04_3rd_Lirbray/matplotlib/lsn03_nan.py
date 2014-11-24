##encoding=utf8
##version =py27, py33
##author  =sanhe
##date    =2014-10-16

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
points = np.arange(-5, 5, 0.01)
xs, ys = np.meshgrid(points, points) ##
z = np.sqrt(xs ** 2 + ys ** 2)
plt.imshow(z, cmap = 'afmhot') ## 更多参数，参考 http://matplotlib.org/examples/color/colormaps_reference.html
plt.colorbar()
plt.show()