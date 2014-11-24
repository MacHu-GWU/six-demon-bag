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
__dict__ 是将对象所有的属性和其值变成字典的形式输出。
当我们定义新类的时候，如果是从object继承而来的，那么就也会继承__dict__这个属性
从而实现__dict__的功能。

但是并不是所有的对象都定义了__dict__这个属性。比如一些built-in对象，列表，字典
"""

from __future__ import print_function

def example1():
    class Person(object):
        def __init__(self, name, date_of_birth):
            self.name = name
            self.dob = date_of_birth
            
    
    p = Person("bob", "1993-01-01")
    print(p.__dict__)
    
    LIST = [1,2,3,4]
    DICT = {"a":1, "b":2}
    print(LIST.__dict__, DICT.__dict__)
    
example1()