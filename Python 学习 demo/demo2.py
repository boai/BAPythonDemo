
import BAEmployee

emp1 = BAEmployee.BAEmployee('boai', 2000)
emp1.age = 18

emp2 = BAEmployee.BAEmployee('tom', 1888)
emp2.age = 20

emp1.ba_displayDetail()
emp2.ba_displayDetail()

emp1.ba_displayCount()

print('emp1 age = ', getattr(emp1, 'age'))

'''
你也可以使用以下函数的方式来访问属性：
getattr(obj, name[, default]) : 访问对象的属性。
hasattr(obj,name) : 检查是否存在一个属性。
setattr(obj,name,value) : 设置一个属性。如果属性不存在，会创建一个新属性。
delattr(obj, name) : 删除属性。
hasattr(emp1, 'age')    # 如果存在 'age' 属性返回 True。
getattr(emp1, 'age')    # 返回 'age' 属性的值
setattr(emp1, 'age', 8) # 添加属性 'age' 值为 8
delattr(empl, 'age')    # 删除属性 'age'
'''
isHaveAge = hasattr('emp1', 'age')
print('是否含有 age 属性：', isHaveAge)



