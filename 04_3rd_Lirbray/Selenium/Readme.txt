Selenium

Links:
	pypi 下载页 = https://pypi.python.org/pypi/selenium
	官方网站 = http://www.seleniumhq.org/
	精品教程 = http://selenium-python.readthedocs.org/ #<== 推荐阅读的学习网站

介绍:
	Selenium是一个内嵌了firefox, chrome, safari等主流浏览器API的插件。能够完全模仿
	人类的行为去操作浏览器，相当于专为浏览器设计的按键精灵。Selenium主要被用来做自动化
	网站测试，但是由于其直接操作浏览器的特性，所以也可以用来做网页爬虫，爬那些需要很多人
	类进行干预，有许多Javascript的页面。
	
不太兼容Mac OS, 通常在windows下运行

在selenium中选择元素最强大的方法就是用 find_element_by_xpath
	精品例子 = http://selenium-python.readthedocs.org/locating-elements.html#locating-by-xpath
	在精品例子中还有几个链接，更详细的介绍了xpath