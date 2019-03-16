# OAuth
import requests
from requests_oauthlib import OAuth1

url = 'https://api.twitter.com/1.1/account/virify_verify_credentials.json'
auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET','USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
requests.get(url, auth=auth)
# 前提你可以翻墙并且有自己的twitter账号
