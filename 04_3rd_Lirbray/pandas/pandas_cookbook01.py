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
import pandas as pd

def example1():
    df = pd.DataFrame(np.random.randn(6,4), columns = list('ABCD'))
    print(df)
    df.ix[df.A > 0] = 0 # 对于A列的值大于0的那些行，赋值0
    print(df)
    
example1()