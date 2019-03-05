import requests

data = {
    'name':'germey',
    'age':'22'
}

r = requests.get("http://httpbin.org/get",params=data)
print(r.text)
print(type(r.text))
print(r.json())
print(type(r.json()))# 返回的结果是json格式的字符串转换为字典