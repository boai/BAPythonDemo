import urllib.request
import urllib.parse
import http.cookiejar

'''
#声明一个CookieJar对象实例来保存cookie
cookie = cookielib.CookieJar()
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler=urllib2.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = urllib2.build_opener(handler)
#此处的open方法同urllib2的urlopen方法，也可以传入request
response = opener.open('http://www.baidu.com')
for item in cookie:
    print 'Name = '+item.name
    print 'Value = '+item.value
'''

# #声明一个CookieJar对象实例来保存cookie
# cookie = http.cookiejar.CookieJar()
# #利用urllib库的HTTPCookieProcessor对象来创建cookie处理器
# handler = urllib.request.HTTPCookieProcessor(cookie)
# #通过handler来构建opener
# opener = urllib.request.build_opener(handler)
# #此处的open方法同urllib2的urlopen方法，也可以传入request
# url = 'http://www.baidu.com'
# response = opener.open(url)
# for item in cookie:
#     print('name：', item.name)
#     print('value：', item.value)

'''
打印结果：

name： BAIDUID
value： E807B08CF4C659BC24F1B3A058142EAD:FG=1
name： BIDUPSID
value： E807B08CF4C659BC24F1B3A058142EAD
name： H_PS_PSSID
value： 1467_21124_18560_17001_24879_22160
name： PSTM
value： 1509421872
name： BDSVRTM
value： 0
name： BD_HOME
value： 0

'''

# 保存Cookie到文件
'''
import cookielib
import urllib2
 
#设置保存cookie的文件，同级目录下的cookie.txt
filename = 'cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = urllib2.build_opener(handler)
#创建一个请求，原理同urllib2的urlopen
response = opener.open("http://www.baidu.com")
#保存cookie到文件
cookie.save(ignore_discard=True, ignore_expires=True)
'''

# # 设置保存cookie的文件，同级目录下的cookie.txt
# fileName = 'cookie.txt'
# # 声明一个 MozillaCookieJar 对象实例来保存 cookie，之后写入文件
# cookie = http.cookiejar.MozillaCookieJar(filename = fileName)
# # 利用urllib库的HTTPCookieProcessor对象来创建cookie处理器
# handler = urllib.request.HTTPCookieProcessor(cookie)
# # 通过handler来构建opener
# opener = urllib.request.build_opener(handler)
# # 创建一个请求，原理同urllib的urlopen
# response = opener.open('http://www.baidu.com')
# # 保存cookie到文件
# cookie.save(ignore_discard=True, ignore_expires=True)

'''
关于最后save方法的两个参数在此说明一下：

由此可见，ignore_discard的意思是即使cookies将被丢弃也将它保存下来，
ignore_expires的意思是如果在该文件中 cookies已经存在，则覆盖原文件写入，
在这里，我们将这两个全部设置为True。运行之后，cookies将被保存到cookie.txt文件中
'''

# 从文件中获取Cookie并访问
'''
那么我们已经做到把Cookie保存到文件中了，如果以后想使用，
可以利用下面的方法来读取cookie并访问网站:
#创建MozillaCookieJar实例对象
cookie = cookielib.MozillaCookieJar()
#从文件中读取cookie内容到变量
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
#创建请求的request
req = urllib2.Request("http://www.baidu.com")
#利用urllib2的build_opener方法创建一个opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(req)
print response.read()
'''
# 创建MozillaCookieJar实例对象
cookie = http.cookiejar.MozillaCookieJar()
# 从文件中读取cookie内容到变量
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
# 创建请求的request
request = urllib.request.Request('http://www.baidu.com')
# 利用urllib2的build_opener方法创建一个opener
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
response = opener.open(request)

print('请求结果：', response.read())
'''
设想，如果我们的 cookie.txt 文件中保存的是某个人登录百度的cookie，
那么我们提取出这个cookie文件内容，就可以用以上方法模拟这个人的账号登录百度。
'''

# 利用cookie模拟网站登录





