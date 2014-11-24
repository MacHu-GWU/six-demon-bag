##coding=utf8

"""测试在读取网页，本地文件时，里面的中文编码不是utf-8时，所出现的乱码问题
测试日期: 2014-08-17
测试机器: Macbook Air OS
"""

import requests
import bs4

def url_html(url, timeout = 6):
    """返回url的HTML内容
    """
    headers = {"User-Agent": ("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11, "
                              "(KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"),
               "Accept":"text/html;q=0.9,*/*;q=0.8",
               "Accept-Charset":"ISO-8859-1,utf-8;q=0.7,*;q=0.3",
               "Accept-Encoding":"gzip",
               "Connection":"close",
               "Referer":None}
    r = requests.get(url, headers = headers, timeout = timeout)
    return r.text

def prt_both(ob):
    """打印对象以及对象类型"""
    print "%s - %s" % (ob, type(ob))
    
def example1():
    """测试读取维基百科的中文页面
    """
    url = "http://zh.wikipedia.org/wiki/%E6%B1%89%E8%AF%AD" ## 维基百科
    soup = bs4.BeautifulSoup( url_html(url) )
    print soup.text
    
# example1()

def example2():
    with open("readme.txt", "rb") as f:
        text = f.read()
    print text
    
# example2()