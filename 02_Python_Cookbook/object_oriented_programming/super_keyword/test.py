##encoding=UTF-8

from __future__ import print_function
import sqlite3

def example1():
    class ClassA():
        @staticmethod
        def display():
            print("A")
            
    class ClassB():
        @staticmethod
        def display():
            print("B")
    
    class ClassC(ClassB):
        def display(self):
            """这样写的时候万一你要更改ClassA的名字, 或者改成ClassB, 那么你所有的ClassB.display()
            都要修改
            """
            ClassB.display()
            
    b = ClassC()
    b.display()

# example1()

def example2():
    class ClassA():
        @staticmethod
        def display():
            print("A")
            
    class ClassB():
        @staticmethod
        def display():
            print("B")
            
    class ClassC(ClassB):
        def display(self):
            """这样写你只需要改动ClassC的父类即可
            super(type, self).method()
            是直接调用ClassC的父类的.method()方法
            """
            super(ClassC, self).display()
            
    b = ClassC()
    b.display()

# example2()


def method1():
    """
    在这个例子中, 通常我们这样生成sqltie3.Connection和sqlite3.Cursor对象:
    
    connect = sqlite3.connect(":memory:")
    cursor = connect.cursor()
    
    我们如果要创造一个新的类, 继承了sqltie3.Connection和sqlite3.Cursor的所有方法, 而且要包括一些新的方法
    我们也许需要两个新的类MyConnect和MyCursor。MyConnect继承于sqltie3.Connection, 而要生成MyCursor时, 如
    过我们直接使用MyConnect.cursor(), 由于这个继承于sqlite3.Connection.cursor()方法, 所以返回的是一个
    sqlite3.Cursor, 无法享受到我们为MyCursor定义的方法。
    """
    class MyConnect(sqlite3.Connection):
        def cursor(self):
            return super(MyConnect, self).cursor(MyCursor)
    
    class MyCursor(sqlite3.Cursor):
        def run_cmd(self, *argv, **kwarg):
            return self.execute(*argv, **kwarg)
    
    connect = MyConnect(":memory:")
    cursor = connect.cursor()
    cursor.run_cmd("CREATE TABLE test (value INTEGER)")
    cursor.run_cmd("INSERT INTO test VALUES (?)", (1,))
    print(cursor.run_cmd("SELECT * FROM test").fetchall())
    
# method1()

class C(object):
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")
    
c = C()
print(c.x)