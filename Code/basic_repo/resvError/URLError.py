from urllib import request, error

try:
    response = request.urlopen('https://cuiqingcai.com/index.htm')  # 这里的错误应该是服务器返回的，由函数捕获的。所以不要乱写地址
except error.URLError as e:
    print(e.reason)
