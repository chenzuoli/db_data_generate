# 项目概述

此项目旨在开发测试过程中，往数据库中造数据，方便开发和调试。目前仅供学习使用。
进度：

| 数据库类型      | 支持与否 |
|------------|------|
| Mysql      | 开发中  |
| Pg         | 开发中  |
| Oracle     | 开发中  |
| Mongodb    | 开发中  |
| Sqlite     | 开发中  |
| SqlServer  | 开发中  |
| Hive       | 开发中  |
| Hbase      | 开发中  |
| ES         | 开发中  |
| Druid      | 开发中  |
| ClickHouse | 开发中  |
| StarRocks  | 开发中  |
| TiDB       | 开发中  |
| Impala     | 开发中  |
| Presto     | 开发中  |
| Kylin      | 开发中  |
| GreenPlum  | 开发中  |

# 技术
Flask + Bootstrap

# 内容模块

## 主页

## 数据源

这里配置数据源信息，列一下需要存储的那些信息

| id  | 数据源类型 | 连接url                                  | 用户名  | 密码     | 参数                     | 驱动jar（上传） |
|-----|-------|----------------------------------------|------|--------|------------------------|-----------|
| 1   | mysql | mysql+pymysql://localhost:3306/datagen | root | xxxxxx | characterEncoding=utf8 ||   

为了优化用户体验，可平台自动去下载对应数据库驱动到平台，可后期迭代上线。

后面的数据查询、数据生成功能，将使用此数据源配置表。

这里使用`flask-wtf`扩展包的表单功能

## 数据查询

这里可以编写sql查询数据

## 数据生成

选择不同的数据库类型，生成不同的sql语句，或插入到不同的数据库中

# 快速开始
```commandline
python main.py
```


# 一起开发
微信我：PAIN_7771