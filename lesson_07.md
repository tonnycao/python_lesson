#### SQLAlchemy应用

##### SQLAlchemy组成说明

建立在DB-API之上，使用关系对象映射进行数据库操作。将类和对象转换成SQL，然后使用数据API执行SQL并获取执行结果。

- engine，框架的引擎
- connection pooling 数据库连接池
- Dialect 选择链接数据库的DB-API种类（实际选择哪个模块链接数据库mysqldb,pymysql,mysqlconnector）
- Schema/Types 架构和类型
- SQL Expression Language SQL表达式语言

![sqlalchemy_architecture](./images/sqlalchemy_architecture.png)



##### ORM

###### 创建表

- 创建单表

  ```python
  # table.py
  
  from sqlalchemy import create_engine
  from sqlalchemy.ext.declarative import declarative_base
  from sqlalchemy import Column, Integer, String, DateTime
  from sqlalchemy import Index, UniqueConstraint
  import datetime
  
  ENGINE = create_engine("mysql+pymysql://root:rootroot@127.0.0.1:3306/db_example?charset=utf8mb4")
  
  # Base是declarative_base的实例化对象
  Base = declarative_base()
  
  
  # 每个类都要继承Base
  class UserInfo(Base):
      # __tablename__是必须要的，它是设置实际存在数据库中的表名
      __tablename__ = "user_info"
  
      # Column是列的意思，固定写法 Column(字段类型, 参数)
      # primary_key主键、index索引、nullable是否可以为空
      id = Column(Integer, primary_key=True)
      name = Column(String(32), index=True, nullable=False)
      email = Column(String(32), unique=True)
      create_time = Column(DateTime, default=datetime.datetime.now)
  
  
      __table_args__ = (
          UniqueConstraint("id", "name", name="uni_id_name"),
          Index("name", "email")
      )
  
   def create_db():
      # metadata.create_all创建所有表
      Base.metadata.create_all(ENGINE)
  
  def drop_db():
      # metadata.drop_all删除所有表
      Base.metadata.drop_all(ENGINE)
  
  if __name__ == '__main__':
      create_db()
  ```

  

- 创建一对多表

  ```python
  # many_table.py
  
  from sqlalchemy import create_engine
  from sqlalchemy.ext.declarative import declarative_base
  from sqlalchemy import Column, Integer, String, DateTime
  from sqlalchemy import Index, UniqueConstraint, ForeignKey
  from sqlalchemy.orm import relationship
  import datetime
  
  
  ENGINE = create_engine("mysql+pymysql://root:123abc@127.0.0.1:3306/test?charset=utf8mb4",)
  
  Base = declarative_base()
  
  
  # ======一对多示例=======
  class UserInfo(Base):
      __tablename__ = "user_info"
  
      id = Column(Integer, primary_key=True)
      # index=True,设置索引
      name = Column(String(32), index=True, nullable=False)
      email = Column(String(32), unique=True)
      create_time = Column(DateTime, default=datetime.datetime.now)
      # ForeignKey字段的建立,需要指定外键绑定哪个表的哪个字段
      hobby_id = Column(Integer, ForeignKey("hobby.id"))
      # 不生成表结构 方便查询和增加的操作
      # 第一个参数是关联到哪个类(表), backref是给关联的那个类反向查询用的
      hobby = relationship("Hobby", backref="user")
  
      __table_args__ = (
          # UniqueConstraint联合唯一，这个联合唯一的字段名为：uni_id_name
          UniqueConstraint("id", "name", name="uni_id_name"),
          # 联合索引
          Index("name", "email")
      )
  
  
  class Hobby(Base):
      __tablename__ = "hobby"
  
      id = Column(Integer, primary_key=True)
      title = Column(String(32), default="coding")
  
  
  
  
  def create_db():
      Base.metadata.create_all(ENGINE)
  
  
  def drop_db():
      Base.metadata.drop_all(ENGINE)
  
  
  
  if __name__ == '__main__':
      create_db()
  ```

  

