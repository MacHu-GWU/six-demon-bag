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
# Ref=https://docs.python.org/2/library/collections.html?highlight=ordereddict#counter-objects

""" [高级计数器 Counter]
counter 可以理解为一个频率统计计数器。
1. 支持从可迭代对象中生成counter
2. 把counter的keys, values, items 转化成各种经典数据结构
3. 很方便的往容器里添加，删除元素
4. 支持数学操作符运算
"""

from __future__ import print_function
from collections import Counter

def demo1_initial():
    """Counter对象的初始化
    """
    c = Counter()                           # a new, empty counter
    c = Counter("gallahad")                 # a new counter from an iterable
    print("counter = %s" % c)
    
    c = Counter({"red": 4, "blue": 2})      # a new counter from a mapping
    print("counter = %s" % c)
    
    c = Counter(cats=4, dogs=8)             # a new counter from keyword args
    print("counter = %s" % c)
    
demo1_initial()

def demo2_getitem():
    c = Counter("abbccc")
    print("""c["c"] = %s""" % c["c"]) # get a item exists
    print("""c["d"] = %s""" % c["d"]) # get a item not exists
    print("c.keys() = %s" % list(c.keys()))
    print("c.values() = %s" % list(c.values()))
    print("c.items() = %s" % list(c.items()))
    print("c.elements() = %s" % list(c.elements())) # expand the dict
    
demo2_getitem()

def demo3_method():
    c = Counter("abbccc")
    print("c.most_common(3) = %s, c.most_common(4) = %s" % (c.most_common(3), c.most_common(4)))
    
    c.subtract("ab") ## 从 abbccc 中减去了 ab，相当于减法,和 c - Counter("ab")不同的是，保留负值
    print(c)
    
    c.update("ab") ## 从 bccc 中加上了 ab，相当于加法
    print(c)

demo3_method()

def demo4_math_operation():
    """ some math operation in between two counter
    """
    c = Counter(a=3, b=1)
    d = Counter(a=1, b=2)
    print(c + d)                       # add two counters together:  c[x] + d[x]
    print(c - d)                       # subtract (keeping only positive counts)
    print(c & d)                       # intersection:  min(c[x], d[x])
    print(c | d)                       # union:  max(c[x], d[x])
    
demo4_math_operation()
    