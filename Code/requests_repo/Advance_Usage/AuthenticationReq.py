import requests
from requests.auth import HTTPBasicAuth
r = requests.get('http://localhost:5000', auth=HTTPBasicAuth('username','password'))
r = requests.get('http://localhost:5000', auth=('username','password')) # 含义同上
# 这里的url是需要验证的网站页面，后面的参数是用户名和密码


#还有OAuth认证


