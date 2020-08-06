## MySQL

##### 关系型数据库

```
关系型数据库，是指采用了关系模型来组织数据的数据库，其以行和列的形式存储数据，以便于用户理解，关系型数据库这一系列的行和列被称为表，一组表组成了数据库。用户通过查询来检索数据库中的数据，而查询是一个用于限定数据库中某些区域的执行代码。关系模型可以简单理解为二维表格模型，而一个关系型数据库就是由二维表及其之间的关系组成的一个数据组织。
常见的关系型数据库：MySQL MSSQL Oracle


```

![20170928110355446](/Users/panchengxian/sites/python_lesson/20170928110355446.png)

##### 存储引擎

```
常见存储引擎
MyISAM: 表锁级，不支持事务，适合读多写少项目。
INNODB：行锁级，支持事务，适合读多写多的项目。

```



##### 语句

![20170928110411496](/Users/panchengxian/sites/python_lesson/20170928110411496.jpg)

##### 索引

```
MySQL 事务主要用于处理操作量大，复杂度高的数据。
在 MySQL 中只有使用了 Innodb 数据库引擎的数据库或表才支持事务。
事务处理可以用来维护数据库的完整性，保证成批的 SQL 语句要么全部执行，要么全部不执行。事务用来管理 insert,update,delete 语句。
事务是必须满足4个条件（ACID）：：原子性（Atomicity，或称不可分割性）、一致性（Consistency）、隔离性（Isolation，又称独立性）、持久性（Durability）

原子性：一个事务（transaction）中的所有操作，要么全部完成，要么全部不完成，不会结束在中间某个环节。事务在执行过程中发生错误，会被回滚（Rollback）到事务开始前的状态，就像这个事务从来没有执行过一样。

一致性：在事务开始之前和事务结束以后，数据库的完整性没有被破坏。这表示写入的资料必须完全符合所有的预设规则，这包含资料的精确度、串联性以及后续数据库可以自发性地完成预定的工作。

隔离性：数据库允许多个并发事务同时对其数据进行读写和修改的能力，隔离性可以防止多个事务并发执行时由于交叉执行而导致数据的不一致。事务隔离分为不同级别，包括读未提交（Read uncommitted）、读提交（read committed）、可重复读（repeatable read）和串行化（Serializable）。

持久性：事务处理结束后，对数据的修改就是永久的，即便系统故障也不会丢失。

在 MySQL 命令行的默认设置下，事务都是自动提交的，即执行 SQL 语句后就会马上执行 COMMIT 操作。因此要显式地开启一个事务务须使用命令 BEGIN 或 START TRANSACTION，或者执行命令 SET AUTOCOMMIT=0，用来禁止使用当前会话的自动提交。


MYSQL 事务处理主要有两种方法：
1、用 BEGIN, ROLLBACK, COMMIT来实现

BEGIN 开始一个事务
ROLLBACK 事务回滚
COMMIT 事务确认
2、直接用 SET 来改变 MySQL 的自动提交模式:

SET AUTOCOMMIT=0 禁止自动提交
SET AUTOCOMMIT=1 开启自动提交

普通索引（辅助索引）
CREATE INDEX indexName ON mytable(username); 
ALTER table tableName ADD INDEX indexName(columnName);
CREATE TABLE mytable(
ID INT NOT NULL,
username VARCHAR(16) NOT NULL,
INDEX [indexName] (username(length))  
);  
DROP INDEX [indexName] ON mytable; 


唯一索引（辅助索引）
CREATE UNIQUE INDEX indexName ON mytable(username(length)); 
ALTER table mytable ADD UNIQUE [indexName] (username(length));
CREATE TABLE mytable(
ID INT NOT NULL,
username VARCHAR(16) NOT NULL,
UNIQUE [indexName] (username(length)) 
);  

组合索引（辅助索引）
CREATE INDEX idx_name ON mytable(username,age); 


主键索引 primary key
```



##### 函数

```
FIND_IN_SET(s1,s2)
REPLACE(s,s1,s2)
SUBSTR(s, start, length)
TRIM(s)
MAX(expression)
MIN(expression)
SUM()
COUNT()
```



##### 性能优化

```
0. 合理的表设计
1. 高效的SQL语句
2. 合理使用索引
3. 合理使用缓存
4. 使用压测工具和分析工具
```

![1680d23c8e041b32](/Users/panchengxian/sites/python_lesson/1680d23c8e041b32.png)



## SQLAlchemy  ##



