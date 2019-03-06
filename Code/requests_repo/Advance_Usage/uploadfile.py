import requests

files = {'file': open('favicon.ico', 'rb')}
r = requests.post("http://httpbin.org/post", files = files )
print(r.text)

# 网站会返回响应，里面包含了files字段，form字段是空的。证明文件上传部分会单独有一个files字段来标识