- 创建多对多表

  ```python
  # many_to_many.py
  from sqlalchemy import create_engine
  from sqlalchemy.ext.declarative import declarative_base
  from sqlalchemy import Column, Integer, String, DateTime
  from sqlalchemy import Index, UniqueConstraint, ForeignKey
  from sqlalchemy.orm import relationship
  import datetime
  
  
  ENGINE = create_engine("mysql+pymysql://root:rootroot@127.0.0.1:3306/db_example?charset=utf8mb4",)
  
  Base = declarative_base()
  
  
  Entiry-Relation
  
  # ======多对多示例=======
  class Book(Base):
      __tablename__ = "book"
  
      id = Column(Integer, primary_key=True)
      title = Column(String(32))
      # 不生成表字段 仅用于查询和增加方便
      # 多对多的relationship还需要设置额外的参数secondary：绑定多对多的中间表
      tags = relationship("Tag", secondary="book2tag", backref="books")
  
  
  class Tag(Base):
      __tablename__ = "tag"
  
      id = Column(Integer, primary_key=True)
      title = Column(String(32))
  
  
  class Book2Tag(Base):
      __tablename__ = "book2tag"
  
      id = Column(Integer, primary_key=True)
      book_id = Column(Integer, ForeignKey("book.id"))
      tag_id = Column(Integer, ForeignKey("tag.id"))
  
  
  def create_db():
      Base.metadata.create_all(ENGINE)
  
  def drop_db():
      Base.metadata.drop_all(ENGINE)
  
  if __name__ == '__main__':
      create_db()
      # drop_db()
      
  # models_demo.py
  from sqlalchemy import create_engine, ForeignKey, UniqueConstraint, Index
  from sqlalchemy import Column, Integer, String
  from sqlalchemy.ext.declarative import declarative_base
  from sqlalchemy.orm import sessionmaker, scoped_session
  from sqlalchemy.orm import relationship
  from sqlalchemy import Index, UniqueConstraint
  
  conn = create_engine(
      "mysql+pymysql://root:123abc@127.0.0.1:3306/mytest?charset=utf8mb4",
      max_overflow=0,  # 超过连接池大小外最多创建的连接数
      pool_size=5,  # 连接池大小
      pool_timeout=30,  # 连接池中没有线程最多等待时间，否则报错
      pool_recycle=-1,  # 多久之后对连接池中的连接进行回收（重置）-1不回收
  )
  
  Base = declarative_base()
  
  
  class Book(Base):
      __tablename__ = 'book'
  
      id = Column(Integer, primary_key=True)
      title = Column(String(64), nullable=False)
      publisher_id = Column(Integer, ForeignKey('publisher.id'))
      publisher = relationship('Publisher', backref='books')
      tags = relationship('Tag', backref='books', secondary='book2tag')
  
      __table_args__ = (
          # UniqueConstraint联合唯一，这个联合唯一的字段名为：uni_id_name
          UniqueConstraint("id", "title", name="uni_id_title"),
          # 联合索引
          Index("id", "title")
      )
  
      def __repr__(self):
          return self.title
  
  
  class Publisher(Base):
      __tablename__ = 'publisher'
  
      id = Column(Integer, primary_key=True)
      title = Column(String(64), nullable=False)
  
      def __repr__(self):
          return self.title
  
  
  class Tag(Base):
      __tablename__ = 'tag'
  
      id = Column(Integer, primary_key=True)
      title = Column(String(64), nullable=False)
  
      def __repr__(self):
          return self.title
  
  
  class Book2Tag(Base):
      __tablename__ = 'book2tag'
  
      id = Column(Integer, primary_key=True)
      book_id = Column(Integer, ForeignKey('book.id'))
      tag_id = Column(Integer, ForeignKey('tag.id'))
  
  
  def create_db():
      # metadata.create_all创建所有表
      Base.metadata.create_all(conn)
  
  
  def drop_db():
      # metadata.drop_all删除所有表
      Base.metadata.drop_all(conn)
  
  
  # 每次执行数据库操作的时候，都需要创建一个session,相当于管理器(相当于Django的ORM的objects)
  session_factory = sessionmaker(bind=conn)
  # 线程安全，基于本地线程实现每个线程用同一个session
  Session = scoped_session(session_factory)
  # 实例化(相当于实现了一个单例模式)
  session = Session()
  session1 = Session()
  # session2 = Session() --> session is session2
  
  
  # 下面这种情况
  # session_factory = sessionmaker(bind=conn)
  # session3 = session_factory()
  # session4 = session_factory()
  # session3 is not session4
  
  
  if __name__ == '__main__':
      # create_db()
      # drop_db()
  
      # publisher_obj = Publisher(title='xxx出版社')
      # book_obj = Book(title='时间简史', publisher=publisher_obj)
      # tag_obj1 = Tag(title='python')
      # tag_obj2 = Tag(title='go')
      # tag_obj3 = Tag(title='linux')
      # session.add(publisher_obj)
      # session.add(book_obj)
      # session.add_all([tag_obj1, tag_obj2, tag_obj3])
      # session.commit()
      # session.close()
  
      # ret1 = session.query(Tag).filter(Tag.id==1).first()
      # ret2 = session.query(Tag).filter_by(id=2).first()
      # print(ret1)
      # print(ret2)
  
      # session.query(Tag).filter_by(id=2).update({"title": 'golang'})
      # tag_obj = Tag(title='heihei2')
      # tag_obj.books = [session.query(Book).filter_by(id=1).first()]
      # session.add(tag_obj)
      # session.commit()
  
      # book_obj = Book(title='狗屎仔',
      #                 publisher_id=1,
      #                 tags=[session.query(Tag).filter_by(id=1).first(), session.query(Tag).filter_by(id=2).first()])
      # session.add(book_obj)
      # session.commit()
  
      # ret = session.query(Book, Publisher).filter(Book.publisher_id==Publisher.id).all()
      # ret = session.query(Book).join(Publisher).all()
      # ret = session.query(Book).join(Publisher, isouter=True).all()
      ret = session.query(Book).outerjoin(Publisher).all()
      print(ret)
  ```

  

