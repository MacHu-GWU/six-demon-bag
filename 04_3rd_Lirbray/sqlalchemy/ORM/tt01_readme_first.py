##encoding=utf8

"""
在ORM中, 每一个对象是一个数据表。对象的每一个属性是数据表中的一个列。
而Session(会话)用于跟database进行交互。Session的概念类似于数据库中的transaction(事务), 也支持
rollback(回滚)。而所有用户自定义的对象都是由sqlalchemy.ext.declarative.declarative_base()继承而来。

所以一套完整的workflow(工作流程)如下面所示:
    1. Define your mapping
    2. Create a session

官方文档:
    Declare a mapping, Create a Schema, Create an Instance of the Mapped Class:
        http://docs.sqlalchemy.org/en/rel_0_9/orm/tutorial.html#declare-a-mapping

    在定义表时, 会涉及定义不同的data type和constrain. 请参考:
    Define your Columns and Data Types:
        http://docs.sqlalchemy.org/en/rel_0_9/core/type_basics.html
        
    Define constrain:
        http://docs.sqlalchemy.org/en/rel_0_9/core/constraints.html
        
下面我们以sqlite电影数据库为例, 简单介绍如何定义ORM(对象到数据库的映射)。和创建Session准备和数据库通话。
关于Data type, 不同的引擎有不同的定义, 对于sqlite推荐使用如下设置:
    TEXT, Integer, REAL, DateTime, Date, PickleType
"""

from __future__ import print_function
from sqlalchemy.ext.declarative import declarative_base # 用于声明基类
from sqlalchemy import create_engine # 用于创建数据库引擎
from sqlalchemy.orm import sessionmaker # 用于创建会话

from sqlalchemy import Column # 列的定义
from sqlalchemy import Integer, BigInteger, SmallInteger, Boolean # 整数相关
from sqlalchemy import Float, Numeric, DECIMAL, REAL # 浮点小数相关
from sqlalchemy import String, TEXT # 字符串相关
from sqlalchemy import DateTime, Date, Time # 时间相关的
from sqlalchemy import PickleType # 任意python对象

import datetime # 在Movie.create_datetime会用到

Base = declarative_base() # 声明基类
class Movie(Base): # 从基类继承而来
    """定义object relation mapping
    如果前面学过sqlalchemy CORE中的Table, 我们可以用Movie.__table__来调用Movie所对应的Table对象,
    从而使用CORE中的语法对表进行增, 删, 插, 改。 
    """
    __tablename__ = "imdb"
    ID = Column(Integer, primary_key=True)
    title = Column(TEXT, nullable=False)
    release_date = Column(Date)
    imdb_rate = Column(REAL, nullable=False) # 0 ~ 10
    num_of_vote = Column(Integer, nullable=False)
    tags = Column(PickleType(protocol=3)) # python set
    create_datetime = Column(DateTime, default=datetime.datetime.now())
    
    def __str__(self): # define print(), str() behavior
        return """Movie(ID="{0}", title="{1}", release_date="{2}", imdb_rate={3}, num_of_vote={4}, 
            tags={5}""".format(self.ID, self.title, self.release_date, self.imdb_rate, self.num_of_vote, self.tags)
     

    def __repr__(self): # define repr() behavior
        return """Movie(ID="{0}", title="{1}", release_date="{2}", imdb_rate={3}, num_of_vote={4},
            tags={5}""".format(self.ID, self.title, self.release_date, self.imdb_rate, self.num_of_vote, self.tags)

engine = create_engine(r"sqlite:///ORM_tutorial.db", echo=False) # create a sqlite engine
Base.metadata.create_all(engine) # create the database
Session = sessionmaker() # create a session
Session.configure(bind=engine) # bind session to engine, one session can only bind to one engine at one time
session = Session() # create a session instance

"""
Now let's move to the next topic:
    basic, create table, select, insert, update, delete
"""