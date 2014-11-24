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

from __future__ import print_function

def example1():
    """
    seq[::stride]         # [seq[0],   seq[stride],     ..., seq[-1]    ]
    seq[low::stride]      # [seq[low], seq[low+stride], ..., seq[-1]    ]
    seq[:high:stride]     # [seq[0],   seq[stride],     ..., seq[high-1]]
    seq[low:high:stride]  # [seq[low], seq[low+stride], ..., seq[high-1]]
    """
    l = list("abcdefgh")
    print(l[::2]) # 从0开始隔n个取一个
    print(l[1::2]) # 从1开始隔n个取一个
    print(l[:3:2]) # 从头开始到3为止，隔n个取一个
    print(l[0:3:2]) # 从0开始到3为止，隔n个取一个
    
example1()

def example2():
    l = list("12345678")
    print(l[::-1]) # 从最后一个开始，逆序排列
    print(l[::-2]) # 从最后一个开始，隔2个取一个
    print(l[-2::-2]) # 从-2开始，隔2个取一个
    print(l[:3:-2]) # 从最后开始，到3为止，隔2个取一个
    
example2()