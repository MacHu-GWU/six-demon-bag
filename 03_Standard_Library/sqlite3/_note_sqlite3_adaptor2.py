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
import sqlite3
        
def adapt_list(LIST):
    """类 -> 字符串 转换"""
    return "&".join(LIST)

def convert_list(STRING):
    """字符串 -> 类 转换"""
    return STRING.decode().split("&")
    
def unit_test1():
    """测试adaptor和convertor在数据库中的行为
    """
    sqlite3.register_adapter(list, adapt_list) # 注册转换器, class name, adaptor
    sqlite3.register_converter("LIST", convert_list) # 定义新的数据类型, class name in string, converter
    conn = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES) # 加入detect_types的参数后
                                                                             # 才能使得类转换器生效
    c = conn.cursor()
    c.execute("create table test (l LIST)")
    c.execute("insert into test(l) values (?)", (['sanhe','wangyu','zhangtao','fenhan'],))
    c.execute("select * from test")
    for row in c.fetchall():
        print(row)

unit_test1()

def adapt_set(SET):
    """类 -> 字符串 转换"""
    return '&'.join(SET)

def convert_set(STRING):
    """字符串 -> 类 转换"""
    return set(STRING.decode().split('&'))
    
def unit_test2():
    """测试adaptor和convertor在数据库中的行为
    """
    sqlite3.register_adapter(set, adapt_set) # 注册转换器, class name, adaptor
    sqlite3.register_converter("PYTHONSET", convert_set) # 定义新的数据类型, class name in string, converter
    conn = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES) # 加入detect_types的参数后
                                                                             # 才能使得类转换器生效
    c = conn.cursor()
    c.execute("create table test (name_set PYTHONSET)")
    c.execute("insert into test (name_set) values (?)", ({"bob", "jack"},))
    c.execute("select * from test")
    for row in c.fetchall():
        print(row)

# unit_test2()

