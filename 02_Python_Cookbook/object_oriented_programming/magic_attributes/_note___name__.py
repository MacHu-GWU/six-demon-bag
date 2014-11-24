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

"""
from __future__ import print_function

""" ================ 定义 ================
    __name__是.py文件的内部属性。主要用来进行模块测试。方法如下：
    当该.py文件是在被直接运行的时候，__name__返回"__main__"
    如果.py文件是在被import调用，__name__返回"调用名"，例如：
    在本脚本中输入
    import math
    print(math.__name__)
    >> math
    作为经常被调用的模块中，如果有那么一行：if __name__ == "__main__"
    则如果该文件被别的文件import了，那么if之后的表达式都不会执行。
    此技巧通常被用于单元测试
"""

print("本脚本的__name__属性：", __name__)

import math
print("当前被调用的math.py文件的__name__属性：", math.__name__)

