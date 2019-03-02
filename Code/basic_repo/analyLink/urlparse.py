from urllib.parse import urlparse

# scheme://netloc/path?query#fragment
result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result),result)

# scheme
result = urlparse('www.baidu.com/index.html;user?id=5#comment',scheme='https')
print(result)
"""
如果链接没有带协议信息，会将这个参数作为默认的协议，链接如果带了scheme信息，则首先使用链接的schemem信息

"""
result = urlparse('http://www.baidu.com/index.html;user?id=5#comment',scheme='https')

# allow_fragment  这里例子有点看不懂，后面再说

result = urlparse('www.baidu.com/index.html;user?id=5#comment',allow_fragments=False)
print(result)


