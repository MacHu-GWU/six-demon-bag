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
import pandas as pd
import numpy as np
import sys

def example():
    """测试numpy.array对象和pandas对象在内存消耗上的差别
    结论：
    1. 无论如何改变randn的大小，np和pd的内存消耗都不变。
        说明np和pd对象本身存储的只是指针。
    """
    data = np.random.randn(1000, 1000)
    df = pd.DataFrame(data)
    print(sys.getsizeof(data)) # 80
    print(sys.getsizeof(df)) # 56
    
example()