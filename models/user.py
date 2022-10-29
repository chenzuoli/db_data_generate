# coding=utf-8

from sqlalchemy.orm import registry
from sqlalchemy.types import String, Integer
from sqlalchemy import Column
from werkzeug.security import generate_password_hash, check_password_hash

my_registry = registry()

# 获取模型基类
Base = my_registry.generate_base()


class User(Base):
    """
    用户表
    """
    __tablename__ = "user"

    id = Column(Integer, autoincrement=True, primary_key=True, unique=True, nullable=False)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    _password_hash = Column(String, nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    @property
    def password(self):
        raise Exception('密码不能被读取')  # 为了保持使用习惯，还是设置一个password字段用来设置密码，当然也不能被读取。

    # 赋值password，自动加密存储
    @password.setter
    def password(self, value):
        self._password_hash = generate_password_hash(value)

    # 使用check_password进行密码校验，相同返回true，否则返回false
    def check_password(self, password):
        return check_password_hash(self._password_hash, password)

    def __repr__(self):
        return "username: %s, email: %s" % (self.username, self.email)
