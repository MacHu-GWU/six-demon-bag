''' PyGeocoder Tutorial
By.Sanhe 3-16-2014
Python2.7
Encode: UTF-8
'''
''' ================ What is pygeocoder for ==================
it's a powerful Google Map API
''' 
''' ================ Installation pygeocoder in Windows 32 ==================
1. google: python pip (py package manager tools), install it
2. open cmd in windows, 
3. cd\
4. cd python27\scripts
5. pip install pygeocoder --- DONE!
'''
from pygeocoder import Geocoder
''' ================= Basic Function =================== '''
# address = 'washington,950 25th ST'
# address = '1400 S Joyce St, Arlington, VA, 22202'
''' address to everything '''
# result = Geocoder.geocode(address)
# print result ## print Address
# print result.coordinates ## Longitude and Latitude, returns the decimal format coordinates
# print result.country ## Country
# print result.postal_code ## Zip code
# print result.count ## how many result you got, you can try '1400 S Joyce St'

''' coordinates to address '''    
# result = Geocoder.reverse_geocode(38.86141, -77.065015)
# print(result)
''' verify an address '''
# print Geocoder.geocode(address).valid_address
''''''

''' === given a degree coordinate: 38.862869, -77.064655, return 38.51'46.32", -78.56'7.24" === '''
def cood_to_degree(longitude,latitude):
    '''
    Input:
        degree coordinate in decimal: 38.862869, -77.064655
    Output:
        return 38.51'46.32", -78.56'7.24" in radian
    '''
    long_sign = int(abs(longitude)/longitude)
    lati_sign = int(abs(longitude)/longitude)
    longitude = abs(longitude)
    lati_sign = abs(lati_sign)
    v1 = int(longitude//1)
    s = (longitude - v1)*3600
    v2 = int(s//60)
    v3 = str(s%60)
    head, tail = v3.split('.')
    v3 = head+'.'+tail[0:2]
    longitude = str(v1)+'.'+str(v2)+'\''+v3+'\"'
    if long_sign < 0:
        longitude = '-' + longitude
    v1 = int(latitude//1)
    s = (latitude - v1)*3600
    v2 = int(s//60)
    v3 = str(s%60)
    head, tail = v3.split('.')
    v3 = head+'.'+tail[0:2]
    latitude = str(v1)+'.'+str(v2)+'\''+v3+'\"'
    if lati_sign < 0:
        latitude = '-' + latitude
    return longitude,latitude

''' === given two address, find the distance === '''
import math
def degree_to_rad(degree):
    ''' input: 90 degree, return: 0.5 * pi '''
    return math.pi * degree / 180

def dist((lotA,latA),(lotB,latB)): ## require: degree_to_rad
    ''' given two (longitude,latitude) pairs, return distance in mile. '''
    lotA = degree_to_rad(lotA)
    latA = degree_to_rad(latA)
    lotB = degree_to_rad(lotB)
    latB = degree_to_rad(latB)
    R = 6356.755 * 0.621371192
    C = math.sin(latA)*math.sin(latB)*math.cos(lotA-lotB) + math.cos(latA)*math.cos(latB)
    Distance = R*math.acos(C)
    return Distance

def dist_address(addr1, addr2):
    ''' given two address, return distance in miles '''
    result1 = Geocoder.geocode(addr1)
    result2 = Geocoder.geocode(addr2)
    if (result1.count==1)&(result2.count==1): ## if only one valid address
        return dist(result1.coordinates, result2.coordinates) ## dist(coordinate1, coordinate2)
    else:
        print 'Error'
        return None
    
''' ============== test ================ '''
addr1 = '1400 S Joyce St, Arlington, VA, 22202'
addr2 = '2250 Corporate Park Dr, Herdon, VA, 20171'
print dist_address(addr1, addr2)

 

