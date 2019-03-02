from urllib.parse import urlsplit

result = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(result)
#返回结果是一个SplitResult，其实是一个远足类型，可以用属性获取，也可以用索引获取

print(result.scheme, result[0])