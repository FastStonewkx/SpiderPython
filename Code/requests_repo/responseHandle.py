import requests
headers =  {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36'}
r = requests.get('http://www.jianshu.com', headers = headers)
print(type(r.text),r.text)
print(type(r.content), r.content)
print(type(r.status_code), r.status_code)
print(type(r.cookies), r.cookies)
print(type(r.headers), r.headers)
print(type(r.history), r.history)  # 请求历史

exit() if not r.status_code == requests.codes.ok else print('Request Successfully')

