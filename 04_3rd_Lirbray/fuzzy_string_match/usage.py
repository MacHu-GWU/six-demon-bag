##encoding=utf8

"""
fuzzywuzzy: Fuzzy string matching in python
    download = https://pypi.python.org/pypi/fuzzywuzzy

python-Levenshtein: optional, provides a 4-10x speedup in String Matching)
    download = http://www.lfd.uci.edu/~gohlke/pythonlibs/#python-levenshtein
    
在python3中，由于bytes的问题以及levenshtein的作者没有完全解决这一兼容性问题，所以导致
python3中一旦levenshtein包存在，就无法计算除了ratio以外的所有匹配模式。
所以推荐
"""

from __future__ import print_function
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def ratio_and_partial_ratio():
    print( fuzz.ratio("this is a test", "this is a test!") )
    print( fuzz.partial_ratio("this is a test", "this is a test! first is partial of second") )

ratio_and_partial_ratio()

def token_sort_ratio():
    """token_sort_ratio是指讲两个字符串中的词排序之后，再进行比较
    这样可以排除掉词语顺序的因素
    """
    print( fuzz.ratio("fuzzy wuzzy was a bear", "wuzzy fuzzy was a bear") )
    print( fuzz.token_sort_ratio("fuzzy wuzzy was a bear", "wuzzy fuzzy was a bear") )

# token_sort_ratio()

def token_set_ratio():
    """token_set_ratio是指将两个字符串看作两个词语的集合，如果前者是后者的子集，那么后者就能被匹配上
    """
    print( fuzz.token_sort_ratio("fuzzy was a bear", "fuzzy fuzzy was a bear") )
    print( fuzz.token_set_ratio("fuzzy was a bear", "fuzzy fuzzy was a bear") )

# token_set_ratio()

def select_best_match():
    """process.extract 默认采用的是 WRatio, 一种优化后的智能选择最佳ratio的匹配算法
    """
    choices = ["Atlanta Falcons", "New York Jets", "New York Giants", "Dallas Cowboys"]
    print( process.extract("new york jets", choices, limit=2) )
    print( process.extractOne("cowboys", choices) )
    
# select_best_match()