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


# 6. 遍历文档树
'''
tag 的 .content 属性可以将tag的子节点以列表的方式输出
输出方式为列表，我们可以用列表索引来获取它的某一个元素

soup.head.contents： [<title>The Dormouse's story</title>]
soup.head.contents[0]： <title>The Dormouse's story</title>
'''
print('soup.head.contents：', soup.head.contents)
print('soup.head.contents[0]：', soup.head.contents[0])

'''
.children

它返回的不是一个 list，不过我们可以通过遍历获取所有子节点。

我们打印输出 .children 看一下，可以发现它是一个 list 生成器对象,
我们怎样获得里面的内容呢？很简单，遍历一下就好了，代码及结果如下

soup.head.children： <list_iterator object at 0x1046e42e8>
child： <title>The Dormouse's story</title>
'''
print('soup.head.children：', soup.head.children)
for child in soup.head.children:
    print('child：', child)

'''
body.children： 

body.children： <p class="boaiClass" name="boaihome"><b>The Dormouse's story</b></p>
body.children： 

body.children： <p class="story">Once upon a time there were three little sisters; and their names were
<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>,
<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
body.children： 

body.children： <p class="story">...</p>
body.children： 
'''
# for child in soup.body.children:
    # print('body.children：', child)

'''
soup.descendants： <html><head><title>The Dormouse's story</title></head>
<body>
<p class="boaiClass" name="boaihome"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>,
<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
</body></html>
soup.descendants： <head><title>The Dormouse's story</title></head>
soup.descendants： <title>The Dormouse's story</title>
soup.descendants： The Dormouse's story
soup.descendants： 

soup.descendants： <body>
<p class="boaiClass" name="boaihome"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>,
<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
</body>
soup.descendants： 

soup.descendants： <p class="boaiClass" name="boaihome"><b>The Dormouse's story</b></p>
soup.descendants： <b>The Dormouse's story</b>
soup.descendants： The Dormouse's story
soup.descendants： 

soup.descendants： <p class="story">Once upon a time there were three little sisters; and their names were
<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>,
<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
soup.descendants： Once upon a time there were three little sisters; and their names were

soup.descendants： <a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>
soup.descendants：  Elsie 
soup.descendants： ,

soup.descendants： <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
soup.descendants： Lacie
soup.descendants：  and

soup.descendants： <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
soup.descendants： Tillie
soup.descendants： ;
and they lived at the bottom of a well.
soup.descendants： 

soup.descendants： <p class="story">...</p>
soup.descendants： ...
soup.descendants： 
'''
# for child in soup.descendants:
    # print('soup.descendants：', child)

'''
.strings

获取多个内容，不过需要遍历获取，比如下面的例子

soup.strings：
 The Dormouse's story
soup.strings：
 

soup.strings：
 

soup.strings：
 The Dormouse's story
soup.strings：
 

soup.strings：
 Once upon a time there were three little sisters; and their names were

soup.strings：
 ,

soup.strings：
 Lacie
soup.strings：
  and

soup.strings：
 Tillie
soup.strings：
 ;
and they lived at the bottom of a well.
soup.strings：
 

soup.strings：
 ...
soup.strings：
'''
# for string in soup.strings:
#     print('soup.strings：\n', string)

'''
.stripped_strings

输出的字符串中可能包含了很多空格或空行,使用 .stripped_strings 可以去除多余空白内容

soup.strings：
 The Dormouse's story
soup.strings：
 The Dormouse's story
soup.strings：
 Once upon a time there were three little sisters; and their names were
soup.strings：
 ,
soup.strings：
 Lacie
soup.strings：
 and
soup.strings：
 Tillie
soup.strings：
 ;
and they lived at the bottom of a well.
soup.strings：
 ...
'''
# for string in soup.stripped_strings:
#     print('soup.strings：\n', string)

'''
父节点

知识点： .parent 属性

soup.p.parent.name： body
soup.head.title.string.parent.name： title
'''
print('soup.p.parent.name：', soup.p.parent.name)
print('soup.head.title.string.parent.name：', soup.head.title.string.parent.name)

'''
全部父节点

知识点：.parents 属性
通过元素的 .parents 属性可以递归得到元素的所有父辈节点，例如

soup.head.title.string.parents： title
soup.head.title.string.parents： head
soup.head.title.string.parents： html
soup.head.title.string.parents： [document]
'''
# for parent in soup.head.title.string.parents:
#     print('soup.head.title.string.parents：', parent.name)


'''
兄弟节点

知识点：.next_sibling .previous_sibling 属性
兄弟节点可以理解为和本节点处在统一级的节点，
.next_sibling 属性获取了该节点的下一个兄弟节点，
.previous_sibling 则与之相反，如果节点不存在，则返回 None

注意：实际文档中的tag的 .next_sibling 和 .previous_sibling 属性通常是字符串或空白，
因为空白或者换行也可以被视作一个节点，所以得到的结果可能是空白或者换行

soup.p.next_sibling： 
#       实际该处为空白
soup.p.prev_sibling： None
soup.p.next_sibling.next_sibling： 
<p class="story">Once upon a time there were three little sisters; and their names were
<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>,
<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

'''
# print('soup.p.next_sibling：', soup.p.next_sibling)
# print('soup.p.prev_sibling：', soup.p.prev_sibling)
# print('soup.p.next_sibling.next_sibling：', soup.p.next_sibling.next_sibling)

'''
全部兄弟节点

知识点：.next_siblings .previous_siblings 属性
通过 .next_siblings 和 .previous_siblings 属性可以对当前节点的兄弟节点迭代输出

soup.a.next_siblings： ',\n'
soup.a.next_siblings： <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
soup.a.next_siblings： ' and\n'
soup.a.next_siblings： <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
soup.a.next_siblings： ';\nand they lived at the bottom of a well.'

'''
# for sibling in soup.a.next_siblings:
#     print('soup.a.next_siblings：', repr(sibling))

'''
前后节点

知识点：.next_element .previous_element 属性
与 .next_sibling .previous_sibling 不同，它并不是针对于兄弟节点，而是在所有节点，不分层次

比如 head 节点为
'''
print('soup.head.next_element：', soup.head.next_element)


















