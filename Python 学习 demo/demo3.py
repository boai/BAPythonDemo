

class BAParent:
    parentAttr = 100

    __money = 20

    def __init__(self):
        print("调用父类构造函数")

    def parentMethod(self):
        print('调用父类方法')

    def setAttr(self, attr):
        BAParent.parentAttr = attr

    def getAttr(self):
        print("父类属性 :", BAParent.parentAttr)

    def testFunction(self):
        print('调用父类方法')

class BAChild(BAParent):

    def __init__(self):
        print("调用子类构造方法")

    def childMethod(self):
        print('调用子类方法 child method')

    def testFunction(self):
        print('调用子类方法')


c = BAChild()        # 实例化子类
c.childMethod()      # 调用子类的方法
c.parentMethod()     # 调用父类方法
c.setAttr(200)       # 再次调用父类的方法
c.getAttr()          # 再次调用父类的方法

c.testFunction()

print('私有变量：', c.__money)


