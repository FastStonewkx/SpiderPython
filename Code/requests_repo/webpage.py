import requests
import re

headers = {
    'User-Agent': 'Molilla/5.0 (Macintosh; Intel Mac OS 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
r = requests.get("https://www.zhihu.com/explore", headers=headers)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
titles = re.findall(pattern, r.text)
print(titles)
# User-Agent 浏览器的标志信息，如果不加这个，知乎会禁止抓取
# 知乎的一个页面，返回的是一个html文档