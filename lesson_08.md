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

if __name__ == '__main__':
    app.run()


# mysite_nginx.conf

# the upstream component nginx needs to connect to
upstream flask_app {
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
        uwsgi_pass  flask_app;
        include     /path/to/your/mysite/uwsgi_params; # the uwsgi_params file you installed
    }
}

#uwsgi
uwsgi --http-use-socket 127.0.0.1:3031 --wsgi-file myflaskapp.py --callable app --processes 4 --threads 2 --stats 127.0.0.1:9191 --buffer-size=25530

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
- http://wsgi.tutorial.codepoint.net/application-interface
- https://uwsgi-docs.readthedocs.io/en/latest