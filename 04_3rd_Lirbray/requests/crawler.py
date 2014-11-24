##encoding=utf8
##version =py27
##author=Sanhe
##date  =2014-09-02

'''
This module pack some frequently used operation up in functions
'''
import requests
import sys

reload(sys); # change the system default encoding = utf-8
eval('sys.setdefaultencoding("utf-8")')

class Crawler(object):
    '''Simple http Crawler class
    '''
    def __init__(self):
        self.user_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1',
                            'Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11',
                            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
                            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11, (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11']
        self.auth = None # initialize the self.auth. Then if there's no login, Crawler.html can work in regular mode
    
    def _gen_header(self):
        headers = {'User-Agent': random.choice(self.user_agents),
                   'Accept':'text/html;q=0.9,*/*;q=0.8',
                   'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                   'Accept-Encoding':'gzip',
                   'Connection':'close',
                   'Referer':None}
        return headers
    
    def _login(self, url, payload, timeout = 6):
        '''website log in
        url = login_page_url
        payload = {key1: acc, key2: password}
        '''
        self.auth = requests.Session()
        try:
            self.auth.post(url, data=payload, timeout = timeout)
            print 'successfully loged in to %s' % url
            return True
        except:
            return False
    
    def html(self, url, timeout = 6):
        '''return the html for the url
        '''
        if not self.auth: # if no login needed, then self.c = None, then not self.c = True
            ## regular get html, use requests.get
            try:
                r = requests.get(url, headers = self._gen_header(), timeout = timeout)
                return r.text # if success, return html
            except:
#                 print '%s time out!' % url # <=== ����ʱ����
                return None # if failed, return none
        else: # if login needed, use self.auth.get
            try:
                r = self.auth.get(url, headers = self.headers, timeout = timeout)
                return r.text # if success, return html
            except:
#                 print '%s time out!' % url <=== ����ʱ����
                return None # if failed, return none