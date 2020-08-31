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

  

##### 参考

http://www.pythondoc.com/flask-mega-tutorial/index.html

http://wtforms.simplecodes.com/docs/1.0.1/ext.html#id3

https://flask-wtf.readthedocs.io/en/latest/

http://www.pythondoc.com/flask-restful/third.html

https://itsdangerous.palletsprojects.com/en/1.1.x/signer/

https://flask-restful.readthedocs.io/en/latest/

https://owasp.org/www-community/attacks/csrf