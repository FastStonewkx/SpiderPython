
# HTTPError是URLError的子类，专门用来处理HTTP请求错误
# code
# reason
# header

from urllib import request,error
try:
    response = request.urlopen('https://cuiqingcai.com/index.htm')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
# 继续
except error.URLError as e:
    print(e.reason)
else:
    print('Request Successfully')
# 这样就可以先捕获HTTPError，获取错误状态码、原因、headers等信息。如果不是HTTPError异常，就会捕获URLError异常