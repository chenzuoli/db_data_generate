# coding=utf-8

from sqlalchemy import Column
from sqlalchemy.orm import registry
from sqlalchemy.types import String, Integer
from werkzeug.security import generate_password_hash, check_password_hash

my_registry = registry()

# 获取模型基类
Base = my_registry.generate_base()


"""
flask admin用
"""
class Connections(Base):
    """
    数据源管理
    """
    __tablename__ = "connections"

    conn_id = Column(Integer, autoincrement=True, primary_key=True, unique=True, nullable=False)
    table_type = Column(String(50), nullable=False)
    url = Column(String(100))
    username = Column(String(100))
    _password_hash = Column(String(200))
    host = Column(String(50))
    port = Column(String(10))
    db = Column(String(20))
    param = Column(String(10))
    driver_jar = Column(String(100))

    def __init__(self, conn_id, table_type, url, username, password, host, port, db, parameter, driver_jar):
        self.conn_id = conn_id
        self.table_type = table_type
        self.url = url
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.db = db
        self.param = parameter
        self.driver_jar = driver_jar

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
        return "conn_id: %s, table_type: %s, url: %s, username: %s, host: %s, port: %s, parameter: %s, driver_jar: %s" \
               % (self.conn_id, self.table_type, self.url, self.username, self.host, self.port,
                  self.param, self.driver_jar)
