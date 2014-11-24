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
__new__：创建对象时调用，返回当前对象的一个实例，相当于java里面的构造器差不多

__init__：创建完对象后调用，对当前对象的实例的一些初始化，无返回值

__new__
    accepts a type as the first argument, and (usually) returns a new instance of that type. 
    Thus it is suitable for use with both mutable and immutable types.

__init__ accepts an instance as the first argument and modifies the attributes of that instance. This is inappropriate for an immutable type, as it would allow them to be modified after creation by calling obj.__init__(*args)

"""

from __future__ import print_function

x = (1, 2)
x.__init__((3, 4, 5))
print(x)

y = [1, 2]
y.__init__([3, 4, 5])
print(y)