##################################
#encoding=utf8                   #
#version =py27, py33             #
#author  =sanhe                  #
#date    =2014-10-29             #
#                                #
#    (\ (\                       #
#    ( -.-)o    I am a Rabbit!   #
#    o_(")(")                    #
#                                #
##################################

"""prettytable tutorial
Ref = https://code.google.com/p/prettytable/wiki/Tutorial
"""

from __future__ import print_function
from prettytable import PrettyTable
from prettytable import from_db_cursor

def example1():
    """通过行构造表格
    """
    print("{:=^40}".format("example1"))
    x = PrettyTable(["City name", "Area", "Population", "Annual Rainfall"])
    x.align["City name"] = "l" # Left align city names
    x.padding_width = 1 # One space between column edges and contents (default)
    x.add_row(["Adelaide",1295, 1158259, 600.5])
    x.add_row(["Brisbane",5905, 1857594, 1146.4])
    x.add_row(["Darwin", 112, 120900, 1714.7])
    x.add_row(["Hobart", 1357, 205556, 619.5])
    x.add_row(["Sydney", 2058, 4336374, 1214.8])
    x.add_row(["Melbourne", 1566, 3806092, 646.9])
    x.add_row(["Perth", 5386, 1554769, 869.4])
    print(x)

example1()
  
def example2():
    """通过列构造表格
    """
    print("{:=^40}".format("example2"))
    x = PrettyTable()
    x.add_column("City name",["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"])
    x.add_column("Area", [1295, 5905, 112, 1357, 2058, 1566, 5386])
    x.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374, 3806092, 1554769])
    x.add_column("Annual Rainfall",[600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9, 869.4])
    print(x)

example2()

def example3():
    """打印数据库SELECT的结果
    """
    import sqlite3
    
    print("{:=^40}".format("example3"))
    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.execute("CREATE TABLE employee (name TEXT, age INTEGER)")
    c.executemany("INSERT INTO employee VALUES (?,?)", [("bob", 32), ("jack", 21)])
    c.execute("SELECT * FROM employee")
    x = from_db_cursor(c)
    print(x)
    
example3()
