##encoding=utf8

from __future__ import print_function
from multiprocessing.dummy import Pool
import requests
import os
import time

try:
    os.mkdir("html")
except:
    pass
try:
    os.mkdir("html1")
except:
    pass

urls = [
    "http://www.python.org", 
    "http://www.python.org/about/",
    "http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html",
    "http://www.python.org/doc/",
    "http://www.python.org/download/",
    "http://www.python.org/getit/",
    "http://www.python.org/community/",
    "https://wiki.python.org/moin/",
    "http://planet.python.org/",
    "https://wiki.python.org/moin/LocalUserGroups",
    "http://www.python.org/psf/",
    "http://docs.python.org/devguide/",
    "http://www.python.org/community/awards/"
    ]

def save_url_request1(url):
    """save url as html in folder "html"
    """
    html = requests.get(url).text
    with open(os.path.join("html", str(hash(url))+".html" ), "wb") as f:
        f.write(html.encode("utf8"))

def save_url_request2(argument):
    """
    由于pool.map中map函数只支持单一输入的函数，所以我们的主函数必须只有一个输入
    """
    url, folder = argument
    html = requests.get(url).text
    with open(os.path.join(folder, str(hash(url))+".html" ), "wb") as f:
        f.write(html.encode("utf8"))


## 单进程
st = time.clock() # 8.919
for url in urls:
    save_url_request1(url) 
print(time.clock() - st)

## 多进程方法
pool = Pool(4) # 3.015
arguments = [(url, "html1") for url in urls]
st = time.clock()
pool.map(save_url_request2, arguments)
print(time.clock() - st)
