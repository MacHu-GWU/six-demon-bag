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

"""UPDATE关键字的用法
SQL UPDATE Syntax
-----------------

UPDATE table_name
SET column1=value1,column2=value2,...
WHERE some_column=some_value;
"""

from __future__ import print_function
from prettytable import from_db_cursor as fdc
import sqlite3

conn = sqlite3.connect("wc3_demo_db.db")
c = conn.cursor()

c.execute("""SELECT * FROM Customers WHERE CustomerName="Alfreds Futterkiste";""")
print(fdc(c))

c.execute("""UPDATE Customers SET ContactName="Alfred Schmidt", City="Hamburg" 
WHERE CustomerName="Alfreds Futterkiste";""")

c.execute("""SELECT * FROM Customers WHERE CustomerName="Alfreds Futterkiste";""")
print(fdc(c))

