##encoding=utf8
##version =py27, py34
##author  =sanhe
##date    =2014-10-12

from __future__ import print_function
import numpy as np
from sklearn.neighbors import kneighbors_graph, radius_neighbors_graph

def example1():
    """画出k-近邻关系图
    距离最近的k个样本将被看做近邻
    """
    train = np.array([[1,2,4,7,9,10]]).transpose()
    graph = kneighbors_graph(train, 2) # k = 2
    print(graph)
    print(graph.toarray())
    
example1()

def example2():
    """画出radius-近邻关系图
    距离<=radius的将被看做近邻
    """
    train = np.array([[1,2,4,7,9,10]]).transpose()
    graph = radius_neighbors_graph(train, 2.5) # radius = 2.5
    print(graph)
    print(graph.toarray())
    
example2()