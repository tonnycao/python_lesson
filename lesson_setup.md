#### SetUp ####

##### Python #####

* url
```
https://www.python.org/downloads/
https://docs.python.org/zh-cn/3/
```
* cmd
```
brew install python3
```
##### PIP #####

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
  
  #豆瓣：https://pypi.doubanio.com/simple
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
##### Virtual Env #####

* pipenv
```
pip install --user pipenv
cd project_folder
pipenv install requests
main.py
pipenv run python main.py
```

* venv

```
  # create virtual env
  python3 -m venv venv
  virtualenv venv
  
  #激活
  . venv/bin/activate
  #取消激活
  deactivate
```


##### Pycharm #####

* download url
```
https://www.jetbrains.com/pycharm/download/
```
* config

```
https://www.jetbrains.com/pycharm/features/
```


##### jupyter #####

* download

```
https://jupyter.org/install.html
https://jupyter.org/documentation

# pip 安装jupyter 
pip install jupyter
pip install jupyter-1.0.0-py2.py3-none-any.whl 
jupyter notebook
```

##### git & github #####

* git
```
https://git-scm.com/downloads
https://git-scm.com/docs
```
* github
```
https://github.com/
https://gitee.com/
```
