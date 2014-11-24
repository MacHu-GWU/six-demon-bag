##encoding=utf8

"""
zillow作为美国房地产咨询的第一大门户网站，有很多人都觊觎它的数据。所以zillow的防爬虫技术也特别的强大。
每次用机器登录zillow的网页，都会需要输入图片上的验证码。所以我们不得不使用selenium技术直接操作浏览器，
从而绕开它的拦阻。
"""

from __future__ import print_function
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as BS4
import time
import sys

reload(sys); # change the system default encoding = utf-8
eval('sys.setdefaultencoding("utf-8")') # python3中不需要这样做

def sleep(n):
    time.sleep(n)
    print("\t wake up from %s second." % n)
    
def property_detail_by_street_and_zipcode(driver, street, zipcode):
    """ENTER text in a input box"""
    driver.get("http://www.zillow.com/") # 再次打开页面
    elem = driver.find_element_by_name("citystatezip") # 定位到 name = "q" 的query搜索框
    elem.send_keys("%s %s" % (street, zipcode)) # 在文本框内输入内容
    elem.send_keys(Keys.RETURN) # 把内容send出去(相当于点击了"search")
    html = driver.page_source
    
    soup = BS4(html)
    a = soup.find("a", class_ = "routable mask hdp-link")
    url = "http://www.zillow.com" + a["href"]
    
    driver.get(url)
    html = driver.page_source
    return html
    
def main():
    query = [("4533 Whittemore Pl # 1531","22030"),
             ("13 Trudy Way","20878")]
    driver = webdriver.Firefox()
    driver.get("http://www.zillow.com/")
    sleep(10)
    for street, zipcode in query:
        html = property_detail_by_street_and_zipcode(driver, street, zipcode)
        with open("%s_%s.html" % (street, zipcode), "w") as f:
            f.write(html.encode())
    print("Complete")
    
main()