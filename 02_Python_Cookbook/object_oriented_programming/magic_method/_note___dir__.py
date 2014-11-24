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
__dir__ 方法定义的是 dir(class)的行为
返回的是class的所有方法名 和 属性名
"""

from __future__ import print_function
from datetime import datetime

print(dir(datetime))