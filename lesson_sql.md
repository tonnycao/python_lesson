#### Database

```
RDBMS 指关系型数据库管理系统，全称 Relational Database Management System。RDBMS 是 SQL 的基础，同样也是所有现代数据库系统的基础，比如 MS SQL Server、IBM DB2、Oracle、MySQL 以及 Microsoft Access。RDBMS 中的数据存储在被称为表table的数据库对象中。表table是相关的数据项的集合，它由列columns和行rows组成。
```

#### ER **model**

```
帮助用户设计数据库，存储数据，理解表与表之间的关系。用ER图来表示。
```



* Entity实体

  ```
  现实的事物就是实体，是具体的人和物，用名词表示，也可以是抽象的概念，能与其他实体区别。
  
  ```

  

* Attributes属性

  ```
  实体的特点和性质
  ```

  

* Relationships关系

  ```
  实体与实体的关系，一般用动词表示
  
  1对1
  
  1对多
  
  多对多
  ```

  

#### Data Types数据类型

* **Text 类型：**

  ```sql
  CHAR(size)	保存固定长度的字符串（可包含字母、数字以及特殊字符）。在括号中指定字符串的长度。最多 255 个字符。
  VARCHAR(size)	保存可变长度的字符串（可包含字母、数字以及特殊字符）。在括号中指定字符串的最大长度。最多 255 个字符。注释：如果值的长度大于 255，则被转换为 TEXT 类型。
  TINYTEXT	存放最大长度为 255 个字符的字符串。
  TEXT	存放最大长度为 65,535 个字符的字符串。
  BLOB	用于 BLOBs（Binary Large OBjects）。存放最多 65,535 字节的数据。
  MEDIUMTEXT	存放最大长度为 16,777,215 个字符的字符串。
  MEDIUMBLOB	用于 BLOBs（Binary Large OBjects）。存放最多 16,777,215 字节的数据。
  LONGTEXT	存放最大长度为 4,294,967,295 个字符的字符串。
  LONGBLOB	用于 BLOBs (Binary Large OBjects)。存放最多 4,294,967,295 字节的数据。
  ENUM(x,y,z,etc.)	允许您输入可能值的列表。可以在 ENUM 列表中列出最大 65535 个值。如果列表中不存在插入的值，则插入空值。
  注释：这些值是按照您输入的顺序排序的。
  
  可以按照此格式输入可能的值： ENUM('X','Y','Z')
  
  SET	与 ENUM 类似，不同的是，SET 最多只能包含 64 个列表项且 SET 可存储一个以上的选择。
  ```

  

* **Number 类型：**

  ```sql
  TINYINT(size)	带符号-128到127 ，无符号0到255。
  SMALLINT(size)	带符号范围-32768到32767，无符号0到65535, size 默认为 6。
  MEDIUMINT(size)	带符号范围-8388608到8388607，无符号的范围是0到16777215。 size 默认为9
  INT(size)	带符号范围-2147483648到2147483647，无符号的范围是0到4294967295。 size 默认为 11
  BIGINT(size)	带符号的范围是-9223372036854775808到9223372036854775807，无符号的范围是0到18446744073709551615。size 默认为 20
  FLOAT(size,d)	带有浮动小数点的小数字。在 size 参数中规定显示最大位数。在 d 参数中规定小数点右侧的最大位数。
  DOUBLE(size,d)	带有浮动小数点的大数字。在 size 参数中规显示定最大位数。在 d 参数中规定小数点右侧的最大位数。
  DECIMAL(12,4)	作为字符串存储的 DOUBLE 类型，允许固定的小数点。在 size 参数中规定显示最大位数。在 d 参数中规定小数点右侧的最大位数。
  ```

  





