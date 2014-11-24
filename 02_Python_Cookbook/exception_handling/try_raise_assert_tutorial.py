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
    """try... except... clause
    try之后的语句中如果不出错，那么就一直执行下去；
    如果出错，则终端并跳转执行except之后的语句。
    try所包含的语句出错不会中断程序运行
    """
    try:
        a = 1
        b = 1
        b -= 1
        print(a/b)
    except:
        print("denominator can not be 0")
        
# example1()

def example2():
    """raise...
    强制抛出一个异常，并中断程序。
    通常在try... except...中的except从句中出现
    """
    try:
        res = 1/0
    except:
        raise Exception("0 CANNOT be the denominator")
    print("see if we can get here")
    
# example2()

def example3():
    """或是通过条件判断 if 抛出异常
    """
    a = 1
    if a > 0:
        raise Exception("something wrong")
    print("see if we can get here")
    
# example3()

def example4():
    """assert...
    assert 后面的条件若是不满足，那么就会抛出assert异常
    assert a_condition 可以粗略的认为等效于：
    
    if not condition:
        raise AssertionError()
    """
    # assert 1 > 2
    assert isinstance([1,2,3], set)
        
# example4()