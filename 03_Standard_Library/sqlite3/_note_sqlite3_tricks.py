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
import random
import time
from datetime import date, datetime
import os
import random

conn = sqlite3.connect(":memory:")
c = conn.cursor()

def count_number_of_record():
    """如何用最小的时间和内存复杂度得到表中有多少条数据
    """
    ## initial schema
    c.execute("""CREATE TABLE float_number
                 (ID INTEGER PRIMARY KEY NOT NULL, value INTEGER)""")
    
    ## insert value
    n = 1000
    values = [( random.random(), ) for i in xrange(n)]
    c.executemany("INSERT INTO float_number VALUES (NULL,?)", values)
    
    ## bad way
    st = time.clock()
    c.execute("SELECT * FROM float_number")
    print(len(c.fetchall()))
    print("bad way = %s" % (time.clock() - st))
    
    ## good way
    st = time.clock()
    c.execute("SELECT count(*) FROM (SELECT * FROM float_number);")
    print(c.fetchall())
    print("good way = %s" % (time.clock() - st))

# count_number_of_record()

def handle_date():
    """如何在sqlite3中使用Date格式，使得query可以对Date数据进行数学运算操作
    """
    c.execute("CREATE TABLE test1 (id INTEGER, d DATE)")
    c.execute("INSERT INTO test1 (id, d) VALUES (?, ?)", (1, "2010-01-15") ) # one standard date string format
    c.execute("INSERT INTO test1 (id, d) VALUES (?, ?)", (2, date(2010,1,20) ) ) # date object
    c.execute("SELECT * FROM test1 WHERE d > ? AND d < ?", (date(2010,1,17), date(2010,1,21) ) )
    for row in c.fetchall():
        print(row)
    c.execute("SELECT * FROM test1 WHERE d > ? AND d < ?", ("2010-01-17", "2010-01-21") )
    for row in c.fetchall():
        print(row)
             
# handle_date()

def handle_datetime():
    """如何在sqlite3中使用Datetime格式，使得query可以对Datetime数据进行数学运算操作
    """
    c.execute("CREATE TABLE test2 (id INTEGER, dt DATETIME)")
    c.execute("INSERT INTO test2 (id, dt) VALUES (?, ?)", (1, "2010-01-15 18:05:00") ) # standard date string format
    c.execute("INSERT INTO test2 (id, dt) VALUES (?, ?)", (2, datetime(2010,1,20,6,0,5) ) ) # date object
    c.execute("SELECT * FROM test2 WHERE dt > ? AND dt < ?", (datetime(2010,1,20,6,0,4), datetime(2010,1,21) ) )
    for row in c.fetchall():
        print(row)
        
# handle_datetime()

def get_all_tablename():
    """如何得到sqlite3数据库中所有的表名
    在sqlite3中有一个特殊的表名叫做sqlite_master，是作为隐藏的表存在的。储存着sqlite3中其他
    表的metadata信息
    """
    c.execute("CREATE TABLE test1 (id INTEGER, d DATE)")
    c.execute("CREATE TABLE test2 (id INTEGER, dt DATETIME)")
    c.execute("""SELECT name FROM sqlite_master WHERE type="table";""")
    for row in c.fetchall():
        print(row)
    
# get_all_tablename()

def get_all_columns_setting():
    """如何得到sqlite3表中所有列的定义
    sqlite3中的特殊命令 PRAGMA table_info(#tablename)
    """
    c.execute("CREATE TABLE test (id INTEGER PRIMARY KEY NOT NULL, name TEXT, dob DATE)")
    c.execute("PRAGMA table_info(test)") ## 取得列信息
    print("{0[0]:<10}{0[1]:<20}{0[2]:<10}{0[3]:<10}{0[4]:<20}{0[5]:<10}".format(("cID", ##字符美化输出
                                                                                 "COLUMN NAME",
                                                                                 "TYPE",
                                                                                 "NOT NULL",
                                                                                 "dflt_value",
                                                                                 "IS PRIMARY KEY")) )
    for row in c.fetchall(): # ("cid", "name", "type", "notnull", "dflt_value", "pk")
        print("{0[0]:<10}{0[1]:<20}{0[2]:<10}{0[3]:<10}{0[4]:<20}{0[5]:<10}".format(row) )
        
get_all_columns_setting()

def iter_cursor():
    """对select的结果进行循环
    """
    c.execute("CREATE TABLE test (id INTEGER PRIMARY KEY NOT NULL, name INTEGER)")
    records = list()
    for i in xrange(1000000): # 大一点 最好百万级, 运行时间大约5秒
        records.append( ( random.randint(1,1024),) )
    c.executemany("INSERT INTO test VALUES (NULL, ?)", records)
    c.execute("SELECT * FROM test")
    for row in c.fetchall():
        print(row)
    print("COMPLETE")
        
# iter_cursor()
