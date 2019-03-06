import requests

r = requests.get('https://www.zhihu.com/explore')
print(r.text) # An internal  server error occured

#  如果加上headers并加上User-Agent信息，就OK
print('================================================')
headers =  {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36'}
r = requests.get('https://www.zhihu.com/explore',headers  = headers)
print(r.text)
