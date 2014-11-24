import urllib2
import bs4

def url_to_soup(url, timeout = 6):
    ''' Function: given a url, generate BeautifulSoup object
    '''
    ''' === disguise as browser === '''
    req = urllib2.Request(url,headers={'User-Agent':'Magic Browser'})
    ''' === crawl it !=== '''
    try: ## can avoid to raise an error
        content = urllib2.urlopen(req,timeout).read() ## response is a string
        print 'successfully read html\n'
    except:
        print 'time out!', url
        return 'NA'
    return bs4.BeautifulSoup(content)

''' ======================= extract info by tag =========================== '''
''' === find all tag="tag", and loop in results=== '''
def demo_findAllTag():
    url = 'http://www.javlibrary.com/cn/?v=javlijq72u'
    soup = url_to_soup(url)
    result = soup.find_all('td')
    for tag in result:
        print tag.string ## type = <class 'bs4.element.Tag'>
        print '================================================'
    print len(result), 'results has been found.'
    return None

# demo_findAllTag()

''' === tag object === '''
# tag has two very useful attributes
# tag.name
# tag.attrs
def demo_tagObject():
    url = 'http://news.cnet.com/8301-1035_3-57620089-94/medium-plans-to-release-ios-reading-app-next-week/'
    soup = url_to_soup(url)
    tag = soup.meta
    # example: tag itself = '<meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>'
    print 'tag itself = ',tag ## tag it self
    print 'tag name = ',tag.name ## tag name
    print 'tag attrs dict = ',tag.attrs ## tag attributes
    print 'tag string = ',tag.string ## tag string
    ## how to call tag attributes?
    print tag['content']

# demo_tagObject()

''' tag tree - find all children.  syntax: tag.contents'''
def demo_tagChildren():
    url = 'http://www.javlibrary.com/cn/?v=javlijq72u'
    soup = url_to_soup(url)
    result = soup.find_all('tr')
    for tag in result:
        print tag.contents ## type = <class 'bs4.element.Tag'>
        print '================================================'
    print len(result), 'results has been found.'
    
# demo_tagChildren()
