import urllib.parse
import urllib.request

data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf-8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read())

# 这里的请求站点是httpbin.org,他可以提供HTTP请求测试 这里测试POST请求

'''
{\n  "args": {}, \n  "data": "", \n  "files": {}, \n  "form": {\n    "word": "hello"\n  }, \n  "headers": {\n    "Accept-Encoding": "identity", \n    "Content-Length": "10", \n    "Content-Type": "application/x-www-form-urlencoded", \n    "Host": "httpbin.org", \n    "User-Agent": "Python-urllib/3.7"\n  }, \n  "json": null, \n  "origin": "123.139.41.225, 123.139.41.225", \n  "url": "https://httpbin.org/post"\n}
'''