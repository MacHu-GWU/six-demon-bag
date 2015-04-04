#Install Extension
------

安装python第三方扩展通常有以下几种方式 ([Official Documentaion](https://docs.python.org/2/install/))

- source code build and install 从源码包自己编译后安装
- pip install 用pip包管理工具安装
- easy\_install 用easy\_install包管理工具安装
- compiled binary release install 双击编译好的exe可执行文件安装
- wheel 不推荐
- python egg 不推荐

公认的最优雅的方法是**pip安装和源码安装**两种。 这两种方法兼容Windows, MacOS, Linux, Unix系统。 最偷懒的方法当然是用别人编译好的exe文件双击, 然后一路next安装。 但是只能在Windows系统上这么做, 而且要有好心人预先编译好了。

由于我们通常说的Python是Python在C语言上的实现, 也就是cPython。 而第三方扩展从实现上可以大致分为两类:

1. 纯Python实现
2. 包含有C语言实现的部分, 通常是对性能要求苛刻的部分。

第一类扩张包由于所有的代码都是建立在纯python上的。 就好象自己写了一小段helloworld.py的文件, 就可以作为一个安装包。

第二类由于部分代码是用的C语言实现, 所以需要用C++编译器将其编译成.pyc文件, Python才能够正确的调用其中的功能。 在Windows系统下通常使用微软的Visual Studio C++编译器。 而在Linux, Unix, Mac OS中内置默认的是开源的[GCC编译器](https://gcc.gnu.org/)。

下面我们就来介绍一下在各个平台上最主流的安装Python扩展包的方式。

##Windows OS

###1. source code build and install

我们以pypi上排名第五的http库requests为例进行讲解。 [源码github链接戳我](https://github.com/kennethreitz/requests)

一个典型的源码包release都有一个setup.py文件。 我们要做的就是讲源码包下载下来, 然后解压到任意英文目录, 例如:

	C:\download\requests

然后我们打开windows命令行控制台(开始菜单, 输入command prompt或者cmd, 回车)。 CD到解压的目录:

	cd C:\download\requests

然后依次执行如下命令:
	
	python setup.py build # 将.py文件编译成
	python setup.py setup # 将编译好的文件安装到Python27\Lib\site-packages目录下

然后我们就可以在python中调用我们刚才安装好的包了

	import requests

####注意

这个方法要求用户已经安装了这个包所依赖的其他包。 例如pandas依赖于numpy, 你如果不安装numpy, 这个方法是无法成功安装pandas的。


###2. pip install

pip是python社区最有名的包管理工具。 pip的优点是能够智能的选择当前最新最稳定的安装包进行智能下载, 安装。 也可以由用户自由指定版本进行安装。 还可以智能的找到所依赖的其他安装包并自动下载安装补全。 当然包的卸载也不在话下。

[官方网页](https://pypi.python.org/pypi/pip/)

[官方文档](https://pip.pypa.io/en/latest/quickstart.html)

在用pip安装其他包之前, 我们首先要安装pip本身。 我们可以用之前讲过的source code build and install方法安装。 也可以采用下面的简洁方法:

到这里下载[get-pip.py](https://bootstrap.pypa.io/get-pip.py)文件。
然后用对应的python版本运行get-pip.py文件。 比如你用python27运行的, 那么你就为python27安装了pip, 如果是用python33运行的, 那么你就为python33安装了pip。 安装完之后, pip会在对应的Python版本目录下的scripts目录生成一个pip.exe的可执行文件。 例如:

	C:\Python27\Scripts\pip.exe

之后无论你想安装什么扩展包, 只要在命令行界面, CD到pip.exe所在目录, 然后执行如下命令:

	cd C:\Python27\Scripts
	pip install requests

pip就会自动下载最新最稳定的版本, 以及下载所依赖的组件。
除了最基本的pip install命令, pip还有如下[常用命令](https://pip.pypa.io/en/latest/user_guide.html#installing-packages):
	
	pip install requests                    # latest version
	pip install requests==2.4.1             # specific version
	pip install 'requests>=2.3.2'           # minimum version
	pip uninstall requests

####[CN]在Windows下安装C++编译器

以上两种方法在windows环境下安装需要C++编译器的包时通常会出现如下错误:

	Unable to find vcvarsall.bat

解决方法如下:
	
- Windows环境下[下载](http://www.microsoft.com/en-us/download/confirmation.aspx?id=44266)微软的Visual C++编译器
- Linux, Unix, MacOS一般自带GCC编译器, 万一没有, 可以到这里[下载](https://gcc.gnu.org/)一个。

双击安装之后, 我们要教会我们的python如何调用我们刚刚安装的C++编译器。 Python寻找vcvarsall.bat的原理是这样的。 在需要C++编译器时, python会到这个目录下运行的msvc9compiler.py文件中def find_vcvarsall()函数。

	C:\Python27\Lib\distutils\msvc9compiler.py

然后我们可以将函数主体全部注释掉。 不用担心, 里面的内容是通过读取windows注册表来尝试寻找vcvarsall.bat, 我们不再需要它。 最后将主体内容手动替换成我们刚才安装的vcvalsall.bat的绝对路径。 你可以通过在C盘下搜索vcvalsall.bat文件来得到这个路径。 具体代码如下:

	def find_vcvarsall(version):
	    """Find the vcvarsall.bat file
	
	    At first it tries to find the productdir of VS 2008 in the registry. If
	    that fails it falls back to the VS90COMNTOOLS env var.
	    """
		return r"C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\vcvarsall.bat"
	    # 或者是
		# C:\Users\username\AppData\Local\Programs\Common\Microsoft\Visual C++ for Python\9.0

在这之后, 你就可以用之前的两种方法安装需要C++编译器的扩展包了。

####[EN]Install package requires C++ compiler
Some 3rd party extension requires C++ compiler for installation. For example, numpy. Because
the performance can be greatly improved with C implementation. If you install this type of extension
using: pip install packagea_name, or using: python setup.py build, python setup.py install, and
unfortunately you don't have C++ compiler, then python gonna raise this error:

    Unable to find vcvarsall.bat
    
There are two solutions:

1. download compiled windows binary release from http://www.lfd.uci.edu/~gohlke/pythonlibs/,
most of popular python extension that need C++ compiler can be found here.

2. download [Microsoft Visual C++ Compiler for Python 2.7](http://www.microsoft.com/en-us/download/details.aspx?id=44266) (also works for Python 3). Edit the def find_vcvarsall() function in C:\Python27\Lib\distutils\msvc9compiler.py, commend the body of the function, replace with:

	def find_vcvarsall(version):
	    """Find the vcvarsall.bat file
	
	    At first it tries to find the productdir of VS 2008 in the registry. If
	    that fails it falls back to the VS90COMNTOOLS env var.
	    """
		return r"C:\Users\username\AppData\Local\Programs\Common\Microsoft\Visual C++ for Python\9.0\vcvarsall.bat"

	now python is able to find the vcvarsall.bat file. So you can install extension as usually now.

###3. compiled binary release install

在Windows操作系统中, 我们安装应用程序通常都是通过执行install.exe文件来安装的。 Python中自带了一个模组可以将自己的安装包制作成双击安装的exe文件。 当然前提是包作者不懒, 而且恰巧是在Windows上开发的, 而且恰巧也有心将其制作成了exe然后post在了网上。 不过许多主流的需要C++编译器的扩展包都有编译后的版本, 可以在[这里下载](http://www.lfd.uci.edu/~gohlke/pythonlibs/)到。 比如鼎鼎有名的Scipy-Stack, Numpy, MySqlDB, Psycopg2。 只要根据你的python版本(python27, python33)和操作系统版本(x86, x64)下载正确的安装文件双击一路next安装即可。

##Mac OS

ToDo...

##Linux OS

ToDo...