# !/usr/bin/python3

'''
-*- coding: utf-8 -*-
@Author  : 博爱1616
@Time    : 2017/10/31 下午4:37
@Software: PyCharm
@File    : demo_BeautifulSoup.py
'''

from bs4 import BeautifulSoup
import bs4


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

第一个 a 对象的类型： <class 'bs4.element.Tag'>
'''
print('第一个 a 对象的类型：', type(soup.a))

'''
对于 Tag，它有两个重要的属性，是 name 和 attrs，下面我们分别来感受一下

name： [document]
head.name： head
'''
print('name：', soup.name)
print('head.name：', soup.head.name)

'''
soup 对象本身比较特殊，它的 name 即为 [document]，
对于其他内部标签，输出的值便为标签本身的名称。

p.attrs： {'class': ['title'], 'name': 'dromouse'}
'''
print('p.attrs：', soup.p.attrs)

'''
在这里，我们把 p 标签的所有属性打印输出了出来，得到的类型是一个字典。

如果我们想要单独获取某个属性，可以这样，例如我们获取它的 class 叫什么
还可以这样，利用get方法，传入属性的名称，二者是等价的

p['class']： ['title']
p.get('class')： ['title']
'''
print("p['class']：", soup.p['class'])
print("p.get('class')：", soup.p.get('class'))

'''
我们可以对这些属性和内容等等进行修改，例如

soup.p： <p class="boaiClass" name="boaihome"><b>The Dormouse's story</b></p>
'''
soup.p['class'] = 'boaiClass'
print('soup.p：', soup.p)


'''
NavigableString

既然我们已经得到了标签的内容，那么问题来了，
我们要想获取标签内部的文字怎么办呢？很简单，用 .string 即可，例如

soup.p.string： The Dormouse's story
'''
print('soup.p.string：', soup.p.string)

'''
这样我们就轻松获取到了标签里面的内容，想想如果用正则表达式要多麻烦。
它的类型是一个 NavigableString，翻译过来叫 可以遍历的字符串，
不过我们最好还是称它英文名字吧。来检查一下它的类型

soup.p.string 类型： <class 'bs4.element.NavigableString'>
'''
print('soup.p.string 类型：', type(soup.p.string))

'''
Comment

Comment 对象是一个特殊类型的 NavigableString 对象，其实输出的内容仍然不包括注释符号，但是如果不好好处理它，可能会对我们的文本处理造成意想不到的麻烦。

我们找一个带注释的标签

soup.a： <a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>
soup.a.string：  Elsie 
soup.a.string 类型： <class 'bs4.element.Comment'>
'''
print('soup.a：', soup.a)
print('soup.a.string：', soup.a.string)
print('soup.a.string 类型：', type(soup.a.string))

'''
a 标签里的内容实际上是注释，但是如果我们利用 .string 来输出它的内容，
我们发现它已经把注释符号去掉了，所以这可能会给我们带来不必要的麻烦。

另外我们打印输出下它的类型，发现它是一个 Comment 类型，
所以，我们在使用前最好做一下判断，判断代码如下

soup.a.string 类型2： <class 'bs4.element.Comment'>
'''
if type(soup.a.string) == bs4.element.Comment:
    print('soup.a.string 类型2：', type(soup.a.string))

















































