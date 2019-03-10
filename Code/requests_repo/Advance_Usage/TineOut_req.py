import requests

r = requests.get('https://www.taobao.com', timeout =1) # 设置超时时间为1s，若1s内没有响应，抛出异常
print(r.status_code)

r = requests.get('https://www.taobao.com', timeout =(5, 11, 30)) # 连接 读取  时间总和

r = requests.get('https://www.taobao.com', timeout = None) # 设置永远不会返回超时错误

r = requests.get('https://www.taobao.com')  # 同上句