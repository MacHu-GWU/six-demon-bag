##encoding=utf8
from __future__ import print_function
from HSH.LinearSpider.crawler import Crawler
from HSH.Data.js import load_js
from HSH.Misc.logger import Log
from bs4 import BeautifulSoup as BS4
import re

def gen_url(address, zipcode):
    base = "http://www.zillow.com/homes/"
    return base + address.replace(" ", "-") + "-" + zipcode + "_rb/"

def property_info(address, zipcode):
    url = gen_url(address, zipcode)
    spider = Crawler()
    html = spider.html(url)
    if html:
        try:
            soup = BS4(html)
            dt = soup.find("dt", class_ ="property-data")
            info = dt.text.strip()
            span = soup.find("span", itemprop = "addressLocality")
            city = span.text.strip()
            span = soup.find("span", itemprop = "addressRegion")
            state = span.text.strip()
            return address, city, state, zipcode, info
        except:
            log.write("Failed to analysis address = %s, zipcode = %s" % (address, zipcode), 
                      "Failed Extraction")
            return None
    else:
        log.write("%s Failed to get http request" % url, "Http Error")

log = Log()

pdr14 = load_js("pdr14.json")    
for id, data in pdr14.items():
    address, zipcode = data["address"], data["zipcode"]
    result = property_info(address, zipcode)
    if result:
        print("=========================")
        print("id = %s\naddress = %s\nzipcode = %s\nresult = %s\n" % (id, address, zipcode, result))

# result = property_info("18727 DUKE LAKE DR", "77388")
# print(result)