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

import os, shutil

"""
本文包含了了os和shutil模块中关于文件和文件夹操作的函数
的详细介绍，区别和注意事项
"""

""" === 删除操作 ===
1. 删除单个文件 - os.remove
2. 删除单个空目录 - os.rmdir
3. 删除整个目录 - shutil.rmtree
"""

""" === 拷贝操作 ===
1. 拷贝单个文件 - shutil.copy    shutil.copy2 可以设置buffer以节约内存
2. 拷贝整个目录 - shutil.copytree

copy和copy2的深度解析
    copy是创建一个新文件，即不拷贝metadata
    copy2是包括metadata在内的拷贝文件，连创建时间都会被拷贝过去

    无论是copy还是copy2，如果dst文件已经存在，那么就会覆盖该文件
    如果dst是一个目录，那么文件就会被自动拷贝到该目录下，同理如果
    目录下已有同文件名的文件，那么该文件会被覆盖
        注：由于会覆盖文件，所以有一定的危险性
"""

""" === 移动操作 ===
1. 移动单个文件或整个目录树 - shutil.move
    如果dst是一个目录，那么同copy，文件或目录树就会被自动移动到该目录
    下；同理如果已有同文件名的文件，那么该文件会被覆盖
"""

""" === 创建操作 ===
1. 创建单个目录 - os.mkdir
2. 创建整个目录树 - os.makedirs
"""
os.makedirs(r"data\good\yes")