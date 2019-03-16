import re

content = 'Hello 123 4567 World_This is a Reqex Demo'
print(len(content))
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
print(result)
print(result.group())
print(result.span())
# 😓

"""
Hello\s\d\d\d\s\d{4}\s\w{10}
^匹配的是字符串的开头，也就是以Hello开头；
然后匹配\s匹配空白字符串，用来匹配目标字符串的空格；
\d匹配数字，三个\d表示123；然后再写一个\s匹配空格；
后面依次有4567，但是比较繁琐，这里用\d{4}表示前面的规则4次
\w{10}表示10个字母和下划线
这里并没有匹配完，但是依旧可以，就是结果比较短。恰好是正则表达式规则所匹配的内容
"""

