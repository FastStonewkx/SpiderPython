#  Requests库高级用法

## 文件上传

requests可以模拟提交一些数据。假如有的网站需要上传文件，我们可以用它来实现。

## Cookies

requests获取和设置Cookies比urllib更加方便

## 会话维持

前面说过网站识别用户的登陆状态就是通过会话和cookie协调完成。这里的会话是服务器用来识别用户的身份的方式，如果不设置会话的话，当一个使用get请求另一个是post请求的话，这个相当于在两个浏览器打开了不同的页面。

所以设置会话可以用来保持用户的登陆状态的。requests中，会话使用request.Session()

## SSL证书验证

当发送http请求的时候，它会自动检查SSL证书，可以使用verify参数控制时候检查该证书。默认是true，自动检查

## 代理设置

对于爬虫来说，当大规模爬取网站，网站可能会弹出验证码。或者跳转到登陆页面，甚至或直接封禁客户端ip，一定时间内无法访问

可以设置代理来解决这个问题。

这个我没有买，没有现成的东西，例子就不能演示了。

## 超时设置

网站因为各种原因，导致请求的响应时间特别长。这里就需要设置超时时间


## 身份验证

这个验证需要有一个页面来登陆访问

这个可以拿一个需要登陆的页面做测试



## Propared Request

在urllib中，我们可以将请求的数据表示为数据结构，其中各个参数都可以通过Request对象来表示

在requests中，使用Prepared Request来表示这数据结构

