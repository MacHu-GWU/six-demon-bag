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
rollback机制是数据库中最重要的机制之一。有了它数据库的完整性才能得到保证。
rollback的功能是恢复到最近一次commit()的状态
"""

from __future__ import print_function
import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()

def example1():
    c.execute("CREATE TABLE test (id INTEGER, name TEXT)")
    conn.commit() # 此时表中无数据
    c.executemany("INSERT INTO test VALUES (?,?)", [(1, "bob"), (2, "jack")])
    print(c.execute("SELECT * FROM test").fetchall())
    conn.rollback() # 回到了表中无数据的状态
    print(c.execute("SELECT * FROM test").fetchall())

example1()