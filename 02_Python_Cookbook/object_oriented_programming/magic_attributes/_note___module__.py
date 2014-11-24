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
__module__ 是所有类的内置定义，不可作用与被实例化的类。

官方定义：
The name of the module the function was defined in, or None if unavailable. Writable.
"""

from __future__ import print_function
from datetime import datetime

class Person(object):
    def __init__(self, name, date_of_birth):
        self.name = name
        self.dob = date_of_birth
        
print(Person.__module__) # object的模块名是__main
print(datetime.__module__, type(datetime.__module__) )

dt = datetime(2014,1,1,6,30,0)
print(dt.__module__, type(dt.__module__)) # 实例没有__module__属性
