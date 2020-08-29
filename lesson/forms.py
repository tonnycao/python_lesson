# -*- coding: utf-8 -*-
# @Time : 2020/8/29 3:58 下午
# @Author : tonnycao
# @Email : jian860129@126.com
# @File : forms.py
# @Project : flasker


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email


class UserNamePasswordForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])