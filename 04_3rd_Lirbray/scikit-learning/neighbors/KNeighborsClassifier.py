##encoding=utf8
##version =py27, py34
##author  =sanhe
##date    =2014-10-12

from __future__ import print_function
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

def example():
    """knn分类器的使用
    注意：
        KNeighborsClassifier不会自带数据去均值，方差的预处理功能。如果需要预处理，
        用sklearn.preprocess模块处理即可
    ref = http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
    """
    train = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]]) # 训练数据
    train_label = np.array(["A", "A", "A", "B", "B", "B"]) # 训练数据类标
    neigh = KNeighborsClassifier(n_neighbors=3) # knn分类器
    neigh.fit(train, train_label) # 训练
    
    test = np.array([0.5, 0.5]) # 测试数据
    test_label = neigh.predict(test) # 分类
    print(test_label)
    
# example()

def repack(train, train_label, test, k=1):
    """knn分类器重包装
    """
    neigh = KNeighborsClassifier(n_neighbors=3)
    neigh.fit(train, train_label)
    return neigh.predict(test)

print(repack([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]],
             ["A", "A", "A", "B", "B", "B"],
             [[0.5, 0.5], [-0.5, -0.5]]) )
    
    