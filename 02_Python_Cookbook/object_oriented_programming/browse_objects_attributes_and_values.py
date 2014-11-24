##encoding=utf8
##version =py27, py33
##author  =sanhe
##date    =2014-10-23

from __future__ import print_function

class MyClass(object): # <= object is the most basic class for creating all other class
    """Test Class
    """
    def __init__(self):
        """This special method is to initialize the object
        """
        self.a = 1
        self.b = 2.5
        self.c = ["a", "b"]
        self.d = {1: "a", 2: "b"}
        
    def showoff(self):
        """Customized method for test"""
        print("<%s><%s><%s><%s>" % (self.a, self.b, self.c, self.d) )
        
def example1():
    """Print all (attribute, value) pairs
    """
    mc = MyClass()
    for k, v in vars(mc).items():
        print("%s = %s" % (k, v) )

# example1()

def example2(): # magic attributes
    """__class__ 
    ref = http://pyzh.readthedocs.org/en/latest/python-questions-on-stackoverflow.html#id17
    """
    mc = MyClass()
    print(mc.__class__) # = MyClass
    print(mc.__class__.__class__) # type class is a class to create all other class
    text = "abcd"
    print(text.__class__) # = string
    print(text.__class__.__class__) # = type
    
# example2()

def example3(): # magic attributes
    """__doc__ is to print object document string.
    In python, class, function are all object
    """
    mc = MyClass()
    print(mc.__doc__) # mc is a class, so print the class doc string
    print(mc.__init__.__doc__) # mc.__init__ is a function, so print the function doc string
    print(help(mc)) # print all doc string for class "MyClass"

# example3()

def example4(): # magic attributes
    mc = MyClass()
    print(mc.__dict__) # alternative for: for attr, value in vars(mc).iteritems():
       
# example4()

def example5(): #
    """__format__ built in format method. Substitute the "%s" % variable method in PYTHON 3
    ref = https://docs.python.org/2/whatsnew/2.6.html#pep-3101-advanced-string-formatting
    """
    mc = MyClass()
    print(format(mc))
    
# example5()