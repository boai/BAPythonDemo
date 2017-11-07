# !/usr/bin/python3

'''
-*- coding: utf-8 -*-scapy
@Author  : 博爱1616
@Time    : 2017/11/3 下午1:56
@Software: PyCharm
@File    : zhuabao_scapy.py
'''



import re
import urllib
import urllib.request
import http.cookiejar
from collections import deque

# import re
# import urllib
# import urllib.request
# from collections import
#
# url = "http://www.163.com"
#
# queue = deque()
# visited = set()
# total_count = 1
# queue.append(url)
#
# while queue:
#     url = queue.popleft()
#     visited |= {url}
#     print("正在抓取第 " + str(total_count) + " 个, " + url)
#     total_count += 1
#     urllop = urllib.request.urlopen(url, timeout=1)
#     if "html" not in urllop.getheader('Content-Type'):
#         print(urllop + " 不是html页面，忽略！")
#         continue
#     try:
#         data = urllop.read().decode("utf-8")
#     except Exception as e:
#         print(e)
#         continue
#     count_per_page = 0
#
#     linkre = re.compile('href="(.+?)"')
#     for x in linkre.findall(data):
#         if 'https://www.you_compay_home_page.com/' in x and x not in visited:
#             count_per_page += 1
#             queue.append(x)  # 注意调试的时候注释本行,以免对服务器造成压力
#             print("加入待爬页面：" + x)
#     print("本页面共加入待爬页面:" + str(count_per_page))



print("\n\n*************** Step 1: visit index page and get the token generated in server side ******************")
url = "http://gitlab.your_company_addr.com/users/sign_in"

header = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Host': 'www.zhihu.com',
    'DNT': '1'
    # 'Cookie': '_gitlab_session=f00c50db7dc2c83989419079760e5786'
}


def getToken(data):
    cer = re.compile('name=\"authenticity_token\" value=\"(.+?)\"')
    strlist = cer.findall(data)
    return strlist[0]


def getOpener(head):
    # deal with the Cookies
    cj = cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener


opener = getOpener(header)
op = opener.open(url)
data = op.read().decode("utf-8")
token = getToken(data)
print(token)


