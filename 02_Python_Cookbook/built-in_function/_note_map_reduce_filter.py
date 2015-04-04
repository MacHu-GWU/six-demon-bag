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
try:
    from functools import reduce
except:
    pass
def example1():
    """map是通过一个函数，将iterable中的元素批量的通过该函数映射到新的iterable对象上
    """
    def add1(value):
        return value + 1
    
    l = [1,2,3,4,5]
    print(map(add1, l))
    
# example1()

def example11():
    def add2value(value1, value2):
        return value1 + value2
    l = [(1,2), (3,4)]
    
    print(map(add2value, *l))
    
# example11()

def example2():
    """reduce是将一个iterable object中的元素, 1和2算, 结果再和3算, 结果再和4算, 这样不断reduce的过程
    文档: http://www.python-course.eu/lambda.php
    
    在python2中reduce是built-in
    在python3中，需要 from functools import reduce
    """
    a = [1,2,3,4,5]
    print(reduce(lambda x, y : x + y, a) )

# example2()

def example3():
    """filter是通过一个能返回boolean值的函数，对iterable中的元素进行筛选。如果函数
    返回真，则留下；反之，抛弃
    
    讨论：
        在python2中，filter返回的是经过筛选之后的iterable对象。原对象如果是列表
        那么返回的也是列表。
        
        在python3中，filter返回的值filter object，其实是指向筛选后的iterable的一串
        指针。
        
        所以在性能上python3中的filter的速度要成千倍的高于python2中返回实际的对象。
        但是python2中返回的是实际对象，你可以对它进行赋值，循环等任意操作。而filter指针
        对象你在用for调用过其中的元素一次之后，就无法再次进行利用了。
    """
    def ispos(value):
        if value >= 0:
            return True
        else:
            return False
    
    l = [-1, 2, -2, 3, -3]
    print(filter(ispos, l))
    
# example3()
