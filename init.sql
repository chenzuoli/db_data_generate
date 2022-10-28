CREATE TABLE datagen.`user` (
	id BIGINT auto_increment primary key not NULL,
	name varchar(100) NOT NULL,
	gender BOOL NULL
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;
