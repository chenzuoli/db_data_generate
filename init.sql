CREATE TABLE `datagen`.`user` (
	id BIGINT auto_increment primary key not NULL,
	username varchar(100) NOT NULL,
	email varchar(50) not null,
	_password_hash varchar(200) not null
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;
