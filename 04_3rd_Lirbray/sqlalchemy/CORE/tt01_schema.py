##encoding=utf8

"""
SqlAlchemy Core 提供了一种抽象的方式, 通过Table, Column这些抽象类的insert, update, delete这些方法,
直接跟数据库进行交互。而只要你绑定了某一个数据库引擎, 而且定义了列的抽象数据类型, 则SA会自动帮用户处理
各个数据库中同一种数据类型的有不同格式的问题。而用户则免去了些SQL语句的麻烦。

参考资料:

    sql表达式
        http://docs.sqlalchemy.org/en/rel_0_9/core/tutorial.html#sql-expression-language-tutorial

    在定义表时, 会涉及定义不同的data type和constrain. 请参考:
    Define your Columns and Data Types:
        http://docs.sqlalchemy.org/en/rel_0_9/core/type_basics.html
        
    Define constrain:
        http://docs.sqlalchemy.org/en/rel_0_9/core/constraints.html
        
    Core
        http://docs.sqlalchemy.org/en/rel_0_9/core/connections.html
        
"""

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, MetaData
from sqlalchemy import Integer, String, ForeignKey, TEXT, Date
import os

try:
    os.remove("Core_tutorial.db")
except:
    pass

engine = create_engine('sqlite:///Core_tutorial.db', echo=True)

metadata = MetaData()
users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('fullname', String), 
)

addresses = Table('addresses', metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', None, ForeignKey('users.id')),
    Column('email_address', String, nullable=False),
)


metadata.create_all(engine)

ins = users.insert()

conn = engine.connect()

records = [{"id": 3, "name": "wendy", "fullname": "bob"},
           {"id": 4, "name": "wendy", "fullname": "bob"}]

# for record in records:
#     try:
#         conn.execute(ins, record) 
#     except:
#         pass
