import re

content = 'Hello 123 4567 World_This is a Regex demo'
result = re.match('^Hello.*demo', content)
print(result)
print(result.group())
print(result.span())

"""
<_sre.SRE_Match object; span=(0, 41), match='Hello 123 4567 World_This is a Regex demo'>
Hello 123 4567 World_This is a Regex demo
(0, 41)
"""