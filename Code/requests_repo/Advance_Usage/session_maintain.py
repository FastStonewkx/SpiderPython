import requests
"""
希望设置一个cookie，名称叫做number，内容是123456789
"""
requests.get('http://httpbin.org/cookies/set/number/123456789')
r = requests.get('http://httpbin.org/cookies')
print(r.text)
# 无法设置cookies，说明不同会话cookies不共用

s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)

# 对比一个会话和不同会话的区别

# 同一个会话使用一个cookie