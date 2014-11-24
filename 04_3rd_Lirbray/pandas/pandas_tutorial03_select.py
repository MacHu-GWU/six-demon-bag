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
本文档主要介绍如何从pandas的series和dataframe中快速的选择数据
reference = http://pandas.pydata.org/pandas-docs/stable/10min.html
"""

from __future__ import print_function
import pandas as pd
import numpy as np

def example1():
    """用.loc方法，根据行和列的index选择数据
    .loc is strictly label based, will raise KeyError when the items are not found, allowed inputs are:
        A single label, e.g. 5 or "a", (note that 5 is interpreted as a label of the index. This use is not an integer position along the index)
        A list or array of labels ["a", "b", "c"]
        A slice object with labels "a":"f", (note that contrary to usual python slices, both the start and the stop are included!)
        A boolean array
    """
    df = pd.DataFrame(np.random.randn(8, 4), columns = list("ABCD"))
    print("=== 原始数据等于 ===\n%s\n" % df)
    print("=== 第2行，第3列 ===\n%s" % df.loc[1,"A"])
    print("=== 第2,3行，第1,3列 ===\n%s" % df.loc[range(1,3), ["A", "C"]])
    print("=== 第1-3行，第1-3列 ===\n%s" % df.loc[1:3, "A":"C"]) # 也支持 :3 从头到第三个, 3: 从第三个到最后， ::-1 逆序选择
    
# example1()

def example2():
    """用.iloc方法根据行的index选择数据
    .iloc is strictly integer position based (from 0 to length-1 of the axis), will raise IndexError if an indexer
     is requested and it is out-of-bounds, except slice indexers which allow out-of-bounds indexing. 
     (this conforms with python/numpy slice semantics). Allowed inputs are:
        An integer e.g. 5
        A list or array of integers [4, 3, 0]
        A slice object with ints 1:7
    """
    df = pd.DataFrame(np.random.randn(8, 4), columns = list("ABCD"))
    print("=== 原始数据等于 ===\n%s\n" % df)
    print("=== 第2行 === \n%s" % df.iloc[1])
    print("=== 第0,2,4行 === \n%s" % df.iloc[[0,2,4]])
    print("=== 第1,3,5行 === \n%s" % df.iloc[range(1,6,2)])
    
# example2()

def example3():
    """WHERE syntax
    根据逻辑运算选择数据
    """
    data = [[1,30],[2,40],[3,20],[4,28]]
    df = pd.DataFrame(data, columns = list("AB"))
    print("=== 原始数据等于 ===\n%s\n" % df)
    print("=== 根据表中的元素选择数据 ===\n%s\n" % df[ df> 25] )
    print("=== 根据某列的逻辑运算选择 ===\n%s\n" % df[ df["B"] > 20 ] )
    
# example3()

def example4():
    """Customized WHERE syntax
    根据复杂逻辑运算选择数据，相当于np.where
    """
    df = pd.DataFrame({"a" : ["one", "one", "two", "three", "two", "one", "six"],
                       "b" : ["x", "y", "y", "x", "y", "x", "x"],
                       "c" : np.random.randn(7)})
    
    criterion1 = df["a"].map(lambda x: x.startswith("t")) # a列的值是以字母"t"开头
    criterion2 = df["c"].map(lambda x: x >= 0) # c列的值大于等于0
    print("=== 原始数据等于 ===\n%s\n" % df)
    print("=== 选择a列的值以字母't'开头，并且c列的值大于等于0 ===\n%s" % df[criterion1 & criterion2])
    
# example4()

def example5():
    """对于离散元素.isin是一个快速获取数据的好的方法
    """
    df = pd.DataFrame({"a" : ["one", "one", "two", "three", "two", "one", "six"],
                       "b" : ["x", "y", "y", "x", "y", "x", "x"],
                       "c" : np.random.randn(7)})
    print("=== 原始数据等于 ===\n%s\n" % df)
    print("=== 选择a列的值在 .isin(列表) 中的数据 ===\n%s\n" % df[ df["a"].isin(["two","three"]) ] )

# example5()

def example6():
    """
    isnull 和 notnull 根据单元格内的值是否是空值返回True or False
    """
    df = pd.DataFrame({"a": [1,2,None],
                       "b": [10,20,30]})
    print("=== 原始数据等于 ===\n%s\n" % df)
    print(  
            df[ 
                df["a"].notnull() 
               ] 
          )

# example6()