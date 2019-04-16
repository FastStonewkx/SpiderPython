import re
html = open("example.html", 'r', encoding='UTF-8')
try:
    file_text = html.read()
    # print(file_text)
    result = re.sub('<a.*?>|</a>', '', file_text)
    print(result)
    results = re.findall('<li.*?>(.*?)</li>', result, re.S)
    for res in results:
        print(res.strip())

        """
        先将a节点去掉，然后使用findall()提取就好了
        """
finally:
    html.close()