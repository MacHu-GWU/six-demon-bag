##encoding=utf8
##version =py27, py33
##author  =sanhe

from __future__ import print_function
from sklearn import cross_validation
import numpy as np
import random

def load_data():
    n = 24
    data = np.array([[i, i+1] for i in range(n)]) # [(0,1),(1,2),...,(23,24)]
    data_label = np.array(list(range(n))) # [0,1,2,...,23]
    return data, data_label

def algorithm(train, train_label, test):
    """
    """
    return test_label

def KFolder_split(data, data_label, k = 10):
    kf = cross_validation.KFold(len(data), n_folds=k)
    for train_index, test_index in kf:
        yield data[train_index], data_label[train_index], data[test_index], data_label[test_index]

def performance_test(data_set, algorithm):
    data, data_label = load_data()
    for train, train_l, test, test_l in KFolder_split(data, data_label, k=6):
        print( train, train_l, test, test_l )
    
    
#     res = algorithm(data_set)
#     print(res)
performance_test(1, algorithm)