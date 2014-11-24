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
在数据IO的过程中有一类情况是计算机无法解决的。那就是长数字的类型判断。
对于一个长数字：例如 8327427590102398472374，任何程序都无法在人类不
干预的情况下知道这是一个字符串还是一个整数。

结论：
    用txt作为储存的容器
    用xlsx作为阅览使用
    用database作为大容量IO的工具
"""

from __future__ import print_function
import numpy as np
import pandas as pd
import datetime

def txt_file_is_better():
    df = pd.read_csv(r"resources\long_int.txt", index_col = False)
    print(df)
    print(df.dtypes) # 过长数字字符串不能被转化成整数，自动按照字符串处理
    
    df.to_csv(r"resources\long_int_good.txt", index=False) # txt不会丢失精度
    df.to_csv(r"resources\long_int_bad.csv", index=False) # csv会丢失精度
    
txt_file_is_better()