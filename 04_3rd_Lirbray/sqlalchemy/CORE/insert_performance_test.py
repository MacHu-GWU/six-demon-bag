##encoding=utf8

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
conn = engine.connect()

rows = [{"id": i, "text": "abcdefghijklmnopqrstuvwxyz"} for i in range(1000)] + \
    [{"id": random.randint(1, 1000), "text": "abcdefghijklmnopqrstuvwxyz"} for i in range(10)]
    
def test1():
    ins = documents.insert()
    st = time.clock()
    for row in rows:
        try:
            conn.execute(ins, row)
        except:
            pass
    print(time.clock() - st)
    
#     for row in conn.execute("SELECT * FROM documents"):
#         print(row)
        
# test1()

def test2():
    ins = documents.insert()
    st = time.clock()
    for row in rows:
        try:
            conn.execute(ins, row).execution_options(autocommit=False)
        except:
            pass
    print(time.clock() - st)

#     for row in conn.execute("SELECT * FROM documents"):
#         print(row)

test2()