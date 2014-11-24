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
许多时候我们有一个函数f, 由于一些随机因素，有可能成功，也有可能不成功。所以我们在程序中有这样的需要：
    对某个不确定成功的函数尝试N次，如果N次都不成功，抛出不成功所带来的异常。如果成功，就继续进行下去。
用户可以自定义是否将异常写入日志
"""

from __future__ import print_function
import random

def rand_string(length):
    """length fixed random string generator"""
    test_chars = u"0123456789abc"
    return "".join([random.choice(test_chars) for i in range(length)])

def convert_int(length):
    """将随机字符串转化为整数。由于随机字符串有可能出现abc，所以有一定概率失败
    """
    s = rand_string(length)
    return int(s)

def tryit(howmany, func, *argv, **kwarg):
    """这个函数使用了一个重要的技巧将原函数的参数原封不动的封装成tryit这个函数的参数了
    用户只要跟使用func原函数一样使用tryit函数就好了，只不过在前面多了两个howmany和func的参数
        howmany 是尝试次数
        func 是你所要尝试的函数
        *argv, **kwarg 是func中的参数
    """
    flag = 1
    while flag <= howmany:
        try:
            return func(*argv, **kwarg)
        except Exception as e:
            flag += 1
    raise e

if __name__ == "__main__":
    """在主程序中，我们只需要用一个简单的try except调用tryit就可以了"""
    try:
        print(tryit(3, convert_int, 10) )
    except Exception as e:
        print(e) # 当然用户也可以选择把异常写入日志