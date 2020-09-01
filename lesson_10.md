#### Flask 进阶

##### 包形式的项目

- 目录结构

  ```python
  config.py #配置模块
  requirements.txt #依赖库列表
  run.py #入口文件
  instance/ #实例配置 版本环境无关
      config.py
  yourapp/ #应用目录
      __init__.py #包标记 项目初始化
      views.py #路由模块
      models.py #数据库模型
      forms.py #表单模块
      static/ #css js image静态资源目录
      templates/ #模版目录
  ```

  

- 项目配置

  ```python
  # 1.简单模式
  
  #环境变量
  app.config.from_object(os.environ['APP_SETTINGS'])
  #类文件
  app.config.from_object('config')
  #文件
  app = Flask(__name__, instance_relative_config=True)
  app.config.from_pyfile('config.py')
  app.config.from_object(os.environ['APP_SETTINGS'])
  
  export APP_SETTINGS=config.DevelopmentConfig
  
  
  # 2.模块方式
  
  config/default.py #默认每种环境都加载
  config/development.py #开发环境
  config/production.py #生产环境
  config/staging.py #演示环境
  
  app = Flask(__name__, instance_relative_config=True)
  
  app.config.from_object('config.default')
  app.config.from_pyfile('config.py')
  app.config.from_envvar('APP_CONFIG_FILE')
  
  export APP_CONFIG_FILE=/var/www/yourapp/config/production.py
  ```


- 表单

  ```python
  #1. 安装与配置
  #WTForms的flask扩展
  pip3 install Flask-WTF
  pip3 install email-validator
  #生成SECRET_KEY
  os.urandom(24)
  WTF_CSRF_ENABLED = True
  WTF_CSRF_SECRET_KEY = "secret"
  SECRET_KEY
  (CSRF跨域站点保护: Cross-site request forgery)
  
  #2. 简单应用
  
  from flask_wtf import FlaskForm
  from wtforms import StringField, BooleanField
  from wtforms.validators import DataRequired
  
  class UserNamePasswordForm(FlaskForm):
      username = StringField('Username', validators=[DataRequired()])
      password = PasswordField('Password', validators=[DataRequired()])
      
  class LoginForm(Form):
      openid = StringField('openid', validators=[DataRequired()])
      remember_me = BooleanField('remember_me', default=False)
      
      
  #3. 表单模版
  
  <!-- extend from base layout -->
  {% extends "base.html" %}
  
  {% block content %}
  <h1>Sign In</h1>
  <form action="" method="post" name="login">
      {{form.hidden_tag()}}
      <p>
          Please enter your OpenID:<br>
          {{form.openid(size=80)}}<br>
      </p>
      <p>{{form.remember_me}} Remember Me</p>
      <p><input type="submit" value="Sign In"></p>
  </form>
  {% endblock %}
  
  
  #4.表单接受数据
  
  @app.route('/login', methods = ['GET', 'POST'])
  def login():
      form = LoginForm()
      if form.validate_on_submit():
          flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
          return redirect('/index')
      return render_template('login.html',
          title = 'Sign In',
          form = form)
    
  #5. 表单中处理业务
  
  class ArticleEdit(FlaskForm):
      title    = TextField()
      column   = QuerySetSelectField(get_label='title', allow_blank=True)
      category = QuerySetSelectField(queryset=Category.objects.all())
  ```

  

- 数据库

  ```python
  #1. 安装与配置
  pymysql
  sqlalchemy
  flask-sqlalchemy
  Flask-Migrate
  Flask-Script
  
  SQLALCHEMY_DATABASE_URI=mysql://username:password@server/db
  SQLALCHEMY_ECHO=True
  SQLALCHEMY_RECORD_QUERIES=True
  
  #2. 数据库迁移
  #创建manage.py
  import os
  from flask_script import Manager
  from flask_migrate import Migrate, MigrateCommand
  from app import app, db
  from models import City, Company, Employee
  
  app.config.from_object(os.environ['APP_SETTINGS'])
  
  migrate = Migrate(app, db)
  manager = Manager(app)
  
  manager.add_command('db', MigrateCommand)
  
  
  if __name__ == '__main__':
      manager.run()
      
  #创建models.py
  from app import db
  
  class User(db.Model):
      id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
      email = db.Column(db.String(100), unique=True)
      password = db.Column(db.String(100))
      name = db.Column(db.String(1000))
      
  #执行python3 manage.py
  python3 manage.py db help #获取帮助 
  python3 manage.py db init #初始化 生成一个目录migrations
  python3 manage.py db migrate #提交一次记录
  python3 manage.py db upgrade #更新 生成一个table alembic_version
  python3 manage.py db current #当前版本
  ```

  

