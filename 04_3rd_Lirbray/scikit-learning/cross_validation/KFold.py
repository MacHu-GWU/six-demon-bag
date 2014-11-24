##encoding=utf8
##version =py27, py33
##author  =sanhe

"""
cross_validation 交叉验证

在机器学习任务中，为了测试算法的有效性，我们通常采取交叉验证的办法。具体流程是：
1. 把数据集随机近似划分成n等分
2. 进行n次试验，每次试验用第i等分作为训练集，用剩余的n-1等分作为测试集
通常我们取n = 10
"""

from __future__ import print_function
from sklearn import cross_validation
import numpy as np
import random

def example1():
    """KFold划分样本为n等分进行交叉验证
    """
    n = 24
    data = np.array([[i, i+1] for i in range(n)]) # [(0,1),(1,2),...,(23,24)]
    data_label = np.array(list(range(n))) # [0,1,2,...,23]
    kf = cross_validation.KFold(24, #选用前若干个样本，不一定使用全部的数据集
                                n_folds=6)
    for train_index, test_index in kf:
        print("TRAIN:", train_index, "TEST:", test_index)
        train, test = data[train_index], data[test_index]
        train_label, test_label = data_label[train_index], data_label[test_index]
        
# example1()

def example2():
    """train_test_split单次划分训练集和测试集
    """
    n = 24
    data = np.array([[i, i+1] for i in range(n)]) # [(0,1),(1,2),...,(23,24)]
    data_label = np.array(list(range(n))) # [0,1,2,...,23]
    ## random_state 是随机数种子，同样的种子会导致同样的输出，所以我们可以用随机种子代替
    train, test, train_label, test_label = cross_validation.train_test_split(data,
                                                                             data_label,
                                                                             train_size = 0.6,
                                                                             test_size = 0.4,
                                                                             random_state = random.randint(0,9999))
    print("TRAIN:\n%s\n" % train)
    print("TEST:\n%s\n" % test)
    
# example2()