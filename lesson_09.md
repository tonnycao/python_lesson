##### Flask 入门

###### 架构
- 单模块 Single Module

  ```
  app.py #所有业务逻辑
  config.py #配置
  requirements.txt #依赖文件
  static/ #css js image
  templates/ #模版
  ```

  

- 包 Package

  ```
  config.py #配置
  requirements.txt #依赖文件
  run.py #入口文件
  instance/
      config.py # 实例配置文件 与版本无关
  yourapp/
      __init__.py 
      views.py # 路由
      models.py # 数据库 模型
      forms.py # 表单
      static/ # css js image
      templates/# 模版 
  ```

  

- 蓝图 Blueprints

  ```
  run.py
  config.py
  app           
     __init__.py
     mod_auth   # Our first module, mod_auth
         __init__.py
         views.py
         models.py
         forms.py
         templates
            404.html
            auth
            signin.html
         static
  ```

  

###### 配置

* export

  ```
  # export linux 环境获取环境变量命令 
  export FLASK_APP=hello.py
  
  ```

  

* Python File

  ```
  # key=>value 方式
  # config.py
  DEBUG = True # Turns on debugging features in Flask
  BCRYPT_LOG_ROUNDS = 12 # Configuration for the Flask-Bcrypt extension
  MAIL_FROM_EMAIL = "robert@example.com" # For use in application emails
  
  #app.py
  from flask import Flask
  
  app = Flask(__name__)
  app.config.from_object('config')
  
  # 如果有instance 目录配置
  # instance/config.py
  
  SECRET_KEY = 'Sm9obiBTY2hyb20ga2lja3MgYXNz'
  STRIPE_API_KEY = 'SmFjb2IgS2FwbGFuLU1vc3MgaXMgYSBoZXJv'
  SQLALCHEMY_DATABASE_URI= \
  "postgresql://user:TWljaGHFgiBCYXJ0b3N6a2lld2ljeiEh@localhost/databasename"
  
  #app.py or __init__.py
  app = Flask(__name__, instance_relative_config=True)
  app.config.from_object('config')
  app.config.from_pyfile('config.py')
  ```

  

* Python Pakage

  ```
  # config 目录
  requirements.txt
  run.py
  config/
    __init__.py 
    default.py #默认
    production.py # 生产环境
    development.py #开发环境
    staging.py # 演示环境
  instance/
    config.py
  yourapp/
    __init__.py
    models.py
    views.py
    static/
    templates
    
    
  # yourapp/__init__.py
  
  app = Flask(__name__, instance_relative_config=True)
  
  # Load the default configuration
  app.config.from_object('config.default')
  
  # Load the configuration from the instance folder
  app.config.from_pyfile('config.py')
  
  # Load the file specified by the APP_CONFIG_FILE environment variable
  # Variables defined here will override those in the default configuration
  app.config.from_envvar('APP_CONFIG_FILE')
  
  # start.sh
  
  export APP_CONFIG_FILE=/var/www/yourapp/config/production.py
  python run.py
  ```

  

###### 路由

- 装饰器

  ````
  @app.route('/')
  def index():
      return 'Index Page'
  
  @app.route('/login', methods=['GET', 'POST'])
  def login():
      if request.method == 'POST':
          return do_the_login()
      else:
          return show_the_login_form()
  
   
  @app.route('/user/<username>')
  def show_user_profile(username):
      # show the user profile for that user
      return 'User %s' % escape(username)
  
  @app.route('/post/<int:post_id>')
  def show_post(post_id):
      # show the post with the given id, the id is an integer
      return 'Post %d' % post_id
  
  @app.route('/path/<path:subpath>')
  def show_subpath(subpath):
      # show the subpath after /path/
      return 'Subpath %s' % escape(subpath)
   
  
  # string(default) accepts any text without a slash
  # int accepts positive integers
  # float accepts positive floating point values
  # path like string but also accepts slashes
  # uuid accepts UUID strings
  ````

  

- 跳转

  ```
  url_for 
  url_for('login', next='/') # /login?next=/
  url_for('profile', username='John Doe') #/user/John%20Doe
  url_for('static', filename='style.css')
  
  redirect(url_for('login'))
  ```

  

###### 模版

- Jinja2

  ```
  http://docs.jinkan.org/docs/jinja2/templates.html
  ```

  

###### 数据库

* Flask-SQLAlchemy

```
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:rootroot@127.0.0.1:3306/db_example?charset=utf8mb4'
db = SQLAlchemy(app)


```

