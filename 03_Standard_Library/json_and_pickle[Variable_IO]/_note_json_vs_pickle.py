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
import json
import pickle
import time
import random
import sys

"""
比较json和pickle在IO时候的时间和空间性能
注意：在python2和python3中会有非常大的差别
"""

def rand_string(length):
    """highest performance non-dependent pure python random string generator
    """
    # All the characters you want to use in your strings:
    test_chars = u"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return "".join(random.sample(test_chars, length) )

def json_vs_pickle(data):
    """
    pickle:
        优点: 可以保存任意的python对象
        缺点: 读，写，磁盘占用都比较大。特别是读写时间开销大
    json:
        优点: 读，写快，磁盘占用小，人类可阅读
        缺点: 无法储存复杂的数据对象。只支持:
            dict, list, unicode, int, long, float, True, False, None
    """

    print("size of serialized string data = \n%s\n" % sys.getsizeof( pickle.dumps(data) ) ) # pickle是字节，会小一些
    print("size of json string data = \n%s\n" % sys.getsizeof( json.dumps(data) ) ) # json 是字符串，会大一些
    
    st = time.clock()
    pickle.dump(data, open("data.p", "wb")) # pickle.dumps的是字节，所以要用"wb"
    print("pickle dump takes:\n%s\n" % (time.clock() - st) )
    
    st = time.clock()
    with open("data.json", "w") as f:
        f.write(json.dumps(data)) # json.dumps的是字符串，所以要用"w"
    print("json dump takes:\n%s\n" % (time.clock() - st) )
    
    st = time.clock()
    data1 = pickle.load(open("data.p", "rb"))
    print("pickle load takes:\n%s\n" % (time.clock() - st) )
    
    st = time.clock()
    with open("data.json", "r") as f:
        data2 = json.loads( f.read() )
    print("json load takes:\n%s\n" % (time.clock() - st) )

def performace_test():
    """
    分析：
    python2中：
        测试数据1，数据结构复杂时：
            pickle空间和时间消耗都远优于json
        测试数据2，数据结构简单，但是量大时：
            pickle空间消耗略多于json
            json读写消耗远远优于pickle
            
    python3中：
        测试数据1，数据结构复杂时：
            pickle空间和时间消耗都远优于json
        测试数据2，数据结构简单，但是量大时：
            pickle和json空间消耗都差不多
            但是读写消耗要优于json
             
    结论：
        python2中用json, python3中用pickle
        若要考虑版本兼容的问题，用json较好
    """
    """测试数据1，纯json所支持的内置数据结构，有多重嵌套的字典"""
    data = {i : {rand_string(32): list(range(100)) for j in range(100)} for i in range(100)}
    """测试数据2，结构简单，但是数量众多的字典数据"""
#     data = {i : rand_string(32) for i in range(100000)}
    json_vs_pickle(data)

if __name__ == "__main__":
    performace_test()