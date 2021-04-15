#### 变量/常量/字面量 ####


##### 变量 #####

- 小写
- 字母数字字符组合（ !, @, #, $, %, etc.）
- 有意义的英文
- 格式 驼峰或者下划线

``` 
number = 10

str_abc = "abc"

string2 = '1234'

articleTitle = None

a, b, c = 5, 3.2, "Hello"

x = y = z = "same"

```



##### 常量 #####

- 大写
- 字母数字字符组合（ !, @, #, $, %, etc.） 
- 有意义的英文  
- 格式 函数和变量 驼峰或者下划线

```
PI = 3.14
GRAVITY = 9.8

const.py


a.py

import const

const.PI


from const import *

PI


```

##### 字面量 #####


- 数值型

```
a = 0b1010 #Binary Literals
b = 100 #Decimal Literal 
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal

#Float Literal
float_1 = 10.5 
float_2 = 1.5e2

#Complex Literal 
x = 3.14j

```


- 字符串类型

```
strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\u00dcnic\u00f6de"
raw_str = r"raw \n string"

sp_string = "Tonny's Mac"
```

- 布尔类型

```
a = True
b = False
```

- 集合

```
fruits = ["apple", "mango", "orange"] #list
numbers = (1, 2, 3) #tuple
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} #dictionary
vowels = {'a', 'e', 'i' , 'o', 'u'} #set
list dict set 可变 tuple 不可
https://docs.python.org/zh-cn/3.7/tutorial/index.html
```

### 数据类型 ###


#### 数字 number ####

- int
- float
- long

#### 字符串 string ####
- string 
#### 布尔类型 boolean ####
- True
- False 

#### 集合类型 ####

- List 数组
- Set 一个无序不重复元素集
- Dictionary 字典{"key":"value"}
- Tuple 不可变的有序数组()

#### 数据类型之间的转换 ####

- 类型判断
```
type(p)

isinstance(p, object)
```

- 整型与字符串

```
int(x [,base ])         将x转换为一个整数  
long(x [,base ])        将x转换为一个长整数  
float(x )               将x转换到一个浮点数   
str(x )                 将对象 x 转换为字符串   
eval(str )              用来计算在字符串中的有效Python表达式,并返回一个对象  
tuple(s )               将序列 s 转换为一个元组  
list(s )                将序列 s 转换为一个列表  
chr(x )                 将一个整数转换为一个字符
```
- 集合之间转换

```
list_num = [1,2,3]

dict_num = {5,6,7}

str = 'python'

set(list_num)

tuple(dict_num)

list(str)

```
- 数学函数math

```
abs(x)	返回数字的绝对值，如abs(-10) 返回 10
ceil(x)	返回数字的上入整数，如math.ceil(4.1) 返回 5
cmp(x, y)	如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1
exp(x)	返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
fabs(x)	返回数字的绝对值，如math.fabs(-10) 返回10.0
floor(x)	返回数字的下舍整数，如math.floor(4.9)返回 4
log(x)	如math.log(math.e)返回1.0,math.log(100,10)返回2.0
log10(x)	返回以10为基数的x的对数，如math.log10(100)返回 2.0
max(x1, x2,...)	返回给定参数的最大值，参数可以为序列。
min(x1, x2,...)	返回给定参数的最小值，参数可以为序列。
modf(x)	返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
pow(x, y)	x**y 运算后的值。
round(x [,n])	返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
sqrt(x)	返回数字x的平方根

decimal(12, 4) 元
int(12) 分

alipay
wxpay int 分
```

#### 中文编码 ####

```
#!/usr/bin/python
# -*- coding: UTF-8 -*-
```
#### 作业 ####

- 判断质数
- 100以内质数之和
- 2进制 8进制 10进制 16进制数字之间的转换
