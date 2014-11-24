##coding=utf8
##reference = http://docs.python-requests.org/en/latest/user/quickstart/
import requests

r = requests.post("http://httpbin.org/post")
r = requests.get('https://github.com/timeline.json')
print r.text
print r.encoding