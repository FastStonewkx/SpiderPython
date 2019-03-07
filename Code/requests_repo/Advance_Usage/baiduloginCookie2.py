#  通过cookies参数来设置，需要构造RequestsCookieJar对象，需要分割Cookies。
# 同1

import requests

cookies = 'A^`=0000000000rD93001414469; PSTM=1535985244; BIDUPSID=4423E6F772CCC688125C9980AF419142; BAIDUID=4A19C89E067259BAC471BF947EDF6574:FG=1; BD_UPN=12314753; BDUSS=zk5dVJ2QWtKNGZUTU5wd3hqU3dTdGtpd1VsZW9UdHpRaXQ4LUZSeGx3ZlRTSjVjQVFBQUFBJCQAAAAAAAAAAAEAAAA2hoQus6y8trD0sPTMx3p6eAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANO7dlzTu3Zcc; BDRCVFR[Ipe9RQ2Gv_s]=IdAnGome-nsnWnYPi4WUvY; delPer=0; BD_CK_SAM=1; PSINO=2; H_PS_PSSID=1442_25810_21108_20697_28608_28584_28557_28604_28625_28606; H_PS_645EC=14caKAjgZ56vis5Zfe%2B2cuCkaJupCNyjh4Udyo%2BYjxf1%2FwItHHvkWxDYBRHGGK9Fmvg%2BKw; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BD_HOME=1; sug=3; sugstore=0; ORIGIN=0; bdime=0'
jar = requests.cookies.RequestsCookieJar()
headers = {
'host':'www.baidu.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}

for cookies in cookies.split(';'):
    key, value = cookies.split('=', 1)
    jar.set(key, value)
r = requests.get('http://www.baidu.com', cookies=jar, headers = headers)
print(r.text)

"""
这里首先新建了一个RequestCookieJar对象，然后复制下来的cookies利用split()方法分割，接着利用set()方法设置好每个Cookie的
key和value，然后通过调用requests的get()方法并传递cookies参数即可
可以登录

为了安全，我已经退出重新生成了新的cookie，这个代码已经无效了
"""