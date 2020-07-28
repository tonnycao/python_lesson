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
from collections import Iterable
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



##### 列表生成器generator

```python

```



##### 迭代器

```python

```



### 函数式编程

##### 高阶函数

##### 返回函数

##### 匿名函数

##### 装饰器



### 作业

- 利用切片操作，实现一个trim()函数，去除字符串首尾的空格。
- 利用datetime，实现一个friend_datetime函数，类似Mac中文件时间显示，比如Today at 3:00 PM，刚刚，几秒前，几分钟前。

