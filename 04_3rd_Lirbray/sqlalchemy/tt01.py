##encoding=utf8

"""
下面通过一个简单的例子说明，在sqlalchemy中通过定义对象对数据库进行操作是多么的简单。
"""

from __future__ import print_function
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
import os

try:
    os.remove("testdatabase.db")
except:
    pass

"""
首先要通过create_engine定义数据库引擎，定义了之后并不会自动的连接数据库。连接数据库进行操作，请参考
Session的部分。
"""
engine = create_engine(r"sqlite:///testdatabase.db", echo = False) # 定义引擎, echo表示是否打印日志信息

"""
declarative_base方法返回一个基类。所有用户定义的类需要由这个类继承而来。
基类里面内置了map到数据库的细节。当用户定义了一个通过基类继承而来的自定义类，那么自定义类的metadata就会
被写入基类。当用户最后完成定义后，可以通过Base.metadata.create_all(engine)根据数据引擎，自动生成表。
相当于sqlalchemy自动根据你写的类生成CREATE TABLE语句。
"""
Base = declarative_base() # 定义基类

class User(Base):
    __tablename__ = 'users' # define table name
    id = Column(Integer, primary_key=True) # define primary key column
    name = Column(String)
    fullname = Column(String)
    password = Column(String)
    
    def __repr__(self):
       return "<User(name='%s', fullname='%s', password='%s')>" % (
                            self.name, self.fullname, self.password)
           
Base.metadata.create_all(engine) 

"""
在sqlalchemy对数据库进行操作是通过Session来进行的。一个session相当于建立了一个连接。session是一个抽象
的网络连接。建立了连接之后我们需要将其和数据库引擎进行绑定。绑定之后我们就可以新建一个实体连接了。
"""
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

"""
然后我们就可以对数据库进行增查删改等操作了，这里我们仅仅介绍insert和select在sqlarchemy中的做法
"""

## INSERT
session.add(User(name='ed', fullname='Ed Jones', password='edspassword'))
session.add(User(name='jack', fullname='Jack Jones', password='jackspassword'))
session.add(User(name='jackson', fullname='Michael Jackson', password='jacksonspassword'))
session.commit()

## SELECT
print(session.query(User).filter_by(name='ed').first()) # 相当于 c.execute(sqlcmd).fetchone()
for i in session.query(User).filter(User.name.in_(["ed", "jack"])): # 相当于 for row in c.execute(sqlcmd).fetchall()
    print(i)
print(session.query(User).filter(User.name.in_(["ed", "jack"])).all()) # 相当于 c.execute(sqlcmd).fetchall()


