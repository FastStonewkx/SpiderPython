import re

html = open("example.html",'r',encoding='UTF-8')
try:
    file_text = html.read()
    print(file_text)

    # https://www.cnblogs.com/mengyu/p/6638975.html
    result = re.search('<li.*?active.*?singler="(.*?)">(.*?)</a>', file_text, re.S)
    """
    首先尝试获取class为active的li节点内部的超链接包含的歌手名和歌名，此时需要提取第三个节点下a节点的singer属性和文本
    
    此时正则表达式以li开头，然后寻找一个标志符active，中间的部分可以用.*?来匹配。接下来，要提取singer这个属性，所以
    还需要写入singer="(.*?)",这里需要提取的部分用小括号括起来，以便用group()方法提取出来，它的两侧边界是双引号。然后
    还需要匹配a节点的文本，其中他的左边界是>,右边界是</a>。然后目标内容依旧用(.*?)
    """
    print(result.group(1), result.group(2))
finally:
    html.close()

