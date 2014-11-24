##coding=utf8

from __future__ import print_function
import pprint as ppt

def prt_both(ob):
    """打印对象以及对象类型"""
    print("%s - %s" % (ob, type(ob)) )

def example1():
    """打印文本的原始字符码
    因为有的时候原来文本中的空行可能是 \n, \r, \t中得一种
    那么用以下技巧可以查看空行的真实字符码
    """
    with open("readme.txt", "rb") as f:
        text = f.read()
    res = text.split("\n")
    ppt.pprint(res)
    
example1()