

class BAEmployee:

    '所有员工的基类'

    empCount = 0

    def __init__(self, userName, userSalary):
        self.userName = userName
        self.userSalary = userSalary
        BAEmployee.empCount += 1

    def ba_displayCount(self):
        print('总共有 %s 人！' % (BAEmployee.empCount))

    def ba_displayDetail(self):
        print('name：%s，salary：%s！'%(self.userName, self.userSalary))



# emp1 = BAEmployee('boai', 2000)
# emp2 = BAEmployee("Manni", 5000)
#
# emp1.ba_displayDetail()
# emp2.ba_displayDetail()
#
# emp1.ba_displayCount()

'''
Python内置类属性

__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
__doc__ :类的文档字符串
__name__: 类名
__module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
__bases__ : 类的所有父类构成元素（包含了以个由所有父类组成的元组）
Python内置类属性调用实例如下：
'''
print('BAEmployee.__doc__：', BAEmployee.__doc__)
print('BAEmployee.__name__：', BAEmployee.__name__)
print('BAEmployee.__module__：', BAEmployee.__module__)
print('BAEmployee.__bases__：', BAEmployee.__bases__)
print('BAEmployee.__dict__：', BAEmployee.__dict__)







