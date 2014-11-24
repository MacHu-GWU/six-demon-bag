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
reference = http://pandas.pydata.org/pandas-docs/stable/merging.html
"""

from __future__ import print_function
import pandas as pd, numpy as np

def example1():
    """二维表增加列，或者增加行
    """
    df = pd.DataFrame([[1,2,3,4],
                       [5,6,7,8]], columns = list("ABCD"))
    df["E"] = 5 # 增加列
    print(df)
    
    df.loc[df.shape[0]] = [10,20,30,40,50] # 在index是从0开始顺序编号时使用
    df.loc[df.index[-1]+1] = [10,200,300,400,500] # 此方法性能较差，最好不用
    print(df)
    
    df = df.append(pd.DataFrame([[1,2,3,4,5]], 
                                columns = list("ABCDE")) ) # 增加新行，必须保证列定义相同
    print(df)
    
# example1()

def example2():
    """从表中删除行，删除列
    当然也可以参考SELECT章节中的方法，select一个子集并赋值给新对象
    """
    df = pd.DataFrame([[1,2,3,4],
                       [5,6,7,8],
                       [9,10,11,12]], columns = list("ABCD"))
    print(df.drop([0,1]) ) # 抛弃行
    print(df.drop(["A", "C"], axis = 1)) # 抛弃列
    
# example2()

def example3():
    """多个同结构的dataframe连接
    """
    df1 = pd.DataFrame(np.random.randn(1, 4))
    df2 = pd.DataFrame(np.random.randn(2, 4))
    df3 = pd.DataFrame(np.random.randn(3, 4))
    df = pd.concat([df1, df2, df3]) # 连接3个表，columns必须相同，index可以相同也可以不同
    print(df)
    df.index = list(range(df.shape[0])) # 重新标记index
    print(df)
    
# example3()
