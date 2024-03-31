# coding=utf-8

from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from models.connections import Connections
from urls import session
from faker import Faker
fk = Faker(locale='zh_CN')

mysql_url = "mysql+pymysql://localhost:3306/datagen"

Base = declarative_base()

# 初始化数据库连接
engine = create_engine(mysql_url)

# 创建session
Session = sessionmaker(engine)


def read_metadata(conn_id, table):
    # 查询datagen数据库，获取连接串
    conn: Connections = session.query(Connections).filter(Connections.conn_id == conn_id).first()

    # 拼接mysql数据源url
    mysql_url = "mysql+pymysql://%s:%s/%s" % (conn.host, conn.port, conn.db)


def data_gen(url: str, database: str, table: str):
    # 获取目标表的表结构，和对应字段的类型，根据类型，生成随机的数据
    engine = create_engine(url)
    insp = inspect(engine)
    dbs = insp.get_schema_names()
    tbls = insp.get_table_names(schema=database)
    cols= insp.get_columns(table, schema=database)
    for name, tp in cols:
        if tp == int:
            v = fk.random_int()
        elif tp == str:
            v = fk.word()
        elif tp == float:
            v = fk.random_float()



def insert():
    pass
