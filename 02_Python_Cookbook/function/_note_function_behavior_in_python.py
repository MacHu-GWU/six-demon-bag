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

from __future__ import print_function

def add1(base, add):
    return base + add
print(add1(5,3))

def add2(a):
    def delta(t):
        return t + a
    return delta
print(add2(5)(3)) ## add(a) = delta 其中 a = 3
