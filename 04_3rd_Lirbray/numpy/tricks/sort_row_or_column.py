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
在数据分析的时候，很多时候会想要把矩阵中的每一行，或者每一列"独立"的各自排序。
本文档内容就是为了解决这一问题的。
[ref]: http://docs.scipy.org/doc/numpy/reference/generated/numpy.sort.html
"""

from __future__ import print_function
import numpy as np
a = np.array([[1,3,7],
              [3,1,5],
              [2,6,8]])

def example1():
    """ 所有元素排序，并且压平到向量 """
    print("=== 原始数据为 ===\n%s\n" % a)
    print(np.sort(a, axis = None))
    print(np.sort(a, axis = None)[::-1]) ## [重要技巧！]逆序输出结果

example1()

def example2():
    """ 按列排序，即每列中的元素，内部进行排序 """
    print("=== 原始数据为 ===\n%s\n" % a)
    print("每列数据正序排列\n%s\n" % np.sort(a, axis = 0) )
    print("每列数据逆序排列\n%s\n" % np.sort(a, axis = 0)[::-1] )## [重要技巧！]逆序输出结果

example2()

def example3():
    """ 按行排序, 即每行中的元素，内部进行排序 """
    print("=== 原始数据为 ===\n%s\n" % a)
    print("每行数据正序排列\n%s\n" % np.sort(a, axis = 1) )
    print("每行数据逆序排列\n%s\n" % 
          np.sort(a, axis = 1).transpose()[::-1].transpose() )## [重要技巧！]逆序输出结果
    
example3()