* **Date 类型：**

  ```sql
  DATE()	日期。格式：YYYY-MM-DD
  注释：支持的范围是从 '1000-01-01' 到 '9999-12-31'
  
  DATETIME()	*日期和时间的组合。格式：YYYY-MM-DD HH:MM:SS
  注释：支持的范围是从 '1000-01-01 00:00:00' 到 '9999-12-31 23:59:59'
  
  TIMESTAMP()	*时间戳。TIMESTAMP 值使用 Unix 纪元('1970-01-01 00:00:00' UTC) 至今的秒数来存储。格式：YYYY-MM-DD HH:MM:SS
  注释：支持的范围是从 '1970-01-01 00:00:01' UTC 到 '2038-01-09 03:14:07' UTC
  
  TIME()	时间。格式：HH:MM:SS
  注释：支持的范围是从 '-838:59:59' 到 '838:59:59'
  
  YEAR()	2 位或 4 位格式的年。
  注释：4 位格式所允许的值：1901 到 2155。2 位格式所允许的值：70 到 69，表示从 1970 到 2069。
  ```

  

#### SQL（Structured Query Language）

* SQL 让您可以访问和处理数据库，包括数据插入、查询、更新和删除。

  ```sql
  SHOW DATABASES;
  SHOW TABLES;
  SHOW FIELDS FROM table / DESCRIBE table;
  SHOW CREATE TABLE table;
  SHOW PROCESSLIST;
  
  CREATE DATABASE DatabaseName;
  CREATE DATABASE DatabaseName CHARACTER SET utf8mb4;
  USE DatabaseName
  DROP DATABASE DatabaseName;
  ALTER DATABASE DatabaseName CHARACTER SET utf8mb4;
  ```

  

* SQL 面向数据库执行查询。

  ```sql
  CREATE TABLE table (field1 type1, field2 type2, PRIMARY KEY (field1));
  DROP TABLE table;
  DROP TABLE IF EXISTS table;
  
  ALTER TABLE table MODIFY field1 type1
  ALTER TABLE table MODIFY field1 type1 FIRST
  ALTER TABLE table MODIFY field1 type1 AFTER another_field
  
  ALTER TABLE table CHANGE old_name_field1 new_name_field1 type1 FIRST
  
  truncate table_name
  drop table_name
  ```

  

* SQL 可从数据库取回数据。

  ```sql
  SELECT * FROM table;
  SELECT * FROM table1, table2;
  SELECT field1, field2 FROM table1, table2;
  page_size = 10;
  page = 2;
  offset = (page-1)*page_size;
  
  SELECT ... FROM ... WHERE condition order by id desc limit offset, page_size;
  
  ```

  

* SQL 可在数据库中插入新的记录。

  ```
  INSERT INTO table1 (field1, field2) VALUES (value1, value2),(value1, value2),(value1, value2);
  
  INSERT INTO table1 VALUES (value1, value2);
  ```

  

* SQL 可更新数据库中的数据。

  ```sql
  UPDATE table1 SET field1=new_value1 WHERE condition;
  UPDATE table1, table2 SET field1=new_value1, field2=new_value2, ... WHERE
    table1.id1 = table2.id2 AND condition;
  ```

  

* SQL 可从数据库删除记录。

  ```sql
  DELETE FROM table1 / TRUNCATE table1
  DELETE FROM table1 WHERE condition
  DELETE FROM table1, table2 FROM table1, table2 WHERE table1.id1 =
    table2.id2 AND condition
  ```

  

* SQL 可创建新数据库。

  ```sql
  CREATE DATABASE DatabaseName;
  CREATE DATABASE DatabaseName CHARACTER SET utf8mb4;
  ```

  

* SQL 可在数据库中创建新表。

  ```sql
  CREATE TABLE table (field1 type1, field2 type2);
  CREATE TABLE table IF NOT EXISTS;
  CREATE TEMPORARY TABLE table;
  ```





#### Jupyter For MySQL

* install

  ```
  pip install git+https://github.com/shemic/jupyter-mysql-kernel
  ```

  

* config

  ```
  mkdir -p ~/.local/config/
  vi ~/.local/config/mysql_config.json
  
  {
      "user"     : "root",
      "port"     : "3306",
      "host"     : "127.0.0.1",
      "charset"  : "utf8",
      "password" : "123456"
  }
  ```

  

  

#### 参考

* http://c.biancheng.net/view/8264.html

* https://www.guru99.com/er-diagram-tutorial-dbms.html

* https://devhints.io/mysql
* https://dev.mysql.com/doc/refman/8.0/en/
* https://pymysql.readthedocs.io/en/latest/
* https://docs.sqlalchemy.org/en/14/orm/examples.html