###### 操作表

- 连接 session

  ```python
  
  # 1. scoped_session
  from sqlalchemy import create_engine
  from sqlalchemy.orm import sessionmaker, scoped_session
  from models_demo import Tag
  
  
  ENGINE = create_engine("mysql+pymysql://root:rootroot@127.0.0.1:3306/db_example?charset=utf8mb4",)
  
  # 每次执行数据库操作的时候，都需要创建一个session,相当于管理器(相当于Django的ORM的objects)
  Session = sessionmaker(bind=ENGINE)
  # 线程安全，基于本地线程实现每个线程用同一个session
  session = scoped_session(Session)
  
  
  # =======执行ORM操作==========
  tag_obj = Tag(title="SQLAlchemy")
  # 添加
  session.add(tag_obj)
  # 提交
  session.commit()
  # 关闭session
  session.close()
  ```

  

- 基本操作

  ```python
  # add query update delete
  from sqlalchemy import create_engine
  from sqlalchemy.orm import sessionmaker, scoped_session
  from models_demo import Tag, UserInfo
  import threading
  
  
  ENGINE = create_engine("mysql+pymysql://root:123abc@127.0.0.1:3306/test?charset=utf8mb4",)
  
  Session = sessionmaker(bind=ENGINE)
  
  # 每次执行数据库操作的时候，都需要创建一个session
  session = Session()
  session = scoped_session(Session)
  
  
  # ============添加================
  tag_obj = Tag(title="SQLAlchemy")
  session.add(tag_obj)
  
  # 批量添加
  session.add_all([
      Tag(title="Python"),
      Tag(title="Django"),
  ])
  # 提交
  session.commit()
  # 关闭session
  session.close()
  
  
  # ============基础查询============
  ret = session.query(Tag).all()
  # get(id)
  ret1 = session.query(Tag).get(1)  # 查询Tag表 id=1的记录
  # filter(表达式)
  ret2 = session.query(Tag).filter(Tag.title == "Python").all()
  # filter_by(字段=xx)
  ret3 = session.query(Tag).filter_by(title="Python").all()
  ret4 = session.query(Tag).filter_by(title="Python").first()
  print(ret1, ret2, ret3, ret4)
  
  
  # ============删除===========
  session.query(Tag).filter_by(id=1).delete()
  session.commit()
  
  
  # ===========修改===========
  session.query(Tag).filter_by(id=22).update({Tag.title: "LOL"})
  session.query(Tag).filter_by(id=23).update({"title": "吃鸡"})
  session.query(Tag).filter_by(id=24).update({"title": Tag.title + "~"}, synchronize_session=False)
  # synchronize_session="evaluate" 默认值进行数字加减
  session.commit()
  ```

  

- 常用操作

