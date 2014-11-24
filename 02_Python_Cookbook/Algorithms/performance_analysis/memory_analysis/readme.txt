内存测量器
	https://pypi.python.org/pypi/memory_profiler
	为保证性能所依赖的包
		https://pypi.python.org/pypi/psutil

	版本支持2.7, 3.3

用法1
	在要被测量的函数前加上装饰器@profile
	然后在cmd命令行中输入：
		python -m memory_profiler myscript.py
		即可看到程序运行时的内存消耗

用法2
	在程序最前面加上
	from memory_profiler import profile
	然后直接运行该脚本即可