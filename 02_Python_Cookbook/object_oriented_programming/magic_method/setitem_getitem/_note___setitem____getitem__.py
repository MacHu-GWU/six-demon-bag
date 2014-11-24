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
def __setitem__ (self, key, value): return X ---> defines the behavior of self[key] = value
def __getitem__ (self, value): return X ---> defines the behavior of self[value]
"""
from __future__ import print_function

def example1():
    """
    list like slicing get item
    """
    class Container(object):
        def __init__(self):
            self.list = list()
        
        def __getitem__(self, key):
            return self.list[key]
        
        def __setitem__(self, key, value):
            self.list[key] = value
    
    print("{:=^40}".format("example1"))
          
    c = Container()
    c.list += [1,2,3,4,5]
    print(c[1:4])
    c[2] = 999
    print(c[2])
    
example1()

def example2():
    """
    dict like get item
    """
    class Container(object):
        def __init__(self):
            self.dict = dict()
        
        def __getitem__(self, key):
            return self.dict[key]
        
        def __setitem__(self, key, value):
            self.dict.setdefault(key, value)
    
    print("{:=^40}".format("example1"))
         
    c = Container()
    c.dict[1] = "bob"
    c[2] = "jack"
    print(c[1])
    print(c[2])
    c[2] = "tom"
    print(c[2])
    
example2()
