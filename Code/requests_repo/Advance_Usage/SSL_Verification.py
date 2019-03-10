
# 你的连接不是私密连接
import requests

response = requests.get('https://moyuv5.com/')
print(response.status_code)

# ssl.CertificateError: hostname 'moyuv5.com' doesn't match either of 'seavilia.com',

# 12306官方的证书似乎已经添加到CA机构的信任库中了，囧