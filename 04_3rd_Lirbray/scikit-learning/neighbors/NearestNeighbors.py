##encoding=utf8
##version =py27, py34
##author  =sanhe
##date    =2014-10-12

"""
In this example, you can understand once given a training data-set, having any
test sample, how to quickly get the k-neighboors and the distances.
ref = http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html
"""

from __future__ import print_function
import numpy as np, pandas as pd
from sklearn.neighbors import NearestNeighbors
import time

def example1():
    """ EXAMPLE1
    Performance test - KNN search algorithms: ball_tree & kd_tree
    This is a demo to compare the speed of these two algorithms. Usually, kd_tree
    has better performance.
    """
    
    X = pd.read_csv(r"test_data/copd_1000.txt", # load data
                    header = None,
                    index_col = False)

    """ ball_tree algorithm """
    st = time.clock()
    ## create a neighboors object. apply NearestNeighbors.fit(data) method 
    nbrs1 = NearestNeighbors(n_neighbors=2, algorithm="ball_tree").fit(X)
#     print("\nnbrs1.kneighbors(X): \n", nbrs1.kneighbors(X) )## returns tuple(distance, index)
    print("\nball_tree cost seconds: \n", time.clock() - st )## calculate time consuminig
    
    """ kd_tree algorithm """
    st = time.clock()
    nbrs2 = NearestNeighbors(n_neighbors=2, algorithm="kd_tree").fit(X)
#     print("\nnbrs2.kneighbors(X): \n", nbrs2.kneighbors(X))
    print("\nkd_tree cost seconds: \n", time.clock() - st)

example1()
