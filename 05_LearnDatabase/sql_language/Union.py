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

"""UNION关键字的用法
SQL UNION Syntax
----------------

SELECT column_name(s) FROM table1
UNION
SELECT column_name(s) FROM table2;


SQL UNION ALL Syntax
--------------------

SELECT column_name(s) FROM table1
UNION ALL
SELECT column_name(s) FROM table2;
"""

from __future__ import print_function
from prettytable import from_db_cursor as fdc
import sqlite3

conn = sqlite3.connect("wc3_demo_db.db")
c = conn.cursor()
c.execute("""
SELECT City FROM Customers 
UNION
SELECT City FROM Suppliers
ORDER BY City;""")
print(fdc(c))

c.execute("""
SELECT City FROM Customers
UNION ALL
SELECT City FROM Suppliers
ORDER BY City;
""")
print(fdc(c))