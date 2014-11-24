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

""" 官方文档： https://docs.python.org/2/library/re.html """

from __future__ import print_function
import re

""" ====== 正则能用来干什么？ ======
在字符串匹配中的两个定义：模式串，匹配串
模式串：我们要寻找的目标串，其具有某种模式，所以叫模式串
匹配串：被我们在其中搜索的源字符串本身，被称作匹配串
"""
""" ====== 什么是正则 regular expression ： re ======
正则就是根据编程语法，用正则代码表示模式串，然后用高速的正则算法
从匹配串中找到能匹配的模式串。所以学习正则，实际上是学习如何用
正则代码表示各种模式，请看下面的例子:

    re.findall(模式串，匹配串)是re中最主要的函数，其功能是：
    re.findall(模式串，匹配串) => 返回所有匹配结果的列表
"""

print(re.findall("abc","xxxabcxxx")) ## 返回 ["abc"]

