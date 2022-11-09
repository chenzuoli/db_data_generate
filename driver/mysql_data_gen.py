# coding=utf-8

import os
import sys
import pymysql
import sqlalchemy
from urls import session
from models.connections import Connections


def read_metadata(conn_id, table):
    # 查询datagen数据库，获取连接串
    conn: Connections = session.query(Connections).filter(Connections.conn_id == conn_id).first()

    # 拼接mysql数据源url
    mysql_url = "mysql+pymysql://%s:%s/%s" % (conn.host, conn.port, conn.db)


def fake_data():
    pass


def insert():
    pass
