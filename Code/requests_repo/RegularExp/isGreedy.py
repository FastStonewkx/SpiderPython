import re

content= 'Hello 1234567 World_This is a Regex demo'
result = re.match('^He.*(\d+).*demo$', content)
print(result)
print(result.group(1))


print('=============================================')

result = re.match('^He.*?(\d+).*demo$', content)
print(result)
print(result.group(1))

# 字符传中间尽可能使用非贪婪匹配
print("注意***************************注意")
content = 'http://weibo.com/comment/kEraCN'
result1=re.match('http.*?comment/(.*?)',content)
result2=re.match('http.*?comment/(.*)',content)

print('result1', result1.group(1))
print('result', result2.group(1))

#匹配的结果在字符串结尾，.*?就有可能匹配不到任何内容了。