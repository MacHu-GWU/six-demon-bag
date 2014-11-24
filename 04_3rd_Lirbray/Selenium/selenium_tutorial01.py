##encoding=utf8
##version =py27
##author  =sanhe
##data    =2014-09-06

import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

reload(sys); # change the system default encoding = utf-8
eval('sys.setdefaultencoding("utf-8")')

def sleep(n):
    time.sleep(n)
    print '\t wake up from %s second.' % n

def example1():
    '''ENTER text in a input box'''
    driver = webdriver.Firefox()
    driver.get('https://www.python.org') # 打开python官方主页
    sleep(3)
    elem = driver.find_element_by_name('q') # 定位到 name = "q" 的query搜索框
    elem.send_keys("python 3.4.0") # 在文本框内输入内容
    elem.send_keys(Keys.RETURN) # 把内容send出去(相当于点击了"search")
    sleep(3)
    driver.close()
    
# example1()

def example2():
    driver = webdriver.Firefox()
    driver.get('https://www.python.org') # 打开python官方主页
    sleep(3)
    elem = driver.find_element_by_id('news')
    elem.click()
    elem = driver.find_element_by_xpath("//a[@title='Python Insider Blog Posts']")
    elem.click()
example2()