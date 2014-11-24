##################################
#encoding=utf8                   #
#version =py27, py33             #
#author  =sanhe                  #
#date    =2014-11-01             #
#                                #
#    (\ (\                       #
#    ( -.-)o    I am a Rabbit!   #
#    o_(")(")                    #
#                                #
##################################

from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt

def norm_dstr(min, max, n): ## 正态分布快速生成器
    ''' generate n samples obey normal distribution
    95% percents of samples fall in range(min, max)
    '''
    u, v = 0.5*(min+max), float(min+max)/4
    data = np.random.randn(n) * v + np.ones(n) * u
    return data

if __name__ == "__main__":
    plt.hist(norm_dstr(10,30,1000000), 15, normed=True)
    plt.show()