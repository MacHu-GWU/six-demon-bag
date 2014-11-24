##encoding=utf8
##version =py27
##author  =sanhe
##date    =2014-09-11

import psycopg2
from datetime import datetime
import random

## EFA test postgres database
conn = psycopg2.connect(host = '10.0.80.180',  dbname = 'securiport', user = 'postgres', password = '')
c = conn.cursor()

def initial():
    cmd = \
    """
    CREATE TABLE my_test_select (
    id INTEGER UNIQUE NOT NULL, 
    value INTEGER, 
    name VARCHAR(255) NOT NULL,
    create_time TIMESTAMP NOT NULL
    )
    """
    try:
        c.execute(cmd)
    except:
        pass
    
    records = [(1, 50, 'sanhe', datetime(2014, 1, 1, 0, 0, 0) ),
               (2, 40, 'fenhan', datetime(2014, 1, 2, 0, 0, 0) ),
               (3, 30, 'wangyu', datetime(2014, 1, 3, 0, 0, 0) ),
               (4, 20, 'songyu', datetime(2014, 1, 4, 0, 0, 0) ),
               (5, 10, 'sanhe', datetime(2014, 1, 5, 0, 0, 0) ),
               (6, 50, 'zhangtao', datetime(2014, 1, 5, 0, 0, 0) ),]
    c.executemany("INSERT INTO my_test_select VALUES (%s,%s,%s,%s)", records)

initial()
c.execute("SELECT my_test_select.* FROM my_test_select GROUP BY my_test_select.value")
for row in c.fetchall():
    print row