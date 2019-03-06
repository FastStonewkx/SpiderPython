import requests

r = requests.get('https://github.com/favicon.ico')
print(r.text)
print(r.content)

# 这个是站点图标，浏览器每个页面显示的小图标

# 前两行显示r.text（这里乱码），后两行显示content（bytes类型的数据）

with open('favicon.ico', 'wb') as  f:
    f.write(r.content)

# 将提取到的图片保存下来


