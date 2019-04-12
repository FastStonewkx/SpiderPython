import re

content = '''Hello 1234567 World_This 
is a Regex Demo'''
try:
    result = re.match('^He.*?(\d+).*?Demo$', content)
    print(result.group(1)) # 因为有换行符，所以匹配失败
except AttributeError:
    print("=============================================")
    result = re.match('^He.*?(\d+).*?Demo$', content,re.S) # 添加修饰符re.S. 正常匹配
    print(result.group(1))