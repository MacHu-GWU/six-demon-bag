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

""" =========================
           M e t h o d
    =========================
"""
""" match object 匹配对象的定义，参考文献
    http://docs.python.org/3.3/library/re.html#match-objects
"""
""" === re.compile ===
    Compile a regular expression pattern into a regular expression object,
    which can be used for matching using its match() and search() methods,
    described below.
    凡是需要用到很多次的模式，用compile能大大增加运行速度，不需要每次都对模式进行编译
"""

# p = re.compile(r"\b(?:ab)+\b") ##ab重复多次，并且前后是空格 
# text = "ababab abbabb aabaab"
# result = p.match(text) ##p是模式类，result是匹配类
# print(result)

""" === re.findall ===
    return a list of all non-overlapping matches in the string
"""

p = r"\b\d{3}\b"
text = "1 22 333 4444 55555 666666"
ans = re.findall(p,text)
print(ans)

""" === re.IGNORECASE ===
忽略大小写模式
"""

p = re.compile(r"\ba\b", re.IGNORECASE) 
text = "a A b B"
ans = re.findall(p,text)
print(ans)
