## 面向对象

##### 基本概念 

```
面向对象编程(OOP)的本质是通过抽象建立模型来解决问题，其特点有：封装，继承和多态。
类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。类相当于工厂里面的模具，对象相当于通过这个模具生产的产品。
对象(Object)：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。
实例化(Instance)：创建一个类的实例，类的具体对象。
类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
数据成员：类变量或者实例变量, 用于处理类及其实例对象的相关的数据。
方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
局部变量：定义在方法中的变量，只作用于当前实例的类。
实例变量：在类的声明中，属性是用变量来表示的。这种变量就称为实例变量，是在类声明的内部但是在类的其他成员方法之外声明的。
继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
方法：类中定义的函数。
```

##### 创建类

```

class Employee(object):
   '所有员工的基类'
   #empCount 类变量，它的值将在这个类的所有实例之间共享。你可以在内部类或外部类使用 Employee.empCount 访问。
   empCount = 0
 
   #构造函数
   #self 代表类的实例，self 在定义类的方法时是必须有的
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
      
   #成员函数
   def displayCount(self):
     print("Total Employee %d" % Employee.empCount)
     
   #成员函数
   def displayEmployee(self):
      print("Name : ", self.name,  ", Salary: ", self.salary)
      

```



##### 创建实例对象

```
#实例化类其他编程语言中一般用关键字 new，但是在 Python 中并没有这个关键字，类的实例化类似函数调用方式。
#以下使用类的名称 Employee 来实例化，并通过 __init__ 方法接收参数。

"创建 Employee 类的第一个对象"
emp1 = Employee("Zara", 2000)
"创建 Employee 类的第二个对象"
emp2 = Employee("Manni", 5000)

```





##### 访问属性

```
#您可以使用点号 . 来访问对象的属性。使用如下类的名称访问类变量:

emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empCount)


# 添加，删除，修改类的属性

emp1.age = 7  # 添加一个 'age' 属性
emp1.age = 8  # 修改 'age' 属性
del emp1.age  # 删除 'age' 属性


可以使用以下函数的方式来访问属性：

getattr(obj, name[, default]); 访问对象的属性。
hasattr(obj,name); 检查是否存在一个属性。
setattr(obj,name,value); 设置一个属性。如果属性不存在，会创建一个新属性。
delattr(obj, name);删除属性。

hasattr(emp1, 'age')    # 如果存在 'age' 属性返回 True。
getattr(emp1, 'age')    # 返回 'age' 属性的值
setattr(emp1, 'age', 8) # 添加属性 'age' 值为 8
delattr(emp1, 'age')    # 删除属性 'age'


```



##### Python内置类属性

```
__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
__doc__ :类的文档字符串
__name__: 类名
__module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
__bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）


print("Employee.__doc__:"), Employee.__doc__
print("Employee.__name__:"), Employee.__name__
print("Employee.__module__:"), Employee.__module__
print("Employee.__bases__:"), Employee.__bases__
print("Employee.__dict__:"), Employee.__dict__
```



##### python对象销毁(垃圾回收)



```
Python 使用了引用计数这一简单技术来跟踪和回收垃圾。在 Python 内部记录着所有使用中的对象各有多少引用。一个内部跟踪变量，称为一个引用计数器。当对象被创建时， 就创建了一个引用计数， 当这个对象不再需要时， 也就是说， 这个对象的引用计数变为0 时， 它被垃圾回收。但是回收不是"立即"的， 由解释器在适当的时机，将垃圾对象占用的内存空间回收。

a = 40      # 创建对象  <40>
b = a       # 增加引用， <40> 的计数
c = [b]     # 增加引用.  <40> 的计数

del a       # 减少引用 <40> 的计数
b = 100     # 减少引用 <40> 的计数
c[0] = -1   # 减少引用 <40> 的计数

垃圾回收机制不仅针对引用计数为0的对象，同样也可以处理循环引用的情况。循环引用指的是，两个对象相互引用，但是没有其他变量引用他们。这种情况下，仅使用引用计数是不够的。Python 的垃圾收集器实际上是一个引用计数器和一个循环垃圾收集器。作为引用计数的补充， 垃圾收集器也会留心被分配的总量很大（及未通过引用计数销毁的那些）的对象。 在这种情况下， 解释器会暂停下来， 试图清理所有未引用的循环。


class Point:
   def __init__( self, x=0, y=0):
      self.x = x
      self.y = y
   def __del__(self):
      class_name = self.__class__.__name__
      print(class_name, "销毁")
 
pt1 = Point()
pt2 = pt1
pt3 = pt1
print(id(pt1), id(pt2), id(pt3)) # 打印对象的id
del pt1
del pt2
del pt3
```



##### 继承

