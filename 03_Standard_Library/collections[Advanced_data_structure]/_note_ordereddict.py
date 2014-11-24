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
# Ref=https://docs.python.org/2/library/collections.html?highlight=ordereddict#ordereddict-objects

from __future__ import print_function
import sys
from collections import OrderedDict

def demo_OrderedDict():
    """ [有序字典]
    可以对字典的 key: value对，根据key或者 value自由升序或者降序排序输出
    """

    d = {"c":1,
         "a":3,
         "b":2}
    od = OrderedDict( sorted(list(d.items()), 
                             key=lambda t: t[1], ## t[0]指根据key排序, t[1]指根据value排序
                             reverse = False) ) ## True指逆序排序，False指正序排序
    for k,v in list(od.items()):
        print(k,v) ## 看看是否按照设定有序输出
    print("原始字典占用内存大小为: %s" % sys.getsizeof(d)) ## 普通字典和有序字典
    print("有序字典占用内存大小为: %s" % sys.getsizeof(od)) ## 占用的空间大小其实是一样的

demo_OrderedDict()
