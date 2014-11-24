##################################
#encoding=utf8                   #
#version =py27, py33             #
#author  =sanhe                  #
#date    =2014-11-10             #
#                                #
#    (\ (\                       #
#    ( -.-)o    I am a Rabbit!   #
#    o_(")(")                    #
#                                #
##################################
"""
"""

from __future__ import print_function
from sklearn import preprocessing
from sklearn import datasets
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from numpy import linalg

def example1():
    """使用swiss roll数据来展示pca算法内部的各步骤。
    协方差矩阵，特征值，特征值的筛选
    """
    X, color = datasets.samples_generator.make_swiss_roll(n_samples=1500) # load data
    
    pca = PCA(n_components=0.8) # 选择2个主成份
    pca.fit(X) # 训练
    X1 = pca.fit_transform(X) # 自适应
    
    print(X1[:,0].var(), X1[:,1].var(), X1[:,2].var()) # 降纬后各特征的方差
    print(pca.get_covariance()) # 协方差矩阵
    
    eigvalue, eigvector = linalg.eig(np.cov(X.T) ) # 协方差矩阵的特征值，和特征变量
    print(eigvalue)
    print(eigvector)

example1()