```python
# 条件查询
ret1 = session.query(Tag).filter_by(id=22).first()
ret2 = session.query(Tag).filter(Tag.id > 1, Tag.title == "LOL").all()
ret3 = session.query(Tag).filter(Tag.id.between(22, 24)).all()
ret4 = session.query(Tag).filter(~Tag.id.in_([22, 24])).first()
from sqlalchemy import and_, or_
ret5 = session.query(Tag).filter(and_(Tag.id > 1, Tag.title == "LOL")).first()
ret6 = session.query(Tag).filter(or_(Tag.id > 1, Tag.title == "LOL")).first()
ret7 = session.query(Tag).filter(or_(
    Tag.id>1,
    and_(Tag.id>3, Tag.title=="LOL")
)).all()

# 通配符
ret8 = session.query(Tag).filter(Tag.title.like("L%")).all()
ret9 = session.query(Tag).filter(~Tag.title.like("L%")).all()

# 限制
ret10 = session.query(Tag).filter(~Tag.title.like("L%")).all()[1:2]

# 排序
ret11 = session.query(Tag).order_by(Tag.id.desc()).all()  # 倒序
ret12 = session.query(Tag).order_by(Tag.id.asc()).all()  # 正序

# 分组
ret13 = session.query(Tag.test).group_by(Tag.test).all()

# 聚合函数
from sqlalchemy.sql import func
ret14 = session.query(
    func.max(Tag.id),
    func.sum(Tag.test),
    func.min(Tag.id)
).group_by(Tag.title).having(func.max(Tag.id > 22)).all()

# 连表
# print(ret15) 得到一个列表套元组 元组里是两个对象
# [(user_obj1, hobby_obj1), (user_obj2, hobby_obj2), ]
ret15 = session.query(UserInfo, Hobby).filter(UserInfo.hobby_id == Hobby.id).all()

# print(ret16) 得到列表里面是前一个对象，join相当于inner join
# [user_obj1, user_obj2, ]
ret16 = session.query(UserInfo).join(Hobby).all()

# 相当于inner join
# for i in ret16:
#     # print(i[0].name, i[1].title)
#     print(i.hobby.title)

# 指定isouter=True相当于left join
ret17 = session.query(Hobby).join(UserInfo, isouter=True).all()
ret17_1 = session.query(UserInfo).join(Hobby, isouter=True).all()

# 或者直接用outerjoin也是相当于left join
ret18 = session.query(Hobby).outerjoin(UserInfo).all()
ret18_1 = session.query(UserInfo).outerjoin(Hobby).all()
print(ret17)
print(ret17_1)
print(ret18)
print(ret18_1)

```

- 基于relationship的ForeignKey

```python
# 添加
user_obj = UserInfo(name="提莫", hobby=Hobby(title="种蘑菇"))
session.add(user_obj)

hobby = Hobby(title="弹奏一曲")
hobby.user = [UserInfo(name="琴女"), UserInfo(name="妹纸")]
# hobby.user = [session.query(UserInfo).filter_by(id=1).first(), ]
session.add(hobby)
session.commit()

# 基于relationship的正向查询
user_obj_1 = session.query(UserInfo).first()
print(user_obj_1.name)
print(user_obj_1.hobby.title)

# 基于relationship的反向查询
hb = session.query(Hobby).first()
print(hb.title)
for i in hb.user:
    print(i.name)

session.close()

```



- 基于relationship的M2M

```python
# 添加
# 直接给中间表添加
book_obj = Book(title="Python源码剖析")
tag_obj = Tag(title="Python")
b2t = Book2Tag(book_id=book_obj.id, tag_id=tag_obj.id)
session.add_all([
    book_obj,
    tag_obj,
    b2t,
])
session.commit()

# 通过反向字段添加
book = Book(title="测试")
book.tags = [Tag(title="测试标签1"), Tag(title="测试标签2")]
# book.tags = [session.query(Tag).filter_by(id=1).first(), ]
session.add(book)
session.commit()

tag = Tag(title="LOL")
tag.books = [Book(title="大龙刷新时间"), Book(title="小龙刷新时间")]
session.add(tag)
session.commit()

# 基于relationship的正向查询
book_obj = session.query(Book).filter_by(id=4).first()
print(book_obj.title)
print(book_obj.tags)
# 基于relationship的反向查询
tag_obj = session.query(Tag).first()
print(tag_obj.title)
print(tag_obj.books)
```



##### 推荐项目结构

- Root 根目录
- ----bin 可执行文件目录 
- ----config 配置文件目录
- ----data 存储输入文件目录（权限读写）
- ----lib 类库文件目录
- ----handle 处理业务目录
- ----tests 测试目录
- ----log 日志文件目录（权限读写）



##### 参考

https://docs.sqlalchemy.org/en/13/orm/tutorial.html

https://docs.python.org/zh-cn/3.7/library/index.html

https://zhuanlan.zhihu.com/p/27400862