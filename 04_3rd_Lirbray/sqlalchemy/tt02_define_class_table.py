##encoding=utf8

"""
本节主要介绍如何定义数据表
ref=http://www.cnblogs.com/harrychinese/archive/2012/09/12/My_Own_Tutorial_For_SqlAlchemy.html
"""

from __future__ import print_function
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String, DateTime, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime, date, timedelta
import os

try:
    os.remove("testdatabase.db")
except:
    pass

engine = create_engine(r"sqlite:///testdatabase.db", echo=False)
Base = declarative_base()

"""
数据库中表常有的数据类型有：
INTEGER, FLOAT, STRING, BOOLEAN, DATE, DATETIME, SERIERS(自增ID)
常用的constrain有：
PRIMARY KEY, UNIQUE, DEFAULT, NOT NULL

在sqlarchemy中如何详细的定义表请参考:
    data type = http://docs.sqlalchemy.org/en/rel_0_9/core/types.html 
    constrain = http://docs.sqlalchemy.org/en/rel_0_9/core/constraints.html
    default = http://docs.sqlalchemy.org/en/latest/core/defaults.html
下面我们通过定义一个魔兽世界中的玩家角色类来说明
"""

class Character(Base):
    __tablename__ = "character"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True, nullable=False) # 游戏角色名不得超过30个字符
    level = Column(Integer, default=1) # 等级，创建角色时服务器自动设定为1
    create_datetime = Column(DateTime, default=datetime.now()) # 游戏角色创建时间
    expire_date = Column(Date, default=date(2020,1,1)) # 游戏角色失效日期
    class_code = Column(Integer, nullable=False) # 职业编号
    
    def __str__(self): # str是用来直接打印这个类的，直接打印时打印id
       return """Character(id='%s', name='%s', level=%s, create_datetime='%s', expire_date='%s', 
       class_code=%s)""" % (self.id, self.name, self.level, self.create_datetime, self.expire_date, self.class_code)
    
    # repr是在session中操作时候用来展示的，这里我们不展示id。因为repr跟eval直接对应，
    # 我们从repr的结果能直接复原这个类就够了，所以不需要id。
    def __repr__(self): 
       return """Character(name='%s', level=%s, create_datetime='%s', expire_date='%s', 
       class_code=%s)""" % (self.name, self.level, self.create_datetime, self.expire_date, self.class_code)
       
Base.metadata.create_all(engine)

Session = sessionmaker()
Session.configure(bind=engine)
ses = Session()

ses.add(Character(name="vutune", class_code=5))
ses.add(Character(name="otherguy", class_code=5))
ses.add(Character(name="sardnea", class_code=5))

# print(type(ses.query(Character).all() ) ) # 是一个list，和cursor.execute(cmd).fetchall() 一样
print(ses.query(Character).all()) # 打印的是列表而不是类本身，所以调用的是__repr__而不是__str__

for char in ses.query(Character).all():
    print(type(char), char) # 直接打印的是类 ，所以调用的是__str__
    
    