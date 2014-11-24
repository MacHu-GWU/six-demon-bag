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

"""
超强字符输出函数string.format用法详解
Ref = https://docs.python.org/2/library/string.html
"""

from __future__ import print_function

def example1():
    """basic usage
    Ref = https://docs.python.org/2/library/string.html#format-string-syntax
    """
    print("{:=^40}".format("example1"))
    
    s = "First, thou shalt count to {0}".format(100) # References first positional argument
    print(s)
    
    s = "Bring me a {}".format("banana") # Implicitly references the first positional argument
    print(s)
    
    s = "From {} to {}".format(1, 100) # Same as "From {0} to {1}"
    print(s)
    
    s = "From {0} to {1}".format(1, 100) # Same as "From {} to {}"
    print(s)
    
    s = "{2}, {1}, {0}".format(*"abc")      # unpacking argument sequence
    print(s)
    
    s = "{0}{1}{0}".format("aaa", "bbb")   # arguments" indices can be repeated
    print(s)
    
    s = "My quest is {name}".format(50, name=100) # References keyword argument "name"
    print(s)
    
    s = "Units destroyed: {players[0]}".format(players=[99, 98, 97])  # First element of keyword argument "players".
    print(s)
    
    s = "Get item from dictionary: {translate[1]}".format(translate={1:"easy", 
                                                                     2:"hard"})
    print(s)

example1()

def example2():
    class Ak(object):
        def __str__(self):
            return "I am an AK47, dadada!!!"
        
        def __repr__(self):
            return "name = ak"
    
    print("{:=^40}".format("example2"))
    ak = Ak()
    s = "{0!s}".format(ak)  # Calls str() on the argument first
    print(s)

    s = "{0!r}".format(ak)  # Calls repr() on the argument first
    print(s)

example2()

def example3():
    """
    [EN]Alignment
    [CN]对齐
    Ref = https://docs.python.org/2/library/string.html#format-specification-mini-language
    """
    print("{:=^40}".format("example3"))

    s = "{:<30}".format("left aligned")
    print(s)
    
    s = "{:>30}".format("right aligned")
    print(s)
    
    s = "{:^30}".format("centered")
    print(s)
    
    s = "{:*^30}".format("centered")  # use "*" as a fill char
    print(s)
    
example3()

def example4():
    """正负号符号显示
    """
    print("{:=^40}".format("example4"))
    s = "{:+f}; {:+f}".format(3.14, -3.14)  # show it always
    print(s)

    s = "{: f}; {: f}".format(3.14, -3.14)  # show a space for positive numbers
    print(s)

    s = "{:-f}; {:-f}".format(3.14, -3.14)  # show only the minus -- same as "{:f}; {:f}"
    print(s)
   
example4()

def example5():
    # format also supports binary numbers
    print("{:=^40}".format("example5"))
    
    s = "int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42)
    print(s)
    
    # with 0x, 0o, or 0b as prefix:
    s = "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42)    
    print(s)
    
example5()

def example6():
    """千分号
    """
    print("{:=^40}".format("example6"))
    s = '{:,}'.format(1234567890)
    print(s)
    
example6()

def example7():
    """小数点精度
    """
    print("{:=^40}".format("example7"))
    points = 19.5
    total = 22
    s = "Correct answers: {:.2%}".format(points/total)
    print(s)

example7()