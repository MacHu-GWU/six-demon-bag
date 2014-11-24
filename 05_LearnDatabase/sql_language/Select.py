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

"""SELECT关键字的用法
SQL SELECT Syntax
-----------------

SELECT column_name,column_name
FROM table_name;
and

SELECT * FROM table_name;
"""

from __future__ import print_function
from prettytable import from_db_cursor as fdc
import sqlite3

conn = sqlite3.connect("wc3_demo_db.db")
c = conn.cursor()
c.execute("SELECT CustomerName, ContactName, Address, City FROM customers")
print(fdc(c))

c.execute("SELECT * FROM customers")
print(fdc(c))