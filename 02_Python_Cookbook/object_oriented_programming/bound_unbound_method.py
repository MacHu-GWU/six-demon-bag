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
    """bound method和unbound method的区别
    调用bound method时必须建立一个类的实例
    调用unbound method时可以直接通过 类名.方法名(参数) 直接调用
    """
    class MyClass(object):
        def bound_add(self, value): # bound method
            print(100 + value)
        
        @staticmethod
        def unbound_add(value): # unbound method
            print(100 + value)
            
    MyClass().bound_add(3) # call a bound method
    MyClass.unbound_add(3) # no need to create an instance to call this unbound method
    MyClass.bound_add(3) # Error! To call bound method have to create an instance first
    
example1()