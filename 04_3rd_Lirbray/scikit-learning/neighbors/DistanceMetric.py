##encoding=utf8
##version =py27, py34
##author  =sanhe
##date    =2014-10-12

"""
ref = http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.DistanceMetric.html
"""

from __future__ import print_function
import numpy as np
from sklearn.neighbors import DistanceMetric

def example1():
    dist = DistanceMetric.get_metric("euclidean")
    train = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
    test = np.array([[0.5, 0.5], [-0.5, -0.5]])
    
    distance_matrix = dist.pairwise(train, test)
    print(distance_matrix) # distance_matrix
    
    reduced_distance_matrix = dist.dist_to_rdist(distance_matrix) # reduced_distance_matrix
    print(reduced_distance_matrix) # for euclidean, it's squared distance_matrix
    
    print(dist.rdist_to_dist(reduced_distance_matrix))

# example1()

def example2():
    """using customized distance
    """
    from HSH.Misc.shgeo import dist
    def earthdist(x, y): # latitude, longitude earth surface distance
        return dist((x[0], x[1]), (y[0], y[1]))
    
    dist_cal = DistanceMetric.get_metric(earthdist)
    train = np.array([[32.5, 101.0], [32.5, 102.0]])
    test = np.array([[31.5, 101.0], [39.5, 101.0]])
    print(dist_cal.pairwise(train, test))
    
example2()