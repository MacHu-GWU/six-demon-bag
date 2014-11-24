[主题] 如何开发一个自己的python包?

在这个例子里，我们使用mathtools这个演示包作为例子。mathtools有两个简单功能: 加法和乘法。这两个功能都是作为子包而存在的。下面我们用实际例子来解释一个可用的python包的结构。

mathtools/ ## 主包名
	__init__.py ## __init__.py 文件标识了本文件夹应该被当做一个包来对待
	calculator.py ## Calculator 类
	chengfa/ ## 子包1名字
		__init__.py ## __init__.py 文件标识了本文件夹应该被当做一个包来对待
		times_X.py ## time_X 函数包，里面都是函数，没有类
	jiafa/ ## 子包2名字
		__init__.py ## __init__.py 文件标识了本文件夹应该被当做一个包来对待
		plus_X.py ## plus_X 函数包，里面都是函数，没有类

我们建立了一个测试脚本 test_mathtools.py。首先我们要保证包整个文件夹被放在 site-packages 或者和测试脚本同一目录下。这样在import的时候python才能够找到我们编写的包。

在test_mathtools.py文件中的脚本是这样的

from mathtools.calculator import calculator
a = calculator()
a.run('times10', 5)
a.run('times100', 5)
a.run('plus1', 5)
a.run('plus2', 5)

我们来看看每一行发生了什么。
第一行 from mathtools.calculator import calculator
	我们导入了calculator这个类. 注意，当calculator这个类被导入时，calculator的前两行做了这样的事:
		from .chengfa.times_X import *
		from .jiafa.plus_X import *
	
	这是的calculator这个类文件，导入了chengfa子包下的times_X函数库中的所有函数. (注意！这里是导入了函数文件中的所有函数而不是导入了包中的所有类。到最后我们会说说这有什么不同。)
	
	可能大家会注意到，包前面的.是什么意思呢？.的是指回到上一级目录的意思。也就是说一个点就是跳回一级目录。这里.chengfa 是指首先跳回到calculator.py的上级目录mathtools中，然后在mathtools中找一个叫chengfa的包。然后再chengfa的包中找一个叫times_X的类或函数库。如果我们没有这个点，calculator.py是无法顺利找到chengfa和jiafa这两个子包的

第三-六行基本类似，我们以第三行为例: a.run('times10', 5)
	因为a是mathtools.calculator.Calculator类, 其中run方法是这么定义的
    def run(self, cmd, num):
        print(eval(cmd + '(%s)' % num))
    
    于是 a.run('times10', 5) 等效于:
    	print eval(  'time10' + '(5)'  )
    等效于:
    	print eval('time10(5)')
	等效于:
		print time10(5)
		
	time10这个函数已经在from .chengfa.times_X import *中被导入了。根据下面的定义， time10(5) 当然是返回 50。
	def times10(num):
	    return num * 10

我们在很多例子里，能够看到 from xxxpackage import *。这和我们之前 from .chengfa.times_X import * 是有很大区别的。前者是从一个包里导入所有的类或函数的文件。后者是从一个文件里导入所有的类或者函数。前者是导入文件，后者是导入文件里面的代码。而前者的*所代表的那个"全部"，是要求被定义的。

比如我们如果在把test_mathtools.py 的头两行改成:

from mathtools import *
a = calculator.Calculator()

那么编译器会报错。这是因为 * 中没有定义 calculator.py这个文件。定义 from xxxpackage import * 行为的方法是，打开包对应的__init__.py文件并在里面加入一行:
__all__ = ["calculator"]

于是我们import * 的时候就会自动导入calculator了

参考资料:
	python官方文档: https://docs.python.org/2/tutorial/modules.html#packages