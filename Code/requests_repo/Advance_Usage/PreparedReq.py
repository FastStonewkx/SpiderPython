from requests import Request, Session

url = 'http://httpbin.org/post'
data = {
    'name': 'germey'
}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}

s = Session()
req = Request('POST', url, data=data, headers=headers)
propped = s.prepare_request(req)
r = s.send(propped)
print(r.text)