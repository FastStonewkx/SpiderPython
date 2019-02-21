import urllib.request
# python官网的简单爬取
response = urllib.request.urlopen('http://www.python.org')
print(response.read().decode('utf-8'))
print(type(response))
"""
urlopen() urllib.request模块提供了最基本的构造http请求的方法
"""