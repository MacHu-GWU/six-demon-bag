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

"""ORDER BY关键字的用法

SQL ORDER BY Syntax
-------------------

SELECT column_name,column_name
FROM table_name
ORDER BY column_name,column_name ASC|DESC;
"""

from __future__ import print_function
from prettytable import from_db_cursor as fdc
import sqlite3

conn = sqlite3.connect("wc3_demo_db.db")
c = conn.cursor()
# 根据单个关键字排序
c.execute("SELECT CustomerName, Country FROM Customers ORDER BY Country DESC;")
print(fdc(c))

# 根据多个关键字排序
c.execute("SELECT CustomerName, Country FROM Customers ORDER BY Country DESC, CustomerName ASC;")
print(fdc(c))