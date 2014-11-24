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

"""DELETE关键字的用法
SQL DELETE Syntax
-----------------

DELETE FROM table_name
WHERE some_column=some_value;
"""

from __future__ import print_function
from prettytable import from_db_cursor as fdc
import sqlite3

conn = sqlite3.connect("wc3_demo_db.db")
c = conn.cursor()

c.execute("""SELECT * FROM Customers WHERE CustomerName="Alfreds Futterkiste";""")
print(fdc(c))

c.execute("""DELETE FROM Customers 
WHERE CustomerName="Alfreds Futterkiste" AND ContactName="Maria Anders";""")

c.execute("""SELECT * FROM Customers WHERE CustomerName="Alfreds Futterkiste";""")
print(fdc(c))