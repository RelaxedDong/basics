#encoding:utf-8

# class Myclass():
#     i = 12345
#     def f(self):
#         return 'hello world'
#
# x = Myclass()
# print('Myclass 得属性为：',x.i)
# print('Myclass类方法输出为',x.f())


#构造函数
# class Complex():
#     def __init__(self,realpart,imagpart):
#         self.r = realpart
#         self.i = imagpart
#     def __str__(self):
#         return 'ong is %s,other one is%s'%(self.r,self.i)
# x = Complex(2,3)
# print(x)

# class Test():
#     def ptr(self):
#         print(self)
#         print(self.__class__)
#         def __str__(self):
#             return 'one is %s %s'%(self,self.__class__)
# t = Test()
# t.ptr()
#类得方法：
# class People():
#     age = 20
#     name = 'donghao'
#     # 定义私有属性,私有属性在类外部无法直接进行访问
#     __weight = 120
#     def __init__(self,a,n,w):
#         self.age = a
#         self.name = n
#         self.__weight = w
#     def speak(self):
#         print('%s说，我%s岁,%s'%(self.name,self.age,self.__weight))
# #
# # p = Perple(20,'donghao',20)
# # p.speak()
#
# #继承
# class children(People):
#     grade = ''
#     def __init__(self,a,n,w,g):
#         People.__init__(self,a,n,w)
#         self.grade =  g
#     def speak(self):
#         print('%s说，我%s岁,%s年级' % (self.name, self.age,self.grade))
# s = children(20,'donghao',20,3)
# s.speak()


# class speker():
#     name = ''
#     topoc = ''
#     def __init__(self,n,t):
#         self.name = n
#         self.topoc = t
#     def speak(self):
#         print('我叫%s,我是一个学生,主题是%s'%(self.name,self.topoc))
#
# class sample(speker,children):
#     a = ''
#     def __init__(self,n,a,w,g,t):
#         children.__init__(self,a,n,w,g)
#         speker.__init__(self,n,t)
#
# test = sample('donghao',20,110,4,'python')
# test.speak()


#方法重写
# class Parent:
#     def myMethod(self):
#         print('调用父类的方法')
#
# class Child(Parent):
#     def myMethod(self):
#         # super(Child,self).myMethod()
#         print('调用子类方法')
#
# c = Child()
# c.myMethod()
# super(Child,c).myMethod()

#类的私有方法
# class justCount():
#     __precount = 0
#     publiccount = 0
#     def count(self):
#         self.__precount+=1
#         self.publiccount+=1
#         print(self.__precount)
#
# c = justCount()
# c.count()
# c.count()
# print(c.publiccount)

#类的私有方法
# class Site():
#     def __init__(self,name,url):
#         self.name = name #public
#         self.url = url
#     def who(self):
#         print('name is :',self.name)
#         print('url is :',self.url)
#     def __foo(self):#私有方法
#         print('私有方法')
#     def foo(self):
#         print('这是共有方法')
#         self.__foo()
# site = Site('菜鸟教程','www.runoob.com')
# site.who()
# site.foo()
# site.__foo()#AttributeError: 'Site' object has no attribute '__foo'


# 类的专有方法：
#
# __init__: 构造函数，在生成对象时调用
# __del__: 析构函数，释放对象时使用
# __repr__: 打印，转换
# __setitem__: 按照索引赋值
# __getitem__: 按照索引获取值
# __len__: 获得长度
# __cmp__: 比较运算
# __call__: 函数调用
# __add__: 加运算
# __sub__: 减运算
# __mul__: 乘运算
# __div__: 除运算
# __mod__: 求余运算
# __pow__: 乘方

#运算符重载
# class Count():
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def __repr__(self):
#         return 'vector(%d,%d)'%(self.a,self.b)
#     def __add__(self, other):
#         return Count(self.a+other.a,self.b+other.b)
# c1 = Count(2,10)
# c2 = Count(5,-2)
# print((c1+c2))

class People():
    def __init__(self,n,g):
        self.name = n
        self.age = g
    def __str__(self):
        return '名字：%s,年龄%s'%(self.name,self.age)

p = People('donghao',20)
print(p)














