##encoding=utf8
##version =py27, py33
##author  =sanhe
##date    =2014-10-13

"""
把矩阵中的所有元素，根据一个门限e
= 0    if i <= e
= 1    if i > e
"""

from __future__ import print_function
from sklearn import preprocessing
import numpy as np

def example1():
    """方法1[推荐]
    """
    X = np.array([[1, -1,  2], ## "f"非常重要，为了标准化，矩阵元素必须是浮点类型
                  [2,  0,  0],
                  [0,  1, -1]], dtype = "f")
    binarizer = preprocessing.Binarizer(threshold=1.1).fit(X)
    print("binarized X = \n%s\n" % binarizer.transform(X))
    
example1()

def example2():
    """方法2[推荐]
    """
    X = np.array([[1, -1,  2], ## "f"非常重要，为了标准化，矩阵元素必须是浮点类型
                  [2,  0,  0],
                  [0,  1, -1]], dtype = "f")
    print("binarized X = \n%s\n" % preprocessing.binarize(X, threshold=1.1))

example2()