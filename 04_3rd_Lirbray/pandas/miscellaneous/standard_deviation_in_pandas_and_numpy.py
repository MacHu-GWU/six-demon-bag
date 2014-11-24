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
在numpy和pandas中std命令的含义是不同的
numpy中是求标准差(除以n)
pandas中是求样本标准差(除以n-1)
"""

from __future__ import print_function
import numpy as np
import pandas as pd

data1 = np.array([-1,0,1])
df1 = pd.DataFrame(data1)
print(data1.std() ) # = 0.816 = ( ((x1-m)^2 + (x2-m)^2 + (x3-m)^2)/3 ) ** 0.5
print(df1.std() ) # = 1 ( ((x1-m)^2 + (x2-m)^2 + (x3-m)^2)/(3-1) ) ** 0.5

data2 = np.array([-2,0,2]) # = 1.633 = (8/3) ** 0.5
df2 = pd.DataFrame(data2) # = 2 = (8/2) ** 0.5
print(data2.std() )
print(df2.std() ) 
