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

""" ====== 前后向界定 ======
    (?<=...)be proceded by 前向是... 
    (?<!...)not be proceded by前向不是...
    (?=...)match next 后面跟着的是...
    (?!...)not match next 后面跟着的不是...

最常用的模板：
    前缀 + 任意字符 重复若干次 + 后缀
    r"(?<=前缀)[\s\S]{1,10}(?=后缀)"
"""

p = r"""(?<=发行日期:</td><td class="text">).{1,10}(?=</td>)""" ## .{1,10} 表示中间重复1-10次
text = """<td class="header">发行日期:</td><td class="text">2013-06-01</td>"""
print(re.findall(p,text))
