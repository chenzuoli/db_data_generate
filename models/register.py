from wtforms import StringField, PasswordField, SubmitField, BooleanField, validators

from flask_wtf import FlaskForm
from wtforms.validators import DataRequired


# 设置表单

class RegisterForm(FlaskForm):
    # username
    username = StringField('Username', [DataRequired("请输入用户名"),
                                        validators.Length(min=4, max=25)])
    email = StringField('Email Address', [
        DataRequired("请输入邮箱"),
        validators.Length(min=6, max=35),
        validators.Email()])
    password = PasswordField('New Password', [
        validators.DataRequired("请输入密码"),
        validators.EqualTo('confirm', message='两次密码必须一致')
    ])
    confirm = PasswordField('Repeat Password', [validators.DataRequired("请确认密码")])
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired("请同意")])
    # submit
    submit = SubmitField("提交")
