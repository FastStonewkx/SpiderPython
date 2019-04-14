import re

html = open("example.html", 'r', encoding='UTF-8')
try:
    file_text = html.read()
    # print(file_text)
    result = re.findall('<li.*?href="(.*?)".*?singler="(.*?)">(.*?)</a>', file_text, re.S)
    print(result)
    print(type(result))
    for res in result:
        print(res)
        print(res[0],res[1],res[2])
finally:
    html.close()

