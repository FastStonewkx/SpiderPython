import requests

data = {'name':'gerney','age':'23'}
r = requests.post("http://httpbin.org/post", data=data)
print(r.text)

