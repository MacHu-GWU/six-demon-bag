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
c风格的字符串格式化输出语法介绍
"""

from __future__ import print_function

def example1():
    print("{:=^40}".format("example1"))
    
    print("this list is: %s" % [1,2,3]) # 一个需要被字符串化的对象
    
    name, age = "bob", 21
    print("my name is: %s, my age is: %s" % (name, age)) # 多个需要被字符串化的对象要被放在元组中
    
    print("answer1 = %.2f, answer2 = %f" % (3.1415926, 5)) # %f是浮点数输出
    
    print("answer1 = %i" % 3.1415926) # %i 是整数输出
    
example1()