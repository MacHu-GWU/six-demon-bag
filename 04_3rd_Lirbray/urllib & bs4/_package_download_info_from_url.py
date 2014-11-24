'''
Create by Sanhe, 2014/4/1
Encoded UTF-8
'''
import urllib2
import urllib
import cookielib ## cookies
import bs4 ## beautiful soup

### regular webpage crawl, no need password ###
def url_to_content(url, timeout = 6):
    ''' Function: given a url, return html text
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
    return content

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

### if the webpage you want to crawl need login, use this function ###
def url_to_content_login(url, login_url, acc_pwd, time_out = 10):
    '''
        url: the url you want to crawl
        login_url: the login webpage
        acc_pwd: {key1: value1, key2: value2}
            key1, key2:
            open login_url in chrome => right click => inspect element
            => click the little search icon => move mouse to login bar
            (the place you enter your account and pwd) => check the
            source code, find the key the website use to log in. Different
            website have different keys
            example:
                key1 = 'account', key2 = 'password'
                key1 = 'email', key2 = 'pwd'
            value1: user name, value2: password
    '''
    cj = cookielib.CookieJar() ## add cookies
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj)) ## build opener
    opener.addheaders = [('User-agent','Mozilla/5.0 \
                        (compatible; MSIE 6.0; Windows NT 5.1)')] ## browser header
    data = urllib.urlencode(acc_pwd) ## encode login acc and pwd
    try: ## handle login connection time out
        opener.open(login_url,data,time_out)
    except:
        print 'log in - times out!', login_url
        return 'NA'
    try: ## handle open url connection time out
        content = opener.open(url, None, time_out).read()
    except:
        print 'open url - times out', url
        return 'NA'
    return content

''' example '''
url = 'http://www.archives.com/member/Default.aspx?_act=VitalSearchResult&LastName=Smith&Country=US&State=VA&RecordType=2&DeathYear=2004&DeathYearSpan=10&activityID=b66c79f0-155a-4b2a-97a8-4bc965be3589&pagesize=10&pageNumber=1&pagesizeAP=10&pageNumberAP=1'
login_url = 'http://www.archives.com/member/'
acc_pwd = {'__uid':'sanhe.hu@theeagleforce.net','__pwd':'diablo1987'}

content = url_to_content_login(url, login_url, acc_pwd, 10)
print content