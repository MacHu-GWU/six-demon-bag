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
    """全局变量在函数内部被调用，然后被修改，当跳出函数内部时
    全局变量的值已经是被修改过的了
    """
    def test():
        d["a"] += 1
        
    d = {"a": 1}
    test()
    print(d)
        
# example1()

def example2():
    """局部变量没有被函数内部共享调用"""
    def test(num):
        num += 1
        return num
    a = 1 # 原num对象
    b = test(a)
    print(b) # 传递进去的是num的副本，而不是num
    print(a) # 所以num没有收到影响
    
# example2()

def example3():
    """对于mutable对象，被传入函数中如果做了变化，那么
    函数外的原来的对象也会被变化。请看list和dict的例子
    """
    def test1(array):
        array.append(1)
        return array
    l = [1,2,3]
    l1 = test(l)
    print(l1)
    print(l)

    def test(dictionary):
        dictionary["HELLO"] = "WORLD"
        return dictionary
    
    d = {1: "a"}
    d1 = test(d)
    print(d1)
    print(d)
    
# example3()

def example4():
    """对于mutable对象，被传入函数中如果做了变化，那么
    函数外的原来的对象也会被变化。
    为了避免这一情况，可以用copy强制生成一个新对象
    """
    import copy
    def test(array):
        array = copy.copy(array)
        array.append(1)
        return array
    l = [1,2,3]
    l1 = test(l)
    print(l1)
    print(l)

# example4()