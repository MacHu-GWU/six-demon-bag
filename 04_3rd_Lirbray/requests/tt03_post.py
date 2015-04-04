##encoding=UTF-8

import requests

# url = "http://www.airnow.gov/index.cfm?action=airnow.local_state"
# r = requests.post(url, data={"stateid":"21"})
# print(r.text)

url = "http://aqarmap.com/eg/en/alexandria"
r = requests.post(url, data={
                             
                             "data[Listing][city]": "alexandria",
                             "data[Listing][ng_neighborhood]": 33,
                             "data[Listing][category]": "FOR_SALE",
                             })
print(r.text)