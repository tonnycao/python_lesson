#### 流程控制 ###

- if else

  ```python
  python 中非0就是True，None 和 0 都是False

  if test expression:
      Body of if
  else:
      Body of else
      
      
  if test expression:
      Body of if
  elif test expression:
      Body of elif
  else: 
      Body of else
      
      
   num = 3.4
  
    if num > 0:
        print("Positive number")
    elif num == 0:
        print("Zero")
    else:
        print("Negative number")
  
  ```

 

- for

  ```python

for val in sequence:
  	Body of for

  numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

  sum = 0
  for val in numbers:
  	sum = sum+val
  print("The sum is", sum)

  range()

  print(range(10))

  print(list(range(10)))

  print(list(range(2, 8)))

  print(list(range(2, 20, 3)))

  [2, 5, 8, 11, 14, 17]

  genre = ['pop', 'rock', 'jazz']
  for i in range(len(genre)):
  	print("I like", genre[i])
  	
  	
  digits = [0, 1, 5]

  for i in digits:
      print(i)
  else:
      print("No items left.")

  IteralStop

  student_name = 'Soyuj'

  marks = {'James': 90, 'Jules': 55, 'Arthur': 77}

  for student in marks:
      if student == student_name:
          print(marks[student])
          break
  else:
      print('No entry with that name found.')


  ```
- while

  ```python
while test_expression:
      Body of while

  n = 10
  sum = 0
  i = 1

  while i <= n:
      sum = sum + i
      i = i+1 

  print("The sum is", sum)



  counter = 0

  while counter < 3:
      print("Inside loop")
      counter = counter + 1
  else:
      print("Inside else")



  ```
- break and continue

  ```python


//在for while 循环中使用

  //break 退出循环体
 // 当 break 将控制流传出一个带有 finally 子句的 try 语句时，该 finally 子句会先被执行然后再真正离开该循环

 // continue 退出本地循环，继续下次循环
 // 当 continue 将控制流传出一个带有 finally 子句的 try 语句时，该 finally 子句会先被执行然后再真正开始循环的下一个轮次。

  for val in "string":
      if val == "i":
          break
      print(val)

  print("The end")



  for val in "string":
      if val == "i":
          continue
      print(val)

  print("The end")


  ```
- pass

  ```python

 //不做任何操作，占位符，以后可能需要做处理

  sequence = {'p', 'a', 's', 's'}
  for val in sequence:
      pass

  def function(args):
      pass



  ```
- with

  ```python

 with 语句用于包装带有使用上下文管理器,定义的方法的代码块的执行。 这允许对普通的 try...except...finally 使用模式进行封装以方便地重用。

  带有一个 with 语句的执行过程如下:

  对上下文表达式 (在 with_item 中给出的表达式) 求值以获得一个上下文管理器。
  载入上下文管理器的 enter() 以便后续使用。
  载入上下文管理器的 exit() 以便后续使用。
  发起调用上下文管理器的 enter() 方法。
  如果 with 语句中包含一个目标，来自 enter() 的返回值将被赋值给它。

  上下文管理器 是一个对象，它定义了在执行 with 语句时要建立的运行时上下文。 上下文管理器处理进入和退出所需运行时上下文以执行代码块。 通常使用 with 语句，但是也可以通过直接调用它们的方法来使用。

  上下文管理器的典型用法包括保存和恢复各种全局状态，锁定和解锁资源，关闭打开的文件等等。



  ```
 #### 函数 ####

- 定义

  ```python
def function_name(parameters):
  	   """docstring"""
  	   pass


  ```
