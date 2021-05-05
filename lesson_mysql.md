## MySQL

##### 关系型数据库

```
关系型数据库，是指采用了关系模型来组织数据的数据库，其以行和列的形式存储数据，以便于用户理解，关系型数据库这一系列的行和列被称为表，一组表组成了数据库。用户通过查询来检索数据库中的数据，而查询是一个用于限定数据库中某些区域的执行代码。关系模型可以简单理解为二维表格模型，而一个关系型数据库就是由二维表及其之间的关系组成的一个数据组织。
常见的关系型数据库：MySQL MSSQL Oracle


```

![mysql_architecture](./images/mysql_architecture.png)

##### 存储引擎

```
常见存储引擎
MyISAM: 表锁级，不支持事务，适合读多写少项目。
INNODB：行锁级，支持事务，适合读多写多的项目。

```



##### 语句

![mysql_query](./images/mysql_query.jpg)

##### 事务与索引

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

```sql
FIND_IN_SET(s1,s2)
select FIND_IN_SET(set_field, "ENUM_VALUE") form table_name;

REPLACE(s,s1,s2)
select REPLACE(field_name, "abc", "ABC") form table_name;

SUBSTR(s, start, length)
select SUBSTR(field_name, 1, length(field_name)) form table_name;

TRIM(s)
select TRIM(field_name) as max_id form table_name;

MAX(expression)
select MAX(id) as max_id form table_name;

MIN(expression)
select MIN(id) as min_id form table_name;

SUM()
select sum(field_name) as total form table_name;

COUNT()
select count(*) as total form table_name;
```



##### 性能优化

```
0. 合理的表设计
1. 高效的SQL语句
2. 合理使用索引
3. 合理使用缓存
4. 使用压测工具和分析工具
```

![mysql](./images/mysql.png)



## Python与MySQL  ##

##### pymysql

```python
# 安装
pip3 install PyMySQL
# 实例
import pymysql

# 打开数据库连接
db = pymysql.connect("localhost","root","rootroot","test")
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 使用 execute()  方法执行 SQL 查询 
cursor.execute("SELECT VERSION()")
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
 
print ("Database version : %s " % data)
 
# 关闭数据库连接
db.close()

# mysql 基类
class MySql:
    logfile = LOG_PATH + '/mysql.log'

    def __init__(self, host, user, passwd, port, db, charset, table):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.port = port
        self.db = db
        self.charset = charset
        self.table = table
        self._connect()

    def _connect(self):
        self.connect = pymysql.connect(host=self.host, user=self.user, password=self.passwd, port=self.port, db=self.db,
                                       charset=self.charset)
        self.cursor = self.connect.cursor()

    def get_one_data(self, sql):
        row = None
        try:
            self.cursor.execute(sql)
            row = self.cursor.fetchone()
        except Exception as e:
            file = open(self.logfile, 'a+', encoding='utf8')
            file.write(sql + '\n')
            file.write(str(e) + '\n')
            self.connect.rollback()
        return row

    def query_many_data(self, sql, size=100):
        rows = None
        try:
            self.cursor.execute(sql)
            rows = self.cursor.fetchmany(size)
        except Exception as e:
            file = open(self.logfile, 'a+', encoding='utf8')
            file.write(sql + '\n')
            file.write(str(e) + '\n')
            self.connect.rollback()
        return rows

    def insert_with_id(self, sql):
        last_id = 0
        try:
            if self.cursor.execute(sql):
                self.connect.commit()
                last_id = self.cursor.lastrowid
        except Exception as e:
            file = open(self.logfile, mode='a+', encoding='utf8')
            file.write(sql+'\n')
            file.write(str(e) + '\n')
            self.connect.rollback()
        return last_id

    def update_data(self, sql):
        try:
            if self.cursor.execute(sql):
                self.connect.commit()
        except Exception as e:
            file = open(self.logfile, 'a+', encoding='utf8')
            file.write(sql + '\n')
            file.write(str(e) + '\n')
            self.connect.rollback()

    def close(self):
        self.cursor.close()
        self.connect.close()

        
```

##### SQLAlchemy

```
pip3 install sqlalchemy

sqlalchemy是mysql的ORM

import sqlalchemy
sqlalchemy.__version__

from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:rootroot@localhost:3306/db_example?charset=utf8mb4', pool_recycle=3600)

from sqlalchemy import Column, String, Integer,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()


class City(Base):
    # 表的名字:
    __tablename__ = 'city'

    # 表的结构:
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    population = Column(Integer)
    state = Column(String(255))


DBSession = sessionmaker(bind=engine)


session = DBSession()
# 创建新User对象:
new_one = City(id='10', name='Beijing', population=10, state='Beijin')
# 添加到session:
session.add(new_one)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()
```



#### 参考

* https://dev.mysql.com/doc/refman/8.0/en/optimization.html

* https://z.itpub.net/article/detail/108D0B57B3FCAFCAF8BF3B373469F4EF
* https://pymysql.readthedocs.io/
* https://github.com/PyMySQL/PyMySQL/
* https://docs.sqlalchemy.org/en/14/tutorial/index.html
* https://zhuanlan.zhihu.com/p/27400862
* https://mariadb.com/docs/clients/connector-python/

##### 作业

```
利用sqlalchemy存储这三个文件
https://share.weiyun.com/wO86xTYL
```

