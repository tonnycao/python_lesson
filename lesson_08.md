##### Flask

###### 依赖

- 版本Python 3 以上
- Flask版本 1.1.1 

- Werkzeug  0.16.0 python web service gateway interface 
- Jinja2 模板语言
- MarkupSafe与 Jinja 共用，在渲染页面时用于避免不可信的输入，防止注入攻击。
- ItsDangerous 保证数据完整性的安全标志数据，用于保护 Flask 的 session cookie.
- Click 是一个命令行应用的框架。用于提供 `flask` 命令，并允许添加自定义 管理命令。
- 单线程，阻塞执行，部署续作WSGI容器，例如Gunicorn 或 uWSGI。

###### 环境

- pip3 说明

  ```
  #pip 是一个 Python 包安装与管理工具 pip3 for python3
  
  #install
  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
  sudo python3 get-pip.py
  
  # 查看版本
  pip3 --version
  
  #从PyPI安装软件包
  pip3 install SomePackage
  
  #特定版本的包
  pip3 install Flask==1.1.2
  
  #安装已经从PyPI下载或从其他地方获得的软件包
  pip3 install SomePackage-1.0-py2.py3-none-any.whl
  
  #显示安装了哪些文件
  pip3 show --files SomePackage
  
  #列出哪些软件包已过期
  pip3 list --outdate
  
  #卸载
  pip3 uninstall package
  
  #使用某个数据源安装某个包
  pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
  
  #配置新的数据源
  pip3 install pip -U
  pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
  
  #豆瓣：https://pypi.doubanio.com/simple/
  #清华：https://pypi.tuna.tsinghua.edu.cn/simple
  
  #搜索包
  pip3 search SomePackage
  
  #显示安装包信息
  pip3 show 
  
  # 查看指定包的详细信息
  pip3 show -f SomePackage
  
  # 列出已安装的包
  pip3 list
  
  # 查看可升级的包
  pip3 list -o
  ```

  

- 安装虚拟环境管理依赖包 pip3 install virtualenv

- 激活与使用

  ```
  # create virtual env
  python3 -m venv venv
  virtualenv venv
  
  #激活
  . venv/bin/activate
  #取消激活
  deactivate
  ```

- 安装Flask

  ```
  pip3 install flask
  pip3 install Werkzeug
  ```

  

- 制作依赖文件

  ```
  pip3 freeze > requirements.txt
  
  ```

  

###### 最小的项目

###### 部署

参考

- https://exploreflask.com/en/latest/preface.html
- https://dormousehole.readthedocs.io/en/latest
- https://docs.python.org/zh-cn/3/howto/functional.html
- https://github.com/pxzhang/awesome-flask
- http://wsgi.tutorial.codepoint.net/application-interface
- https://uwsgi-docs.readthedocs.io/en/latest