import re

context = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
result = re.match('Hello.*?(\d+).*?Demo', context)# match
print(result)
# print(result.group(1))
print("=======================================")
result = re.search('Hello.*?(\d+).*?Demo', context)
print(result)
print(result.group(1))