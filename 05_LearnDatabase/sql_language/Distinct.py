##################################
#encoding=utf8                   #
#version =py27, py33             #
#author  =sanhe                  #
#date    =2014-10-31             #
#                                #
#    (\ (\                       #
#    ( -.-)o    I am a Rabbit!   #
#    o_(")(")                    #
#                                #
##################################

"""DISTINCT 关键字的用法

SQL SELECT DISTINCT Syntax
--------------------------

SELECT DISTINCT column_name,column_name
FROM table_name;

阅读完本脚本之后思考如下问题：
    为什么DISTINCT语句不支持部分DISTINCT？能不能只让country DISTINCT，
    而其他的列随机的输出？
"""

from __future__ import print_function
from prettytable import from_db_cursor as fdc
import sqlite3

conn = sqlite3.connect("wc3_demo_db.db")
c = conn.cursor()
c.execute("SELECT DISTINCT country FROM customers")
print(fdc(c))

c.execute("SELECT DISTINCT country, city FROM customers")
print(fdc(c)) # 是按照 country, city 两者共同的独立性。现在country里是不是有重复的了?