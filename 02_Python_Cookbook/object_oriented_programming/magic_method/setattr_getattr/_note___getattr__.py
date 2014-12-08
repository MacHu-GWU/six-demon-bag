##################################
#encoding=utf8                   #
#version =py27, py33             #
#author  =sanhe                  #
#date    =2014-10-29             #
#                                #
#    (\ (\                       #
#    ( -.-)o    I am a Rabbit!   #
#    o_(")(")                    #
#                                #
##################################

from __future__ import print_function

def example1():
    """
    def __getattr__ (self, attr): return X ---> defines the behavior of self.attr
    """
    class Form(object):
        def __init__(self, name):
            self.name = name
            self.info = dict()
            
        def __str__(self):
            return str(self.info)
        
        def __getattr__(self, attr):
            return self.info[attr]
    
    print("{:=^40}".format("example1"))
    
    f = Form("I-20")
    f.info = {"fullname": "Mac",
              "age" : 25,
              "gender" : "male"}
    
    print(f.name, f.fullname)
    print(hasattr(f, "name")) # "hasattr" is a built-in function, return boolean of having attributes
    print(hasattr(f, "age")) # "hasattr" also works as the way of __getattr__
    print(hasattr(f, "height")) # not in attributes
    print(f.height) # not exist, then raise an error
    
# example1()
    
def example2():
    class Form(object):
        def __init__(self, name):
            self.name = name
            self.info = dict()
            
        def __str__(self):
            return str(self.info)
        
        def __getattr__(self, attr):
            if attr in self.info: ##<==定义了属性存在的情况
                return self.info[attr]
            else: ##<==定义了属性不存在的情况，返回None
                return None
    
    print("{:=^40}".format("example2"))
    
    f = Form("I-20")
    f.info = {"fullname": "Mac",
              "age" : 25,
              "gender" : "male"}

    print(f.name, f.fullname, f.height)
    print(hasattr(f, "name")) # "hasattr" is a built-in function, return boolean of having attributes
    print(hasattr(f, "age")) # "hasattr" also works as the way of __getattr__
    
    ## 注意：
    ## 当height不在self.info中的时候，由于定义了属性不存在的情况
    ## __getattr__也是会返回None的。所以无论name是什么, 即使属性中没有
    ## hasattr(f, name) 都会返回True
    print(hasattr(f, "height")) # not in attributes
    
# example2()

def example3():
    class Form(object):
        def __init__(self, name):
            self.name = name
            self.info = dict()
            
        def __str__(self):
            return str(self.info)
        
        def __getattr__(self, attr):
            if attr in self.info: ##<==定义了属性存在的情况
                return self.info[attr]
            else: ##<==定义了属性不存在的情况，返回None
                return None
    
    print("{:=^40}".format("example3"))
    f = Form("I-20")
    f.info = {"fullname": "Mac",
              "age" : 25,
              "gender" : "male",
              "info": 9999}
    print(f.age)
    
    # 如果属性名称是类中自带的属性名，而不是通过setattr设定的属性名，我们调用的时候会调用哪一个？
    # 会调用默认的属性。因为系统会优先在属性__dir__中找，如果找不到，再去调用__getattr__
    print(f.info) 
    
example3()