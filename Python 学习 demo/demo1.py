

# 第一个 Python 程序

print ("Hello, World!")

# 直接打印中文，前提 Python 3
print ("你好，世界！")

# bool 变量、if else 用法
isLog = False

if isLog:
    print ("打开了开关")
else:
    print ("关闭了开关")

# python 中多行注释使用三个单引号(''')或三个双引号(""")。

'''
这里是多行注释！
'''

# 测试换行
print("我\n爱\n你")

# raw_input("\n\nPress the enter key to exit.")

# 同一行显示多条语句
import sys; x = 'boai'; sys.stdout.write(x + '\n love\n\n')


'''
变量赋值

Python中的变量不需要声明，变量的赋值操作既是变量声明和定义的过程。
每个变量在内存中创建，都包括变量的标识，名称和数据这些信息。
每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
等号（=）用来给变量赋值。
等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值。例如：
'''
a = 100
b = 9.90
c = 'boai'

print('a =',a)
print('b =',b)
print('c =',c)

# 可以为多个对象指定多个变量
d, e, f = 88, 5.20, '我是博爱！'
print('d =',d)
print('e =',e)
print('f =',f)

str = 'hello，world！'

# 输出完整字符串
print(str)
# 输出字符串中的第一个字符
print(str[0])
# 输出字符串中第三个至第五个之间的字符串
print(str[0:5])
# 输出从第三个字符开始的字符串
print(str[2:])
# 输出字符串两次
print(str * 2)
# 输出连接的字符串
print(str + 'Test')

'''
Python列表

List（列表） 是 Python 中使用最频繁的数据类型。
列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（所谓嵌套）。
列表用[ ]标识。是python最通用的复合数据类型。看这段代码就明白。
列表中的值得分割也可以用到变量[头下标:尾下标]，就可以截取相应的列表，从左到右索引默认0开始的，从右到左索引默认-1开始，下标可以为空表示取到头或尾。
加号（+）是列表连接运算符，星号（*）是重复操作。如下实例：
'''
list = ['boai', 123, 5.20, 'love']
list2 = ['dandan', 'ai']

print(list)
print(list[0])
print(list[1:2])
print(list[2:])
print(list * 2)
print(list + list2)

'''
Python字典

字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象集合，字典是无序的对象集合。
两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典用"{ }"标识。字典由索引(key)和它对应的值value组成。
'''
dict = {"name":"boai", "age":18}
print(dict['name'])
print(dict.keys())
print(dict.values())








