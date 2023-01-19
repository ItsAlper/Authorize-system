CREATE TABLE user_types(
user_type_id INT PRIMARY KEY,
user_type_name VARCHAR(255)
);

CREATE TABLE users(
user_id INT PRIMARY KEY,
username VARCHAR(255),
password VARCHAR(255),
user_type_id INT,
FOREIGN KEY (user_type_id) REFERENCES user_types(user_type_id)
);

INSERT INTO user_types (user_type_id, user_type_name)
VALUES (1, 'silver'), (2, 'gold'), (3, 'platinum');

INSERT INTO users (user_id, username, password, user_type_id)
VALUES (1, 'johndoe', 'password123', 1), (2, 'janedoe', 'password456', 2);