import urllib.request

response = urllib.request.urlopen('https://www.python.org')
print(response.status) # 状态码
print(response.getheaders())  # 响应的头消息
print(response.getheader('Server'))   # 传递一个参数server值，这里结果是ngixn，说明python官网的服务器是用nginx搭建的

