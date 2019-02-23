# import urllib.request
#
# response = urllib.request.urlopen('http://httpbin.org/get', timeout=0)
# print(response.read())

# 这里故意设置超时时间为0秒，和原书有区别，因为不到一秒就响应了，错误原因：超时  😰

# 通过设置超时时间来控制页面长时间未响应，跳过它的抓取，使用 try except

import socket
import urllib.request
import urllib.error

try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')

# TIME OUT 爬虫中处理超时的常用手段