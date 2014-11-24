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

"""LIKE关键字的用法

相当于简易版的正则表达式字符串匹配
SQL LIKE Syntax
---------------

SELECT column_name(s)
FROM table_name
WHERE column_name LIKE pattern;
"""

from __future__ import print_function
from prettytable import from_db_cursor as fdc
import sqlite3

conn = sqlite3.connect("wc3_demo_db.db")
c = conn.cursor()
c.execute("""SELECT * FROM Customers WHERE City LIKE "s%";""")
print(fdc(c))

c.execute("""SELECT * FROM Customers WHERE City LIKE "%s";""")
print(fdc(c))