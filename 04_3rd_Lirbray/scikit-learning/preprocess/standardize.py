##encoding=utf8
##version =py27, py33
##author  =sanhe
##date    =2014-10-13

"""
对矩阵数据中的每一列去除均值和方差的预处理
定义：
v = [a1, a2, a3]
v' = (v - mean(v) ) / std(v)
"""

from __future__ import print_function
from sklearn import preprocessing
import numpy as np

def example1():
    """对矩阵数据中的每一列去均值和方差，方法1[推荐]
    """
    X = np.array([[1,2,3], ## "f"非常重要，为了标准化，矩阵元素必须是浮点类型
                  [3,5,7],
                  [5,8,11]], dtype="f")
    scaler = preprocessing.StandardScaler(copy=True).fit(X) # 如果.fit()的输入已经是numpy.array，则可以设置copy = False以节约内存
    print("mean of each column = \n%s\n" % scaler.mean_) # mean value of each column
    print("std of each column = \n%s\n" % scaler.std_) # standard deviation of each column
    print("scaled data = \n%s\n" % scaler.transform(X)) # scaled data
    
# example1()

def example2():
    """对矩阵数据中的每一列去均值和方差，方法2
    """
    X = np.array([[1,2,3], ## "f"非常重要，为了标准化，矩阵元素必须是浮点类型
                  [3,5,7],
                  [5,8,11]], dtype="f")
    print("scaled data = \n%s\n" % preprocessing.scale(X) )
    
# example2()