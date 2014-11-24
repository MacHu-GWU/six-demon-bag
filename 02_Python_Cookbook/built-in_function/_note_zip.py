##################################
#encoding=utf8                   #
#version =py27, py33             #
#author  =sanhe                  #
#date    =2014-10-29             #
#                                #
#    (\ (\                       #
#    ( -.-)o    I am a Rabbit!   #
#    o_(")(")                    #
#                                #
##################################

from __future__ import print_function

def example1():
    """压缩和解压缩
    """
    x = [1, 2, 3]
    y = [4, 5, 6]
    zipped = zip(x, y)
    print(zipped)
    
    tuple_list = [(1, 2), (3, 4), (5, 6)]
    x1, y1 = zip(*tuple_list)
    print(x1, y1)

example1()

def example2():
    """星号*作为拆分tuple的标志符的用法
    """
    def add3(a,b,c):
        return a+b+c
    
    a, b = 1, (2,3)
    print(add3(a, *b))
    
example2()