##encoding=utf8
##version =py27, py33
##author  =sanhe
##date    =2014-10-16

"""
画频率直方图以及获得直方图频率统计信息
"""

from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt

def example1():
    """画频率分布直方图
    for more information, run this:
        print(matplotlib.pyplot.hist.__doc__)
    http://matplotlib.org/api/pyplot_api.html
    """
    mu, sigma = 100, 15
    x = mu + sigma*np.random.randn(10000)
    n, bins, patches = plt.hist(x, # patches not important
                                bins = 50, # number of bins
                                range = (50, 150), # only plot value in named range
                                normed = False, # ie the integral of the histogram will sum to 1
                                facecolor='green', # bin color
                                cumulative = False, # plot cdf rather than pdf
                                alpha= 0.75) # Transparency, 0 = blank, 1 = pure green
    print(n) # if normed = False, then n = how many items falls in each bar
    print(bins) # range information for each bar
    plt.show()
    
example1()