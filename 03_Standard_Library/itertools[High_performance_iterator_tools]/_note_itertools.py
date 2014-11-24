##################################
#encoding=utf8                   #
#version =py27, py33             #
#author  =sanhe                  #
#date    =2014-11-15             #
#                                #
#    (\ (\                       #
#    ( -.-)o    I am a Rabbit!   #
#    o_(")(")                    #
#                                #
##################################

from __future__ import print_function
import itertools

def demo_count(): ## 计数器
    """ itertools.count(start, step) """
    print("{:=^40}".format("demo_count"))
    tank = ["a", "b", "c"]
    counter = itertools.count(1,1) ## begin with 1, step is 1
    for i in tank: ##[注：]由于counter是无限长的生成器，但如果counter不是无限长
        print(i, next(counter)) ## 而当counter长度小于tank的时候，就会因为counter中的元素用完，无法next，而产生异常
        
# demo_count()

def demo_cycle(): ## 循环器
    """ itertools.cycle(iterables) """
    print("{:=^40}".format("demo_cycle"))
    cycler = itertools.cycle([1,2,3])
    data = "abcdefghijklmnopqrstuvwxyz"
    for i in data:
        print(i, next(cycler))
        
# demo_cycle()

def demo_chain(): ## 对多个可迭代对象，按顺序依次迭代。相当于可迭代对象的合并
    """ itertools.chain(*iterables) """
    print("{:=^40}".format("demo_chain"))
    c = itertools.chain("123", "abc", "XYZ") ## 先123,再abc,最后XYZ
    for i in c:
        print(i)
        
# demo_chain()

def demo_izip(): ## 低内存消耗的zip方法
    """ itertools.izip(iterable_obj1, iterable_obj2) 
    在python3中，zip的工作原理已经是生成器模式了，所以无需再用izip
    """
    print("{:=^40}".format("demo_izip"))
    a1 = "abcde"
    a2 = [1,2,3,4] ## [注:]长度可以不同
    print(zip(a1,a2) )## 普通的zip，一次对全部进行压缩
    ## 当a1和a2特别大的时候，如果要同时对两个进行循环，那么内存消耗就会很大
    for i in itertools.izip(a1, a2): ## itertools.izip一次只zip一对
        print(i)
        
# demo_izip()

def demo_izip_longest():
    """ 按照给定的若干个iterable中最常的那个进行打包，不够的部分用fillvalue填
    """
    print("{:=^40}".format("demo_izip"))
    for i in itertools.izip_longest("abc", [1,2,3,4], "ABCDE", fillvalue = "O"):
        print(i)
    
# demo_izip_longest()

def demo_repeat():
    """ itertools.repeat(object, number)"""
    ## 如果要重复对一个对象进行操作很多次，如果用 for i in obj * n: 这样内存中需要
    ## 建立n个obj的副本，很浪费内存，而用 for i in itertools.repeat(obj, n)就不用
    print("{:=^40}".format("demo_repeat"))
    r = itertools.repeat("abcde", 2)
    for obj in r:
        print(obj)
        
# demo_repeat()

def demo_compress(): ## 数据+选择器，根据选择器的定义，从数据中选则数据
    """ itertools.compress(data, selectors) """
    print("{:=^40}".format("demo_compress"))
    data = "abcdefg" ## 可迭代数据
    selector = [1,0,1,0,0,1] ## 选择器列表
    for i in itertools.compress(data, selector):
        print(i)
        
# demo_compress()

def demo_combinations(): ## 排列组合之-组合
    """ itertools.combinations(iterables, number) """
    print("{:=^40}".format("demo_combinations"))
    c = itertools.combinations("abc", 2) ## 从可迭代对象中，选取n个元素，变成元组
    for i in c: ## 对所有可能的组合，进行循环
        print(i)
        
# demo_combinations()

def demo_permutations(): ## 排列组合之-排列
    """ itertools.permutations(iterables, number)"""
    print("{:=^40}".format("demo_permutations"))
    c = itertools.permutations("abc", 2) ## 从可迭代对象中，选取n个元素，变成元组
    for i in c: ## 对所有可能的排列，进行循环
        print(i)
        
# demo_permutations()
