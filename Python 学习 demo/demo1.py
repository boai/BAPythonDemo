

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






