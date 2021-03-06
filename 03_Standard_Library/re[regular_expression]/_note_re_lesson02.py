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
import re

""" =========== 元字符 及作用 ============
元字符包括 ^ $ * + ? { [ ] \ | ( ) -
普通来说，如果模式串是a，那么被匹配的就是a。但是对于模式串来说，如果模式串是?，那么被匹配的并不是?。
每个元字符都有自己的特殊用途和含义。

1. [和]：表示集合。例如：
    [abc]将匹配"a", "b", 或 "c"中的任意一个字符
    
2. - : 表示 从x至y。例如：
    [a-c]将匹配区间a-c内的所有字符，同[abc]
    
3. []集合中的元字符会失去元字符的特殊功能，而自动转化为普通字符，例如：
    [akm$]将匹配字符"a", "k", "m", 或 "$" 中的任意一个；"$"通常用作元字符，但在字符类别里，其特性被除去，恢复成普通字符。
    
4. ^：表示补集，可以用补集来匹配不在区间范围内的字符。
其做法是把"^"作为类别的首个字符；其它地方的"^"只会简单匹配 "^"字符本身。例如：
    例如，[^5] 将匹配除 "5" 之外的任意字符。

5. |：表示或，例如：
    a|b将匹配a或者b
    
6. \：表示转义字符。在\之后的字符将会被转义，
\之后的元字符将失去特性，恢复成普通字符，例如：
    \?将匹配问号本身, \\将匹配\本身
而\之后的普通字符将不再是普通字符,而会变成预定义字符集
这点将放在<预定义字符集>一节中详细说明

7. ?, +, *, {}表示重复，将在lesson4中详细介绍

8. r"模式串"：模式串之前的r是表示普通字符串。在正则中由于如果要匹配\，则实际上要2个\。
如果要匹配2个\，那实际上要4个\。如果加上r的话就表示\后面的全部都是普通字符串，
那么为了匹配2个\，只需要用3个\即r"\\\"就好了, 所以r关键字则可以方便的处理反斜杠。例如：
    r"a\\b" 则能匹配到 "xxxa\\byyy" 中的 "a\\b", 而仅仅"a\\b"则是无法匹配到的
"""
## Example1: []表集合
print(1, re.findall(r"[abc]", "xxxayyybzzzckkk") ) ## 1.匹配到a, b, c

## Example2: - 表示 x 至 y
print(2, re.findall(r"[a-c]", "xxxayyybzzzckkk") ) ## 2.匹配到a, b, c

## Example3: []集合中的元字符失去普通字符
print(3, re.findall(r"[abc?]", "xxxayyybzzzckkk?") ) ## 3.匹配到a, b, c, ?

## Example4: ^表示补集合
print(4, re.findall(r"[^abc]", "xxxayyybzzzckkk") ) ## 4.匹配到x, y, z, k

## Example5: |表示或
print(5, re.findall(r"a|b", "xxxayyybbzzz") ) ## 5.匹配到a, b, b

## Example6: \表示转义字符
print(6, re.findall(r"a\\b", "xxxa\\byyy") ) ## 6.匹配 a\\b
print(7, re.findall("a\\\\b", "xxxa\\byyy") ) ## 7.匹配到 a\\b