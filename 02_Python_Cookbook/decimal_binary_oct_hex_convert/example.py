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

def prt_dtype(ob):
    """打印对象以及对象类型"""
    print("%s - %s" % (ob, type(ob)) )
    
def example1():
    """十进制转其他进制
    python built-in function: bin(), oct(), hex()
        output: type = string
    """
    prt_dtype( bin(31) )
    prt_dtype( oct(31) )
    prt_dtype( hex(31) )
    
example1()

def example2():
    """其他进制转十进制
    python built in fucntion: int( string_int, format)
        output: type = int
    """
    prt_dtype( int("11111", 2) )
    prt_dtype( int("37", 8) )
    prt_dtype( int("1f", 16) )

example2()

def example3():
    """其他进制之间互相转化
    """
    prt_dtype( bin(0x1f) )
    prt_dtype( hex(0b11111))

example3()