## 错误与异常

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



##### 自定义异常

```

```



##### 参考

```
https://docs.python.org/zh-cn/3.7/tutorial/errors.html
https://docs.python.org/zh-cn/3.7/library/exceptions.html
https://www.programiz.com/python-programming/exceptions
```





## 面向对象

##### 类与实例

```

```

##### 继承

```

```



#####  重载

```

```



##### 多态

```

```



