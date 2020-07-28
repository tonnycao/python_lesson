### 高级特性

##### 切片Slice

```python
#取一个list或tuple的部分元素

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

t1 = [L[0], L[1], L[2]]
t2 = L[0:2]

t3 = []
n = 3

for i in range(n):
     t3.append(L[i])

t4 = L[:3]

a = L[1:3]
a2 = L[-2:]
a3 = L[-2:-1]


T = list(range(100))
s1 = T[10:20]
s2 = T[:10:2]
s3 = T[::5]

n = (0, 1, 2, 3, 4, 5)[:3]
s = 'ABCDEFG'[:3]
```



##### 迭代Iteration

```python
#可以通过for循环来遍历对象，这种遍历我们称为迭代（Iteration）。
#集合可以迭代
from collections.abc import Iterable
isinstance(obj, Iterable) # obj 是否可迭代

for i, value in enumerate(['A', 'B', 'C']):
...     print(i, value)
```



##### 列表生成式

```python
#列表生成式即List Comprehensions
list(range(1, 11))

L = []
for x in range(1, 11):
    L.append(x * x)
    
[x * x for x in range(1, 11)]

[x * x for x in range(1, 11) if x % 2 == 0]

[m + n for m in 'ABC' for n in 'XYZ']

import os
[d for d in os.listdir('.')]


d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
    print(k, '=', v)

[x if x % 2 == 0 else -x for x in range(1, 11)]

L = ['Hello', 'World', 'IBM', 'Apple']
[s.lower() for s in L]
```



##### 生成器 Generator

```python
#Generator 是一个用于创建迭代器的简单而强大的工具。 它们的写法类似标准的函数，但当它们要返回数据时会使用 yield 语句。 每次对生成器调用 next() 时，它会从上次离开位置恢复执行（它会记住上次执行语句时的所有数据值）。好处是一边循环一边计算，节省大量的空间。

# 1. yield 定义 
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
for char in reverse('golf'):
    print(char)
    
# 2. 列表生成式的[]改成()
g = (x * x for x in range(10))
next(g)
for n in g:
    print(n)
    
# Fibonacci
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
next(fib)
```



##### 迭代器 Iterator

```python
#一类是集合数据类型，如list、tuple、dict、set、str等；一类是generator，包括生成器和带yield的generator function。这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。

from collections.abc import Iterable
from collections.abc import Iterator
isinstance([], Iterable)
isinstance({}, Iterable)
isinstance('abc', Iterable)
isinstance((x for x in range(10)), Iterable)
isinstance(100, Iterable)

#把list、dict、str等Iterable变成Iterator可以使用iter()函数。

for x in [1, 2, 3, 4, 5]:
    pass

it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
```



### 函数式编程

##### 高阶函数

```python
# map 接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
from functools import reduce

def f(x):
    return x * x
  
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
list(r)

list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

#reduce 把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算

reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

def fn(x, y):
    return x * 10 + y
 
reduce(fn, [1, 3, 5, 7, 9])

#filter 用于过滤序列, 把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

def is_odd(n):
    return n % 2 == 1

list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))

def not_empty(s):
    return s and s.strip()

list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))

#sorted 

sorted([36, 5, -12, 9, -21])
sorted([36, 5, -12, 9, -21], key=abs)
sorted(['bob', 'about', 'Zoo', 'Credit'])
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
```



##### 返回函数

```python
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax
    
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
    
f = lazy_sum(1, 3, 5, 7, 9)
f()
```



##### 装饰器 Decorator

```python

# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
import functools

def now():
   print('2020-7-28')
f = now
f()

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
  

def log(func):
   @functools.wraps(func)
   def wrapper(*args, **kw):
       print('call %s():' % func.__name__)
       return func(*args, **kw)
   return wrapper
  
@log
def now():
    print('2020-7-28')



```





### 作业

- 利用切片操作，实现一个trim()函数，去除字符串首尾的空格。
- 利用datetime，实现一个friend_datetime函数，类似Mac中文件时间显示，比如Today at 3:00 PM，刚刚，几秒前，几分钟前。
- 使用生成器实现杨辉三角。

