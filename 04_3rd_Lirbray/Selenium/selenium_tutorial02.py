##encoding=utf8
##version =py27
##author  =sanhe
##Date    =2014-09-07

'''
如何选择下拉菜单中的选项
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

def sleep(n):
    time.sleep(n)
    print '\t wake up from %s second.' % n

def example1():
    '''把priceline上的rooms修改成2 Rooms
    '''
    url = 'http://www.priceline.com/' #
    driver = webdriver.Firefox()
    driver.get(url)
    sleep(3)
    select = Select(  driver.find_element_by_id('hotel-rooms')  ) # 从html元素生成一个select对象
    print [element.text for element in select.options] # 打印所有选项
    select.select_by_visible_text('2 Rooms') # 通过文本选择select选项
    sleep(10)
    driver.close()
    
# example1()

def example2():
    '''修改priceline上的check-in, check-out日期
    '''
    pass

# example2()