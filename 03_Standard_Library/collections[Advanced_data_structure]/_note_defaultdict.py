##################################
#encoding=utf8                   #
#version =py27, py33             #
#author  =sanhe                  #
#date    =2014-11-15             #
#                                #
#    (\ (\                       #
#    ( -.-)o    I am a Rabbit!   #
#    o_(")(")                    #
#                                #
##################################
# Ref=https://docs.python.org/2/library/collections.html?highlight=ordereddict#collections.defaultdict

""" [带默认值的字典 defaultdict]
个人认为用处不大
"""

from __future__ import print_function
from collections import defaultdict

def demo1():
    s = [("yellow", 1), ("blue", 2), ("yellow", 3), ("blue", 4), ("red", 1)]
    d = defaultdict(list)
    for k, v in s:
        d[k].append(v)
    print(d)
    
demo1()    