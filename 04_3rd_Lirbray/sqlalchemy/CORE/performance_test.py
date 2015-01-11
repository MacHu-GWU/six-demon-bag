##encoding=utf8

"""
测试用python自带的sqlite3进行select和用SqlAlchemy通过Table进行select的速度差别
"""

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, MetaData
from sqlalchemy import Integer, TEXT
from sqlalchemy.sql import select
import time
import os
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

def initial():
    conn = engine.connect()
    
    records = [{"id": i, "text": "abcdefghijklmnopqrstuvwxyz"} for i in range(1000)]
    
    ins = documents.insert()
    conn.execute(ins, records)
    
    
initial()

def test1():
    conn = engine.connect()
    
    st = time.clock() # 速度是原生的select的 1/3
    for row in conn.execute(select([documents])):
        pass
    print(time.clock() - st)
    
test1()

def test2():
    conn = sqlite3.connect("performance_test.db")
    c = conn.cursor()
    
    st = time.clock() # 速度是通过SqlAlchemy的 3倍
    for row in c.execute("SELECT * FROM documents"):
        pass
    print(time.clock() - st)
    
test2()
    
try:
    os.remove("performance_test.db")
except:
    pass
