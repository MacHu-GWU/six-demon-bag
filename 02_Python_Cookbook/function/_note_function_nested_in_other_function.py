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

"""============= PROBLEM description ============
[EN] How to take a function as an input parameter in another function
[CN] 如何实现把函数对象本身当作一个参数传入另外一个函数中。
"""

from __future__ import print_function

def add1(a):
    return a+1

def add100(a):
    return a+100

def example1():
    """
    [Chn][推荐]由于python中函数本身也是一个对象，函数中的参数当然也是对象，所以可以直接把函数名当成参数传入函数
    [Eng][Recommended]Because everythin even a function is an object in python, so we can simply
    take the function name as an input parameter in another function
    """    
    def do_something1(add, num):
        print(add(num)) ## <== function name is the parameter
    
    do_something1(add1, 100)
    do_something1(add100, 100)

example1()

def example2():
    """ Method 2
    [Chn][不推荐]eval命令是把字符串转化为纯python命令， 比如"int("3")"这是一个字符串，而eval("int("3")")的结果就是
    int("3")等于3. 这个技巧可以比较简单粗暴的用字符串代表函数表达式
    [Eng][Avoid this]there"s a very useful built-in function "eval", it takes any strings and convert it to 
    pure python expression. Which means: eval("int("3")") = int("3") = 3. But this trick are not recommended
    """
    def do_something2(mode, num):
        print(eval(mode)(num)) ## <==
        return None
    
    do_something2("add1", 100)
    do_something2("add100", 100)

example2()