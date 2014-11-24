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

from __future__ import print_function
import re

""" 接 lesson02 元字符及作用中的第7点，重复 """
""" ====== 重复 ======
1. * 指定前一个字符可以被匹配零次或更多次
    ca*t 将匹配 "ct" (0 个 "a" 字符), "cat" (1 个 "a"), "caaat" (3 个 "a" 字符)等等
2. + 重复
    + 表示匹配一或更多次，至少出现一次！
    ca+t 就可以匹配 "cat" (1 个 "a")， "caaat" (3 个 "a")， 但不能匹配 "ct"。
3. ? 重复
    ? 匹配一次或零次；你可以认为它用于标识某事物是可选的。
    home-?brew 匹配 "homebrew" 或 "home-brew"
4. {m,n} 指定次数重复
    {m,n}，其中 m 和 n 是十进制整数。该限定符的意思是至少有 m 个重复，至多到 n 个重复。
"""

print(1, re.findall(r"ca*t", "xxxctttyyy") ) ## 1.匹配 "caat"
print(2, re.findall(r"ca+t", "xxxctttyyy") ) ## 2.匹配不到任何，因为+表示至少一次
print(3, re.findall(r"ca?t", "xxxctttyyy") ) ## 3.匹配 "ct"
print(4, re.findall(r"ca{3,4}t", "xxxcaaaatttyyy") ) ## 4.匹配到caaaat