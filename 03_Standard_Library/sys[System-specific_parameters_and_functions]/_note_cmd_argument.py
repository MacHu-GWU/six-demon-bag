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

"""
sys.argv 环境变量的用途

当我们从命令行运行python脚本的时候，例如 test.py，我们通常这么做：
    python test.py argument1 argument2...

    执行器 -执行器参数 被执行文件名 参数1 参数2 ...

参数之间用空格隔开

如果在命令行中调用了参数，那么argv是一个字符串列表，每个元素是参数，元素的类型是字符串
如果在命令行中没有调用参数，那么argv是一个只有一个元素的字符串列表，元素是被执行的语句名
即被执行文件名
"""

from __future__ import print_function
import sys

if __name__ == "__main__":
    for argument in sys.argv:
        print(argument, type(argument))
