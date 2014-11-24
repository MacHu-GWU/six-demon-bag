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
数据表中的格式转换
reference = http://pandas.pydata.org/pandas-docs/stable/merging.html
"""

from __future__ import print_function
import pandas as pd, numpy as np

def example1():
    """整数和字符串"""
    df = pd.DataFrame(np.random.randint(1000000000000, 9999999999999, (3,5)), columns = list("ABCD"))
    
example1()