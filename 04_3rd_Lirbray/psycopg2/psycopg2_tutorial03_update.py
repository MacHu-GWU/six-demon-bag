##encoding=utf8
##version =py27
##author  =sanhe
##date    =2014-09-11

import psycopg2
from datetime import datetime

## EFA test postgres database
conn = psycopg2.connect(host = "10.0.80.180",  dbname = "securiport", user = "postgres", password = "")
c = conn.cursor()

def example1():
    """
    [EN]postgres UPDATE syntax
    [CN]postgres UPDATE 语句语法
    """
    c.execute("CREATE TABLE public.sanhe_test (id INTEGER UNIQUE NOT NULL, value INTEGER);")
    c.executemany("INSERT INTO public.sanhe_test VALUES (%s,%s);", [(1, 10),(3, 30),(4, 40),(5, 50),(6, 60)] )

    print "========== 执行update之前 =========="
    c.execute("SELECT * FROM sanhe_test")
    for row in c.fetchall():
        print row
    
    c.execute("UPDATE sanhe_test SET value = %s WHERE id = %s", (30, 5)) # 单次
    c.executemany("UPDATE sanhe_test SET value = %s WHERE id = %s", [(30, 4),(30, 6)]) # 批量
    
    print "========== 执行update之后 =========="
    c.execute("SELECT * FROM sanhe_test")
    for row in c.fetchall():
        print row
        
example1()