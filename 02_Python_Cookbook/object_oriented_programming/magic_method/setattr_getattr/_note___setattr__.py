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

"""
def __setattr__ (self, attr, value): return X ---> defines the behavior of self.attr = value
"""

from __future__ import print_function

def example1():
    """False example, don't do this
    这是因为在创建t = Tree()的时候，调用了__init__中的self.data = dict()
    于是这个操作又调用了__setattr__(self, data, dict()), 而这时还没有创建self.data呢
    所以会提示找不到attribute data.
    
    总结：
        一旦我们overwrite了__setattr__方法之后，在__init__中的所有属性的初始化赋值
        都会受到严重影响。解决的方法请看example2和example3
    """
    class Tree(object):
        def __init__(self):
            self.data = dict() # AttributeError: 'Tree' object has no attribute 'data'
            
        def __setattr__(self, attr, value):
            self.data.setdefault(attr, value)
            
    t = Tree()
    t.item = 3
    
# example1()

def example2():
    """
    由于Tree方法是从object(python的class基类)继承而来。我们overwrite的是Tree中的__setattr__方法，
    而object.__setattr__(obj, attr, value)还没有被overwrite，那么我们就可以用这个命令进行属性初始化
    """
    class Tree(object):
        def __init__(self):
            object.__setattr__(self, "data", dict())
            
        def __setattr__(self, attr, value):
            self.data[attr] = value
            
    t = Tree()
    t.node1 = 3
    print(t.data)
    print(t.data["node1"])
    
example2()