```
面向对象的编程带来的主要好处之一是代码的重用，实现这种重用的方法之一是通过继承机制。通过继承创建的新类称为子类或派生类，被继承的类称为基类、父类或超类

class 派生类名(基类名)
    pass

class SubClassName (ParentClass1[, ParentClass2, ...]):
    pass
 
 class Parent:        # 定义父类
   parentAttr = 100
   def __init__(self):
      print("调用父类构造函数")
 
   def parentMethod(self):
      print('调用父类方法')
 
   def setAttr(self, attr):
      Parent.parentAttr = attr
 
   def getAttr(self):
      print("父类属性 :", Parent.parentAttr)
 
class Child(Parent): # 定义子类
   def __init__(self):
      print("调用子类构造方法")
 
   def childMethod(self):
      print('调用子类方法')
 
c = Child()          # 实例化子类
c.childMethod()      # 调用子类的方法
c.parentMethod()     # 调用父类方法
c.setAttr(200)       # 再次调用父类的方法 - 设置属性值
c.getAttr()          # 再次调用父类的方法 - 获取属性值


你可以使用issubclass()或者isinstance()方法来检测。

issubclass() - 布尔函数判断一个类是另一个类的子类或者子孙类，语法：issubclass(sub,sup)
isinstance(obj, Class) 布尔函数如果obj是Class类的实例对象或者是一个Class子类的实例对象则返回true。

```



##### 重载

```
class Parent:        # 定义父类
   def myMethod(self):
      print('调用父类方法')
 
class Child(Parent): # 定义子类
   def myMethod(self):
      print('调用子类方法')
 
c = Child()          # 子类实例
c.myMethod()  

常见的重载函数
1 __init__ ( self [,args...] )
构造函数
简单的调用方法: obj = className(args)
2	__del__( self )
析构方法, 删除一个对象
简单的调用方法 : del obj
3	__repr__( self )
转化为供解释器读取的形式
简单的调用方法 : repr(obj)
4	__str__( self )
用于将值转化为适于人阅读的形式
简单的调用方法 : str(obj)
5	__cmp__ ( self, x )
对象比较
简单的调用方法 : cmp(obj, x)


class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b
 
   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   
   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)
 
v1 = Vector(2,10)
v2 = Vector(5,-2)
print v1 + v2
```



##### 类属性与方法

```
类的私有属性
__private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。

类的方法
在类的内部，使用 def 关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数 self,且为第一个参数

类的私有方法
__private_method：两个下划线开头，声明该方法为私有方法，不能在类的外部调用。在类的内部调用 self.__private_methods

class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0    # 公开变量
 
    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)
 
counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
print(counter.__secretCount)  # 报错，实例不能访问私有变量

Python不允许实例化的类访问私有数据，但你可以使用 object._className__attrName（ 对象名._类名__私有属性名 ）访问属性，参考以下实例：

class ClassName:
    __site = "this is private"

pp = ClassName()
print(pp._ClassName__site)

class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
        
单下划线、双下划线、头尾双下划线说明：
__foo__: 定义的是特殊方法，一般是系统定义名字 ，类似 __init__() 之类的。

_foo: 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module import *

__foo: 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了。

```



##### 枚举类

```
from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

取值：
Weekday.Tue.value
Weekday(6).value

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
```





### 错误与异常

##### 错误

```
语法错误: 格式引起，不符合Python解析。
```



##### 系统异常

```]
即使语句或表达式在语法上是正确的，但在尝试执行时，它仍可能会引发错误。
```



##### 异常处理

```
try 
 pass
except 
 pass
except
 raise
else

finally

try 语句的工作原理如下。
首先，执行 try 子句 （try 和 except 关键字之间的（多行）语句）。
如果没有异常发生，则跳过 except 子句 并完成 try 语句的执行。
如果在执行try 子句时发生了异常，则跳过该子句中剩下的部分。然后，如果异常的类型和 except 关键字后面的异常匹配，则执行 except 子句 ，然后继续执行 try 语句之后的代码。
如果发生的异常和 except 子句中指定的异常不匹配，则将其传递到外部的 try 语句中；如果没有找到处理程序，则它是一个 未处理异常，执行将停止并显示如上所示的消息。
一个 try 语句可能有多个 except 子句，以指定不同异常的处理程序。 最多会执行一个处理程序。 处理程序只处理相应的 try 子句中发生的异常，而不处理同一 try 语句内其他处理程序中的异常。

finally 在异常抛出前执行
```



##### 参考

```
https://docs.python.org/zh-cn/3.7/tutorial/errors.html
https://docs.python.org/zh-cn/3.7/library/exceptions.html
https://www.programiz.com/python-programming/exceptions
```



