
import urllib.parse
import urllib.request
import ssl


ssl._create_default_https_context = ssl._create_unverified_context

'''
python3对urllib和urllib2进行了重构，拆分成了urllib.request, urllib.response, urllib.parse, urllib.error等几个子模块，这样的架构从逻辑和结构上说更加合理。
urljoin现在对应的函数是urllib.parse.urljoin

详见：http://www.cnblogs.com/myis55555/p/6680933.html
'''

# # response = urllib.request.urlopen('http://www.baidu.com')
#
# # 构造Requset
# request = urllib.request.Request('http://www.baidu.com')
#
# # 分分钟扒一个网页下来
# response = urllib.request.urlopen(request)
#
# print('抓取结果：', response.read())

# POST和GET数据传送
'''
数据传送分为POST和GET两种方式，两种方式有什么区别呢？

最重要的区别是GET方式是直接以链接形式访问，链接中包含了所有的参数，
当然如果包含了密码的话是一种不安全的选择，不过你可以直观地看到自己提交了什么内容。
POST则不会在网址上显示所有的参数，不过如果你想直接查看提交了什么就不太方便了，
大家可以酌情选择。
'''

# values = {"username":"137361770@qq.com","password":"137361770"}
# data = bytes(urllib.parse.urlencode(values), encoding='utf-8')
# url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
# response = urllib.request.urlopen(url, data)
# print('抓取结果：', response.read())

'''
import urllib2 

httpHandler = urllib2.HTTPHandler(debuglevel=1)  
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)  
opener = urllib2.build_opener(httpHandler, httpsHandler)  
urllib2.install_opener(opener)  
res = urllib2.urlopen('http://www.baidu.com')
'''

# import urllib
# http_handler = urllib.request.HTTPHandler()
# https_handler = urllib.request.HTTPSHandler(debuglevel=1)
# opener = urllib.request.build_opener(http_handler, https_handler)
# urllib.request.install_opener(opener)
# response = urllib.request.urlopen("http://www.baidu.com")
# print('抓取结果：', response.read())


'''
1.URLError

首先解释下URLError可能产生的原因：

网络无连接，即本机无法上网
连接不到特定的服务器
服务器不存在
'''

# requset = urllib2.Request('http://www.xxxxx.com')
# try:
#     urllib2.urlopen(requset)
# except urllib2.URLError, e:
#     print
#     e.reason

request = urllib.request.Request('http://www.**.com')
try:
    urllib.request.urlopen(request)
except urllib.request.URLError as e:
    print(e.reason)
'''
上面打印结果：[Errno 8] nodename nor servname provided, or not known
'''






