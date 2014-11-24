##encoding=utf8

"""
Ref = http://python-future.org/compatible_idioms.html#dictionaries

1. 在2中 dict.keys(), dict.values(), dict.items()都是列表。
    而在3中有是三个特殊的类<class "dict_keys">, <class "dict_values">, <class "dict_items">
    所以在python3中如果需要把key或value变成列表需要用 list(dict.keys())

2. 在2中 dict.iterkeys(), dict.itervalues(), dict.iteritems()将会
    以生成器模式输出key, value。从而避免了另外建立一个list消耗额外内存
    而在3中由于dict_keys, dict_values, dict_items这三个特殊的类的存在
    for k, v in dict.items(): 默认就会以生成器的形式存在
"""

from __future__ import print_function
from six import iteritems

def different1():
    """展示python2和3中dict.keys(), dict.values(), dict.items()的不同
    """
    d = {1: "a", 2: "b", 3: "c"}
    print(type(d.keys() ) ) # in py2 <type "list">, in py3 <class "dict_keys">
    print(type(d.values() ) ) # in in py2 <type "list">, in py3 <class "dict_values">
    print(type(d.items() ) )
    
different1() # run this script in both 2 and 3

def solution():
    """python2,3中 iterkeys, itervalues, iteritems的兼容性解决方案
    """
    d = {1: "a", 2: "b", 3: "c"}
    for k, v in iteritems(d):
        print(k, v)
        
solution() # run this script in both 2 and 3
    
