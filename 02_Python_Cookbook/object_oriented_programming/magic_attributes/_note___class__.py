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
在python中一切都是对象。任何对象在python中都有__class__这个属性，其中储存的是该对象所属的类

在python中有一个特殊的元类type，任何类的所属的类都是这个类继承过来的。
比如说list, dict, set这些对象都是从type继承而来的
"""

from __future__ import print_function
from datetime import datetime

dt = datetime(2014,1,1,6,30,0)
print(dt.__class__) # dt的类是datetime
print(type(dt))
print(dt.__class__ == type(dt))

print(dt.__class__.__class__) # datetime是从type继承而来的
print(dt.__class__.__class__.__class__) # type本身也是从type继承而来的

def add2(a, b):
    return a + b

print(add2.__class__) # add2的类是function
print(add2.__class__.__class__) # function也是从type继承而来的 