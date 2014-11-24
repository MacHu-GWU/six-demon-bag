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

"""AND 和 OR 关键字的用法

The SQL AND & OR Operators
--------------------------
The AND operator displays a record if both the first condition AND the second condition are true.
The OR operator displays a record if either the first condition OR the second condition is true.
"""

from __future__ import print_function
from prettytable import from_db_cursor as fdc
import sqlite3

conn = sqlite3.connect("wc3_demo_db.db")
c = conn.cursor()
c.execute("SELECT * FROM Customers WHERE Country='Germany' AND City='Berlin';")
print(fdc(c))

c.execute("SELECT * FROM Customers WHERE City='Berlin' OR City='München'")
print(fdc(c))