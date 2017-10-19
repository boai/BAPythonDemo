
import time
import calendar

from BAKit_Common import *

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

'''
Python算术运算符

以下假设变量a为10，变量b为20：
运算符	描述	实例
+	加 - 两个对象相加	a + b 输出结果 30
-	减 - 得到负数或是一个数减去另一个数	a - b 输出结果 -10
*	乘 - 两个数相乘或是返回一个被重复若干次的字符串	a * b 输出结果 200
/	除 - x除以y	b / a 输出结果 2
%	取模 - 返回除法的余数	b % a 输出结果 0
**	幂 - 返回x的y次幂	a**b 为10的20次方， 输出结果 100000000000000000000
//	取整除 - 返回商的整数部分	9//2 输出结果 4 , 9.0//2.0 输出结果 4.0

Python位运算符

按位运算符是把数字看作二进制来进行计算的。Python中的按位运算法则如下：
运算符	描述	实例
&	按位与运算符	(a & b) 输出结果 12 ，二进制解释： 0000 1100
|	按位或运算符	(a | b) 输出结果 61 ，二进制解释： 0011 1101
^	按位异或运算符	(a ^ b) 输出结果 49 ，二进制解释： 0011 0001
~	按位取反运算符	(~a ) 输出结果 -61 ，二进制解释： 1100 0011， 在一个有符号二进制数的补码形式。
<<	左移动运算符	a << 2 输出结果 240 ，二进制解释： 1111 0000
>>	右移动运算符	a >> 2 输出结果 15 ，二进制解释： 0000 1111
'''
a = 20
b = 5
c = 3
d = 5

print('a + b =', a+b)
print('a - b =', a-b)
print('a * b =', a*b)
print('a % b =', a%b)
print('a & b =', a&b)
print('a | b =', a|b)
print('a ^ b =', a^b)
print('~a =', ~a)


if a == b:
    print('a = b')
else:
    print('a != b')

