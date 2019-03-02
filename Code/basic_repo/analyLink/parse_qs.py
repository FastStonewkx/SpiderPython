from urllib.parse import parse_qs

query = 'name=germy&age=22'
print(parse_qs(query))