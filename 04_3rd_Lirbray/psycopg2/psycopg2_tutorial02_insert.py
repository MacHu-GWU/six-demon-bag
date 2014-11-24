##encoding=utf8
##version =py27
##author  =sanhe
##date    =2014-09-11

import psycopg2
import random

## EFA test postgres database
conn = psycopg2.connect(host = '10.0.80.180',  dbname = 'securiport', user = 'postgres', password = '')
c = conn.cursor()

def example1():
    '''
    [EN]postgres INSERT syntax
    [CN]postgres INSERT 语句语法
    1. sqlite3 use ?, but postgres use %s
    '''
    c.execute("CREATE TABLE public.sanhe_test (id INTEGER PRIMARY KEY NOT NULL, value INTEGER);")
    c.execute("INSERT INTO public.sanhe_test VALUES (344, 2000)") # syntax 1 不指定列，对所有的列进行插入
    c.execute("INSERT INTO public.sanhe_test VALUES (%s,%s)", (343, 1000)) # syntax 2 不指定列，用SQL风格的字符串化
    c.execute("INSERT INTO public.sanhe_test (value, id) VALUES (3000, 345)") # syntax 3, customize the order of columns 指定列
    ## executemany works far more quickly than execute, if there's no exception raised.
    c.executemany("INSERT INTO public.sanhe_test VALUES (%s,%s)", [tpl for tpl in enumerate([random.randint(10,100) for i in xrange(4)] ) ] )
    c.execute("SELECT * FROM public.sanhe_test")
    for row in c.fetchall():
        print row
        
# example1()

def example2():
    '''
    [EN]Graceful Primary Key Error handling in Python/psycopg2
    [CN]如何批量插入数据，当有数据主键冲突时跳过该条记录
    ref = http://stackoverflow.com/questions/8497886/graceful-primary-key-error-handling-in-python-psycopg2
    '''
    # make sure you DON't HAVE TABLE "sanhe_test" in your database
    c.execute("CREATE TABLE public.sanhe_test (id INTEGER UNIQUE NOT NULL, value INTEGER);")
    c.executemany("INSERT INTO public.sanhe_test VALUES (%s,%s);", [(1, 10),(3, 30),(5, 50)] )
    conn.commit() # <=== 注：为了测试rollback，所以必须保存数据库
    ## === 如何优雅的处理有primary key或者unique属性的列遭遇重复的情况 ===
    # 无论是execute还是executemany遭遇到IntegrityError时，之后都无法execute任何SQL语句了
    # 这是由于postgres内部引擎机制造成的。只有rollback到上一次commit的状态之后，才能够继续
    # execute新的语句。
    # 我们首先try，如果正确，则运行else中的commit()；如果出错，则rollback到上一次commit的状态。
    # 正确之后commit非常重要。因为成功后如果不commit，那么下一步一旦出错，那么就会rollback回
    # 这次成功之前的状态。    
    records = [(4,100),(5,100),(6,100)]
    try:
        c.executemany("INSERT INTO public.sanhe_test VALUES (%s, %s)", records)
    except psycopg2.IntegrityError:
        conn.rollback() # rollback 然后试着逐条insert
        for record in records:
            try:
                c.execute("INSERT INTO public.sanhe_test VALUES (%s,%s)", record)
            except psycopg2.IntegrityError:
                conn.rollback()
            else:
                conn.commit()
    else:
        conn.commit()
        
    c.execute("SELECT * FROM public.sanhe_test")
    for row in c.fetchall():
        print row
    
    # 删除数据库
    c.execute("DROP TABLE public.sanhe_test")
    conn.commit()
    
# example2()

def example3():
    '''
    [CN]如何批量插入时，如果主键重复，则用新数据覆盖原数据
    '''
    c.execute("CREATE TABLE public.sanhe_test (id INTEGER UNIQUE NOT NULL, value INTEGER);")
    c.executemany("INSERT INTO public.sanhe_test VALUES (%s,%s);", [(1, 10),(3, 30),(5, 50)] )
    conn.commit()
    
    records = [(4,100),(5,100),(6,100)]
    try:
        c.executemany("INSERT INTO public.sanhe_test VALUES (%s, %s)", records)
    except psycopg2.IntegrityError:
        conn.rollback() # rollback 然后试着逐条insert
        for record in records:
            try:
                c.execute("INSERT INTO public.sanhe_test VALUES (%s,%s)", record)
            except psycopg2.IntegrityError:
                conn.rollback()
                c.execute("UPDATE public.sanhe_test SET id = %s, value = %s WHERE id=%s" , (record[0], record[1], record[0]) )
                conn.commit()
            else:
                conn.commit()
    else:
        conn.commit()

    c.execute("SELECT * FROM public.sanhe_test")
    for row in c.fetchall(): # 如果 (5, 100) 说明重复的值被替代了
        print row
        
    # 删除数据库
    c.execute("DROP TABLE public.sanhe_test")
    conn.commit()
    
# example3()
