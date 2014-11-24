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
str()和repr()函数的区别
"""

from __future__ import print_function
import datetime

def example1():
    """
    __str__ 用于print函数的输出
    __repr__(object) 的结果res等效于你在屏幕上输入res字符串，你就能得到一个object
    eval只作用于字符串，其结果是得到一个你在屏幕上输入该字符串所能得到的python脚本
        e.g. eval("3 >= 2") -> True
    """
    print("{:=^40}".format("example1"))
    dt = datetime.datetime(2014,1,1,10,0,0)
    print(str(dt)) # 为了显示目的而存在
    print(repr(dt)) # 所输出的字符串可以直接用于生成这个对象
    
example1()

def example2():
    """
    __repr__ 对于自定义的类，默认是没有实现__repr__方法的。所以repr方法提供了一个
    将任意自定义的类存储成字符串，而之后我们可以从字符串中完完全全的恢复该对象。
    对于用户自定义的类，有些时候pickle.dump会失效，但如果我们定义了__repr__那么
    我们就可以把任意的对象都保存成字符串，放入pickle中或者是数据库中
    
    一个可以被字符串化和从字符串生成的类应该具有以下特点：
    1. 所有的属性参数都可以在初始化时被初始化。（所以不要有某些方法可以在初始化之后
        又生成一个新的属性。尽量在初始化时就赋予初始值）
    
    """
    class person(object):
        def __init__(self, name, age = 0):
            self.name = name
            self.age = age
            
        def grow_up(self, years = 1):
            self.age += years
        
        def rename(self, newname):
            self.name = newname
        
        def __str__(self):
            return "My name is %s, I am %s years old now." % (self.name, self.age)
        
        def __repr__(self):
            return "person(name='%s',age=%s)" % (self.name, self.age)
    
    print("{:=^40}".format("example2"))
    sam = person("Sam")
    sam.grow_up(15)
    print(sam)
    p_repr = repr(sam) # dump to string
    print(p_repr)
    jack = eval(p_repr) # load from string
    jack.grow_up(3)
    jack.rename("Jack")
    print(jack)
    
example2()