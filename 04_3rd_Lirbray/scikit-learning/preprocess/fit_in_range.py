##encoding=utf8
##version =py27, py33
##author  =sanhe
##date    =2014-10-13

"""
每一列的元素，压缩到[a, b]区间。使得数据之间的相对间隔按比例缩小
定义：
v = [a1, a2, a3]
v' = ( v - min(v) ) / (max(v) - min(v) )
"""

from __future__ import print_function
from sklearn import preprocessing
import numpy as np

def example1():
    X = np.array([[1,2,3], ## "f"非常重要，为了标准化，矩阵元素必须是浮点类型
                  [2,3,4],
                  [5,8,11]], dtype = "f")
    min_max_scaler = preprocessing.MinMaxScaler(feature_range=(0, 1), # 自定义被压缩到的范围，默认(0, 1)
                                                copy=True).fit(X) # 如果.fit()的输入已经是numpy.array，则可以设置copy = False以节约内存
    X_minmax = min_max_scaler.transform(X)
    print("scaled data = \n%s\n" % X_minmax) # scaled data
    print("每一列去最小值后所乘的系数 = \n%s\n" % min_max_scaler.scale_) # 每一列去最小值后所乘的系数
    
example1()