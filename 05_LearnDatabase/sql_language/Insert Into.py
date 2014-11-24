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

"""INSERT INTO关键字的用法

SQL INSERT INTO Syntax
----------------------
It is possible to write the INSERT INTO statement in two forms.

The first form does not specify the column names where the data will be inserted, only their values:

INSERT INTO table_name
VALUES (value1,value2,value3,...);
The second form specifies both the column names and the values to be inserted:

INSERT INTO table_name (column1,column2,column3,...)
VALUES (value1,value2,value3,...);
"""

from __future__ import print_function
from prettytable import from_db_cursor as fdc
import sqlite3

conn = sqlite3.connect("wc3_demo_db.db")
c = conn.cursor()
c.execute("""INSERT INTO Shippers (ShipperID, ShipperName, Phone) VALUES (99, "UPS", "(202) 123-4567");""")
c.execute("SELECT * FROM shippers")
print(fdc(c))