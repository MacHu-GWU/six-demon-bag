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

""" 接 lesson02 元字符及作用中的第6点，预定义字符集 """
""" ====== 以\开头的 特殊预定义字符集 ======
    \d  匹配任何十进制数；它相当于类 [0-9]。
    \D  匹配任何非数字字符；它相当于类 [^0-9]。
    \s  匹配任何空白字符；它相当于类  [ \t\n\r\f\v]。
    \S  匹配任何非空白字符；它相当于类 [^ \t\n\r\f\v]。
    \w  匹配任何字母数字字符；它相当于类 [a-zA-Z0-9_]。
    \W  匹配任何非字母数字字符；它相当于类 [^a-zA-Z0-9_]。
    \b  匹配任何空白字符，和\s不同的是仅限于位于单词的两边，只匹配单词本身，不匹配空格本身
    \B  匹配任何非空白字符，和\b相反
    . 匹配任何东西，除了换行符\n, 如果要真的做到匹配任何东西，可以用[\s\S]*
"""
print(1, re.findall(r"\d", "abc123defg") ) ## 1.匹配到 1, 2, 3
print(2, re.findall(r"\D", "abc123defg") ) ## 2.匹配到 abcdefg
print(3, re.findall(r"\s", "abc 123 defg") ) ## 3.匹配到 两个空格
print(4, re.findall(r"\S", "abc 123 defg") ) ## 4.匹配到 abc123defg
print(5, re.findall(r"\w", "abc 123 defg") ) ## 5.匹配到 abc123defg
print(6, re.findall(r"\W", "abc 123 defg") ) ## 6.匹配到 两个空格
print(7, re.findall(r"\babc\b", " abc ") ) ## 7.匹配到 "abc", 如果\sabc\s则会匹配到 " abc "
print(8, re.findall(r"\B", " abc ") ) ## 8.匹配到任何空字符
print(9, re.findall(r".", "abc 123 defg") ) ## 9.匹配到 所有字符
print(10, re.findall(r".{1,3}", "中文") ) ## 10.匹配到 "中" 注意，一个中文在utf-8编码中算3个字符