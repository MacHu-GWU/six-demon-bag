##encoding=utf8
##version =py27
##author  =sanhe
##date    =2014-09-11

"""
当postgres服务器建立的时候，会自带建立有3个数据库：
information_schema = 数据库的schema信息
pg_catalog = 数据库的访问权限，配置等信息
public = 用户具体的数据表所存放的位置

根据以上描述，前面的两个表是系统表，通常不要做任何修改。而用户
的数据表则被存放在public数据库中。这一点，跟sqlite3中系统隐藏
自带的sqlite_master系统表类似。

所以如果要得到用户的表的schema一类的信息的时候，我们直接在
inforamtion_schema中查询就可以了，无需对用户的表进行查询
"""

import psycopg2
from pprint import pprint as ppt

conn = psycopg2.connect(host = '10.0.80.180',  dbname = 'securiport', user = 'postgres', password = '')
c = conn.cursor()

def example1():
    """get the list of table name in this database
    获得数据库中所有的数据表名
    """
    cmd = \
    """
    select column_name from information_schema.columns where table_schema = 'YOUR_SCHEMA_NAME' and table_name='YOUR_TABLE_NAME'
    """
    c.execute("select table_name from information_schema.tables WHERE table_schema = 'public'")
    for row in c.fetchall():
        print row
    
# example1()

def example2():
    '''get the columns information in Postgres table.
    获得数据表中所有列的列信息
    you can use this instead:
        cursor.execute("SELECT * FROM tablename")
        print cursor.discription
    '''
    tablename = 'arrive_at_flights'
    cmd = \
    """
    SELECT
        column_name,
        ordinal_position,
        is_nullable,
        data_type
    FROM
        information_schema.columns
    WHERE 
        table_schema = 'public' and table_name = '%s'
    """ % tablename
    c.execute(cmd)
    for row in c.fetchall():
        print row
        
example2()