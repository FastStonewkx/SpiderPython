import urllib.request
# python官网的简单爬取
response = urllib.request.urlopen('http://www.python.org')
print(response.read().decode('utf-8'))
print(type(response))
"""
 urllib.request模块提供了最基本的构造http请求的方法，用它来弄你一个请求发起过程，还有处理授权验证（authentication）、重定向（redirect）、浏览器Cookie及其他内容。
 
 urlopen() 打开一个网页，并返回页面的所有源代码
"""