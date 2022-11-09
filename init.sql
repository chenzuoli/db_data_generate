use datagen;
CREATE TABLE if not exists `datagen`.`user` (
	id BIGINT auto_increment primary key not NULL comment '主键自增id',
	username varchar(100) NOT NULL comment '用户名',
	email varchar(50) not null comment '邮箱',
	_password_hash varchar(200) not null comment '密码（hash值）'
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

create table if not exists datagen.connections(
    conn_id bigint auto_increment primary key not null comment '主键自增id',
    table_type varchar(50) not null comment '表类型',
    url varchar(100) comment '连接url',
    username varchar(100) comment '用户名',
    _password_hash varchar(200) comment '密码',
    host varchar(50) comment 'ip地址',
    port varchar(10) comment '端口号',
    db varchar(20) comment '数据库',
    param varchar(100) comment '连接参数',
    driver_jar varchar(100) comment 'jar包文件服务器地址'
)ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

