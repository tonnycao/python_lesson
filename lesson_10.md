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

  

