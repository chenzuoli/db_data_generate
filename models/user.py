# coding=utf-8

from sqlalchemy.orm import registry
from sqlalchemy.types import String, Integer, Boolean
from sqlalchemy import Column

my_registry = registry()

# 获取模型基类
Base = my_registry.generate_base()


class User(Base):
    """
    用户表
    """
    __tablename__ = "user"
    id = Column(Integer, autoincrement=True, primary_key=True, unique=True, nullable=False)
    name = Column(String, nullable=False)
    gender = Column(Boolean)
