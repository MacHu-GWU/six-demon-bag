##encoding=utf8

"""
测试用python自带的sqlite3进行select和用SqlAlchemy通过Table进行select的速度差别
简要的介绍了如何:
    1. define schema
    2. create table
    3. insert data
    4. select data
"""

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, MetaData
from sqlalchemy import Integer, TEXT
from sqlalchemy.sql import select
import time
import os
import random
import sqlite3

try:
    os.remove("performance_test.db")
except:
    pass

engine = create_engine("sqlite:///performance_test.db", echo=False)

metadata = MetaData()

documents = Table("documents", metadata,
    Column("id", Integer, primary_key=True),
    Column("text", TEXT),
)
metadata.create_all(engine) 

def insert1():
    """测试用SA中的bulk insert插入多条数据的速度 0.01 - 0.05 跟原生sqlite3 API速度相近
    """
    conn = engine.connect()
    records = [{"id": i, "text": "abcdefghijklmnopqrstuvwxyz"} for i in range(1000)]
    ins = documents.insert()
    st = time.clock()
    conn.execute(ins, records)
    print(time.clock() - st)
    
# insert1()

def insert2():
    """测试SA中的逐条插入在数据有可能有IntegrityError的情况下的速度, 6 - 9,
    速度最慢。注: 这由于sqlite3在发生错误之后不需要回滚, 所以原生API在速度上会有优势。 在其他数据库
    系统中原生API的优势不大。
    """
    conn = engine.connect()
    records = [{"id": i, "text": "abcdefghijklmnopqrstuvwxyz"} for i in range(1000)]
    records = records + [{"id": random.randint(1, 1000), 
                          "text": "abcdefghijklmnopqrstuvwxyz"} for i in range(10)]
    ins = documents.insert()
    st = time.clock()
    for record in records:
        try:
            conn.execute(ins, record)
        except:
            pass
    print(time.clock() - st)

insert2()

def insert3():
    """测试原生Sqlite3 API插入速度, 0.01 - 0.05 跟SA中bulk insert速度相似
    """
    conn = sqlite3.connect("performance_test.db")
    c = conn.cursor()
    records = [(i, "abcdefghijklmnopqrstuvwxyz") for i in range(1000)]
    records = records + [(random.randint(0, 999), "abcdefghijklmnopqrstuvwxyz") for i in range(10)]

    st = time.clock()
    for record in records:
        try:
            c.execute("INSERT INTO documents VALUES (?,?);", record)
        except:
            pass
    conn.commit()
    print(time.clock() - st)

# insert3()

def select1():
    """测试通过SA执行SELECT的速度
    """
    conn = engine.connect()
    
    st = time.clock() # 速度是原生的select的 1/3
    for row in conn.execute(select([documents])):
        pass
    print(time.clock() - st)
    
# select1()

def select2():
    """测试通过原生sqlite3 API执行SELECT的速度
    """
    conn = sqlite3.connect("performance_test.db")
    c = conn.cursor()
    
    st = time.clock() # 速度是通过SqlAlchemy的 3倍
    for row in c.execute("SELECT * FROM documents"):
        pass
    print(time.clock() - st)
    
# select2()
    
try:
    os.remove("performance_test.db")
except:
    pass
