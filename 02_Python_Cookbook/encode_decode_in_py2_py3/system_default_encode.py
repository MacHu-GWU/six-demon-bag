##############################
#encoding=utf8
#version =py27, py33
#author  =sanhe
#date    =2014-10-18
#
#    (\ (\
#    ( -.-)o    I am a Rabbit!
#    o_(")(")
#
##############################

"""
As per the documentation: This allows you to switch from the default ASCII to other encodings 
such as UTF-8, which the Python runtime will use whenever it has to decode a string buffer to
unicode. This function is only available at Python start-up time, when Python scans the 
environment. It has to be called in a system-wide module, sitecustomize.py, After this 
module has been evaluated, the setdefaultencoding() function is removed from the sys module.

The only way to actually use it is with a reload hack that brings the attribute back.

Also, the use of sys.setdefaultencoding() has always been discouraged, and it has become 
a no-op in py3k. The encoding is hard-wired to utf-8 and changing it raises an error.

I suggest some pointers for read-up:

http://blog.ianbicking.org/illusive-setdefaultencoding.html
http://nedbatchelder.com/blog/200401/printing_unicode_from_python.html
http://www.diveintopython3.net/strings.html#one-ring-to-rule-them-all
http://boodebr.org/main/python/all-about-python-and-unicode
http://blog.notdot.net/2010/07/Getting-unicode-right-in-Python

扩展阅读:
    深入理解字符编码    http://my.oschina.net/goldenshaw/blog?catalog=536953
"""

from __future__ import print_function
import sys

def example1():
    """How to print UTF-8 encoded text to the console in Python < 3
    Have to run this script in console.
    """
    reload(sys)
    sys.setdefaultencoding("utf-8")
    print("中国")
    
example1()
