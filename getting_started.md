## Getting Started

### 基础知识


#### 什么是编程
     a tool (written instructions) you use to tell the computer what to do
##### 1. 简介
##### 2. 前端 VS 后端
      客户端 client iOS程序 安卓程序 window程序 Mac客户端
      服务端 sever 电脑用来对外提供服务 服务器
      前端: html css javascript swift c#
      后端: shell python php java go rust c/c++
      全栈: 前端+后端


  
##### 3. 前端语言
    abstraction 抽象
    data structure 数据结构
        string
        number
        array
        object or dictionary
    flow control 流程
        if 
        if / else
        while /for
    HTML
    CSS: 
    JavaScript
    
    更多
    https://developer.mozilla.org/en-US/docs/Web/HTML
    https://developer.mozilla.org/en-US/docs/Web/CSS
    https://developer.mozilla.org/en-US/docs/Web/JavaScript

##### 4. 后端语言
     Python
     PHP
     Ruby
     JavaScript
     Go
     Java
     C++
     C#
     
     更多
     https://www.python.org/
     https://www.ruby-lang.org/en/
     http://www.php.net/
     https://nodejs.org/en/
     https://golang.org/

#### 编程语言选择
     Python 算法 数据处理 web应用
     Java 分布式系统 大数据 流式计算
     Go 高并发应用 微服务
     C/C++ 操作系统 嵌入式 高性能服务
     PHP web应用 服务器脚本

####  Python是如何运行的
      基于c语言实现，CPython
      编译compiler -> 解释 tokenizer -> 解析parser -> pyc文件 生成字节码文件 -> 运行 run



### 术语
##### 1. HTTP网络请求
      经历了域名解析、TCP的三次握手、建立TCP连接后发起HTTP请求、服务器响应HTTP请求、浏览器解析html代码，同时请求html代码中的资源（如js、css、图片等）、最后浏览器对页面进行渲染并呈现给用户。
      1. 域名解析
      2. TCP的三次握手
      3. HTTP请求
      4. 浏览器解析html,css,js代码，并请求html代码中的资源
##### 2. 内存
      Memory内存储器和主存储器，其作用是用于暂时存放CPU中的运算数据，以及与硬盘等外部存储器交换的数据。只要计算机在运行中，操作系统就会把需要运算的数据从内存调到CPU中进行运算，当运算完成后CPU再将结果传送出来，内存的运行也决定了计算机的稳定运行。
##### 3. 堆栈
      堆栈是一种数据结构。堆栈都是一种数据项按序排列的数据结构，只能在一端(称为栈顶(top))对数据项进行插入和删除。在单片机应用中，堆栈是个特殊的存储区，主要功能是暂时存放数据和地址，通常用来保护断点和现场。
      堆（stock）:操作系统自动分配释放，存放函数的参数值，局部变量的值等.堆可以被看成是一棵树，如：堆排序。堆是向高地址扩展的数据结构，是不连续的内存区域。栈是向低地址扩展的数据结构，是一块连续的内存的区域。栈顶的地址和栈的最大容量是系统预先规定好的。
      栈（heap）:一般由程序员分配释放， 若程序员不释放，程序结束时可能由OS（操作系统）回收.一种先进后出的数据结构。
##### 4. 套接字 Socket
      Socket(套接字)可以看成是两个网络应用程序进行通信时，各自通信连接中的端点，这是一个逻辑上的概念。它是网络环境中进程间通信的API(应用程序编程接口)，也是可以被命名和寻址的通信端点，使用中的每一个套接字都有其类型和一个与之相连进程。
      (1)服务器监听。
      (2)客户端请求。
      (3)连接确认。 
##### 5. 抓包
      packet capture：将网络传输发送与接收的数据包进行截获、重发、编辑、转存等操作，也用来检查网络安全。抓包也经常被用来进行数据截取等。
     数据在网络上是以很小的称为帧（Frame）的单位传输的，帧由几部分组成，不同的部分执行不同的功能。帧通过特定的称为网络驱动程序的软件进行成型，然后通过网卡发送到网线上，通过网线到达它们的目的机器，在目的机器的一端执行相反的过程。接收端机器的以太网卡捕获到这些帧，并告诉操作系统帧已到达，然后对其进行存储。就是在这个传输和接收的过程中，嗅探器会带来安全方面的问题。
     工具：wireshark，Fiddler，Sniffer，postman。
##### 6. 环境变量
      environment variables：给系统或用户应用程序设置的一些参数，具体起什么作用这当然和具体的环境变量相关。
      Linux：/etc/profile， .bashrc。profile文件和.bashrc文件的区别：两个profile都只在系统启动时被读取一次，而.bashrc在系统启动和每次调用shell的时候都要被读取。

##### 7. 进程/线程/协程

      进程Process：计算机中的程序关于某数据集合上的一次运行活动，是系统进行资源分配和调度的基本单位，是操作系统结构的基础。程序是指令、数据及其组织形式的描述，进程是程序的实体。  
      第一，进程是一个实体。每一个进程都有它自己的地址空间，包括文本区域（text region）、数据区域（data region）和堆栈（stack region）。文本区域存储处理器执行的代码；数据区域存储变量和进程执行期间使用的动态分配的内存；堆栈区域存储着活动过程调用的指令和本地变量。第二，进程是一个“执行中的程序”。程序是一个没有生命的实体，只有处理器赋予程序生命时（操作系统执行之），它才能成为一个活动的实体，我们称其为进程。就绪状态（Ready），运行状态(Running)，阻塞状态(Blocked)。  
     线程thread：操作系统能够进行运算调度的最小单位。它被包含在进程之中，是进程中的实际运作单位。一条线程指的是进程中一个单一顺序的控制流，一个进程中可以并发多个线程，每条线程并行执行不同的任务。  
     线程的基本操作：
     派生：线程在进程内派生出来，它即可由进程派生，也可由线程派生。  
     阻塞（Block）：如果一个线程在执行过程中需要等待某个事件发生，则被阻塞。  
     激活（unblock）：如果阻塞线程的事件发生，则该线程被激活并进入就绪队列。  
     调度（schedule）：选择一个就绪线程进入执行状态。  
     结束（Finish）：如果一个线程执行结束，它的寄存器上下文以及堆栈内容等将被释放。  
     协程coroutine：


### 方向
#### 1. 数据分析
     sql
     excel 
     python
     工具：powner bi, tablue
#### 2. 运维
     服务器脚本与shell混合使用
#### 3. web
     flask
     djange
     fastapi
### 环境搭建 Setup
#### Python不同环境安装
     windows mac linux
#### 编辑器
     pycharm
#### Git 版本控制
#### Github 代码管理



