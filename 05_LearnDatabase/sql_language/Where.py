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

"""WHERE关键字的用法

SQL WHERE Syntax
----------------

SELECT column_name,column_name
FROM table_name
WHERE column_name operator value;

Operators in The WHERE Clause
-----------------------------
The following operators can be used in the WHERE clause:

Operator     Description
=            Equal
<>           Not equal. Note: In some versions of SQL this operator may be written as !=
>            Greater than
<            Less than
>=           Greater than or equal
<=           Less than or equal
BETWEEN      Between an inclusive range
LIKE         Search for a pattern
IN           To specify multiple possible values for a column
"""

from __future__ import print_function
from prettytable import from_db_cursor as fdc
import sqlite3

conn = sqlite3.connect("wc3_demo_db.db")
c = conn.cursor()
c.execute("SELECT * FROM Customers WHERE Country='Mexico';")
print(fdc(c))

c.execute("SELECT * FROM customers WHERE CustomerID=1")
print(fdc(c))