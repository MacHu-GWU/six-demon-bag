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

"""SELECT TOP关键字的用法

SQL Server / MS Access Syntax
-----------------------------

SELECT TOP number|percent column_name(s)
FROM table_name;


SQL SELECT TOP Equivalent in MySQL and Oracle
---------------------------------------------
MySQL Syntax

SELECT column_name(s)
FROM table_name
LIMIT number;
Example

SELECT *
FROM Persons
LIMIT 5;
Oracle Syntax

SELECT column_name(s)
FROM table_name
WHERE ROWNUM <= number;
Example

SELECT *
FROM Persons
WHERE ROWNUM <=5;
"""

from __future__ import print_function
from prettytable import from_db_cursor as fdc
import sqlite3

conn = sqlite3.connect("wc3_demo_db.db")
c = conn.cursor()
c.execute("SELECT * FROM Customers LIMIT 5") # 只选择前5条记录
print(fdc(c))