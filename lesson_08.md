##### Flask

###### 依赖

- 版本Python 3。
- Flask版本 1.1.1。 

- Werkzeug  0.16.0 python web service gateway interface 。
- Jinja2 模板语言，渲染页面。
- MarkupSafe与 Jinja 共用，在渲染页面时用于避免不可信的输入，防止注入攻击。
- ItsDangerous 保证数据完整性的安全标志数据，用于保护 Flask 的 session cookie。
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
  #
  export PYTHONDONTWRITEBYTECODE=1
  export PYTHONPYCACHEPREFIX=/tmp
  #python解释器的工作顺序：
  #1 完成模块的加载和链接；
  #2 将源代码编译为PyCodeObject对象(即字节码)，写入内存中，供CPU读取；
  #3 从内存中读取并执行，结束后将PyCodeObject写回硬盘当中，也就是复制到.pyc或.pyo文件中，以保存当前目录下所有脚本的字节码文件；
  #4 之后若再次执行该脚本，它先检查【本地是否有上述字节码文件】和【该字节码文件的修改时间是否与其脚本一致】。是就直接执行，否则重复#上述步骤。
  #不产生 __pycache__ 目录
  python3 -B foo.py
  ```

  

###### 最小的项目

```
#1.the web client <-> the socket <-> uWSGI <-> Python

#foobar.py
def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"]

#uwsgi
uwsgi --http :9090 --wsgi-file foobar.py
uwsgi --http :9090 --wsgi-file foobar.py --master --processes 4 --threads 2 --stats 127.0.0.1:9191

#2. the web client <-> the web server <-> the socket <-> uWSGI <-> Python

# myflaskapp.py
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return "<span style='color:red'>I am app 1</span>"
    
# mysite_nginx.conf

# the upstream component nginx needs to connect to
upstream flask {
    # server unix:///path/to/your/mysite/mysite.sock; # for a file socket
    server 127.0.0.1:8001; # for a web port socket (we'll use this first)
}

# configuration of the server
server {
    # the port your site will be served on
    listen      8000;
    # the domain name it will serve for
    server_name example.com; # substitute your machine's IP address or FQDN
    charset     utf-8;

    # max upload size
    client_max_body_size 75M;   # adjust to taste

    # flask media
    location /media  {
        alias /path/to/your/mysite/media;  # your flask project's media files - amend as required
    }

    location /static {
        alias /path/to/your/mysite/static; # your flask project's static files - amend as required
    }

    # Finally, send all non-media requests to the Django server.
    location / {
        uwsgi_pass  django;
        include     /path/to/your/mysite/uwsgi_params; # the uwsgi_params file you installed
    }
}

#uwsgi
uwsgi --http-socket :3031 --wsgi-file myflaskapp.py --callable app --processes 4 --threads 2 --stats 127.0.0.1:9191 --buffer-size=25530

#yourfile.ini
[uwsgi]
socket = 127.0.0.1:3031
chdir = /home/foobar/myproject/
wsgi-file = myproject/wsgi.py
processes = 4
threads = 2
stats = 127.0.0.1:9191

#uwsgi yourfile.ini
```



###### 部署

参考

- https://exploreflask.com/en/latest/preface.html
- https://dormousehole.readthedocs.io/en/latest
- https://docs.python.org/zh-cn/3/howto/functional.html
- https://github.com/pxzhang/awesome-flask
- http://wsgi.tutorial.codepoint.net/application-interface
- https://uwsgi-docs.readthedocs.io/en/latest