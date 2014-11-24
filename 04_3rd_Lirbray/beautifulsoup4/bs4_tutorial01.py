##encoding=utf8
##version =py27
##author=Sanhe
##date  =2014-09-06

from crawler import Crawler
from bs4 import BeautifulSoup as BS4 # 用BS4 代替 bs4.BeautifulSoup
import requests
import re

def example1():
    '''两大基本找tag的方式
    1. find
    2. findAll (py2中是findAll, 但是由于py3的新的命名标准, 被更改为了find_all。但是原来的findAll依然可用
                这两种method的本质是一模一样的)
    '''
    url = 'http://www.cvs.com/stores/cvs-pharmacy-locations'
    spider = Crawler()
    html = spider.html(url)
    if html:
        soup = BS4(html)
#         print soup.find('li') # just find the first one
#         print soup.find_all('li') # find a list of tag match your search
        print soup.find_all('li', limit = 3) # find first 3 tag match your search

# example1()

def example2():
    '''find tag by id
    注：除了id，bs4同样可以根据其他的tag属性比如href, title来搜索。
    使用上只要把id替换成其他属性名即可。但是注意一点，class由于是
    python内置关键字，所以class属性无法用 soup.find("tagname", class = "category")
    来查找
    '''
    html = '<li><a id="nav-world" class="nav-on" href="/WORLD/" title="World News International Headlines Stories and Video from CNN.com">World</a></li>'
    soup = BS4(html)
    print '==========原html==========\n%s\n==========以下是输出结果==========' % soup.prettify()
    print soup.find('a', id = 'nav-world')
    
# example2()

def example3():
    '''find tag by regular expression
    注：example2, example3中的这种根据某个tag属性来查找的方法，还
    可以组合起来进行。比如: id = xxx, href = xxx... 这里就不做演示了
    '''
    html = '<li><a href="/stores/cvs-pharmacy-locations/California">California</a></li>'
    soup = BS4(html)
    print '==========原html==========\n%s\n==========以下是输出结果==========' % soup.prettify()
    print soup.find('a', href = re.compile(r'/stores/cvs-pharmacy-locations/[\s\S]*') )
    
# example3()

def example4():
    '''
    有部分在html5中的tag属性不符合python的命名空间，也就无法作为keyword
    被传入find的参数里，所以也就无法通过上面的两种方法来查找，但是我们可以
    将它们传入一个字典中查找。请看例子：
    '''
    html = '<div data-foo="value">foo!</div>'
    soup = BS4(html)
    print '==========原html==========\n%s\n==========以下是输出结果==========' % soup.prettify()
    print soup.find('div', attrs = {'data-foo': 'value'})

# example4()

def example5():
    '''
    class这个tag属性比较特殊，由于他和python中的class关键字冲突，所以
    bs4中用class_来代表class keyword
    '''
    html = '<div class="value" href="/stores/cvs-pharmacy-locations/California">foo!</div>'
    soup = BS4(html)
    print '==========原html==========\n%s\n==========以下是输出结果==========' % soup.prettify()
    print soup.find('div',
                    class_ = re.compile(r'value'),
                    href = re.compile(r'/stores/cvs-pharmacy-locations/[\s\S]*') )

# example5()

def example6():
    '''recursive arugment
    If you call mytag.find_all(), Beautiful Soup will examine all the descendants of 
    mytag: its children, its children’s children, and so on. If you only want Beautiful 
    Soup to consider direct children, you can pass in recursive=False. See the difference here:
    '''
    html = '<li>fruit<li>apple</li><li>orange</li></li><li>bird<li>eagle</li><li>hawk</li></li>'
    soup = BS4(html)
    print '===========Pretty print=================='
    print soup.prettify()
    print '===========recursive = True 找所有的子标签 =================='
    print soup.find_all('li') # 找到所有的li标签
    print '===========recursive = False 只找第一级子标签==========='
    print soup.find_all('li', recursive = False) # 只找第一级的li子标签
        
# example6()

def example7():
    
    with open('test_html.html', 'rb') as f:
        html = f.read()
        
    soup = BS4(html)
    ## access children tag
#     print soup.html.head 
    
    ## access tag attribute "class"
    tag = soup.find('p')
#     print tag
#     print tag['class']
    
    ## access tag all attributes
#     print tag.attrs
    
    ## access tag all childrens
#     print tag.contents
example7()
