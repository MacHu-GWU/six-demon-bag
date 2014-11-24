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
reference: http://pandas.pydata.org/pandas-docs/stable/10min.html
"""

from __future__ import print_function
import pandas as pd
import numpy as np
from datetime import date

def example1():
    """强制转换列的数据类型
    """
    print("{:=^40}".format("example1"))
    data = [[1, 2.2, "sanhe", date(2000,1,1)]]
    df = pd.DataFrame(data, columns = ["id", "value", "name", "date"])
    df["id"] = df["id"].astype(str)
    df["value"] = df["value"].astype(float)
    df["name"] = df["name"].astype(str)
    df["date"] = df["date"].astype(date)
    
    print(df)
    print(df.dtypes)
    
example1()