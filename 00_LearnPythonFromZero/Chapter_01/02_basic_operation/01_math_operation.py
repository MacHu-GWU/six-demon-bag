##################################
#encoding=utf8                   #
#version =py27, py33             #
#author  =sanhe                  #
#date    =2014-11-01             #
#                                #
#    (\ (\                       #
#    ( -.-)o    I am a Rabbit!   #
#    o_(")(")                    #
#                                #
##################################

""""数学运算符
"""

from __future__ import print_function

print(1+2)
print(2.5-1)
print(2.5*4)        # 浮点乘以整数变成浮点
print(11/3)         # 整数/整数 在python2中还是整数
print(11.0/3)       # 浮点数/整数 或 整数/浮点数结果是浮点数
print(11%3)         # 余数
print(11.2%3)       # 余数可以
print(-2%3)         # 负数是向下取余数
print(2**3)         # 乘方
print(2**0.5)       # 开方可以用乘方的形式来计算