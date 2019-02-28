import http.cookiejar, urllib.request

# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# open = urllib.request.build_opener(handler)
# response = open.open('http://www.baidu.com')
# for item in cookie:
#     print(item.name+"="+item.value)

# 这里输出了每条Cookie的名称和值

# 下面将cookie输出成文件格式

filename1 = 'cookie1.txt'
filename2 = 'cookie2.txt'
cookie = http.cookiejar.MozillaCookieJar(filename1)
cookie = http.cookiejar.LWPCookieJar(filename2)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)

"""
以上代码会生成一个cookies.txt/lwp文件

CookieJar需要转换成MozillaCookieJar，它在生成文件时会用到，是CookieJar的子类，可以用来处理Cookie和文件相关的事件，
比如读取和保存Cookie、将Cookie保存成Mozilla型浏览器的Cookie格式
"""

# 生成了文件后，如何读取并利用

print(response.read().decode('utf-8'))
