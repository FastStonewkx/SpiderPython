import requests

r = requests.get('https://www.baidu.com/')
r1 = requests.get('http://httpbin.org/get')
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)
print("=======================")
print(r1.text)
"""
{
  "args": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.21.0"
  }, 
  "origin": "1.80.192.25, 1.80.192.25", 
  "url": "https://httpbin.org/get"
}
"""



