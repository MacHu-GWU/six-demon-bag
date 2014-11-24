##encoding=utf8
##version =py27, py33
##author  =sanhe
##date    =2014-10-13

"""
把每一行（注意在sklearn.preprocessing.Normalizer中是行！）的向量归一化
默认使用norm2方式

v = [a1, a2, a3]
    norm2 归一化定义：
        v' = v / sqrt(a1^2 + a2^2 + a3^2)
    norm1 归一化定义：
        v' = v / sum(abs(a1) + abs(a2) + abs(a3))
"""

from __future__ import print_function
from sklearn import preprocessing
import numpy as np

def example1():
    """把矩阵数据中的每一行归一化。有norm1, norm2两种模式
    """
    X = np.array([[1, -1,  2], ## "f"非常重要，为了标准化，矩阵元素必须是浮点类型
                  [2,  0,  0],
                  [0,  1, -1]], dtype = "f")
    normalizer = preprocessing.Normalizer(copy=True, # 如果.fit()的输入已经是numpy.array，则可以设置copy = False以节约内存
                                          norm="l1").fit(X) # norm = "l1" or "l2", default norm = "l2"
                                          
    print("normalized X = \n%s\n" % normalizer.transform(X))
    
example1()

def example2():
    """方法2， preprocessing.normalize(X)
    """
    X = np.array([[1, -1,  2], ## "f"非常重要，为了标准化，矩阵元素必须是浮点类型
                  [2,  0,  0],
                  [0,  1, -1]], dtype = "f")
    X_normalized  = preprocessing.normalize(X, 
                                            copy=True, # 如果.fit()的输入已经是numpy.array，则可以设置copy = False以节约内存
                                            norm="l2")
                                          
    print("normalized X = \n%s\n" % X_normalized)
    
example2()