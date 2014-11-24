##encoding=utf8
##version =py27
##author  =sanhe
##date    =2014-09-02
# ==================================================================================
# official website = https://github.com/geopy/geopy
# geopy 是一个汇聚了非常多个geocoding service engine的python第三方扩展库
# 比如，geopy支持:
#     googlev3
#     bing
#     baidu
#     arcgis等
#     
# 要使用geopy，首先要在你要使用的engine的官方网站获得api key。
#     例如googlev3的在 https://developers.google.com/maps/documentation/geocoding/#BYB
#     注册完之后，在site-packages/geopy/geocoders/googlev3.py中查看类里面的__init__时所设置
#     的api key。以后创建类的时候，使用：
#         googlev3(apikey = 'xxxxxx',
#                  secret = 'xxxxxx')
#         
# 如果你得api key的请求次数限制不够用，那么可以多申请几个不同的engine，然后动态的
# 调用engine，这样可以一定程度上缓解api key不够用得问题。
#
# ==================================================================================
# geopy的特色是，在geocode engine之外，有一些包可以用来进行地理数据处理，而不需要用到api requests

import pickle

def example1():
    '''Simple Geocoding
    '''
    from geopy.geocoders import Nominatim # Nominatim 替换成你要用到的引擎
    engine = Nominatim()
    loc = engine.geocode('1400 S Joyce St Arlington, VA 22202')
    print loc.address
    
# example1()

def example2():
    '''GoogleV3 API 使用说明 2014-09-04
    官方介绍 = https://developers.google.com/maps/documentation/geocoding/
    用户控制台 = https://code.google.com/apis/console/
    1. login your google account & google developer account
    2. Go to google developer console, if there's no project, create one with any name.
    3. Go "Service" It's on your left hand panel.
    4. Activate "Geocoding API"
    5. Go "API Access" it's on your left hand panel.
    6. Scroll down, see "Simple API access", click "Create new server key", and leave it empty
        (It allows all ip access)
    7. Then API key is there
    
    注：普通用户只要API key就可以了，而bussiness用户需要Client_id和Secret_key
    '''
    from geopy.geocoders import GoogleV3
    from pprint import pprint as ppt
    ## 把查询到得结果保存到本地，节约测试时用得API access limit
    try:
        LOC = pickle.load(open('location.p', 'rb'))
    except:
        print 'Warning! Calling Google Geocoding API'
        engine = GoogleV3('AIzaSyBq-NZmY8G6Tm7Fzpx4dAR55Uk0n-5AIDQ')
        location = engine.geocode("238 MCMECHEN STREET BALTIMORE MD, 21217")
        LOC = location.raw # <=== 建议把这个保存了
    pickle.dump(LOC.raw, open('location.p', 'wb'))
    ppt( LOC ) 
    
# example2()

def example3():
    """Reverse Geocoding
    """
    from geopy.geocoders import GoogleV3
    from pprint import pprint as ppt
    ## 把查询到得结果保存到本地，节约测试时用得API access limit
    try:
        LOC = pickle.load(open('location.p', 'rb'))
    except:
        print 'Warning! Calling Google Geocoding API'
        engine = GoogleV3('AIzaSyAuzs8xdbysdYZO1wNV3vVw1AdzbL_Dnpk')
        location = engine.reverse("44.44, -104.51")[0] # <== 根据坐标反向查询
        print location, dir(location), location.raw
        LOC = location.raw # <=== 建议把这个保存了
    pickle.dump(LOC, open('location.p', 'wb'))
    ppt( LOC )
    
example3()