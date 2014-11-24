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

"""IN关键字的用法
SQL IN Syntax
-------------

SELECT column_name(s)
FROM table_name
WHERE column_name IN (value1,value2,...);
"""

from __future__ import print_function
from prettytable import from_db_cursor as fdc
import sqlite3

conn = sqlite3.connect("wc3_demo_db.db")
c = conn.cursor()
c.execute("SELECT * FROM Customers WHERE City IN ('Paris','London');")
print(fdc(c))