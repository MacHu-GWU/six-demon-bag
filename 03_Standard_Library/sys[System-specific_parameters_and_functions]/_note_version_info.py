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
import sys

print(sys.version, type(sys.version)) # python版本信息的字符串
print(sys.version_info, type(sys.version_info), sys.version_info.major) # python版本信息的具体信息

print(sys.platform)             # 操作系统名称
print(sys.getwindowsversion())  # windows版本信息

print(sys.exec_prefix)  # python编译器安装目录
print(sys.executable)   # python可执行文件路径

