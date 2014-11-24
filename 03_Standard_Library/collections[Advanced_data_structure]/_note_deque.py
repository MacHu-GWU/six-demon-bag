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
# Ref=https://docs.python.org/2/library/collections.html?highlight=ordereddict#collections.deque

""" [高级链表 deque]
deque可以理解为一个：
1. 支持头尾插入，删除操作的链表
2. 支持循环位移的环形链表
而在初始化的时候，语句是： d = deque(iterable_object, max)
d是一个大小为max的双头FIFO，然后对iterable_object中的iter，填充到FIFO中
"""

from __future__ import print_function
import sys
from collections import deque

def demo_deque1():
    """deque 的初始化
    """
    l = [1,2,3]
    d = deque([1,2,3])
    print("print d = %s" % d)
    print("原始列表占用内存大小为: %s" % sys.getsizeof(l)) ## 普通列表占用空间小
    print("高级列表占用内存大小为: %s" % sys.getsizeof(d)) ## 高级列表占用空间大，插入删除速度快
    d1 = deque([1,2,3,4], 3) ## 像一个大小为3的fifo一样，按照顺序填充deque
    print(d1)
    d1.append(4)
    print(d1) # left append
    d1.appendleft(5)
    print(d1)
    
# demo_deque1()

def demo_deque2(): ## [注意]请每次解除注销掉一个方法的代码进行演示
    """deque方法演示
    """
    """ a1 从后面插入"""
    d = deque([1,2,3])
    print("之前是%s" % d)
    d.append(4) # append
    print("之后是%s" % d)
    
    """ a2 从前面插入"""
    d = deque([1,2,3])
    print("之前是%s" % d)
    d.appendleft(4) # appendleft
    print("之后是%s" % d)
    
    """ b1 从后面取出"""
    d = deque([1,2,3])
    print("之前是%s" % d)
    print(d.pop()) # pop
    print("之后是%s" % d)
    
    """ b2 从前面取出"""
    d = deque([1,2,3])
    print("之前是%s" % d)
    print(d.popleft()) # popleft
    print("之后是%s" % d)
    
    """ c1 从后面批量插入"""
    d = deque([1,2,3])
    print("之前是%s" % d)
    print(d.extend([4,5])) # extend
    print("之后是%s" % d)
    
    """ c2 从前面批量插入"""
    d = deque([1,2,3])
    print("之前是%s" % d)
    print(d.extendleft([4,5])) # extendleft
    print("之后是%s" % d)
    
    """ d 全列表循环向右边移 """
    d = deque([1,2,3])
    print("之前是%s" % d)
    d.rotate(1)
    print("之后是%s" % d)

# demo_deque2()

def demo_deque3():
    def slide_window(iterable, size):
        fifo = deque(maxlen=size)
        for i in iterable:
            fifo.append(i)
            if len(fifo) == size:
                yield fifo
                
    array = [1,2,3,4,5,6,7,8,9,10]
    for window in slide_window(array, 3):
        print(window)
        
demo_deque3()