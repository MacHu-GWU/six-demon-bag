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

"""
将numpy和pandas中的数据都当成二维表看待时，我们经常
会有要将行按照其中的某几列按照优先顺序，升序或者降序
进行排序。所以我们来比较一下分别在numpy和pandas中这么
做的时间复杂度如何

结论：pandas快
"""
from __future__ import print_function
import numpy as np, pandas as pd
import random
import time

def rand_string(length):
    """highest performance non-dependent pure python random string generator
    """
    # All the characters you want to use in your strings:
    test_chars = u"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return "".join([random.choice(test_chars) for i in range(length)])

n = 100000
a = np.random.randint(1024, size=n)
b = np.random.randn(n)
c = [rand_string(32) for i in range(n)]

data = np.array([row for row in zip(a,b,c)], 
                dtype = [("a", int),("b", float),("c", "S2")])
df = pd.DataFrame(data, columns = list("abc"))

st = time.clock()
data.sort(order = ["a", "b"]) # numpy array sort doens't support ascend, descend
print(time.clock()-st)

st = time.clock()
df = df.sort(columns = ["a", "b"], ascending = [1, 0])
print(time.clock()-st)
