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

def example1():
    """两个函数的私有函数虽然有相同的函数名，但是并不会互相误用
    """
    def process1():
        def operation(a):
            return a+1
        b = 1
        print(operation(b))
    
    process1()
    
    def process2():
        def operation(a):
            return a+2
        b = 1
        print(operation(b))
    
    process2()
    
example1()