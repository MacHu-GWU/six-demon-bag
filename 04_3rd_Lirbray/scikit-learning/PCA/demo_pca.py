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
[问题]sklearn中的pca是否采用了去均值和方差的数据预处理

[结论]sklearn中的pca即没有去均值，也没有去方差

[讨论]
    用户需要自己决定，是否在pca之前需要数据预处理。通常某个维度和其他的维度度量单位非常不同，则通常
    我们要使用数据预处理。
    
    从example2, example3中可以看到，使用去均值不会特别影响pca的结果，而使用去方差则会较大的影响pca的结果
    
    而在人脸识别中，每个维度是0-255的像素区间，所以无需数据预处理。example3中
    swiss roll每个维度都是数值变量，所以不采用数据预处理的结果要更好一些。
"""

from __future__ import print_function
from sklearn import preprocessing
from sklearn import datasets
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def example1():
    """使用swiss roll数据来展示pca算法的性能
    """
    X, color = datasets.samples_generator.make_swiss_roll(n_samples=1500) # load data
    
    pca = PCA(n_components=2) # 选择2个主成份
    pca.fit(X) # 训练
    X1 = pca.fit_transform(X) # 自适应
    print(X1)
    
    fig = plt.figure()
    ax = fig.add_subplot(211, projection='3d') # 画3d图
    ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=color, cmap=plt.cm.Spectral)
      
    ax = fig.add_subplot(212) # 画2d图
    ax.scatter(X1[:, 0], X1[:, 1], c=color, cmap=plt.cm.Spectral)
    plt.show()

example1()

def example2():
    """验证sklearn中的pca算法是否使用了数据预处理。
    本例中使用了去均值处理。
    """
    X, color = datasets.samples_generator.make_swiss_roll(n_samples=1500) # load data
    X = X - X.mean(axis=0) # 去均值
    
    pca = PCA(n_components=2) # 选择2个主成份
    pca.fit(X) # 训练
    X1 = pca.fit_transform(X) # 自适应
    print(X1)
     
    fig = plt.figure()
    ax = fig.add_subplot(211, projection='3d') # 画3d图
    ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=color, cmap=plt.cm.Spectral)
      
    ax = fig.add_subplot(212) # 画2d图
    ax.scatter(X1[:, 0], X1[:, 1], c=color, cmap=plt.cm.Spectral)
    plt.show()

example2()

def example3():
    """验证sklearn中的pca算法是否使用了数据预处理。
    本例中使用了去均值和方差处理。
    """
    X, color = datasets.samples_generator.make_swiss_roll(n_samples=1500) # load data
    
    scaler = preprocessing.StandardScaler(copy=True).fit(X)
    X = scaler.transform(X)
    
    pca = PCA(n_components=2) # 选择2个主成份
    pca.fit(X) # 训练
    
    X1 = pca.fit_transform(X) # 自适应
    print(X1)
    
    fig = plt.figure()
    ax = fig.add_subplot(211, projection='3d') # 画3d图
    ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=color, cmap=plt.cm.Spectral)
     
    ax = fig.add_subplot(212) # 画2d图
    ax.scatter(X1[:, 0], X1[:, 1], c=color, cmap=plt.cm.Spectral)
    plt.show()

example3()