- 参数

  ```python

 常规传参
  def enroll(name, gender):
      print('name:', name)
      print('gender:', gender)
      
  可变参数问题

  可变变量 list dict set
  不可变变量 tuple int string float

  def add_end(L=[]):
      L.append('END')
      return L
       
  默认参数
  def greet(name, msg="Good morning!"):
      """
      This function greets to
      the person with the
      provided message.
      If the message is not provided,
      it defaults to "Good
      morning!"
      """

			print("Hello", name + ', ' + msg)
     
  greet("Kate")
  greet("Bruce", "How do you do?")

  可变参数 tuple
  def greet(*names):
      """This function greets all
      the person in the names tuple."""

    # names is a tuple with arguments
    for name in names:
        print("Hello", name)
  
  greet("Monica", "Luke", "Steve", "John")

  关键字参数
  def person(name, age, kw):
      print('name:', name, 'age:', age, 'other:', kw)
      
  def zidian(kwargs):
      print(kwargs)

  zidian(a=1,b=2,c=3)
  zidian(a=1,b=2,c=3,d=4)

  {'a': 1, 'b': 2, 'c': 3}
  {'a': 1, 'b': 2, 'c': 3, 'd': 4}

  ```
 

- 递归

  ```python

 //最大的递归深度 1000，超过会引起 RecursionError

  def recursor():
      recursor()
  recursor()

  def factorial(x):
      """This is a recursive function
      to find the factorial of an integer"""


  if x == 1:
      return 1
  else:
      return (x * factorial(x-1))
    
  num = 3
  print("The factorial of", num, "is", factorial(num))
  ```
 

- 匿名函数

  ```python

lambda [arg1 [,arg2, ... argN]] : expression

  double = lambda x: x * 2
  print(double(5))

  filter()
  my_list = [1, 5, 4, 6, 8, 11, 3, 12]
  new_list = list(filter(lambda x: (x%2 == 0) , my_list))
  print(new_list)

  map()
  my_list = [1, 5, 4, 6, 8, 11, 3, 12]
  new_list = list(map(lambda x: x * 2 , my_list))
  print(new_list)



  ```
- 全局参数与局部参数

  ```python
局部变量

  x = "global"

  def foo():
      x = x * 2
      print(x)

  foo()

  def foo():
      y = "local"

  foo()
  print(y)

  全局变量
  x = "global "

  def foo():
      global x
      y = "local"
      x = x * 2
      print(x)
      print(y)

  foo()


 Nonlocal 变量

  语句会使得所列出的名称指向之前在最近的包含作用域中绑定的除全局变量以外的变量。 绑定的默认行为是先搜索局部命名空间。 这个语句允许被封装的代码重新绑定局部作用域以外且非全局（模块）作用域当中的变量。

  def outer():
      x = "local"

  def inner():
      nonlocal x
      x = "nonlocal"
      print("inner:", x)

  inner()
  print("outer:", x)
  
  outer()
  ```
  

- 模块

  ```python
 一般情况下一个python文件就是一个模块

  引用模块
  import foo              # foo imported and bound locally
  import foo.bar.baz      # foo.bar.baz imported, foo bound locally
  import foo.bar.baz as fbb # foo.bar.baz imported and bound as fbb
  from foo.bar import baz  # foo.bar.baz imported and bound as baz
  from foo import attr    # foo imported and foo.attr bound as attr
  from foo imort *

  如果标识符列表改为一个星号 ('*')，则在模块中定义的全部公有名称都将按 import 语句所在的作用域被绑定到局部命名空间。

  定义模块


!/usr/bin/env python3

-- coding: utf-8 --

  ' a test module '

  author = 'Michael Liao'

  import sys

  def test():
      args = sys.argv
      if len(args)==1:
          print('Hello, world!')
      elif len(args)==2:
          print('Hello, %s!' % args[1])
      else:
          print('Too many arguments!')
          
  def main():
  	pass
  	
  if name=='main':
      main()

  ```
- 包

  ```

目录和模块构成了包。目录中必须包含 init.py和子包或者模块文件。
引用方式
from Game.Level import start
start.select_difficulty(2)

from Game.Level.start import select_difficulty
select_difficulty(2)



  ```


#### 课后作业 ####

- 用匿名函数改造下面函数

```python

  def is_odd(n):
      return n % 2 == 1

  L = list(filter(is_odd, range(1, 20)))

```
- 熟悉常见模块

  ```python
  math datetime collections base64 hashlib hmac itertools XML HTMLParser urllib
  ```
- 定义一个模块 实现网址完整性的校验