- 认证

  ```python
  #1. 认证的几种方式
  HTTP BASIC Authentication user:pass
  COOKIE and Session 
  Token HTTP Header or HTTP body playload
  OAuth 认证
  
  #2 常见方式 COOKIE and Session 
  import hashlib
  md5 = hashlib.md5()
  md5.update(request.form['pass'].encode('utf-8'))
  password = md5.hexdigest()
  
  #3 使用 PassLib
  pip3 install PassLib
  
  from passlib.apps import custom_app_context as pwd_context
  
  class User(db.Model):
      # ...
      def hash_password(self, password):
          self.password_hash = pwd_context.encrypt(password)
  
      def verify_password(self, password):
          return pwd_context.verify(password, self.password_hash)
  ```



##### Git 

- git config

  ```shell
  git config --list
  
  git config user.name
  
  git config --global user.name "maxsu"
  git config --global user.email "yiibai.com@gmail.com"
  
  git config  user.name "maxsu"
  git config user.email "yiibai.com@gmail.com"
  ```

  

- git init

  ```shell
  git init命令创建一个空的Git仓库或重新初始化一个现有仓库。
  ```

  

- git add 

  ```shell
  git add .  # 将所有修改添加到暂存区
  git add *  # Ant风格添加修改
  git add *Controller   # 将以Controller结尾的文件的所有修改添加到暂存区
  
  git add Hello*   # 将所有以Hello开头的文件的修改添加到暂存区 例如:HelloWorld.txt,Hello.java,HelloGit.txt ...
  
  git add Hello?   # 将以Hello开头后面只有一位的文件的修改提交到暂存区 例如:Hello1.txt,HelloA.java 如果是HelloGit.txt或者Hello.java是不会被添加的
  
  #查看中被所有修改过或已删除文件但没有提交的文件，并通过其revert子命令可以查看<path>中所有未跟踪的文件，同时进入一个子命令系统。
   git add -i 
  ```

  

- git commit

  ```
  git commit
  git commit -a
  git commit file_name
  ```

  

- git push

  ```shell
  # 本地的master分支推送到origin主机的master分支。如果master不存在，则会被新建。
  git push origin master
  git push -u origin master
  
  # 默认只推送当前分支
  git push
  
  # 本地分支与远程分支有差异，版本落后于远程分支
  git push --force origin
  
  # 用本地分支lbranch-3覆盖远程分支rbranch-1
  git push -f origin lbranch-2:refs/rbranch-1
  ```

  

- git pull

  ```shell
  # git pull从远程获取最新版本并merge到本地
  git pull origin next
  #与下面命令相同
  git fetch origin next
  git merge origin next
  ```

  

- git clone HTTPS/SSH

  ```shell
  # 克隆到lesson目录
  git clone https://github.com/tonnycao/python_lesson.git lesson
  # 下载到默认 python_lesson 目录
  git clone git@github.com:tonnycao/python_lesson.git
  ```

  

- git remote

  ```
  git remote add origin git_url
  git remote show origin
  git remote -v
  
  ```


- git tag 

  ```shell
  # Git 也可以对某一时间点上的版本打上标签。人们在发布某个软件版本(比如 v1.0 等等)的时候，经常这么做。
  # 列显已有的标签
  git tag
  # 1.4.2 列表 
  git tag -l 'v1.4.2.*'
  # 添加一个tag
  git tag -a v1.4 -m 'my version 1.4'
  # 详情
  git show v1.4
  ```

  

##### 参考

http://www.pythondoc.com/flask-mega-tutorial/index.html

http://wtforms.simplecodes.com/docs/1.0.1/ext.html#id3

https://flask-wtf.readthedocs.io/en/latest/

http://www.pythondoc.com/flask-restful/third.html

https://itsdangerous.palletsprojects.com/en/1.1.x/signer/

https://flask-restful.readthedocs.io/en/latest/

https://owasp.org/www-community/attacks/csrf