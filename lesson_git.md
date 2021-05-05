#### Git

##### 安装
* brew install git &&  brew install git-gui
* apt-get install git && yum install git

##### 常见用法

* git config

  ```shell
  git config --list
  
  git config user.name
  
  git config --global user.name "maxsu"
  git config --global user.email "yiibai.com@gmail.com"
  
  git config  user.name "maxsu"
  git config user.email "yiibai.com@gmail.com"
  ```
  
* git init

  ```shell
  git init命令创建一个空的Git仓库或重新初始化一个现有仓库。
  ```
  
* git add 

  ```shell
  git add .  # 将所有修改添加到暂存区
  git add *  # Ant风格添加修改
  git add *Controller   # 将以Controller结尾的文件的所有修改添加到暂存区
  
  git add Hello*   # 将所有以Hello开头的文件的修改添加到暂存区 例如:HelloWorld.txt,Hello.java,HelloGit.txt ...
  
  git add Hello?   # 将以Hello开头后面只有一位的文件的修改提交到暂存区 例如:Hello1.txt,HelloA.java 如果是HelloGit.txt或者Hello.java是不会被添加的
  
  #查看中被所有修改过或已删除文件但没有提交的文件，并通过其revert子命令可以查看<path>中所有未跟踪的文件，同时进入一个子命令系统。
   git add -i 
  ```
  
* git commit

  ```
  git commit
  git commit -a
  git commit file_name
  ```
  
* git push

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
  
* git pull
  
  ```shell
  # git pull从远程获取最新版本并merge到本地
  git pull origin next
  #与下面命令相同
  git fetch origin next
  git merge origin next
  ```
  
* git clone
  ```shell
  # 克隆到lesson目录
  git clone https://github.com/tonnycao/python_lesson.git lesson
  # 下载到默认 python_lesson 目录
  git clone git@github.com:tonnycao/python_lesson.git
  # 下载特定的分支或者tag
  git clone -b branch_name git@github.com:tonnycao/python_lesson.git
  git checkout branch_name git@github.com:tonnycao/python_lesson.git
  ```
* git remote
  ```
  git remote add origin git_url
  git remote show origin
  git remote -v
  
  ```
  
* git tag 

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

* https://git-scm.com/doc
* https://git-scm.com/downloads

