##################################
#encoding=utf8                   #
#version =py27, py33             #
#author  =sanhe                  #
#date    =2014-11-01             #
#                                #
#    (\ (\                       #
#    ( -.-)o    I am a Rabbit!   #
#    o_(")(")                    #
#                                #
##################################

"""字符串
字符我们都知道其实是一个

扩展阅读:
    深入理解字符编码    http://my.oschina.net/goldenshaw/blog?catalog=536953
"""

from __future__ import print_function

text1 = "Hello world!"
text2 = "Welcome to Python world."
text = text1 + " " + text2
print(text)
print(text.split(" ")) # 以" "为分隔符把字符串分割开

# 在python中字符串是不可变对象，也就意味着text1 = text1 + text2时，
# 是额外创建了一个新的字符串text1+text2 然后赋值给了text1。当你有
# 很多字符串需要相连时，如果用循环，然后 text = text + text_i的方式
# 会创建很多不必要的临时字符串。而用"".join(list_of_strings)才是正确
# 的做法

print(" ".join(['Hello', 
               'world!', 
               'Welcome', 
               'to', 
               'Python', 
               'world.'])) # 以空格字符为字符串连接所有的字符串

print(chr(88))  # 把ASCII码转化为字符
print(ord("X")) # 把字符转化为ASCII码
print(len("HelloWorld")) # 取得字符串的长度
