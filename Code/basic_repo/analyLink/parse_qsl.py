from urllib.parse import parse_qsl

query = 'name=gernqy&age=22'
print(parse_qsl(query))