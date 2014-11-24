##################################
#encoding=utf8                   #
#version =py27, py33             #
#author  =sanhe                  #
#date    =2014-11-15             #
#                                #
#    (\ (\                       #
#    ( -.-)o    I am a Rabbit!   #
#    o_(")(")                    #
#                                #
##################################
# Ref=https://docs.python.org/2/library/collections.html?highlight=ordereddict#collections.namedtuple

""" [nametuple]
nametuple是一个简单的，一个名字，多个属性的数据类型。
比如，一个人就是这个类的名字，多个属性有:
    lastname
    firstname
    age
    address
    SSN
collections.nametuple只是预先帮人们封装好了这种对象的类的定义，
免去了自己写类的麻烦。非常的方便。下面两种方法可以创建nametuple类

第一种， 用列表定义属性, verbose=True 表示print的时候，顺带打印类定义
的字符串
Point = collections。namedtuple("Point", ["x", "y"], verbose=True)

第二种， 用字符串定义属性，属性名称用逗号隔开
Point = collections.namedtuple("Point", "x, y", verbose=False)
"""

from __future__ import print_function
import sys
from collections import namedtuple

def demo_nametuple1():
    Point = namedtuple("Point", "x, y", verbose=False)
    p = Point(x=11, y=22)
    print(p.x, p.y) ## 用属性名调用值
    
    p1 = Point(33, 44)
    print(p1) ## 用人类可读的语言打印Point对象
    
demo_nametuple1()