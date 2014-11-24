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
import pandas as pd, numpy as np


def demo_pd_indexed_DataFrame():
    """4. 创建pandas带index的二维表
    """
    dates = pd.date_range("20130101", periods=6)
    cindex = list("ABCD")
    print(dates) ## 行标号
    print(cindex) ## 列标号
    df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=cindex)
    print("\ndf:\n%s" % df)
    print("\ndf.T:\n%s" % df.T) ## 转置
    print("\ndf.head():\n%s" % df.head()) ## 去掉最后一行
    print("\ndf.tail():\n%s" % df.tail()) ## 去掉第一行
    print("\ndf.index:\n%s" % df.index) ## 行标 = 索引
    print("\ndf.columns:\n%s" % df.columns) ## 列标 = 列
    print("\ndf.values:\n%s" % df.values) ## 值, np对象
    print("\ndf.describe():\n%s" % df.describe()) ## 统计每列的基本统计参数
    
    print("\ndf.sort_index(axis=1, ascending=False):\n%s" % 
          df.sort_index(axis=1, ascending=False)) ## 按照行标号排序，降序
    print("\ndf.sort(columns='B')\n%s" % 
          df.sort(columns="B", ascending=False)) ## 按照B列排序，降序
            
    print("\ndf.where(df > 0)\n%s" % df.where(df > 0))
    print("\ndf.mean()\n%s" % df.mean())
    print("\ndf.var()\n%s" % df.var())

# demo_pd_indexed_DataFrame()

def index_and_columns_handle():
    df = pd.DataFrame(np.array([[1,2,3,4],
                                [8,7,6,5],
                                [9,10,11,12],
                                [16,15,14,13],
                                [17,18,19,20],
                                [24,23,22,21],]), columns = list("ABCD"))
    print("df:\n", df)
    df = df.reindex(index=[1,2,3] )
    print("df:\n", df)
index_and_columns_handle()