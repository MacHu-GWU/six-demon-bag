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

"""PRIMARY KEYS关键字的用法
"""

from __future__ import print_function
from prettytable import from_db_cursor as fdc
import sqlite3

conn = sqlite3.connect("wc3_demo_db.db")
c = conn.cursor()
try: # 多重PRIMARY KEYS
    c.execute("""CREATE TABLE multiple_pkey (address TEXT, zipcode TEXT, price INTEGER, PRIMARY KEY (address, zipcode) );""")
except:
    pass
c.execute("INSERT INTO multiple_pkey VALUES (?,?,?)", ("1400 S", "22202", 1000))
c.execute("INSERT INTO multiple_pkey VALUES (?,?,?)", ("1400 S", "75000", 2000))
c.execute("SELECT * FROM multiple_pkey")
print(fdc(c))