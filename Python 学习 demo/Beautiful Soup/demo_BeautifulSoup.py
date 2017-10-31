# !/usr/bin/python3

'''
-*- coding: utf-8 -*-
@Author  : 博爱1616
@Time    : 2017/10/31 下午4:37
@Software: PyCharm
@File    : demo_BeautifulSoup.py
'''

from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="boaihome"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

# 创建 beautifulsoup 对象
soup = BeautifulSoup(html, 'lxml')
# 另外，我们还可以用本地 HTML 文件来创建对象，例如
# soup2 = BeautifulSoup(open('test2.html'), 'lxml')

'''
上面这句代码便是将本地 test2.html 文件打开，用它来创建 soup 对象

下面我们来打印一下 soup 对象的内容，格式化输出
'''

# print('格式化抓取内容：\n%s ' % (soup2.prettify()))


'''
四大对象种类

Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以归纳为4种:

Tag
NavigableString
BeautifulSoup
Comment
下面我们进行一一介绍

（1）Tag

Tag 是什么？通俗点讲就是 HTML 中的一个个标签，
上面的 title a 等等 HTML 标签加上里面包括的内容就是 Tag，下面我们来感受一下怎样用 Beautiful Soup 来方便地获取 Tags

下面每一段代码中注释部分即为运行结果
'''

print('title：', soup.title)
print('head：', soup.head)
print('a：', soup.a)
print('p：', soup.p)

'''
我们可以利用 soup加标签名轻松地获取这些标签的内容，是不是感觉比正则表达式方便多了？不过有一点是，它查找的是在所有内容中的第一个符合要求的标签，如果要查询所有的标签，我们在后面进行介绍。

我们可以验证一下这些对象的类型
'''
print('第一个 a 对象的类型：', type(soup.a))

'''
对于 Tag，它有两个重要的属性，是 name 和 attrs，下面我们分别来感受一下
'''
print('name：', soup.name)
print('head.name：', soup.head.name)

'''
soup 对象本身比较特殊，它的 name 即为 [document]，
对于其他内部标签，输出的值便为标签本身的名称。
'''
print('p.attrs：', soup.p.attrs)





