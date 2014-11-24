#encoding=utf8

"""
在2维图形中用颜色表示三纬数据。
当我们的数据形式是：
    当 x = x1, y = y1 时 z = z1
    当 x = x2, y = y2 时 z = z2
    ...
    
我们希望在二维的坐标轴上，在x1, y1的点上，用深色表示大的值，用浅色表示小的值。
这就叫2d-colormap

当我们希望把相近的值用一个区域围起来，就成了等高线图(contour map)

下面我们就来教如何画2d-colormap和contour map
"""
from __future__ import print_function
import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
import numpy as np

def example1():
    """标准栅格情况下的画法
    当 x = [1,2,3,4], y = [1,2,3,4], 也就是一共是16个点，x和y相互对应的时候。这就叫标准栅格。
    """
    dx, dy = 0.01, 0.01
    x = np.arange(0.0, 10.0, 0.05)
    y = np.arange(0.0, 5.0, 0.05)
    x, y = np.meshgrid(x, y)
    z = np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)
    
    levels = MaxNLocator(nbins=15).tick_values(z.min(), z.max())
    cmap = plt.get_cmap('PiYG')
    norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)
    
    plt.subplot(2, 1, 1)
    im = plt.pcolormesh(x, y, z, cmap=cmap, norm=norm)
    plt.colorbar()
    plt.axis([x.min(), x.max(), y.min(), y.max()])
    plt.title('pcolormesh with levels')
    
    plt.subplot(2, 1, 2)
    plt.contourf(x + dx / 2.,
                 y + dy / 2., z, levels=levels,
                 cmap=cmap)
    plt.colorbar()
    plt.title('contourf with levels')

    plt.show()
    
example1()

def example2():
    """散点栅格情况下的画法
    x, y = (1,7), (4,9), (11,2),... 这种没有规律的散点x,y坐标，我们称其为散点栅格
    """
    dx, dy = 0.05, 0.05
    x = np.array([[1, 2],
                  [1, 3]])
    y = np.array([[3, 3],
                  [1, 1]])
    z = np.array([[5, 10],[15, 20]])
                  
    levels = MaxNLocator(nbins=4).tick_values(z.min(), z.max())
    cmap = plt.get_cmap('PiYG')
    norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)
    
    plt.subplot(2, 1, 1)
    im = plt.pcolormesh(x, y, z, cmap=cmap, norm=norm)
    plt.colorbar()
    plt.axis([x.min(), x.max(), y.min(), y.max()])
    plt.title('pcolormesh with levels')

    plt.subplot(2, 1, 2)
    plt.contourf(x + dx / 2.,
                 y + dy / 2., z, levels=levels,
                 cmap=cmap)
    plt.colorbar()
    plt.title('contourf with levels')

    plt.show()
    
example2()