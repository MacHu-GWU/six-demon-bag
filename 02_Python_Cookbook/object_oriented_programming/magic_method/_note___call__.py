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
__call__是把类本身当作一种方法来调用

也就是 类名(*参数) 这样调用

"""

from __future__ import print_function

class g_dpm(object):
    def __init__(self, g):
        self.g = g

    def __call__(self, t):
        return (self.g * t ** 2) / 2
    
e_dpm = g_dpm(9.8)
print(e_dpm(3))