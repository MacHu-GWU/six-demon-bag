##encoding=utf8

"""
sqlalchemy(下简称SA)的哲学

SA的核心有两个完全不同的功能, 一个在另一个之上工作。一个是SQL语言构造器(CORE), 另一个是ORM。
    SQL语言构造器允许调用ClauseElements来构造SQL表达式。这些ClauseElements可以在编译成字符串并绑定到数据
    库后用于执行, 并返回一个叫做ResultProxy的对象, 类似于一个结果集对象, 但是更象dbapi高版本的cursor对象。

    ORM是建立在SQL语言构造器之上的工具集, 用于将Python对象映射到数据库的行, 提供了一系列接口用于从数据库中
    存取对象(行)。在ORM工作时, 在底层调用SQL语言构造器的API, 这些通用的操作有些许的不同。不同的是, 你不再
    使用行, 而是使用自定义类的对象来操作。另外, 数据库的查询方式也不同, ORM的可以生成大多数的SQL查询, 除此
    之外还可以在类中定义更多操作。

SA功能强大, 无与伦比, 只是有两个混合在一起的方法有些复杂。有效的使用SA的方法是先了解这两种不同的工具集, 这
是两个不同的概念, 而大家常常混交SQL语言构造器和ORM。关键的不同是, 使用cursor形式的结果集时使用的是SQL语言
构造器；而使用类实例进行管理时使用的是ORM。

Full document:
    http://docs.sqlalchemy.org/en/rel_0_9/index.html

学习CORE, 请阅读tutorial/CORE/01_readme_first.py    
学习ORM, 请阅读tutorial/ORM/01_readme_first.py
"""