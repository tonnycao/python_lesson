# -*- coding: utf-8 -*-
# @Time : 2020/9/5 1:10 下午
# @Author : tonnycao
# @Email : jian860129@126.com
# @File : run.py.py
# @Project : flask_three

from flasker import create_app

app = create_app()

app.run(host='0.0.0.0', port=9090, debug=True)