##encoding=utf8
##version =python27
##author  =sanhe
##date    =2014-09-02

'''
Useful funcationality repack from geopy
'''
from pygeocoder import Geocoder

def correct(value):
    if value == None:
        return ''
    else:
        return value
    
def GEO(full_address):
    '''
    INPUT:  an address to geocode
    OUTPUT: formatted_address, street_number, route, city, state, zipcode, coordinate
    '''
    results = Geocoder.geocode(full_address)
    if results.valid_address: # if it's a valid address
        if results.count == 1: # only one valid result
            formatted_address = correct(results.formatted_address) # fancy address
            street_number = correct(results.street_number) # street number
            route = correct(results.route) # route name
            city = correct(results.city) # city name
            state = correct(results.state) # state name
            zipcode = correct(results.postal_code) # zipcode
            coordinate = results.coordinates # coordinate
            return formatted_address, street_number, route, city, state, zipcode, coordinate
        else: # result > 1, return none
            print 'More than 1 results been found by search %s' % full_address
            return None, None, None, None, None, None, None # return None, then you know if it works properly
    else:
        print 'ERROR! %s is not a valid address!' % full_address
        return None, None, None, None, None, None, None

def GEO_reverse(coordinate):
    '''Return the first address match the coordinate
    INPUT:  (longitude, latitude)
    OUTPUT: formatted_address, street_number, route, city, state, zipcode, coordinate
    '''
    results = Geocoder.reverse_geocode(coordinate[0], coordinate[1])
    ## we assume the first result is the one we want
    formatted_address = correct(results.formatted_address) # fancy address
    street_number = correct(results.street_number) # street number
    route = correct(results.route) # route name
    city = correct(results.city) # city name
    state = correct(results.state) # state name
    zipcode = correct(results.postal_code) # zipcode
    coordinate = results.coordinates # coordinate
    return formatted_address, street_number, route, city, state, zipcode, coordinate
       
def unit_test():
    addr = '1400 S Joyce St Arlington, VA 22202'
    print GEO(addr)
    coordinate = (38.8616613, -77.0647329)
    print GEO_reverse(coordinate)
    
if __name__ == '__main__':
    unit_test()