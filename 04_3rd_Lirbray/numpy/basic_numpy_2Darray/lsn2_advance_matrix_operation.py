##################################
#encoding=utf8                   #
#version =py27, py33             #
#author  =sanhe                  #
#date    =2014-11-01             #
#                                #
#    (\ (\                       #
#    ( -.-)o    I am a Rabbit!   #
#    o_(")(")                    #
#                                #
##################################

"""
矩阵乘法
矩阵求逆
矩阵除法
向量乘法，内积
对角阵
二范数
解有解的线型方程组
矩阵分解
"""

from __future__ import print_function
import numpy as np
import numpy.linalg as npl

def example1():
    """ Matrix dot with Matrix 矩阵相乘 """
    A = np.array([[1,2],
                  [3,4]])
    B = np.array([[2,0],
                  [0,2]])
    print(np.dot(A,B) )

# example1()

def example2():
    """ 矩阵求逆 """
    A = np.array([[7,3,9],
                  [4,1,8],
                  [5,6,2]])
    print(npl.inv(A) )## 矩阵求逆

# example2()

def example3():
    """ 矩阵相除 """
    A = np.array([[1,2],
                  [3,4]])
    B = np.array([[2,0],
                  [0,2]])
    C = np.dot(A,B)
    print(np.dot(C, npl.inv(B) ) )## 矩阵相除 等于 乘以逆矩阵

# example3()

def example4():
    """ Vector dot vs Vector 向量 相乘 """
    A, B = np.array([1,2,3]), np.array([-1,0,1])
    print(np.vdot(A,B) )## 向量相乘默认内积
    print(np.inner(A,B) )## 内积
    print(np.outer(A,B) )## 外积

# example4()

def example5():
    """ 求矩阵对角元素 """
    A = np.array([[7,3,9],
                  [4,1,8],
                  [5,6,2],
                  [8,8,8]])
    print(np.diagonal(A) )## 求对角元素

    """ 从向量建立对角阵 """
    A = np.array([1,2,3])
    print(np.diag(A) )## 从向量生成对角阵
    
# example5()

def example6():
    """ 求二范数 """
    A = np.array([3,4])
    B = np.array([[3,4],
                  [1,2]])
    print(npl.norm(A) )## 求标准二范数 
    print(npl.norm(B, axis = 0) )## 基本上所有对向量的操作符，当操作对象为矩阵时，都可以通过设置
    print(npl.norm(B, axis = 1) )## axis = 0 or 1 来决定是对行向量操作或是对列向量操作

# example6()

def example7():
    """ 解有解的线性方程，无解则会报错 """
    X = np.array([[3,1],[2,4]])
    y = np.array([8,9])
    print(npl.solve(X,y) )

example7()

""" Matrix Decomposition 矩阵分解 """

def example8():
    """ 奇异值分解 """
    A = np.array([[7,3,9],
                  [4,1,8],
                  [5,6,2]])
    U,d,V = npl.svd(A) ## 在python中SVD的结果是： U * diag(d) * V = A
    print("=== 原矩阵 ===\n%s\n" % A)
    print("U = \n%s\n" % U) ## 正交阵
    print("d = \n%s\n" % d) ## 对角线元素
    print("V = \n%s\n" % V) ## 正交阵
    D = np.diag(d) ## 生成对角阵
    print("验证q的正交性:\n%s\n" % np.dot(np.dot(U, D), V) )## 计算 U * diag(d) * V
    
# example8()

def example9():
    """ QR 分解  以及 Gram Schmidt 标准正交化"""
    A = np.array([[1,1,6],  ## [注意] numpy.linalg 是对列向量进行标准正交化
                  [1,2,4],
                  [1,3,2]])
    q, r = npl.qr(A)
    print("半正交矩阵q:\n%s\n" % q)
    print("上三角矩阵r:\n%s\n" % r)
    print("验证q的正交性:\n%s\n" % np.dot(q, q.transpose()) )
    
# example9()