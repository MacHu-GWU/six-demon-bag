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

"""
adaptor和converter是一种对类到字符串进行转换的函数
adaptor负责把类转化成字符串
converter负责把字符串转化为类

在python中有两个默认的adaptor: DATE和DATETIME
在数据库中其实储存的是字符串, 也就是说即使你选择的是的DATETIME而实际上储存的是字符串。
而默认的adaptor会自动

这样数据库就可以把任何自定义的类都以字符串的形式存放
在数据库中了
"""

from __future__ import print_function
import sqlite3
import datetime

class Point(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return "(%f;%f)" % (self.x, self.y)
    
    def __gt__(self, other):
        if self.x > other.x and self.y > other.y:
            return True
        else:
            return False
        
def adapt_point(point):
    """类 -> 字符串 转换"""
    return "%f;%f" % (point.x, point.y)

def convert_point(s):
    """字符串 -> 类 转换"""
    x, y = map(float, s.split(";"))
    return Point(x, y)

def unit_test1():
    """测试转换器的效果
    """
    p = Point(1,2)
    print(adapt_point(p))
    s = '1.00;2.00'
    print(convert_point(s))
    
# unit_test1()
    
def unit_test2():
    """测试adaptor和convertor在数据库中的行为
    """
    sqlite3.register_adapter(Point, adapt_point) # 注册转换器
    sqlite3.register_converter("point", convert_point) # 定义新的数据类型
    conn = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES) # 加入detect_types的参数后
                                                                             # 才能使得类转换器生效
    c = conn.cursor()
    c.execute("create table test(p point)")
    c.execute("insert into test(p) values (?)", (Point(1,2),))
    ##注！这条比较查询语句中，数据库对于>的行为并不是用户定义的Point __gt__，而是对adapt_point
    ##所转换后的字符串进行比较。sqlite3貌似不支持用户定义的比较操作符
    c.execute("select p from test WHERE p > ?", (Point(1,1),))
    for row in c.fetchall():
        print(row)
                
# unit_test2()

def unit_test3():
    """测试默认的两个adapter, DATE, DATETIME.
    注: python datetime.datetime 对应 TIMESTAMP
    """
    conn = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
    c = conn.cursor()
    c.execute("CREATE TABLE test (value1 TIMESTAMP, value2 DATE)")
    c.execute("INSERT INTO test (value1, value2) VALUES (?, ?)", (datetime.datetime.now(), datetime.date(2010,1,1)))
    conn.commit()
    print(c.execute("SELECT * FROM test").fetchall())    

# unit_test3()