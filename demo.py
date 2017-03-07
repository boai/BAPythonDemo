#!/usr/bin/env 
# -*- coding:UTF-8 -*-

# print("hello, world!")
# print("hello, world1", "123")
# name = input("Please enter your name：")
# print("hello", name)


# a = input('请输入变量a：')
# b = input('请输入变量b：')
# print("a + b = ", a + b)
# 请输入变量a：1024
# 请输入变量b：2
# a + b =  10242


# a = 100
# if a % 2 == 0:
# 	print('你输入的是2的倍数！')
# else:
# 	print('你输入的不是2的倍数！')


# 转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\，可以在Python的交互式命令行用print()打印字符串看看：
# print('I\'m OK !')
# print('''...line1...line2''')
# print('''line1
# ... line2
# ... line3''')
# print('''line1
# line2
# line3''')


# n = 123
# f = 456.789
# s1 = 'Hello, world'
# s2 = 'Hello, \'Adam\''
# s3 = r'Hello, "Bart"'
# s4 = r'''Hello,
# boai!'''

# print(n, f, s1, s2, s3, s4)

# if True:
# 	print('True')
# else:
# 	print('False')
	
 # Fibonacci series: 斐波纳契数列
 # 两个元素的总和确定了下一个数
# a, b = 0, 1
# print(a, b)

# a = 4.3-1
# print(a)
# b = 2**3
# print(b)


# 与C字符串不同的是，Python字符串不能被改变。向一个索引位置赋值，比如word[0] = 'm'会导致错误。
# 注意：
# 1、反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
# 2、字符串可以用+运算符连接在一起，用*运算符重复。
# 3、Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
# 4、Python中的字符串不能改变。

# string = "我是博爱！"
# print(string[1], string[3])
# string = "I love Python!"
# print(string[2:6])
# print(string[-12:-8])

# string2 = "：boai"
# print(string + string2)


# List（列表）

# List（列表） 是 Python 中使用最频繁的数据类型。
# 列表是写在方括号之间、用逗号分隔开的元素列表。列表中元素的类型可以不相同：
# a = ['我是博爱，', '今年', 18, '岁了！']
# print(a)

# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a+b
# print(c)

# c[0] = 9
# print(c)
# c[2:4] = [88, 99]
# print(c)
# # [9, 2, 88, 99, 5, 6]

# List内置了有很多方法，例如append()、pop()等等，这在后面会讲到。
# 注意：
# 1、List写在方括号之间，元素用逗号隔开。
# 2、和字符串一样，list可以被索引和切片。
# 3、List可以使用+操作符进行拼接。
# 4、List中的元素是可以改变的。


# Tuple（元组）

# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号里，元素之间用逗号隔开。
# 元组中的元素类型也可以不相同：
# tup = (1, 2, 3, 4, 5)
# print(tup[0], tup[1:5])
# # 1 (2, 3, 4, 5)

# tup1 , tup2 = (1,2,3), (4,5,6)
# print(tup1+tup2)
# # (1, 2, 3, 4, 5, 6)

# string、list和tuple都属于sequence（序列）。
# 注意：
# 1、与字符串一样，元组的元素不能修改。
# 2、元组也可以被索引和切片，方法一样。
# 3、注意构造包含0或1个元素的元组的特殊语法规则。
# 4、元组也可以使用+操作符进行拼接。


# Sets（集合）

# 集合（set）是一个无序不重复元素的集。
# 基本功能是进行成员关系测试和消除重复元素。
# 可以使用大括号 或者 set()函数创建set集合，注意：创建一个空集合必须用 set() 而不是 { }，因为{ }是用来创建一个空字典。

# student = {'博爱', '晓峰', '石少'}
# print(student)
# # {'博爱', '石少', '晓峰'}

# set可以进行集合运算
# a = set('aabbccf')
# b = set('abcd')
# # a 
# # {'a', 'b', 's', 'f'}
# # a和b的差集
# c = a - b
# print(c)
# # {'f'}

# # a和b的并集
# c = a | b
# print(c)
# # {'b', 'd', 'f', 'a', 'c'}

# a和b的交集
# c = a & b
# print(c)
# # {'c', 'a', 'b'}

# a和b中不同时存在的元素
# c = a ^ b
# print(c)
# # {'d', 'f'}


# Dictionaries（字典）

# 字典（dictionary）是Python中另一个非常有用的内置数据类型。
# 字典是一种映射类型（mapping type），它是一个无序的键 : 值对集合。
# 关键字必须使用不可变类型，也就是说list和包含可变类型的tuple不能做关键字。
# 在同一个字典中，关键字还必须互不相同。

# dic = {'boai':16, '石少':18}
# # print(dic)
# # # {'boai': 16, '石少': 18}
# # print(dic['boai'])
# # # 16

# # 添加一个键值对
# dic['tom'] = 20
# # print(dic)
# # {'boai': 16, '石少': 18, 'tom': 20}

# # 返回所有key组成的list
# print(list(dic.keys()))
# # ['boai', '石少', 'tom']

# # 按key排序
# dic['mars'] = 17
# # print(dic)
# # {'boai': 16, '石少': 18, 'tom': 20, 'mars': 17}
# print(sorted(dic.keys()))
# # ['boai', 'mars', 'tom', '石少']
# print(sorted(dic.values()))
# # [16, 17, 18, 20]

# # 成员测试
#  # bool a = 'tom' in dic
# print('tom' in dic)
# # True
# print('mars' not in dic)
# # False

# 另外，字典类型也有一些内置的函数，例如clear()、keys()、values()等。
# 注意：
# 1、字典是一种映射类型，它的元素是键值对。
# 2、字典的关键字必须为不可变类型，且不能重复。
# 3、创建空字典使用{ }。


































