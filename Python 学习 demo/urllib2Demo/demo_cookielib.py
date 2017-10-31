
import urllib.request
import urllib.parse
import http.cookiejar

'''
url = "http://c.highpin.cn/Users/CLogin"
postdata =urllib.parse.urlencode({ 
"Logon_Password":"sunmin",
"Logon_PostCode":"fghc",
"Logon_RememberMe":"false",
"Logon_UserEmail":"sun121@qq.com"
}).encode('utf-8')
header = {
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Encoding":"utf-8",
"Accept-Language":"zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
"Connection":"keep-alive",
"Host":"c.highpin.cn",
"Referer":"http://c.highpin.cn/",
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0"
}
req = urllib.request.Request(url,postdata,header)
##print(urllib.request.urlopen(req).read().decode('utf-8'))

#自动记住cookie
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
r = opener.open(req)
print(r.read().decode('utf-8'))

以前用的是python2.7，但是python3开始很多包的位置和以前不一样了，就对这里用到的说明一下：

urllib2合并到了urllib下，urlopen使用时包的位置为urllib.request.urlopen，urlencode使用包位置为urllib.parse.urlencode

cookielib变更为了http.cookiejar
'''

url = 'http://c.highpin.cn/Users/CLogin'
values = {
    'Logon_Password':'**',
    'Logon_PostCode':'fghc',
    'Logon_RememberMe':'false',
    'Logon_UserEmail':'sunbo@**.com'
          }
data = bytes(urllib.parse.urlencode(values), encoding='utf-8')
header = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding':'utf-8',
    'Accept-Language':'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
    'Connection':'keep-alive',
    'Host':'c.highpin.cn',
    'Referer':'http://c.highpin.cn/',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0'
}

request = urllib.request.Request(url, data, header)
# print(urllib.request.urlopen(request).read().decode('utf-8'))

#自动记住cookie
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

r = opener.open(request)
print(r.read().decode('utf-8'))

'''
说明：带cookie的打印出来必须用opener.open(req).read().decode('utf-8')来发送的请求才会带上cookie，如果用urllib.request.urlopen()是不带cookie的

 

说明：
1.urllib.request.Request()返回了一个request的请求实例
2.urlopen是一个封装好的OpenerDirector实例，里面只有三个参数（url，data，timeout）
3.通过build_opener可以自己创建一个OpenerDirector实例，所以如果想要构建一个cookie管理
   build_opener(*handlers)，将handler类实例化增加到OpenerDirector中，比如像上面的例子里增加cookie，
 
 
如果已知cookie内容，且要用这个固定cookie去发送请求，可以在header中直接添加cookie内容去发送请求，例子如下：
比如通过fiddle抓取请求包，看到请求和相应的raw格式，可以看到cookie（cookie属于header）。
'''

