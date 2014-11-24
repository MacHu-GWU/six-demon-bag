##encoding=utf8
##version =py27
##author  =sanhe
##date    =2014-09-11

"""CREATE TABLE in POSTGRES with different datatype
reference = http://www.postgresql.org/docs/9.3/interactive/datatype.html
"""
import psycopg2
from datetime import datetime, date

conn = psycopg2.connect(host = "10.0.80.180",  dbname = "securiport", user = "postgres", password = "")
c = conn.cursor()
    
def example1():
    """
    [EN]Primary key auto-increment
    [CN]设置主键从1开始自动递增
    注: 一旦采用了主键自动递增，在insert的时候就不可以人为的指定主键的值。
    必须让服务器自动添加。
    """    
    cmd = \
    """
    CREATE TABLE public.sanhe_test (
    id SERIAL PRIMARY KEY NOT NULL,
    value INTEGER NOT NULL)
    """
    c.execute(cmd) # create table
    records = [(10,),(20,),(30,)] # insert test data
    c.executemany("INSERT INTO public.sanhe_test (value) VALUES (%s);", records)
    c.execute("SELECT * FROM public.sanhe_test") # exam auto-increment
    for row in c.fetchall():
        print row

# example1()
    
def example2():
    """
    [EN]datetime datatype in postgres
    [CN]postgres数据库中的"时间"数据类型
    注：注意学习什么是SQL风格的字符串化
    """
    cmd = \
    """
    CREATE TABLE public.sanhe_test (
    id SERIAL PRIMARY KEY NOT NULL,
    content VARCHAR(255),
    value INTEGER NOT NULL,
    when_time TIMESTAMP,
    when_date DATE);
    """
    c.execute(cmd)
    records = [("sanhe's dog", 25, datetime(2014,1,1,18,0,0,0), date(2013,6,1)),
               ("jack - ryan", 30, datetime(2014,1,2,6,0,0,0), date(2013,7,1)),]
    c.executemany("INSERT INTO public.sanhe_test (content, value, when_time, when_date) VALUES (%s,%s,%s,%s);", records)
    
    print "====== Display All ======"
    c.execute("SELECT * FROM public.sanhe_test")
    for row in c.fetchall():
        print row
        
    print "\n====== SELECT with DATETIME operation ======"
    print "首先我们可以用时间戳字符串进行搜索"
    c.execute("SELECT * FROM public.sanhe_test WHERE when_time > '2014-01-01 20:00:00'") # syntax 1
    for row in c.fetchall():
        print row
    print "当然我们可以用python风格的%s对象字符串化的方法达到同样的目的，但并不推荐这么做，原因见下一例"
    c.execute("SELECT * FROM public.sanhe_test WHERE when_time > '%s'" % datetime(2014,1,1,20,0,0) ) # syntax 2
    for row in c.fetchall():
        print row
    print "PYTHON OPDB2.0协议支持SQL风格的字符串化，execute会对数据格式进行自动处理"
    c.execute("SELECT * FROM public.sanhe_test WHERE when_time > %s", (datetime(2014,1,1,20,0,0), )  ) # syntax 3
    for row in c.fetchall():
        print row
        
    print "\n====== SELECT with DATE operation ======"
    print "跟时间戳类似，我们可以用日期格式的字符串进行搜索"
    c.execute("SELECT * FROM public.sanhe_test WHERE when_date < '2013-06-15'") # syntax 1
    for row in c.fetchall():
        print row
    print "跟时间戳类似，推荐使用SQL风格的字符串化"
    c.execute("SELECT * FROM public.sanhe_test WHERE when_date > %s", (date(2013,6,20),)) # syntax 2
    for row in c.fetchall():
        print row

# example2()