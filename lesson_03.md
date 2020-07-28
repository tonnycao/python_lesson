#### IO编程 ####

- 概述

  ```
  在计算机中，IO是Input/Output的简写，也就是输入和输出。
  IO编程中，Stream（流）是一个很重要的概念，可以把流想象成一个水管，数据就是水管里的水，但是只能单向流动。Input Stream就是数据从外面（磁盘、网络）流进内存，Output Stream就是数据从内存流到外面去。对于浏览网页来说，浏览器和服务器之间至少需要建立两根水管，才可以既能发数据，又能收数据。程序和运行时数据是在内存中驻留，由CPU这个超快的计算核心来执行，涉及到数据交换的地方，通常是磁盘、网络等，就需要IO接口。
  ```

  

- 文件操作

  ```
  读文件
  
  f = open('/Users/michael/test.txt', 'r')
  f = open('/Users/michael/test.jpg', 'rb')
  f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
  f.read()
  
  for line in f.readlines():
      print(line.strip())
      
  大文件读取
  bigfile = open('bigfilename','r')
  tmp_lines = bigfile.readlines(BUF_SIZE)
  while tmp_lines:
      process([line for line in tmp_lines])
      tmp_lines = bigfile.readlines(BUF_SIZE)
  
  写文件
  with open('/Users/michael/test.txt', 'w') as f:
      f.write('Hello, world!')
  ```

  

- 目录

  ```
  目录的新建 重命名 移动 删除 路径 
  os 模块的使用
  import os
  os.name # 操作系统类型
  os.uname()
  os.environ
  os.environ.get('PATH')
  os.path.abspath('.') # 查看当前目录的绝对路径
  ```

  

- StringIO和BytesIO

  ```
  StringIO 内存中读写字符串
  from io import StringIO
  f = StringIO()
  f.write('hello')
  f.getvalue()
  
  f = StringIO('Hello!\nHi!\nGoodbye!')
  while True:
       s = f.readline()
       if s == '':
           break
       print(s.strip())
  
  BytesIO 读写字节也就是二进制数据
  
  from io import BytesIO
  f = BytesIO()
  f.write('中文'.encode('utf-8'))
  
  f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
  f.read()
  ```

  

- 序列化

  ```
  我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening，都是一个意思。
  
  pickle
  
  pickle.dumps() 序列化bytes
  
  import pickle
  d = dict(name='Bob', age=20, score=88)
  pickle.dumps(d)
  
  
  pickle.load() 反序列化
  
  f = open('dump.txt', 'wb')
  pickle.dump(d, f)
  f.close()
  
  
  
  JSON
  
  JSON类型	Python类型
  {}	dict
  []	list
  "string"	str
  1234.56	 int或float
  true/false	True/False
  null	None
  
  
  import json
  d = dict(name='Bob', age=20, score=88)
  json.dumps(d)
  
  json_str = '{"age": 20, "score": 88, "name": "Bob"}'
  json.loads(json_str)
  ```

  

  

#### 作业 ####

- 使用os模块实现 shell ls命令
- 文件读取

- 序列化

  ```
  obj = dict(name='曹建', age=30)
  ```

  

