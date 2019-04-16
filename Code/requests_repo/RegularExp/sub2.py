import re
html = open("example.html", 'r', encoding='UTF-8')
try:
    file_text = html.read()
    # print(file_text)
    result = re.findall('<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>', file_text, re.S)
    for res in result:
        print(res[1])
finally:
    html.close()