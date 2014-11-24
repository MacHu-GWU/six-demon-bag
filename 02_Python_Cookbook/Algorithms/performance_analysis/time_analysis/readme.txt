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
## reference = http://www.oschina.net/translate/python-performance-analysis?print

"""
很多时候，我们需要分析程序中哪一个函数，甚至是哪一行运行了多长的时间，哪一行重复运行了多少次。
经过这样的分析，我们就能很快的找到时间开销的瓶颈所在。下面我们就来介绍一下在Python中如何分析
程序的运行时间。
"""

"""
首先我们来看看这个文件夹下有什么。在看完本文档之前，请不要动该文件夹下的任何文件。
"""
# README.py                               	就是本说明文档啦！
# line_profiler-1.0b3.win32-py2.7.exe     	line_profiler的安装包，作者rkern
# kernprof.py                             	用于测量时间的主函数。
# test1.py								  	被用来测试的程序1，是一个简单的快速排序的python程序
# test2.py                               	被用来测试的程序2，是一个简单的快速排序的python程序


"""
line_profiler就是我们所要用到的工具，用这个工具可以很清楚的列出：
"""
#     1. Hits     被运行的次数
#     2. Time     被运行的总时间
#     3. Per Hit  平均每次运行的时间 = Time/Hits
#     4. %Time    占整个程序运行时间的百分比

"""
line_profiler这个包的工作方式跟一般的包不太一样。一般的包都是安装了之后，然后import 包名称。
而lin_profiler是通过kernprof.py这个可执行程序，将它和需要测试的sort.py放到同一个文件夹下。
然后运行windows或者linux命令行，cd到该目录下，然后用命令行参数调用：
    python kernprof.py -l -v sort.py
所以我们在安装了这个包之后，还需要妥善保存kernprof.py这个文件。
"""

"""
好了，我们来试试看到底怎么用line_profiler来测试sort.py的性能吧。
首先，我们需要用对我们的程序sort.py进行一些改动。line_profiler是用装饰器关键字@profile
来标识我们想要测的函数。我们只需要把@profile放在函数定义def qsort(L): 的前一行就可以了。
在这里，sort.py文件已经修改好了。

第一步: 双击 exe 文件。 这个包不支持pip安装，而且只有python27版本
第二步: 把kernprof.py和sort.py拷贝到任意文件夹下。当然，尽量放在路径短的目录下
第三步: 打开windows cmd命令行 (如果你不知道这是什么，打开windows开始菜单，在搜索框输入cmd...)
第四步: 假设我们把文件放在了 C:\test 目录下 依次输入如下命令:
    cd\  回车
    cd test 回车
    kernprof.py -l -v sort.py 回车
然后我们就会看到:
"""
# Line #    Hits        Time    Per Hit    % Time    Line Contents
# ==============================================================================
#     7                                               @profile
#     8                                               def qsort(L):
#     9       13          31          2.4     16.8        if len(L) <= 1:         
#     10       7          13          1.9      7.0            return L
#     11      46         141          3.1     76.2        return qsort([lt for lt in 
# L[1:] if lt < L[0]]) + L[0:1] + qsort([ge for ge in L[1:] if ge >= L[0]]) 

"""
如果想要验证 Hits 这些数字的正确性，可以用文本编辑器打开sort.py，看看最后面对快速排序算法的
描述，看到底一共return了多少次L
"""

COMPLETE = raw_input("请用文本编辑器打开此文件, 按回车退出... ")