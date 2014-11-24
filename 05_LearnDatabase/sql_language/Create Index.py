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

"""CREATE INDEX关键字的用法

SQL CREATE INDEX Syntax
-----------------------
Creates an index on a table. Duplicate values are allowed:

CREATE INDEX index_name
ON table_name (column_name)

SQL CREATE UNIQUE INDEX Syntax
------------------------------
Creates a unique index on a table. Duplicate values are not allowed:

CREATE UNIQUE INDEX index_name
ON table_name (column_name)

什么情况下需要，什么情况下不需要创建索引：
    参考资料 = http://baike.baidu.com/view/2079871.htm
"""

from __future__ import print_function
from prettytable import from_db_cursor as fdc
import sqlite3
import time

conn = sqlite3.connect("wc3_demo_db.db")
c = conn.cursor()

st = time.clock()
c.execute("SELECT * FROM OrderDetails WHERE productID = 24 AND Quantity > 10;")
print(time.clock() - st) # without index 0.000296500946712
print(fdc(c))

c.execute("CREATE INDEX ORDER_INDEX ON OrderDetails (ProductID, Quantity)")
st = time.clock()
c.execute("SELECT * FROM OrderDetails WHERE productID = 24 AND Quantity > 10;")
print(time.clock() - st) # with index 0.0000897105428514