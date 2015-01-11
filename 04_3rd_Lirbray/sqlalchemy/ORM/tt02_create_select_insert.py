##encoding=utf8

"""
CREATE TABLE:
    
    sqlalchemy automatically create all table when
    
        Base = declarative_base()
    
        define schema...
        
        engine = create_engine(r"sqlite:///ORM_tutorial.db", echo=False)
        Base.metadata.create_all(engine) # <=== user defined schema is stored in metadata.


Flush and Commit
    http://stackoverflow.com/questions/4201455/sqlalchemy-whats-the-difference-between-flush-and-commit
"""

from __future__ import print_function
from datetime import date
import os
import timeit

def reset(): # 用于快速重置数据库
    try: os.remove("ORM_tutorial.db") 
    except: pass
    
reset() # <=== comment it to prevent reseting

from tt01_readme_first import Movie, session as ses

def prt_all(): # 为了测试方便, 首先我们要学会如何打印表中的所有内容
    """本函数用于打印目前表中的所有内容, 相当于select *;"""
    for movie in ses.query(Movie):
        print(movie)

def insert_data():
    """通常有2种insert方式
    1. insert one, commit one
        if raise IntegrityError, we can roll back and skip to the next entry.
        usually x10 slower than insert all, commit once
        
    2. insert many, commit once
        if raise IntegrityError, then you lose all insert.
        if there's no IntegrityError, it's usually x10 faster than insert one, commit one
    """
    
    from sqlalchemy.exc import IntegrityError # 完整性异常
    
    entries = [
               Movie(ID=1, title="The Shawshank Redemption", release_date=date(1994,10,14), imdb_rate=9.3, 
                     num_of_vote=1361062, tags=set(["Crime", "Drama"])),
               Movie(ID=2, title="The Godfather", release_date=date(1972,3,2), imdb_rate=9.2, 
                     num_of_vote=937204, tags=set(["Crime", "Drama"])),
               Movie(ID=3, title="Schindler's List", release_date=date(1994,2,4), imdb_rate=8.9, 
                     num_of_vote=687998, tags=set(["History", "Biography", "Drama"])),
               Movie(ID=4, title="The Lord of the Rings: The Return of the King", release_date=date(2003,12,17), imdb_rate=8.9, 
                     num_of_vote=972328, tags=set(["Adventure", "Fantasy"])),
               ]
    
    entries1 = [entries[0], entries[1], entries[2] ]
    entries2 = [entries[1], entries[2], entries[3] ]
    
    def insert1():
        """insert one, commit one"""
        for movie in entries:
            ses.add(movie)
            try:
                ses.commit()
            except IntegrityError:
                ses.rollback()
    
    insert1()
    
    def insert2():
        """insert many, commit once"""
        for movie in entries:
            ses.add(movie)
        try: # 尝试commit
            ses.commit()
        except IntegrityError: # 完整性错误
            ses.rollback() # 回滚
            for movie in entries: # 逐条插入
                ses.add(movie)
                try: # 尝试commit
                    ses.commit()
                except IntegrityError: # 完整性错误
                    ses.rollback() # 回滚
                    
#     insert2()

#     prt_all()
    
insert_data()


def query_data():
    """
    关于以ORM方式进行query的性能问题的一些结论
    
    我们对一个存放了200,000条User的表做了如下实验:
    for user in session.query(User): # 12.0 second
        break # 只返回了1条记录用了 12 秒
    
    for user in session.query(User): # 12.5 second
        pass # 返回了所有200,000条记录也只用了 12.5 秒
    
    for user in session.query(User).limit(1): # 0.01
        pass # 而如果query的结果只有1条记录, 则只用了0.01秒, 和直接执行sql语句相差无几
    
    for row in engine.connect.execute("SELECT * FROM user"): # 0.006 
        break # 直接执行sql语句只用了0.006秒, 节省的0.004秒可能被用来将row转化为User(object)了
        
    可见ORM query的机制是先把所有的结果转化成对象, 最后再以生成器的形式返回给用户。在搜索结果很多的时候
    会消耗大量时间
    
    Query
        http://docs.sqlalchemy.org/en/rel_0_9/orm/tutorial.html#querying
        
        http://docs.sqlalchemy.org/en/rel_0_9/orm/query.html
    """
    from sqlalchemy import and_ # for SQL BETWEEN Clause
    
    def select_all():
        print("\n### {} ###".format("SELECT * FROM imdb;"))
        for movie in ses.query(Movie):
            print(movie, type(movie))
    
#     select_all()

    def select_where():
        print("\n### {} ###".format("SELECT * FROM imdb WHERE imdb_rate > 9.0;"))
        for movie in ses.query(Movie).filter(Movie.imdb_rate > 9.0):
            print("\t", movie)
                
        print("\n### {} ###".format("SELECT * FROM imdb WHERE release_date BETWEEN '1990-01-01' AND '2000-01-01';"))
        for movie in ses.query(Movie).filter(Movie.release_date.between(date(1900,1,1), date(2000,1,1) ) ):
            print("\t", movie)

        print("\n### {} ###".format("SELECT * FROM imdb WHERE release_date < '1990-01-01' AND imdb_rate > 8.5;"))
        for movie in ses.query(Movie).filter(and_(Movie.release_date < date(1990,1,1), Movie.imdb_rate > 8.5)):
            print("\t", movie)

        print("\n### {} ###".format("SELECT * FROM imdb WHERE title in ('The Shawshank Redemption', 'The Godfather');"))
        for movie in ses.query(Movie).filter(Movie.title.in_(["The Shawshank Redemption",
                                                              "The Godfather"])):
            print("\t", movie)
            
#     select_where()
    
    def select_order_by():
        print("\n### {} ###".format("SELECT * FROM imdb ORDER BY imdb_rate DESC, release_date DESC;"))
        for movie in ses.query(Movie).order_by(Movie.imdb_rate.desc(), Movie.release_date.desc()):
            print(movie)
    
#     select_order_by()
    
    def select_limit():
        print("\n### {} ###".format("SELECT * FROM imdb LIMIT 3;"))
        for movie in ses.query(Movie).limit(3):
            print(movie, type(movie))
            
#     select_limit()
    
# query_data()


def update_data():
    ### === 方法1, 直接对query的结果进行统一的update ===
#     ses.query(Movie).filter(Movie.ID == 1).update({"title": "new title"})
    
    ### === 方法2 === 
    for movie in ses.query(Movie).all(): # 这种方式, 可以突破sql语句的限制, 进行复杂的条件筛选
        if movie.release_date < date(1980,1,1): # 1980年之前的电影标题加后缀[old movie]
            ses.query(Movie).filter(Movie.ID == movie.ID).update({"title": movie.title + "[old movie]"})    
    ses.commit()
    
    
    prt_all()
    
# update_data()