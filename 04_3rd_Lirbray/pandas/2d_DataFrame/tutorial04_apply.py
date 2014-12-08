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
"""

from __future__ import print_function
import pandas as pd, numpy as np

def example1():
    df = pd.DataFrame(np.random.randn(3,5))
    print(df)
    print(df.apply(lambda x: x >= 0))
    
example1()