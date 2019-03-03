# Robots协议

## 概述

Robots协议，也称作爬虫协议，全名叫网络爬虫排除标准(Robots    Exclusion Protocol,用来告诉泡虫和搜索引擎那些页面可以抓取，那些不可以抓取
通常是一个robots.txt文本文件，在网站的根目录

当搜索引擎访问一个站点的时候，回首先检查这个站点根目录下是否存在robots.txt文件。如果存在，搜索引擎会根据其中定义的爬取范围来爬取。如果没有，则会访问所有可能直接访问的页面。

## 爬虫名称

爬虫名称

名称

网站

BaiduSpider

百度

www.baidu.com

Googlebot

谷歌

www.google.com

360Spider

360搜索

www.so.com

YodaoBot

有道

www.youdao.com

ia_archiver

Alexa

www.alexa.cn

Scooter

altavista

www.altavista.com

##  robotparse

使用该模块来解析robots.txt。

该模块提供了一个类 RobotFileParser，下面列出了常用的几个方法。

- set_url():用来设置robots.txt文件的链接。如果在创建RobotFileParser对象时引入了链接，就不需要在使用这个方法了。
- read(): 读取robots.txt文件并进行分析。注意，这个方法执行一个读取和分析操作，如果不调用这个方法，接下来的判断都会为False，这个方法不会返回任何内容，但是执行了读取操作。
- parse(): 用来解析robots.txt文件，擦混入的参数是robots.txt某些行的内容，会按照robots.txt的语法规则分析这些内容
- can_fetch(): 该方法传入两个参数。第一个是User-agent，第二个是要抓取的url，返回的内容是该搜索引擎似乎否可以抓取这个url，true或者false
- mtime(): 返回的是上次抓取和分析robots.txt的时间，这对于长时间分析和抓取的搜索爬虫是很必要的，你需要定期检查抓取最新的robots.txt
- modified(): 将当前时间设置为上次抓取和分析robots.txt的时间

 