if a or b:
    print("2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("2 - 变量 a 和 b 都不为 true")

list = [20, 3, 5]

if a in list:
    print("1 - 变量 a 在给定的列表中 list 中")
else:
    print("1 - 变量 a 不在给定的列表中 list 中")

if a is b:
    print("1 - a 和 b 有相同的标识")
else:
    print("1 - a 和 b 没有相同的标识")

flag = False
name = 'boai'

if name == 'Python':
    flag = True
    print('welcome boss')
else:
    print(name)

num = 5

if num == 1:
    print('🐱')
elif num == 3:
    print('🐶')
elif num == 5:
    print('🐽')
else:
    print('🐔')

num = 5
if num > 0 and num < 5:
    print('num 大于 0 小于 5')
elif num >= 5 and num < 10:
    print('num >= 5 < 10')
else:
    print('num >= 10 或者 num <= 0')

count = 0
while count < 8:
    print('count =', count)
    count = count +1
print('循环结束')


for letter in "boai":
    print('当前 letter =', letter)

list = ['apple', 'bananer', 'orange']
for fruit in list:
    print('当前水果：', fruit)

'''
循环使用 else 语句

在 python 中，for … else 表示这样的意思，for 中的语句和普通的没有区别，else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行，while … else 也是一样。
如下实例：
'''
for num in range(5,15):
    for i in range(2, num):
        if num % 2 == 0:
            j = num / i
            print(num, '=', i, '*', j)
            break
    else:
        print(num, '是一个质数')

# 嵌套循环输出2~100之间的素数：
i = 2
while i < 100:
    j = 2
    while (j <= (i/j)):
        if not (i%j): break
        j = j + 1
    if (j > i/j):
        print(i, '是素数')
    i = i + 1
print('循环结束！')

for i in range(2, 100):
    j = 2
    while (j <= (i/j)):
        if not (i % j): break
        j = j + 1
    if (j > i / j):
        print(i, '是素数')
    i = i + 1
print('循环结束！')


for letter in 'Python':
    if letter == 'h':
        break
    else:
        print('当前字母 :', letter)

var = 10
while var > 0:
    print('当前变量值 :', var)

    var = var - 1
    if var == 5:
        break
print('循环结束！')

'''
Python continue 语句

Python continue 语句跳出本次循环，而break跳出整个循环。
continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环。
continue语句用在while和for循环中。
'''
for letter in 'Python':
    if letter == 'h':
        continue
    print('当前字母 :', letter)

'''
Python pass 语句

Python pass是空语句，是为了保持程序结构的完整性。
pass 不做任何事情，一般用做占位语句。
'''
for letter in 'Python':
    if letter == 'h':
        pass
        print('这是 pass 块')
    print('当前字母 :', letter)

var1 = 'Python'
var2 = 'Hello, world'

print('var1[0]：', var1[0])
print('var2[0:5]：', var2[0:5])

var3 = 'Hello, world'
print('更新字符串 ：', var3[:7] + 'boai！')


'''
Python转义字符

在需要在字符中使用特殊字符时，python用反斜杠(\)转义字符。如下表：
转义字符	描述
\(在行尾时)	续行符
\\	反斜杠符号
\'	单引号
\"	双引号
\a	响铃
\b	退格(Backspace)
\e	转义
00	空
\n	换行
\v	纵向制表符
\t	横向制表符
\r	回车
\f	换页
\oyy	八进制数，yy代表的字符，例如：\o12代表换行
\other	其它的字符以普通格式输出
'''

'''
Python字符串格式化

Python 支持格式化字符串的输出 。尽管这样可能会用到非常复杂的表达式，但最基本的用法是将一个值插入到一个有字符串格式符 %s 的字符串中。
在 Python 中，字符串格式化使用与 C 中 sprintf 函数一样的语法。
如下实例：
'''
a = 'my name is %(name)s, age is %(age)s' % {'name': 'boai', 'age':18}
print(a)

b = "My name is %s and weight is %d kg!" % ('boai', 50)
print(b)


'''
Python三引号（triple quotes）

python中三引号可以将复杂的字符串进行复制:
python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。
三引号的语法是一对连续的单引号或者双引号（通常都是成对的用）。

三引号让程序员从引号和特殊字符串的泥潭里面解脱出来，自始至终保持一小块字符串的格式是所谓的WYSIWYG（所见即所得）格式的。
一个典型的用例是，当你需要一块HTML或者SQL时，这时用字符串组合，特殊字符串转义将会非常的繁琐。
'''
var = '''
hello
boai！
'''
print(var)

loginHtml = '''
<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s</B><P>
<FORM><INPUT TYPE=button VALUE=Back ONCLICK="window.history.back()"></FORM>
</BODY></HTML>
'''
print(loginHtml)

tuple = (20)
print(tuple)

tuple1 = (2, 5, 8, 20)
print('tuple1[1] = ', tuple1[1])

'''
Python 日期和时间

Python 程序能用很多方式处理日期和时间，转换日期格式是一个常见的功能。
Python 提供了一个 time 和 calendar 模块可以用于格式化日期和时间。
时间间隔是以秒为单位的浮点小数。
每个时间戳都以自从1970年1月1日午夜（历元）经过了多长时间来表示。
Python 的 time 模块下有很多函数可以转换常见日期格式。如函数time.time()用于获取当前时间戳, 如下实例:
'''
ticks = time.time()
print('当前时间的时间戳：',ticks)

var = time.localtime(time.time())
print('当前时间的时间：',var)

loaclTime = time.asctime(time.localtime(time.time()))
print('当前时间的时间：',loaclTime)

'''
python中时间日期格式化符号：
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
'''
# 格式化成2016-03-20 11:45:39形式
currentTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
print('当前时间的时间：',currentTime)

# 将格式字符串转换为时间戳
var = time.asctime(time.localtime(time.time()))
print(time.mktime(time.strptime(var, "%a %b %d %H:%M:%S %Y")))


'''
获取某月日历

Calendar模块有很广泛的方法用来处理年历和月历，例如打印某月的月历：

time、日历 这块儿的详细函数：https://www.w3cschool.cn/python/python-date-time.html
'''

cal = calendar.month(2017, 10)
print("以下输出2017年10月份的日历:\n", cal)

def printStr(str):
    print(str)
    return

printStr('This is a test function!')

# 这是从另一个封装文件【BAKit_Common.py】读取的函数：
currentTime = ba_getCurrentTimeWithYMDHMS()

# 这是从另一个封装文件【BAKit_Common.py】读取的函数：
currentCalendar = ba_getCurrentCalendarWithMonth(2017, 10)

ba_algorithm_sum(10, 15)











