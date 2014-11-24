##coding=utf8
import nltk
import pprint as ppt

def example1():
    ''' tokenize and tag some text (句子拆分成单词，判断词性)
    '''
    sentence = """At eight o'clock on Thursday morning ... Arthur didn't feel very good."""
    tokens = nltk.word_tokenize(sentence) ## need to download "punkt" - "Punkt Tokenizer Models"
    ppt.pprint( tokens ) ## 句子拆分成单词
    
    tagged = nltk.pos_tag(tokens) ## need to download "maxent_treebank_pos_tag " - "Treebank Part of Speech Tagger (Maxium Entropy)" 9.7MB
    ppt.pprint(tagged )
    
# example1()

def example2():
    '''分句算法
    '''
    ## 第一段有3句话：第一句中，人名中的点没有被判定为句号，成功地正确解析了句子
    ## 第二句是正常的句子，有的时候句子不一定以大写字母开头，下一句就是例子
    ## 第三句中，就没有以大写字母开头
    text1 = \
    """
    Punkt knows that the periods in Mr. Smith and Johann S. 
    Bach do not mark sentence boundaries.
    And sometimes sentences can start with non-capitalized words. 
    i is a good variable name.
    """
    ## 
    text2 = \
    """
    This tokenizer divides a text into a list of sentences by using an 
    unsupervised algorithm to build a model for abbreviation words, 
    collocations, and words that start sentences. It must be trained on 
    a large collection of plaintext in the target language before it can be used.
    """
    # need to download "punkt" and "ptb"
    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle') 
    ppt.pprint(  sent_detector.tokenize(text1.strip())  )
    ppt.pprint(  sent_detector.tokenize(text2.strip())  )
    
# example2()

def example3(word = 'Amevive'):
    '''stem algorithm (词根解析算法)
    '''
    ''' nltk.stem.lancaster module ''' ## 推荐分词算法1
    from nltk.stem.lancaster import LancasterStemmer
    st = LancasterStemmer()
    print st.stem(word)

    ''' nltk.stem.porter module ''' ## 推荐分词算法2
    from nltk.stem.porter import PorterStemmer
    stemmer = PorterStemmer()
    print stemmer.stem(word)
    
    ''' nltk.stem.regexp module ''' ## 正则分词算法
    from nltk.stem import RegexpStemmer
    st = RegexpStemmer('ing$|s$|e$', min=4)
    print st.stem(word)
     
    ''' nltk.stem.snowball module ''' ## 多语言支持分词算法
    from nltk.stem import SnowballStemmer
    stemmer = SnowballStemmer('english') # Choose a language
    print stemmer.stem(word)
    
example3('coming')

# nltk.download()