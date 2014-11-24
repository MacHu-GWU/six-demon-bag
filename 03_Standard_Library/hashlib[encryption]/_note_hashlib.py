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
import hashlib

"""对一个字符串进行hash通常有两种方法"""

def demo1_hash_a_string1():
    """=== 方法1 ===
    注:  m.update(string) 如果多次用，第二次是在已有的基础上，从后面append字符。例如:
    m.update("a") 接着 m.update("b")
    与 一开始就 m.update("ab")等效，如果要重新hash另一个字符串，必须新建一个hash对象
    """
    m = hashlib.md5() ## md5, sha1, sha512 通常用sha512比较安全
    m.update("a".encode("utf-8") ) ## 给m填充字节流，在python3中需要编码。
    print(m.digest() ) ## 产生字节码，显示的字符跟当前环境下的默认编码格式有关
    print(m.hexdigest() ) ## <=== 产生人类可读的hash后的字符串, 网站注册用的密码通常就是这个

# demo1_hash_a_string1()
    
def demo2_hash_a_string2():
    """=== 方法2 ===
    """
    h = hashlib.new("md5","ab".encode("utf-8") ) ## hashlib.new(algorithm, string)
    print(h.digest() )
    print(h.hexdigest() )

# demo2_hash_a_string2()

"""通常在储存用户密码的时候，为了防止字典破解，彩虹表破解等方法，要给用户的密码在前面
或者后面加上盐。盐需要符合几个条件： 1.随机生成    2.长度够长。 盐可以明文储存在服务器上
python中有一个函数 os.urandom(number)可以用来生成指定长度的字符串。
=== 网站用户登录，身份验证密码校验流程 ===
"""

def demo3_salted_hash_encryption():
    ## 生成指定字长的随机字符串
    import os
    salt = os.urandom(32) ## 生成指定长度的随机字符串作为盐
    pwd =("obama2014".encode("utf-8")) # <==用户注册时使用的密码
    h = hashlib.new("sha512", pwd)
    h.update(salt)
    stored_pwd = h.hexdigest()
    print("数据库中储存的hash值为:\n%s" % stored_pwd)

    ## 用户输入自己的密码
    enter = "obama2014".encode("utf-8")
    h = hashlib.new("sha512", enter + salt)
    print("用户输入的密码加盐后生成的hash值为:\n%s" % h.hexdigest() )
    
demo3_salted_hash_encryption()