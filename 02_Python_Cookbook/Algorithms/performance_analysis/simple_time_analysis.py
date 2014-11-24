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
import timeit

def test():
    a = [i for i in range(100000)]
    return a

a = test()

tt = \
"""
def test():
    a = [i for i in range(100000)]
    return a

test()
"""
print(timeit.timeit(tt, number = 1))
print(timeit.timeit('a = "-".join([str(n) for n in range(100)])', number=10000))